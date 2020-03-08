 
        
import RPi.GPIO as GPIO
import serial
import time, sys
import datetime

#SERIAL_PORT = "/dev/ttyAMA0"  # Raspberry Pi 2
SERIAL_PORT = "/dev/ttyUSB0"    # Raspberry Pi 3
ser = serial.Serial(SERIAL_PORT, baudrate = 9600, timeout = 5)


while True:
     
    
    ser.write(b"AT+CGPSPWR=1\r\n") # set gps on /enable
    time.sleep(3)
    ser.write(b"AT+CGPSINF=32\r\n") # set to recive location
    msg=ser.readline()
    smsg = str(msg, encoding = 'utf-8')
    smsg=smsg.split(",")
    print(smsg)
    
    #msg=msg.encode()
    x = len(smsg)
    if x>8:
        
        print("latitude")
        print(smsg[5] )
        print("logitude")
        print(smsg[7])
    
    
    time.sleep(3)
         
         
       
 
