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

        self.fig_counter = 0
        self.intraop_drr_counter = 0
        self.preop_drr_counter = 0
        self.labeled_image_counter = 0
        self.window_counter = 0
        self.window_dict = {}

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
        self.mac_info.triggered.connect(self.print_images)

        # button actions func connections
        self.rbu_intraop_drr.setChecked(True)
        self.rbu_preop_drr.toggled.connect(self.input_settings_state_change)
        self.rbu_intraop_drr.toggled.connect(self.input_settings_state_change)
        self.pbu_drr_start.clicked.connect(self.generate_drr_clicked)
        self.pbu_reg_start.clicked.connect(self.start_registration)

        # signal to change multires factors on level change
        self.led_multires_levels.textChanged.connect(self.update_multires_factors)

        # display first toolbox page
        self.tab_main.setCurrentIndex(0)
        self.twi_data_list.itemDoubleClicked.connect(self.display_double_clicked_item)

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

            self.add_tree_child(0, ct_metadata["patient_name"])

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
                intraop_drr_data.all_images[f"drr_{self.intraop_drr_counter}"] = drr_image
                self.intraop_drr_counter += 1

                self.add_tree_child(1, file_name)
                self.add_intraop_item(file_name)

            elif self.sender().objectName() == "mac_read_preop_drr":
                preop_drr_data.drr_image = drr_image
                preop_drr_data.exist_state = True
                preop_drr_data.all_images[f"drr_{self.preop_drr_counter}"] = drr_image
                self.preop_drr_counter += 1

                self.add_tree_child(2, file_name)
                self.add_preop_item(file_name)

            drr_array = sitk.GetArrayFromImage(drr_image)
            self.display_image(drr_image, file_name)

    def add_intraop_item(self, image_name):
        if self.intraop_drr_counter == 1:
            self.cbo_intraop_input.setItemText(0, image_name)
        else:
            self.cbo_intraop_input.addItem(image_name)
            self.cbo_intraop_input.setCurrentIndex(self.intraop_drr_counter - 1)

    def add_preop_item(self, image_name):
        if self.preop_drr_counter == 1:
            self.cbo_preop_input.setItemText(0, image_name)
        else:
            self.cbo_preop_input.addItem(image_name)
            self.cbo_preop_input.setCurrentIndex(self.preop_drr_counter - 1)

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

            if not intraop_ct_data.exist_state:
                self.tbr_output_messages.insertPlainText("CHYBÍ CT DATA \n")
                return None

            output_drr_image = features.generate_intraop_drr(intraop_ct_data.ct_volume,
                                                             drr_settings)
            intraop_drr_data.drr_image = output_drr_image
            intraop_drr_data.exist_state = True
            intraop_drr_data.all_images[f"drr_{self.intraop_drr_counter}"] = output_drr_image

            self.intraop_drr_counter += 1
            self.add_intraop_item(intraop_ct_data.ct_meta["patient_name"])
            self.add_tree_child(1, intraop_ct_data.ct_meta["patient_name"])

            output_image_array = sitk.GetArrayFromImage(output_drr_image)
            self.display_image(output_drr_image, intraop_ct_data.ct_meta["patient_name"])

        elif self.rbu_preop_drr.isChecked():  # generate preop drr
            pelvis_mesh_file_path = qtw.QFileDialog.getOpenFileName(self, caption="Otevřít STL pánve",
                                                                    dir=os.getcwd(),
                                                                    filter="STL (*.stl)")
            guide_mesh_file_path = qtw.QFileDialog.getOpenFileName(self, caption="Otevřít STL vodícího drátu",
                                                                   dir=os.getcwd(),
                                                                   filter="STL (*.stl)")

            if pelvis_mesh_file_path and guide_mesh_file_path:
                output_drr_image = features.generate_preop_drr(pelvis_mesh_file_path[0],
                                                               guide_mesh_file_path[0],
                                                               drr_settings)
                preop_drr_data.drr_image = output_drr_image
                preop_drr_data.exist_state = True
                preop_drr_name = re.split("[/.]", pelvis_mesh_file_path[0])[-2]
                preop_drr_data.all_images[f"drr_{self.preop_drr_counter}"] = output_drr_image

                self.preop_drr_counter += 1
                self.add_preop_item(preop_drr_name)
                self.add_tree_child(2, preop_drr_name)

                output_image_array = sitk.GetArrayFromImage(output_drr_image)
                self.display_image(output_drr_image, preop_drr_name)

    def start_registration(self):
        if self.cbo_intraop_input.currentText() == "---" and self.cbo_preop_input.currentText() == "---":
            self.tbr_output_messages.insertPlainText("CHYBÍ INTRAOPERAČNÍ A PŘEDOPERAČNÍ DRR OBRAZY\n")
            return None
        elif self.cbo_intraop_input.currentText() == "---":
            self.tbr_output_messages.insertPlainText("CHYBÍ INTRAOPERAČNÍ DRR OBRAZ\n")
            return None
        elif self.cbo_preop_input.currentText() == "---":
            self.tbr_output_messages.insertPlainText("CHYBÍ PŘEDOPERAČNÍ DRR OBRAZ\n")
            return None

        shrink_factors = []
        smoothing_sigmas = []
        if len(self.led_shrink_factors.text()) > 0:
            shrink_factors = list(map(int, self.led_shrink_factors.text().split(";")))

        if len(self.led_sigma_factors.text()) > 0:
            smoothing_sigmas = list(map(float, self.led_sigma_factors.text().split(";")))

        registration_settings = {"method": self.cbo_optim_method.currentIndex(),
                                 "shrink_factors": shrink_factors,
                                 "smoothing_sigmas": smoothing_sigmas}

        fixed_image = intraop_drr_data.all_images[f"drr_{self.cbo_intraop_input.currentIndex()}"]
        moving_image = preop_drr_data.all_images[f"drr_{self.cbo_preop_input.currentIndex()}"]

        registered_image = features.register_images(fixed_image=fixed_image,
                                                    moving_image=moving_image,
                                                    reg_settings=registration_settings,
                                                    progress_window=self.tbr_output_messages)
        registration_data.registered_image = registered_image
        registration_data.exist_state = True

        lower_thresh = self.led_lower_edge_thresh.text()
        upper_thresh = self.led_upper_edge_thresh.text()

        labeled_image = features.get_labeled_edges(fixed_image, registered_image,
                                                   guide_low_thresh=float(lower_thresh),
                                                   guide_up_thresh=float(upper_thresh),
                                                   colors=edge_colors)
        registration_data.all_images[f"labeled_{self.labeled_image_counter}"] = labeled_image
        self.labeled_image_counter += 1

        self.add_tree_child(3, f"hrany_Low{lower_thresh}_Up{upper_thresh}")

        labeled_array = sitk.GetArrayFromImage(labeled_image)
        self.display_image(labeled_image, "labeled_image")

    def display_image(self, image_data, image_name):

        self.window_dict[self.window_counter] = ImageViewer(image_data, image_name)
        self.window_dict[self.window_counter].show()
        self.window_counter += 1
        # fig, axes = plt.subplots(1, 1, num=self.fig_counter)
        # axes.set_title(image_name)
        # axes.set_axis_off()
        # self.fig_counter += 1

        # image_array = sitk.GetArrayFromImage(image_data)
        # shape = image_array.shape
        # if image_array.ndim == 2:
            #axes.imshow(image_array, cmap="gray")
        # elif image_array.ndim == 3:
        #     axes.imshow(image_array)


        #plt.show(block=False)

    def closeEvent(self, event: qtg.QCloseEvent) -> None:
        super().closeEvent(event)
        sys.exit()

    def input_settings_state_change(self):
        if self.rbu_intraop_drr.isChecked():
            self.led_drr_thresh.setEnabled(True)
        else:
            self.led_drr_thresh.setEnabled(False)
            self.led_drr_thresh.setText("0")

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

    def add_tree_child(self, level_index, child_name):

        subitem = qtw.QTreeWidgetItem([child_name])

        match level_index:
            case 0:  # ct item
                self.twi_data_list.topLevelItem(0).addChild(subitem)
            case 1:  # intraop drr item
                self.twi_data_list.topLevelItem(1).addChild(subitem)
            case 2:  # preop drr item
                self.twi_data_list.topLevelItem(2).addChild(subitem)
            case 3:  # registered items
                self.twi_data_list.topLevelItem(3).addChild(subitem)
        self.twi_data_list.topLevelItem(level_index).setExpanded(True)

    def display_double_clicked_item(self, item: qtw.QTreeWidgetItem):

        if item.parent() is None:
            return None

        index = self.twi_data_list.indexFromItem(item, 0).row()
        image_name = item.text(0)
        match item.parent().text(0):
            case "Intraoperační DRR":
                image_data = intraop_drr_data.all_images[f"drr_{index}"]
                image_array = sitk.GetArrayFromImage(image_data)
            case "Předoperační DRR":
                image_data = preop_drr_data.all_images[f"drr_{index}"]
                image_array = sitk.GetArrayFromImage(image_data)
            case "Výstup registrace":
                image_data = registration_data.all_images[f"labeled_{index}"]
            case _:
                return None

        self.display_image(image_data, image_name)

    def print_images(self):
        print(self.twi_data_list.selectedItems())
        print(self.cbo_optim_method.count())
        print(intraop_drr_data.drr_image.GetSize())
        print(preop_drr_data.drr_image.GetSize())
        print(registration_data.registered_image.GetSize())


class ImageViewer(qtw.QWidget):
    def __init__(self, image_data, image_name=None):
        super().__init__()
        qlayout = qtw.QVBoxLayout()
        self.qlabel = qtw.QLabel(image_name)
        qlayout.addWidget(self.qlabel)
        self.setLayout(qlayout)
        self.display_image(image_data, image_name)

    def display_image(self, image_data: sitk.Image, image_name):

        if image_data.GetPixelID() in {sitk.sitkUInt16, sitk.sitkInt16, sitk.sitkFloat32, sitk.sitkFloat64}:
            image_data = features.rescale_intensity(image_data)

        image_array = sitk.GetArrayFromImage(image_data)
        shape = image_array.shape
        if image_array.ndim == 2:
            qimage = qtg.QImage(image_array.data, shape[1], shape[0], image_array.strides[0],
                                qtg.QImage.Format.Format_Grayscale8)
        elif image_array.ndim == 3:
            qimage = qtg.QImage(image_array.data, shape[1], shape[0], image_array.strides[0],
                                qtg.QImage.Format.Format_RGB888)
        else:
            return None
        qpixmap = qtg.QPixmap(qimage)
        self.qlabel.setPixmap(qpixmap)


preop_drr_data = data_storage.PreOpDrrData()
intraop_ct_data = data_storage.IntraOpCtData()
intraop_drr_data = data_storage.IntraOpDrrData()
registration_data = data_storage.RegistrationData()
warning_stylesheet = "font-weight: bold; color: red"
warning_ct_text = "CHYBÍ CT DATA"
default_ct_text = "---"
edge_colors = {"yellow": [255, 255, 0],
               "red": [255, 0, 0]}
edge_yellow_color = np.array([255, 255, 0], dtype=np.uint8)
edge_red_color = np.array([255, 0, 0], dtype=np.uint8)
