import RPi.GPIO as GPIO


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




GPIO.setmode(GPIO.BCM)



# Enabling Supply Parallel Resistors to reduce LCAS Supply to 0.407 @ Startup
GPIO.setup(ctl_sw1, GPIO.OUT)
GPIO.setup(ctl_sw2, GPIO.OUT)
GPIO.setup(ctl_sw3, GPIO.OUT)
GPIO.setup(ctl_sw4, GPIO.OUT)

GPIO.output(ctl_sw1, GPIO.HIGH)
GPIO.output(ctl_sw2, GPIO.HIGH)
GPIO.output(ctl_sw3, GPIO.HIGH)
GPIO.output(ctl_sw4, GPIO.HIGH)


# Setup Dig POT to be configured as Down Counter in case
GPIO.setup(pot_cs, GPIO.OUT)
GPIO.setup(pot_ud, GPIO.OUT)

GPIO.output(pot_cs, GPIO.HIGH)
GPIO.output(pot_ud, GPIO.LOW)

# Setup Chip Control Pins to 0
GPIO.setup(sda_lcas, GPIO.OUT)
GPIO.setup(scl_lcas, GPIO.OUT)
GPIO.setup(dmon_lcas, GPIO.IN)
GPIO.setup(rst_lcas, GPIO.OUT)
GPIO.setup(rst_cmos, GPIO.OUT)

GPIO.output(sda_lcas, GPIO.LOW)
GPIO.output(scl_lcas, GPIO.LOW)

GPIO.output(rst_lcas, GPIO.LOW)
GPIO.output(rst_cmos, GPIO.LOW)


GPIO.setup(lv_en,GPIO.OUT)
GPIO.output(lv_en,GPIO.LOW)
# Enable LvShifter after setting up the GPIOs
# # This should be disabled since 1V8 is not enabled and LvSh required both VCCA/VCCB to be settled before its enabled



