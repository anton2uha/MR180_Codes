import RPi.GPIO as GPIO
import time
import smbus
from libraries import ADS1115


adc_addr = 0x48



class adc_main():
    def __init__(self):
        self.adc = None

    def breadboard_init(self):
        GPIO.setmode(GPIO.BCM)
        self.adc = ADS1115()


    def read_amon(self):
        self.adc.set_addr_ADS1115(adc_addr)
        self.adc.set_gain(0x06)
        self.adc.set_channel(3)
        read_amon = self.adc.read_voltage(3)
        return read_amon
    
if __name__ == "__main__":

    try:
        main_run = adc_main()
        main_run.breadboard_init()
        amon_value = main_run.read_amon()
        print ("AMON:%fmV"%(amon_value['r']))

    except KeyboardInterrupt:
        print('Finished')
