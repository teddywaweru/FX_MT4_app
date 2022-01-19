import sys
import time
from pathlib import Path
from PyQt5 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Slot, Qt
from UI_templates import main_window as main_window
# from DWX_ZeroMQ_Connector_v2_0_1_RC8 import DWX_ZeroMQ_Connector as dwx
from dwx_connector_MVC import DwxModel
from table_MVC import TableModel
import pandas as pd


class CallUi(QtWidgets.QMainWindow):
    """[summary]

    Args:
        QtWidgets ([type]): [description]
    """    

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)

        self.dwx_MVC = DwxModel()
        self.ui = main_window.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setUpBtnconnect()
        # self.setUpLabelconnect()

        #ADD textlabel function to be loaded, similar to setupBtnconnect
        # also for text edits,
        #writing functions instead of loading in the __init__ will make the code more organized.

        data = [
            [4, 9, 2],
            [1, 0, 0],
            [3, 5, 0],
            [3, 3, 2],
            [7, 8, 9],
        ]

        data = pd.DataFrame(data)

        self.table_model = TableModel(data)
        self.ui.tableView.setModel(self.table_model)



    def setUpBtnconnect(self):   
        self.ui.INIT_CONNECTOR_BTN.clicked.connect(DwxModel)
        test_hist_req_data = [
            {'_symbol': 'EURUSD', '_timeframe': 1440, '_start': '2021.01.01 00:00:00', '_end': pd.Timestamp.now().strftime('%Y.%m.%d %H.%M.00') }
        ]
        self.ui.SEND_HIST_REQUEST_BTN.clicked.connect(self.dwx_MVC.send_hist_request)
        self.ui.PREPARE_NEW_TRADE.clicked.connect(self.prepare_new_trade)
        # self.ui.tableView.setRowCount(5)
        # self.ui.pushButton.clicked.connect(self.myFunction)

    # def myFunction(self):
    #     os.system("ipconfig")
    #     # raw_input()


    def prepare_new_trade(self):
        
        _symbol = self.ui.CURRENCY_PAIRS_COMBOBOX.currentText()
        if _symbol not in [self.ui.CURRENCY_PAIRS_COMBOBOX.itemText(i) for i in range(self.ui.CURRENCY_PAIRS_COMBOBOX.count())]:
            _symbol = 'EURUSD'
        #Check if the text entered is a valid currency pair that can be operated on ie. existing pairs on the list.
        #Else default value is EURUSD
        
        _order = 'BUY' if self.ui.BUY_SELL_SLIDER.sliderPosition() else 'SELL'
        #Default value of sider is 'SELL' (0)

        _timeframe = 1440 

        new_trade_dict = {
            '_symbol': _symbol,
            '_order': _order,
            '_timeframe': _timeframe
        }
        prep_new_trade = self.dwx_MVC.prepare_new_trade(new_trade_dict)
        print(prep_new_trade.pip_value)
        print('Completed')
        self.ui.PIP_VALUE_TEXT.setText(str(round(prep_new_trade.pip_value, 4)))
        self.ui.ATR_IN_PIPS_TEXT.setText(str(round(prep_new_trade.atr_in_pips, 2)))
        self.ui.LOT_SIZE_TEXT.setText(str(str(round(prep_new_trade.lot_size, 2))))
        self.ui.RISK_AMOUNT_TEXT.setText(str(round(prep_new_trade.risk_amount, 4)))
        self.ui.ACCOUNT_BALANCE_TEXT.setText(str(prep_new_trade.account_info['_data']['accountequity']))
        self.ui.STOP_LOSS_TEXT.setText(str(round(prep_new_trade.stop_loss, 5)))
        self.ui.TAKE_PROFIT_TEXT.setText(str(round(prep_new_trade.take_profit, 5)))

    # def setUpLabelconnect(self):

def setUpWindow():
    """
    Initialize app window
    """    
    app = QtWidgets.QApplication(sys.argv)
    nowWindow = CallUi()
    nowWindow.show()
    sys.exit(app.exec_())