import time
import sys

import stomp

class MyListener(stomp.ConnectionListener):
    def on_error(self, headers, message):
        print('received an error "%s"' % message)
    def on_message(self, headers, message):
        print('received a message "%s"' % message)

conn = stomp.Connection([('192.168.1.21',61613)], auto_content_length=False)
conn.set_listener('', MyListener())
conn.start()
conn.connect('admin', 'password', wait=True)

#conn.subscribe(destination='/queue/test', id=1, ack='auto')

#Email{to="info@example.com", body="Hello"}
#{"to":"info@example.com","body":"Hello"}

conn.send(body='{"to":"info@example.com","body":"Hello mf"}', content_type='text/plain', headers={'_type': 'hello.Email'}, destination='/queue/mailbox')
#conn.send(body=' '.join(sys.argv[1:]), destination='/queue/test')

time.sleep(5)
conn.disconnect()
