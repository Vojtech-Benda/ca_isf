# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QGridLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QTabWidget, QTextBrowser,
    QTreeWidget, QTreeWidgetItem, QWidget)

class Ui_win_main_window(object):
    def setupUi(self, win_main_window):
        if not win_main_window.objectName():
            win_main_window.setObjectName(u"win_main_window")
        win_main_window.resize(600, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(win_main_window.sizePolicy().hasHeightForWidth())
        win_main_window.setSizePolicy(sizePolicy)
        win_main_window.setMinimumSize(QSize(600, 600))
        win_main_window.setMaximumSize(QSize(600, 600))
        win_main_window.setToolButtonStyle(Qt.ToolButtonIconOnly)
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
        self.mac_write_preop_drr = QAction(win_main_window)
        self.mac_write_preop_drr.setObjectName(u"mac_write_preop_drr")
        self.mac_write_intraop_drr = QAction(win_main_window)
        self.mac_write_intraop_drr.setObjectName(u"mac_write_intraop_drr")
        self.mac_gen_drr = QAction(win_main_window)
        self.mac_gen_drr.setObjectName(u"mac_gen_drr")
        self.actionIntraopera_n_CT = QAction(win_main_window)
        self.actionIntraopera_n_CT.setObjectName(u"actionIntraopera_n_CT")
        self.mac_read_preop_drr = QAction(win_main_window)
        self.mac_read_preop_drr.setObjectName(u"mac_read_preop_drr")
        self.mac_read_preop_drr.setMenuRole(QAction.TextHeuristicRole)
        self.mac_read_intraop_drr = QAction(win_main_window)
        self.mac_read_intraop_drr.setObjectName(u"mac_read_intraop_drr")
        self.mac_write_registered_drr = QAction(win_main_window)
        self.mac_write_registered_drr.setObjectName(u"mac_write_registered_drr")
        self.actionNov_pacient = QAction(win_main_window)
        self.actionNov_pacient.setObjectName(u"actionNov_pacient")
        self.lay_main_layout = QWidget(win_main_window)
        self.lay_main_layout.setObjectName(u"lay_main_layout")
        self.gridLayout = QGridLayout(self.lay_main_layout)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tbr_output_messages = QTextBrowser(self.lay_main_layout)
        self.tbr_output_messages.setObjectName(u"tbr_output_messages")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tbr_output_messages.sizePolicy().hasHeightForWidth())
        self.tbr_output_messages.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.tbr_output_messages, 2, 0, 2, 3)

        self.twi_data_list = QTreeWidget(self.lay_main_layout)
        QTreeWidgetItem(self.twi_data_list)
        QTreeWidgetItem(self.twi_data_list)
        QTreeWidgetItem(self.twi_data_list)
        QTreeWidgetItem(self.twi_data_list)
        self.twi_data_list.setObjectName(u"twi_data_list")
        sizePolicy1.setHeightForWidth(self.twi_data_list.sizePolicy().hasHeightForWidth())
        self.twi_data_list.setSizePolicy(sizePolicy1)
        self.twi_data_list.setMidLineWidth(0)
        self.twi_data_list.setEditTriggers(QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed)
        self.twi_data_list.setAnimated(False)
        self.twi_data_list.setAllColumnsShowFocus(False)
        self.twi_data_list.setWordWrap(False)
        self.twi_data_list.setHeaderHidden(False)
        self.twi_data_list.header().setVisible(True)
        self.twi_data_list.header().setCascadingSectionResizes(False)
        self.twi_data_list.header().setHighlightSections(False)
        self.twi_data_list.header().setProperty("showSortIndicator", False)

        self.gridLayout.addWidget(self.twi_data_list, 0, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.tab_main = QTabWidget(self.lay_main_layout)
        self.tab_main.setObjectName(u"tab_main")
        sizePolicy.setHeightForWidth(self.tab_main.sizePolicy().hasHeightForWidth())
        self.tab_main.setSizePolicy(sizePolicy)
        self.tab_main.setMinimumSize(QSize(375, 300))
        self.tab_main.setMaximumSize(QSize(375, 300))
        self.tab_main.setAutoFillBackground(False)
        self.tab_main.setUsesScrollButtons(True)
        self.tab_main.setDocumentMode(False)
        self.tab_main.setTabsClosable(False)
        self.tab_main.setMovable(False)
        self.tab_main.setTabBarAutoHide(False)
        self.tab_drr_obrazy = QWidget()
        self.tab_drr_obrazy.setObjectName(u"tab_drr_obrazy")
        self.gridLayout_3 = QGridLayout(self.tab_drr_obrazy)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lab_drr_width = QLabel(self.tab_drr_obrazy)
        self.lab_drr_width.setObjectName(u"lab_drr_width")
        sizePolicy.setHeightForWidth(self.lab_drr_width.sizePolicy().hasHeightForWidth())
        self.lab_drr_width.setSizePolicy(sizePolicy)
        self.lab_drr_width.setMinimumSize(QSize(65, 20))

        self.gridLayout_3.addWidget(self.lab_drr_width, 4, 0, 1, 1)

        self.led_drr_width = QLineEdit(self.tab_drr_obrazy)
        self.led_drr_width.setObjectName(u"led_drr_width")
        self.led_drr_width.setMaximumSize(QSize(50, 60))

        self.gridLayout_3.addWidget(self.led_drr_width, 4, 2, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_5, 6, 3, 1, 1)

        self.lab_sid = QLabel(self.tab_drr_obrazy)
        self.lab_sid.setObjectName(u"lab_sid")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lab_sid.sizePolicy().hasHeightForWidth())
        self.lab_sid.setSizePolicy(sizePolicy2)
        self.lab_sid.setMinimumSize(QSize(65, 20))
        self.lab_sid.setTextFormat(Qt.AutoText)
        self.lab_sid.setWordWrap(True)
        self.lab_sid.setMargin(0)

        self.gridLayout_3.addWidget(self.lab_sid, 6, 0, 1, 2)

        self.rbu_preop_drr = QRadioButton(self.tab_drr_obrazy)
        self.rbu_preop_drr.setObjectName(u"rbu_preop_drr")

        self.gridLayout_3.addWidget(self.rbu_preop_drr, 2, 2, 1, 1)

        self.lab_drr_height = QLabel(self.tab_drr_obrazy)
        self.lab_drr_height.setObjectName(u"lab_drr_height")
        sizePolicy.setHeightForWidth(self.lab_drr_height.sizePolicy().hasHeightForWidth())
        self.lab_drr_height.setSizePolicy(sizePolicy)
        self.lab_drr_height.setMinimumSize(QSize(65, 20))

        self.gridLayout_3.addWidget(self.lab_drr_height, 5, 0, 1, 1)

        self.lab_drr_type = QLabel(self.tab_drr_obrazy)
        self.lab_drr_type.setObjectName(u"lab_drr_type")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lab_drr_type.sizePolicy().hasHeightForWidth())
        self.lab_drr_type.setSizePolicy(sizePolicy3)
        self.lab_drr_type.setMinimumSize(QSize(65, 20))
        self.lab_drr_type.setTextFormat(Qt.AutoText)
        self.lab_drr_type.setWordWrap(True)
        self.lab_drr_type.setMargin(0)

        self.gridLayout_3.addWidget(self.lab_drr_type, 0, 0, 1, 1)

        self.pbu_drr_start = QPushButton(self.tab_drr_obrazy)
        self.pbu_drr_start.setObjectName(u"pbu_drr_start")
        self.pbu_drr_start.setMinimumSize(QSize(100, 25))
        self.pbu_drr_start.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_3.addWidget(self.pbu_drr_start, 10, 0, 1, 1)

        self.led_sid = QLineEdit(self.tab_drr_obrazy)
        self.led_sid.setObjectName(u"led_sid")
        self.led_sid.setMaximumSize(QSize(50, 25))

        self.gridLayout_3.addWidget(self.led_sid, 6, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 11, 0, 1, 1)

        self.rbu_intraop_drr = QRadioButton(self.tab_drr_obrazy)
        self.rbu_intraop_drr.setObjectName(u"rbu_intraop_drr")
        sizePolicy1.setHeightForWidth(self.rbu_intraop_drr.sizePolicy().hasHeightForWidth())
        self.rbu_intraop_drr.setSizePolicy(sizePolicy1)
        self.rbu_intraop_drr.setChecked(True)

        self.gridLayout_3.addWidget(self.rbu_intraop_drr, 0, 2, 1, 1)

        self.led_drr_height = QLineEdit(self.tab_drr_obrazy)
        self.led_drr_height.setObjectName(u"led_drr_height")
        self.led_drr_height.setMaximumSize(QSize(50, 16777215))
        self.led_drr_height.setFrame(True)

        self.gridLayout_3.addWidget(self.led_drr_height, 5, 2, 1, 1)

        self.led_drr_thresh = QLineEdit(self.tab_drr_obrazy)
        self.led_drr_thresh.setObjectName(u"led_drr_thresh")
        self.led_drr_thresh.setMaximumSize(QSize(50, 30))

        self.gridLayout_3.addWidget(self.led_drr_thresh, 7, 2, 1, 1)

        self.lab_ct_thresh = QLabel(self.tab_drr_obrazy)
        self.lab_ct_thresh.setObjectName(u"lab_ct_thresh")
        sizePolicy.setHeightForWidth(self.lab_ct_thresh.sizePolicy().hasHeightForWidth())
        self.lab_ct_thresh.setSizePolicy(sizePolicy)
        self.lab_ct_thresh.setMinimumSize(QSize(65, 20))

        self.gridLayout_3.addWidget(self.lab_ct_thresh, 7, 0, 1, 1)

        self.tab_main.addTab(self.tab_drr_obrazy, "")
        self.tab_reg = QWidget()
        self.tab_reg.setObjectName(u"tab_reg")
        self.gridLayout_4 = QGridLayout(self.tab_reg)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.labm_input_warning = QLabel(self.tab_reg)
        self.labm_input_warning.setObjectName(u"labm_input_warning")

        self.gridLayout_4.addWidget(self.labm_input_warning, 10, 3, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_6, 1, 4, 12, 1)

        self.lab_fixed_drr = QLabel(self.tab_reg)
        self.lab_fixed_drr.setObjectName(u"lab_fixed_drr")

        self.gridLayout_4.addWidget(self.lab_fixed_drr, 1, 0, 1, 1)

        self.lab_optim_method = QLabel(self.tab_reg)
        self.lab_optim_method.setObjectName(u"lab_optim_method")

        self.gridLayout_4.addWidget(self.lab_optim_method, 9, 0, 1, 1)

        self.lab_moving_drr = QLabel(self.tab_reg)
        self.lab_moving_drr.setObjectName(u"lab_moving_drr")

        self.gridLayout_4.addWidget(self.lab_moving_drr, 2, 0, 1, 1)

        self.lab_multires_levels = QLabel(self.tab_reg)
        self.lab_multires_levels.setObjectName(u"lab_multires_levels")

        self.gridLayout_4.addWidget(self.lab_multires_levels, 5, 0, 1, 3)

        self.led_multires_levels = QLineEdit(self.tab_reg)
        self.led_multires_levels.setObjectName(u"led_multires_levels")
        self.led_multires_levels.setMinimumSize(QSize(50, 0))
        self.led_multires_levels.setMaximumSize(QSize(25, 25))
        self.led_multires_levels.setMaxLength(1)

        self.gridLayout_4.addWidget(self.led_multires_levels, 5, 3, 1, 1)

        self.led_lower_edge_thresh = QLineEdit(self.tab_reg)
        self.led_lower_edge_thresh.setObjectName(u"led_lower_edge_thresh")
        self.led_lower_edge_thresh.setMinimumSize(QSize(50, 0))
        self.led_lower_edge_thresh.setMaximumSize(QSize(25, 25))

        self.gridLayout_4.addWidget(self.led_lower_edge_thresh, 11, 3, 1, 1)

        self.lab_lower_edge_thresh = QLabel(self.tab_reg)
        self.lab_lower_edge_thresh.setObjectName(u"lab_lower_edge_thresh")

        self.gridLayout_4.addWidget(self.lab_lower_edge_thresh, 11, 0, 1, 1)

        self.led_upper_edge_thresh = QLineEdit(self.tab_reg)
        self.led_upper_edge_thresh.setObjectName(u"led_upper_edge_thresh")
        self.led_upper_edge_thresh.setMinimumSize(QSize(50, 0))
        self.led_upper_edge_thresh.setMaximumSize(QSize(25, 25))

        self.gridLayout_4.addWidget(self.led_upper_edge_thresh, 12, 3, 1, 1)

        self.cbo_optim_method = QComboBox(self.tab_reg)
        self.cbo_optim_method.addItem("")
        self.cbo_optim_method.addItem("")
        self.cbo_optim_method.addItem("")
        self.cbo_optim_method.setObjectName(u"cbo_optim_method")
        self.cbo_optim_method.setMinimumSize(QSize(0, 25))
        self.cbo_optim_method.setMaxVisibleItems(3)

        self.gridLayout_4.addWidget(self.cbo_optim_method, 9, 3, 1, 1)

        self.lab_sigma_factors = QLabel(self.tab_reg)
        self.lab_sigma_factors.setObjectName(u"lab_sigma_factors")

        self.gridLayout_4.addWidget(self.lab_sigma_factors, 7, 0, 1, 3)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_6, 15, 0, 1, 5)

        self.led_sigma_factors = QLineEdit(self.tab_reg)
        self.led_sigma_factors.setObjectName(u"led_sigma_factors")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.led_sigma_factors.sizePolicy().hasHeightForWidth())
        self.led_sigma_factors.setSizePolicy(sizePolicy4)
        self.led_sigma_factors.setMinimumSize(QSize(75, 0))
        self.led_sigma_factors.setMaximumSize(QSize(100, 25))

        self.gridLayout_4.addWidget(self.led_sigma_factors, 7, 3, 1, 1)

        self.pbu_reg_start = QPushButton(self.tab_reg)
        self.pbu_reg_start.setObjectName(u"pbu_reg_start")
        self.pbu_reg_start.setMinimumSize(QSize(0, 25))

        self.gridLayout_4.addWidget(self.pbu_reg_start, 10, 0, 1, 1)

        self.led_shrink_factors = QLineEdit(self.tab_reg)
        self.led_shrink_factors.setObjectName(u"led_shrink_factors")
        sizePolicy4.setHeightForWidth(self.led_shrink_factors.sizePolicy().hasHeightForWidth())
        self.led_shrink_factors.setSizePolicy(sizePolicy4)
        self.led_shrink_factors.setMinimumSize(QSize(75, 0))
        self.led_shrink_factors.setMaximumSize(QSize(100, 25))

        self.gridLayout_4.addWidget(self.led_shrink_factors, 6, 3, 1, 1)

        self.lab_upper_edge_thresh = QLabel(self.tab_reg)
        self.lab_upper_edge_thresh.setObjectName(u"lab_upper_edge_thresh")

        self.gridLayout_4.addWidget(self.lab_upper_edge_thresh, 12, 0, 1, 1)

        self.lab_shrink_factors = QLabel(self.tab_reg)
        self.lab_shrink_factors.setObjectName(u"lab_shrink_factors")

        self.gridLayout_4.addWidget(self.lab_shrink_factors, 6, 0, 1, 3)

        self.cbo_intraop_input = QComboBox(self.tab_reg)
        self.cbo_intraop_input.addItem("")
        self.cbo_intraop_input.setObjectName(u"cbo_intraop_input")

        self.gridLayout_4.addWidget(self.cbo_intraop_input, 1, 3, 1, 1)

        self.cbo_preop_input = QComboBox(self.tab_reg)
        self.cbo_preop_input.addItem("")
        self.cbo_preop_input.setObjectName(u"cbo_preop_input")

        self.gridLayout_4.addWidget(self.cbo_preop_input, 2, 3, 1, 1)

        self.tab_main.addTab(self.tab_reg, "")

        self.gridLayout.addWidget(self.tab_main, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 3)

        win_main_window.setCentralWidget(self.lay_main_layout)
        self.mba_main_menu = QMenuBar(win_main_window)
        self.mba_main_menu.setObjectName(u"mba_main_menu")
        self.mba_main_menu.setGeometry(QRect(0, 0, 600, 22))
        self.men_file = QMenu(self.mba_main_menu)
        self.men_file.setObjectName(u"men_file")
        self.men_read = QMenu(self.men_file)
        self.men_read.setObjectName(u"men_read")
        self.men_read.setTearOffEnabled(False)
        self.men_read.setSeparatorsCollapsible(False)
        self.men_write = QMenu(self.men_file)
        self.men_write.setObjectName(u"men_write")
        win_main_window.setMenuBar(self.mba_main_menu)
        QWidget.setTabOrder(self.tab_main, self.rbu_intraop_drr)
        QWidget.setTabOrder(self.rbu_intraop_drr, self.rbu_preop_drr)
        QWidget.setTabOrder(self.rbu_preop_drr, self.led_drr_width)
        QWidget.setTabOrder(self.led_drr_width, self.led_drr_height)
        QWidget.setTabOrder(self.led_drr_height, self.led_sid)
        QWidget.setTabOrder(self.led_sid, self.led_drr_thresh)
        QWidget.setTabOrder(self.led_drr_thresh, self.pbu_drr_start)
        QWidget.setTabOrder(self.pbu_drr_start, self.cbo_intraop_input)
        QWidget.setTabOrder(self.cbo_intraop_input, self.cbo_preop_input)
        QWidget.setTabOrder(self.cbo_preop_input, self.led_multires_levels)
        QWidget.setTabOrder(self.led_multires_levels, self.led_shrink_factors)
        QWidget.setTabOrder(self.led_shrink_factors, self.led_sigma_factors)
        QWidget.setTabOrder(self.led_sigma_factors, self.cbo_optim_method)
        QWidget.setTabOrder(self.cbo_optim_method, self.pbu_reg_start)
        QWidget.setTabOrder(self.pbu_reg_start, self.led_lower_edge_thresh)
        QWidget.setTabOrder(self.led_lower_edge_thresh, self.led_upper_edge_thresh)
        QWidget.setTabOrder(self.led_upper_edge_thresh, self.tbr_output_messages)
        QWidget.setTabOrder(self.tbr_output_messages, self.twi_data_list)

        self.mba_main_menu.addAction(self.men_file.menuAction())
        self.men_file.addAction(self.men_read.menuAction())
        self.men_file.addAction(self.men_write.menuAction())
        self.men_file.addAction(self.mac_info)
        self.men_file.addSeparator()
        self.men_file.addAction(self.mac_exit)
        self.men_read.addAction(self.mac_read_intra_ct)
        self.men_read.addAction(self.mac_read_intraop_drr)
        self.men_read.addAction(self.mac_read_preop_drr)
        self.men_write.addAction(self.mac_write_preop_drr)
        self.men_write.addAction(self.mac_write_intraop_drr)
        self.men_write.addAction(self.mac_write_registered_drr)

        self.retranslateUi(win_main_window)

        self.tab_main.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(win_main_window)
    # setupUi

    def retranslateUi(self, win_main_window):
        win_main_window.setWindowTitle(QCoreApplication.translate("win_main_window", u"Casif", None))
        self.mac_info.setText(QCoreApplication.translate("win_main_window", u"Informace", None))
        self.mac_exit.setText(QCoreApplication.translate("win_main_window", u"Ukon\u010dit", None))
        self.mac_read_pre_ct.setText(QCoreApplication.translate("win_main_window", u"P\u0159edopera\u010dn\u00ed CT pl\u00e1n", None))
        self.mac_read_xray.setText(QCoreApplication.translate("win_main_window", u"RTG obraz", None))
        self.mac_read_intra_ct.setText(QCoreApplication.translate("win_main_window", u"Intraopera\u010dn\u00ed CT", None))
        self.mac_write_preop_drr.setText(QCoreApplication.translate("win_main_window", u"P\u0159edopera\u010dn\u00ed DRR", None))
        self.mac_write_intraop_drr.setText(QCoreApplication.translate("win_main_window", u"Intraopera\u010dn\u00ed DRR", None))
        self.mac_gen_drr.setText(QCoreApplication.translate("win_main_window", u"Vytvo\u0159it DRR obraz", None))
        self.actionIntraopera_n_CT.setText(QCoreApplication.translate("win_main_window", u"Intraopera\u010dn\u00ed CT", None))
        self.mac_read_preop_drr.setText(QCoreApplication.translate("win_main_window", u"P\u0159edopera\u010dn\u00ed DRR", None))
        self.mac_read_intraop_drr.setText(QCoreApplication.translate("win_main_window", u"Intraopera\u010dn\u00ed DRR", None))
        self.mac_write_registered_drr.setText(QCoreApplication.translate("win_main_window", u"Registrovan\u00e9 DRR", None))
        self.actionNov_pacient.setText(QCoreApplication.translate("win_main_window", u"Nov\u00fd pacient", None))
        ___qtreewidgetitem = self.twi_data_list.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("win_main_window", u"Data pacienta:", None));

        __sortingEnabled = self.twi_data_list.isSortingEnabled()
        self.twi_data_list.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.twi_data_list.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("win_main_window", u"CT", None));
        ___qtreewidgetitem2 = self.twi_data_list.topLevelItem(1)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("win_main_window", u"Intraopera\u010dn\u00ed DRR", None));
        ___qtreewidgetitem3 = self.twi_data_list.topLevelItem(2)
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("win_main_window", u"P\u0159edopera\u010dn\u00ed DRR", None));
        ___qtreewidgetitem4 = self.twi_data_list.topLevelItem(3)
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("win_main_window", u"V\u00fdstup registrace", None));
        self.twi_data_list.setSortingEnabled(__sortingEnabled)

        self.lab_drr_width.setText(QCoreApplication.translate("win_main_window", u"\u0160\u00ed\u0159ka obrazu (px):", None))
        self.led_drr_width.setInputMask("")
        self.led_drr_width.setText(QCoreApplication.translate("win_main_window", u"1000", None))
        self.lab_sid.setText(QCoreApplication.translate("win_main_window", u"Vzd\u00e1lenost zdroj-detektor (mm):", None))
        self.rbu_preop_drr.setText(QCoreApplication.translate("win_main_window", u"P\u0159edopera\u010dn\u00ed", None))
        self.lab_drr_height.setText(QCoreApplication.translate("win_main_window", u"V\u00fd\u0161ka obrazu (px):", None))
        self.lab_drr_type.setText(QCoreApplication.translate("win_main_window", u"DRR obraz:", None))
        self.pbu_drr_start.setText(QCoreApplication.translate("win_main_window", u"Vytvo\u0159it DRR", None))
        self.led_sid.setText(QCoreApplication.translate("win_main_window", u"1000.0", None))
        self.rbu_intraop_drr.setText(QCoreApplication.translate("win_main_window", u"Intraopera\u010dn\u00ed", None))
        self.led_drr_height.setText(QCoreApplication.translate("win_main_window", u"1000", None))
        self.led_drr_thresh.setText(QCoreApplication.translate("win_main_window", u"0", None))
        self.lab_ct_thresh.setText(QCoreApplication.translate("win_main_window", u"Pr\u00e1h voxel\u016f (HU):", None))
        self.tab_main.setTabText(self.tab_main.indexOf(self.tab_drr_obrazy), QCoreApplication.translate("win_main_window", u"DRR obrazy", None))
        self.labm_input_warning.setText(QCoreApplication.translate("win_main_window", u"---", None))
        self.lab_fixed_drr.setText(QCoreApplication.translate("win_main_window", u"Intraopera\u010dn\u00ed DRR:", None))
        self.lab_optim_method.setText(QCoreApplication.translate("win_main_window", u"Optimaliza\u010dn\u00ed metoda:", None))
        self.lab_moving_drr.setText(QCoreApplication.translate("win_main_window", u"P\u0159edopera\u010dn\u00ed DRR:", None))
        self.lab_multires_levels.setText(QCoreApplication.translate("win_main_window", u"Po\u010det registra\u010dn\u00edch \u00farovn\u00ed:", None))
        self.led_multires_levels.setText(QCoreApplication.translate("win_main_window", u"2", None))
        self.led_lower_edge_thresh.setText(QCoreApplication.translate("win_main_window", u"0.1", None))
        self.lab_lower_edge_thresh.setText(QCoreApplication.translate("win_main_window", u"Doln\u00ed pr\u00e1h hran:", None))
        self.led_upper_edge_thresh.setText(QCoreApplication.translate("win_main_window", u"0.5", None))
        self.cbo_optim_method.setItemText(0, QCoreApplication.translate("win_main_window", u"Gradientn\u00ed sestup", None))
        self.cbo_optim_method.setItemText(1, QCoreApplication.translate("win_main_window", u"Gradientn\u00ed sestup se zl. \u0159ezem", None))
        self.cbo_optim_method.setItemText(2, QCoreApplication.translate("win_main_window", u"BFGS s omezenou pam\u011bt\u00ed", None))

        self.cbo_optim_method.setCurrentText(QCoreApplication.translate("win_main_window", u"Gradientn\u00ed sestup", None))
        self.lab_sigma_factors.setText(QCoreApplication.translate("win_main_window", u"Rozptyly Gaussova filtru:", None))
        self.led_sigma_factors.setText(QCoreApplication.translate("win_main_window", u"3.0; 0.0", None))
        self.pbu_reg_start.setText(QCoreApplication.translate("win_main_window", u"Spustit registraci", None))
        self.led_shrink_factors.setText(QCoreApplication.translate("win_main_window", u"4; 1", None))
        self.lab_upper_edge_thresh.setText(QCoreApplication.translate("win_main_window", u"Horn\u00ed pr\u00e1h hran:", None))
        self.lab_shrink_factors.setText(QCoreApplication.translate("win_main_window", u"\u0160k\u00e1lovac\u00ed konstanty:", None))
        self.cbo_intraop_input.setItemText(0, QCoreApplication.translate("win_main_window", u"---", None))

        self.cbo_preop_input.setItemText(0, QCoreApplication.translate("win_main_window", u"---", None))

        self.tab_main.setTabText(self.tab_main.indexOf(self.tab_reg), QCoreApplication.translate("win_main_window", u"Registrace obraz\u016f", None))
        self.men_file.setTitle(QCoreApplication.translate("win_main_window", u"Soubor", None))
        self.men_read.setTitle(QCoreApplication.translate("win_main_window", u"Otev\u0159\u00edt", None))
        self.men_write.setTitle(QCoreApplication.translate("win_main_window", u"Ulo\u017eit", None))
    # retranslateUi

