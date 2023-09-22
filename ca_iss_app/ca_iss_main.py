import sys
from PySide6.QtWidgets import QApplication

from ca_iss_app.ca_iss_gui import MainWindow, DrrGenWindow


def run_main():
    app = QApplication(sys.argv)

    drr_gen_window = DrrGenWindow()
    main_window = MainWindow(drr_gen_window)
    main_window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    run_main()
