#import websocket
#
#ws = websocket.WebSocket()
#ws.connect('ws://localhost:8080/gs-guide-websocket/topic/greetings/app')

#import stomp
#
#c = stomp.Connection([('127.0.0.1', 62613)])
#c.start()
import time
import sys

import stomp

class MyListener(stomp.ConnectionListener):
    def on_error(self, headers, message):
        print('received an error "%s"' % message)
    def on_message(self, headers, message):
        print('received a message "%s"' % message)

conn = stomp.Connection([('127.0.0.1', 8080)])
conn.set_listener('', MyListener())
conn.start()
conn.connect(wait=False)

time.sleep(10)

conn.subscribe(destination='/topic/greetings', id=1, ack='auto')

conn.send(body=' '.join(sys.argv[1:]), destination='/app/hello')

time.sleep(2)
conn.disconnect()
