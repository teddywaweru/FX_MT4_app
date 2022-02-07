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
        MainWindow.resize(825, 813)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.INIT_CONNECTOR_BTN = QtWidgets.QPushButton(self.centralwidget)
        self.INIT_CONNECTOR_BTN.setGeometry(QtCore.QRect(630, 10, 161, 41))
        self.INIT_CONNECTOR_BTN.setObjectName("INIT_CONNECTOR_BTN")
        self.SEND_HIST_REQUEST_BTN = QtWidgets.QPushButton(self.centralwidget)
        self.SEND_HIST_REQUEST_BTN.setGeometry(QtCore.QRect(510, 20, 111, 31))
        self.SEND_HIST_REQUEST_BTN.setCheckable(False)
        self.SEND_HIST_REQUEST_BTN.setChecked(False)
        self.SEND_HIST_REQUEST_BTN.setObjectName("SEND_HIST_REQUEST_BTN")
        self.PREPARE_NEW_TRADE_BTN = QtWidgets.QPushButton(self.centralwidget)
        self.PREPARE_NEW_TRADE_BTN.setGeometry(QtCore.QRect(230, 430, 121, 41))
        self.PREPARE_NEW_TRADE_BTN.setObjectName("PREPARE_NEW_TRADE_BTN")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(440, 50, 101, 61))
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
        self.PIP_VALUE_TEXT = QtWidgets.QLabel(self.centralwidget)
        self.PIP_VALUE_TEXT.setGeometry(QtCore.QRect(300, 220, 81, 21))
        self.PIP_VALUE_TEXT.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.PIP_VALUE_TEXT.setObjectName("PIP_VALUE_TEXT")
        self.PIP_VALUE_LABEL = QtWidgets.QLabel(self.centralwidget)
        self.PIP_VALUE_LABEL.setGeometry(QtCore.QRect(210, 220, 71, 21))
        self.PIP_VALUE_LABEL.setTextFormat(QtCore.Qt.PlainText)
        self.PIP_VALUE_LABEL.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.PIP_VALUE_LABEL.setObjectName("PIP_VALUE_LABEL")
        self.ATR_IN_PIPS_TEXT = QtWidgets.QLabel(self.centralwidget)
        self.ATR_IN_PIPS_TEXT.setGeometry(QtCore.QRect(300, 250, 81, 21))
        self.ATR_IN_PIPS_TEXT.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.ATR_IN_PIPS_TEXT.setObjectName("ATR_IN_PIPS_TEXT")
        self.ATR_IN_PIPS_LABEL = QtWidgets.QLabel(self.centralwidget)
        self.ATR_IN_PIPS_LABEL.setGeometry(QtCore.QRect(210, 250, 71, 21))
        self.ATR_IN_PIPS_LABEL.setTextFormat(QtCore.Qt.PlainText)
        self.ATR_IN_PIPS_LABEL.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ATR_IN_PIPS_LABEL.setObjectName("ATR_IN_PIPS_LABEL")
        self.ACCOUNT_BALANCE_TEXT = QtWidgets.QLabel(self.centralwidget)
        self.ACCOUNT_BALANCE_TEXT.setGeometry(QtCore.QRect(300, 280, 81, 21))
        self.ACCOUNT_BALANCE_TEXT.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.ACCOUNT_BALANCE_TEXT.setObjectName("ACCOUNT_BALANCE_TEXT")
        self.ACCOUNT_BALANCE_LABEL = QtWidgets.QLabel(self.centralwidget)
        self.ACCOUNT_BALANCE_LABEL.setGeometry(QtCore.QRect(180, 280, 101, 21))
        self.ACCOUNT_BALANCE_LABEL.setTextFormat(QtCore.Qt.PlainText)
        self.ACCOUNT_BALANCE_LABEL.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ACCOUNT_BALANCE_LABEL.setObjectName("ACCOUNT_BALANCE_LABEL")
        self.RISK_AMOUNT_TEXT = QtWidgets.QLabel(self.centralwidget)
        self.RISK_AMOUNT_TEXT.setGeometry(QtCore.QRect(300, 310, 81, 21))
        self.RISK_AMOUNT_TEXT.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.RISK_AMOUNT_TEXT.setObjectName("RISK_AMOUNT_TEXT")
        self.RISK_AMOUNT_LABEL = QtWidgets.QLabel(self.centralwidget)
        self.RISK_AMOUNT_LABEL.setGeometry(QtCore.QRect(200, 310, 81, 21))
        self.RISK_AMOUNT_LABEL.setTextFormat(QtCore.Qt.PlainText)
        self.RISK_AMOUNT_LABEL.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.RISK_AMOUNT_LABEL.setObjectName("RISK_AMOUNT_LABEL")
        self.LOT_SIZE_TEXT = QtWidgets.QLabel(self.centralwidget)
        self.LOT_SIZE_TEXT.setGeometry(QtCore.QRect(300, 340, 81, 21))
        self.LOT_SIZE_TEXT.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.LOT_SIZE_TEXT.setObjectName("LOT_SIZE_TEXT")
        self.LOT_SIZE_LABEL = QtWidgets.QLabel(self.centralwidget)
        self.LOT_SIZE_LABEL.setGeometry(QtCore.QRect(210, 340, 71, 20))
        self.LOT_SIZE_LABEL.setTextFormat(QtCore.Qt.PlainText)
        self.LOT_SIZE_LABEL.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.LOT_SIZE_LABEL.setObjectName("LOT_SIZE_LABEL")
        self.EXECUTE_NEW_TRADE_BTN = QtWidgets.QPushButton(self.centralwidget)
        self.EXECUTE_NEW_TRADE_BTN.setEnabled(False)
        self.EXECUTE_NEW_TRADE_BTN.setGeometry(QtCore.QRect(180, 530, 211, 41))
        self.EXECUTE_NEW_TRADE_BTN.setObjectName("EXECUTE_NEW_TRADE_BTN")
        self.STOP_LOSS_TEXT = QtWidgets.QLabel(self.centralwidget)
        self.STOP_LOSS_TEXT.setGeometry(QtCore.QRect(300, 370, 81, 21))
        self.STOP_LOSS_TEXT.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.STOP_LOSS_TEXT.setObjectName("STOP_LOSS_TEXT")
        self.STOP_LOSS_LABEL = QtWidgets.QLabel(self.centralwidget)
        self.STOP_LOSS_LABEL.setGeometry(QtCore.QRect(210, 370, 71, 21))
        self.STOP_LOSS_LABEL.setTextFormat(QtCore.Qt.PlainText)
        self.STOP_LOSS_LABEL.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.STOP_LOSS_LABEL.setObjectName("STOP_LOSS_LABEL")
        self.TAKE_PROFIT_LABEL = QtWidgets.QLabel(self.centralwidget)
        self.TAKE_PROFIT_LABEL.setGeometry(QtCore.QRect(210, 400, 71, 21))
        self.TAKE_PROFIT_LABEL.setTextFormat(QtCore.Qt.PlainText)
        self.TAKE_PROFIT_LABEL.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.TAKE_PROFIT_LABEL.setObjectName("TAKE_PROFIT_LABEL")
        self.TAKE_PROFIT_TEXT = QtWidgets.QLabel(self.centralwidget)
        self.TAKE_PROFIT_TEXT.setGeometry(QtCore.QRect(300, 400, 81, 21))
        self.TAKE_PROFIT_TEXT.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.TAKE_PROFIT_TEXT.setObjectName("TAKE_PROFIT_TEXT")
        self.CURRENCY_PAIRS_COMBOBOX = QtWidgets.QComboBox(self.centralwidget)
        self.CURRENCY_PAIRS_COMBOBOX.setGeometry(QtCore.QRect(10, 340, 110, 23))
        self.CURRENCY_PAIRS_COMBOBOX.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.CURRENCY_PAIRS_COMBOBOX.setEditable(True)
        self.CURRENCY_PAIRS_COMBOBOX.setCurrentText("")
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
        self.CURRENCY_PAIRS_COMBOBOX.addItem("")
        self.BUY_BTN = QtWidgets.QPushButton(self.centralwidget)
        self.BUY_BTN.setGeometry(QtCore.QRect(10, 220, 71, 28))
        self.BUY_BTN.setCheckable(True)
        self.BUY_BTN.setObjectName("BUY_BTN")
        self.SELL_BTN = QtWidgets.QPushButton(self.centralwidget)
        self.SELL_BTN.setGeometry(QtCore.QRect(90, 220, 71, 28))
        self.SELL_BTN.setCheckable(True)
        self.SELL_BTN.setObjectName("SELL_BTN")
        self.BUY_LMT_BTN = QtWidgets.QPushButton(self.centralwidget)
        self.BUY_LMT_BTN.setGeometry(QtCore.QRect(10, 250, 71, 28))
        self.BUY_LMT_BTN.setCheckable(True)
        self.BUY_LMT_BTN.setObjectName("BUY_LMT_BTN")
        self.SELL_LMT_BTN = QtWidgets.QPushButton(self.centralwidget)
        self.SELL_LMT_BTN.setGeometry(QtCore.QRect(90, 250, 71, 28))
        self.SELL_LMT_BTN.setCheckable(True)
        self.SELL_LMT_BTN.setObjectName("SELL_LMT_BTN")
        self.SINGLE_TRADE_BTN = QtWidgets.QPushButton(self.centralwidget)
        self.SINGLE_TRADE_BTN.setGeometry(QtCore.QRect(180, 500, 101, 28))
        self.SINGLE_TRADE_BTN.setCheckable(True)
        self.SINGLE_TRADE_BTN.setObjectName("SINGLE_TRADE_BTN")
        self.SPLIT_TRADE_BTN = QtWidgets.QPushButton(self.centralwidget)
        self.SPLIT_TRADE_BTN.setGeometry(QtCore.QRect(290, 500, 101, 28))
        self.SPLIT_TRADE_BTN.setCheckable(True)
        self.SPLIT_TRADE_BTN.setObjectName("SPLIT_TRADE_BTN")
        self.SELL_STOP_BTN = QtWidgets.QPushButton(self.centralwidget)
        self.SELL_STOP_BTN.setGeometry(QtCore.QRect(90, 280, 71, 28))
        self.SELL_STOP_BTN.setCheckable(True)
        self.SELL_STOP_BTN.setObjectName("SELL_STOP_BTN")
        self.BUY_STOP_BTN = QtWidgets.QPushButton(self.centralwidget)
        self.BUY_STOP_BTN.setGeometry(QtCore.QRect(10, 280, 71, 28))
        self.BUY_STOP_BTN.setCheckable(True)
        self.BUY_STOP_BTN.setObjectName("BUY_STOP_BTN")
        self.MIN_15_BTN = QtWidgets.QPushButton(self.centralwidget)
        self.MIN_15_BTN.setGeometry(QtCore.QRect(10, 150, 71, 28))
        self.MIN_15_BTN.setCheckable(True)
        self.MIN_15_BTN.setObjectName("MIN_15_BTN")
        self.MIN_60_BTN = QtWidgets.QPushButton(self.centralwidget)
        self.MIN_60_BTN.setGeometry(QtCore.QRect(90, 150, 71, 28))
        self.MIN_60_BTN.setCheckable(True)
        self.MIN_60_BTN.setObjectName("MIN_60_BTN")
        self.MIN_1440_BTN = QtWidgets.QPushButton(self.centralwidget)
        self.MIN_1440_BTN.setGeometry(QtCore.QRect(170, 150, 71, 28))
        self.MIN_1440_BTN.setCheckable(True)
        self.MIN_1440_BTN.setObjectName("MIN_1440_BTN")
        self.ORDER_TYPE_LABEL = QtWidgets.QLabel(self.centralwidget)
        self.ORDER_TYPE_LABEL.setGeometry(QtCore.QRect(50, 200, 81, 21))
        self.ORDER_TYPE_LABEL.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.ORDER_TYPE_LABEL.setObjectName("ORDER_TYPE_LABEL")
        self.CURRENC_PAIR_LABEL = QtWidgets.QLabel(self.centralwidget)
        self.CURRENC_PAIR_LABEL.setGeometry(QtCore.QRect(10, 320, 151, 21))
        self.CURRENC_PAIR_LABEL.setAlignment(QtCore.Qt.AlignCenter)
        self.CURRENC_PAIR_LABEL.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.CURRENC_PAIR_LABEL.setObjectName("CURRENC_PAIR_LABEL")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 825, 23))
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
        self.PREPARE_NEW_TRADE_BTN.setText(_translate("MainWindow", "Prepare New Trade"))
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
        self.EXECUTE_NEW_TRADE_BTN.setText(_translate("MainWindow", "Execute New Trade"))
        self.STOP_LOSS_TEXT.setText(_translate("MainWindow", "__________"))
        self.STOP_LOSS_LABEL.setText(_translate("MainWindow", "Stop Loss:"))
        self.TAKE_PROFIT_LABEL.setText(_translate("MainWindow", "Take Profit:"))
        self.TAKE_PROFIT_TEXT.setText(_translate("MainWindow", "__________"))
        self.CURRENCY_PAIRS_COMBOBOX.setPlaceholderText(_translate("MainWindow", "Currency Pairs"))
        self.CURRENCY_PAIRS_COMBOBOX.setItemText(0, _translate("MainWindow", "AUDCAD"))
        self.CURRENCY_PAIRS_COMBOBOX.setItemText(1, _translate("MainWindow", "AUDCHF"))
        self.CURRENCY_PAIRS_COMBOBOX.setItemText(2, _translate("MainWindow", "AUDJPY"))
        self.CURRENCY_PAIRS_COMBOBOX.setItemText(3, _translate("MainWindow", "AUDNZD"))
        self.CURRENCY_PAIRS_COMBOBOX.setItemText(4, _translate("MainWindow", "AUDSGD"))
        self.CURRENCY_PAIRS_COMBOBOX.setItemText(5, _translate("MainWindow", "AUDUSD"))
        self.CURRENCY_PAIRS_COMBOBOX.setItemText(6, _translate("MainWindow", "CADCHF"))
        self.CURRENCY_PAIRS_COMBOBOX.setItemText(7, _translate("MainWindow", "CADJPY"))
        self.CURRENCY_PAIRS_COMBOBOX.setItemText(8, _translate("MainWindow", "CHFJPY"))
        self.CURRENCY_PAIRS_COMBOBOX.setItemText(9, _translate("MainWindow", "CHFSGD"))
        self.CURRENCY_PAIRS_COMBOBOX.setItemText(10, _translate("MainWindow", "EURAUD"))
        self.CURRENCY_PAIRS_COMBOBOX.setItemText(11, _translate("MainWindow", "EURCAD"))
        self.CURRENCY_PAIRS_COMBOBOX.setItemText(12, _translate("MainWindow", "EURCHF"))
        self.CURRENCY_PAIRS_COMBOBOX.setItemText(13, _translate("MainWindow", "EURGBP"))
        self.CURRENCY_PAIRS_COMBOBOX.setItemText(14, _translate("MainWindow", "EURJPY"))
        self.CURRENCY_PAIRS_COMBOBOX.setItemText(15, _translate("MainWindow", "EURNZD"))
        self.CURRENCY_PAIRS_COMBOBOX.setItemText(16, _translate("MainWindow", "EURSGD"))
        self.CURRENCY_PAIRS_COMBOBOX.setItemText(17, _translate("MainWindow", "EURUSD"))
        self.CURRENCY_PAIRS_COMBOBOX.setItemText(18, _translate("MainWindow", "GBPCAD"))
        self.CURRENCY_PAIRS_COMBOBOX.setItemText(19, _translate("MainWindow", "GBPCHF"))
        self.CURRENCY_PAIRS_COMBOBOX.setItemText(20, _translate("MainWindow", "GBPNZD"))
        self.CURRENCY_PAIRS_COMBOBOX.setItemText(21, _translate("MainWindow", "GBPUSD"))
        self.CURRENCY_PAIRS_COMBOBOX.setItemText(22, _translate("MainWindow", "NZDCAD"))
        self.CURRENCY_PAIRS_COMBOBOX.setItemText(23, _translate("MainWindow", "NZDCHF"))
        self.CURRENCY_PAIRS_COMBOBOX.setItemText(24, _translate("MainWindow", "NZDJPY"))
        self.CURRENCY_PAIRS_COMBOBOX.setItemText(25, _translate("MainWindow", "USDCHF"))
        self.CURRENCY_PAIRS_COMBOBOX.setItemText(26, _translate("MainWindow", "USDJPY"))
        self.BUY_BTN.setText(_translate("MainWindow", "BUY"))
        self.SELL_BTN.setText(_translate("MainWindow", "SELL"))
        self.BUY_LMT_BTN.setText(_translate("MainWindow", "BUY LIMIT"))
        self.SELL_LMT_BTN.setText(_translate("MainWindow", "SELL LIMIT"))
        self.SINGLE_TRADE_BTN.setText(_translate("MainWindow", "SINGLE TRADE"))
        self.SPLIT_TRADE_BTN.setText(_translate("MainWindow", "SPLIT TRADE"))
        self.SELL_STOP_BTN.setText(_translate("MainWindow", "SELL STOP"))
        self.BUY_STOP_BTN.setText(_translate("MainWindow", "BUY STOP"))
        self.MIN_15_BTN.setText(_translate("MainWindow", "15 MIN"))
        self.MIN_60_BTN.setText(_translate("MainWindow", "1 HR"))
        self.MIN_1440_BTN.setText(_translate("MainWindow", "DAILY"))
        self.ORDER_TYPE_LABEL.setText(_translate("MainWindow", "ORDER TYPE"))
        self.CURRENC_PAIR_LABEL.setText(_translate("MainWindow", "CURRENCY PAIR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
