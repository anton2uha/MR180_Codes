import RPi.GPIO as GPIO
import time

class supply_04var121:
    def __init__(self, cs_pin, updown_pin, sw1_pin, sw2_pin, sw3_pin, sw4_pin):
        self.cs = cs_pin
        self.updown = updown_pin
        self.sw1 = sw1_pin 
        self.sw2 = sw2_pin
        self.sw3 = sw3_pin
        self.sw4  =sw4_pin
        
        #Config Analog switch component's pins
        GPIO.setup(self.sw1,GPIO.OUT)     
        GPIO.setup(self.sw2,GPIO.OUT)
        GPIO.setup(self.sw3,GPIO.OUT)
        GPIO.setup(self.sw4,GPIO.OUT)
        #Resetting Analog switch component's pins
        GPIO.output(self.sw1,GPIO.LOW)
        GPIO.output(self.sw2,GPIO.LOW)
        GPIO.output(self.sw3,GPIO.LOW)
        GPIO.output(self.sw4,GPIO.LOW)

        #Config Dig_pot component's pins
        GPIO.setup(self.cs,GPIO.OUT)
        GPIO.setup(self.updown,GPIO.OUT)

    def config_up(self):
        # configures the dig_pot to count up
        GPIO.output(self.cs,GPIO.HIGH)       
        GPIO.output(self.updown,GPIO.HIGH)       

    def config_down(self):
        # configures the dig_pot to count down
        GPIO.output(self.cs,GPIO.HIGH)
        GPIO.output(self.updown,GPIO.LOW)        
        

    def count_up_full(self):
        # Disabling parralel switches
        GPIO.output(self.sw1,GPIO.LOW)
        GPIO.output(self.sw2,GPIO.LOW)
        GPIO.output(self.sw3,GPIO.LOW)
        GPIO.output(self.sw4,GPIO.LOW)
        # setting cs low while updown is settled
        GPIO.output(self.cs,GPIO.LOW)

        for k in range(1,65,1):
            GPIO.output(self.updown,GPIO.LOW)       
            time.sleep(0.001)               
            GPIO.output(self.updown,GPIO.HIGH)        
            time.sleep(0.001)                   
            GPIO.output(self.updown,GPIO.LOW) 
            print('{} Step Up' .format(k))
            time.sleep(2)
        #Disable the dig_pot
        GPIO.output(self.cs,GPIO.HIGH)

    def count_up_stp(self,step):
        # max_step is 64
        # setting cs low while updown is settled
        GPIO.output(self.cs,GPIO.LOW)

        for k in range(0,step,1):
            GPIO.output(self.updown,GPIO.LOW)       
            time.sleep(0.001)               
            GPIO.output(self.updown,GPIO.HIGH)        
            time.sleep(0.001)                   
            GPIO.output(self.updown,GPIO.LOW)
            k2 = k + 1 
            print('{} Step Up' .format(k2))
            time.sleep(2)
        # Disable the dig_pot
        GPIO.output(self.cs,GPIO.HIGH)
    
    def count_down_full(self):
        # Disabling parralel switches
        GPIO.output(self.sw1,GPIO.LOW)
        GPIO.output(self.sw2,GPIO.LOW)
        GPIO.output(self.sw3,GPIO.LOW)
        GPIO.output(self.sw4,GPIO.LOW)
        # setting cs low while updown is settled        
        GPIO.output(self.cs,GPIO.LOW)
        for k in range(1,65,1):
            if k != 64:
                GPIO.output(self.updown,GPIO.HIGH)
                time.sleep(0.001)
                GPIO.output(self.updown,GPIO.LOW)
                print('{} Step Down' .format(k))
                time.sleep(2)
            else:
                GPIO.output(self.updown,GPIO.HIGH)
                time.sleep(0.001)
                print('{} Final Step' .format(k))
                time.sleep(2)
        # Disable the dig_pot
        GPIO.output(self.cs,GPIO.HIGH)
        # Enabling parralel switches
        GPIO.output(self.sw1,GPIO.HIGH)
        print('1st SW Enabled')
        time.sleep(2)
        GPIO.output(self.sw2,GPIO.HIGH)
        print('2nd SW Enabled')
        time.sleep(2)
        GPIO.output(self.sw3,GPIO.HIGH)
        print('3rd SW Enabled')
        time.sleep(2)
        GPIO.output(self.sw4,GPIO.HIGH)
        print('4th SW Enabled')
        time.sleep(2)


    def count_down_stp(self,step):
        # max_step is 64
        # setting cs low while updown is settled
        GPIO.output(self.cs,GPIO.LOW)
        for k in range(0,step,1):
            GPIO.output(self.updown,GPIO.HIGH)
            time.sleep(0.001)
            GPIO.output(self.updown,GPIO.LOW)
            k2 = k + 1
            print('{} Step Down' .format(k2))
            time.sleep(2) 
        # Disable the dig_pot
        GPIO.output(self.cs,GPIO.HIGH)

               
    def switch_en(self,sw_num):
        match sw_num:
            case 1:
                GPIO.output(self.sw1,GPIO.HIGH)
                print('1st SW Enabled')
                time.sleep(2)
            case 2:
                GPIO.output(self.sw2,GPIO.HIGH)
                print('2nd SW Enabled')
                time.sleep(2)
            case 3:
                GPIO.output(self.sw3,GPIO.HIGH)
                print('3rd SW Enabled')
                time.sleep(2)                
            case 4:
                GPIO.output(self.sw4,GPIO.HIGH)
                print('4th SW Enabled')
                time.sleep(2)  

    def switch_dis(self,sw_num):
        match sw_num:
            case 1:
                GPIO.output(self.sw1,GPIO.LOW)
                print('1st SW Disabled')
                time.sleep(2)
            case 2:
                GPIO.output(self.sw2,GPIO.LOW)
                print('2nd SW Disabled')
                time.sleep(2)
            case 3:
                GPIO.output(self.sw3,GPIO.LOW)
                print('3rd SW Disabled')
                time.sleep(2)                
            case 4:
                GPIO.output(self.sw4,GPIO.LOW)
                print('4th SW Disabled')
                time.sleep(2)

    def dis_switches_all(self):
        # Disabling parralel switches
        GPIO.output(self.sw1,GPIO.LOW)
        GPIO.output(self.sw2,GPIO.LOW)
        GPIO.output(self.sw3,GPIO.LOW)
        GPIO.output(self.sw4,GPIO.LOW)
        print('All Paralel Switches Disabled...')
        time.sleep(2)

    def en_switches_all(self):
        # Disabling parralel switches
        GPIO.output(self.sw1,GPIO.HIGH)
        GPIO.output(self.sw2,GPIO.HIGH)
        GPIO.output(self.sw3,GPIO.HIGH)
        GPIO.output(self.sw4,GPIO.HIGH)
        print('All Paralel Switches Enabled...')
        time.sleep(2)    


