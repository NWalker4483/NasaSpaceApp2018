from threading import Thread
import time 
import socket 

class SensorNodeHandler(Thread):
    def __init__(self,socket, UDP_IP, UDP_PORT, port,latitude = 0,longitude = 0):
        Thread.__init__(self)
        self.ip = UDP_IP
        self.port = UDP_PORT
        self.latitude = latitude
        self.longitude = longitude
        self.socket=socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((UDP_IP, UDP_PORT))

    def run(self):
        while True:
            time.sleep(0.1)
            data = self.sock.recvfrom(1024)	
            line = data.split(',')
            if len(line) == 3:
                #flowstr = str(self.flow[i])
                #flowstr = flowstr.replace("{","")
                #flowstr = flowstr.replace("}","")
                #flowstr = flowstr.replace('"',"")
                self.socket.emit("geo_update",
                            {"data":line},
                            namespace="/")
            else:
                print("received incomplete TCP packet from android IMU")