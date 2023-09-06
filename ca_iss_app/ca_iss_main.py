import sys
from PySide6.QtWidgets import QApplication

from ca_iss_app.ca_iss_gui import MainWindow, DrrGenWindow


def run_main():
    # ct_image = io.read_ct(dir_path=r"D:\skola\DP\dp_isr\sample_files\dicom")
    # xray_image = io.read_xray(dir_path=r"/rtg")
    # xray_metadata = io.read_metadata("xray")
    # drr_image = features.generate_drr(ct_image, xray_metadata, drr_size=(1024.0, 1024.0), rz_angle_deg=0.0)
    # drr_image_casted = features.cast_image(drr_image)
    # io.write_drr(drr_image_casted, dir_path="/\\")

    app = QApplication(sys.argv)

    drr_gen_window = DrrGenWindow()
    main_window = MainWindow(drr_gen_window)
    main_window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    run_main()
