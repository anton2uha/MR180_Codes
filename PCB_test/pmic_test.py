import RPi.GPIO as GPIO
import time
import smbus
from libraries import INA233


class main2():
    def __init__(self):
        self.pmic = None

    def breadboard_init(self):
        print('Initiating breadboard')
        GPIO.setmode(GPIO.BCM)
        self.pmic = INA233()
    
    def my_vbus(self):
        if self.pmic:
            vb = self.pmic.read_vbus()
            print(f"Here is the Voltage on VBus: {vb}")
        else:
            print('LCAS PMIC Component is Not Setup')
    
    def my_vshunt(self):
        if self.pmic:
            vsh = self.pmic.read_vshunt()
            print(f"Here is the Voltage on VShunt: {vsh}")
        else:
            print('LCAS PMIC Component is Not Setup')
    
    def my_iin(self):
        if self.pmic:
            i_in = self.pmic.read_iin()
            print(f"Here is the Input Current: {i_in}")
        else:
            print('LCAS PMIC Component is Not Setup')

    
    def my_pwr(self):
        if self.pmic:
            pwr = self.pmic.read_pwr()
            print(f"Here is the Power: {pwr}")
        else:
            print('LCAS PMIC Component is Not Setup')


def cleanup():
    GPIO.cleanup()

if __name__ == "__main__":
    try:
        script_run = main2()
        script_run.breadboard_init()
        print('Breadboard Configured')
        print('Now Running the Methods')
        script_run.my_vbus()
        script_run.my_vshunt()
        script_run.my_iin()
        script_run.my_pwr()
    except KeyboardInterrupt:
        cleanup()





