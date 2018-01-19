import sys
import subprocess
import requests

cookie = {'PHPSESSID': '0047f2100ebf9957a43ab8ab08d75558', 'admin': '0', 'SMFCookie89': 'a%3A4%3A%7Bi%3A0%3Bs%3A5%3A%2266929%22%3Bi%3A1%3Bs%3A40%3A%228aa08e09e0976cb352be5a6eff657591f1b75e5e%22%3Bi%3A2%3Bi%3A1633801647%3Bi%3A3%3Bi%3A0%3B%7D'}

inURL = "https://www.newbiecontest.org/epreuves/prog/prog10.php"
outURL = "https://www.newbiecontest.org/epreuves/prog/verifpr10.php"

r = requests.get(inURL, cookies=cookie)

if r.status_code != 200:
    sys.exit("Error when retrieving image")

filename = '/root/Pictures/nbc_tmp_prg10.png'

imgfile = open(filename, 'wb')
for chunk in r:
    imgfile.write(chunk)

imgfile.close()

p = subprocess.Popen(["gocr", "-i", filename], stdout=subprocess.PIPE)
(output, err) = p.communicate()
print("avant split, output = " + output)
output = output.split("\n")[0]
print("Extracted string: " + output)

r2 = requests.get(outURL + "?chaine=" + output, cookies=cookie)

print(r2.text)
