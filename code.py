
class WSHandler(tornado.websocket.WebSocketHandler):
    """ WebSocket handler """

    def initialize(self, notifier):
        """ initialize when a new websocket connects """
        self._notifier = notifier
        self._notifier.register_callback(self.process_notification)

    def process_notification(self, data):
        """ process notification """
        self.write_message(data)

def handle_udp_messages(sock, fd, events):
    """ Handles UDP messages it receives """
    while True:
        try:
            data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
            if not data:
                sock.close()
                break
            else:
                # for debugging purpose
                print "Received %d bytes: '%s'" % (len(data), data)

                # notify that we have new data
                notifier.notify(data)
        except socket.error, e:
            break