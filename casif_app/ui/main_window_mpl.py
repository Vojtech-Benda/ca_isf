# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window_mpl.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QGroupBox, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QTabWidget, QTextBrowser,
    QWidget)

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
        self.lay_main_layout = QWidget(win_main_window)
        self.lay_main_layout.setObjectName(u"lay_main_layout")
        self.gridLayout = QGridLayout(self.lay_main_layout)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tab_main = QTabWidget(self.lay_main_layout)
        self.tab_main.setObjectName(u"tab_main")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tab_main.sizePolicy().hasHeightForWidth())
        self.tab_main.setSizePolicy(sizePolicy1)
        self.tab_main.setMinimumSize(QSize(375, 0))
        self.tab_main.setMaximumSize(QSize(16777215, 16777215))
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

        self.gridLayout_3.addWidget(self.lab_sid, 6, 0, 1, 3)

        self.led_drr_width = QLineEdit(self.tab_drr_obrazy)
        self.led_drr_width.setObjectName(u"led_drr_width")
        self.led_drr_width.setMaximumSize(QSize(50, 60))

        self.gridLayout_3.addWidget(self.led_drr_width, 4, 3, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 15, 0, 1, 1)

        self.led_drr_height = QLineEdit(self.tab_drr_obrazy)
        self.led_drr_height.setObjectName(u"led_drr_height")
        self.led_drr_height.setMaximumSize(QSize(50, 16777215))
        self.led_drr_height.setFrame(True)

        self.gridLayout_3.addWidget(self.led_drr_height, 5, 3, 1, 1)

        self.lab_drr_height = QLabel(self.tab_drr_obrazy)
        self.lab_drr_height.setObjectName(u"lab_drr_height")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lab_drr_height.sizePolicy().hasHeightForWidth())
        self.lab_drr_height.setSizePolicy(sizePolicy3)
        self.lab_drr_height.setMinimumSize(QSize(65, 20))

        self.gridLayout_3.addWidget(self.lab_drr_height, 5, 0, 1, 1)

        self.gbo_intraop_info = QGroupBox(self.tab_drr_obrazy)
        self.gbo_intraop_info.setObjectName(u"gbo_intraop_info")
        self.gridLayout_6 = QGridLayout(self.gbo_intraop_info)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_3, 0, 4, 2, 1)

        self.lab_intraop_drr_created = QLabel(self.gbo_intraop_info)
        self.lab_intraop_drr_created.setObjectName(u"lab_intraop_drr_created")

        self.gridLayout_6.addWidget(self.lab_intraop_drr_created, 1, 0, 1, 1)

        self.labm_intraop_ct_name = QLabel(self.gbo_intraop_info)
        self.labm_intraop_ct_name.setObjectName(u"labm_intraop_ct_name")
        self.labm_intraop_ct_name.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_6.addWidget(self.labm_intraop_ct_name, 0, 1, 1, 1)

        self.labm_intraop_drr_created = QLabel(self.gbo_intraop_info)
        self.labm_intraop_drr_created.setObjectName(u"labm_intraop_drr_created")
        self.labm_intraop_drr_created.setMinimumSize(QSize(20, 20))
        self.labm_intraop_drr_created.setMaximumSize(QSize(20, 20))
        font = QFont()
        font.setBold(True)
        self.labm_intraop_drr_created.setFont(font)

        self.gridLayout_6.addWidget(self.labm_intraop_drr_created, 1, 1, 1, 1)

        self.lab_intraop_ct_name = QLabel(self.gbo_intraop_info)
        self.lab_intraop_ct_name.setObjectName(u"lab_intraop_ct_name")
        self.lab_intraop_ct_name.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_6.addWidget(self.lab_intraop_ct_name, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.gbo_intraop_info, 14, 0, 1, 4)

        self.pbu_drr_start = QPushButton(self.tab_drr_obrazy)
        self.pbu_drr_start.setObjectName(u"pbu_drr_start")
        self.pbu_drr_start.setMinimumSize(QSize(100, 25))
        self.pbu_drr_start.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_3.addWidget(self.pbu_drr_start, 10, 0, 1, 1)

        self.lab_drr_width = QLabel(self.tab_drr_obrazy)
        self.lab_drr_width.setObjectName(u"lab_drr_width")
        sizePolicy3.setHeightForWidth(self.lab_drr_width.sizePolicy().hasHeightForWidth())
        self.lab_drr_width.setSizePolicy(sizePolicy3)
        self.lab_drr_width.setMinimumSize(QSize(65, 20))

        self.gridLayout_3.addWidget(self.lab_drr_width, 4, 0, 1, 1)

        self.gbo_preop_info = QGroupBox(self.tab_drr_obrazy)
        self.gbo_preop_info.setObjectName(u"gbo_preop_info")
        self.gridLayout_5 = QGridLayout(self.gbo_preop_info)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.lab_preop_drr_created = QLabel(self.gbo_preop_info)
        self.lab_preop_drr_created.setObjectName(u"lab_preop_drr_created")

        self.gridLayout_5.addWidget(self.lab_preop_drr_created, 1, 0, 1, 1)

        self.labm_preop_name = QLabel(self.gbo_preop_info)
        self.labm_preop_name.setObjectName(u"labm_preop_name")
        self.labm_preop_name.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_5.addWidget(self.labm_preop_name, 0, 1, 1, 1)

        self.labm_preop_drr_created = QLabel(self.gbo_preop_info)
        self.labm_preop_drr_created.setObjectName(u"labm_preop_drr_created")
        self.labm_preop_drr_created.setMinimumSize(QSize(20, 20))
        self.labm_preop_drr_created.setMaximumSize(QSize(20, 20))
        self.labm_preop_drr_created.setFont(font)

        self.gridLayout_5.addWidget(self.labm_preop_drr_created, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_2, 0, 2, 2, 1)

        self.lab_preop_model_name = QLabel(self.gbo_preop_info)
        self.lab_preop_model_name.setObjectName(u"lab_preop_model_name")
        self.lab_preop_model_name.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_5.addWidget(self.lab_preop_model_name, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.gbo_preop_info, 12, 0, 1, 4)

        self.lab_drr_type = QLabel(self.tab_drr_obrazy)
        self.lab_drr_type.setObjectName(u"lab_drr_type")
        sizePolicy2.setHeightForWidth(self.lab_drr_type.sizePolicy().hasHeightForWidth())
        self.lab_drr_type.setSizePolicy(sizePolicy2)
        self.lab_drr_type.setMinimumSize(QSize(65, 20))
        self.lab_drr_type.setTextFormat(Qt.AutoText)
        self.lab_drr_type.setWordWrap(True)
        self.lab_drr_type.setMargin(0)

        self.gridLayout_3.addWidget(self.lab_drr_type, 0, 0, 1, 1)

        self.lab_ct_thresh = QLabel(self.tab_drr_obrazy)
        self.lab_ct_thresh.setObjectName(u"lab_ct_thresh")
        sizePolicy3.setHeightForWidth(self.lab_ct_thresh.sizePolicy().hasHeightForWidth())
        self.lab_ct_thresh.setSizePolicy(sizePolicy3)
        self.lab_ct_thresh.setMinimumSize(QSize(65, 20))

        self.gridLayout_3.addWidget(self.lab_ct_thresh, 7, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 13, 0, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_5, 6, 4, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer_4, 11, 0, 1, 1)

        self.led_sid = QLineEdit(self.tab_drr_obrazy)
        self.led_sid.setObjectName(u"led_sid")
        self.led_sid.setMaximumSize(QSize(50, 25))

        self.gridLayout_3.addWidget(self.led_sid, 6, 3, 1, 1)

        self.led_drr_thresh = QLineEdit(self.tab_drr_obrazy)
        self.led_drr_thresh.setObjectName(u"led_drr_thresh")
        self.led_drr_thresh.setMaximumSize(QSize(50, 30))

        self.gridLayout_3.addWidget(self.led_drr_thresh, 7, 3, 1, 1)

        self.rbu_preop_drr = QRadioButton(self.tab_drr_obrazy)
        self.rbu_preop_drr.setObjectName(u"rbu_preop_drr")

        self.gridLayout_3.addWidget(self.rbu_preop_drr, 2, 3, 1, 1)

        self.rbu_intraop_drr = QRadioButton(self.tab_drr_obrazy)
        self.rbu_intraop_drr.setObjectName(u"rbu_intraop_drr")
        self.rbu_intraop_drr.setChecked(True)

        self.gridLayout_3.addWidget(self.rbu_intraop_drr, 0, 3, 1, 1)

        self.labm_data_warning = QLabel(self.tab_drr_obrazy)
        self.labm_data_warning.setObjectName(u"labm_data_warning")
        self.labm_data_warning.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.labm_data_warning, 10, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 10, 1, 1, 2)

        self.tab_main.addTab(self.tab_drr_obrazy, "")
        self.tab_reg = QWidget()
        self.tab_reg.setObjectName(u"tab_reg")
        self.gridLayout_4 = QGridLayout(self.tab_reg)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_6, 3, 4, 3, 1)

        self.pbu_reg_start = QPushButton(self.tab_reg)
        self.pbu_reg_start.setObjectName(u"pbu_reg_start")
        self.pbu_reg_start.setMinimumSize(QSize(0, 25))

        self.gridLayout_4.addWidget(self.pbu_reg_start, 8, 0, 1, 1)

        self.labm_moving_drr = QLabel(self.tab_reg)
        self.labm_moving_drr.setObjectName(u"labm_moving_drr")

        self.gridLayout_4.addWidget(self.labm_moving_drr, 1, 3, 1, 2)

        self.labm_input_warning = QLabel(self.tab_reg)
        self.labm_input_warning.setObjectName(u"labm_input_warning")

        self.gridLayout_4.addWidget(self.labm_input_warning, 8, 2, 1, 2)

        self.labm_fixed_drr = QLabel(self.tab_reg)
        self.labm_fixed_drr.setObjectName(u"labm_fixed_drr")

        self.gridLayout_4.addWidget(self.labm_fixed_drr, 2, 3, 1, 2)

        self.cbo_optim_method = QComboBox(self.tab_reg)
        self.cbo_optim_method.addItem("")
        self.cbo_optim_method.addItem("")
        self.cbo_optim_method.addItem("")
        self.cbo_optim_method.setObjectName(u"cbo_optim_method")
        self.cbo_optim_method.setMinimumSize(QSize(0, 25))
        self.cbo_optim_method.setMaxVisibleItems(3)

        self.gridLayout_4.addWidget(self.cbo_optim_method, 7, 3, 1, 1)

        self.lab_sigma_factors = QLabel(self.tab_reg)
        self.lab_sigma_factors.setObjectName(u"lab_sigma_factors")

        self.gridLayout_4.addWidget(self.lab_sigma_factors, 5, 0, 1, 3)

        self.lab_fixed_drr = QLabel(self.tab_reg)
        self.lab_fixed_drr.setObjectName(u"lab_fixed_drr")

        self.gridLayout_4.addWidget(self.lab_fixed_drr, 2, 0, 1, 1)

        self.led_sigma_factors = QLineEdit(self.tab_reg)
        self.led_sigma_factors.setObjectName(u"led_sigma_factors")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.led_sigma_factors.sizePolicy().hasHeightForWidth())
        self.led_sigma_factors.setSizePolicy(sizePolicy4)
        self.led_sigma_factors.setMinimumSize(QSize(75, 0))
        self.led_sigma_factors.setMaximumSize(QSize(100, 25))

        self.gridLayout_4.addWidget(self.led_sigma_factors, 5, 3, 1, 1)

        self.led_multires_levels = QLineEdit(self.tab_reg)
        self.led_multires_levels.setObjectName(u"led_multires_levels")
        self.led_multires_levels.setMinimumSize(QSize(50, 0))
        self.led_multires_levels.setMaximumSize(QSize(25, 25))
        self.led_multires_levels.setMaxLength(1)

        self.gridLayout_4.addWidget(self.led_multires_levels, 3, 3, 1, 1)

        self.led_shrink_factors = QLineEdit(self.tab_reg)
        self.led_shrink_factors.setObjectName(u"led_shrink_factors")
        sizePolicy4.setHeightForWidth(self.led_shrink_factors.sizePolicy().hasHeightForWidth())
        self.led_shrink_factors.setSizePolicy(sizePolicy4)
        self.led_shrink_factors.setMinimumSize(QSize(75, 0))
        self.led_shrink_factors.setMaximumSize(QSize(100, 25))

        self.gridLayout_4.addWidget(self.led_shrink_factors, 4, 3, 1, 1)

        self.lab_multires_levels = QLabel(self.tab_reg)
        self.lab_multires_levels.setObjectName(u"lab_multires_levels")

        self.gridLayout_4.addWidget(self.lab_multires_levels, 3, 0, 1, 3)

        self.lab_moving_drr = QLabel(self.tab_reg)
        self.lab_moving_drr.setObjectName(u"lab_moving_drr")

        self.gridLayout_4.addWidget(self.lab_moving_drr, 1, 0, 1, 1)

        self.lab_shrink_factors = QLabel(self.tab_reg)
        self.lab_shrink_factors.setObjectName(u"lab_shrink_factors")

        self.gridLayout_4.addWidget(self.lab_shrink_factors, 4, 0, 1, 3)

        self.lab_optim_method = QLabel(self.tab_reg)
        self.lab_optim_method.setObjectName(u"lab_optim_method")

        self.gridLayout_4.addWidget(self.lab_optim_method, 7, 0, 1, 1)

        self.tbr_output_messages = QTextBrowser(self.tab_reg)
        self.tbr_output_messages.setObjectName(u"tbr_output_messages")

        self.gridLayout_4.addWidget(self.tbr_output_messages, 10, 0, 1, 5)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_6, 9, 0, 1, 5)

        self.tab_main.addTab(self.tab_reg, "")

        self.gridLayout.addWidget(self.tab_main, 0, 0, 1, 1)

        self.frame = QFrame(self.lay_main_layout)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Plain)
        self.gridLayout_7 = QGridLayout(self.frame)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)

        self.gridLayout_7.addWidget(self.widget, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 2, 3, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_5, 1, 0, 1, 1)

        self.gbo_image_info = QGroupBox(self.lay_main_layout)
        self.gbo_image_info.setObjectName(u"gbo_image_info")
        self.gbo_image_info.setMaximumSize(QSize(375, 16777215))
        self.gbo_image_info.setCheckable(False)
        self.gridLayout_2 = QGridLayout(self.gbo_image_info)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lab_visualization = QLabel(self.gbo_image_info)
        self.lab_visualization.setObjectName(u"lab_visualization")
        self.lab_visualization.setMaximumSize(QSize(60, 16777215))

        self.gridLayout_2.addWidget(self.lab_visualization, 0, 0, 1, 1)

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

        self.led_upper_edge_thresh = QLineEdit(self.gbo_image_info)
        self.led_upper_edge_thresh.setObjectName(u"led_upper_edge_thresh")
        self.led_upper_edge_thresh.setMinimumSize(QSize(50, 0))
        self.led_upper_edge_thresh.setMaximumSize(QSize(25, 25))

        self.gridLayout_2.addWidget(self.led_upper_edge_thresh, 4, 1, 1, 1)

        self.led_lower_edge_thresh = QLineEdit(self.gbo_image_info)
        self.led_lower_edge_thresh.setObjectName(u"led_lower_edge_thresh")
        self.led_lower_edge_thresh.setMinimumSize(QSize(50, 0))
        self.led_lower_edge_thresh.setMaximumSize(QSize(25, 25))

        self.gridLayout_2.addWidget(self.led_lower_edge_thresh, 3, 1, 1, 1)

        self.lab_lower_edge_thresh = QLabel(self.gbo_image_info)
        self.lab_lower_edge_thresh.setObjectName(u"lab_lower_edge_thresh")

        self.gridLayout_2.addWidget(self.lab_lower_edge_thresh, 3, 0, 1, 1)

        self.lab_upper_edge_thresh = QLabel(self.gbo_image_info)
        self.lab_upper_edge_thresh.setObjectName(u"lab_upper_edge_thresh")

        self.gridLayout_2.addWidget(self.lab_upper_edge_thresh, 4, 0, 1, 1)

        self.labm_vis_warning = QLabel(self.gbo_image_info)
        self.labm_vis_warning.setObjectName(u"labm_vis_warning")

        self.gridLayout_2.addWidget(self.labm_vis_warning, 2, 1, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(100, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_7, 0, 2, 1, 1)


        self.gridLayout.addWidget(self.gbo_image_info, 2, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 0, 1, 3, 1)

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
        QWidget.setTabOrder(self.tab_main, self.rbu_intraop_drr)
        QWidget.setTabOrder(self.rbu_intraop_drr, self.rbu_preop_drr)
        QWidget.setTabOrder(self.rbu_preop_drr, self.led_drr_width)
        QWidget.setTabOrder(self.led_drr_width, self.led_drr_height)
        QWidget.setTabOrder(self.led_drr_height, self.led_sid)
        QWidget.setTabOrder(self.led_sid, self.led_drr_thresh)
        QWidget.setTabOrder(self.led_drr_thresh, self.pbu_drr_start)
        QWidget.setTabOrder(self.pbu_drr_start, self.led_multires_levels)
        QWidget.setTabOrder(self.led_multires_levels, self.led_shrink_factors)
        QWidget.setTabOrder(self.led_shrink_factors, self.led_sigma_factors)
        QWidget.setTabOrder(self.led_sigma_factors, self.cbo_optim_method)
        QWidget.setTabOrder(self.cbo_optim_method, self.pbu_reg_start)
        QWidget.setTabOrder(self.pbu_reg_start, self.tbr_output_messages)
        QWidget.setTabOrder(self.tbr_output_messages, self.cbo_visualization)
        QWidget.setTabOrder(self.cbo_visualization, self.led_lower_edge_thresh)
        QWidget.setTabOrder(self.led_lower_edge_thresh, self.led_upper_edge_thresh)

        self.mba_main_menu.addAction(self.men_file.menuAction())
        self.men_file.addAction(self.men_read.menuAction())
        self.men_file.addAction(self.men_write.menuAction())
        self.men_file.addAction(self.mac_info)
        self.men_file.addSeparator()
        self.men_file.addAction(self.mac_exit)
        self.men_read.addAction(self.mac_read_intra_ct)
        self.men_read.addAction(self.mac_read_preop_drr)
        self.men_read.addAction(self.mac_read_intraop_drr)
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
        self.lab_sid.setText(QCoreApplication.translate("win_main_window", u"Vzd\u00e1lenost zdroj-detektor (mm):", None))
        self.led_drr_width.setInputMask("")
        self.led_drr_width.setText(QCoreApplication.translate("win_main_window", u"1000", None))
        self.led_drr_height.setText(QCoreApplication.translate("win_main_window", u"1000", None))
        self.lab_drr_height.setText(QCoreApplication.translate("win_main_window", u"V\u00fd\u0161ka obrazu (px):", None))
        self.gbo_intraop_info.setTitle(QCoreApplication.translate("win_main_window", u"Intraopera\u010dn\u00ed data", None))
        self.lab_intraop_drr_created.setText(QCoreApplication.translate("win_main_window", u"Vytvo\u0159eno DRR:", None))
        self.labm_intraop_ct_name.setText(QCoreApplication.translate("win_main_window", u"---", None))
        self.labm_intraop_drr_created.setText("")
        self.lab_intraop_ct_name.setText(QCoreApplication.translate("win_main_window", u"N\u00e1zev CT:", None))
        self.pbu_drr_start.setText(QCoreApplication.translate("win_main_window", u"Vytvo\u0159it DRR", None))
        self.lab_drr_width.setText(QCoreApplication.translate("win_main_window", u"\u0160\u00ed\u0159ka obrazu (px):", None))
        self.gbo_preop_info.setTitle(QCoreApplication.translate("win_main_window", u"P\u0159edopera\u010dn\u00ed data", None))
        self.lab_preop_drr_created.setText(QCoreApplication.translate("win_main_window", u"Vytvo\u0159eno DRR:", None))
        self.labm_preop_name.setText(QCoreApplication.translate("win_main_window", u"---", None))
        self.labm_preop_drr_created.setText("")
        self.lab_preop_model_name.setText(QCoreApplication.translate("win_main_window", u"3D model:", None))
        self.lab_drr_type.setText(QCoreApplication.translate("win_main_window", u"DRR obraz:", None))
        self.lab_ct_thresh.setText(QCoreApplication.translate("win_main_window", u"Pr\u00e1h voxel\u016f (HU):", None))
        self.led_sid.setText(QCoreApplication.translate("win_main_window", u"1000.0", None))
        self.led_drr_thresh.setText(QCoreApplication.translate("win_main_window", u"0", None))
        self.rbu_preop_drr.setText(QCoreApplication.translate("win_main_window", u"P\u0159edopera\u010dn\u00ed", None))
        self.rbu_intraop_drr.setText(QCoreApplication.translate("win_main_window", u"Intraopera\u010dn\u00ed", None))
        self.labm_data_warning.setText(QCoreApplication.translate("win_main_window", u"---", None))
        self.tab_main.setTabText(self.tab_main.indexOf(self.tab_drr_obrazy), QCoreApplication.translate("win_main_window", u"DRR obrazy", None))
        self.pbu_reg_start.setText(QCoreApplication.translate("win_main_window", u"Spustit registraci", None))
        self.labm_moving_drr.setText(QCoreApplication.translate("win_main_window", u"---", None))
        self.labm_input_warning.setText(QCoreApplication.translate("win_main_window", u"---", None))
        self.labm_fixed_drr.setText(QCoreApplication.translate("win_main_window", u"---", None))
        self.cbo_optim_method.setItemText(0, QCoreApplication.translate("win_main_window", u"Gradientn\u00ed sestup", None))
        self.cbo_optim_method.setItemText(1, QCoreApplication.translate("win_main_window", u"Gradientn\u00ed sestup se zl. \u0159ezem", None))
        self.cbo_optim_method.setItemText(2, QCoreApplication.translate("win_main_window", u"BFGS s omezenou pam\u011bt\u00ed", None))

        self.cbo_optim_method.setCurrentText(QCoreApplication.translate("win_main_window", u"Gradientn\u00ed sestup", None))
        self.lab_sigma_factors.setText(QCoreApplication.translate("win_main_window", u"Rozptyly Gaussova filtru:", None))
        self.lab_fixed_drr.setText(QCoreApplication.translate("win_main_window", u"Intraopera\u010dn\u00ed DRR:", None))
        self.led_sigma_factors.setText(QCoreApplication.translate("win_main_window", u"3.0; 0.0", None))
        self.led_multires_levels.setText(QCoreApplication.translate("win_main_window", u"2", None))
        self.led_shrink_factors.setText(QCoreApplication.translate("win_main_window", u"4; 1", None))
        self.lab_multires_levels.setText(QCoreApplication.translate("win_main_window", u"Po\u010det registra\u010dn\u00edch \u00farovn\u00ed:", None))
        self.lab_moving_drr.setText(QCoreApplication.translate("win_main_window", u"P\u0159edopera\u010dn\u00ed DRR:", None))
        self.lab_shrink_factors.setText(QCoreApplication.translate("win_main_window", u"\u0160k\u00e1lovac\u00ed konstanty:", None))
        self.lab_optim_method.setText(QCoreApplication.translate("win_main_window", u"Optimaliza\u010dn\u00ed metoda:", None))
        self.tab_main.setTabText(self.tab_main.indexOf(self.tab_reg), QCoreApplication.translate("win_main_window", u"Registrace obraz\u016f", None))
        self.gbo_image_info.setTitle(QCoreApplication.translate("win_main_window", u"Informace o obrazech", None))
        self.lab_visualization.setText(QCoreApplication.translate("win_main_window", u"Zobrazen\u00ed:", None))
        self.cbo_visualization.setItemText(0, QCoreApplication.translate("win_main_window", u"Intraopera\u010dn\u00ed DRR", None))
        self.cbo_visualization.setItemText(1, QCoreApplication.translate("win_main_window", u"Preopera\u010dn\u00ed DRR", None))
        self.cbo_visualization.setItemText(2, QCoreApplication.translate("win_main_window", u"Preop. hrany + Intraop.", None))
        self.cbo_visualization.setItemText(3, QCoreApplication.translate("win_main_window", u"Pr\u016fhledn\u00fd kompozit", None))

        self.led_upper_edge_thresh.setText(QCoreApplication.translate("win_main_window", u"0.5", None))
        self.led_lower_edge_thresh.setText(QCoreApplication.translate("win_main_window", u"0.1", None))
        self.lab_lower_edge_thresh.setText(QCoreApplication.translate("win_main_window", u"Doln\u00ed pr\u00e1h:", None))
        self.lab_upper_edge_thresh.setText(QCoreApplication.translate("win_main_window", u"Horn\u00ed pr\u00e1h:", None))
        self.labm_vis_warning.setText(QCoreApplication.translate("win_main_window", u"---", None))
        self.men_file.setTitle(QCoreApplication.translate("win_main_window", u"Soubor", None))
        self.men_read.setTitle(QCoreApplication.translate("win_main_window", u"Otev\u0159\u00edt", None))
        self.men_write.setTitle(QCoreApplication.translate("win_main_window", u"Ulo\u017eit", None))
    # retranslateUi

