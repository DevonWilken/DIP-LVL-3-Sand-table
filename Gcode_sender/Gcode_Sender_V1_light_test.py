import serial
import time
serialcomm = serial.Serial("COM 4, 9600") #store serial port
serialcomm.timeout = 1

while True:
    i = input("input on /off").strip() 
    if i == "done":
        print("finished programme")
        break
    serialcomm.wirte(i.encode()) #write command to serial port
    time.sleep(0.5)
    print(serialcomm.readline().decode("ascii"))
serialcomm.close()
