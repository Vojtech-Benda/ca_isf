import os
import sys
import SimpleITK as sitk
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from ca_iss_app.ui.main_window import Ui_win_main_window
from ca_iss_app.ui.drr_gen_window import Ui_win_drr_gen

import ca_iss_app.ca_iss_io as io
import ca_iss_app.ca_iss_features as features
import ca_iss_app.ca_iss_data_storage as data_storage
import ca_iss_app.ui.custom_widgets as widgets


class MainWindow(qtw.QMainWindow, Ui_win_main_window):
    def __init__(self, drr_gen_window) -> None:
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.drr_gen_window = drr_gen_window

        self.mac_info.triggered.connect(self.info_triggered)
        self.mac_exit.triggered.connect(sys.exit)
        self.mac_read_ct.triggered.connect(self.read_ct_triggered)
        self.mac_read_xray.triggered.connect(self.read_xray_triggered)
        self.mac_read_drr.triggered.connect(self.read_drr_triggered)
        self.mac_write_xray.triggered.connect(self.write_xray_triggered)
        self.mac_write_drr.triggered.connect(self.write_drr_triggered)
        self.mac_gen_drr.triggered.connect(self.open_drr_gen_window)

        self.gsc_xray = widgets.GraphicsScene()
        self.gvi_xray.setScene(self.gsc_xray)
        self.gvi_xray.set_pos_label(self.labm_xray_x_pos, self.labm_xray_y_pos)

        self.gsc_drr = widgets.GraphicsScene()
        self.gvi_drr.setScene(self.gsc_drr)
        self.gvi_drr.set_pos_label(self.labm_drr_x_pos, self.labm_drr_y_pos)

        self.drr_gen_window.pbu_gen_button.clicked.connect(self.generate_drr_clicked)

        self.pbu_paint.clicked.connect(self.start_painting)

    @qtc.Slot()
    def read_ct_triggered(self) -> None:
        dir_name = qtw.QFileDialog.getExistingDirectory(self, caption="Otevřít CT", dir=os.path.dirname(io.__file__))

        if dir_name:
            ct_data.ct_volume = io.read_dicom_files(dir_path=dir_name)
            ct_data.ct_meta = io.read_metadata(image=ct_data.ct_volume)
            self.labm_drr_name.setText(ct_data.ct_meta["patient_name"])
            self.drr_gen_window.set_ct_metadata()

    @qtc.Slot()
    def read_xray_triggered(self) -> None:
        dir_name = qtw.QFileDialog.getExistingDirectory(self, caption="Otevřít RTG", dir=os.path.dirname(io.__file__))

        if dir_name:
            xray_data.xray_image = io.read_dicom_files(dir_path=dir_name)
            xray_data.xray_meta = io.read_metadata(image=xray_data.xray_image)
            self.labm_xray_name.setText(xray_data.xray_meta["patient_name"])
            self.drr_gen_window.set_xray_metadata()
            self.display_image(xray_data.xray_image, graphics_scene=self.gsc_xray, graphics_view=self.gvi_xray)

    @qtc.Slot()
    def read_drr_triggered(self) -> None:
        print("drr load")

    @qtc.Slot()
    def write_xray_triggered(self) -> None:
        print("write xray")
        # file_name, suffix = qtw.QFileDialog.getSaveFileName(self, caption="Uložit CT", dir=os.path.dirname(io.__file__),
        #                                                     filter="DICOM (*.dcm);;")
        #
        # if file_name:
        #     io.write_ct(file_name, ct_data.ct_volume)

    @qtc.Slot()
    def write_drr_triggered(self) -> None:
        print("write drr")

    @qtc.Slot()
    def open_drr_gen_window(self) -> None:
        if self.drr_gen_window.isVisible():
            if not self.drr_gen_window.isActiveWindow():
                self.drr_gen_window.activateWindow()
        else:
            self.drr_gen_window.show()

    @qtc.Slot()
    def generate_drr_clicked(self):
        drr_size = (float(self.drr_gen_window.led_drr_width.text()),
                    float(self.drr_gen_window.led_drr_height.text()))
        drr_angle = float(self.drr_gen_window.led_drr_angle.text())
        drr_threshold = float(self.drr_gen_window.led_drr_threshold.text())
        drr_data.drr_image = features.generate_drr(ct_data.ct_volume, xray_data.xray_meta, drr_size,
                                                   rz_angle_deg=drr_angle, threshold=drr_threshold)
        self.drr_gen_window.create_drr_metadata()
        self.drr_gen_window.set_drr_metadata()
        self.display_image(drr_data.drr_image, graphics_scene=self.gsc_drr, graphics_view=self.gvi_drr)

    @staticmethod
    def display_image(input_image, graphics_scene: qtw.QGraphicsScene, graphics_view):
        image_rescaled = features.cast_image(input_image, image_type="uint8")
        image_array = sitk.GetArrayFromImage(image_rescaled)[0, ...]
        data = image_array.data
        height, width = image_array.shape
        strides = image_array.strides[0]  # bytes per line for QImage
        image_pixmap = qtg.QPixmap(qtg.QImage(data, width, height, strides, qtg.QImage.Format_Grayscale8))
        graphics_view.setSceneRect(0, 0, width, height)
        image_pixmap.rect()
        graphics_scene.addPixmap(image_pixmap)
        graphics_view.fitInView(0, 0, width, height, qtc.Qt.AspectRatioMode.KeepAspectRatioByExpanding)
        graphics_view.set_image_metadata(xray_data.xray_meta)
        graphics_scene.update()

    @qtc.Slot()
    def start_painting(self):
        if self.gvi_xray.pixel_spacing is not None:
            self.gvi_xray.start_point = None
            self.gvi_xray.end_point = None
            self.gvi_xray.set_painting_flag(True)

    @qtc.Slot()
    def info_triggered(self) -> None:
        print(point_list.points)

    def resizeEvent(self, event: qtg.QResizeEvent) -> None:
        super().resizeEvent(event)

        xray_width, xray_height = xray_data.xray_image.GetSize()[:2]
        self.gvi_xray.fitInView(0, 0, xray_width, xray_height, qtc.Qt.AspectRatioMode.KeepAspectRatioByExpanding)

        drr_width, drr_height = drr_data.drr_image.GetSize()[:2]
        self.gvi_drr.fitInView(0, 0, drr_width, drr_height, qtc.Qt.AspectRatioMode.KeepAspectRatioByExpanding)

    def closeEvent(self, event: qtg.QCloseEvent) -> None:
        super().closeEvent(event)

        sys.exit()


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


ct_data = data_storage.CtData()
xray_data = data_storage.XrayData()
drr_data = data_storage.DrrData()
point_list = data_storage.PointList()
