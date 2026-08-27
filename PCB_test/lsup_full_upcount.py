import RPi.GPIO as GPIO
import time
from libraries import supply_04var121



# POT ctl
pot_cs = 22
pot_ud = 27

# SW ctl 
ctl_sw1 = 9
ctl_sw2 = 15
ctl_sw3 = 14
ctl_sw4 = 10

# Level shifter En
lv_en = 19

# Chip ctl
scl_lcas = 11
sda_lcas = 0
rst_lcas = 5
dmon_lcas = 6

# Ken's group rst
rst_cmos = 13

class Main:
    def __init__(self):
        self.lcas_supp = None
    
    def pcb_init(self):
        print('Configfuring The PCB')
        GPIO.setmode(GPIO.BCM)
        self.lcas_supp = supply_04var121(pot_cs,pot_ud,ctl_sw1,ctl_sw2,ctl_sw3,ctl_sw4)


    def lcas_supp_full_up_count(self):
        if self.lcas_supp:
            self.lcas_supp.config_up()
            print('LCAS supply Configured for Up Count...')
            time.sleep(2)
            print('Beginning Up Count...')
            self.lcas_supp.count_up_full()
        else:
            print('LCAS Supply Component is Not Configured...')


def cleanup():
    GPIO.cleanup()

if __name__ == "__main__":
    try:
        main_run = Main()
        main_run.pcb_init()
        main_run.lcas_supp_full_up_count()
    except KeyboardInterrupt:
        
        print('  Script Terminated')
