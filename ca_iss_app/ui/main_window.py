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
    QGridLayout, QLabel, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)

from ca_iss_app.ui.custom_widgets import GraphicsView

class Ui_win_main_window(object):
    def setupUi(self, win_main_window):
        if not win_main_window.objectName():
            win_main_window.setObjectName(u"win_main_window")
        win_main_window.resize(1366, 768)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(win_main_window.sizePolicy().hasHeightForWidth())
        win_main_window.setSizePolicy(sizePolicy)
        self.mac_info = QAction(win_main_window)
        self.mac_info.setObjectName(u"mac_info")
        self.mac_exit = QAction(win_main_window)
        self.mac_exit.setObjectName(u"mac_exit")
        self.mac_read_ct = QAction(win_main_window)
        self.mac_read_ct.setObjectName(u"mac_read_ct")
        self.mac_read_xray = QAction(win_main_window)
        self.mac_read_xray.setObjectName(u"mac_read_xray")
        self.mac_read_drr = QAction(win_main_window)
        self.mac_read_drr.setObjectName(u"mac_read_drr")
        self.mac_write_xray = QAction(win_main_window)
        self.mac_write_xray.setObjectName(u"mac_write_xray")
        self.mac_write_drr = QAction(win_main_window)
        self.mac_write_drr.setObjectName(u"mac_write_drr")
        self.mac_gen_drr = QAction(win_main_window)
        self.mac_gen_drr.setObjectName(u"mac_gen_drr")
        self.lay_main_layout = QWidget(win_main_window)
        self.lay_main_layout.setObjectName(u"lay_main_layout")
        self.gridLayout = QGridLayout(self.lay_main_layout)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lab_drr_name = QLabel(self.lay_main_layout)
        self.lab_drr_name.setObjectName(u"lab_drr_name")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lab_drr_name.sizePolicy().hasHeightForWidth())
        self.lab_drr_name.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.lab_drr_name.setFont(font)
        self.lab_drr_name.setTextFormat(Qt.PlainText)
        self.lab_drr_name.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lab_drr_name, 0, 5, 2, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 0, 3, 2, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 0, 2, 1)

        self.gvi_xray = GraphicsView(self.lay_main_layout)
        self.gvi_xray.setObjectName(u"gvi_xray")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.gvi_xray.sizePolicy().hasHeightForWidth())
        self.gvi_xray.setSizePolicy(sizePolicy2)
        self.gvi_xray.setMinimumSize(QSize(600, 600))
        self.gvi_xray.setMouseTracking(False)
        self.gvi_xray.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.gvi_xray.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.gvi_xray.setDragMode(QGraphicsView.NoDrag)
        self.gvi_xray.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.gvi_xray.setResizeAnchor(QGraphicsView.NoAnchor)

        self.gridLayout.addWidget(self.gvi_xray, 2, 0, 1, 4)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 0, 4, 2, 1)

        self.labm_xray_name = QLabel(self.lay_main_layout)
        self.labm_xray_name.setObjectName(u"labm_xray_name")
        sizePolicy1.setHeightForWidth(self.labm_xray_name.sizePolicy().hasHeightForWidth())
        self.labm_xray_name.setSizePolicy(sizePolicy1)
        self.labm_xray_name.setFont(font)
        self.labm_xray_name.setTextFormat(Qt.PlainText)
        self.labm_xray_name.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labm_xray_name, 0, 2, 2, 1)

        self.fra_xray_info_panel = QFrame(self.lay_main_layout)
        self.fra_xray_info_panel.setObjectName(u"fra_xray_info_panel")
        self.fra_xray_info_panel.setFrameShape(QFrame.Box)
        self.fra_xray_info_panel.setFrameShadow(QFrame.Plain)
        self.gridLayout_3 = QGridLayout(self.fra_xray_info_panel)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.labm_xray_y_pos = QLabel(self.fra_xray_info_panel)
        self.labm_xray_y_pos.setObjectName(u"labm_xray_y_pos")
        self.labm_xray_y_pos.setMinimumSize(QSize(30, 0))
        self.labm_xray_y_pos.setMaximumSize(QSize(30, 16777215))

        self.gridLayout_3.addWidget(self.labm_xray_y_pos, 0, 4, 1, 1)

        self.labm_xray_x_pos = QLabel(self.fra_xray_info_panel)
        self.labm_xray_x_pos.setObjectName(u"labm_xray_x_pos")
        self.labm_xray_x_pos.setMinimumSize(QSize(30, 0))
        self.labm_xray_x_pos.setMaximumSize(QSize(30, 16777215))

        self.gridLayout_3.addWidget(self.labm_xray_x_pos, 0, 2, 1, 1)

        self.pbu_paint = QPushButton(self.fra_xray_info_panel)
        self.pbu_paint.setObjectName(u"pbu_paint")
        self.pbu_paint.setMaximumSize(QSize(60, 16777215))
        self.pbu_paint.setCheckable(False)
        self.pbu_paint.setChecked(False)
        self.pbu_paint.setAutoDefault(False)
        self.pbu_paint.setFlat(False)

        self.gridLayout_3.addWidget(self.pbu_paint, 1, 0, 1, 1)

        self.lab_xray_x_pos = QLabel(self.fra_xray_info_panel)
        self.lab_xray_x_pos.setObjectName(u"lab_xray_x_pos")

        self.gridLayout_3.addWidget(self.lab_xray_x_pos, 0, 1, 1, 1)

        self.lab_xray_y_pos = QLabel(self.fra_xray_info_panel)
        self.lab_xray_y_pos.setObjectName(u"lab_xray_y_pos")

        self.gridLayout_3.addWidget(self.lab_xray_y_pos, 0, 3, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_4, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.fra_xray_info_panel, 3, 0, 1, 4)

        self.lab_xray_name = QLabel(self.lay_main_layout)
        self.lab_xray_name.setObjectName(u"lab_xray_name")
        sizePolicy1.setHeightForWidth(self.lab_xray_name.sizePolicy().hasHeightForWidth())
        self.lab_xray_name.setSizePolicy(sizePolicy1)
        self.lab_xray_name.setFont(font)

        self.gridLayout.addWidget(self.lab_xray_name, 0, 1, 2, 1)

        self.labm_drr_name = QLabel(self.lay_main_layout)
        self.labm_drr_name.setObjectName(u"labm_drr_name")
        sizePolicy1.setHeightForWidth(self.labm_drr_name.sizePolicy().hasHeightForWidth())
        self.labm_drr_name.setSizePolicy(sizePolicy1)
        self.labm_drr_name.setFont(font)

        self.gridLayout.addWidget(self.labm_drr_name, 0, 6, 2, 2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 8, 1, 1)

        self.gvi_drr = GraphicsView(self.lay_main_layout)
        self.gvi_drr.setObjectName(u"gvi_drr")
        sizePolicy2.setHeightForWidth(self.gvi_drr.sizePolicy().hasHeightForWidth())
        self.gvi_drr.setSizePolicy(sizePolicy2)
        self.gvi_drr.setMinimumSize(QSize(600, 600))
        self.gvi_drr.setMouseTracking(False)
        self.gvi_drr.setFrameShape(QFrame.StyledPanel)
        self.gvi_drr.setFrameShadow(QFrame.Plain)
        self.gvi_drr.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.gvi_drr.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.gvi_drr.setDragMode(QGraphicsView.NoDrag)
        self.gvi_drr.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)

        self.gridLayout.addWidget(self.gvi_drr, 2, 4, 1, 5)

        self.fra_drr_info_panel = QFrame(self.lay_main_layout)
        self.fra_drr_info_panel.setObjectName(u"fra_drr_info_panel")
        self.fra_drr_info_panel.setFrameShape(QFrame.Box)
        self.fra_drr_info_panel.setFrameShadow(QFrame.Plain)
        self.gridLayout_4 = QGridLayout(self.fra_drr_info_panel)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.labm_drr_y_pos = QLabel(self.fra_drr_info_panel)
        self.labm_drr_y_pos.setObjectName(u"labm_drr_y_pos")
        self.labm_drr_y_pos.setMinimumSize(QSize(30, 0))

        self.gridLayout_4.addWidget(self.labm_drr_y_pos, 0, 4, 1, 1)

        self.labm_drr_x_pos = QLabel(self.fra_drr_info_panel)
        self.labm_drr_x_pos.setObjectName(u"labm_drr_x_pos")
        self.labm_drr_x_pos.setMinimumSize(QSize(30, 0))

        self.gridLayout_4.addWidget(self.labm_drr_x_pos, 0, 2, 1, 1)

        self.lab_drr_x_pos = QLabel(self.fra_drr_info_panel)
        self.lab_drr_x_pos.setObjectName(u"lab_drr_x_pos")

        self.gridLayout_4.addWidget(self.lab_drr_x_pos, 0, 1, 1, 1)

        self.lab_drr_y_pos = QLabel(self.fra_drr_info_panel)
        self.lab_drr_y_pos.setObjectName(u"lab_drr_y_pos")

        self.gridLayout_4.addWidget(self.lab_drr_y_pos, 0, 3, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_6, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.fra_drr_info_panel, 3, 4, 1, 5)

        win_main_window.setCentralWidget(self.lay_main_layout)
        self.mba_main_menu = QMenuBar(win_main_window)
        self.mba_main_menu.setObjectName(u"mba_main_menu")
        self.mba_main_menu.setGeometry(QRect(0, 0, 1366, 22))
        self.men_file = QMenu(self.mba_main_menu)
        self.men_file.setObjectName(u"men_file")
        self.men_read = QMenu(self.men_file)
        self.men_read.setObjectName(u"men_read")
        self.men_read.setTearOffEnabled(False)
        self.men_read.setSeparatorsCollapsible(False)
        self.men_write = QMenu(self.men_file)
        self.men_write.setObjectName(u"men_write")
        self.men_drr = QMenu(self.mba_main_menu)
        self.men_drr.setObjectName(u"men_drr")
        win_main_window.setMenuBar(self.mba_main_menu)
        QWidget.setTabOrder(self.gvi_xray, self.gvi_drr)

        self.mba_main_menu.addAction(self.men_file.menuAction())
        self.mba_main_menu.addAction(self.men_drr.menuAction())
        self.men_file.addAction(self.men_read.menuAction())
        self.men_file.addAction(self.men_write.menuAction())
        self.men_file.addAction(self.mac_info)
        self.men_file.addSeparator()
        self.men_file.addAction(self.mac_exit)
        self.men_read.addAction(self.mac_read_ct)
        self.men_read.addAction(self.mac_read_xray)
        self.men_read.addAction(self.mac_read_drr)
        self.men_write.addAction(self.mac_write_xray)
        self.men_write.addAction(self.mac_write_drr)
        self.men_drr.addAction(self.mac_gen_drr)

        self.retranslateUi(win_main_window)

        self.pbu_paint.setDefault(False)


        QMetaObject.connectSlotsByName(win_main_window)
    # setupUi

    def retranslateUi(self, win_main_window):
        win_main_window.setWindowTitle(QCoreApplication.translate("win_main_window", u"CA Iliosakr\u00e1ln\u00ed Fixace", None))
        self.mac_info.setText(QCoreApplication.translate("win_main_window", u"Informace", None))
        self.mac_exit.setText(QCoreApplication.translate("win_main_window", u"Ukon\u010dit", None))
        self.mac_read_ct.setText(QCoreApplication.translate("win_main_window", u"CT \u0159ezy", None))
        self.mac_read_xray.setText(QCoreApplication.translate("win_main_window", u"RTG obraz", None))
        self.mac_read_drr.setText(QCoreApplication.translate("win_main_window", u"DRR obraz", None))
        self.mac_write_xray.setText(QCoreApplication.translate("win_main_window", u"RTG obraz", None))
        self.mac_write_drr.setText(QCoreApplication.translate("win_main_window", u"DRR obraz", None))
        self.mac_gen_drr.setText(QCoreApplication.translate("win_main_window", u"Vytvo\u0159it DRR obraz", None))
        self.lab_drr_name.setText(QCoreApplication.translate("win_main_window", u"DRR:", None))
        self.labm_xray_name.setText(QCoreApplication.translate("win_main_window", u"-", None))
        self.labm_xray_y_pos.setText(QCoreApplication.translate("win_main_window", u"-", None))
        self.labm_xray_x_pos.setText(QCoreApplication.translate("win_main_window", u"-", None))
        self.pbu_paint.setText(QCoreApplication.translate("win_main_window", u"Kreslit", None))
        self.lab_xray_x_pos.setText(QCoreApplication.translate("win_main_window", u"X:", None))
        self.lab_xray_y_pos.setText(QCoreApplication.translate("win_main_window", u"Y:", None))
        self.lab_xray_name.setText(QCoreApplication.translate("win_main_window", u"RTG:", None))
        self.labm_drr_name.setText(QCoreApplication.translate("win_main_window", u"-", None))
        self.labm_drr_y_pos.setText(QCoreApplication.translate("win_main_window", u"-", None))
        self.labm_drr_x_pos.setText(QCoreApplication.translate("win_main_window", u"-", None))
        self.lab_drr_x_pos.setText(QCoreApplication.translate("win_main_window", u"X:", None))
        self.lab_drr_y_pos.setText(QCoreApplication.translate("win_main_window", u"Y:", None))
        self.men_file.setTitle(QCoreApplication.translate("win_main_window", u"Soubor", None))
        self.men_read.setTitle(QCoreApplication.translate("win_main_window", u"Otev\u0159\u00edt", None))
        self.men_write.setTitle(QCoreApplication.translate("win_main_window", u"Ulo\u017eit", None))
        self.men_drr.setTitle(QCoreApplication.translate("win_main_window", u"DRR", None))
    # retranslateUi

