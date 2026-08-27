import RPi.GPIO as GPIO
import time
import os
import smbus
from libraries import INA233
from libraries import ADS1115
import csv
# import pigpio
# pi = pigpio.pi()

######################################################################################################################################
main_dir = os.getcwd()
i2c_path = os.getcwd()
i2c_path = os.path.join(i2c_path,'i2c_files')
# i2c_path = os.path.join(i2c_path,'mac1_offset_L_w1')          # This is the Test Directory Name - Please Specify for each individual test

starting_mac = 5                                          # please specify which MAC is your starting point
num_of_macs = 1                                           # please specify how mant MACs you have the data for
num_of_files_each_test = 2                            # Please Specify How many i2c files are in each test
clock_speed = 10e6                                       # Please specify your MACs clock rate

filter_rc = (60e3)*(10e-6)
noise_sample = 100000*(1/clock_speed)
wait_time = (filter_rc*5 + noise_sample)


#time_step = 5e-9
time_step = 5
quarter_period = 1 * time_step                          # This is the quarter of either LOW or HIGH state on rst, sda & scl
######################### i2c_lib #############################
i2c_lib_path = os.path.join(main_dir,'i2c_lib')
all_rst_path = os.path.join(i2c_lib_path,'all_zero')
amon_rst_path = os.path.join(i2c_lib_path,'amon_rst')                           # amon_rst should be called everytime you wanna read something from AMON
dac0_mon_path = os.path.join(i2c_lib_path,'dac0_macR_actN_mon')
dac1_mon_path = os.path.join(i2c_lib_path,'dac1_macR_actP_mon')
dac2_mon_path = os.path.join(i2c_lib_path,'dac2_macR_wghtN_mon')
dac3_mon_path = os.path.join(i2c_lib_path,'dac3_macR_wghtP_mon')
dac4_mon_path = os.path.join(i2c_lib_path,'dac4_macL_actN_mon')
dac5_mon_path = os.path.join(i2c_lib_path,'dac5_macL_actP_mon')
dac6_mon_path = os.path.join(i2c_lib_path,'dac6_macL_wghtN_mon')
dac7_mon_path = os.path.join(i2c_lib_path,'dac7_macL_wghtP_mon')
vdd_mon_path = os.path.join(i2c_lib_path,'vdd_mon')
vss_mon_path = os.path.join(i2c_lib_path,'vss_mon')
mac1_noise_mon_path = os.path.join(i2c_lib_path,'mac1_noise_mon')
mac2_noise_mon_path = os.path.join(i2c_lib_path,'mac2_noise_mon')
mac3_noise_mon_path = os.path.join(i2c_lib_path,'mac3_noise_mon')
mac4_noise_mon_path = os.path.join(i2c_lib_path,'mac4_noise_mon')
mac5_noise_mon_path = os.path.join(i2c_lib_path,'mac5_noise_mon')
mac6_noise_mon_path = os.path.join(i2c_lib_path,'mac6_noise_mon')
mac7_noise_mon_path = os.path.join(i2c_lib_path,'mac7_noise_mon')
mac8_noise_mon_path = os.path.join(i2c_lib_path,'mac8_noise_mon')
mac9_noise_mon_path = os.path.join(i2c_lib_path,'mac9_noise_mon')
mac10_noise_mon_path = os.path.join(i2c_lib_path,'mac10_noise_mon')
mac11_noise_mon_path = os.path.join(i2c_lib_path,'mac11_noise_mon')
mac12_noise_mon_path = os.path.join(i2c_lib_path,'mac12_noise_mon')
mac13_noise_mon_path = os.path.join(i2c_lib_path,'mac13_noise_mon')
mac14_noise_mon_path = os.path.join(i2c_lib_path,'mac14_noise_mon')
mac15_noise_mon_path = os.path.join(i2c_lib_path,'mac15_noise_mon')
mac16_noise_mon_path = os.path.join(i2c_lib_path,'mac16_noise_mon')

def rst_all():
        rst = []
        sda = []
        scl = []
        read_i2c_file(all_rst_path,rst,sda,scl)
        send_i2c_file_2pi(rst,sda,scl)

def rst_amon():
        rst = []
        sda = []
        scl = []
        read_i2c_file(amon_rst_path,rst,sda,scl)
        send_i2c_file_2pi(rst,sda,scl)

def mon_vdd():
        rst_amon()
        rst = []
        sda = []
        scl = []
        read_i2c_file(vdd_mon_path,rst,sda,scl)
        send_i2c_file_2pi(rst,sda,scl)
        chp_vdd = chp_adc.read_amon()
        print ("On-chip VDD:%fmV"%(chp_vdd['r']))
        return chp_vdd

def mon_vss():
        rst_amon()
        rst = []
        sda = []
        scl = []
        read_i2c_file(vss_mon_path,rst,sda,scl)
        send_i2c_file_2pi(rst,sda,scl)
        chp_vss = chp_adc.read_amon()
        print ("On-chip VSS:%fmV"%(chp_vss['r']))
        return chp_vss

def mon_dac0_macR_actN():
        rst_amon()
        rst = []
        sda = []
        scl = []
        read_i2c_file(dac0_mon_path,rst,sda,scl)
        send_i2c_file_2pi(rst,sda,scl)
        chp_dac0 = chp_adc.read_amon()
        print ("AMON:%fmV"%(chp_dac0['r']))
        return chp_dac0

def mon_dac1_macR_actP():
        rst_amon()
        rst = []
        sda = []
        scl = []
        read_i2c_file(dac1_mon_path,rst,sda,scl)
        send_i2c_file_2pi(rst,sda,scl)
        chp_dac1 = chp_adc.read_amon()
        print ("AMON:%fmV"%(chp_dac1['r']))
        return chp_dac1

def mon_dac2_macR_wghtN():
        rst_amon()
        rst = []
        sda = []
        scl = []
        read_i2c_file(dac2_mon_path,rst,sda,scl)
        send_i2c_file_2pi(rst,sda,scl)
        chp_dac2 = chp_adc.read_amon()
        print ("AMON:%fmV"%(chp_dac2['r']))
        return chp_dac2

def mon_dac3_macR_wghtP():
        rst_amon()
        rst = []
        sda = []
        scl = []
        read_i2c_file(dac3_mon_path,rst,sda,scl)
        send_i2c_file_2pi(rst,sda,scl)
        chp_dac3 = chp_adc.read_amon()
        print ("AMON:%fmV"%(chp_dac3['r']))
        return chp_dac3

def mon_dac4_macL_actN():
        rst_amon()
        rst = []
        sda = []
        scl = []
        read_i2c_file(dac4_mon_path,rst,sda,scl)
        send_i2c_file_2pi(rst,sda,scl)
        chp_dac4 = chp_adc.read_amon()
        print ("AMON:%fmV"%(chp_dac4['r']))
        return chp_dac4

def mon_dac5_macL_actP():
        rst_amon()
        rst = []
        sda = []
        scl = []
        read_i2c_file(dac5_mon_path,rst,sda,scl)
        send_i2c_file_2pi(rst,sda,scl)
        chp_dac5 = chp_adc.read_amon()
        print ("AMON:%fmV"%(chp_dac5['r']))
        return chp_dac5

def mon_dac6_macL_wghtN():
        rst_amon()
        rst = []
        sda = []
        scl = []
        read_i2c_file(dac6_mon_path,rst,sda,scl)
        send_i2c_file_2pi(rst,sda,scl)
        chp_dac6 = chp_adc.read_amon()
        print ("AMON:%fmV"%(chp_dac6['r']))
        return chp_dac6

def mon_dac7_macL_wghtP():
        rst_amon()
        rst = []
        sda = []
        scl = []
        read_i2c_file(dac7_mon_path,rst,sda,scl)
        send_i2c_file_2pi(rst,sda,scl)
        chp_dac7 = chp_adc.read_amon()
        print ("AMON:%fmV"%(chp_dac7['r']))
        return chp_dac7

def mon_mac1_noise():
        rst_amon()
        rst = []
        sda = []
        scl = []
        read_i2c_file(mac1_noise_mon_path,rst,sda,scl)
        send_i2c_file_2pi(rst,sda,scl)
        chp_mac1_noise = chp_adc.read_amon()
        print ("AMON:%fmV"%(chp_mac1_noise['r']))
        return chp_mac1_noise

def mon_mac2_noise():
        rst_amon()
        rst = []
        sda = []
        scl = []
        read_i2c_file(mac2_noise_mon_path,rst,sda,scl)
        send_i2c_file_2pi(rst,sda,scl)
        chp_mac2_noise = chp_adc.read_amon()
        print ("AMON:%fmV"%(chp_mac2_noise['r']))
        return chp_mac2_noise

def mon_mac3_noise():
        rst_amon()
        rst = []
        sda = []
        scl = []
        read_i2c_file(mac3_noise_mon_path,rst,sda,scl)
        send_i2c_file_2pi(rst,sda,scl)
        chp_mac3_noise = chp_adc.read_amon()
        print ("AMON:%fmV"%(chp_mac3_noise['r']))
        return chp_mac3_noise

def mon_mac4_noise():
        rst_amon()
        rst = []
        sda = []
        scl = []
        read_i2c_file(mac4_noise_mon_path,rst,sda,scl)
        send_i2c_file_2pi(rst,sda,scl)
        chp_mac4_noise = chp_adc.read_amon()
        print ("AMON:%fmV"%(chp_mac4_noise['r']))
        return chp_mac4_noise

def mon_mac5_noise():
        rst_amon()
        rst = []
        sda = []
        scl = []
        read_i2c_file(mac5_noise_mon_path,rst,sda,scl)
        send_i2c_file_2pi(rst,sda,scl)
        chp_mac5_noise = chp_adc.read_amon()
        print ("AMON:%fmV"%(chp_mac5_noise['r']))
        return chp_mac5_noise

def mon_mac6_noise():
        rst_amon()
        rst = []
        sda = []
        scl = []
        read_i2c_file(mac6_noise_mon_path,rst,sda,scl)
        send_i2c_file_2pi(rst,sda,scl)
        chp_mac6_noise = chp_adc.read_amon()
        print ("AMON:%fmV"%(chp_mac6_noise['r']))
        return chp_mac6_noise

def mon_mac7_noise():
        rst_amon()
        rst = []
        sda = []
        scl = []
        read_i2c_file(mac7_noise_mon_path,rst,sda,scl)
        send_i2c_file_2pi(rst,sda,scl)
        chp_mac7_noise = chp_adc.read_amon()
        print ("AMON:%fmV"%(chp_mac7_noise['r']))
        return chp_mac7_noise

def mon_mac8_noise():
        rst_amon()
        rst = []
        sda = []
        scl = []
        read_i2c_file(mac8_noise_mon_path,rst,sda,scl)
        send_i2c_file_2pi(rst,sda,scl)
        chp_mac8_noise = chp_adc.read_amon()
        print ("AMON:%fmV"%(chp_mac8_noise['r']))
        return chp_mac8_noise

def mon_mac9_noise():
        rst_amon()
        rst = []
        sda = []
        scl = []
        read_i2c_file(mac9_noise_mon_path,rst,sda,scl)
        send_i2c_file_2pi(rst,sda,scl)
        chp_mac9_noise = chp_adc.read_amon()
        print ("AMON:%fmV"%(chp_mac9_noise['r']))
        return chp_mac9_noise

def mon_mac10_noise():
        rst_amon()
        rst = []
        sda = []
        scl = []
        read_i2c_file(mac10_noise_mon_path,rst,sda,scl)
        send_i2c_file_2pi(rst,sda,scl)
        chp_mac10_noise = chp_adc.read_amon()
        print ("AMON:%fmV"%(chp_mac10_noise['r']))
        return chp_mac10_noise

def mon_mac11_noise():
        rst_amon()
        rst = []
        sda = []
        scl = []
        read_i2c_file(mac11_noise_mon_path,rst,sda,scl)
        send_i2c_file_2pi(rst,sda,scl)
        chp_mac11_noise = chp_adc.read_amon()
        print ("AMON:%fmV"%(chp_mac11_noise['r']))
        return chp_mac11_noise

def mon_mac12_noise():
        rst_amon()
        rst = []
        sda = []
        scl = []
        read_i2c_file(mac12_noise_mon_path,rst,sda,scl)
        send_i2c_file_2pi(rst,sda,scl)
        chp_mac12_noise = chp_adc.read_amon()
        print ("AMON:%fmV"%(chp_mac12_noise['r']))
        return chp_mac12_noise

def mon_mac13_noise():
        rst_amon()
        rst = []
        sda = []
        scl = []
        read_i2c_file(mac13_noise_mon_path,rst,sda,scl)
        send_i2c_file_2pi(rst,sda,scl)
        chp_mac13_noise = chp_adc.read_amon()
        print ("AMON:%fmV"%(chp_mac13_noise['r']))
        return chp_mac13_noise

def mon_mac14_noise():
        rst_amon()
        rst = []
        sda = []
        scl = []
        read_i2c_file(mac14_noise_mon_path,rst,sda,scl)
        send_i2c_file_2pi(rst,sda,scl)
        chp_mac14_noise = chp_adc.read_amon()
        print ("AMON:%fmV"%(chp_mac14_noise['r']))
        return chp_mac14_noise

def mon_mac15_noise():
        rst_amon()
        rst = []
        sda = []
        scl = []
        read_i2c_file(mac15_noise_mon_path,rst,sda,scl)
        send_i2c_file_2pi(rst,sda,scl)
        chp_mac15_noise = chp_adc.read_amon()
        print ("AMON:%fmV"%(chp_mac15_noise['r']))
        return chp_mac15_noise

def mon_mac16_noise():
        rst_amon()
        rst = []
        sda = []
        scl = []
        read_i2c_file(mac16_noise_mon_path,rst,sda,scl)
        send_i2c_file_2pi(rst,sda,scl)
        chp_mac16_noise = chp_adc.read_amon()
        print ("AMON:%fmV"%(chp_mac16_noise['r']))
        return chp_mac16_noise


# you will call these at the beginning of '__main__' and after each i2c to record them in the csv results
# # remember that i2c 'rst' must be disabled for these scripts
#######################################################################################################################################


# The pi showed a delay of changing sda before scl by 20us on the  scope even though they were set to change together
# therefore we should consider these delays and  set sda gpio toggling in a way so it is there before clock transitions.

lv_en = 19

rst_pin = 5
sda_pin = 0
scl_pin = 11
dmon_lcas = 6


rst = []
sda = []
scl = []

##################### chip/pcb - Initial Config ###############################################################
def chp_pcb_config():
    GPIO.setmode(GPIO.BCM)

    # Enable the LV Shifter
    GPIO.setup(lv_en, GPIO.OUT)
    GPIO.output(lv_en,GPIO.HIGH)

    # Enable DMON as Input
    GPIO.setup(dmon_lcas, GPIO.IN, pull_up_down=GPIO.PUD_OFF)

#     pi.set_mode(rst_pin, pigpio.OUTPUT)
#     pi.set_mode(sda_pin, pigpio.OUTPUT)
#     pi.set_mode(scl_pin, pigpio.OUTPUT)

#     pi.write(rst_pin, 0)
#     pi.write(sda_pin,0)
#     pi.write(scl_pin,0)



    GPIO.setup(rst_pin, GPIO.OUT)
    GPIO.setup(sda_pin, GPIO.OUT)
    GPIO.setup(scl_pin, GPIO.OUT)
    GPIO.output(rst_pin, GPIO.LOW)
    GPIO.output(sda_pin, GPIO.LOW)
    GPIO.output(scl_pin, GPIO.LOW)

##################### chip/pcb - Initial Config ###############################################################


##################### ADC - AMON ##############################################################################
adc_addr = 0x48

class adc():
    def __init__(self):
        self.adc = None

    def breadboard_init(self):
        #GPIO.setmode(GPIO.BCM)
        self.adc = ADS1115()


    def read_amon(self):
        self.adc.set_addr_ADS1115(adc_addr)
        self.adc.set_gain(0x06)
        self.adc.set_channel(3)
        read_amon = self.adc.read_voltage(3)
        return read_amon
##################### ADC - AMON ###############################################################################

##################### PMIC - Power Monitoring ##################################################################
class power():
    def __init__(self):
        self.pmic = None

    def breadboard_init(self):
        print('Initiating breadboard')
        #GPIO.setmode(GPIO.BCM)
        self.pmic = INA233()
    
    def vbus(self):
        if self.pmic:
            vb = self.pmic.read_vbus()
            #print(f"Here is the Voltage on VBus: {vb}")
            return vb
        else:
            print('LCAS PMIC Component is Not Setup')
    
    def vshunt(self):
        if self.pmic:
            vsh = self.pmic.read_vshunt()
            #print(f"Here is the Voltage on VShunt: {vsh}")
            return vsh
        else:
            print('LCAS PMIC Component is Not Setup')
    
    def iin(self):
        if self.pmic:
            i_in = self.pmic.read_iin()
            #print(f"Here is the Input Current: {i_in}")
            return i_in
        else:
            print('LCAS PMIC Component is Not Setup')

    
    def pwr(self):
        if self.pmic:
            pwr = self.pmic.read_pwr()
            #print(f"Here is the Power: {pwr}")
            return pwr
        else:
            print('LCAS PMIC Component is Not Setup')
##################### PMIC - Power Monitoring ##################################################################



##################### DMON - Read ##############################################################################
def DMON_read():
    if GPIO.input(dmon_lcas) == GPIO.LOW:
        #print("DMON is 0")
        state = 0
    else:
        #print("DMON is 1")
        state = 1
    return state
##################### DMON - Read ###############################################################################




##################### Save Func - csv ###########################################################################
def save_result(path,file_name,head_iteration,i2c_call_num,head_res1,result1,head_res2,result2,head_res3,result3,head_res4,result4,head_res5,result5,head_res6,result6,head_res7,result7,head_res8,result8,head_res9,result9,head_res10,result10,head_res11,result11,head_res12,result12,head_res13,result13):               # for additional result columns, you can add result2,result3, ... to the end
#def save_result(path,file_name,head_iteration,i2c_call_num,head_res1,result1,head_res2,result2):    
    cur_dir = os.getcwd()
    results_dir = os.path.join(cur_dir,path)
    results_dir = os.path.join(results_dir,file_name)
    os.makedirs(os.path.dirname(results_dir),exist_ok=True)
    file_exists = os.path.isfile(results_dir)

    with open(results_dir, mode='a', newline='') as csvfile:
        writer = csv.writer(csvfile)      
        if not file_exists:
            data_header = [head_iteration,head_res1,head_res2,head_res3,head_res4,head_res5,head_res6,head_res7,head_res8,head_res9,head_res10,head_res11,head_res12,head_res13]
#            data_header = [head_iteration,head_res1,head_res2]
            writer.writerow(data_header)
        data =  ([i2c_call_num]) + ([result1]) + ([result2]) + ([result3])+ ([result4])+ ([result5])+ ([result6])+ ([result7])+ ([result8])+ ([result9])+ ([result10])+ ([result11])+ ([result12])+ ([result13])                        # for additional result columns, you can add result2,result3, ... to the end
#        data =  ([i2c_call_num]) + ([result1]) + ([result2])
        writer.writerow(data)
##################### Save Func - csv ############################################################################

##################### I2C Data Read Func #########################################################################

def read_i2c_file(lcas_i2c_file_path,rst,sda,scl):
    with open(lcas_i2c_file_path, 'r') as file:
        raw_data = file.readlines()
        
    for each_line in raw_data:
        binary_data = each_line.strip().split()
        rst.append(int(binary_data[1]))
        sda.append(int(binary_data[2]))
        scl.append(int(binary_data[3]))
##################### I2C Data Read Func #########################################################################


##################### I2C Data Send Func #########################################################################
# def send_i2c_file_2pi(rst,sda,scl):
#     for rst_iteration, sda_iteration, scl_iteration in zip(rst,sda,scl):
        
#         if rst_iteration == 0:
#             rst_pin_value = GPIO.LOW
#         elif rst_iteration == 1:
#             rst_pin_value = GPIO.HIGH

#         if sda_iteration == 0:
#             sda_pin_value = GPIO.LOW
#         elif sda_iteration == 1:
#             sda_pin_value = GPIO.HIGH
        
#         if scl_iteration == 0:
#             scl_pin_value = GPIO.LOW
#         elif scl_iteration == 1:
#             scl_pin_value = GPIO.HIGH

#         GPIO.output(rst_pin,rst_pin_value)
#         GPIO.output(sda_pin,sda_pin_value)
#         GPIO.output(scl_pin,scl_pin_value)
#         time.sleep(2*quarter_period)
def send_i2c_file_2pi(rst,sda,scl):
    # start_time = time.perf_counter_ns()
    for rst_iteration, sda_iteration, scl_iteration in zip(rst,sda,scl):
        # current_time = time.perf_counter_ns()
        # if current_time - start_time >= (2*quarter_period):
        if rst_iteration == 0:
                rst_pin_value = GPIO.LOW
        elif rst_iteration == 1:
                rst_pin_value = GPIO.HIGH

        if sda_iteration == 0:
                sda_pin_value = GPIO.LOW
        elif sda_iteration == 1:
                sda_pin_value = GPIO.HIGH
        
        if scl_iteration == 0:
                scl_pin_value = GPIO.LOW
        elif scl_iteration == 1:
                scl_pin_value = GPIO.HIGH

        GPIO.output(rst_pin,rst_pin_value)
        GPIO.output(sda_pin,sda_pin_value)
        GPIO.output(scl_pin,scl_pin_value)
                # pi.write(rst_pin,rst_pin_value)
                # pi.write(sda_pin,sda_pin_value)
                # pi.write(scl_pin,scl_pin_value)

                # start_time = current_time
##################### I2C Data Send Func ###################################################################################




if __name__ == "__main__":

    print("PCB Initializing")
    chp_pcb_config()                # configuring all the GPIOs
    time.sleep(0.25)
    chp_pwr = power()               
    chp_pwr.breadboard_init()       # configure PMIC/PCB
    chp_adc = adc()
    chp_adc.breadboard_init()       # configure ADC/PCB

    print("Sending I2C All Reset Data")
    time.sleep(0.25)
    rst_all()
    time.sleep(0.25)
    chp_vdd = mon_vdd()
    time.sleep(0.25)
    chp_vss = mon_vss()
    rst_amon()

    try:

        for i in range (starting_mac,(starting_mac+num_of_macs)):
            main_dir = os.getcwd()
            i2c_path = os.getcwd()
            i2c_path = os.path.join(i2c_path,'i2c_files')
            i2c_path = os.path.join(i2c_path,'noise_mthd1')        #specify what kind of test you are running
            i2c_path = os.path.join(i2c_path,str(i))

            dir1 = os.path.join(i2c_path,'MacL_UpL')               # offset test name
            dir2 = os.path.join(i2c_path,'MacL_UpR')               # offset test name
            dir3 = os.path.join(i2c_path,'MacR_UpL')               # offset test name
            dir4 = os.path.join(i2c_path,'MacR_UpR')               # offset test name
            dir5 = os.path.join(i2c_path,'MacL_Down')               # offset test name
            dir6 = os.path.join(i2c_path,'MacR_Down')               # offset test name                         
        #     directories = [dir1,dir2,dir3,dir4,dir5,dir6]                       # making a list of those names
            directories = [dir1]
            for z, directory in enumerate(directories):
                #for n in range(1,num_files+1):     # this is important 0 or 1 to start from
                #for n in range(0,num_files):        # if your file start from 0 then range should be (0,num_files)
                for n in range(0,num_of_files_each_test):        ############for testing########
                    rst = []                        
                    sda = []
                    scl = []
                    fname = f"{n}"                  # for n=0 you want rst=1 in the 'cmds' file because you dont want previous tests to affect the current one
                                                    # for n>0 thne you set rst=0 to shorten the i2c and keep previous 'cmds' settings unchanged
                    path = os.path.join(directory,fname)
                    read_i2c_file(path,rst,sda,scl)
                    send_i2c_file_2pi(rst,sda,scl)
                    print("..........Data Was Sent.........")       
                    
                    time.sleep(wait_time)
                    avg_noise = chp_adc.read_amon()
                    D_state = DMON_read()
                    print(D_state)

                    

                    # initial_DMON = D_state
                    mon_dac5_macL_actP()
                    actp_l  = chp_adc.read_amon()
                    mon_dac4_macL_actN()
                    actn_l  = chp_adc.read_amon()
                    mon_dac7_macL_wghtP()
                    wghtp_l  = chp_adc.read_amon()
                    mon_dac6_macL_wghtN() 
                    wghtn_l  = chp_adc.read_amon()                        #######this was for MAC_test
                    mon_dac1_macR_actP()
                    actp_r  = chp_adc.read_amon()
                    mon_dac0_macR_actN()
                    actn_r  = chp_adc.read_amon()
                    mon_dac3_macR_wghtP()
                    wghtp_r  = chp_adc.read_amon()
                    mon_dac2_macR_wghtN() 
                    wghtn_r  = chp_adc.read_amon() 
                    print("avg noise:%fmV"%(avg_noise['r']))
                    i_chip = chp_pwr.iin()            # current consumption     
                    save_result(directories[z],'results.csv','iteration',n,'MAC_ACT_POS_L',actp_l['r'],'MAC_ACT_NEG_L',actn_l['r'],'MAC_WGHT_POS_L',wghtp_l['r'],'MAC_WGHT_NEG_L',wghtn_l['r'],'MAC_ACT_POS_R',actp_r['r'],'MAC_ACT_NEG_R',actn_r['r'],'MAC_WGHT_POS_R',wghtp_r['r'],'MAC_WGHT_NEG_R',wghtn_r['r'],'chp_current(A)',i_chip,'chp_supply(mV)',chp_vdd['r'],'chp_vss(mV)',chp_vss['r'],'AVG_Noise',avg_noise['r'],'DMON',D_state)
                    rst_amon()
                    time.sleep(filter_rc)
                    print('...................................................')



    except KeyboardInterrupt:
        print("Exiting")
