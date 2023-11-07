import BlynkLib 

import Adafruit_DHT

token = '<paste the auth token here>'

blynk = BlynkLib.Blynk(token,server="blynk.cloud")

sensor = Adafruit_DHT.DHT11

gpio_pin = 17

while True:

blynk.run()

humidity, temperature = Adafruit_DHT.read_retry(sensor,gpio_pin)

if humidity is not None and temperature is not None:

temperature=float('%.3f'%(temperature)) 

temp_in_f = float('%.3f'%(temperature*1.8)+32) 

temp_in_k = float('%.3f'%(temperature+273.15))

print('Temperature =

{0:0.2f}°C,{0:0.2f}°F,{0:0.2f}°K'.format(temperature,temp_in_f,temp_in_k)') 

print('Humidity =',int(humidity),'%')

print ('upload the data into the connected cloud')

blynk.virtual_write(0,temperature) 

blynk.virtual_write(1,temperature_in_f) 

blynk.virtual_write(2,temperature_in_k) 

blynk.virtual_write(3,int(humidity)) 

print("Data uploaded")

else:

print("Failed to get data in DHT11 Sensor\nRetrying...")
