# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Demo.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Demo(object):
    def setupUi(self, Demo):
        Demo.setObjectName("Demo")
        Demo.resize(870, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Demo.sizePolicy().hasHeightForWidth())
        Demo.setSizePolicy(sizePolicy)
        Demo.setMinimumSize(QtCore.QSize(500, 600))
        Demo.setMaximumSize(QtCore.QSize(1000, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../_images/aperture-1142967_960_720.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Demo.setWindowIcon(icon)
        self.centralWidget = QtWidgets.QWidget(Demo)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 10, 341, 241))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.IST_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.IST_label.setObjectName("IST_label")
        self.verticalLayout_2.addWidget(self.IST_label)
        self.IST_Editor = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.IST_Editor.setEnabled(False)
        self.IST_Editor.setObjectName("IST_Editor")
        self.verticalLayout_2.addWidget(self.IST_Editor)
        self.ICI_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.ICI_label.setObjectName("ICI_label")
        self.verticalLayout_2.addWidget(self.ICI_label)
        self.ICI_spinBox = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.ICI_spinBox.setEnabled(False)
        self.ICI_spinBox.setMinimum(1)
        self.ICI_spinBox.setMaximum(999999999)
        self.ICI_spinBox.setObjectName("ICI_spinBox")
        self.verticalLayout_2.addWidget(self.ICI_spinBox)
        self.ISD_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.ISD_label.setObjectName("ISD_label")
        self.verticalLayout_2.addWidget(self.ISD_label)
        self.ISD_spinBox = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.ISD_spinBox.setEnabled(False)
        self.ISD_spinBox.setMinimum(1)
        self.ISD_spinBox.setMaximum(999999999)
        self.ISD_spinBox.setObjectName("ISD_spinBox")
        self.verticalLayout_2.addWidget(self.ISD_spinBox)
        self.Lower_Bay_Display = QtWidgets.QFrame(self.centralWidget)
        self.Lower_Bay_Display.setGeometry(QtCore.QRect(400, 230, 431, 161))
        self.Lower_Bay_Display.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Lower_Bay_Display.setFrameShape(QtWidgets.QFrame.Box)
        self.Lower_Bay_Display.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Lower_Bay_Display.setLineWidth(3)
        self.Lower_Bay_Display.setObjectName("Lower_Bay_Display")
        self.line_3 = QtWidgets.QFrame(self.Lower_Bay_Display)
        self.line_3.setGeometry(QtCore.QRect(10, 70, 411, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.Unit_0_Label = QtWidgets.QLabel(self.Lower_Bay_Display)
        self.Unit_0_Label.setGeometry(QtCore.QRect(30, 20, 50, 50))
        self.Unit_0_Label.setText("")
        self.Unit_0_Label.setPixmap(QtGui.QPixmap("../_images/stop-red.png"))
        self.Unit_0_Label.setScaledContents(True)
        self.Unit_0_Label.setObjectName("Unit_0_Label")
        self.Unit_2_Label = QtWidgets.QLabel(self.Lower_Bay_Display)
        self.Unit_2_Label.setGeometry(QtCore.QRect(110, 20, 50, 50))
        self.Unit_2_Label.setText("")
        self.Unit_2_Label.setPixmap(QtGui.QPixmap("../_images/stop-red.png"))
        self.Unit_2_Label.setScaledContents(True)
        self.Unit_2_Label.setObjectName("Unit_2_Label")
        self.Unit_6_Label = QtWidgets.QLabel(self.Lower_Bay_Display)
        self.Unit_6_Label.setGeometry(QtCore.QRect(270, 20, 50, 50))
        self.Unit_6_Label.setText("")
        self.Unit_6_Label.setPixmap(QtGui.QPixmap("../_images/stop-red.png"))
        self.Unit_6_Label.setScaledContents(True)
        self.Unit_6_Label.setObjectName("Unit_6_Label")
        self.Unit_4_Label = QtWidgets.QLabel(self.Lower_Bay_Display)
        self.Unit_4_Label.setGeometry(QtCore.QRect(190, 20, 50, 50))
        self.Unit_4_Label.setText("")
        self.Unit_4_Label.setPixmap(QtGui.QPixmap("../_images/stop-red.png"))
        self.Unit_4_Label.setScaledContents(True)
        self.Unit_4_Label.setObjectName("Unit_4_Label")
        self.Unit_1_Label = QtWidgets.QLabel(self.Lower_Bay_Display)
        self.Unit_1_Label.setEnabled(True)
        self.Unit_1_Label.setGeometry(QtCore.QRect(30, 90, 50, 50))
        self.Unit_1_Label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Unit_1_Label.setText("")
        self.Unit_1_Label.setPixmap(QtGui.QPixmap("../_images/stop-red.png"))
        self.Unit_1_Label.setScaledContents(True)
        self.Unit_1_Label.setObjectName("Unit_1_Label")
        self.Unit_3_Label = QtWidgets.QLabel(self.Lower_Bay_Display)
        self.Unit_3_Label.setGeometry(QtCore.QRect(110, 90, 50, 50))
        self.Unit_3_Label.setText("")
        self.Unit_3_Label.setPixmap(QtGui.QPixmap("../_images/stop-red.png"))
        self.Unit_3_Label.setScaledContents(True)
        self.Unit_3_Label.setObjectName("Unit_3_Label")
        self.Unit_5_Label = QtWidgets.QLabel(self.Lower_Bay_Display)
        self.Unit_5_Label.setGeometry(QtCore.QRect(190, 90, 50, 50))
        self.Unit_5_Label.setText("")
        self.Unit_5_Label.setPixmap(QtGui.QPixmap("../_images/stop-red.png"))
        self.Unit_5_Label.setScaledContents(True)
        self.Unit_5_Label.setObjectName("Unit_5_Label")
        self.Unit_7_Label = QtWidgets.QLabel(self.Lower_Bay_Display)
        self.Unit_7_Label.setGeometry(QtCore.QRect(270, 90, 50, 50))
        self.Unit_7_Label.setText("")
        self.Unit_7_Label.setPixmap(QtGui.QPixmap("../_images/stop-red.png"))
        self.Unit_7_Label.setScaledContents(True)
        self.Unit_7_Label.setObjectName("Unit_7_Label")
        self.Unit_8_Label = QtWidgets.QLabel(self.Lower_Bay_Display)
        self.Unit_8_Label.setGeometry(QtCore.QRect(350, 20, 50, 50))
        self.Unit_8_Label.setText("")
        self.Unit_8_Label.setPixmap(QtGui.QPixmap("../_images/stop-red.png"))
        self.Unit_8_Label.setScaledContents(True)
        self.Unit_8_Label.setObjectName("Unit_8_Label")
        self.Unit_9_Label = QtWidgets.QLabel(self.Lower_Bay_Display)
        self.Unit_9_Label.setGeometry(QtCore.QRect(350, 90, 50, 50))
        self.Unit_9_Label.setText("")
        self.Unit_9_Label.setPixmap(QtGui.QPixmap("../_images/stop-red.png"))
        self.Unit_9_Label.setScaledContents(True)
        self.Unit_9_Label.setObjectName("Unit_9_Label")
        self.Upper_Bay_Display = QtWidgets.QFrame(self.centralWidget)
        self.Upper_Bay_Display.setGeometry(QtCore.QRect(400, 30, 431, 161))
        self.Upper_Bay_Display.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Upper_Bay_Display.setFrameShape(QtWidgets.QFrame.Box)
        self.Upper_Bay_Display.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Upper_Bay_Display.setLineWidth(3)
        self.Upper_Bay_Display.setObjectName("Upper_Bay_Display")
        self.line_5 = QtWidgets.QFrame(self.Upper_Bay_Display)
        self.line_5.setGeometry(QtCore.QRect(10, 70, 411, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.Unit_10_Label = QtWidgets.QLabel(self.Upper_Bay_Display)
        self.Unit_10_Label.setGeometry(QtCore.QRect(30, 20, 50, 50))
        self.Unit_10_Label.setText("")
        self.Unit_10_Label.setPixmap(QtGui.QPixmap("../_images/stop-red.png"))
        self.Unit_10_Label.setScaledContents(True)
        self.Unit_10_Label.setObjectName("Unit_10_Label")
        self.Unit_12_Label = QtWidgets.QLabel(self.Upper_Bay_Display)
        self.Unit_12_Label.setGeometry(QtCore.QRect(110, 20, 50, 50))
        self.Unit_12_Label.setText("")
        self.Unit_12_Label.setPixmap(QtGui.QPixmap("../_images/stop-red.png"))
        self.Unit_12_Label.setScaledContents(True)
        self.Unit_12_Label.setObjectName("Unit_12_Label")
        self.Unit_16_Label = QtWidgets.QLabel(self.Upper_Bay_Display)
        self.Unit_16_Label.setGeometry(QtCore.QRect(270, 20, 50, 50))
        self.Unit_16_Label.setText("")
        self.Unit_16_Label.setPixmap(QtGui.QPixmap("../_images/stop-red.png"))
        self.Unit_16_Label.setScaledContents(True)
        self.Unit_16_Label.setObjectName("Unit_16_Label")
        self.Unit_14_Label = QtWidgets.QLabel(self.Upper_Bay_Display)
        self.Unit_14_Label.setGeometry(QtCore.QRect(190, 20, 50, 50))
        self.Unit_14_Label.setText("")
        self.Unit_14_Label.setPixmap(QtGui.QPixmap("../_images/stop-red.png"))
        self.Unit_14_Label.setScaledContents(True)
        self.Unit_14_Label.setObjectName("Unit_14_Label")
        self.Unit_11_Label = QtWidgets.QLabel(self.Upper_Bay_Display)
        self.Unit_11_Label.setGeometry(QtCore.QRect(30, 90, 50, 50))
        self.Unit_11_Label.setText("")
        self.Unit_11_Label.setPixmap(QtGui.QPixmap("../_images/stop-red.png"))
        self.Unit_11_Label.setScaledContents(True)
        self.Unit_11_Label.setObjectName("Unit_11_Label")
        self.Unit_13_Label = QtWidgets.QLabel(self.Upper_Bay_Display)
        self.Unit_13_Label.setGeometry(QtCore.QRect(110, 90, 50, 50))
        self.Unit_13_Label.setText("")
        self.Unit_13_Label.setPixmap(QtGui.QPixmap("../_images/stop-red.png"))
        self.Unit_13_Label.setScaledContents(True)
        self.Unit_13_Label.setObjectName("Unit_13_Label")
        self.Unit_15_Label = QtWidgets.QLabel(self.Upper_Bay_Display)
        self.Unit_15_Label.setGeometry(QtCore.QRect(190, 90, 50, 50))
        self.Unit_15_Label.setText("")
        self.Unit_15_Label.setPixmap(QtGui.QPixmap("../_images/stop-red.png"))
        self.Unit_15_Label.setScaledContents(True)
        self.Unit_15_Label.setObjectName("Unit_15_Label")
        self.Unit_17_Label = QtWidgets.QLabel(self.Upper_Bay_Display)
        self.Unit_17_Label.setGeometry(QtCore.QRect(270, 90, 50, 50))
        self.Unit_17_Label.setText("")
        self.Unit_17_Label.setPixmap(QtGui.QPixmap("../_images/stop-red.png"))
        self.Unit_17_Label.setScaledContents(True)
        self.Unit_17_Label.setObjectName("Unit_17_Label")
        self.Unit_19_Label = QtWidgets.QLabel(self.Upper_Bay_Display)
        self.Unit_19_Label.setGeometry(QtCore.QRect(350, 90, 50, 50))
        self.Unit_19_Label.setText("")
        self.Unit_19_Label.setPixmap(QtGui.QPixmap("../_images/stop-red.png"))
        self.Unit_19_Label.setScaledContents(True)
        self.Unit_19_Label.setObjectName("Unit_19_Label")
        self.Unit_18_Label = QtWidgets.QLabel(self.Upper_Bay_Display)
        self.Unit_18_Label.setGeometry(QtCore.QRect(350, 20, 50, 50))
        self.Unit_18_Label.setText("")
        self.Unit_18_Label.setPixmap(QtGui.QPixmap("../_images/stop-red.png"))
        self.Unit_18_Label.setScaledContents(True)
        self.Unit_18_Label.setObjectName("Unit_18_Label")
        self.Upper_Bay_Label = QtWidgets.QLabel(self.centralWidget)
        self.Upper_Bay_Label.setGeometry(QtCore.QRect(570, 200, 111, 21))
        self.Upper_Bay_Label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Upper_Bay_Label.setObjectName("Upper_Bay_Label")
        self.Lower_Bay_Label = QtWidgets.QLabel(self.centralWidget)
        self.Lower_Bay_Label.setGeometry(QtCore.QRect(570, 395, 111, 21))
        self.Lower_Bay_Label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Lower_Bay_Label.setObjectName("Lower_Bay_Label")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralWidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(40, 320, 341, 101))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Start_Live = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.Start_Live.setEnabled(True)
        self.Start_Live.setObjectName("Start_Live")
        self.verticalLayout.addWidget(self.Start_Live)
        self.Test_Capture = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.Test_Capture.setObjectName("Test_Capture")
        self.verticalLayout.addWidget(self.Test_Capture)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralWidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(40, 420, 781, 171))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Image_Bar = QtWidgets.QProgressBar(self.verticalLayoutWidget_3)
        self.Image_Bar.setEnabled(True)
        self.Image_Bar.setProperty("value", 0)
        self.Image_Bar.setObjectName("Image_Bar")
        self.verticalLayout_3.addWidget(self.Image_Bar)
        self.Update_Status = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.Update_Status.setEnabled(False)
        self.Update_Status.setObjectName("Update_Status")
        self.verticalLayout_3.addWidget(self.Update_Status)
        self.Terminate_Imaging = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.Terminate_Imaging.setEnabled(False)
        self.Terminate_Imaging.setObjectName("Terminate_Imaging")
        self.verticalLayout_3.addWidget(self.Terminate_Imaging)
        self.Start_Imaging = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.Start_Imaging.setEnabled(False)
        self.Start_Imaging.setMinimumSize(QtCore.QSize(2, 0))
        self.Start_Imaging.setObjectName("Start_Imaging")
        self.verticalLayout_3.addWidget(self.Start_Imaging)
        self.StatusBar = QtWidgets.QLabel(self.centralWidget)
        self.StatusBar.setGeometry(QtCore.QRect(60, 265, 301, 41))
        self.StatusBar.setFrameShape(QtWidgets.QFrame.Box)
        self.StatusBar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.StatusBar.setLineWidth(3)
        self.StatusBar.setObjectName("StatusBar")
        Demo.setCentralWidget(self.centralWidget)

        self.retranslateUi(Demo)
        QtCore.QMetaObject.connectSlotsByName(Demo)

    def retranslateUi(self, Demo):
        _translate = QtCore.QCoreApplication.translate
        Demo.setWindowTitle(_translate("Demo", "ABCD COMMAND POINT"))
        self.IST_label.setText(_translate("Demo", "Image Sequence Title:"))
        self.ICI_label.setText(_translate("Demo", "Image Capture Interval:"))
        self.ICI_spinBox.setSuffix(_translate("Demo", " min"))
        self.ISD_label.setText(_translate("Demo", "Image Sequence Duration:"))
        self.ISD_spinBox.setSuffix(_translate("Demo", " min"))
        self.Unit_1_Label.setWhatsThis(_translate("Demo", "Unit one", "asd"))
        self.Upper_Bay_Label.setText(_translate("Demo", "Upper Bay Status:"))
        self.Lower_Bay_Label.setText(_translate("Demo", "Lower Bay Status:"))
        self.Start_Live.setText(_translate("Demo", "Live View"))
        self.Test_Capture.setText(_translate("Demo", "Test Capture"))
        self.Image_Bar.setFormat(_translate("Demo", "%p%"))
        self.Update_Status.setText(_translate("Demo", "Updating Status..."))
        self.Terminate_Imaging.setText(_translate("Demo", "Terminate Imaging"))
        self.Start_Imaging.setText(_translate("Demo", "Start Imaging"))
        self.StatusBar.setText(_translate("Demo", "System Status: Loading..."))

