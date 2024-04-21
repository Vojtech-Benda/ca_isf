import os
import sys
import SimpleITK as sitk
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

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

        # read intraop ct connection
        self.mac_read_intra_ct.triggered.connect(self.read_ct_triggered)

        # read/write drr connections
        self.mac_read_intraop_drr.triggered.connect(self.read_drr_triggered)
        self.mac_read_preop_drr.triggered.connect(self.read_drr_triggered)
        self.mac_write_preop_drr.triggered.connect(self.write_drr_triggered)
        self.mac_write_intraop_drr.triggered.connect(self.write_drr_triggered)

        # button actions func connections
        self.rbu_preop_drr.setChecked(True)
        self.rbu_preop_drr.toggled.connect(self.input_settings_state_change)
        self.rbu_intraop_drr.toggled.connect(self.input_settings_state_change)
        self.pbu_drr_start.clicked.connect(self.generate_drr_clicked)

        # display first toolbox page
        self.tab_main.setCurrentIndex(0)

        # create graphics scene
        self.gsc_drr = qtw.QGraphicsScene()
        self.gvi_drr.setScene(self.gsc_drr)

        self.cbo_visualization.currentIndexChanged.connect(self.display_image_at_index)

    @qtc.Slot()
    def read_ct_triggered(self) -> None:
        dir_path = qtw.QFileDialog.getExistingDirectory(self, caption="Otevřít DICOM CT",
                                                        dir=os.getcwd())

        if dir_path:
            ct_volume = io.read_dicom_files(dir_path=dir_path)
            ct_metadata = io.read_metadata(volume=ct_volume)

            intraop_ct_data.intraop_ct_volume = ct_volume
            intraop_ct_data.intraop_ct_meta = ct_metadata
            self.labm_intra_ct_name.setText(intraop_ct_data.intraop_ct_meta["patient_name"])
            if self.labm_data_warning.text != default_ct_text:
                self.labm_data_warning.setText(default_ct_text)
                self.labm_data_warning.setStyleSheet("")

    @qtc.Slot()
    def read_drr_triggered(self) -> None:
        file_path = qtw.QFileDialog.getOpenFileName(self, caption="Načíst DRR obraz",
                                                    dir=os.getcwd())
        if file_path[0]:
            drr_image = io.read_drr(file_path[0])
            if self.sender().objectName() == "mac_read_intraop_drr":
                intraop_drr_data.intraop_drr_image = drr_image
                intraop_drr_data.exist_state = True
            elif self.sender().objectName() == "mac_read_preop_drr":
                preop_drr_data.preop_drr_image = drr_image
                preop_drr_data.exist_state = True

    @qtc.Slot()
    def write_drr_triggered(self) -> None:
        file_path = qtw.QFileDialog.getSaveFileName(self, caption="Uložit předoperační DRR obraz",
                                                    dir=os.getcwd(),
                                                    filter="MHA (*.mha)")
        if file_path[0]:
            drr_image = None
            if self.sender().objectName() == "mac_write_preop_drr" and preop_drr_data.exist_state is True:
                drr_image = preop_drr_data.preop_drr_image
            elif self.sender().objectName() == "mac_write_intra_drr" and intraop_drr_data.exist_state is True:
                drr_image = intraop_drr_data.intraop_drr_image

            io.write_drr(drr_image, file_path[0])

    @qtc.Slot()
    def write_intraop_drr_triggered(self) -> None:
        pass
        # file_path = qtw.QFileDialog.getSaveFileName(self, caption="Uložit DRR obraz",
        #                                             dir=os.path.dirname(io.__file__),
        #                                             filter="Image (*.png)")
        # if intraop_drr_data.intra_drr_exist_state:
        #     io.write_drr(intraop_drr_data.intraop_drr_image, file_path[0])

    @qtc.Slot()
    def generate_drr_clicked(self):
        drr_size = (int(self.led_drr_width.text()),
                    int(self.led_drr_height.text()))
        drr_threshold = float(self.led_drr_thresh.text())
        drr_sid = float(self.led_sid.text())
        add_rnd_rotation = False
        if self.rbu_preop.isChecked() and self.check_preop_ct_exits():  # generate preop drr
            drr_settings = {"src_img_dist": drr_sid,
                            "output_drr_size": drr_size, "threshold": drr_threshold}
            output_drr_image = features.generate_drr(preop_ct_data.preop_ct_volume,
                                                     drr_settings)

            preop_drr_data.preop_drr_image = output_drr_image
            preop_drr_data.preop_drr_exist_state = True
            self.cbo_visualization.setCurrentIndex(0)
        elif self.rbu_intraop.isChecked() and self.check_intraop_ct_exists():  # generate intraop drr
            #TODO: add gvirtualxray drr image generation
            if self.cbo_inverse_gray.isChecked():
                output_drr_image = features.invert_drr_image(output_drr_image)
            intraop_drr_data.intraop_drr_image = output_drr_image
            intraop_drr_data.intra_drr_exist_state = True
            self.cbo_visualization.setCurrentIndex(1)
        else:
            return None

        self.display_image(output_drr_image)

    def display_image(self, input_image):
        image_rescaled = features.cast_image(input_image, image_type=sitk.sitkUInt8)
        image_array = sitk.GetArrayViewFromImage(image_rescaled)
        data = image_array.data  #
        height, width = image_array.shape
        strides = image_array.strides[0]  # bytes per line for QImage
        image_pixmap = qtg.QPixmap(qtg.QImage(data, width, height, strides,
                                              qtg.QImage.Format.Format_Grayscale8))
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
        if self.rbu_intraop.isChecked():
            self.led_drr_width.setEnabled(False)
            self.led_drr_height.setEnabled(False)
            self.led_sid.setEnabled(False)
            self.led_drr_width.setText("1000")
            self.led_drr_height.setText("1000")
            self.led_sid.setText("1000.0")
            self.led_drr_thresh.setText("-25")
        else:
            self.led_drr_width.setEnabled(True)
            self.led_drr_height.setEnabled(True)
            self.led_sid.setEnabled(True)
            self.led_drr_width.setText("512")
            self.led_drr_height.setText("512")
            self.led_drr_thresh.setText("100")

    def display_image_at_index(self):
        if self.cbo_visualization.currentIndex() == 0:  # display preop drr image
            self.display_image(preop_drr_data.preop_drr_image)
        elif self.cbo_visualization.currentIndex() == 1:  # display intraop drr image
            self.display_image(intraop_drr_data.intraop_drr_image)

    def check_preop_ct_exits(self):
        if self.labm_pre_ct_name.text() == default_ct_text:
            self.labm_preop_ct_warning.setText(warning_ct_text)
            self.labm_preop_ct_warning.setStyleSheet(warning_stylesheet)
            return False
        else:
            return True

    def check_intraop_ct_exists(self):
        if self.labm_intra_ct_name.text() == default_ct_text:
            self.labm_intraop_ct_warning.setText(warning_ct_text)
            self.labm_intraop_ct_warning.setStyleSheet(warning_stylesheet)
            return False
        else:
            return True


preop_drr_data = data_storage.PreOpDrrData()
intraop_ct_data = data_storage.IntraOpCtData()
intraop_drr_data = data_storage.IntraOpDrrData()
warning_stylesheet = "font-weight: bold; color: red"
warning_ct_text = "CHYBÍ CT DATA"
default_ct_text = "---"
