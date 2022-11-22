# import pyfirmata as pf

# import time


# ard = pf.Arduino('/dev/cu.usbserial-2430')

# ard.get_pin('d:8:o') #디지털핀 13번을 출력으로 설정

# while True:

#     ard.digital[8].write(1)

#     time.sleep(2)

#     ard.digital[8].write(0)

#     time.sleep(2)

import pyfirmata as pf
import time

## digital pin control

ard = pf.Arduino('/dev/cu.usbserial-2330') # Different in Mac OS dev/...
a = ard.get_pin('d:8:o') # digital pin 13 output # get pin status 

while True :
    ard.digital[8].write(1)
    time.sleep(0.5)
    ard.digital[8].write(0)
    time.sleep(0.5)

    
# ## or
# ard = pf.Arduino('COM7')
# p13 = ard.get_pin('d:13:o') 
# while True :
#     p13.write(1)
#     time.sleep(0.5)
#     print('p13 status is 1')
#     p13.write(0)
#     time.sleep(0.5)
#     print('p13 status is 0')