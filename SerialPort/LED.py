import serial, mosquitto, random

#CONNECT TO THE CORRECT PORT
port = serial.Serial("/dev/tty.usbmodem1451",9600,timeout=2)

def messageReceived(broker, obj, msg):
        print("Message " + msg.topic + " containing: " + msg.payload)
        if (msg.payload == 'LIGHT ON') :
            port.write("1")
        
        elif (msg.payload == 'LIGHT OFF') :
            port.write("0")


#CREATING CLIENT
client = mosquitto.Mosquitto("Amirul")

#CONNECTING TO BROKER
client.connect("127.0.0.1")

client.subscribe("lights")
client.on_message = messageReceived

while (client != None): client.loop()

while True:
    command = raw_input("insert command: ")
    if (command == '1') :
        port.write("1")
    
    elif (command == '0') :
        port.write("0")
