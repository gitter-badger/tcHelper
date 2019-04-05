# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CongregationWindow.ui'
#
# Created: Tue Mar  3 11:58:42 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui

class Ui_CongregationWindow(object):
    def setupUi(self, CongregationWindow):
        CongregationWindow.setObjectName("CongregationWindow")
        CongregationWindow.resize(323, 363)
        CongregationWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        CongregationWindow.setSizeGripEnabled(True)
        CongregationWindow.setModal(False)
        self.gridLayout = QtGui.QGridLayout(CongregationWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.list_congregation = QtGui.QListWidget(CongregationWindow)
        self.list_congregation.setObjectName("list_congregation")
        self.gridLayout.addWidget(self.list_congregation, 0, 0, 1, 1)
        self.frame_2 = QtGui.QFrame(CongregationWindow)
        self.frame_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_2.setAutoFillBackground(False)
        self.frame_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtGui.QFrame.Plain)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setContentsMargins(6, 6, -1, 6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.button_delete = QtGui.QPushButton(self.frame_2)
        self.button_delete.setObjectName("button_delete")
        self.horizontalLayout.addWidget(self.button_delete)
        self.button_add = QtGui.QPushButton(self.frame_2)
        self.button_add.setObjectName("button_add")
        self.horizontalLayout.addWidget(self.button_add)
        self.button_edit = QtGui.QPushButton(self.frame_2)
        self.button_edit.setObjectName("button_edit")
        self.horizontalLayout.addWidget(self.button_edit)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 1)
        self.frame = QtGui.QFrame(CongregationWindow)
        self.frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtGui.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.button_close = QtGui.QPushButton(self.frame)
        self.button_close.setObjectName("button_close")
        self.gridLayout_3.addWidget(self.button_close, 0, 2, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 0, 1, 1, 1)
        self.frame_3 = QtGui.QFrame(self.frame)
        self.frame_3.setFrameShape(QtGui.QFrame.Box)
        self.frame_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_2 = QtGui.QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.radioAscending = QtGui.QRadioButton(self.frame_3)
        self.radioAscending.setToolTip("")
        self.radioAscending.setChecked(True)
        self.radioAscending.setObjectName("radioAscending")
        self.gridLayout_2.addWidget(self.radioAscending, 2, 0, 1, 1)
        self.label = QtGui.QLabel(self.frame_3)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.radioDistance = QtGui.QRadioButton(self.frame_3)
        self.radioDistance.setEnabled(False)
        self.radioDistance.setObjectName("radioDistance")
        self.gridLayout_2.addWidget(self.radioDistance, 4, 0, 1, 1)
        self.radioDesending = QtGui.QRadioButton(self.frame_3)
        self.radioDesending.setToolTip("")
        self.radioDesending.setObjectName("radioDesending")
        self.gridLayout_2.addWidget(self.radioDesending, 2, 1, 1, 1)
        self.gridLayout_3.addWidget(self.frame_3, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 2, 0, 1, 1)

        self.retranslateUi(CongregationWindow)
        QtCore.QObject.connect(self.button_close, QtCore.SIGNAL("clicked()"), CongregationWindow.close)
        QtCore.QMetaObject.connectSlotsByName(CongregationWindow)
        CongregationWindow.setTabOrder(self.button_add, self.button_edit)
        CongregationWindow.setTabOrder(self.button_edit, self.button_delete)
        CongregationWindow.setTabOrder(self.button_delete, self.radioAscending)
        CongregationWindow.setTabOrder(self.radioAscending, self.button_close)
        CongregationWindow.setTabOrder(self.button_close, self.list_congregation)

    def retranslateUi(self, CongregationWindow):
        CongregationWindow.setWindowTitle(QtGui.QApplication.translate("CongregationWindow", "Congregations", None, QtGui.QApplication.UnicodeUTF8))
        self.button_delete.setText(QtGui.QApplication.translate("CongregationWindow", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.button_add.setText(QtGui.QApplication.translate("CongregationWindow", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.button_edit.setText(QtGui.QApplication.translate("CongregationWindow", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.button_close.setText(QtGui.QApplication.translate("CongregationWindow", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.radioAscending.setWhatsThis(QtGui.QApplication.translate("CongregationWindow", "Sort congregations by alphabetical order.", None, QtGui.QApplication.UnicodeUTF8))
        self.radioAscending.setText(QtGui.QApplication.translate("CongregationWindow", "Ascending", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("CongregationWindow", "Sort by:", None, QtGui.QApplication.UnicodeUTF8))
        self.radioDistance.setToolTip(QtGui.QApplication.translate("CongregationWindow", "Sort by distance has not been implemented yet.", None, QtGui.QApplication.UnicodeUTF8))
        self.radioDistance.setText(QtGui.QApplication.translate("CongregationWindow", "Distance", None, QtGui.QApplication.UnicodeUTF8))
        self.radioDesending.setWhatsThis(QtGui.QApplication.translate("CongregationWindow", "Sort congregations by reverse alphabetical order.", None, QtGui.QApplication.UnicodeUTF8))
        self.radioDesending.setText(QtGui.QApplication.translate("CongregationWindow", "Desending", None, QtGui.QApplication.UnicodeUTF8))
