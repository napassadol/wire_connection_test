import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from templates.main import Ui_Form as Ui_main
from templates.config import Ui_Form as Ui_config
from templates.setting import Ui_Form as Ui_setting
from templates.machine_setup import Ui_Form as Ui_machine
# from control import Control

class MyApp(QMainWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.main = Ui_main()
        self.setting = Ui_setting()
        self.config = Ui_config()
        self.machine = Ui_machine()

        self.machine.setupUi(self)
        self.machine.widget.hide()

        self.main.setupUi(self)
        
        self.setting.setupUi(self)
        self.setting.widget.hide()

        self.config.setupUi(self)
        self.config.widget.hide()

        self.init_button()
        self.control = Control(self.setting, self.config, self.main)

    def init_button(self):
        self.setting.button_config.clicked.connect(self.config.widget.show)
        self.setting.button_config.clicked.connect(self.setting.widget.hide)

        self.setting.button_exit.clicked.connect(self.main.widget.show)
        self.setting.button_exit.clicked.connect(self.setting.widget.hide)

        # self.setting.button_set.clicked.connect(lambda :self.setOperator())
        self.setting.button_set.clicked.connect(self.machine.widget.show)
        self.setting.button_set.clicked.connect(self.setting.widget.hide)

        self.config.button_set.clicked.connect(lambda :self.setOperatorConfig())
        self.config.button_set.clicked.connect(self.setting.widget.show)
        self.config.button_set.clicked.connect(self.config.widget.hide)

        self.config.button_set_2.clicked.connect(self.setting.widget.show)
        self.config.button_set_2.clicked.connect(self.config.widget.hide)

        self.main.setting_button.clicked.connect(self.setting.widget.show)
        self.main.setting_button.clicked.connect(self.main.widget.hide)

        self.machine.button_back.clicked.connect(self.setting.widget.show)
        self.machine.button_back.clicked.connect(self.machine.widget.hide)

        self.machine.button_ok.clicked.connect(self.setting.widget.show)
        self.machine.button_ok.clicked.connect(self.machine.widget.hide)
    
    def setOperator(self):
        # self.control.setOperator()
        pass

    def setOperatorConfig(self):
        # self.control.setOperatorConfig()
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myapp = MyApp()
    myapp.show()
    sys.exit(app.exec_())