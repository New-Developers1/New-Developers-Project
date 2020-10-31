import subprocess
import sys
import time
import urllib3

server = subprocess.Popen([sys.executable, 'server.py'])
time.sleep(2)  # Даем время серверу на запуск

http = urllib3.PoolManager()
ID = 'http://192.168.0.105'
resp = http.request('GET', ID)
#print(resp.status)


resp.status = subprocess.Popen([sys.executable, 'ID.py'])

server.wait()