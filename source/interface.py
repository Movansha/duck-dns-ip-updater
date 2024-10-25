# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(418, 378)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        MainWindow.setWindowTitle(u"Duck DNS IP Updater")
        icon = QIcon()
        icon.addFile(u":/images/resources/window.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background: #f7f7f7; font: 11pt \"Nirmala UI\"; color: #000000;")
        MainWindow.setIconSize(QSize(32, 32))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.central_Layout = QGridLayout(self.centralwidget)
        self.central_Layout.setObjectName(u"central_Layout")
        self.central_Layout.setHorizontalSpacing(5)
        self.central_Layout.setVerticalSpacing(10)
        self.central_Layout.setContentsMargins(10, 15, 10, 10)
        self.header_Spacer3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.central_Layout.addItem(self.header_Spacer3, 0, 3, 1, 1)

        self.header_Spacer4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.central_Layout.addItem(self.header_Spacer4, 0, 4, 1, 1)

        self.vertical_Spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.central_Layout.addItem(self.vertical_Spacer, 6, 1, 1, 3)

        self.header_Spacer2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.central_Layout.addItem(self.header_Spacer2, 0, 1, 1, 1)

        self.header_Spacer1 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.central_Layout.addItem(self.header_Spacer1, 0, 0, 1, 1)

        self.domain_Widget = QWidget(self.centralwidget)
        self.domain_Widget.setObjectName(u"domain_Widget")
        sizePolicy.setHeightForWidth(self.domain_Widget.sizePolicy().hasHeightForWidth())
        self.domain_Widget.setSizePolicy(sizePolicy)
        self.domain_Widget.setMinimumSize(QSize(0, 0))
        self.domain_Widget.setMaximumSize(QSize(16777215, 100))
        self.domain_Widget.setStyleSheet(u"background: #f0f0f0; border: 2 solid #ececec; border-radius: 15;")
        self.domain_Layout = QHBoxLayout(self.domain_Widget)
        self.domain_Layout.setSpacing(15)
        self.domain_Layout.setObjectName(u"domain_Layout")
        self.domain_Layout.setContentsMargins(25, 15, 25, 15)
        self.domain_Label = QLabel(self.domain_Widget)
        self.domain_Label.setObjectName(u"domain_Label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.domain_Label.sizePolicy().hasHeightForWidth())
        self.domain_Label.setSizePolicy(sizePolicy1)
        self.domain_Label.setMaximumSize(QSize(16777215, 16777215))
        self.domain_Label.setSizeIncrement(QSize(0, 0))
        self.domain_Label.setStyleSheet(u"border: 0;")

        self.domain_Layout.addWidget(self.domain_Label)

        self.domain_LineEdit = QLineEdit(self.domain_Widget)
        self.domain_LineEdit.setObjectName(u"domain_LineEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.domain_LineEdit.sizePolicy().hasHeightForWidth())
        self.domain_LineEdit.setSizePolicy(sizePolicy2)
        self.domain_LineEdit.setMinimumSize(QSize(208, 30))
        self.domain_LineEdit.setMaximumSize(QSize(16777215, 36))
        self.domain_LineEdit.setStyleSheet(u"QLineEdit {background: #f6f6f6; font: 10pt \"Nirmala UI\"; border: 1 solid #acacac; border-radius: 10;}\n"
"QLineEdit::focus {border: 1 solid #2590cc;}")
        self.domain_LineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.domain_Layout.addWidget(self.domain_LineEdit)


        self.central_Layout.addWidget(self.domain_Widget, 3, 1, 1, 3)

        self.token_Widget = QWidget(self.centralwidget)
        self.token_Widget.setObjectName(u"token_Widget")
        sizePolicy.setHeightForWidth(self.token_Widget.sizePolicy().hasHeightForWidth())
        self.token_Widget.setSizePolicy(sizePolicy)
        self.token_Widget.setMinimumSize(QSize(0, 0))
        self.token_Widget.setMaximumSize(QSize(16777215, 100))
        self.token_Widget.setStyleSheet(u"background: #f0f0f0; border: 2 solid #ececec; border-radius: 15;")
        self.token_Layout = QHBoxLayout(self.token_Widget)
        self.token_Layout.setSpacing(15)
        self.token_Layout.setObjectName(u"token_Layout")
        self.token_Layout.setContentsMargins(25, 15, 25, 15)
        self.token_Label = QLabel(self.token_Widget)
        self.token_Label.setObjectName(u"token_Label")
        sizePolicy1.setHeightForWidth(self.token_Label.sizePolicy().hasHeightForWidth())
        self.token_Label.setSizePolicy(sizePolicy1)
        self.token_Label.setSizeIncrement(QSize(0, 0))
        self.token_Label.setStyleSheet(u"border: 0;")

        self.token_Layout.addWidget(self.token_Label)

        self.token_LineEdit = QLineEdit(self.token_Widget)
        self.token_LineEdit.setObjectName(u"token_LineEdit")
        sizePolicy2.setHeightForWidth(self.token_LineEdit.sizePolicy().hasHeightForWidth())
        self.token_LineEdit.setSizePolicy(sizePolicy2)
        self.token_LineEdit.setMinimumSize(QSize(208, 30))
        self.token_LineEdit.setMaximumSize(QSize(16777215, 36))
        self.token_LineEdit.setStyleSheet(u"QLineEdit {background: #f6f6f6; font: 10pt \"Nirmala UI\"; border: 1 solid #acacac; border-radius: 10;}\n"
"QLineEdit::focus {border: 1 solid #2590cc;}")
        self.token_LineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.token_Layout.addWidget(self.token_LineEdit)


        self.central_Layout.addWidget(self.token_Widget, 4, 1, 1, 3)

        self.interval_Widget = QWidget(self.centralwidget)
        self.interval_Widget.setObjectName(u"interval_Widget")
        sizePolicy.setHeightForWidth(self.interval_Widget.sizePolicy().hasHeightForWidth())
        self.interval_Widget.setSizePolicy(sizePolicy)
        self.interval_Widget.setMinimumSize(QSize(0, 0))
        self.interval_Widget.setMaximumSize(QSize(16777215, 100))
        self.interval_Widget.setStyleSheet(u"background: #f0f0f0; border: 2 solid #ececec; border-radius: 15;")
        self.interval_Layout = QHBoxLayout(self.interval_Widget)
        self.interval_Layout.setSpacing(15)
        self.interval_Layout.setObjectName(u"interval_Layout")
        self.interval_Layout.setContentsMargins(25, 15, 25, 15)
        self.interval_Label = QLabel(self.interval_Widget)
        self.interval_Label.setObjectName(u"interval_Label")
        sizePolicy1.setHeightForWidth(self.interval_Label.sizePolicy().hasHeightForWidth())
        self.interval_Label.setSizePolicy(sizePolicy1)
        self.interval_Label.setSizeIncrement(QSize(0, 0))
        self.interval_Label.setStyleSheet(u"border: 0;")

        self.interval_Layout.addWidget(self.interval_Label)

        self.interval_LineEdit = QLineEdit(self.interval_Widget)
        self.interval_LineEdit.setObjectName(u"interval_LineEdit")
        sizePolicy2.setHeightForWidth(self.interval_LineEdit.sizePolicy().hasHeightForWidth())
        self.interval_LineEdit.setSizePolicy(sizePolicy2)
        self.interval_LineEdit.setMinimumSize(QSize(108, 30))
        self.interval_LineEdit.setMaximumSize(QSize(16777215, 36))
        self.interval_LineEdit.setStyleSheet(u"QLineEdit {background: #f6f6f6; font: 10pt \"Nirmala UI\"; border: 1 solid #acacac; border-radius: 10;}\n"
"QLineEdit::focus {border: 1 solid #2590cc;}")
        self.interval_LineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.interval_Layout.addWidget(self.interval_LineEdit)


        self.central_Layout.addWidget(self.interval_Widget, 5, 1, 1, 3)

        self.header_Label = QLabel(self.centralwidget)
        self.header_Label.setObjectName(u"header_Label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.header_Label.sizePolicy().hasHeightForWidth())
        self.header_Label.setSizePolicy(sizePolicy3)
        self.header_Label.setStyleSheet(u"font: 14pt \"Nirmala UI\";")

        self.central_Layout.addWidget(self.header_Label, 0, 2, 1, 1)

        self.apply_Button = QPushButton(self.centralwidget)
        self.apply_Button.setObjectName(u"apply_Button")
        sizePolicy2.setHeightForWidth(self.apply_Button.sizePolicy().hasHeightForWidth())
        self.apply_Button.setSizePolicy(sizePolicy2)
        self.apply_Button.setMinimumSize(QSize(80, 35))
        self.apply_Button.setMaximumSize(QSize(135, 38))
        self.apply_Button.setFocusPolicy(Qt.FocusPolicy.TabFocus)
        self.apply_Button.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.apply_Button.setStyleSheet(u"QPushButton {background: #808080; font: 10pt \"Nirmala UI\"; color: #ffffff; border: 2 solid #959595; border-radius: 10;}\n"
"QPushButton::hover {background: #9d9d9d; border: 2 solid #a9a9a9;}\n"
"QPushButton::focus {background: #9d9d9d; border: 2 solid #a9a9a9;}\n"
"QPushButton::pressed {background: #808080; border: 2 solid #959595;}")

        self.central_Layout.addWidget(self.apply_Button, 7, 2, 1, 3)

        self.header_Line = QFrame(self.centralwidget)
        self.header_Line.setObjectName(u"header_Line")
        self.header_Line.setMinimumSize(QSize(0, 1))
        self.header_Line.setMaximumSize(QSize(16777215, 1))
        self.header_Line.setStyleSheet(u"background: #a9a9a9;")
        self.header_Line.setFrameShape(QFrame.Shape.HLine)
        self.header_Line.setFrameShadow(QFrame.Shadow.Sunken)

        self.central_Layout.addWidget(self.header_Line, 2, 2, 1, 1)

        self.web_Button = QPushButton(self.centralwidget)
        self.web_Button.setObjectName(u"web_Button")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.web_Button.sizePolicy().hasHeightForWidth())
        self.web_Button.setSizePolicy(sizePolicy4)
        self.web_Button.setMinimumSize(QSize(50, 50))
        self.web_Button.setMaximumSize(QSize(50, 50))
        self.web_Button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.web_Button.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.web_Button.setStyleSheet(u"background: #f7f7f7; border: 0;")
        icon1 = QIcon()
        icon1.addFile(u":/images/resources/duck.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.web_Button.setIcon(icon1)
        self.web_Button.setIconSize(QSize(50, 50))

        self.central_Layout.addWidget(self.web_Button, 7, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
#if QT_CONFIG(shortcut)
        self.domain_Label.setBuddy(self.domain_LineEdit)
        self.token_Label.setBuddy(self.token_LineEdit)
        self.interval_Label.setBuddy(self.interval_LineEdit)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.domain_LineEdit, self.token_LineEdit)
        QWidget.setTabOrder(self.token_LineEdit, self.interval_LineEdit)
        QWidget.setTabOrder(self.interval_LineEdit, self.apply_Button)

        self.retranslateUi(MainWindow)

        self.apply_Button.setDefault(True)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        self.domain_Label.setText(QCoreApplication.translate("MainWindow", u"Your domain :", None))
        self.domain_LineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"domain ", None))
        self.token_Label.setText(QCoreApplication.translate("MainWindow", u"Your token :", None))
        self.token_LineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"token", None))
        self.interval_Label.setText(QCoreApplication.translate("MainWindow", u"Update interval (minutes) :", None))
        self.interval_LineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"interval", None))
        self.header_Label.setText(QCoreApplication.translate("MainWindow", u"Duck DNS IP Updater", None))
        self.apply_Button.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        pass
    # retranslateUi
