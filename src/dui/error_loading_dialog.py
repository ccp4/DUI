# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'error_loading_dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_LoadErrorDialog(object):
    def setupUi(self, LoadErrorDialog):
        if not LoadErrorDialog.objectName():
            LoadErrorDialog.setObjectName(u"LoadErrorDialog")
        LoadErrorDialog.resize(597, 292)
        LoadErrorDialog.setModal(False)
        self.gridLayout = QGridLayout(LoadErrorDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(LoadErrorDialog)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.errorMessage = QPlainTextEdit(LoadErrorDialog)
        self.errorMessage.setObjectName(u"errorMessage")
        self.errorMessage.setLineWrapMode(QPlainTextEdit.NoWrap)
        self.errorMessage.setReadOnly(True)

        self.verticalLayout.addWidget(self.errorMessage)

        self.label_2 = QLabel(LoadErrorDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setOpenExternalLinks(True)

        self.verticalLayout.addWidget(self.label_2)

        self.buttonBox = QDialogButtonBox(LoadErrorDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)

        self.verticalLayout.addWidget(self.buttonBox)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(LoadErrorDialog)
        self.buttonBox.rejected.connect(LoadErrorDialog.close)

        QMetaObject.connectSlotsByName(LoadErrorDialog)
    # setupUi

    def retranslateUi(self, LoadErrorDialog):
        LoadErrorDialog.setWindowTitle(QCoreApplication.translate("LoadErrorDialog", u"Error loading DUI", None))
        self.label.setText(QCoreApplication.translate("LoadErrorDialog", u"An unexpected error occured whilst loading your previous DUI workspace:", None))
        self.label_2.setText(QCoreApplication.translate("LoadErrorDialog", u"<html><head/><body><p>Please report this error to <a href=\"mailto:dials-support@lists.sourceforge.net\"><span style=\" text-decoration: underline; color:#0000ff;\">dials-support@lists.sourceforge.net</span></a>.</p><p>Please move or remove the <tt>dui-files/</tt> subfolder or change your working directory to continue.</p></body></html>", None))
    # retranslateUi

