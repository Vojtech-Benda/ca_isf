# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window_alt.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            QSize, Qt)
from PySide6.QtGui import (QAction, QFont)
from PySide6.QtWidgets import (QAbstractScrollArea, QCheckBox, QComboBox,
                               QFrame, QGraphicsView, QGridLayout, QGroupBox,
                               QLabel, QLineEdit, QMenu,
                               QMenuBar, QPushButton, QRadioButton, QSizePolicy,
                               QSpacerItem, QToolBox, QWidget)

from casif_app.ui.custom_widgets import GraphicsView

class Ui_win_main_window(object):
    def setupUi(self, win_main_window):
        if not win_main_window.objectName():
            win_main_window.setObjectName(u"win_main_window")
        win_main_window.resize(1200, 768)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(win_main_window.sizePolicy().hasHeightForWidth())
        win_main_window.setSizePolicy(sizePolicy)
        win_main_window.setMinimumSize(QSize(1200, 768))
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
        self.tob_main = QToolBox(self.lay_main_layout)
        self.tob_main.setObjectName(u"tob_main")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tob_main.sizePolicy().hasHeightForWidth())
        self.tob_main.setSizePolicy(sizePolicy1)
        self.tob_main.setMinimumSize(QSize(375, 0))
        self.tob_main.setMaximumSize(QSize(16777215, 16777215))
        self.tob_main.setFrameShape(QFrame.Panel)
        self.tob_main.setFrameShadow(QFrame.Sunken)
        self.pag_drr = QWidget()
        self.pag_drr.setObjectName(u"pag_drr")
        self.pag_drr.setGeometry(QRect(0, 0, 373, 588))
        sizePolicy.setHeightForWidth(self.pag_drr.sizePolicy().hasHeightForWidth())
        self.pag_drr.setSizePolicy(sizePolicy)
        self.pag_drr.setAcceptDrops(False)
        self.gridLayout_3 = QGridLayout(self.pag_drr)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lab_thresh = QLabel(self.pag_drr)
        self.lab_thresh.setObjectName(u"lab_thresh")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lab_thresh.sizePolicy().hasHeightForWidth())
        self.lab_thresh.setSizePolicy(sizePolicy2)
        self.lab_thresh.setMinimumSize(QSize(65, 20))

        self.gridLayout_3.addWidget(self.lab_thresh, 6, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 13, 0, 1, 1)

        self.led_drr_width = QLineEdit(self.pag_drr)
        self.led_drr_width.setObjectName(u"led_drr_width")
        self.led_drr_width.setMaximumSize(QSize(50, 60))

        self.gridLayout_3.addWidget(self.led_drr_width, 4, 1, 1, 1)

        self.cbo_drr_view = QComboBox(self.pag_drr)
        self.cbo_drr_view.addItem("")
        self.cbo_drr_view.addItem("")
        self.cbo_drr_view.addItem("")
        self.cbo_drr_view.addItem("")
        self.cbo_drr_view.setObjectName(u"cbo_drr_view")
        self.cbo_drr_view.setMaximumSize(QSize(120, 16777215))

        self.gridLayout_3.addWidget(self.cbo_drr_view, 8, 1, 1, 1)

        self.cbo_inverse_gray = QCheckBox(self.pag_drr)
        self.cbo_inverse_gray.setObjectName(u"cbo_inverse_gray")

        self.gridLayout_3.addWidget(self.cbo_inverse_gray, 7, 1, 1, 1)

        self.led_drr_thresh = QLineEdit(self.pag_drr)
        self.led_drr_thresh.setObjectName(u"led_drr_thresh")
        self.led_drr_thresh.setMaximumSize(QSize(50, 30))

        self.gridLayout_3.addWidget(self.led_drr_thresh, 6, 1, 1, 1)

        self.led_sid = QLineEdit(self.pag_drr)
        self.led_sid.setObjectName(u"led_sid")
        self.led_sid.setMaximumSize(QSize(50, 25))

        self.gridLayout_3.addWidget(self.led_sid, 9, 2, 1, 1)

        self.lab_sid = QLabel(self.pag_drr)
        self.lab_sid.setObjectName(u"lab_sid")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lab_sid.sizePolicy().hasHeightForWidth())
        self.lab_sid.setSizePolicy(sizePolicy3)
        self.lab_sid.setMinimumSize(QSize(65, 20))
        self.lab_sid.setTextFormat(Qt.AutoText)
        self.lab_sid.setWordWrap(True)
        self.lab_sid.setMargin(0)

        self.gridLayout_3.addWidget(self.lab_sid, 9, 0, 1, 2)

        self.pbu_drr_start = QPushButton(self.pag_drr)
        self.pbu_drr_start.setObjectName(u"pbu_drr_start")
        self.pbu_drr_start.setMinimumSize(QSize(100, 25))
        self.pbu_drr_start.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_3.addWidget(self.pbu_drr_start, 9, 3, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 15, 0, 1, 4)

        self.lab_drr_width = QLabel(self.pag_drr)
        self.lab_drr_width.setObjectName(u"lab_drr_width")
        sizePolicy2.setHeightForWidth(self.lab_drr_width.sizePolicy().hasHeightForWidth())
        self.lab_drr_width.setSizePolicy(sizePolicy2)
        self.lab_drr_width.setMinimumSize(QSize(65, 20))

        self.gridLayout_3.addWidget(self.lab_drr_width, 4, 0, 1, 1)

        self.led_drr_height = QLineEdit(self.pag_drr)
        self.led_drr_height.setObjectName(u"led_drr_height")
        self.led_drr_height.setMaximumSize(QSize(50, 16777215))
        self.led_drr_height.setFrame(True)

        self.gridLayout_3.addWidget(self.led_drr_height, 5, 1, 1, 1)

        self.lab_ct_source = QLabel(self.pag_drr)
        self.lab_ct_source.setObjectName(u"lab_ct_source")
        sizePolicy2.setHeightForWidth(self.lab_ct_source.sizePolicy().hasHeightForWidth())
        self.lab_ct_source.setSizePolicy(sizePolicy2)
        self.lab_ct_source.setMinimumSize(QSize(65, 20))

        self.gridLayout_3.addWidget(self.lab_ct_source, 0, 0, 1, 1)

        self.lab_drr_height = QLabel(self.pag_drr)
        self.lab_drr_height.setObjectName(u"lab_drr_height")
        sizePolicy2.setHeightForWidth(self.lab_drr_height.sizePolicy().hasHeightForWidth())
        self.lab_drr_height.setSizePolicy(sizePolicy2)
        self.lab_drr_height.setMinimumSize(QSize(65, 20))

        self.gridLayout_3.addWidget(self.lab_drr_height, 5, 0, 1, 1)

        self.lab_inverse_gray = QLabel(self.pag_drr)
        self.lab_inverse_gray.setObjectName(u"lab_inverse_gray")
        sizePolicy2.setHeightForWidth(self.lab_inverse_gray.sizePolicy().hasHeightForWidth())
        self.lab_inverse_gray.setSizePolicy(sizePolicy2)
        self.lab_inverse_gray.setMinimumSize(QSize(65, 20))

        self.gridLayout_3.addWidget(self.lab_inverse_gray, 7, 0, 1, 1)

        self.gbo_preop_info = QGroupBox(self.pag_drr)
        self.gbo_preop_info.setObjectName(u"gbo_preop_info")
        self.gridLayout_5 = QGridLayout(self.gbo_preop_info)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.lab_pre_ct_name = QLabel(self.gbo_preop_info)
        self.lab_pre_ct_name.setObjectName(u"lab_pre_ct_name")
        self.lab_pre_ct_name.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_5.addWidget(self.lab_pre_ct_name, 1, 0, 1, 1)

        self.lab_pre_drr_created = QLabel(self.gbo_preop_info)
        self.lab_pre_drr_created.setObjectName(u"lab_pre_drr_created")

        self.gridLayout_5.addWidget(self.lab_pre_drr_created, 3, 0, 1, 1)

        self.labm_pre_drr_created = QLabel(self.gbo_preop_info)
        self.labm_pre_drr_created.setObjectName(u"labm_pre_drr_created")
        self.labm_pre_drr_created.setMinimumSize(QSize(20, 20))
        self.labm_pre_drr_created.setMaximumSize(QSize(20, 20))
        font = QFont()
        font.setBold(True)
        self.labm_pre_drr_created.setFont(font)

        self.gridLayout_5.addWidget(self.labm_pre_drr_created, 3, 1, 1, 1)

        self.labm_pre_ct_name = QLabel(self.gbo_preop_info)
        self.labm_pre_ct_name.setObjectName(u"labm_pre_ct_name")
        self.labm_pre_ct_name.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_5.addWidget(self.labm_pre_ct_name, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_2, 1, 2, 3, 1)


        self.gridLayout_3.addWidget(self.gbo_preop_info, 12, 0, 1, 3)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 10, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 3, 3, 6, 1)

        self.lab_drr_view = QLabel(self.pag_drr)
        self.lab_drr_view.setObjectName(u"lab_drr_view")
        sizePolicy2.setHeightForWidth(self.lab_drr_view.sizePolicy().hasHeightForWidth())
        self.lab_drr_view.setSizePolicy(sizePolicy2)
        self.lab_drr_view.setMinimumSize(QSize(65, 20))

        self.gridLayout_3.addWidget(self.lab_drr_view, 8, 0, 1, 1)

        self.rbu_preop = QRadioButton(self.pag_drr)
        self.rbu_preop.setObjectName(u"rbu_preop")
        self.rbu_preop.setChecked(True)

        self.gridLayout_3.addWidget(self.rbu_preop, 0, 1, 1, 1)

        self.gbo_intraop_info = QGroupBox(self.pag_drr)
        self.gbo_intraop_info.setObjectName(u"gbo_intraop_info")
        self.gridLayout_6 = QGridLayout(self.gbo_intraop_info)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_3, 0, 4, 2, 1)

        self.lab_intra_drr_created = QLabel(self.gbo_intraop_info)
        self.lab_intra_drr_created.setObjectName(u"lab_intra_drr_created")

        self.gridLayout_6.addWidget(self.lab_intra_drr_created, 1, 0, 1, 1)

        self.labm_intra_ct_name = QLabel(self.gbo_intraop_info)
        self.labm_intra_ct_name.setObjectName(u"labm_intra_ct_name")
        self.labm_intra_ct_name.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_6.addWidget(self.labm_intra_ct_name, 0, 1, 1, 1)

        self.labm_intra_drr_created = QLabel(self.gbo_intraop_info)
        self.labm_intra_drr_created.setObjectName(u"labm_intra_drr_created")
        self.labm_intra_drr_created.setMinimumSize(QSize(20, 20))
        self.labm_intra_drr_created.setMaximumSize(QSize(20, 20))
        self.labm_intra_drr_created.setFont(font)

        self.gridLayout_6.addWidget(self.labm_intra_drr_created, 1, 1, 1, 1)

        self.lab_intra_ct_name = QLabel(self.gbo_intraop_info)
        self.lab_intra_ct_name.setObjectName(u"lab_intra_ct_name")
        self.lab_intra_ct_name.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_6.addWidget(self.lab_intra_ct_name, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.gbo_intraop_info, 14, 0, 1, 3)

        self.labm_intraop_ct_warning = QLabel(self.pag_drr)
        self.labm_intraop_ct_warning.setObjectName(u"labm_intraop_ct_warning")
        self.labm_intraop_ct_warning.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.labm_intraop_ct_warning, 1, 3, 1, 1)

        self.rbu_intraop = QRadioButton(self.pag_drr)
        self.rbu_intraop.setObjectName(u"rbu_intraop")

        self.gridLayout_3.addWidget(self.rbu_intraop, 1, 1, 1, 1)

        self.labm_preop_ct_warning = QLabel(self.pag_drr)
        self.labm_preop_ct_warning.setObjectName(u"labm_preop_ct_warning")
        self.labm_preop_ct_warning.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.labm_preop_ct_warning, 0, 3, 1, 1)

        self.tob_main.addItem(self.pag_drr, u"Generace DRR obrazu")
        self.pag_reg = QWidget()
        self.pag_reg.setObjectName(u"pag_reg")
        self.pag_reg.setGeometry(QRect(0, 0, 373, 588))
        self.pbu_reg_start = QPushButton(self.pag_reg)
        self.pbu_reg_start.setObjectName(u"pbu_reg_start")
        self.pbu_reg_start.setGeometry(QRect(110, 70, 75, 25))
        self.pbu_reg_start.setMinimumSize(QSize(0, 25))
        self.cob_reg_method = QComboBox(self.pag_reg)
        self.cob_reg_method.addItem("")
        self.cob_reg_method.addItem("")
        self.cob_reg_method.addItem("")
        self.cob_reg_method.setObjectName(u"cob_reg_method")
        self.cob_reg_method.setGeometry(QRect(80, 30, 111, 22))
        self.lab_reg_method = QLabel(self.pag_reg)
        self.lab_reg_method.setObjectName(u"lab_reg_method")
        self.lab_reg_method.setGeometry(QRect(30, 30, 49, 16))
        self.tob_main.addItem(self.pag_reg, u"Registrace obraz\u016f")

        self.gridLayout.addWidget(self.tob_main, 0, 0, 1, 2)

        self.gbo_image_info = QGroupBox(self.lay_main_layout)
        self.gbo_image_info.setObjectName(u"gbo_image_info")
        self.gbo_image_info.setMaximumSize(QSize(450, 16777215))
        self.gridLayout_2 = QGridLayout(self.gbo_image_info)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lab_visualization = QLabel(self.gbo_image_info)
        self.lab_visualization.setObjectName(u"lab_visualization")
        self.lab_visualization.setMaximumSize(QSize(60, 16777215))

        self.gridLayout_2.addWidget(self.lab_visualization, 0, 0, 1, 1)

        self.labm_vis_warning = QLabel(self.gbo_image_info)
        self.labm_vis_warning.setObjectName(u"labm_vis_warning")

        self.gridLayout_2.addWidget(self.labm_vis_warning, 2, 1, 1, 2)

        self.cbo_visualization = QComboBox(self.gbo_image_info)
        self.cbo_visualization.addItem("")
        self.cbo_visualization.addItem("")
        self.cbo_visualization.addItem("")
        self.cbo_visualization.addItem("")
        self.cbo_visualization.setObjectName(u"cbo_visualization")
        sizePolicy.setHeightForWidth(self.cbo_visualization.sizePolicy().hasHeightForWidth())
        self.cbo_visualization.setSizePolicy(sizePolicy)
        self.cbo_visualization.setMinimumSize(QSize(130, 0))
        self.cbo_visualization.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_2.addWidget(self.cbo_visualization, 0, 1, 2, 1)


        self.gridLayout.addWidget(self.gbo_image_info, 1, 0, 1, 2)

        self.gvi_drr = GraphicsView(self.lay_main_layout)
        self.gvi_drr.setObjectName(u"gvi_drr")
        self.gvi_drr.setEnabled(True)
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.gvi_drr.sizePolicy().hasHeightForWidth())
        self.gvi_drr.setSizePolicy(sizePolicy4)
        self.gvi_drr.setMinimumSize(QSize(512, 512))
        self.gvi_drr.setMouseTracking(False)
        self.gvi_drr.setFrameShape(QFrame.NoFrame)
        self.gvi_drr.setFrameShadow(QFrame.Plain)
        self.gvi_drr.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.gvi_drr.setAlignment(Qt.AlignCenter)
        self.gvi_drr.setDragMode(QGraphicsView.NoDrag)
        self.gvi_drr.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)

        self.gridLayout.addWidget(self.gvi_drr, 0, 3, 2, 1)

        self.horizontalSpacer_4 = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 0, 2, 2, 1)

        win_main_window.setCentralWidget(self.lay_main_layout)
        self.mba_main_menu = QMenuBar(win_main_window)
        self.mba_main_menu.setObjectName(u"mba_main_menu")
        self.mba_main_menu.setGeometry(QRect(0, 0, 1200, 22))
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
        self.lab_thresh.setText(QCoreApplication.translate("win_main_window", u"Pr\u00e1h [HU]:", None))
        self.led_drr_width.setInputMask("")
        self.led_drr_width.setText(QCoreApplication.translate("win_main_window", u"512", None))
        self.cbo_drr_view.setItemText(0, QCoreApplication.translate("win_main_window", u"P\u0159edozadn\u00ed (AP)", None))
        self.cbo_drr_view.setItemText(1, QCoreApplication.translate("win_main_window", u"Bo\u010dn\u00ed zleva", None))
        self.cbo_drr_view.setItemText(2, QCoreApplication.translate("win_main_window", u"Bo\u010dn\u00ed zprava", None))
        self.cbo_drr_view.setItemText(3, QCoreApplication.translate("win_main_window", u"P\u00e1nevn\u00ed vstup", None))

        self.cbo_inverse_gray.setText("")
        self.led_drr_thresh.setText(QCoreApplication.translate("win_main_window", u"200", None))
        self.led_sid.setText(QCoreApplication.translate("win_main_window", u"1000.0", None))
        self.lab_sid.setText(QCoreApplication.translate("win_main_window", u"Vzd\u00e1lenost zdroj-detektor [mm]:", None))
        self.pbu_drr_start.setText(QCoreApplication.translate("win_main_window", u"Vytvo\u0159it DRR", None))
        self.lab_drr_width.setText(QCoreApplication.translate("win_main_window", u"\u0160\u00ed\u0159ka [px]:", None))
        self.led_drr_height.setText(QCoreApplication.translate("win_main_window", u"512", None))
        self.lab_ct_source.setText(QCoreApplication.translate("win_main_window", u"CT zdroj:", None))
        self.lab_drr_height.setText(QCoreApplication.translate("win_main_window", u"V\u00fd\u0161ka [px]:", None))
        self.lab_inverse_gray.setText(QCoreApplication.translate("win_main_window", u"Inverze \u0161edi:", None))
        self.gbo_preop_info.setTitle(QCoreApplication.translate("win_main_window", u"P\u0159edopera\u010dn\u00ed data", None))
        self.lab_pre_ct_name.setText(QCoreApplication.translate("win_main_window", u"N\u00e1zev CT:", None))
        self.lab_pre_drr_created.setText(QCoreApplication.translate("win_main_window", u"Vytvo\u0159eno DRR:", None))
        self.labm_pre_drr_created.setText("")
        self.labm_pre_ct_name.setText(QCoreApplication.translate("win_main_window", u"---", None))
        self.lab_drr_view.setText(QCoreApplication.translate("win_main_window", u"Pohled:", None))
        self.rbu_preop.setText(QCoreApplication.translate("win_main_window", u"P\u0159edopera\u010dn\u00ed", None))
        self.gbo_intraop_info.setTitle(QCoreApplication.translate("win_main_window", u"Intraopera\u010dn\u00ed data", None))
        self.lab_intra_drr_created.setText(QCoreApplication.translate("win_main_window", u"Vytvo\u0159eno DRR:", None))
        self.labm_intra_ct_name.setText(QCoreApplication.translate("win_main_window", u"---", None))
        self.labm_intra_drr_created.setText("")
        self.lab_intra_ct_name.setText(QCoreApplication.translate("win_main_window", u"N\u00e1zev CT:", None))
        self.labm_intraop_ct_warning.setText(QCoreApplication.translate("win_main_window", u"---", None))
        self.rbu_intraop.setText(QCoreApplication.translate("win_main_window", u"Intraopera\u010dn\u00ed", None))
        self.labm_preop_ct_warning.setText(QCoreApplication.translate("win_main_window", u"---", None))
        self.tob_main.setItemText(self.tob_main.indexOf(self.pag_drr), QCoreApplication.translate("win_main_window", u"Generace DRR obrazu", None))
        self.pbu_reg_start.setText(QCoreApplication.translate("win_main_window", u"Spustit", None))
        self.cob_reg_method.setItemText(0, QCoreApplication.translate("win_main_window", u"Metoda 1", None))
        self.cob_reg_method.setItemText(1, QCoreApplication.translate("win_main_window", u"Metoda 2", None))
        self.cob_reg_method.setItemText(2, QCoreApplication.translate("win_main_window", u"Metoda 3", None))

        self.lab_reg_method.setText(QCoreApplication.translate("win_main_window", u"Metoda:", None))
        self.tob_main.setItemText(self.tob_main.indexOf(self.pag_reg), QCoreApplication.translate("win_main_window", u"Registrace obraz\u016f", None))
        self.gbo_image_info.setTitle(QCoreApplication.translate("win_main_window", u"Informace o obrazech", None))
        self.lab_visualization.setText(QCoreApplication.translate("win_main_window", u"Zobrazen\u00ed:", None))
        self.labm_vis_warning.setText(QCoreApplication.translate("win_main_window", u"---", None))
        self.cbo_visualization.setItemText(0, QCoreApplication.translate("win_main_window", u"Preopera\u010dn\u00ed DRR", None))
        self.cbo_visualization.setItemText(1, QCoreApplication.translate("win_main_window", u"Intraopera\u010dn\u00ed DRR", None))
        self.cbo_visualization.setItemText(2, QCoreApplication.translate("win_main_window", u"Preop + Intraop hrany", None))
        self.cbo_visualization.setItemText(3, QCoreApplication.translate("win_main_window", u"\u0160achovnice", None))

        self.men_file.setTitle(QCoreApplication.translate("win_main_window", u"Soubor", None))
        self.men_read.setTitle(QCoreApplication.translate("win_main_window", u"Otev\u0159\u00edt", None))
        self.men_write.setTitle(QCoreApplication.translate("win_main_window", u"Ulo\u017eit", None))
    # retranslateUi

