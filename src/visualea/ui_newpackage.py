# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newpackage.ui'
#
# Created: Fri Apr  6 11:45:11 2007
#      by: PyQt4 UI code generator 4.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui

class Ui_NewPackageDialog(object):
    def setupUi(self, NewPackageDialog):
        NewPackageDialog.setObjectName("NewPackageDialog")
        NewPackageDialog.resize(QtCore.QSize(QtCore.QRect(0,0,479,435).size()).expandedTo(NewPackageDialog.minimumSizeHint()))

        self.vboxlayout = QtGui.QVBoxLayout(NewPackageDialog)
        self.vboxlayout.setMargin(9)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")

        self.gridlayout = QtGui.QGridLayout()
        self.gridlayout.setMargin(0)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")

        self.authorsEdit = QtGui.QLineEdit(NewPackageDialog)
        self.authorsEdit.setObjectName("authorsEdit")
        self.gridlayout.addWidget(self.authorsEdit,4,1,1,1)

        self.label_2 = QtGui.QLabel(NewPackageDialog)
        self.label_2.setObjectName("label_2")
        self.gridlayout.addWidget(self.label_2,1,0,1,1)

        self.pathButton = QtGui.QPushButton(NewPackageDialog)
        self.pathButton.setObjectName("pathButton")
        self.gridlayout.addWidget(self.pathButton,7,2,1,1)

        self.label = QtGui.QLabel(NewPackageDialog)
        self.label.setObjectName("label")
        self.gridlayout.addWidget(self.label,0,0,1,1)

        self.versionEdit = QtGui.QLineEdit(NewPackageDialog)
        self.versionEdit.setObjectName("versionEdit")
        self.gridlayout.addWidget(self.versionEdit,2,1,1,1)

        self.label_7 = QtGui.QLabel(NewPackageDialog)
        self.label_7.setObjectName("label_7")
        self.gridlayout.addWidget(self.label_7,6,0,1,1)

        self.label_8 = QtGui.QLabel(NewPackageDialog)
        self.label_8.setObjectName("label_8")
        self.gridlayout.addWidget(self.label_8,7,0,1,1)

        self.pathEdit = QtGui.QLineEdit(NewPackageDialog)
        self.pathEdit.setObjectName("pathEdit")
        self.gridlayout.addWidget(self.pathEdit,7,1,1,1)

        self.label_6 = QtGui.QLabel(NewPackageDialog)
        self.label_6.setObjectName("label_6")
        self.gridlayout.addWidget(self.label_6,5,0,1,1)

        self.descriptionEdit = QtGui.QLineEdit(NewPackageDialog)
        self.descriptionEdit.setObjectName("descriptionEdit")
        self.gridlayout.addWidget(self.descriptionEdit,1,1,1,1)

        self.label_3 = QtGui.QLabel(NewPackageDialog)
        self.label_3.setObjectName("label_3")
        self.gridlayout.addWidget(self.label_3,2,0,1,1)

        self.intitutesEdit = QtGui.QLineEdit(NewPackageDialog)
        self.intitutesEdit.setObjectName("intitutesEdit")
        self.gridlayout.addWidget(self.intitutesEdit,5,1,1,1)

        self.licenseBox = QtGui.QComboBox(NewPackageDialog)
        self.licenseBox.setEditable(True)
        self.licenseBox.setObjectName("licenseBox")
        self.gridlayout.addWidget(self.licenseBox,3,1,1,1)

        self.urlEdit = QtGui.QLineEdit(NewPackageDialog)
        self.urlEdit.setObjectName("urlEdit")
        self.gridlayout.addWidget(self.urlEdit,6,1,1,1)

        self.label_4 = QtGui.QLabel(NewPackageDialog)
        self.label_4.setObjectName("label_4")
        self.gridlayout.addWidget(self.label_4,3,0,1,1)

        self.nameEdit = QtGui.QLineEdit(NewPackageDialog)
        self.nameEdit.setObjectName("nameEdit")
        self.gridlayout.addWidget(self.nameEdit,0,1,1,1)

        self.label_5 = QtGui.QLabel(NewPackageDialog)
        self.label_5.setObjectName("label_5")
        self.gridlayout.addWidget(self.label_5,4,0,1,1)
        self.vboxlayout.addLayout(self.gridlayout)

        self.buttonBox = QtGui.QDialogButtonBox(NewPackageDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.NoButton|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(NewPackageDialog)
        QtCore.QObject.connect(self.buttonBox,QtCore.SIGNAL("accepted()"),NewPackageDialog.accept)
        QtCore.QObject.connect(self.buttonBox,QtCore.SIGNAL("rejected()"),NewPackageDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(NewPackageDialog)

    def retranslateUi(self, NewPackageDialog):
        NewPackageDialog.setWindowTitle(QtGui.QApplication.translate("NewPackageDialog", "Package", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("NewPackageDialog", "Description", None, QtGui.QApplication.UnicodeUTF8))
        self.pathButton.setText(QtGui.QApplication.translate("NewPackageDialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("NewPackageDialog", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("NewPackageDialog", "URL", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("NewPackageDialog", "Path", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("NewPackageDialog", "Institutes", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("NewPackageDialog", "Version", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("NewPackageDialog", "License", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("NewPackageDialog", "Authors", None, QtGui.QApplication.UnicodeUTF8))

