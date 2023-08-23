import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from ca_iss_app.ui.main_window import Ui_app_window

import ca_iss_app.ca_iss_io as io
import ca_iss_app.ca_iss_features as features


class MainWindow(qtw.QMainWindow, Ui_app_window):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.menu_exit_action.triggered.connect(self.close)

        self.load_ct_action = qtg.QAction()
        self.load_ct_action.triggered.connect(self.load_ct_triggered)
        self.load_ct_action.setText("Načíst CT")

        self.load_drr_action = qtg.QAction()
        self.load_drr_action.triggered.connect(self.load_drr_triggered)
        self.load_drr_action.setText("Načíst DRR")

        self.load_rtg_action = qtg.QAction()
        self.load_rtg_action.triggered.connect(self.load_rtg_triggered)
        self.load_rtg_action.setText("Načíst RTG")

        self.load_menu = qtw.QMenu()
        self.load_menu.addActions([self.load_ct_action, self.load_rtg_action, self.load_drr_action])
        self.load_button.setMenu(self.load_menu)

    def load_ct_triggered(self):
        print("ct load")
        dir_name = qtw.QFileDialog.getExistingDirectory(self, caption="Otevřít CT")
        ct_volume = io.read_ct(dir_path=dir_name)
        ct_meta = io.read_metadata(image_modality="ct")
        print(ct_volume)
        print(ct_meta)
        self.drr_name_value.setText(ct_meta["patient_name"])
        self.drr_count_value.setText(str(ct_meta["slices"]))

    def load_rtg_triggered(self):
        print("xray load")
        dir_name = qtw.QFileDialog.getExistingDirectory(self, caption="Otevřít RTG")
        xray_image = io.read_xray(dir_path=dir_name)
        xray_meta = io.read_metadata(image_modality="xray")
        print(xray_image)
        print(xray_meta)
        self.xray_name_value.setText(xray_meta["patient_name"])
        self.xray_size_value.setText(f"{xray_meta['rows']}x{xray_meta['columns']}")

    def load_drr_triggered(self):
        print("drr load")

