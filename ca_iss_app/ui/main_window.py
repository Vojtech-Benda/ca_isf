# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QGraphicsView,
    QGridLayout, QLabel, QLayout, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QToolButton, QWidget)

class Ui_win_main_window(object):
    def setupUi(self, win_main_window):
        if not win_main_window.objectName():
            win_main_window.setObjectName(u"win_main_window")
        win_main_window.resize(1005, 855)
        self.mac_info = QAction(win_main_window)
        self.mac_info.setObjectName(u"mac_info")
        self.mac_exit = QAction(win_main_window)
        self.mac_exit.setObjectName(u"mac_exit")
        self.lay_main_layout = QWidget(win_main_window)
        self.lay_main_layout.setObjectName(u"lay_main_layout")
        self.gridLayout = QGridLayout(self.lay_main_layout)
        self.gridLayout.setObjectName(u"gridLayout")
        self.labm_xray_name = QLabel(self.lay_main_layout)
        self.labm_xray_name.setObjectName(u"labm_xray_name")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.labm_xray_name.setFont(font)
        self.labm_xray_name.setTextFormat(Qt.PlainText)
        self.labm_xray_name.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labm_xray_name, 2, 2, 1, 2)

        self.gvi_xray = QGraphicsView(self.lay_main_layout)
        self.gvi_xray.setObjectName(u"gvi_xray")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gvi_xray.sizePolicy().hasHeightForWidth())
        self.gvi_xray.setSizePolicy(sizePolicy)
        self.gvi_xray.setMinimumSize(QSize(480, 680))
        self.gvi_xray.setMouseTracking(True)
        self.gvi_xray.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.gvi_xray.setDragMode(QGraphicsView.ScrollHandDrag)
        self.gvi_xray.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.gvi_xray.setResizeAnchor(QGraphicsView.NoAnchor)

        self.gridLayout.addWidget(self.gvi_xray, 3, 0, 1, 5)

        self.fra_control_frame = QFrame(self.lay_main_layout)
        self.fra_control_frame.setObjectName(u"fra_control_frame")
        self.fra_control_frame.setFrameShape(QFrame.NoFrame)
        self.fra_control_frame.setFrameShadow(QFrame.Plain)
        self.fra_control_frame.setLineWidth(1)
        self.fra_control_frame.setMidLineWidth(0)
        self.gridLayout_2 = QGridLayout(self.fra_control_frame)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pbu_open_gen_window = QPushButton(self.fra_control_frame)
        self.pbu_open_gen_window.setObjectName(u"pbu_open_gen_window")
        self.pbu_open_gen_window.setMinimumSize(QSize(60, 55))
        self.pbu_open_gen_window.setMaximumSize(QSize(60, 55))
        self.pbu_open_gen_window.setIconSize(QSize(25, 30))

        self.gridLayout_2.addWidget(self.pbu_open_gen_window, 0, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 4, 1, 1)

        self.tbu_read_button = QToolButton(self.fra_control_frame)
        self.tbu_read_button.setObjectName(u"tbu_read_button")
        self.tbu_read_button.setMinimumSize(QSize(60, 55))
        self.tbu_read_button.setMaximumSize(QSize(60, 55))
        self.tbu_read_button.setIconSize(QSize(30, 30))
        self.tbu_read_button.setPopupMode(QToolButton.InstantPopup)
        self.tbu_read_button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.tbu_read_button.setAutoRaise(False)
        self.tbu_read_button.setArrowType(Qt.NoArrow)

        self.gridLayout_2.addWidget(self.tbu_read_button, 0, 1, 1, 1)

        self.tbu_write_button = QToolButton(self.fra_control_frame)
        self.tbu_write_button.setObjectName(u"tbu_write_button")
        self.tbu_write_button.setMinimumSize(QSize(60, 55))
        self.tbu_write_button.setMaximumSize(QSize(60, 55))
        self.tbu_write_button.setIconSize(QSize(30, 30))
        self.tbu_write_button.setCheckable(False)
        self.tbu_write_button.setChecked(False)
        self.tbu_write_button.setPopupMode(QToolButton.InstantPopup)
        self.tbu_write_button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.tbu_write_button.setAutoRaise(False)
        self.tbu_write_button.setArrowType(Qt.NoArrow)

        self.gridLayout_2.addWidget(self.tbu_write_button, 0, 2, 1, 1)


        self.gridLayout.addWidget(self.fra_control_frame, 0, 0, 1, 9)

        self.labm_drr_name = QLabel(self.lay_main_layout)
        self.labm_drr_name.setObjectName(u"labm_drr_name")
        self.labm_drr_name.setFont(font)

        self.gridLayout.addWidget(self.labm_drr_name, 2, 7, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 2, 4, 1, 1)

        self.lab_xray_name = QLabel(self.lay_main_layout)
        self.lab_xray_name.setObjectName(u"lab_xray_name")
        self.lab_xray_name.setFont(font)

        self.gridLayout.addWidget(self.lab_xray_name, 2, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 2, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 2, 8, 1, 1)

        self.lab_drr_name = QLabel(self.lay_main_layout)
        self.lab_drr_name.setObjectName(u"lab_drr_name")
        self.lab_drr_name.setFont(font)
        self.lab_drr_name.setTextFormat(Qt.PlainText)
        self.lab_drr_name.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lab_drr_name, 2, 6, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 2, 5, 1, 1)

        self.gvi_drr = QGraphicsView(self.lay_main_layout)
        self.gvi_drr.setObjectName(u"gvi_drr")
        self.gvi_drr.setMinimumSize(QSize(480, 680))
        self.gvi_drr.setFrameShape(QFrame.StyledPanel)
        self.gvi_drr.setFrameShadow(QFrame.Plain)
        self.gvi_drr.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.gvi_drr.setDragMode(QGraphicsView.RubberBandDrag)
        self.gvi_drr.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)

        self.gridLayout.addWidget(self.gvi_drr, 3, 5, 1, 4)

        win_main_window.setCentralWidget(self.lay_main_layout)
        self.mba_main_menu = QMenuBar(win_main_window)
        self.mba_main_menu.setObjectName(u"mba_main_menu")
        self.mba_main_menu.setGeometry(QRect(0, 0, 1005, 22))
        self.men_file_menu = QMenu(self.mba_main_menu)
        self.men_file_menu.setObjectName(u"men_file_menu")
        win_main_window.setMenuBar(self.mba_main_menu)
        QWidget.setTabOrder(self.tbu_read_button, self.tbu_write_button)
        QWidget.setTabOrder(self.tbu_write_button, self.pbu_open_gen_window)
        QWidget.setTabOrder(self.pbu_open_gen_window, self.gvi_xray)
        QWidget.setTabOrder(self.gvi_xray, self.gvi_drr)

        self.mba_main_menu.addAction(self.men_file_menu.menuAction())
        self.men_file_menu.addAction(self.mac_info)
        self.men_file_menu.addSeparator()
        self.men_file_menu.addAction(self.mac_exit)

        self.retranslateUi(win_main_window)

        QMetaObject.connectSlotsByName(win_main_window)
    # setupUi

    def retranslateUi(self, win_main_window):
        win_main_window.setWindowTitle(QCoreApplication.translate("win_main_window", u"CA Iliosakr\u00e1ln\u00ed Fixace", None))
        self.mac_info.setText(QCoreApplication.translate("win_main_window", u"Informace", None))
        self.mac_exit.setText(QCoreApplication.translate("win_main_window", u"Ukon\u010dit", None))
        self.labm_xray_name.setText(QCoreApplication.translate("win_main_window", u"-", None))
        self.pbu_open_gen_window.setText(QCoreApplication.translate("win_main_window", u"Vytvo\u0159it\n"
"DRR", None))
        self.tbu_read_button.setText(QCoreApplication.translate("win_main_window", u"Otev\u0159\u00edt", None))
        self.tbu_write_button.setText(QCoreApplication.translate("win_main_window", u"Ulo\u017eit", None))
        self.labm_drr_name.setText(QCoreApplication.translate("win_main_window", u"-", None))
        self.lab_xray_name.setText(QCoreApplication.translate("win_main_window", u"RTG:", None))
        self.lab_drr_name.setText(QCoreApplication.translate("win_main_window", u"DRR:", None))
        self.men_file_menu.setTitle(QCoreApplication.translate("win_main_window", u"Soubor", None))
    # retranslateUi

