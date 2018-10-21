from threading import Thread
import time 
import socket 

class SensorNodeHandler(Thread):
    def __init__(self, UDP_IP, UDP_PORT,latitude = 0,longitude = 0, Socket = None):
        Thread.__init__(self)
        self.daemon = True
        self.ip = UDP_IP
        self.port = UDP_PORT
        self.latitude = latitude
        self.longitude = longitude
        self.data = []
        #self.socket = Socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((UDP_IP, UDP_PORT))

    def run(self):
        while True:
            time.sleep(.75)
            data, _ = self.sock.recvfrom(1024)	
            line = data.strip().decode('ascii').split(',')
            line = [float(i) for i in line]
            if len(line) == 3:
                self.data = line 
                print(line)
                """
                self.socket.emit("geo_update",
                            {"data":(self.latitude,
                                self.longitude,
                                line[2]*2)},
                            namespace="/")
                """"
                            
            else:
                print("received incomplete UCP packet from android IMU")
if __name__ == "__main__":
    Test = SensorNodeHandler("10.99.96.134",5000)
    Test.start()

    