import serial
port = serial.Serial("COM13",9600,timeout=2)

white True:
    input = raw_input("Please enter number: ")
    if(input == '1'):
        port.write('1')
    else if(input == '0'):
        port.write('1')

        
    
                     
