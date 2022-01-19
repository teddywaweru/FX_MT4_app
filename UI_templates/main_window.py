# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_templates/main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(909, 614)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.INIT_CONNECTOR_BTN = QtWidgets.QPushButton(self.centralwidget)
        self.INIT_CONNECTOR_BTN.setGeometry(QtCore.QRect(630, 10, 161, 41))
        self.INIT_CONNECTOR_BTN.setObjectName("INIT_CONNECTOR_BTN")
        self.SEND_HIST_REQUEST_BTN = QtWidgets.QPushButton(self.centralwidget)
        self.SEND_HIST_REQUEST_BTN.setGeometry(QtCore.QRect(540, 110, 111, 31))
        self.SEND_HIST_REQUEST_BTN.setCheckable(False)
        self.SEND_HIST_REQUEST_BTN.setChecked(False)
        self.SEND_HIST_REQUEST_BTN.setObjectName("SEND_HIST_REQUEST_BTN")
        self.PREPARE_NEW_TRADE = QtWidgets.QPushButton(self.centralwidget)
        self.PREPARE_NEW_TRADE.setGeometry(QtCore.QRect(160, 140, 121, 41))
        self.PREPARE_NEW_TRADE.setObjectName("PREPARE_NEW_TRADE")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(540, 150, 256, 192))
        self.tableView.setObjectName("tableView")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 30, 421, 71))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(30, 20, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(660, 110, 91, 31))
        self.textEdit.setObjectName("textEdit")
        self.PIP_VALUE_TEXT = QtWidgets.QLabel(self.centralwidget)
        self.PIP_VALUE_TEXT.setGeometry(QtCore.QRect(230, 180, 81, 21))
        self.PIP_VALUE_TEXT.setObjectName("PIP_VALUE_TEXT")
        self.PIP_VALUE_LABEL = QtWidgets.QLabel(self.centralwidget)
        self.PIP_VALUE_LABEL.setGeometry(QtCore.QRect(140, 180, 71, 21))
        self.PIP_VALUE_LABEL.setTextFormat(QtCore.Qt.PlainText)
        self.PIP_VALUE_LABEL.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.PIP_VALUE_LABEL.setObjectName("PIP_VALUE_LABEL")
        self.ATR_IN_PIPS_TEXT = QtWidgets.QLabel(self.centralwidget)
        self.ATR_IN_PIPS_TEXT.setGeometry(QtCore.QRect(230, 210, 81, 21))
        self.ATR_IN_PIPS_TEXT.setObjectName("ATR_IN_PIPS_TEXT")
        self.ATR_IN_PIPS_LABEL = QtWidgets.QLabel(self.centralwidget)
        self.ATR_IN_PIPS_LABEL.setGeometry(QtCore.QRect(140, 210, 71, 21))
        self.ATR_IN_PIPS_LABEL.setTextFormat(QtCore.Qt.PlainText)
        self.ATR_IN_PIPS_LABEL.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ATR_IN_PIPS_LABEL.setObjectName("ATR_IN_PIPS_LABEL")
        self.ACCOUNT_BALANCE_TEXT = QtWidgets.QLabel(self.centralwidget)
        self.ACCOUNT_BALANCE_TEXT.setGeometry(QtCore.QRect(230, 240, 81, 21))
        self.ACCOUNT_BALANCE_TEXT.setObjectName("ACCOUNT_BALANCE_TEXT")
        self.ACCOUNT_BALANCE_LABEL = QtWidgets.QLabel(self.centralwidget)
        self.ACCOUNT_BALANCE_LABEL.setGeometry(QtCore.QRect(110, 240, 101, 21))
        self.ACCOUNT_BALANCE_LABEL.setTextFormat(QtCore.Qt.PlainText)
        self.ACCOUNT_BALANCE_LABEL.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ACCOUNT_BALANCE_LABEL.setObjectName("ACCOUNT_BALANCE_LABEL")
        self.RISK_AMOUNT_TEXT = QtWidgets.QLabel(self.centralwidget)
        self.RISK_AMOUNT_TEXT.setGeometry(QtCore.QRect(230, 270, 81, 21))
        self.RISK_AMOUNT_TEXT.setObjectName("RISK_AMOUNT_TEXT")
        self.RISK_AMOUNT_LABEL = QtWidgets.QLabel(self.centralwidget)
        self.RISK_AMOUNT_LABEL.setGeometry(QtCore.QRect(130, 270, 81, 21))
        self.RISK_AMOUNT_LABEL.setTextFormat(QtCore.Qt.PlainText)
        self.RISK_AMOUNT_LABEL.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.RISK_AMOUNT_LABEL.setObjectName("RISK_AMOUNT_LABEL")
        self.LOT_SIZE_TEXT = QtWidgets.QLabel(self.centralwidget)
        self.LOT_SIZE_TEXT.setGeometry(QtCore.QRect(230, 300, 81, 21))
        self.LOT_SIZE_TEXT.setObjectName("LOT_SIZE_TEXT")
        self.LOT_SIZE_LABEL = QtWidgets.QLabel(self.centralwidget)
        self.LOT_SIZE_LABEL.setGeometry(QtCore.QRect(140, 300, 71, 20))
        self.LOT_SIZE_LABEL.setTextFormat(QtCore.Qt.PlainText)
        self.LOT_SIZE_LABEL.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.LOT_SIZE_LABEL.setObjectName("LOT_SIZE_LABEL")
        self.EXECUTE_NEW_TRADE = QtWidgets.QPushButton(self.centralwidget)
        self.EXECUTE_NEW_TRADE.setGeometry(QtCore.QRect(50, 480, 121, 41))
        self.EXECUTE_NEW_TRADE.setObjectName("EXECUTE_NEW_TRADE")
        self.STOP_LOSS_TEXT = QtWidgets.QLabel(self.centralwidget)
        self.STOP_LOSS_TEXT.setGeometry(QtCore.QRect(230, 330, 81, 21))
        self.STOP_LOSS_TEXT.setObjectName("STOP_LOSS_TEXT")
        self.STOP_LOSS_LABEL = QtWidgets.QLabel(self.centralwidget)
        self.STOP_LOSS_LABEL.setGeometry(QtCore.QRect(140, 330, 71, 21))
        self.STOP_LOSS_LABEL.setTextFormat(QtCore.Qt.PlainText)
        self.STOP_LOSS_LABEL.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.STOP_LOSS_LABEL.setObjectName("STOP_LOSS_LABEL")
        self.TAKE_PROFIT_LABEL = QtWidgets.QLabel(self.centralwidget)
        self.TAKE_PROFIT_LABEL.setGeometry(QtCore.QRect(140, 360, 71, 21))
        self.TAKE_PROFIT_LABEL.setTextFormat(QtCore.Qt.PlainText)
        self.TAKE_PROFIT_LABEL.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.TAKE_PROFIT_LABEL.setObjectName("TAKE_PROFIT_LABEL")
        self.TAKE_PROFIT_TEXT = QtWidgets.QLabel(self.centralwidget)
        self.TAKE_PROFIT_TEXT.setGeometry(QtCore.QRect(230, 360, 81, 21))
        self.TAKE_PROFIT_TEXT.setObjectName("TAKE_PROFIT_TEXT")
        self.CURRENCY_PAIRS_COMBOBOX = QtWidgets.QComboBox(self.centralwidget)
        self.CURRENCY_PAIRS_COMBOBOX.setGeometry(QtCore.QRect(0, 270, 94, 19))
        self.CURRENCY_PAIRS_COMBOBOX.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.CURRENCY_PAIRS_COMBOBOX.setEditable(True)
        self.CURRENCY_PAIRS_COMBOBOX.setMaxVisibleItems(20)
        self.CURRENCY_PAIRS_COMBOBOX.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.CURRENCY_PAIRS_COMBOBOX.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.CURRENCY_PAIRS_COMBOBOX.setObjectName("CURRENCY_PAIRS_COMBOBOX")
        self.CURRENCY_PAIRS_COMBOBOX.addItem("")
        self.CURRENCY_PAIRS_COMBOBOX.addItem("")
        self.CURRENCY_PAIRS_COMBOBOX.addItem("")
        self.CURRENCY_PAIRS_COMBOBOX.addItem("")
        self.CURRENCY_PAIRS_COMBOBOX.addItem("")
        self.CURRENCY_PAIRS_COMBOBOX.addItem("")
        self.CURRENCY_PAIRS_COMBOBOX.addItem("")
        self.CURRENCY_PAIRS_COMBOBOX.addItem("")
        self.CURRENCY_PAIRS_COMBOBOX.addItem("")
        self.CURRENCY_PAIRS_COMBOBOX.addItem("")
        self.CURRENCY_PAIRS_COMBOBOX.addItem("")
        self.CURRENCY_PAIRS_COMBOBOX.addItem("")
        self.CURRENCY_PAIRS_COMBOBOX.addItem("")
        self.BUY_SELL_SLIDER = QtWidgets.QSlider(self.centralwidget)
        self.BUY_SELL_SLIDER.setGeometry(QtCore.QRect(20, 170, 31, 71))
        self.BUY_SELL_SLIDER.setMaximum(1)
        self.BUY_SELL_SLIDER.setOrientation(QtCore.Qt.Vertical)
        self.BUY_SELL_SLIDER.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.BUY_SELL_SLIDER.setObjectName("BUY_SELL_SLIDER")
        self.BUY_SELL_LABEL = QtWidgets.QLabel(self.centralwidget)
        self.BUY_SELL_LABEL.setGeometry(QtCore.QRect(50, 160, 41, 21))
        self.BUY_SELL_LABEL.setTextFormat(QtCore.Qt.PlainText)
        self.BUY_SELL_LABEL.setAlignment(QtCore.Qt.AlignCenter)
        self.BUY_SELL_LABEL.setObjectName("BUY_SELL_LABEL")
        self.dial = QtWidgets.QDial(self.centralwidget)
        self.dial.setGeometry(QtCore.QRect(320, 420, 50, 64))
        self.dial.setMaximum(10)
        self.dial.setPageStep(5)
        self.dial.setSliderPosition(2)
        self.dial.setInvertedAppearance(False)
        self.dial.setWrapping(False)
        self.dial.setNotchTarget(13.7)
        self.dial.setNotchesVisible(True)
        self.dial.setObjectName("dial")
        self.BUY_SELL_LABEL_2 = QtWidgets.QLabel(self.centralwidget)
        self.BUY_SELL_LABEL_2.setGeometry(QtCore.QRect(50, 220, 41, 21))
        self.BUY_SELL_LABEL_2.setTextFormat(QtCore.Qt.PlainText)
        self.BUY_SELL_LABEL_2.setAlignment(QtCore.Qt.AlignCenter)
        self.BUY_SELL_LABEL_2.setObjectName("BUY_SELL_LABEL_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 909, 19))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        self.CURRENCY_PAIRS_COMBOBOX.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.INIT_CONNECTOR_BTN.setText(_translate("MainWindow", "Init MT4 Connection"))
        self.SEND_HIST_REQUEST_BTN.setText(_translate("MainWindow", "Request Hist Data"))
        self.PREPARE_NEW_TRADE.setText(_translate("MainWindow", "Prepare New Trade"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Page"))
        self.PIP_VALUE_TEXT.setText(_translate("MainWindow", "TextLabel"))
        self.PIP_VALUE_LABEL.setText(_translate("MainWindow", "Pip Value:"))
        self.ATR_IN_PIPS_TEXT.setText(_translate("MainWindow", "TextLabel"))
        self.ATR_IN_PIPS_LABEL.setText(_translate("MainWindow", "ATR In Pips:"))
        self.ACCOUNT_BALANCE_TEXT.setText(_translate("MainWindow", "TextLabel"))
        self.ACCOUNT_BALANCE_LABEL.setText(_translate("MainWindow", "Account Balance:"))
        self.RISK_AMOUNT_TEXT.setText(_translate("MainWindow", "TextLabel"))
        self.RISK_AMOUNT_LABEL.setText(_translate("MainWindow", "Risk Amount:"))
        self.LOT_SIZE_TEXT.setText(_translate("MainWindow", "TextLabel"))
        self.LOT_SIZE_LABEL.setText(_translate("MainWindow", "Lot Size:"))
        self.EXECUTE_NEW_TRADE.setText(_translate("MainWindow", "Execute New Trade"))
        self.STOP_LOSS_TEXT.setText(_translate("MainWindow", "__________"))
        self.STOP_LOSS_LABEL.setText(_translate("MainWindow", "Stop Loss:"))
        self.TAKE_PROFIT_LABEL.setText(_translate("MainWindow", "Take Profit:"))
        self.TAKE_PROFIT_TEXT.setText(_translate("MainWindow", "__________"))
        self.CURRENCY_PAIRS_COMBOBOX.setCurrentText(_translate("MainWindow", "Currency Pairs"))
        self.CURRENCY_PAIRS_COMBOBOX.setPlaceholderText(_translate("MainWindow", "Currency Pairs"))
        self.CURRENCY_PAIRS_COMBOBOX.setItemText(0, _translate("MainWindow", "AUDUSD"))
        self.CURRENCY_PAIRS_COMBOBOX.setItemText(1, _translate("MainWindow", "EURCHF"))
        self.CURRENCY_PAIRS_COMBOBOX.setItemText(2, _translate("MainWindow", "CADCHF"))
        self.CURRENCY_PAIRS_COMBOBOX.setItemText(3, _translate("MainWindow", "CHFJPY"))
        self.CURRENCY_PAIRS_COMBOBOX.setItemText(4, _translate("MainWindow", "NZDCAD"))
        self.CURRENCY_PAIRS_COMBOBOX.setItemText(5, _translate("MainWindow", "EURCAD"))
        self.CURRENCY_PAIRS_COMBOBOX.setItemText(6, _translate("MainWindow", "AUDCHF"))
        self.CURRENCY_PAIRS_COMBOBOX.setItemText(7, _translate("MainWindow", "EURUSD"))
        self.CURRENCY_PAIRS_COMBOBOX.setItemText(8, _translate("MainWindow", "EURGBP"))
        self.CURRENCY_PAIRS_COMBOBOX.setItemText(9, _translate("MainWindow", "EURAUD"))
        self.CURRENCY_PAIRS_COMBOBOX.setItemText(10, _translate("MainWindow", "USDJPY"))
        self.CURRENCY_PAIRS_COMBOBOX.setItemText(11, _translate("MainWindow", "AUDJPY"))
        self.CURRENCY_PAIRS_COMBOBOX.setItemText(12, _translate("MainWindow", "USDCHF"))
        self.BUY_SELL_LABEL.setText(_translate("MainWindow", "LONG"))
        self.BUY_SELL_LABEL_2.setText(_translate("MainWindow", "SHORT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())