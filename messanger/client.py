import socket 
import time

conn = socket.socket()
conn.connect( ("127.0.0.1", 14900) )
conn.send(b"Hello! \n")
data = b""
tmp = conn.recv(1024)
while tmp:
    data += tmp
    tmp = conn.recv(1024)
print( data.decode("utf-8") )
conn.close()
conn = socket.socket()
conn.connect( ("vk.com", 80) )
conn.setblocking(0)

try: data = conn.recv(1024)
except socket.error: 
    pass 
else: 
    print(data)
    
conn = socket.socket()
conn.bind( ("", 8989) )
conn.listen(5)
conn.setblocking(0)

try: client, addr = conn.accept()
except socket.error: 
    pass 
else: 
    client.setblocking(0) 
    parse(client, addr)
    
    
