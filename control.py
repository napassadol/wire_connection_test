import RPi.GPIO as GPIO
import time
import board
import busio
# import adafruit_ads1x15.ads1115 as ADS
# from adafruit_ads1x15.analog_in import AnalogIn

ads = None

pins = {
    'r1': 35,
    'l1': 36,
    'ohm': 37,
    'short': 38,
    'bypass': 40,
    'mode': 11,
    'start': 12,
    'count_ok': 13,
    'emergency': 15,
    'ferrier': 16,
    'pen_ok': 7,
    'n_pen': 18,
    'n_d': 22,
    'n_k': 29,
    'l_fail': 31,
    'l_pass': 32,
    'l_count_ok': 33,
    'in_r1': 8,
    'in_l1': 19
}

def initialPins():
    global ads
    # GPIO.setmode(GPIO.BOARD)

    GPIO.setup(pins['r1'], GPIO.OUT)
    GPIO.setup(pins['l1'], GPIO.OUT)
    GPIO.setup(pins['ohm'], GPIO.OUT)
    GPIO.setup(pins['short'], GPIO.OUT)
    GPIO.setup(pins['bypass'], GPIO.OUT)

    GPIO.setup(pins['pen_ok'], GPIO.OUT)
    GPIO.setup(pins['n_pen'], GPIO.OUT)
    GPIO.setup(pins['n_d'], GPIO.OUT)
    GPIO.setup(pins['n_k'], GPIO.OUT)
    GPIO.setup(pins['l_fail'], GPIO.OUT)
    GPIO.setup(pins['l_pass'], GPIO.OUT)
    GPIO.setup(pins['l_count_ok'], GPIO.OUT)

    GPIO.setup(pins['mode'], GPIO.IN) #auto
    GPIO.setup(pins['start'], GPIO.IN) #start
    GPIO.setup(pins['count_ok'], GPIO.IN) #count ok
    GPIO.setup(pins['emergency'], GPIO.IN) #emergency
    GPIO.setup(pins['ferrier'], GPIO.IN) #ferrier

    GPIO.setup(pins['in_r1'], GPIO.IN)
    GPIO.setup(pins['in_l1'], GPIO.IN)

    GPIO.output(pins['r1'], 0)
    GPIO.output(pins['l1'], 1)
    GPIO.output(pins['ohm'], 1)
    GPIO.output(pins['short'], 1)
    GPIO.output(pins['bypass'], 1)

    GPIO.output(pins['pen_ok'], 1)
    GPIO.output(pins['n_pen'], 1)
    GPIO.output(pins['n_d'], 1)
    GPIO.output(pins['n_k'], 1)
    GPIO.output(pins['l_fail'], 1)
    GPIO.output(pins['l_pass'], 1)
    GPIO.output(pins['l_count_ok'], 1)

    # i2c = busio.I2C(board.SCL, board.SDA)
    i2c = busio.I2C(5, 3)
    # ads = ADS.ADS1115(i2c)

    print('initial pin success')

    # chan0 = AnalogIn(ads, ADS.P0)
    # chan1 = AnalogIn(ads, ADS.P1)
    # chan2 = AnalogIn(ads, ADS.P2)
    # print("{:>2} | {:>2} | {:>2}".format(chan0.voltage, chan1.voltage, chan2.voltage))
    # GPIO.add_event_detect(cash_box, GPIO.FALLING, callback=calculateCash, bouncetime=50)
    # def calculateCash(channel):

    # adc0 = adc.read_adc(0, gain=GAIN) * 0.1875 / 1000

class Control():
    def __init__(self, ui_setting, ui_config, ui_main):
        self.setting = ui_setting
        self.config = ui_config
        self.main = ui_main
        self.param = dict()
        self.param['setting'] = {
            'yeild': False,
            'label': True,
            'report': True,
            'count': 10,
            'ip': '0.0.0.0'
        }
        self.param['config'] = {
            'model': 'AAA',
            'revision': '001',
            'name': 'test',
            'connect': '10.0',
            'resistance': '500.1',
            'isolate': '10.0'
        }
        self.count = 0
        self.lpass = 0
        self.fail = 0
        self.yeild = 0
        self.setUI()
        initialPins()

    def setUI(self):
        self.setting.check_box_yeild.setChecked(self.param['setting']['yeild'])
        self.setting.check_box_print_label.setChecked(self.param['setting']['label'])
        self.setting.check_box_report.setChecked(self.param['setting']['report'])
        self.setting.spin_box_count_set.setValue(self.param['setting']['count'])
        self.setting.label_ip.setText(self.param['setting']['ip'])

        self.config.label_model.setText(self.param['config']['model'])
        self.config.label_revision.setText(self.param['config']['revision'])
        self.config.label_name.setText(self.param['config']['name'])
        self.config.label_check_connect_level.setText(str(self.param['config']['connect']))
        self.config.label_resistance_limit.setText(str(self.param['config']['resistance']))
        self.config.label_isolate_limit.setText(str(self.param['config']['isolate']))

        self.main.label_count.setText('Count: ' + str(self.count))
        self.main.label_count.setText('Pass: ' + str(self.lpass))
        self.main.label_count.setText('Fail: ' + str(self.fail))
        self.main.label_count.setText('Yeild: ' + str(self.yeild))
    
    def setOperator(self):
        self.param['setting'] = {
            'yeild': self.setting.check_box_yeild.isChecked,
            'label': self.setting.check_box_print_label.isChecked,
            'report': self.setting.check_box_report.isChecked,
            'count': self.setting.spin_box_count_set.value,
            'ip': self.setting.label_ip.text
        }
    
    def setOperatorConfig(self):
        self.param['config'] = {
            'model': self.config.label_model.text,
            'revision': self.config.label_revision.text,
            'name': self.config.label_name.text,
            'connect': self.config.label_check_connect_level.text,
            'resistance': self.config.label_check_connect_level.text,
            'isolate': self.config.label_check_connect_level.text
        }
    
    def checkFerier(self):
        ferrier = GPIO.input(pins['ferrier'])
        if ferrier == 0:
            return False
        else:
            return True

    def checkWireConnectionR1(self):
        in_r1 = GPIO.input(pins['in_r1'])
        in_l1 = GPIO.input(pins['in_l1'])

        result = {
            'status': True,
            'message': 'PASS'
        }
        if in_r1 == 1 and in_l1 == 0:
            return result
        elif in_r1 == 0 and in_l1 == 0:
            result['status'] = False
            result['message'] = 'FAULT สายขาด'
        elif in_r1 == 0 and in_l1 == 1:
            result['status'] = False
            result['message'] = 'FAULT สายสลับ'
        elif in_r1 == 1 and in_l1 == 1:
            result['status'] = False
            result['message'] = 'FAULT สายช๊อต'
        return result
    
    def checkWireConnectionL1(self):
        in_r1 = GPIO.input(pins['in_r1'])
        in_l1 = GPIO.input(pins['in_l1'])

        result = {
            'status': True,
            'message': 'PASS'
        }
        if in_r1 == 0 and in_l1 == 1:
            return result
        elif in_r1 == 0 and in_l1 == 0:
            result['status'] = False
            result['message'] = 'FAULT สายขาด'
        elif in_r1 == 1 and in_l1 == 0:
            result['status'] = False
            result['message'] = 'FAULT สายสลับ'
        elif in_r1 == 1 and in_l1 == 1:
            result['status'] = False
            result['message'] = 'FAULT สายช๊อต'
        return result
    
    def readVR1(self):
        global ads
        vr1 = AnalogIn(ads, ADS.P0)
        return vr1 * 12 / 5
    
    def readVL1(self):
        global ads
        vr1 = AnalogIn(ads, ADS.P1)
        return vr1 * 12 / 5

    def testConnectionWire(self):
        if self.checkFerier() == False:
            self.main.label_ferite.setStyleSheet("background:rgb(255, 0, 0)")
            self.main.label_ferite.setText("FAIL")
            return
        
        self.main.label_ferite.setStyleSheet("background:rgb(0, 255, 0)")
        self.main.label_ferite.setText("PASS")

        GPIO.output(pins['n_pen'], 0)
        GPIO.output(pins['n_d'], 0)
        GPIO.output(pins['n_k'], 0)
        GPIO.output(pins['bypass'], 0)
        time.sleep(0.15)

        GPIO.output(pins['r1'], 0)
        wire_conn_r1 = self.checkWireConnectionR1()
        if wire_conn_r1['status'] == False:
            self.main.label_wireconn_status.setStyleSheet("background:rgb(255, 0, 0)")
            self.main.label_wireconn_status.setText("FAIL")
            return
        
        vr1 = self.readVR1()
        if vr1 < 10:
            self.main.label_wireconn_status.setStyleSheet("background:rgb(255, 0, 0)")
            self.main.label_wireconn_status.setText("FAIL")
            return
        
        GPIO.output(pins['r1'], 1)
        GPIO.output(pins['l1'], 0)
        wire_conn_l1 = self.checkWireConnectionL1()
        if wire_conn_l1['status'] == False:
            self.main.label_wireconn_status.setStyleSheet("background:rgb(255, 0, 0)")
            self.main.label_wireconn_status.setText("FAIL")
            return
        
        vl1 = self.readVL1()
        if vl1 < 10:
            self.main.label_wireconn_status.setStyleSheet("background:rgb(255, 0, 0)")
            self.main.label_wireconn_status.setText("FAIL")
            return
        
        volt_res = (vl1 + vr1) / 2
        self.main.label_wireconn_status.setStyleSheet("background:rgb(0, 255, 0)")
        self.main.label_wireconn_status.setText(str(volt_res))
        
        GPIO.output(pins['l1'], 1)
        GPIO.output(pins['bypass'], 0)
        


