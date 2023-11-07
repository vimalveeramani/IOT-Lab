import RPi.GPIO as GPIO

import BlynkLib 

import time

GPIO.setwarnings(False) 

GPIO.setmode(GPIO.BOARD) 

GPIO.setup(11, GPIO.IN) 

GPIO.setup(3, GPIO.OUT)

GPIO.setup(5, GPIO.OUT)

token = "<Paste the Auth Token here>"

blynk = BlynkLib.Blynk(token,server="blynk.cloud")

@blynk.VIRTUAL_WRITE(0)
def Power_supply(value):

while (int(value[0]) == 1):

GPIO.output(5,1) # Turn On Power LED 

blynk.virtual_write(2,1)

i=GPIO.input(11)

if i==0:

# When output from motion sensor is LOW

print("No Motion")

blynk.virtual_write(1,"No Motion")

GPIO.output(3, 0) # when motion is not detected ,Turn OFF LED

blynk.virtual_write(3,0)

time.sleep(0.1)

elif i==1: # When output from motion sensor is HIGH 

print("Motion detected")

blynk.virtual_write(1,"Motion Detected")

GPIO.output(3, 1) # when motion is detected , Turn ON LED 

blynk.virtual_write(3,1)

time.sleep(0.1)

blynk.sync_virtual(0)

break

if(int(value[0]) == 0):

GPIO.output(5,0) 

blynk.virtual_write(2,0)

while True:

blynk.run()
