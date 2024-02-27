import sys
from PySide6.QtWidgets import QApplication

from ca_iss_app.ca_iss_gui import MainWindow


def run_main():
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    run_main()
