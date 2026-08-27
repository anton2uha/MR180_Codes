import RPi.GPIO as GPIO
import smbus
import time



# PMIC Address
INA233_addr = 0x40

# PMIC Register Address
read_vbus_adr = 0x88
read_vshunt_adr = 0xD1
read_iin_adr = 0x89
read_pwr_adr = 0x97

# PMIC Calibrator Address
MFR_adc_adr = 0xD0
MFR_calib_adr = 0xD4

# Setting the Current LSB and calculating the MFR Calib message
chip_max_current = 2.097e-3
chip_max_current_assumption = 2.1845e-3 
curr_lsb = 6.66e-8
R_shunt = 20
#MFR_calib_msg = 3940
MFR_calib_msg = 0x0F00  # calculated with rshunt = 20ohms


# MFR ADC messages      Bits: 15=0, 14=1, 13=0, 12=0 Reserved
    # Averaging bits config Bits: [11,10,9] = [AVG2,AVG1,AVG0]
#MFR_adc_calib_avg = 0b000           # of AVG = 1 (Default)
#MFR_adc_calib_avg = 0b001           # of AVG = 4
#MFR_adc_calib_avg = 0b010           # of AVG = 16
MFR_adc_calib_avg = 0b011           # of AVG = 64
#MFR_adc_calib_avg = 0b100           # of AVG = 128
#MFR_adc_calib_avg = 0b101           # of AVG = 256
#MFR_adc_calib_avg = 0b110           # of AVG = 512
#MFR_adc_calib_avg = 0b111           # of AVG = 1024

    # VBUS Conversion Time Bits: [8,7,6]
#MFR_adc_calib_vbus_time = 0b000     # 140us
#MFR_adc_calib_vbus_time = 0b001     # 204us
#MFR_adc_calib_vbus_time = 0b010     # 332us
#MFR_adc_calib_vbus_time = 0b011     # 588us
#MFR_adc_calib_vbus_time = 0b100     # 1.1ms (Default)
#MFR_adc_calib_vbus_time = 0b101     # 2.116ms
#MFR_adc_calib_vbus_time = 0b110     # 4.156ms
MFR_adc_calib_vbus_time = 0b111     # 8.244ms

    # VShunt Conversion Time Bits: [5,4,3]
#MFR_adc_calib_vshunt_time = 0b000     # 140us
#MFR_adc_calib_vshunt_time = 0b001     # 204us
#MFR_adc_calib_vshunt_time = 0b010     # 332us
#MFR_adc_calib_vshunt_time = 0b011     # 588us
#MFR_adc_calib_vshunt_time = 0b100     # 1.1ms (Default)
#MFR_adc_calib_vshunt_time = 0b101     # 2.116ms
#MFR_adc_calib_vshunt_time = 0b110     # 4.156ms
MFR_adc_calib_vshunt_time = 0b111     # 8.244ms

    # Operating Mode Bits: [2,1,0]
#MFR_adc_calib_vshunt_time = 0b000     # shutdown
#MFR_adc_calib_vshunt_time = 0b001     # shunt voltage triggered
#MFR_adc_calib_vshunt_time = 0b010     # bus voltage triggered
#MFR_adc_calib_vshunt_time = 0b011     # shunt and bus triggered
#MFR_adc_calib_vshunt_time = 0b100     # shutdown
#MFR_adc_calib_vshunt_time = 0b101     # shunt voltage continuous
#MFR_adc_calib_vshunt_time = 0b110     # bus voltage continuous
MFR_adc_calib_vshunt_time = 0b111     # shunt and bus continuous (Default)

#MFR_ADC_calib_msg for avg 64 and 8.244ms convert time on both = 0b0100011111111111
####MFR_ADC_calib_msg = 0x47FF
#### And this is for the default
MFR_ADC_calib_msg = 0x47FF

# Converseion Variable Values
    # Constants
m_vbus = 8
b_vbus = 0
R_vbus = 2

m_vshunt = 4
b_vshunt = 0
R_vshunt = 5
    # Calculated
m_iin = 15000
b_iin = 0
R_iin = 3

m_pwr = 600
b_pwr = 0
R_pwr = 3



class INA233:
    def __init__(self):
        
        self.pmic_address = INA233_addr
        self.i2c_channel = 1
        self.i2c_bus = smbus.SMBus(self.i2c_channel)
        #configuration of MFR registers
        print('Setting Calibration Registers for INA233')
        self.i2c_bus.write_word_data(self.pmic_address,MFR_adc_adr,MFR_ADC_calib_msg)
        time.sleep(1)
        self.i2c_bus.write_word_data(self.pmic_address,MFR_calib_adr,MFR_calib_msg)
        time.sleep(1)

    def read_vbus(self):
        print('reading the vbus value')
        # Digital Value
        vbus_raw = self.i2c_bus.read_word_data(INA233_addr,read_vbus_adr)
        # Real World Value
        return (1/m_vbus)*(vbus_raw*(10**(-R_vbus)) - b_vbus)

    def read_vshunt(self):
        print('Reading Input Shunt Resistor Voltage')
        # Digital Value
        vshunt_raw = self.i2c_bus.read_word_data(INA233_addr,read_vshunt_adr)
        # real World Value
        return (1/m_vshunt)*(vshunt_raw*(10**(-R_vshunt)) - b_vshunt)

    def read_iin(self):
        print('Reading Input Current')
        # Digital Value
        iin_raw = self.i2c_bus.read_word_data(INA233_addr,read_iin_adr)
        # real World Value
        return (1/m_iin)*(iin_raw*(10**(-R_iin)) - b_iin)
    
    def read_pwr(self):
        print('Reading Power Consumption - vbus*iin')
        # Digital Value
        pwr_raw = self.i2c_bus.read_word_data(INA233_addr,read_pwr_adr)
        # real World Value
        return (1/m_pwr)*(pwr_raw*(10**(-R_pwr)) - b_pwr)