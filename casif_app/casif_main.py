import sys
from PySide6.QtWidgets import QApplication

from casif_app.casif_gui import MainWindow


def run_main():
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    run_main()
