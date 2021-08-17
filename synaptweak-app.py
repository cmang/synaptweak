#!/usr/bin/env python3
# Synaptweak
# aka My Synaptics Touchpad Config App
# Lets me tweak and play with the pressure sensitivity settings on my
# laptop's Synaptics Trackpad, to try to find the sweet spot to avoid
# triggering accidental clicks.
#
# Todo: Have a test click area
# Save settings profiles (json?)
#
# Setting sensitivity settings:
# xinput set-prop "SynPS/2 Synaptics TouchPad" "Synaptics Finger" 25 30 50
#
# Synaptics Capabilities (342):	1, 0, 0, 1, 1, 1, 1
# from man page: https://linux.die.net/man/4/synaptics
# Synaptics Capabilities
# This read-only property expresses the physical capability of the touchpad, most notably whether the touchpad hardware supports multi-finger tapping and scrolling. 
# 8 bit (BOOL), 7 values (read-only), has left button, has middle button, has right button, two-finger detection, three-finger detection, pressure detection, and finger/palm width detection.
#


from synaptweak_ui import Ui_Form

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui

import subprocess, sys

class SynapticsConfigWindow(qtw.QWidget):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # super init QWidget

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Load config from synclient
        self.loadSynclientConfig() # populate self.synConfig dict
        self.revertSynConfig = self.synConfig.copy()  # for the "revert" button
        self.setInitialValues()
        self.connectGuiHandlers()
        self.setWindowIcon(QtGui.QIcon('synaptweak-icon.png'))
        self.updateUIFromSynConfig()

    def connectGuiHandlers(self):
        # connect widgets to their handler methods
        self.ui.applyButton.clicked.connect(self.clickedApply)
        self.ui.reloadButton.clicked.connect(self.clickedReload)
        self.ui.revertButton.clicked.connect(self.clickedRevert)
        self.ui.exportButton.clicked.connect(self.clickedExport)
        self.ui.quitButton.clicked.connect(self.clickedQuit)
        self.ui.fingerLowSlider.valueChanged.connect(self.updateSliders)
        self.ui.fingerHighSlider.valueChanged.connect(self.updateSliders)
        self.ui.fingerPressSlider.valueChanged.connect(self.updateSliders)
        self.ui.fingerLowEdit.textChanged.connect(self.setSlidersFromEditBoxes)
        self.ui.fingerHighEdit.textChanged.connect(self.setSlidersFromEditBoxes)
        self.ui.fingerPressEdit.textChanged.connect(self.setSlidersFromEditBoxes)

    def setSlidersFromEditBoxes(self):
        # Take values from edit boxes, set slider to them
        self.ui.fingerLowSlider.setValue(int(self.ui.fingerLowEdit.text()))
        self.ui.fingerHighSlider.setValue(int(self.ui.fingerHighEdit.text()))
        self.ui.fingerPressSlider.setValue(int(self.ui.fingerPressEdit.text()))

    def getValueFromSynclient(self, value):
        # Return value of value from synclient
        pass

    def getFingerProperties(self):
        # Get current Synaptic Finger config from xinput
        # return 3 values - low, high and press
        completedProcess = subprocess.run(['xinput', 'list-props', 'SynPS/2 Synaptics TouchPad'], capture_output=True, text=True)
        touchpadProps = completedProcess.stdout.split('\n')
        if completedProcess.returncode == 0:
            print("xinput ran successfully")
        else:
            print("xinput didn't run successfully?")
            #print(completedProcess.stdout)
            print(completedProcess.stderr)
        for prop in touchpadProps:
            if "Synaptics Finger" in prop:
                print("Found settings from driver:")
                print(prop)
                fingerProp = prop
                fingerLow, fingerHigh, fingerPress = fingerProp.split('\t')[2].split(', ')
                print("Extracted values: ", end="")
                print(fingerLow, fingerHigh, fingerPress)
        return fingerLow, fingerHigh, fingerPress


    def setInitialValues(self):
        # Set initial values
        fingerLow = 30 
        fingerHigh = 45 
        fingerPress = 65
        # Or get them from the driver/xinput!
        fingerLow, fingerHigh, fingerPress = self.getFingerProperties()
        # Set them in the UI and program logic
        self.setUIFingerValues(fingerLow, fingerHigh, fingerPress)
        # Save values to revert
        self.originalFingerLow = fingerLow
        self.originalFingerHigh = fingerHigh
        self.originalFingerPress = fingerPress

    def updateUIFromSynConfig(self):
        print("Checking for PalmDetect.")
        if self.synConfig['PalmDetect'] == '1':
            print("PalmDetect enabled!")
            # turn on palmDetectCheckBox
            self.ui.palmDetectCheckBox.setChecked(True)
        elif self.synConfig['PalmDetect'] == '0':
            print("PalmDetect disabled!")
            self.ui.palmDetectCheckBox.setChecked(False)
        if self.synConfig['TapAndDragGesture'] == '1':
            print("Tap And Drag enabled")
            self.ui.tapDragCheckBox.setChecked(True)
        elif self.synConfig['TapAndDragGesture'] == '0':
            print("Tap And Drag disabled")
            self.ui.tapDragCheckBox.setChecked(False)


    def loadSynclientConfig(self):
        # Run synclient, parse output into key/value dict. Return dict, or key value?
        ranCommand = subprocess.run('synclient', capture_output=True, text=True)
        proplist = ranCommand.stdout.split('\n')    # split lines into list
        templist = []   # this is too ugly, don't do this
        settingsDict = {}
        for item in proplist: templist.append(item.split('='))  # make sublists of ["key", "value"]
        for item in templist: # for each key/value pair
            if len(item) == 2:
                settingsDict[item[0].strip()] = item[1].strip() # Populate dict with key pair
        print(settingsDict)
        self.synConfig = settingsDict
        return settingsDict


    def setFingerValues(self, low, high, press):
        # run the xinput command to set the values specified
        completedProcess = subprocess.run(['xinput', 'set-prop', 'SynPS/2 Synaptics TouchPad', 'Synaptics Finger', str(low), str(high), str(press)], capture_output=True, text=True)
        if completedProcess.returncode == 0:
            print(completedProcess.stdout)
            print("xinput appears to have ran successfully")
        else:
            print(completedProcess.stderr)
            print("xinput appears to have failed")

    def setUIFingerValues(self, low, high, press):
        #print("DEBUG: setUIFingerValues low %d, high %d, press %d" % (int(low), int(high), int(press)))
        self.ui.fingerLowEdit.setText(str(low))
        self.ui.fingerHighEdit.setText(str(high))
        self.ui.fingerPressEdit.setText(str(press))
        self.setSlidersFromEditBoxes()
        #self.updateSliders()

    def getUIFingerValues(self):
        low = int(self.ui.fingerLowEdit.text())
        high = int(self.ui.fingerHighEdit.text())
        press = int(self.ui.fingerPressEdit.text())
        return low, high, press

    def updateSliders(self):
        # Get value from sliders, assign them into edit boxes
        pass
        fingerLowSliderValue = self.ui.fingerLowSlider.value()
        self.ui.fingerLowEdit.setText(str(fingerLowSliderValue))
        fingerHighSliderValue = self.ui.fingerHighSlider.value()
        self.ui.fingerHighEdit.setText(str(fingerHighSliderValue))
        fingerPressSliderValue = self.ui.fingerPressSlider.value()
        self.ui.fingerPressEdit.setText(str(fingerPressSliderValue))

    def clickedApply(self):
        self.updateDriverFromUI()

    def updateDriverFromUI(self):
        # Take all values from UI and apply them to driver/synclient
        # Get values from fingerLowEdit, fingerHighEdit and fingerPress
        fingerLowStr = self.ui.fingerLowEdit.text()
        fingerHighStr = self.ui.fingerHighEdit.text()
        fingerPressStr = self.ui.fingerPressEdit.text()
        if fingerLowStr.isdigit():
            fingerLow = int(fingerLowStr)
        if fingerHighStr.isdigit():
            fingerHigh = int(fingerHighStr)
        if fingerPressStr.isdigit():
            fingerPress = int(fingerPressStr)
        # Do something with them, like run xinput
        print("Clicked Apply")
        print(fingerLow, fingerHigh, fingerPress)
        self.setFingerValues(fingerLow, fingerHigh, fingerPress)
        if self.ui.palmDetectCheckBox.checkState(): # if the box is checked 
            palmDetectValue = 1
        else:   # if it's not checked
            palmDetectValue = 0
        completedProcess = subprocess.run(['synclient', 'PalmDetect=' + str(palmDetectValue)], capture_output=True, text=True)
        if completedProcess.returncode != 0:
            print("synclient failed to set PalmDetect")

        if self.ui.tapDragCheckBox.checkState(): 
            tapDragValue = 1
        else:
            tapDragValue = 0
        completedProcess = subprocess.run(['synclient', 'TapAndDragGesture=' + str(tapDragValue)], capture_output=True, text=True)
        if completedProcess.returncode != 0:
            print("synclient failed to set TapAndDragGesture")

        print("New (applied) settings:")
        print(self.getFingerProperties())
        self.updateUIFromDriver()

    def updateUIFromDriver(self):
        # Query the driver, update the UI to match
        low, high, press = self.getFingerProperties()
        self.setUIFingerValues(low, high, press)
        self.loadSynclientConfig()
        self.updateUIFromSynConfig()


    def clickedRevert(self):
        print("Reverting back to old config!")
        self.setFingerValues(self.originalFingerLow, self.originalFingerHigh, self.originalFingerPress)
        self.synConfig = self.revertSynConfig.copy()  
        print("new (reverted) settings:")
        print(self.getFingerProperties())
        self.updateUIFromDriver()

    def clickedReload(self):
        # Update UI to reflect what is currently set in the Driver
        self.loadSynclientConfig()
        self.updateUIFromDriver()

    def clickedExport(self):
        # Generate an xinput command and write it to a file
        outputCommandFinger = 'xinput set-prop "SynPS/2 Synaptics TouchPad" "Synaptics Finger" '
        outputCommandFinger += '%d %d %d' % (self.getUIFingerValues())
        outputCommandPalmDetection = 'synclient PalmDetect='
        # if Palm Detection is checked
        if self.ui.palmDetectCheckBox.checkState():
            palmDetectValue = '1'
        else:
            palmDetectValue = '0'
        outputCommandPalmDetection += palmDetectValue

        outputCommandTapAndDragGesture = 'synclient TapAndDragGesture='
        # if Palm Detection is checked
        if self.ui.tapDragCheckBox.checkState():
            TapAndDragGestureValue = '1'
        else:
            TapAndDragGestureValue = '0'
        outputCommandTapAndDragGesture += TapAndDragGestureValue

        writeFilename = self.saveFileDialog()
        if writeFilename:   # if saveFileDialog didn't return "None"
            print("Writing to file: ", end="")
            print(writeFilename)
            writeFile = open(writeFilename, "w")
            writeFile.write(outputCommandFinger)
            writeFile.write('\n')
            writeFile.write(outputCommandPalmDetection)
            writeFile.write('\n')
            writeFile.write(outputCommandTapAndDragGesture)
            writeFile.write("\n")
            writeFile.close()
        #print(writeFilename)
        #print(outputCommand)

    def clickedQuit(self):
        # Try to exit cleanly
        #QCoreApplication.quit()     # terminate widget run loop?
        sys.exit()

    def saveFileDialog(self):
        options = qtw.QFileDialog.Options()
        options |= qtw.QFileDialog.DontUseNativeDialog
        fileName, _ = qtw.QFileDialog.getSaveFileName(self,"Export shell script","","All Files (*);;Shell Scripts (*.sh)", options=options)
        if fileName:
            print(fileName)
            return fileName

if (__name__ == '__main__'):
    app = qtw.QApplication([])

    widget = SynapticsConfigWindow()
    widget.show()

    app.exec_()
