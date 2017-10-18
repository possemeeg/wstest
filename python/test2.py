import websocket

#ws = websocket.WebSocket()
#ws.connect('ws://localhost:8080/gs-guide-websocket')

from websocket import create_connection

ws = create_connection("ws://localhost:8080/gs-guide-websocket")
print("Sending 'Hello, World'...")
ws.send("Hello, World")
print("Sent")
print("Receiving...")
result =  ws.recv()
print("Received '%s'" % result)
ws.close()
