# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'change_version_form.ui'
#
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from tank.platform.qt import QtCore, QtGui

class Ui_ChangeVersionForm(object):
    def setupUi(self, ChangeVersionForm):
        ChangeVersionForm.setObjectName("ChangeVersionForm")
        ChangeVersionForm.resize(320, 190)
        ChangeVersionForm.setMinimumSize(QtCore.QSize(320, 190))
        ChangeVersionForm.setMaximumSize(QtCore.QSize(16777215, 16777215))
        ChangeVersionForm.setFocusPolicy(QtCore.Qt.TabFocus)
        self.verticalLayout = QtGui.QVBoxLayout(ChangeVersionForm)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setContentsMargins(12, 12, 12, 4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtGui.QLabel(ChangeVersionForm)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(30, -1, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setSpacing(8)
        self.gridLayout.setObjectName("gridLayout")
        self.new_version_edit = QtGui.QLineEdit(ChangeVersionForm)
        self.new_version_edit.setMaximumSize(QtCore.QSize(60, 16777215))
        self.new_version_edit.setInputMask("")
        self.new_version_edit.setMaxLength(32767)
        self.new_version_edit.setFrame(True)
        self.new_version_edit.setObjectName("new_version_edit")
        self.gridLayout.addWidget(self.new_version_edit, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(ChangeVersionForm)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_2 = QtGui.QLabel(ChangeVersionForm)
        self.label_2.setMinimumSize(QtCore.QSize(140, 0))
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.current_version_label = QtGui.QLabel(ChangeVersionForm)
        self.current_version_label.setObjectName("current_version_label")
        self.gridLayout.addWidget(self.current_version_label, 0, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.horizontalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        spacerItem1 = QtGui.QSpacerItem(20, 1, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.break_line = QtGui.QFrame(ChangeVersionForm)
        self.break_line.setFrameShape(QtGui.QFrame.HLine)
        self.break_line.setFrameShadow(QtGui.QFrame.Sunken)
        self.break_line.setObjectName("break_line")
        self.verticalLayout.addWidget(self.break_line)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(12, 8, 12, 12)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.cancel_btn = QtGui.QPushButton(ChangeVersionForm)
        self.cancel_btn.setObjectName("cancel_btn")
        self.horizontalLayout.addWidget(self.cancel_btn)
        self.change_version_btn = QtGui.QPushButton(ChangeVersionForm)
        self.change_version_btn.setDefault(True)
        self.change_version_btn.setObjectName("change_version_btn")
        self.horizontalLayout.addWidget(self.change_version_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(2, 1)

        self.retranslateUi(ChangeVersionForm)
        QtCore.QObject.connect(self.new_version_edit, QtCore.SIGNAL("returnPressed()"), self.change_version_btn.click)
        QtCore.QMetaObject.connectSlotsByName(ChangeVersionForm)
        ChangeVersionForm.setTabOrder(self.new_version_edit, self.change_version_btn)
        ChangeVersionForm.setTabOrder(self.change_version_btn, self.cancel_btn)

    def retranslateUi(self, ChangeVersionForm):
        ChangeVersionForm.setWindowTitle(QtGui.QApplication.translate("ChangeVersionForm", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ChangeVersionForm", "Below you can change the version number of your current scene without doing a publish", None, QtGui.QApplication.UnicodeUTF8))
        self.new_version_edit.setToolTip(QtGui.QApplication.translate("ChangeVersionForm", "Enter a new version for your work file", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ChangeVersionForm", "<html><head/><body><p><span style=\" font-weight:600;\">New Version:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ChangeVersionForm", "<html><head/><body><p><span style=\" font-weight:600;\">Current Version:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.current_version_label.setToolTip(QtGui.QApplication.translate("ChangeVersionForm", "The current version of your work file", None, QtGui.QApplication.UnicodeUTF8))
        self.current_version_label.setText(QtGui.QApplication.translate("ChangeVersionForm", "?", None, QtGui.QApplication.UnicodeUTF8))
        self.cancel_btn.setText(QtGui.QApplication.translate("ChangeVersionForm", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.change_version_btn.setText(QtGui.QApplication.translate("ChangeVersionForm", "Change Version", None, QtGui.QApplication.UnicodeUTF8))

