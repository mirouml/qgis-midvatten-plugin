# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'midvsettingsdialog.ui'
#
# Created: Sun Jan 20 20:22:43 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(543, 329)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.txtpath = QtGui.QLineEdit(Dialog)
        self.txtpath.setReadOnly(True)
        self.txtpath.setObjectName(_fromUtf8("txtpath"))
        self.gridLayout.addWidget(self.txtpath, 1, 0, 1, 1)
        self.btnSetDB = QtGui.QPushButton(Dialog)
        self.btnSetDB.setObjectName(_fromUtf8("btnSetDB"))
        self.gridLayout.addWidget(self.btnSetDB, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 2)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 2)
        self.tabWidget = QtGui.QTabWidget(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.TAB_TSPLOT = QtGui.QWidget()
        self.TAB_TSPLOT.setObjectName(_fromUtf8("TAB_TSPLOT"))
        self.gridLayout_3 = QtGui.QGridLayout(self.TAB_TSPLOT)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label = QtGui.QLabel(self.TAB_TSPLOT)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.ListOfTables = QtGui.QComboBox(self.TAB_TSPLOT)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ListOfTables.sizePolicy().hasHeightForWidth())
        self.ListOfTables.setSizePolicy(sizePolicy)
        self.ListOfTables.setObjectName(_fromUtf8("ListOfTables"))
        self.gridLayout_3.addWidget(self.ListOfTables, 1, 0, 1, 1)
        self.InfoTxtTSPlot = QtGui.QLabel(self.TAB_TSPLOT)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InfoTxtTSPlot.sizePolicy().hasHeightForWidth())
        self.InfoTxtTSPlot.setSizePolicy(sizePolicy)
        self.InfoTxtTSPlot.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.InfoTxtTSPlot.setWordWrap(True)
        self.InfoTxtTSPlot.setObjectName(_fromUtf8("InfoTxtTSPlot"))
        self.gridLayout_3.addWidget(self.InfoTxtTSPlot, 1, 1, 5, 1)
        self.label_3 = QtGui.QLabel(self.TAB_TSPLOT)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_3.addWidget(self.label_3, 2, 0, 1, 1)
        self.ListOfColumns = QtGui.QComboBox(self.TAB_TSPLOT)
        self.ListOfColumns.setObjectName(_fromUtf8("ListOfColumns"))
        self.gridLayout_3.addWidget(self.ListOfColumns, 3, 0, 1, 1)
        self.checkBoxDataPoints = QtGui.QCheckBox(self.TAB_TSPLOT)
        self.checkBoxDataPoints.setEnabled(True)
        self.checkBoxDataPoints.setObjectName(_fromUtf8("checkBoxDataPoints"))
        self.gridLayout_3.addWidget(self.checkBoxDataPoints, 4, 0, 1, 1)
        self.checkBoxStepPlot = QtGui.QCheckBox(self.TAB_TSPLOT)
        self.checkBoxStepPlot.setEnabled(True)
        self.checkBoxStepPlot.setObjectName(_fromUtf8("checkBoxStepPlot"))
        self.gridLayout_3.addWidget(self.checkBoxStepPlot, 5, 0, 1, 1)
        self.tabWidget.addTab(self.TAB_TSPLOT, _fromUtf8(""))
        self.TAB_XYPLOT = QtGui.QWidget()
        self.TAB_XYPLOT.setObjectName(_fromUtf8("TAB_XYPLOT"))
        self.gridLayout_2 = QtGui.QGridLayout(self.TAB_XYPLOT)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_5 = QtGui.QLabel(self.TAB_XYPLOT)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.TAB_XYPLOT)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_2.addWidget(self.label_6, 0, 1, 1, 1)
        self.ListOfTables_2 = QtGui.QComboBox(self.TAB_XYPLOT)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ListOfTables_2.sizePolicy().hasHeightForWidth())
        self.ListOfTables_2.setSizePolicy(sizePolicy)
        self.ListOfTables_2.setObjectName(_fromUtf8("ListOfTables_2"))
        self.gridLayout_2.addWidget(self.ListOfTables_2, 1, 0, 1, 1)
        self.ListOfColumns_3 = QtGui.QComboBox(self.TAB_XYPLOT)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ListOfColumns_3.sizePolicy().hasHeightForWidth())
        self.ListOfColumns_3.setSizePolicy(sizePolicy)
        self.ListOfColumns_3.setObjectName(_fromUtf8("ListOfColumns_3"))
        self.gridLayout_2.addWidget(self.ListOfColumns_3, 1, 1, 1, 1)
        self.label_10 = QtGui.QLabel(self.TAB_XYPLOT)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_2.addWidget(self.label_10, 2, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.TAB_XYPLOT)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_2.addWidget(self.label_7, 2, 1, 1, 1)
        self.ListOfColumns_2 = QtGui.QComboBox(self.TAB_XYPLOT)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ListOfColumns_2.sizePolicy().hasHeightForWidth())
        self.ListOfColumns_2.setSizePolicy(sizePolicy)
        self.ListOfColumns_2.setObjectName(_fromUtf8("ListOfColumns_2"))
        self.gridLayout_2.addWidget(self.ListOfColumns_2, 3, 0, 1, 1)
        self.ListOfColumns_4 = QtGui.QComboBox(self.TAB_XYPLOT)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ListOfColumns_4.sizePolicy().hasHeightForWidth())
        self.ListOfColumns_4.setSizePolicy(sizePolicy)
        self.ListOfColumns_4.setObjectName(_fromUtf8("ListOfColumns_4"))
        self.gridLayout_2.addWidget(self.ListOfColumns_4, 3, 1, 1, 1)
        self.checkBoxDataPoints_2 = QtGui.QCheckBox(self.TAB_XYPLOT)
        self.checkBoxDataPoints_2.setEnabled(True)
        self.checkBoxDataPoints_2.setObjectName(_fromUtf8("checkBoxDataPoints_2"))
        self.gridLayout_2.addWidget(self.checkBoxDataPoints_2, 4, 0, 2, 1)
        self.label_8 = QtGui.QLabel(self.TAB_XYPLOT)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_2.addWidget(self.label_8, 4, 1, 1, 1)
        self.ListOfColumns_5 = QtGui.QComboBox(self.TAB_XYPLOT)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ListOfColumns_5.sizePolicy().hasHeightForWidth())
        self.ListOfColumns_5.setSizePolicy(sizePolicy)
        self.ListOfColumns_5.setObjectName(_fromUtf8("ListOfColumns_5"))
        self.gridLayout_2.addWidget(self.ListOfColumns_5, 5, 1, 2, 1)
        self.InfoTxtXYPlot = QtGui.QLabel(self.TAB_XYPLOT)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InfoTxtXYPlot.sizePolicy().hasHeightForWidth())
        self.InfoTxtXYPlot.setSizePolicy(sizePolicy)
        self.InfoTxtXYPlot.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.InfoTxtXYPlot.setWordWrap(True)
        self.InfoTxtXYPlot.setObjectName(_fromUtf8("InfoTxtXYPlot"))
        self.gridLayout_2.addWidget(self.InfoTxtXYPlot, 6, 0, 1, 1)
        self.tabWidget.addTab(self.TAB_XYPLOT, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_4 = QtGui.QGridLayout(self.tab)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label_18 = QtGui.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_18.setFont(font)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.gridLayout_4.addWidget(self.label_18, 0, 0, 1, 1)
        self.label_23 = QtGui.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_23.setFont(font)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.gridLayout_4.addWidget(self.label_23, 0, 1, 1, 1)
        self.ListOfTables_WQUAL = QtGui.QComboBox(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ListOfTables_WQUAL.sizePolicy().hasHeightForWidth())
        self.ListOfTables_WQUAL.setSizePolicy(sizePolicy)
        self.ListOfTables_WQUAL.setObjectName(_fromUtf8("ListOfTables_WQUAL"))
        self.gridLayout_4.addWidget(self.ListOfTables_WQUAL, 1, 0, 1, 1)
        self.ListOfColumns_WQUALUNIT = QtGui.QComboBox(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ListOfColumns_WQUALUNIT.sizePolicy().hasHeightForWidth())
        self.ListOfColumns_WQUALUNIT.setSizePolicy(sizePolicy)
        self.ListOfColumns_WQUALUNIT.setObjectName(_fromUtf8("ListOfColumns_WQUALUNIT"))
        self.gridLayout_4.addWidget(self.ListOfColumns_WQUALUNIT, 1, 1, 1, 1)
        self.label_22 = QtGui.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_22.setFont(font)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.gridLayout_4.addWidget(self.label_22, 2, 0, 1, 1)
        self.label_21 = QtGui.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_21.setFont(font)
        self.label_21.setWordWrap(True)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.gridLayout_4.addWidget(self.label_21, 2, 1, 2, 1)
        self.ListOfColumns_WQUALPARAM = QtGui.QComboBox(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ListOfColumns_WQUALPARAM.sizePolicy().hasHeightForWidth())
        self.ListOfColumns_WQUALPARAM.setSizePolicy(sizePolicy)
        self.ListOfColumns_WQUALPARAM.setObjectName(_fromUtf8("ListOfColumns_WQUALPARAM"))
        self.gridLayout_4.addWidget(self.ListOfColumns_WQUALPARAM, 3, 0, 2, 1)
        self.ListOfColumns_WQUALSORTING = QtGui.QComboBox(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ListOfColumns_WQUALSORTING.sizePolicy().hasHeightForWidth())
        self.ListOfColumns_WQUALSORTING.setSizePolicy(sizePolicy)
        self.ListOfColumns_WQUALSORTING.setObjectName(_fromUtf8("ListOfColumns_WQUALSORTING"))
        self.gridLayout_4.addWidget(self.ListOfColumns_WQUALSORTING, 4, 1, 2, 1)
        self.label_20 = QtGui.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_20.setFont(font)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.gridLayout_4.addWidget(self.label_20, 5, 0, 1, 1)
        self.ListOfColumns_WQUALVALUE = QtGui.QComboBox(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ListOfColumns_WQUALVALUE.sizePolicy().hasHeightForWidth())
        self.ListOfColumns_WQUALVALUE.setSizePolicy(sizePolicy)
        self.ListOfColumns_WQUALVALUE.setObjectName(_fromUtf8("ListOfColumns_WQUALVALUE"))
        self.gridLayout_4.addWidget(self.ListOfColumns_WQUALVALUE, 6, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 28, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem, 6, 1, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.TAB_STRATIGRAPHY = QtGui.QWidget()
        self.TAB_STRATIGRAPHY.setObjectName(_fromUtf8("TAB_STRATIGRAPHY"))
        self.gridLayout_5 = QtGui.QGridLayout(self.TAB_STRATIGRAPHY)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.label_9 = QtGui.QLabel(self.TAB_STRATIGRAPHY)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_5.addWidget(self.label_9, 0, 0, 1, 1)
        self.ListOfTables_3 = QtGui.QComboBox(self.TAB_STRATIGRAPHY)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ListOfTables_3.sizePolicy().hasHeightForWidth())
        self.ListOfTables_3.setSizePolicy(sizePolicy)
        self.ListOfTables_3.setObjectName(_fromUtf8("ListOfTables_3"))
        self.gridLayout_5.addWidget(self.ListOfTables_3, 1, 0, 1, 1)
        self.InfoTxtStratigraphy = QtGui.QLabel(self.TAB_STRATIGRAPHY)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InfoTxtStratigraphy.sizePolicy().hasHeightForWidth())
        self.InfoTxtStratigraphy.setSizePolicy(sizePolicy)
        self.InfoTxtStratigraphy.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.InfoTxtStratigraphy.setWordWrap(True)
        self.InfoTxtStratigraphy.setObjectName(_fromUtf8("InfoTxtStratigraphy"))
        self.gridLayout_5.addWidget(self.InfoTxtStratigraphy, 1, 1, 2, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 104, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem1, 2, 0, 1, 1)
        self.tabWidget.addTab(self.TAB_STRATIGRAPHY, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 2, 0, 1, 2)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.txtpath, self.btnSetDB)
        Dialog.setTabOrder(self.btnSetDB, self.tabWidget)
        Dialog.setTabOrder(self.tabWidget, self.ListOfTables)
        Dialog.setTabOrder(self.ListOfTables, self.ListOfColumns)
        Dialog.setTabOrder(self.ListOfColumns, self.checkBoxDataPoints)
        Dialog.setTabOrder(self.checkBoxDataPoints, self.checkBoxStepPlot)
        Dialog.setTabOrder(self.checkBoxStepPlot, self.ListOfTables_2)
        Dialog.setTabOrder(self.ListOfTables_2, self.ListOfColumns_2)
        Dialog.setTabOrder(self.ListOfColumns_2, self.ListOfColumns_3)
        Dialog.setTabOrder(self.ListOfColumns_3, self.ListOfColumns_4)
        Dialog.setTabOrder(self.ListOfColumns_4, self.ListOfColumns_5)
        Dialog.setTabOrder(self.ListOfColumns_5, self.checkBoxDataPoints_2)
        Dialog.setTabOrder(self.checkBoxDataPoints_2, self.ListOfTables_WQUAL)
        Dialog.setTabOrder(self.ListOfTables_WQUAL, self.ListOfColumns_WQUALPARAM)
        Dialog.setTabOrder(self.ListOfColumns_WQUALPARAM, self.ListOfColumns_WQUALVALUE)
        Dialog.setTabOrder(self.ListOfColumns_WQUALVALUE, self.ListOfColumns_WQUALUNIT)
        Dialog.setTabOrder(self.ListOfColumns_WQUALUNIT, self.ListOfColumns_WQUALSORTING)
        Dialog.setTabOrder(self.ListOfColumns_WQUALSORTING, self.ListOfTables_3)
        Dialog.setTabOrder(self.ListOfTables_3, self.buttonBox)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.txtpath.setWhatsThis(QtGui.QApplication.translate("Dialog", "Selected SpatiaLite Database", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSetDB.setText(QtGui.QApplication.translate("Dialog", "Select DB", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "SQLite database:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Table:", None, QtGui.QApplication.UnicodeUTF8))
        self.InfoTxtTSPlot.setText(QtGui.QApplication.translate("Dialog", "Table Status", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Column:", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxDataPoints.setText(QtGui.QApplication.translate("Dialog", "Dot markers on line", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxStepPlot.setText(QtGui.QApplication.translate("Dialog", "Step-plot", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TAB_TSPLOT), QtGui.QApplication.translate("Dialog", "Time Series", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "Table:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Dialog", "y1-column:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("Dialog", "x-column:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Dialog", "y2-column:", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxDataPoints_2.setText(QtGui.QApplication.translate("Dialog", "Dot markers on lines", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Dialog", "y3-column:", None, QtGui.QApplication.UnicodeUTF8))
        self.InfoTxtXYPlot.setText(QtGui.QApplication.translate("Dialog", "Table Status", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TAB_XYPLOT), QtGui.QApplication.translate("Dialog", "XY Scatter", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setText(QtGui.QApplication.translate("Dialog", "Table:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_23.setText(QtGui.QApplication.translate("Dialog", "Unit column (empty if none):", None, QtGui.QApplication.UnicodeUTF8))
        self.label_22.setText(QtGui.QApplication.translate("Dialog", "Parameter name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_21.setText(QtGui.QApplication.translate("Dialog", "Column for additional sorting, besides from date_time (e.g. sample depth, lab report no.):", None, QtGui.QApplication.UnicodeUTF8))
        self.label_20.setText(QtGui.QApplication.translate("Dialog", "Analysis value:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("Dialog", "W quality report", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("Dialog", "Table:", None, QtGui.QApplication.UnicodeUTF8))
        self.InfoTxtStratigraphy.setText(QtGui.QApplication.translate("Dialog", "Table status", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TAB_STRATIGRAPHY), QtGui.QApplication.translate("Dialog", "Stratigraphy", None, QtGui.QApplication.UnicodeUTF8))
