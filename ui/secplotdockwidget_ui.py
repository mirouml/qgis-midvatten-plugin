# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'secplotdockwidget_ui.ui'
#
# Created: Tue Jan 28 23:22:32 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_SecPlotDock(object):
    def setupUi(self, SecPlotDock):
        SecPlotDock.setObjectName(_fromUtf8("SecPlotDock"))
        SecPlotDock.resize(728, 288)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.gridLayout_2 = QtGui.QGridLayout(self.dockWidgetContents)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.frame = QtGui.QFrame(self.dockWidgetContents)
        self.frame.setMinimumSize(QtCore.QSize(110, 200))
        self.frame.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.formLayout_5 = QtGui.QFormLayout()
        self.formLayout_5.setObjectName(_fromUtf8("formLayout_5"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout_5.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.wlvltableComboBox = QtGui.QComboBox(self.frame)
        self.wlvltableComboBox.setObjectName(_fromUtf8("wlvltableComboBox"))
        self.formLayout_5.setWidget(0, QtGui.QFormLayout.FieldRole, self.wlvltableComboBox)
        self.verticalLayout_2.addLayout(self.formLayout_5)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_3 = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.datetimetextEdit = QtGui.QTextEdit(self.frame)
        self.datetimetextEdit.setObjectName(_fromUtf8("datetimetextEdit"))
        self.verticalLayout.addWidget(self.datetimetextEdit)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.drillstoplineEdit = QtGui.QLineEdit(self.frame)
        self.drillstoplineEdit.setObjectName(_fromUtf8("drillstoplineEdit"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.drillstoplineEdit)
        self.verticalLayout_2.addLayout(self.formLayout_2)
        self.formLayout_4 = QtGui.QFormLayout()
        self.formLayout_4.setObjectName(_fromUtf8("formLayout_4"))
        self.label_4 = QtGui.QLabel(self.frame)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_4)
        self.colorComboBox = QtGui.QComboBox(self.frame)
        self.colorComboBox.setObjectName(_fromUtf8("colorComboBox"))
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.FieldRole, self.colorComboBox)
        self.verticalLayout_2.addLayout(self.formLayout_4)
        self.formLayout_3 = QtGui.QFormLayout()
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.label_5 = QtGui.QLabel(self.frame)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_5)
        self.textcolComboBox = QtGui.QComboBox(self.frame)
        self.textcolComboBox.setObjectName(_fromUtf8("textcolComboBox"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.textcolComboBox)
        self.verticalLayout_2.addLayout(self.formLayout_3)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_6 = QtGui.QLabel(self.frame)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_6)
        self.barwidthdoubleSpinBox = QtGui.QDoubleSpinBox(self.frame)
        self.barwidthdoubleSpinBox.setDecimals(1)
        self.barwidthdoubleSpinBox.setProperty("value", 2.0)
        self.barwidthdoubleSpinBox.setObjectName(_fromUtf8("barwidthdoubleSpinBox"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.barwidthdoubleSpinBox)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.pushButton = QtGui.QPushButton(self.frame)
        self.pushButton.setMaximumSize(QtCore.QSize(250, 16777215))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout_2.addWidget(self.pushButton)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
        self.plotareawidget = QtGui.QWidget(self.dockWidgetContents)
        self.plotareawidget.setMinimumSize(QtCore.QSize(500, 0))
        self.plotareawidget.setObjectName(_fromUtf8("plotareawidget"))
        self.gridLayout = QtGui.QGridLayout(self.plotareawidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.mplplotlayout = QtGui.QVBoxLayout()
        self.mplplotlayout.setObjectName(_fromUtf8("mplplotlayout"))
        self.gridLayout.addLayout(self.mplplotlayout, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.plotareawidget, 0, 1, 1, 1)
        SecPlotDock.setWidget(self.dockWidgetContents)
        self.label.setBuddy(self.wlvltableComboBox)
        self.label_3.setBuddy(self.wlvltableComboBox)
        self.label_2.setBuddy(self.wlvltableComboBox)
        self.label_4.setBuddy(self.wlvltableComboBox)
        self.label_5.setBuddy(self.wlvltableComboBox)
        self.label_6.setBuddy(self.wlvltableComboBox)

        self.retranslateUi(SecPlotDock)
        QtCore.QMetaObject.connectSlotsByName(SecPlotDock)

    def retranslateUi(self, SecPlotDock):
        SecPlotDock.setWindowTitle(QtGui.QApplication.translate("SecPlotDock", "Midvatten Section Plot", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("SecPlotDock", "w level table:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("SecPlotDock", "date time f w level", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("SecPlotDock", "drillstop:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("SecPlotDock", "color:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("SecPlotDock", "text:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("SecPlotDock", "width(%)", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("SecPlotDock", "Replot", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    SecPlotDock = QtGui.QDockWidget()
    ui = Ui_SecPlotDock()
    ui.setupUi(SecPlotDock)
    SecPlotDock.show()
    sys.exit(app.exec_())
