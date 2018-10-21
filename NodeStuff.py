from threading import Thread
import time 
import socket 
import random
class SensorNodeHandler(Thread):
    def __init__(self, UDP_IP = "192.168.43.14", UDP_PORT = 5000,latitude = 0,longitude = 0):
        Thread.__init__(self)
        self.daemon = True
        self.ip = UDP_IP
        self.port = UDP_PORT
        self.latitude = latitude
        self.longitude = longitude
        self.data = {}
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((UDP_IP, UDP_PORT))

    def run(self):
        while True:
            time.sleep(.75)
            data, _ = self.sock.recvfrom(1024)	
            line = data.strip().decode('ascii').split(',')
            line = [float(i) for i in line]
            if len(line) == 3:
                self.data['rads'] = line[2]*2
            else:
                print("received incomplete UCP packet from android IMU")
if __name__ == "__main__":
    Test = SensorNodeHandler("192.168.43.14",5000)
    Test.start()

    