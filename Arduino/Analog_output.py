import pyfirmata as pf
import time
## analog pin control

ard = pf.Arduino('/dev/cu.usbserial-2330')
print('connected')
# 아날로그 핀 사용위해 아래의 두줄이 필요함.
pf.util.Iterator(ard).start()
ard.analog[0].enable_reporting()

while True :
    a0 = ard.analog[0].read() #[0,1] 범위의 실수 변환
    print(a0)

## or
# pf.util.Iterator(ard).start()
# ard.analog[0].enable_reporing()
# a0p = ard.get_pin('a:0:i') # 아날로그 , 0번핀, 인풋

# while True :
#     a0 = a0p.read()
#     pirnt(a0)