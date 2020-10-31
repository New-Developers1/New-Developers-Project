import sqlite3 as lite
import sys



con = lite.connect('db')
postid = input()


cur = con.cursor()
cur.execute("select id from People where id=?", (postid,))
data = cur.fetchall()
if not data:
        print ('Не найдено совпадений')
else:
        print ('Найдено совпадение')
