#from utilities import *
import ArduinoConnect
import os
import time

#intial variables
intialPort = 0
testPhrase = 'i'
homePhrase='$H'+'\r\n'
pushupPhrase='O'
pushDown='V'


filelist=os.listdir('/dev')
ttylist=[file for file in filelist if file.startswith('tty.usb')]

print(ttylist)

ttyport='/dev/'+str(ttylist[intialPort])
ttyport2='/dev/'+str(ttylist[intialPort+1])

testDuino = ArduinoConnect.duino(ttyport)

if 'init' in testDuino.writeRead(testPhrase):
    solContrl = ArduinoConnect.duino(ttyport)
    motContrl = ArduinoConnect.duino(ttyport2)
    print('sol is 0 mot is 1')
    
else:
    solContrl = ArduinoConnect.duino(ttyport2)
    motContrl = ArduinoConnect.duino(ttyport)
    print('sol is 1 mot is 0')

motContrl.writeRead(homePhrase)
solContrl.writeRead('i')
motContrl.goToWell(1,1)
solContrl.pushUp(motContrl)
motContrl.goToWell(7,7)
solContrl.pushDown(motContrl)
motContrl.goToWell(5,5)
solContrl.pushUp(motContrl)
motContrl.goToWellArray(range(1,5),range(1,5),1,solContrl)


motContrl.closePort()
solContrl.closePort()