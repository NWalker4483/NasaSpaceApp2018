from threading import Thread
import time 
import socket 

class SensorNodeHandler(Thread):
    def __init__(self, UDP_IP, UDP_PORT,latitude = 0,longitude = 0, Socket = None):
        Thread.__init__(self)
        self.ip = UDP_IP
        self.port = UDP_PORT
        self.latitude = latitude
        self.longitude = longitude
        #self.socket=Socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((UDP_IP, UDP_PORT))

    def run(self):
        while True:
            time.sleep(0.1)
            data, _ = self.sock.recvfrom(1024)	
            
            line = data.strip().decode('ascii').split(',')
            print(line)
            if len(line) == 3:
                print(line)
                #flowstr = str(self.flow[i])
                #flowstr = flowstr.replace("{","")
                #flowstr = flowstr.replace("}","")
                #flowstr = flowstr.replace('"',"")
                #self.socket.emit("geo_update",
                            #{"data":line},
                            #namespace="/")
            else:
                print("received incomplete UCP packet from android IMU")
if __name__ == "__main__":
    Test = SensorNodeHandler("192.168.43.14",5000)
    Test.run()