import listports
import serial
import time

devices_available = listports.serial_ports()
count = len(devices_available)
ser = serial.Serial()
device_list = []
device_id = []

def device_info():
        if count != 0:
                for i in range(0,count):
                        ser.port = str(devices_available[i])
                        ser.baudrate = 115200
                        ser.open()
                        time.sleep(2)
                        device_name = str(ser.read_all())
                        ser.close()
                        device_list.append([device_name,devices_available[i]])
                        total_devices = len(device_list)

                for i in range(0,total_devices):
                        if device_list[i][0][10:14] == 'Grbl':
                                device_id.append(('Grbl 0.9j',device_list[i][1]))
                        elif device_list[i][0][2:6] == 'Pneu':
                                device_id.append(('Pneumatic Controller',device_list[i][1]))
                        elif device_list[i][0][2:6] == 'Pump':
                                device_id.append(('DC Pump Controller',device_list[i][1]))
                        else:
                                device_id.append(('Unkown Device',device_list[i][1]))
        else:
                print("No device found")
                exit()
                
                
        return device_id
	
