import serial
import time

import face_train_use_keras

portx = 'COM1'  # 要打开的串口
bps = 115200    # 串口的波特率
timex = 5       # 超时时间

result = False
# 打开串口
sel = serial.Serial(portx,bps,timeout=timex)
str1 = 'dd 08 24 00 02'     # 开启报警器
str2 = 'dd 08 24 00 03'     # 关闭报警器
str3 = 'dd 08 24 00 09'     # 开门
str4 = 'dd 08 24 00 0A'     # 关门

# 关门
def closeDoor():
    hex_str4 = bytes.fromhex(str4)
    sel.write(hex_str4)
    pass

# 开门
def openDoor():
    hex_str3 = bytes.fromhex(str3)
    sel.write(hex_str3)
    pass

# 开启报警器
def openAlarm():
    hex_str1 = bytes.fromhex(str1)
    sel.write(hex_str1)
    pass

def closeAlarm():
    hex_str2 = bytes.fromhex(str2)
    sel.write(hex_str2)
    pass

def knockDoor(result):
    if (result == True):
        openDoor()
        time.sleep(2)
        closeDoor()
    else:
        openAlarm()
        time.sleep(2)
        closeAlarm()

if __name__ == '__main__':

    knockDoor(result)
