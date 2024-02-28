import os
import sys
import SimpleITK as sitk
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from casif_app.ui.main_window_alt import Ui_win_main_window

import casif_app.casif_io as io
import casif_app.casif_features as features
import casif_app.casif_data_storage as data_storage


# import ca_iss_app.ui.custom_widgets as widgets


class MainWindow(qtw.QMainWindow, Ui_win_main_window):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # menu actions func connections
        self.mac_exit.triggered.connect(sys.exit)
        self.mac_read_pre_ct.triggered.connect(self.read_ct_triggered)
        self.mac_read_intra_ct.triggered.connect(self.read_ct_triggered)
        self.mac_read_drr.triggered.connect(self.read_drr_triggered)
        self.mac_write_pre_drr.triggered.connect(self.write_drr_triggered)
        self.mac_write_intra_drr.triggered.connect(self.write_drr_triggered)

        # button actions func connections
        self.rbu_preop.setChecked(True)
        self.rbu_preop.toggled.connect(self.input_settings_state_change)
        self.rbu_intraop.toggled.connect(self.input_settings_state_change)
        self.pbu_drr_start.clicked.connect(self.generate_drr_clicked)

        # display first toolbox page
        self.tob_main.setCurrentIndex(0)

        # create graphics scene
        self.gsc_drr = qtw.QGraphicsScene()
        self.gvi_drr.setScene(self.gsc_drr)

        self.cbo_visualization.currentIndexChanged.connect(self.display_image_at_index)

    @qtc.Slot()
    def read_ct_triggered(self) -> None:
        dir_name = qtw.QFileDialog.getExistingDirectory(self, caption="Otevřít DICOM CT", dir=os.path.dirname(
            io.__file__))

        if dir_name:
            ct_volume = io.read_dicom_files(dir_path=dir_name)
            ct_metadata = io.read_metadata(image=preop_ct_data.preop_ct_volume)

            if self.sender().objectName() == "mac_read_pre_ct":
                preop_ct_data.preop_ct_volume = ct_volume
                preop_ct_data.preop_ct_meta = ct_metadata
                self.labm_pre_ct_name.setText(preop_ct_data.preop_ct_meta["patient_name"])
                if self.labm_preop_ct_warning.text != default_ct_text:
                    self.labm_preop_ct_warning.setText(default_ct_text)
                    self.labm_preop_ct_warning.setStyleSheet("")
            else:
                intraop_ct_data.intraop_ct_volume = ct_volume
                intraop_ct_data.intraop_ct_meta = ct_metadata
                self.labm_intra_ct_name.setText(intraop_ct_data.intraop_ct_meta["patient_name"])
                if self.labm_intraop_ct_warning.text != default_ct_text:
                    self.labm_intraop_ct_warning.setText(default_ct_text)
                    self.labm_intraop_ct_warning.setStyleSheet("")

    @qtc.Slot()
    def read_drr_triggered(self) -> None:
        print("drr load")

    @qtc.Slot()
    def write_drr_triggered(self) -> None:
        print("write drr")

    @qtc.Slot()
    def generate_drr_clicked(self):
        drr_size = (int(self.led_drr_width.text()),
                    int(self.led_drr_height.text()))
        drr_view = self.cbo_drr_view.currentIndex()
        drr_threshold = float(self.led_drr_thresh.text())
        drr_sid = float(self.led_sid.text())

        if self.rbu_preop.isChecked() and self.check_preop_ct_exits():  # generate preop drr
            output_drr_image = features.generate_drr_alt(preop_ct_data.preop_ct_volume,
                                                         output_view=drr_view,
                                                         src_img_dist=drr_sid,
                                                         output_drr_size=drr_size,
                                                         threshold=drr_threshold,
                                                         ct_source="preop")
            preop_drr_data.preop_drr_image = output_drr_image
            self.cbo_visualization.setCurrentIndex(0)
        elif self.rbu_intraop.isChecked() and self.check_intraop_ct_exists():  # generate intraop drr
            output_drr_image = features.generate_drr_alt(intraop_ct_data.intraop_ct_volume,
                                                         output_view=drr_view,
                                                         src_img_dist=drr_sid,
                                                         output_drr_size=drr_size,
                                                         threshold=drr_threshold,
                                                         ct_source="intraop")
            if self.cbo_inverse_gray.isChecked():
                output_drr_image = features.invert_drr_image(output_drr_image)
            intraop_drr_data.intraop_drr_image = output_drr_image
        else:
            return None

        self.display_image(output_drr_image)
        self.cbo_visualization.setCurrentIndex(1)

    def display_image(self, input_image):
        # image_rescaled = features.cast_image(input_image, image_type="uint8")
        image_array = sitk.GetArrayViewFromImage(input_image)[0, ...]
        data = image_array.data #
        height, width = image_array.shape
        strides = image_array.strides[0]  # bytes per line for QImage
        image_pixmap = qtg.QPixmap(qtg.QImage(data, width, height, strides,
                                              qtg.QImage.Format.Format_Grayscale16))
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
        if self.cbo_visualization.currentIndex() == 0: # display preop drr image
            self.display_image(preop_drr_data.preop_drr_image)
        elif self.cbo_visualization.currentIndex() == 1: # display intraop drr image
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

"""
class DrrGenWindow(qtw.QWidget, Ui_win_drr_gen):
    def __init__(self) -> None:
        super(DrrGenWindow, self).__init__()
        self.setupUi(self)

        self.confirm_icon = self.style().standardIcon(qtw.QStyle.StandardPixmap.SP_DialogApplyButton).pixmap(
            qtc.QSize(20, 20))
        self.cancel_icon = self.style().standardIcon(qtw.QStyle.StandardPixmap.SP_DialogCancelButton).pixmap(
            qtc.QSize(20, 20))
        self.labm_ct_loaded.setPixmap(self.cancel_icon)
        self.labm_xray_loaded.setPixmap(self.cancel_icon)

    def set_ct_metadata(self) -> None:
        ct_meta = ct_data.ct_meta
        self.labm_ct_loaded.setPixmap(self.confirm_icon)
        self.labm_ct_name.setText(ct_meta["patient_name"])
        self.labm_slice_count.setText(f"{ct_meta['size'][2]}")
        self.labm_slice_thickness.setText(f"{ct_meta['pixel_spacing'][2]:.2f}")

    def set_xray_metadata(self) -> None:
        xray_meta = xray_data.xray_meta
        self.labm_xray_loaded.setPixmap(self.confirm_icon)
        self.labm_xray_name.setText(xray_meta["patient_name"])
        self.labm_xray_sdd.setText(f"{xray_meta['src_det_distance']}")
        self.labm_xray_size.setText(f"{xray_meta['size'][0]}\\"
                                    f"{xray_meta['size'][1]}")
        self.labm_xray_pixel_spacing.setText(f"{xray_meta['pixel_spacing'][0]:.2f}\\"
                                             f"{xray_meta['pixel_spacing'][1]:.2f}")

    def create_drr_metadata(self) -> None:
        drr_size = drr_data.drr_image.GetSize()
        drr_angle = int(self.led_drr_angle.text())
        drr_name = f"{ct_data.ct_meta['patient_name']}_drr_{drr_angle}"
        drr_threshold = int(self.led_drr_threshold.text())
        drr_pixel_spacing = drr_data.drr_image.GetSpacing()

        drr_data.drr_meta = {"name": drr_name, "size": drr_size, "angle": drr_angle, "threshold": drr_threshold,
                             "pixel_spacing": drr_pixel_spacing}

    def set_drr_metadata(self) -> None:
        drr_meta = drr_data.drr_meta
        self.labm_drr_size.setText(f"{drr_meta['size'][0]}\\"
                                   f"{drr_meta['size'][1]}")
        self.labm_drr_pixel_spacing.setText(f"{drr_meta['pixel_spacing'][0]:.2f}\\"
                                            f"{drr_meta['pixel_spacing'][1]:.2f}")
"""

preop_ct_data = data_storage.PreOpCtData()
preop_drr_data = data_storage.PreOpDrrData()
intraop_ct_data = data_storage.IntraOpCtData()
intraop_drr_data = data_storage.IntraOpDrrData()
warning_stylesheet = "font-weight: bold; color: red"
warning_ct_text = "CHYBÍ CT DATA"
default_ct_text = "---"
