import websocket
import thread
import time

def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

xCONNECT = '["CONNECT\\naccept-version:1.1,1.0\\nheart-beat:10000,10000\\n\\n\\u0000"]'
xSUBSCRIBE = '["SUBSCRIBE\\nid:sub-0\\ndestination:/topic/greetings\\n\\n\\u0000"]'
xSEND = '["SEND\\ndestination:/app/hello\\ncontent-length:15\\n\\n{\\"name\\":\\"crap\\"}\\u0000"]'
yCONNECT = """CONNECT
accept-version:1.1,1.0
heart-beat:10000,10000

\u0000"""
ySUBSCRIBE = """SUBSCRIBE
id:sub-0
destination:/topic/greetings


\u0000"""
ySEND = """SEND
destination:/app/hello
content-length:15

{"name":"crap"}
\u0000"""


#["SUBSCRIBE\nid:sub-0\ndestination:/topic/greetings\n\n\u0000"]

def on_open(ws):
    def run(*args):
        #for i in range(3):
        #    time.sleep(1)
        #    ws.send("Hello %d" % i)
        ws.send(CONNECT)
        time.sleep(10)
        ws.close()
        print("thread terminating...")
    thread.start_new_thread(run, ())


if __name__ == "__main__":
    #websocket.enableTrace(True)
    #ws = websocket.WebSocketApp('ws://localhost:8080/gs-guide-websocket/055/o0vba17k/websocket',
    #                          on_message = on_message,
    #                          on_error = on_error,
    #                          on_close = on_close)
    #ws.on_open = on_open
    #ws.run_forever()

    ws = websocket.WebSocket()
    ws.connect('ws://localhost:8080/gs-guide-websocket/055/o0vba17k/websocket')
    #ws.connect('ws://localhost:8080/gs-guide-websocket')
    ws.send(xCONNECT)
    resp = ws.recv()
    print("connected:")
    print(resp)
    ws.send(xSUBSCRIBE)
    resp = ws.recv()
    print("subscribed:")
    print(resp)
    ws.send(xSEND)
    resp = ws.recv()
    print("sent:")
    print(resp)
   #



#import websocket
#
#ws = websocket.WebSocket()
#ws.connect('ws://localhost:8080/gs-guide-websocket/websocket')

#import stomp
#
#c = stomp.Connection([('127.0.0.1', 62613)])
#c.start()
#import time
#import sys
#
#import stomp
#
#class MyListener(stomp.ConnectionListener):
#    def on_error(self, headers, message):
#        print('received an error "%s"' % message)
#    def on_message(self, headers, message):
#        print('received a message "%s"' % message)
#
#conn = stomp.Connection([('127.0.0.1', 8080)])
##/gs-guide-websocket
#conn.set_listener('', MyListener())
#conn.start()
#conn.connect('user','password',wait=False)
##conn.connect('user','password',wait=False)
#
#time.sleep(20)
#
#conn.subscribe(destination='localhost/gs-guide-websocket', id=1, ack='auto')
##conn.subscribe(destination='/topic/greetings', id=1, ack='auto')
#
#conn.send(body=' '.join(sys.argv[1:]), destination='/app/hello')
#
#time.sleep(2)
#conn.disconnect()
