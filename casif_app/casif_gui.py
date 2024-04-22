import os
import sys
import re
import SimpleITK as sitk
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg
import numpy as np


from casif_app.ui.main_window import Ui_win_main_window

import casif_app.casif_io as io
import casif_app.casif_features as features
import casif_app.casif_data_storage as data_storage


class MainWindow(qtw.QMainWindow, Ui_win_main_window):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # menu actions func connections
        self.mac_exit.triggered.connect(sys.exit)

        # menu action read intraop ct connection
        self.mac_read_intra_ct.triggered.connect(self.read_ct_triggered)

        # menu action read/write drr connections
        self.mac_read_intraop_drr.triggered.connect(self.read_drr_triggered)
        self.mac_read_preop_drr.triggered.connect(self.read_drr_triggered)
        self.mac_write_preop_drr.triggered.connect(self.write_drr_triggered)
        self.mac_write_intraop_drr.triggered.connect(self.write_drr_triggered)
        self.mac_write_registered_drr.triggered.connect(self.write_drr_triggered)

        # button actions func connections
        self.rbu_intraop_drr.setChecked(True)
        self.rbu_preop_drr.toggled.connect(self.input_settings_state_change)
        self.rbu_intraop_drr.toggled.connect(self.input_settings_state_change)
        self.pbu_drr_start.clicked.connect(self.generate_drr_clicked)
        self.pbu_reg_start.clicked.connect(self.start_registration)

        # display first toolbox page
        self.tab_main.setCurrentIndex(0)

        # create graphics scene
        self.gsc_drr = qtw.QGraphicsScene()
        self.gvi_drr.setScene(self.gsc_drr)

        self.cbo_visualization.currentIndexChanged.connect(self.display_image_at_index)

        # update shrink factors and sigmas
        self.led_multires_levels.textChanged.connect(self.update_multires_factors)
        self.led_lower_edge_thresh.textChanged.connect(self.update_edge_labels)
        self.led_upper_edge_thresh.textChanged.connect(self.update_edge_labels)

        self.mac_info.triggered.connect(self.print_images)

    @qtc.Slot()
    def read_ct_triggered(self) -> None:
        dir_path = qtw.QFileDialog.getExistingDirectory(self, caption="Otevřít DICOM CT",
                                                        dir=os.getcwd())

        if dir_path:
            ct_volume = io.read_dicom_files(dir_path=dir_path)
            ct_metadata = io.read_metadata(volume=ct_volume)

            intraop_ct_data.ct_volume = ct_volume
            intraop_ct_data.ct_meta = ct_metadata
            intraop_ct_data.exist_state = True
            self.labm_intraop_ct_name.setText(intraop_ct_data.ct_meta["patient_name"])
            if self.labm_data_warning.text != default_ct_text:
                self.labm_data_warning.setText(default_ct_text)
                self.labm_data_warning.setStyleSheet("")

    @qtc.Slot()
    def read_drr_triggered(self) -> None:
        file_path = qtw.QFileDialog.getOpenFileName(self, caption="Načíst DRR obraz",
                                                    dir=os.getcwd())
        if file_path[0]:
            drr_image = io.read_drr(file_path[0])
            file_name = re.split("[/.]", file_path[0])[-2]
            if self.sender().objectName() == "mac_read_intraop_drr":
                intraop_drr_data.drr_image = drr_image
                intraop_drr_data.exist_state = True
                self.display_image(drr_image)
                self.cbo_visualization.setCurrentIndex(0)

                self.labm_fixed_drr.setText(file_name)

            elif self.sender().objectName() == "mac_read_preop_drr":
                preop_drr_data.drr_image = drr_image
                preop_drr_data.exist_state = True
                self.display_image(drr_image)
                self.cbo_visualization.setCurrentIndex(1)

                self.labm_moving_drr.setText(file_name)

    @qtc.Slot()
    def write_drr_triggered(self) -> None:
        file_path = qtw.QFileDialog.getSaveFileName(self, caption="Uložit předoperační DRR obraz",
                                                    dir=os.getcwd(),
                                                    filter="MHA (*.mha)")
        if file_path[0]:
            drr_image = None
            if self.sender().objectName() == "mac_write_preop_drr" and preop_drr_data.exist_state:
                drr_image = preop_drr_data.drr_image
            elif self.sender().objectName() == "mac_write_intraop_drr" and intraop_drr_data.exist_state:
                drr_image = intraop_drr_data.drr_image
            elif self.sender().objectName() == "mac_write_registered_drr" and registration_data.exist_state:
                drr_image = registration_data.registered_image

            io.write_drr(drr_image, file_path[0])

    @qtc.Slot()
    def generate_drr_clicked(self):
        drr_size = (int(self.led_drr_width.text()),
                    int(self.led_drr_height.text()))
        drr_threshold = float(self.led_drr_thresh.text())
        drr_sid = float(self.led_sid.text())
        drr_settings = {"src_img_dist": drr_sid,
                        "output_drr_size": drr_size, "threshold": drr_threshold}

        if self.rbu_intraop_drr.isChecked():  # generate intraop drr

            # do nothing if ct doesn't exist
            if not self.check_intraop_ct_exists():
                return None

            output_drr_image = features.generate_intraop_drr(intraop_ct_data.ct_volume,
                                                             drr_settings)

            intraop_drr_data.drr_image = output_drr_image
            intraop_drr_data.exist_state = True
            self.cbo_visualization.setCurrentIndex(0)

            self.labm_fixed_drr.setText(self.labm_intraop_ct_name.text())

        elif self.rbu_preop_drr.isChecked():  # generate preop drr
            #TODO: add gvirtualxray drr image generation
            pelvis_mesh_file_path = qtw.QFileDialog.getOpenFileName(self, caption="Otevřít STL pánve",
                                                                    dir=os.getcwd(),
                                                                    filter="STL (*.stl)")
            guide_mesh_file_path = qtw.QFileDialog.getOpenFileName(self, caption="Otevřít STL vodícího drátu",
                                                                   dir=os.getcwd(),
                                                                   filter="STL (*.stl)")

            output_drr_image = features.generate_preop_drr(pelvis_mesh_file_path[0],
                                                           guide_mesh_file_path[0],
                                                           drr_settings)
            preop_drr_data.drr_image = output_drr_image
            preop_drr_data.exist_state = True
            preop_drr_name = re.split("[/.]", pelvis_mesh_file_path[0])[-2]
            self.labm_preop_name.setText(preop_drr_name)
            self.cbo_visualization.setCurrentIndex(1)

            self.labm_moving_drr.setText(preop_drr_name)

        self.display_image(output_drr_image)

    def start_registration(self):
        shrink_factors = []
        smoothing_sigmas = []
        if len(self.led_shrink_factors.text()) > 0:
            shrink_factors = list(map(int, self.led_shrink_factors.text().split(";")))

        if len(self.led_sigma_factors.text()) > 0:
            smoothing_sigmas = list(map(float, self.led_sigma_factors.text().split(";")))

        registration_settings = {"method": self.cbo_optim_method.currentIndex(),
                                 "shrink_factors": shrink_factors,
                                 "smoothing_sigmas": smoothing_sigmas}

        registered_image = features.register_images(fixed_image=intraop_drr_data.drr_image,
                                                    moving_image=preop_drr_data.drr_image,
                                                    reg_settings=registration_settings,
                                                    progress_window=self.tbr_output_messages)
        registration_data.registered_image = registered_image
        registration_data.exist_state = True

        alpha_blended_image = features.get_alpha_blend(intraop_drr_data.drr_image,
                                                       registration_data.registered_image)
        registration_data.alpha_blended_image = alpha_blended_image
        self.display_image(alpha_blended_image)
        self.cbo_visualization.setCurrentIndex(3)

    def display_image(self, input_image):
        image_rescaled = features.cast_image(input_image, image_type=sitk.sitkUInt8)
        image_array = sitk.GetArrayViewFromImage(image_rescaled)
        data = image_array.data

        height, width = image_array.shape
        bytes_per_line = image_array.strides[0]  # bytes per line for QImage
        image_pixmap = qtg.QPixmap(qtg.QImage(data, width, height, bytes_per_line,
                                              qtg.QImage.Format.Format_Grayscale8))
        self.gvi_drr.setSceneRect(0, 0, width, height)
        self.gsc_drr.addPixmap(image_pixmap)
        self.gvi_drr.fitInView(0, 0, width, height, qtc.Qt.AspectRatioMode.KeepAspectRatioByExpanding)
        self.gsc_drr.update()

    def display_labeled_image(self, labeled_image):
        fixed_rescaled_image = features.cast_image(intraop_drr_data.drr_image, image_type=sitk.sitkUInt8)
        fixed_image_array = sitk.GetArrayFromImage(fixed_rescaled_image)
        label_array = sitk.GetArrayFromImage(labeled_image)
        height, width, channels = label_array.shape
        #FIXME: try embedding matplotlib instead as custom widget in QtDesigner
        data = label_array.data
        bytes_per_line = channels * width
        image_pixmap = qtg.QPixmap(qtg.QImage(data, width, height, bytes_per_line,
                                              qtg.QImage.Format.Format))
        self.gvi_drr.setSceneRect(0, 0, width, height)
        self.gsc_drr.addPixmap(image_pixmap)
        self.gvi_drr.fitInView(0, 0, width, height, qtc.Qt.AspectRatioMode.KeepAspectRatioByExpanding)
        self.gsc_drr.update()

    def resizeEvent(self, event: qtg.QResizeEvent) -> None:
        super().resizeEvent(event)

        # drr_width, drr_height = drr_data.drr_image.GetSize()[:2]
        # self.gvi_drr.fitInView(0, 0, drr_width, drr_height, qtc.Qt.AspectRatioMode.KeepAspectRatioByExpanding)

    def closeEvent(self, event: qtg.QCloseEvent) -> None:
        super().closeEvent(event)

        sys.exit()

    def input_settings_state_change(self):
        if self.rbu_intraop_drr.isChecked():
            self.led_drr_thresh.setEnabled(True)
        else:
            self.led_drr_thresh.setEnabled(False)
            self.led_drr_thresh.setText("0")

    def display_image_at_index(self):
        if self.cbo_visualization.currentIndex() == 0:  # display preop drr image
            self.display_image(intraop_drr_data.drr_image)
        elif self.cbo_visualization.currentIndex() == 1:  # display intraop drr image
            self.display_image(preop_drr_data.drr_image)
        elif self.cbo_visualization.currentIndex() == 2 and registration_data.exist_state:
            lower_thresh = float(self.led_lower_edge_thresh.text())
            upper_thresh = float(self.led_upper_edge_thresh.text())

            labeled_image = features.get_labeled_edges(intraop_drr_data.drr_image, preop_drr_data.drr_image,
                                                       guide_low_thresh=lower_thresh, guide_up_thresh=upper_thresh,
                                                       colors=[edge_red_color, edge_yellow_color])
            registration_data.labeled_image = labeled_image
            self.display_labeled_image(labeled_image)

        elif self.cbo_visualization.currentIndex() == 3:
            self.display_image(registration_data.alpha_blended_image)

    def check_intraop_ct_exists(self):
        if not intraop_ct_data.exist_state:
            self.labm_data_warning.setText(warning_ct_text)
            self.labm_data_warning.setStyleSheet(warning_stylesheet)
            return False
        else:
            return True

    def update_multires_factors(self):
        if len(self.led_multires_levels.text()) > 0:
            shrink_factors, smooth_sigmas = features.get_multires_params(int(self.led_multires_levels.text()))
            shrinks = "; ".join(map(str, shrink_factors))
            smooth = "; ".join(map(str, smooth_sigmas))

            self.led_shrink_factors.setText(shrinks)
            self.led_sigma_factors.setText(smooth)
        else:
            self.led_shrink_factors.setText("")
            self.led_sigma_factors.setText("")

    def update_edge_labels(self):
        if not registration_data.exist_state:
            return None

        if len(self.led_lower_edge_thresh.text()) > 1 or len(self.led_upper_edge_thresh.text()) > 1:
            lower_thresh = float(self.led_lower_edge_thresh.text())
            upper_thresh = float(self.led_upper_edge_thresh.text())

            labeled_image = features.get_labeled_edges(intraop_drr_data.drr_image, preop_drr_data.drr_image,
                                                       guide_low_thresh=lower_thresh, guide_up_thresh=upper_thresh,
                                                       colors=[edge_red_color, edge_yellow_color])
            registration_data.labeled_image = labeled_image
            self.display_labeled_image(labeled_image)

    def print_images(self):
        print(intraop_drr_data.drr_image.GetSize())
        print(preop_drr_data.drr_image.GetSize())
        print(registration_data.registered_image.GetSize())


preop_drr_data = data_storage.PreOpDrrData()
intraop_ct_data = data_storage.IntraOpCtData()
intraop_drr_data = data_storage.IntraOpDrrData()
registration_data = data_storage.RegistrationData()
warning_stylesheet = "font-weight: bold; color: red"
warning_ct_text = "CHYBÍ CT DATA"
default_ct_text = "---"
edge_yellow_color = np.array([255, 255, 0], dtype=np.uint8)
edge_red_color = np.array([255, 0, 0], dtype=np.uint8)
