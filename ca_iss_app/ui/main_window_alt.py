# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window_alt.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QCheckBox, QComboBox,
    QFrame, QGraphicsView, QGridLayout, QGroupBox,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QToolBox, QWidget)

from ca_iss_app.ui.custom_widgets import GraphicsView

class Ui_win_main_window(object):
    def setupUi(self, win_main_window):
        if not win_main_window.objectName():
            win_main_window.setObjectName(u"win_main_window")
        win_main_window.resize(1024, 768)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(win_main_window.sizePolicy().hasHeightForWidth())
        win_main_window.setSizePolicy(sizePolicy)
        self.mac_info = QAction(win_main_window)
        self.mac_info.setObjectName(u"mac_info")
        self.mac_exit = QAction(win_main_window)
        self.mac_exit.setObjectName(u"mac_exit")
        self.mac_read_pre_ct = QAction(win_main_window)
        self.mac_read_pre_ct.setObjectName(u"mac_read_pre_ct")
        self.mac_read_xray = QAction(win_main_window)
        self.mac_read_xray.setObjectName(u"mac_read_xray")
        self.mac_read_intra_ct = QAction(win_main_window)
        self.mac_read_intra_ct.setObjectName(u"mac_read_intra_ct")
        self.mac_write_pre_drr = QAction(win_main_window)
        self.mac_write_pre_drr.setObjectName(u"mac_write_pre_drr")
        self.mac_write_intra_drr = QAction(win_main_window)
        self.mac_write_intra_drr.setObjectName(u"mac_write_intra_drr")
        self.mac_gen_drr = QAction(win_main_window)
        self.mac_gen_drr.setObjectName(u"mac_gen_drr")
        self.actionIntraopera_n_CT = QAction(win_main_window)
        self.actionIntraopera_n_CT.setObjectName(u"actionIntraopera_n_CT")
        self.mac_read_drr = QAction(win_main_window)
        self.mac_read_drr.setObjectName(u"mac_read_drr")
        self.mac_read_drr.setMenuRole(QAction.TextHeuristicRole)
        self.lay_main_layout = QWidget(win_main_window)
        self.lay_main_layout.setObjectName(u"lay_main_layout")
        self.gridLayout = QGridLayout(self.lay_main_layout)
        self.gridLayout.setObjectName(u"gridLayout")
        self.grb_info = QGroupBox(self.lay_main_layout)
        self.grb_info.setObjectName(u"grb_info")
        self.gridLayout_2 = QGridLayout(self.grb_info)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.cob_visualization = QComboBox(self.grb_info)
        self.cob_visualization.addItem("")
        self.cob_visualization.addItem("")
        self.cob_visualization.addItem("")
        self.cob_visualization.addItem("")
        self.cob_visualization.setObjectName(u"cob_visualization")
        self.cob_visualization.setMinimumSize(QSize(130, 0))

        self.gridLayout_2.addWidget(self.cob_visualization, 0, 1, 2, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 0, 2, 1, 1)

        self.label_2 = QLabel(self.grb_info)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(75, 16777215))

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.grb_info, 1, 0, 1, 2)

        self.gvi_drr = GraphicsView(self.lay_main_layout)
        self.gvi_drr.setObjectName(u"gvi_drr")
        self.gvi_drr.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.gvi_drr.sizePolicy().hasHeightForWidth())
        self.gvi_drr.setSizePolicy(sizePolicy1)
        self.gvi_drr.setMinimumSize(QSize(512, 512))
        self.gvi_drr.setMouseTracking(False)
        self.gvi_drr.setFrameShape(QFrame.NoFrame)
        self.gvi_drr.setFrameShadow(QFrame.Plain)
        self.gvi_drr.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.gvi_drr.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.gvi_drr.setDragMode(QGraphicsView.NoDrag)
        self.gvi_drr.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)

        self.gridLayout.addWidget(self.gvi_drr, 0, 2, 2, 2)

        self.tob_main = QToolBox(self.lay_main_layout)
        self.tob_main.setObjectName(u"tob_main")
        sizePolicy.setHeightForWidth(self.tob_main.sizePolicy().hasHeightForWidth())
        self.tob_main.setSizePolicy(sizePolicy)
        self.tob_main.setFrameShape(QFrame.Panel)
        self.tob_main.setFrameShadow(QFrame.Sunken)
        self.page_drr = QWidget()
        self.page_drr.setObjectName(u"page_drr")
        self.page_drr.setGeometry(QRect(0, 0, 486, 610))
        sizePolicy.setHeightForWidth(self.page_drr.sizePolicy().hasHeightForWidth())
        self.page_drr.setSizePolicy(sizePolicy)
        self.page_drr.setAcceptDrops(False)
        self.gridLayout_3 = QGridLayout(self.page_drr)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_7 = QLabel(self.page_drr)
        self.label_7.setObjectName(u"label_7")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy2)
        self.label_7.setMinimumSize(QSize(65, 20))

        self.gridLayout_3.addWidget(self.label_7, 6, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 13, 0, 1, 1)

        self.lineEdit = QLineEdit(self.page_drr)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(50, 60))

        self.gridLayout_3.addWidget(self.lineEdit, 4, 1, 1, 1)

        self.comboBox = QComboBox(self.page_drr)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMaximumSize(QSize(120, 16777215))

        self.gridLayout_3.addWidget(self.comboBox, 8, 1, 1, 1)

        self.checkBox = QCheckBox(self.page_drr)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout_3.addWidget(self.checkBox, 7, 1, 1, 1)

        self.lineEdit_3 = QLineEdit(self.page_drr)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMaximumSize(QSize(50, 30))

        self.gridLayout_3.addWidget(self.lineEdit_3, 6, 1, 1, 1)

        self.lineEdit_4 = QLineEdit(self.page_drr)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMaximumSize(QSize(50, 25))

        self.gridLayout_3.addWidget(self.lineEdit_4, 9, 2, 1, 1)

        self.label_10 = QLabel(self.page_drr)
        self.label_10.setObjectName(u"label_10")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy3)
        self.label_10.setMinimumSize(QSize(65, 20))
        self.label_10.setTextFormat(Qt.AutoText)
        self.label_10.setWordWrap(True)
        self.label_10.setMargin(0)

        self.gridLayout_3.addWidget(self.label_10, 9, 0, 1, 2)

        self.pushButton = QPushButton(self.page_drr)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(100, 25))
        self.pushButton.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_3.addWidget(self.pushButton, 9, 3, 1, 1)

        self.label_22 = QLabel(self.page_drr)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_22, 0, 3, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 15, 0, 1, 4)

        self.label_3 = QLabel(self.page_drr)
        self.label_3.setObjectName(u"label_3")
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)
        self.label_3.setMinimumSize(QSize(65, 20))

        self.gridLayout_3.addWidget(self.label_3, 4, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.page_drr)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMaximumSize(QSize(50, 16777215))
        self.lineEdit_2.setFrame(True)

        self.gridLayout_3.addWidget(self.lineEdit_2, 5, 1, 1, 1)

        self.label_6 = QLabel(self.page_drr)
        self.label_6.setObjectName(u"label_6")
        sizePolicy2.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy2)
        self.label_6.setMinimumSize(QSize(65, 20))

        self.gridLayout_3.addWidget(self.label_6, 0, 0, 1, 1)

        self.label_4 = QLabel(self.page_drr)
        self.label_4.setObjectName(u"label_4")
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)
        self.label_4.setMinimumSize(QSize(65, 20))

        self.gridLayout_3.addWidget(self.label_4, 5, 0, 1, 1)

        self.label_8 = QLabel(self.page_drr)
        self.label_8.setObjectName(u"label_8")
        sizePolicy2.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy2)
        self.label_8.setMinimumSize(QSize(65, 20))

        self.gridLayout_3.addWidget(self.label_8, 7, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.page_drr)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_5 = QGridLayout(self.groupBox_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_5.addWidget(self.label_9, 1, 0, 1, 1)

        self.label_13 = QLabel(self.groupBox_2)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_5.addWidget(self.label_13, 3, 0, 1, 1)

        self.label_11 = QLabel(self.groupBox_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_5.addWidget(self.label_11, 1, 1, 1, 1)

        self.label_15 = QLabel(self.groupBox_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(20, 20))
        self.label_15.setMaximumSize(QSize(20, 20))
        font = QFont()
        font.setBold(True)
        self.label_15.setFont(font)

        self.gridLayout_5.addWidget(self.label_15, 3, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_2, 2, 2, 2, 1)


        self.gridLayout_3.addWidget(self.groupBox_2, 12, 0, 1, 3)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 10, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 3, 3, 6, 1)

        self.label_5 = QLabel(self.page_drr)
        self.label_5.setObjectName(u"label_5")
        sizePolicy2.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy2)
        self.label_5.setMinimumSize(QSize(65, 20))

        self.gridLayout_3.addWidget(self.label_5, 8, 0, 1, 1)

        self.radioButton = QRadioButton(self.page_drr)
        self.radioButton.setObjectName(u"radioButton")

        self.gridLayout_3.addWidget(self.radioButton, 0, 1, 1, 1)

        self.groupBox_3 = QGroupBox(self.page_drr)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_6 = QGridLayout(self.groupBox_3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_3, 0, 4, 2, 1)

        self.label_14 = QLabel(self.groupBox_3)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_6.addWidget(self.label_14, 1, 0, 1, 1)

        self.label_12 = QLabel(self.groupBox_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_6.addWidget(self.label_12, 0, 1, 1, 1)

        self.label_16 = QLabel(self.groupBox_3)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(20, 20))
        self.label_16.setMaximumSize(QSize(20, 20))
        self.label_16.setFont(font)

        self.gridLayout_6.addWidget(self.label_16, 1, 1, 1, 1)

        self.label_17 = QLabel(self.groupBox_3)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_6.addWidget(self.label_17, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_3, 14, 0, 1, 3)

        self.label_23 = QLabel(self.page_drr)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_23, 1, 3, 1, 1)

        self.radioButton_2 = QRadioButton(self.page_drr)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.gridLayout_3.addWidget(self.radioButton_2, 1, 1, 1, 1)

        self.tob_main.addItem(self.page_drr, u"Generace DRR obrazu")
        self.page_registration = QWidget()
        self.page_registration.setObjectName(u"page_registration")
        self.page_registration.setGeometry(QRect(0, 0, 486, 610))
        self.pushButton_2 = QPushButton(self.page_registration)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(110, 70, 75, 25))
        self.pushButton_2.setMinimumSize(QSize(0, 25))
        self.comboBox_2 = QComboBox(self.page_registration)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(80, 30, 111, 22))
        self.label = QLabel(self.page_registration)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 30, 49, 16))
        self.tob_main.addItem(self.page_registration, u"Registrace obraz\u016f")

        self.gridLayout.addWidget(self.tob_main, 0, 0, 1, 2)

        win_main_window.setCentralWidget(self.lay_main_layout)
        self.mba_main_menu = QMenuBar(win_main_window)
        self.mba_main_menu.setObjectName(u"mba_main_menu")
        self.mba_main_menu.setGeometry(QRect(0, 0, 1024, 22))
        self.men_file = QMenu(self.mba_main_menu)
        self.men_file.setObjectName(u"men_file")
        self.men_read = QMenu(self.men_file)
        self.men_read.setObjectName(u"men_read")
        self.men_read.setTearOffEnabled(False)
        self.men_read.setSeparatorsCollapsible(False)
        self.men_write = QMenu(self.men_file)
        self.men_write.setObjectName(u"men_write")
        win_main_window.setMenuBar(self.mba_main_menu)

        self.mba_main_menu.addAction(self.men_file.menuAction())
        self.men_file.addAction(self.men_read.menuAction())
        self.men_file.addAction(self.men_write.menuAction())
        self.men_file.addAction(self.mac_info)
        self.men_file.addSeparator()
        self.men_file.addAction(self.mac_exit)
        self.men_read.addAction(self.mac_read_pre_ct)
        self.men_read.addAction(self.mac_read_intra_ct)
        self.men_read.addAction(self.mac_read_drr)
        self.men_write.addAction(self.mac_write_pre_drr)
        self.men_write.addAction(self.mac_write_intra_drr)

        self.retranslateUi(win_main_window)

        self.tob_main.setCurrentIndex(0)
        self.tob_main.layout().setSpacing(2)


        QMetaObject.connectSlotsByName(win_main_window)
    # setupUi

    def retranslateUi(self, win_main_window):
        win_main_window.setWindowTitle(QCoreApplication.translate("win_main_window", u"Casif", None))
        self.mac_info.setText(QCoreApplication.translate("win_main_window", u"Informace", None))
        self.mac_exit.setText(QCoreApplication.translate("win_main_window", u"Ukon\u010dit", None))
        self.mac_read_pre_ct.setText(QCoreApplication.translate("win_main_window", u"P\u0159edopera\u010dn\u00ed CT pl\u00e1n", None))
        self.mac_read_xray.setText(QCoreApplication.translate("win_main_window", u"RTG obraz", None))
        self.mac_read_intra_ct.setText(QCoreApplication.translate("win_main_window", u"Intraopera\u010dn\u00ed CT", None))
        self.mac_write_pre_drr.setText(QCoreApplication.translate("win_main_window", u"P\u0159edopera\u010dn\u00ed DRR", None))
        self.mac_write_intra_drr.setText(QCoreApplication.translate("win_main_window", u"Intraopera\u010dn\u00ed DRR", None))
        self.mac_gen_drr.setText(QCoreApplication.translate("win_main_window", u"Vytvo\u0159it DRR obraz", None))
        self.actionIntraopera_n_CT.setText(QCoreApplication.translate("win_main_window", u"Intraopera\u010dn\u00ed CT", None))
        self.mac_read_drr.setText(QCoreApplication.translate("win_main_window", u"DRR obraz", None))
        self.grb_info.setTitle(QCoreApplication.translate("win_main_window", u"Informace o obrazech", None))
        self.cob_visualization.setItemText(0, QCoreApplication.translate("win_main_window", u"Preopera\u010dn\u00ed DRR", None))
        self.cob_visualization.setItemText(1, QCoreApplication.translate("win_main_window", u"Intraopera\u010dn\u00ed DRR", None))
        self.cob_visualization.setItemText(2, QCoreApplication.translate("win_main_window", u"Preop + Intraop hrany", None))
        self.cob_visualization.setItemText(3, QCoreApplication.translate("win_main_window", u"\u0160achovnice", None))

        self.label_2.setText(QCoreApplication.translate("win_main_window", u"Zobrazen\u00ed:", None))
        self.label_7.setText(QCoreApplication.translate("win_main_window", u"Pr\u00e1h [HU]:", None))
        self.lineEdit.setInputMask("")
        self.lineEdit.setText(QCoreApplication.translate("win_main_window", u"1024", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("win_main_window", u"P\u0159edozadn\u00ed (AP)", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("win_main_window", u"Bo\u010dn\u00ed zleva", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("win_main_window", u"Bo\u010dn\u00ed zprava", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("win_main_window", u"P\u00e1nevn\u00ed vstup", None))

        self.checkBox.setText("")
        self.lineEdit_3.setText(QCoreApplication.translate("win_main_window", u"200", None))
        self.lineEdit_4.setText(QCoreApplication.translate("win_main_window", u"1000.0", None))
        self.label_10.setText(QCoreApplication.translate("win_main_window", u"Vzd\u00e1lenost zdroj-detektor [mm]:", None))
        self.pushButton.setText(QCoreApplication.translate("win_main_window", u"Vytvo\u0159it DRR", None))
        self.label_22.setText(QCoreApplication.translate("win_main_window", u"---", None))
        self.label_3.setText(QCoreApplication.translate("win_main_window", u"\u0160\u00ed\u0159ka [px]:", None))
        self.lineEdit_2.setText(QCoreApplication.translate("win_main_window", u"1024", None))
        self.label_6.setText(QCoreApplication.translate("win_main_window", u"CT zdroj:", None))
        self.label_4.setText(QCoreApplication.translate("win_main_window", u"V\u00fd\u0161ka [px]:", None))
        self.label_8.setText(QCoreApplication.translate("win_main_window", u"Inverze \u0161edi:", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("win_main_window", u"P\u0159edopera\u010dn\u00ed data", None))
        self.label_9.setText(QCoreApplication.translate("win_main_window", u"N\u00e1zev CT:", None))
        self.label_13.setText(QCoreApplication.translate("win_main_window", u"Vytvo\u0159eno DRR:", None))
        self.label_11.setText(QCoreApplication.translate("win_main_window", u"---", None))
        self.label_15.setText("")
        self.label_5.setText(QCoreApplication.translate("win_main_window", u"Pohled:", None))
        self.radioButton.setText(QCoreApplication.translate("win_main_window", u"P\u0159edopera\u010dn\u00ed", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("win_main_window", u"Intraopera\u010dn\u00ed data", None))
        self.label_14.setText(QCoreApplication.translate("win_main_window", u"Vytvo\u0159eno DRR:", None))
        self.label_12.setText(QCoreApplication.translate("win_main_window", u"---", None))
        self.label_16.setText("")
        self.label_17.setText(QCoreApplication.translate("win_main_window", u"N\u00e1zev CT:", None))
        self.label_23.setText(QCoreApplication.translate("win_main_window", u"---", None))
        self.radioButton_2.setText(QCoreApplication.translate("win_main_window", u"Intraopera\u010dn\u00ed", None))
        self.tob_main.setItemText(self.tob_main.indexOf(self.page_drr), QCoreApplication.translate("win_main_window", u"Generace DRR obrazu", None))
        self.pushButton_2.setText(QCoreApplication.translate("win_main_window", u"Spustit", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("win_main_window", u"Metoda 1", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("win_main_window", u"Metoda 2", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("win_main_window", u"Metoda 3", None))

        self.label.setText(QCoreApplication.translate("win_main_window", u"Metoda:", None))
        self.tob_main.setItemText(self.tob_main.indexOf(self.page_registration), QCoreApplication.translate("win_main_window", u"Registrace obraz\u016f", None))
        self.men_file.setTitle(QCoreApplication.translate("win_main_window", u"Soubor", None))
        self.men_read.setTitle(QCoreApplication.translate("win_main_window", u"Otev\u0159\u00edt", None))
        self.men_write.setTitle(QCoreApplication.translate("win_main_window", u"Ulo\u017eit", None))
    # retranslateUi

