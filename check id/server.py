import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()

print ('connected:', addr)

while True:
    connection = sqlite3.connect('db')
    curs = connection.cursor()
 
    data = conn.recv(1024).decode("utf-8")
    print('Received: ', data)
    if data == 'first':
        cur.execute("select id from People where id=?", (postid,))
        data = curs.fetchall()
        conn.send(b'first: ' + data.encode("utf-8"))
        print('Send: ', data)
