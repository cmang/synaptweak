# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'synaptweak.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(626, 414)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(0, 0))
        Form.setMaximumSize(QtCore.QSize(99999, 482))
        Form.setToolTip("")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 10, 600, 390))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.palmDetectCheckBox = QtWidgets.QCheckBox(self.widget)
        self.palmDetectCheckBox.setObjectName("palmDetectCheckBox")
        self.horizontalLayout_9.addWidget(self.palmDetectCheckBox)
        self.tapDragCheckBox = QtWidgets.QCheckBox(self.widget)
        self.tapDragCheckBox.setObjectName("tapDragCheckBox")
        self.horizontalLayout_9.addWidget(self.tapDragCheckBox)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout_9, 3, 1, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.quitButton = QtWidgets.QPushButton(self.widget)
        self.quitButton.setObjectName("quitButton")
        self.horizontalLayout_4.addWidget(self.quitButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.reloadButton = QtWidgets.QPushButton(self.widget)
        self.reloadButton.setObjectName("reloadButton")
        self.horizontalLayout_4.addWidget(self.reloadButton)
        self.revertButton = QtWidgets.QPushButton(self.widget)
        self.revertButton.setObjectName("revertButton")
        self.horizontalLayout_4.addWidget(self.revertButton)
        self.exportButton = QtWidgets.QPushButton(self.widget)
        self.exportButton.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.exportButton.setCheckable(False)
        self.exportButton.setObjectName("exportButton")
        self.horizontalLayout_4.addWidget(self.exportButton)
        self.applyButton = QtWidgets.QPushButton(self.widget)
        self.applyButton.setObjectName("applyButton")
        self.horizontalLayout_4.addWidget(self.applyButton)
        self.gridLayout.addLayout(self.horizontalLayout_4, 5, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fingerLowLabel = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.fingerLowLabel.setFont(font)
        self.fingerLowLabel.setToolTip("")
        self.fingerLowLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.fingerLowLabel.setObjectName("fingerLowLabel")
        self.horizontalLayout.addWidget(self.fingerLowLabel)
        self.fingerLowSlider = QtWidgets.QSlider(self.widget)
        self.fingerLowSlider.setToolTip("")
        self.fingerLowSlider.setOrientation(QtCore.Qt.Horizontal)
        self.fingerLowSlider.setObjectName("fingerLowSlider")
        self.horizontalLayout.addWidget(self.fingerLowSlider)
        self.fingerLowEdit = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fingerLowEdit.sizePolicy().hasHeightForWidth())
        self.fingerLowEdit.setSizePolicy(sizePolicy)
        self.fingerLowEdit.setMaximumSize(QtCore.QSize(50, 16777215))
        self.fingerLowEdit.setToolTip("")
        self.fingerLowEdit.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.fingerLowEdit.setObjectName("fingerLowEdit")
        self.horizontalLayout.addWidget(self.fingerLowEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem3 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem3)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout_8.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.fingerHighLabel = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.fingerHighLabel.setFont(font)
        self.fingerHighLabel.setToolTip("")
        self.fingerHighLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.fingerHighLabel.setObjectName("fingerHighLabel")
        self.horizontalLayout_2.addWidget(self.fingerHighLabel)
        self.fingerHighSlider = QtWidgets.QSlider(self.widget)
        self.fingerHighSlider.setOrientation(QtCore.Qt.Horizontal)
        self.fingerHighSlider.setObjectName("fingerHighSlider")
        self.horizontalLayout_2.addWidget(self.fingerHighSlider)
        self.fingerHighEdit = QtWidgets.QLineEdit(self.widget)
        self.fingerHighEdit.setMaximumSize(QtCore.QSize(50, 16777215))
        self.fingerHighEdit.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.fingerHighEdit.setObjectName("fingerHighEdit")
        self.horizontalLayout_2.addWidget(self.fingerHighEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem4 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem4)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_10.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.fingerPressLabel = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.fingerPressLabel.setFont(font)
        self.fingerPressLabel.setToolTip("")
        self.fingerPressLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.fingerPressLabel.setObjectName("fingerPressLabel")
        self.horizontalLayout_3.addWidget(self.fingerPressLabel)
        self.fingerPressSlider = QtWidgets.QSlider(self.widget)
        self.fingerPressSlider.setOrientation(QtCore.Qt.Horizontal)
        self.fingerPressSlider.setObjectName("fingerPressSlider")
        self.horizontalLayout_3.addWidget(self.fingerPressSlider)
        self.fingerPressEdit = QtWidgets.QLineEdit(self.widget)
        self.fingerPressEdit.setMaximumSize(QtCore.QSize(50, 16777215))
        self.fingerPressEdit.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.fingerPressEdit.setObjectName("fingerPressEdit")
        self.horizontalLayout_3.addWidget(self.fingerPressEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem5 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem5)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_11.addWidget(self.label_3)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.gridLayout.addLayout(self.verticalLayout, 1, 1, 1, 1)
        self.otherLabel = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.otherLabel.setFont(font)
        self.otherLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.otherLabel.setObjectName("otherLabel")
        self.gridLayout.addWidget(self.otherLabel, 2, 0, 1, 2)
        self.pressureSensitivityLabel = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pressureSensitivityLabel.setFont(font)
        self.pressureSensitivityLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.pressureSensitivityLabel.setObjectName("pressureSensitivityLabel")
        self.gridLayout.addWidget(self.pressureSensitivityLabel, 0, 0, 1, 2)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 4, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Synaptweak"))
        self.palmDetectCheckBox.setText(_translate("Form", "Palm Detection"))
        self.tapDragCheckBox.setText(_translate("Form", "Tap and Drag Gesture"))
        self.quitButton.setToolTip(_translate("Form", "Alt-Q"))
        self.quitButton.setText(_translate("Form", "&Quit"))
        self.quitButton.setShortcut(_translate("Form", "Alt+Q"))
        self.reloadButton.setToolTip(_translate("Form", "Reload Current Values from Driver - Alt-L"))
        self.reloadButton.setText(_translate("Form", "Re&load"))
        self.reloadButton.setShortcut(_translate("Form", "Alt+L"))
        self.revertButton.setToolTip(_translate("Form", "Revert to Original Settings (from driver when Synaptweak was loaded) - Alt-R"))
        self.revertButton.setText(_translate("Form", "&Revert"))
        self.revertButton.setShortcut(_translate("Form", "Alt+R"))
        self.exportButton.setToolTip(_translate("Form", "Export xinput command to file - Alt-E"))
        self.exportButton.setText(_translate("Form", "&Export"))
        self.exportButton.setShortcut(_translate("Form", "Alt+E"))
        self.applyButton.setToolTip(_translate("Form", "Apply Settings To Driver - Alt-A"))
        self.applyButton.setText(_translate("Form", "&Apply"))
        self.applyButton.setShortcut(_translate("Form", "Alt+A"))
        self.fingerLowLabel.setText(_translate("Form", "FingerLow:"))
        self.label.setText(_translate("Form", "When finger pressure drops below this value, the driver counts it as a release."))
        self.fingerHighLabel.setText(_translate("Form", "FingerHigh:"))
        self.label_2.setText(_translate("Form", "When finger pressure goes above this value, the driver counts it as a touch."))
        self.fingerPressLabel.setText(_translate("Form", "FingerPress:"))
        self.label_3.setText(_translate("Form", "When finger pressure goes above this value, the driver counts it as a press. Currently a press is equivalent to putting the touchpad in trackstick emulation mode. "))
        self.otherLabel.setText(_translate("Form", "Other"))
        self.pressureSensitivityLabel.setText(_translate("Form", "Pressure Sensitivity"))