################# library #######################

import RPi.GPIO as GPIO                 #import gpio library
from mfrc522 import SimpleMFRC522       #import rfid mfrc522
 
import serial                           #for communication to usb to serial for gsm
import time, sys
import datetime

##################### Wiring and COnnection##################

#SERIAL_PORT = "/dev/ttyAMA0"  # Raspberry Pi 2
SERIAL_PORT = "/dev/ttyUSB0"    # Raspberry Pi 3
ser = serial.Serial(SERIAL_PORT, baudrate = 9600, timeout = 5)


GPIO.setwarnings(False)

channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)
 
################ Call Back################

def callback(channel):
        if GPIO.input(channel):
                print ("alcohol Detected at driver cabin")
                ser = serial.Serial(SERIAL_PORT, baudrate = 9600, timeout = 5)
                ser.write(b"AT+CMGF=1\r") # set to text mode
                time.sleep(3)
                ser.write(b'AT+CMGS="+918308501188"\r')
                time.sleep(3)
                msg = 'alcohol Detected at driver cabin'
                msg= msg + chr(26)
                #print ("Sending SMS with status info:" + msg)
                #ser.write(msg.encode('ascii') + '\r\n')
                ser.write(msg.encode('ascii'))
                #ser.write(b"hii")
                time.sleep(3)
        else:
                print ("alcohol Detected at driver cabin")
 
GPIO.add_event_detect(channel, GPIO.RISING, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change
 
 

def msgsend():
     
    ser = serial.Serial(SERIAL_PORT, baudrate = 9600, timeout = 5)
    ser.write(b"AT+CMGF=1\r") # set to text mode
    time.sleep(3)
    ser.write(b'AT+CMGS="+918390380973"\r')
    time.sleep(3)
    msg = 'GSM Working'
    msg= msg + chr(26)
    #print ("Sending SMS with status info:" + msg)
    #ser.write(msg.encode('ascii') + '\r\n')
    ser.write(msg.encode('ascii'))
    #ser.write(b"hii")
    time.sleep(3)

        
reader = SimpleMFRC522()   #rfid reader

def rfid():
    id, text = reader.read()
    #print(id)
    return id
    #print(text)
while True:
    val=rfid()
    print(val)
    if(val==284003114022):
        print('Your kid Abhishek is arrive in bus')
        ser = serial.Serial(SERIAL_PORT, baudrate = 9600, timeout = 5)
        ser.write(b"AT+CMGF=1\r") # set to text mode
        time.sleep(3)
        ser.write(b'AT+CMGS="+917028237008"\r')
        time.sleep(3)
        msg = 'Your kid Abhishek is arrive in bus'
        msg= msg + chr(26)
        #print ("Sending SMS with status info:" + msg)
        #ser.write(msg.encode('ascii') + '\r\n')
        ser.write(msg.encode('ascii'))
        #ser.write(b"hii")
        time.sleep(3)
        
    if(val==628726143892):
        print('Your kid Karan is arrive in bus')
        ser = serial.Serial(SERIAL_PORT, baudrate = 9600, timeout = 5)
        ser.write(b"AT+CMGF=1\r") # set to text mode
        time.sleep(3)
        ser.write(b'AT+CMGS="+918390380973"\r')
        time.sleep(3)
        msg = 'Your kid Karan is arrive in bus'
        msg= msg + chr(26)
        #print ("Sending SMS with status info:" + msg)
        #ser.write(msg.encode('ascii') + '\r\n')
        ser.write(msg.encode('ascii'))
        #ser.write(b"hii")
        time.sleep(3)
        
    if(val==180172135518):
        print('Your kid  Prachi is arrive in bus')
        ser = serial.Serial(SERIAL_PORT, baudrate = 9600, timeout = 5)
        ser.write(b"AT+CMGF=1\r") # set to text mode
        time.sleep(3)
        ser.write(b'AT+CMGS="+918956168860"\r')
        time.sleep(3)
        msg = 'Your kid  Prachi is arrive in bus'
        msg= msg + chr(26)
        #print ("Sending SMS with status info:" + msg)
        #ser.write(msg.encode('ascii') + '\r\n')
        ser.write(msg.encode('ascii'))
        #ser.write(b"hii")
        time.sleep(3)
     
          
    
            
            
    
            

        
       
