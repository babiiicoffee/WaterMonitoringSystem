import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt
print("asdas")
client = mqtt.Client() # instance of client
client.connect("test.mosquitto.org", 1883, 60); # client connect to the broker

channel = 21 # this is pin from the raspberry pi
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("Moisture/#")

water_empty = True

def on_message(client, userdata, msg):
    # while water_empty:
    #   if msg.payload == 'Moisture sensor is on for tank 1':
    #       print("Sensor is on")
    #       if GPIO.input(channel):
                # print("The tank is full you need you turn off the motor")
                # client.publish("SaveWater/C2Tank1","Water Detected tank 1")
    #       else:
    #           print("The tank is not yet full")
    #               client.publish("SaveWater/C2Tank1","No Water Detected tank 1")
    #   elif msg.payload == 'Moisture sensor is off for tank 1':
    #       print("Sensor is off")
    #   break
    if msg.payload == "Moisture sensor is on for tank 1":
        while True:
        	while True:
	            if GPIO.input(channel):
	            	client.publish("SaveWater/C2Tank1","No Water Detected tank 1")
	                print("The tank is not yet full")
	                time.sleep(1)
	            else:
	            	client.publish("SaveWater/C2Tank1","Water Detected tank 1")
	                print("The tank is full you need you turn off the motor")
	                time.sleep(1)
	                break
	        break

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()
GPIO.cleanup()
#
#GPIO.add_event_callback(channel, callback)
#while True:


# AO or A - is no wire inserted
# DO or B - wire is connected to GPIO21
# GND or C - wire is connected to GND
# VCC or D - is connected to 3v3