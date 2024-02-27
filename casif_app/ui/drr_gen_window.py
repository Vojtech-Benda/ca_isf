# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'drr_gen_window.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QLabel, QLayout, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_win_drr_gen(object):
    def setupUi(self, win_drr_gen):
        if not win_drr_gen.objectName():
            win_drr_gen.setObjectName(u"win_drr_gen")
        win_drr_gen.resize(587, 379)
        win_drr_gen.setLayoutDirection(Qt.LeftToRight)
        self.gridLayout_5 = QGridLayout(win_drr_gen)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.line = QFrame(win_drr_gen)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_5.addWidget(self.line, 1, 0, 1, 2)

        self.gbo_ct_info = QGroupBox(win_drr_gen)
        self.gbo_ct_info.setObjectName(u"gbo_ct_info")
        self.gbo_ct_info.setMaximumSize(QSize(16777215, 175))
        font = QFont()
        font.setPointSize(10)
        self.gbo_ct_info.setFont(font)
        self.gbo_ct_info.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.gbo_ct_info.setFlat(False)
        self.gbo_ct_info.setCheckable(False)
        self.gridLayout_2 = QGridLayout(self.gbo_ct_info)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_2.setHorizontalSpacing(15)
        self.gridLayout_2.setVerticalSpacing(10)
        self.gridLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.lab_slice_thickness = QLabel(self.gbo_ct_info)
        self.lab_slice_thickness.setObjectName(u"lab_slice_thickness")
        self.lab_slice_thickness.setMinimumSize(QSize(0, 20))
        self.lab_slice_thickness.setMaximumSize(QSize(16777215, 20))
        font1 = QFont()
        font1.setPointSize(9)
        self.lab_slice_thickness.setFont(font1)

        self.gridLayout_2.addWidget(self.lab_slice_thickness, 5, 0, 1, 1)

        self.lab_slice_count = QLabel(self.gbo_ct_info)
        self.lab_slice_count.setObjectName(u"lab_slice_count")
        self.lab_slice_count.setMinimumSize(QSize(0, 20))
        self.lab_slice_count.setMaximumSize(QSize(16777215, 20))
        self.lab_slice_count.setFont(font1)

        self.gridLayout_2.addWidget(self.lab_slice_count, 3, 0, 1, 1)

        self.lab_ct_name = QLabel(self.gbo_ct_info)
        self.lab_ct_name.setObjectName(u"lab_ct_name")
        self.lab_ct_name.setMinimumSize(QSize(0, 20))
        self.lab_ct_name.setMaximumSize(QSize(16777215, 20))
        self.lab_ct_name.setFont(font1)

        self.gridLayout_2.addWidget(self.lab_ct_name, 2, 0, 1, 1)

        self.lab_ct_loaded = QLabel(self.gbo_ct_info)
        self.lab_ct_loaded.setObjectName(u"lab_ct_loaded")
        self.lab_ct_loaded.setMinimumSize(QSize(0, 20))
        self.lab_ct_loaded.setMaximumSize(QSize(16777215, 20))
        self.lab_ct_loaded.setFont(font)

        self.gridLayout_2.addWidget(self.lab_ct_loaded, 0, 0, 1, 1)

        self.labm_ct_name = QLabel(self.gbo_ct_info)
        self.labm_ct_name.setObjectName(u"labm_ct_name")
        self.labm_ct_name.setMinimumSize(QSize(100, 23))
        self.labm_ct_name.setMaximumSize(QSize(16777215, 23))
        self.labm_ct_name.setFont(font1)

        self.gridLayout_2.addWidget(self.labm_ct_name, 2, 1, 1, 2)

        self.labm_slice_count = QLabel(self.gbo_ct_info)
        self.labm_slice_count.setObjectName(u"labm_slice_count")
        self.labm_slice_count.setMinimumSize(QSize(100, 23))
        self.labm_slice_count.setMaximumSize(QSize(16777215, 23))
        self.labm_slice_count.setFont(font1)

        self.gridLayout_2.addWidget(self.labm_slice_count, 3, 1, 1, 2)

        self.labm_slice_thickness = QLabel(self.gbo_ct_info)
        self.labm_slice_thickness.setObjectName(u"labm_slice_thickness")
        self.labm_slice_thickness.setMinimumSize(QSize(100, 23))
        self.labm_slice_thickness.setMaximumSize(QSize(16777215, 23))
        self.labm_slice_thickness.setFont(font1)

        self.gridLayout_2.addWidget(self.labm_slice_thickness, 5, 1, 1, 2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.labm_ct_loaded = QLabel(self.gbo_ct_info)
        self.labm_ct_loaded.setObjectName(u"labm_ct_loaded")
        self.labm_ct_loaded.setMinimumSize(QSize(20, 20))
        self.labm_ct_loaded.setMaximumSize(QSize(20, 20))
        self.labm_ct_loaded.setScaledContents(True)
        self.labm_ct_loaded.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.labm_ct_loaded, 0, 1, 1, 1)


        self.gridLayout_5.addWidget(self.gbo_ct_info, 0, 0, 1, 1)

        self.gbo_drr_info = QGroupBox(win_drr_gen)
        self.gbo_drr_info.setObjectName(u"gbo_drr_info")
        self.gbo_drr_info.setMaximumSize(QSize(16777215, 200))
        self.gbo_drr_info.setFont(font)
        self.gridLayout = QGridLayout(self.gbo_drr_info)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(15)
        self.gridLayout.setVerticalSpacing(10)
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 2, 0, 1, 7)

        self.lab_drr_pixel_spacing = QLabel(self.gbo_drr_info)
        self.lab_drr_pixel_spacing.setObjectName(u"lab_drr_pixel_spacing")
        self.lab_drr_pixel_spacing.setMaximumSize(QSize(16777215, 20))
        self.lab_drr_pixel_spacing.setFont(font1)
        self.lab_drr_pixel_spacing.setWordWrap(False)

        self.gridLayout.addWidget(self.lab_drr_pixel_spacing, 5, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 0, 6, 1, 1)

        self.labm_drr_size = QLabel(self.gbo_drr_info)
        self.labm_drr_size.setObjectName(u"labm_drr_size")
        self.labm_drr_size.setMinimumSize(QSize(60, 20))
        self.labm_drr_size.setMaximumSize(QSize(16777215, 23))
        self.labm_drr_size.setFont(font1)

        self.gridLayout.addWidget(self.labm_drr_size, 4, 1, 1, 3)

        self.labm_drr_pixel_spacing = QLabel(self.gbo_drr_info)
        self.labm_drr_pixel_spacing.setObjectName(u"labm_drr_pixel_spacing")
        self.labm_drr_pixel_spacing.setMinimumSize(QSize(60, 20))
        self.labm_drr_pixel_spacing.setMaximumSize(QSize(16777215, 23))
        self.labm_drr_pixel_spacing.setFont(font1)

        self.gridLayout.addWidget(self.labm_drr_pixel_spacing, 5, 1, 1, 3)

        self.pbu_gen_button = QPushButton(self.gbo_drr_info)
        self.pbu_gen_button.setObjectName(u"pbu_gen_button")
        self.pbu_gen_button.setMinimumSize(QSize(100, 25))
        self.pbu_gen_button.setMaximumSize(QSize(100, 25))
        self.pbu_gen_button.setFont(font)

        self.gridLayout.addWidget(self.pbu_gen_button, 0, 4, 1, 2)

        self.lab_drr_angle = QLabel(self.gbo_drr_info)
        self.lab_drr_angle.setObjectName(u"lab_drr_angle")
        self.lab_drr_angle.setMaximumSize(QSize(16777215, 20))
        self.lab_drr_angle.setFont(font1)

        self.gridLayout.addWidget(self.lab_drr_angle, 0, 2, 1, 1)

        self.lab_drr_size = QLabel(self.gbo_drr_info)
        self.lab_drr_size.setObjectName(u"lab_drr_size")
        self.lab_drr_size.setMaximumSize(QSize(16777215, 20))
        self.lab_drr_size.setFont(font1)

        self.gridLayout.addWidget(self.lab_drr_size, 4, 0, 1, 1)

        self.led_drr_width = QLineEdit(self.gbo_drr_info)
        self.led_drr_width.setObjectName(u"led_drr_width")
        self.led_drr_width.setMinimumSize(QSize(50, 23))
        self.led_drr_width.setMaximumSize(QSize(50, 23))
        self.led_drr_width.setFont(font1)
        self.led_drr_width.setFrame(True)
        self.led_drr_width.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.led_drr_width.setDragEnabled(False)
        self.led_drr_width.setReadOnly(False)
        self.led_drr_width.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.led_drr_width.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.led_drr_width, 0, 1, 1, 1)

        self.lab_drr_height = QLabel(self.gbo_drr_info)
        self.lab_drr_height.setObjectName(u"lab_drr_height")
        self.lab_drr_height.setMaximumSize(QSize(16777215, 20))
        self.lab_drr_height.setFont(font1)

        self.gridLayout.addWidget(self.lab_drr_height, 1, 0, 1, 1)

        self.led_drr_threshold = QLineEdit(self.gbo_drr_info)
        self.led_drr_threshold.setObjectName(u"led_drr_threshold")
        self.led_drr_threshold.setMinimumSize(QSize(50, 23))
        self.led_drr_threshold.setMaximumSize(QSize(50, 23))
        self.led_drr_threshold.setCursor(QCursor(Qt.IBeamCursor))
        self.led_drr_threshold.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.led_drr_threshold, 1, 3, 1, 1)

        self.lab_drr_threshold = QLabel(self.gbo_drr_info)
        self.lab_drr_threshold.setObjectName(u"lab_drr_threshold")
        self.lab_drr_threshold.setMaximumSize(QSize(16777215, 20))

        self.gridLayout.addWidget(self.lab_drr_threshold, 1, 2, 1, 1)

        self.lab_drr_width = QLabel(self.gbo_drr_info)
        self.lab_drr_width.setObjectName(u"lab_drr_width")
        self.lab_drr_width.setMaximumSize(QSize(16777215, 20))
        self.lab_drr_width.setFont(font1)

        self.gridLayout.addWidget(self.lab_drr_width, 0, 0, 1, 1)

        self.led_drr_angle = QLineEdit(self.gbo_drr_info)
        self.led_drr_angle.setObjectName(u"led_drr_angle")
        self.led_drr_angle.setMinimumSize(QSize(50, 23))
        self.led_drr_angle.setMaximumSize(QSize(50, 23))
        self.led_drr_angle.setFont(font1)
        self.led_drr_angle.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.led_drr_angle, 0, 3, 1, 1)

        self.led_drr_height = QLineEdit(self.gbo_drr_info)
        self.led_drr_height.setObjectName(u"led_drr_height")
        self.led_drr_height.setMinimumSize(QSize(50, 23))
        self.led_drr_height.setMaximumSize(QSize(50, 23))
        self.led_drr_height.setFont(font1)
        self.led_drr_height.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.led_drr_height.setDragEnabled(True)
        self.led_drr_height.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.gridLayout.addWidget(self.led_drr_height, 1, 1, 1, 1)


        self.gridLayout_5.addWidget(self.gbo_drr_info, 2, 0, 1, 2)

        self.gbo_xray_info = QGroupBox(win_drr_gen)
        self.gbo_xray_info.setObjectName(u"gbo_xray_info")
        self.gbo_xray_info.setMaximumSize(QSize(16777215, 175))
        self.gbo_xray_info.setFont(font)
        self.gridLayout_3 = QGridLayout(self.gbo_xray_info)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(15)
        self.gridLayout_3.setVerticalSpacing(10)
        self.gridLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.lab_xray_size = QLabel(self.gbo_xray_info)
        self.lab_xray_size.setObjectName(u"lab_xray_size")
        self.lab_xray_size.setMinimumSize(QSize(0, 20))
        self.lab_xray_size.setMaximumSize(QSize(16777215, 20))
        self.lab_xray_size.setFont(font1)

        self.gridLayout_3.addWidget(self.lab_xray_size, 4, 0, 1, 2)

        self.lab_xray_sdd = QLabel(self.gbo_xray_info)
        self.lab_xray_sdd.setObjectName(u"lab_xray_sdd")
        self.lab_xray_sdd.setMinimumSize(QSize(0, 20))
        self.lab_xray_sdd.setMaximumSize(QSize(16777215, 20))
        self.lab_xray_sdd.setFont(font1)
        self.lab_xray_sdd.setWordWrap(False)
        self.lab_xray_sdd.setMargin(0)

        self.gridLayout_3.addWidget(self.lab_xray_sdd, 3, 0, 1, 2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 0, 3, 1, 1)

        self.labm_xray_name = QLabel(self.gbo_xray_info)
        self.labm_xray_name.setObjectName(u"labm_xray_name")
        self.labm_xray_name.setMinimumSize(QSize(100, 23))
        self.labm_xray_name.setMaximumSize(QSize(16777215, 23))
        self.labm_xray_name.setFont(font1)

        self.gridLayout_3.addWidget(self.labm_xray_name, 2, 2, 1, 2)

        self.labm_xray_sdd = QLabel(self.gbo_xray_info)
        self.labm_xray_sdd.setObjectName(u"labm_xray_sdd")
        self.labm_xray_sdd.setMinimumSize(QSize(100, 23))
        self.labm_xray_sdd.setMaximumSize(QSize(16777215, 23))
        self.labm_xray_sdd.setFont(font1)

        self.gridLayout_3.addWidget(self.labm_xray_sdd, 3, 2, 1, 2)

        self.labm_xray_size = QLabel(self.gbo_xray_info)
        self.labm_xray_size.setObjectName(u"labm_xray_size")
        self.labm_xray_size.setMinimumSize(QSize(100, 23))
        self.labm_xray_size.setMaximumSize(QSize(16777215, 23))
        self.labm_xray_size.setFont(font1)

        self.gridLayout_3.addWidget(self.labm_xray_size, 4, 2, 1, 2)

        self.labm_xray_pixel_spacing = QLabel(self.gbo_xray_info)
        self.labm_xray_pixel_spacing.setObjectName(u"labm_xray_pixel_spacing")
        self.labm_xray_pixel_spacing.setMinimumSize(QSize(100, 23))
        self.labm_xray_pixel_spacing.setMaximumSize(QSize(16777215, 23))
        self.labm_xray_pixel_spacing.setFont(font1)

        self.gridLayout_3.addWidget(self.labm_xray_pixel_spacing, 5, 2, 2, 2)

        self.lab_xray_pixel_spacing = QLabel(self.gbo_xray_info)
        self.lab_xray_pixel_spacing.setObjectName(u"lab_xray_pixel_spacing")
        self.lab_xray_pixel_spacing.setMinimumSize(QSize(0, 20))
        self.lab_xray_pixel_spacing.setMaximumSize(QSize(16777215, 20))
        self.lab_xray_pixel_spacing.setFont(font1)

        self.gridLayout_3.addWidget(self.lab_xray_pixel_spacing, 5, 0, 2, 2)

        self.lab_xray_name = QLabel(self.gbo_xray_info)
        self.lab_xray_name.setObjectName(u"lab_xray_name")
        self.lab_xray_name.setMinimumSize(QSize(0, 20))
        self.lab_xray_name.setMaximumSize(QSize(16777215, 20))
        self.lab_xray_name.setFont(font1)

        self.gridLayout_3.addWidget(self.lab_xray_name, 2, 0, 1, 2)

        self.lab_xray_loaded = QLabel(self.gbo_xray_info)
        self.lab_xray_loaded.setObjectName(u"lab_xray_loaded")
        self.lab_xray_loaded.setMinimumSize(QSize(0, 20))
        self.lab_xray_loaded.setMaximumSize(QSize(16777215, 20))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(False)
        self.lab_xray_loaded.setFont(font2)

        self.gridLayout_3.addWidget(self.lab_xray_loaded, 0, 0, 1, 2)

        self.labm_xray_loaded = QLabel(self.gbo_xray_info)
        self.labm_xray_loaded.setObjectName(u"labm_xray_loaded")
        self.labm_xray_loaded.setMinimumSize(QSize(20, 20))
        self.labm_xray_loaded.setMaximumSize(QSize(20, 20))
        self.labm_xray_loaded.setScaledContents(True)
        self.labm_xray_loaded.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.labm_xray_loaded, 0, 2, 1, 1)


        self.gridLayout_5.addWidget(self.gbo_xray_info, 0, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_3, 3, 0, 1, 2)

        QWidget.setTabOrder(self.led_drr_width, self.led_drr_height)
        QWidget.setTabOrder(self.led_drr_height, self.led_drr_angle)
        QWidget.setTabOrder(self.led_drr_angle, self.led_drr_threshold)
        QWidget.setTabOrder(self.led_drr_threshold, self.pbu_gen_button)

        self.retranslateUi(win_drr_gen)

        QMetaObject.connectSlotsByName(win_drr_gen)
    # setupUi

    def retranslateUi(self, win_drr_gen):
        win_drr_gen.setWindowTitle(QCoreApplication.translate("win_drr_gen", u"Vytvo\u0159it DRR obraz", None))
        self.gbo_ct_info.setTitle(QCoreApplication.translate("win_drr_gen", u"CT \u0159ezy", None))
        self.lab_slice_thickness.setText(QCoreApplication.translate("win_drr_gen", u"Tlou\u0161\u0165ka \u0159ezu (mm):", None))
        self.lab_slice_count.setText(QCoreApplication.translate("win_drr_gen", u"Po\u010det \u0159ez\u016f:", None))
        self.lab_ct_name.setText(QCoreApplication.translate("win_drr_gen", u"N\u00e1zev:", None))
        self.lab_ct_loaded.setText(QCoreApplication.translate("win_drr_gen", u"Data na\u010dten\u00e9:", None))
        self.labm_ct_name.setText(QCoreApplication.translate("win_drr_gen", u"-", None))
        self.labm_slice_count.setText(QCoreApplication.translate("win_drr_gen", u"-", None))
        self.labm_slice_thickness.setText(QCoreApplication.translate("win_drr_gen", u"-", None))
        self.labm_ct_loaded.setText("")
        self.gbo_drr_info.setTitle(QCoreApplication.translate("win_drr_gen", u"DRR obraz", None))
        self.lab_drr_pixel_spacing.setText(QCoreApplication.translate("win_drr_gen", u"Rozm\u011bry pixelu (mm):", None))
        self.labm_drr_size.setText(QCoreApplication.translate("win_drr_gen", u"-", None))
        self.labm_drr_pixel_spacing.setText(QCoreApplication.translate("win_drr_gen", u"-", None))
        self.pbu_gen_button.setText(QCoreApplication.translate("win_drr_gen", u"Vytvo\u0159it DRR", None))
        self.lab_drr_angle.setText(QCoreApplication.translate("win_drr_gen", u"\u00dahel (\u00b0):", None))
        self.lab_drr_size.setText(QCoreApplication.translate("win_drr_gen", u"Velikost obrazu (px):", None))
        self.led_drr_width.setInputMask("")
        self.led_drr_width.setText(QCoreApplication.translate("win_drr_gen", u"1024", None))
        self.led_drr_width.setPlaceholderText("")
        self.lab_drr_height.setText(QCoreApplication.translate("win_drr_gen", u"V\u00fd\u0161ka (px):", None))
        self.led_drr_threshold.setText(QCoreApplication.translate("win_drr_gen", u"200", None))
        self.lab_drr_threshold.setText(QCoreApplication.translate("win_drr_gen", u"Pr\u00e1h:", None))
        self.lab_drr_width.setText(QCoreApplication.translate("win_drr_gen", u"\u0160\u00ed\u0159ka (px):", None))
        self.led_drr_angle.setText(QCoreApplication.translate("win_drr_gen", u"0", None))
        self.led_drr_height.setText(QCoreApplication.translate("win_drr_gen", u"1024", None))
        self.gbo_xray_info.setTitle(QCoreApplication.translate("win_drr_gen", u"RTG obraz", None))
        self.lab_xray_size.setText(QCoreApplication.translate("win_drr_gen", u"Velikost obrazu (px):", None))
        self.lab_xray_sdd.setText(QCoreApplication.translate("win_drr_gen", u"Vzd\u00e1lenost zdroj-detektor (mm):", None))
        self.labm_xray_name.setText(QCoreApplication.translate("win_drr_gen", u"-", None))
        self.labm_xray_sdd.setText(QCoreApplication.translate("win_drr_gen", u"-", None))
        self.labm_xray_size.setText(QCoreApplication.translate("win_drr_gen", u"-", None))
        self.labm_xray_pixel_spacing.setText(QCoreApplication.translate("win_drr_gen", u"-", None))
        self.lab_xray_pixel_spacing.setText(QCoreApplication.translate("win_drr_gen", u"Rozm\u011bry pixelu (mm):", None))
        self.lab_xray_name.setText(QCoreApplication.translate("win_drr_gen", u"N\u00e1zev:", None))
        self.lab_xray_loaded.setText(QCoreApplication.translate("win_drr_gen", u"Data na\u010dten\u00e9:", None))
        self.labm_xray_loaded.setText("")
    # retranslateUi

