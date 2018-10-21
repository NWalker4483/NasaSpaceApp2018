from threading import Thread
import time 
import socket 
import random

class SensorNodeCluster:
    def __init__(self,RADES):
        self.__RADES = RADES

class SensorNodeHandler(Thread):
    def __init__(self, UDP_IP = "192.168.43.14", UDP_PORT = 5000, latitude = 0, longitude = 0, debug = False):
        Thread.__init__(self)
        self.daemon = True
        self.ip = UDP_IP
        self.port = UDP_PORT
        self.latitude = latitude
        self.longitude = longitude
        self.debug = debug
        self.data = {"rads":0}
        if self.debug == False:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.sock.bind((UDP_IP, UDP_PORT))
        self.start()
    def get_sensors(self):
        while True:
            data, _ = self.sock.recvfrom(1024)	
            line = data.strip().decode('ascii').split(',')
            line = [float(i) for i in line]
            if len(line) == 3:
                print(line)
                self.data['rads'] = int(line[0]//100)
            else:
                print("received incomplete UCP packet from android IMU")
    def test_sensors(self):
        while True:
            time.sleep(.75)
            self.data['rads'] = random.randint(0,20)
    def run(self):
        if self.debug == True:
            return self.test_sensors()
        elif self.debug == False:
            return self.get_sensors()

if __name__ == "__main__":
    Test = SensorNodeHandler("192.168.43.14",5000)
    Test.start()

    