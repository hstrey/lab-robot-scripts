import ArduinoConnect
import os
import time

intialPort = 0
testPhrase = 'i'
homePhrase='$H'
pushupPhrase='O'

filelist=os.listdir('/dev')
ttylist=[file for file in filelist if file.startswith('tty.usb')]

print(ttylist)

ttyport='/dev/'+str(ttylist[intialPort])

arduino=ArduinoConnect.duino(ttyport)


arduino.test(testPhrase)

#print(arduino.writeRead('i'))

#print(arduino.writeRead('O'))