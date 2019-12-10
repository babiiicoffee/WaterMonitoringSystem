
import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt

# raspberry pin connection
# S - GPIO17
# middle - 3v or 5v
# negative(-) - GND

LedPin = 11    # pin11
def setup():
    GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
    GPIO.setup(LedPin, GPIO.OUT)   # Set LedPin's mode is output
    GPIO.output(LedPin, GPIO.HIGH) # Set LedPin high(+3.3V) to off led

# This is the Subscriber

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("Turn/#")

def on_message(client, userdata, msg):
    if msg.payload == 'Turn off the motor of tank 1': # this will make the laser off for the tank 2
        print("Tank 1 Motor is off")
        client.publish("Moisture/Off","Moisture sensor is off for tank 1")
        GPIO.output(LedPin, GPIO.LOW)
    elif msg.payload == 'Turn on the motor of tank 1': # this will make the laser on for the tank 2
        print("Tank 1 Motor is on") 
        client.publish("Moisture/On","Moisture sensor is on for tank 1")
        GPIO.output(LedPin, GPIO.HIGH)

client = mqtt.Client()
client.connect("test.mosquitto.org", 1883, 60)

client.on_connect = on_connect
client.on_message = on_message
setup()

client.loop_forever()
