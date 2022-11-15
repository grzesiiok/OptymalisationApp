import baza
import sqlite3

bazka = baza.Database('rusztowania.db')
bazka.insert('kasztan',4.4,22)
"""bazka.insert('kasztan2',4.4,22)
bazka.remove(2)"""
kasztan = 'kasztan'
print(bazka.fetch(kasztan))
bazka.__del__()