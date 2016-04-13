import os
import time
import serial
#import utilities.py as util

class duino:
    
    def __init__(self, portNum):
        self.portNum = portNum
        self.arduino = serial.Serial(portNum, 115200, timeout=1)
        time.sleep(7)
            
    def test(self, testPhrase):
        self.writeRead(testPhrase)
        self.arduino.close()
    
    def writeRead(self, word):
        #print(word)
        word = bytes(word, 'utf8')
        self.arduino.write(word)
        time.sleep(0.1)
        buffer_string=''
        #print(self.arduino.inWaiting())
        while self.arduino.inWaiting() > 0:
            buffer_string=buffer_string+str(self.arduino.read(self.arduino.inWaiting()))
        self.arduino.flushInput()
        return buffer_string

    def checkMotor(self):
        motorRunning = True
        while motorRunning:
            state = self.writeRead('?\r\n')
            #print(state)
            if 'Run' in state:
                motorRunning = True
            elif 'Idle' in state:
                motorRunning = False
            #print('Motor is ' + str(motorRunning))
        
    def goToWell(self,i,j):
        well_alt=[]
        #if len(well1 > 3):
         #   print("Incorrect well entered.")
        #util.translateWell(well1)
        
        for x in range(12):
            well_alt.append([])
            for y in range(8):
                well='x'+str(-x*9)+'y'+str(-y*9)+'\r\n'
                well_alt[x].append(well)
            # create matrix with absolute coordinates
        self.checkMotor()
        self.writeRead(well_alt[i][j])
    
    def goToWellArray(self, rangex, rangey,timedelay, solenoidObj):
        for i in rangex:
            for j in rangey:
                self.goToWell(i,j)
                solenoidObj.pushUp(self)
                time.sleep(int(timedelay))
                solenoidObj.pushDown(self)
                
    def pushUp(self, motorObject):
        motorObject.checkMotor()
        self.writeRead('O')
        motorObject.checkMotor()
        
    def pushDown(self,motorObject):
        motorObject.checkMotor()
        self.writeRead('V')
        motorObject.checkMotor()
    
    def closePort(self):
        self.arduino.close()
        