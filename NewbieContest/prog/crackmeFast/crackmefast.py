import r2pipe # radare ftw
import requests

url_in = "https://www.newbiecontest.org/epreuves/prog/prog_crackmefast.php"
url_out = "https://www.newbiecontest.org/epreuves/prog/verifpr_crackmefast.php"
cookies = {
    "PHPSESSID": "0f5a68209c4d3306a80b40f70536937f",
    "SMFCookie89": "a%3A4%3A%7Bi%3A0%3Bs%3A5%3A%2266929%22%3Bi%3A1%3Bs%3A40%3A%228aa08e09e0976cb352be5a6eff657591f1b75e5e%22%3Bi%3A2%3Bi%3A1705080948%3Bi%3A3%3Bi%3A0%3B%7D"
}


def crack_it_fast(filepath):
    # do the thing!
    r2 = r2pipe.open("/home/jd/crackmefast.exe")

    # first, get all the bytes of instructions that write the password
    # asm_bytes looks like c645ec68c645f069c645ef62c645ea74c645e96bc645e868c645eb7ac645ee66c645f161c645ed61
    asm_bytes =  r2.cmd("0x004012d2; px0 40")
    
    # remove the c645 MOV instruction, and split destination from value,
    # AND translate the value from hex to ascii character
    # so asm_bytes looks like [ (ec, 68), (f0, 69), ...]
    asm_bytes = [ (asm_bytes[i+4:i+6], chr(int(asm_bytes[i+6:i+8], 16))) for i in range(0,len(asm_bytes), 8) ]
    
    # now, sort that by destination to get the right order of characters
    asm_bytes.sort()

    # that's it, return the password
    return ''.join(map(lambda x: x[1], asm_bytes))


if __name__ == "__main__":
    r = requests.get(url_in, cookies=cookies)
    binary = r.content

    f = open("/home/jd/crackmefast.exe", "wb")
    f.write(binary)
    f.close()

    print("crackin' it now")
    password = crack_it_fast("/home/jd/crackmefast.exe")

    payload = {
        "reponse": password
    }

    r = requests.get(url_out, cookies=cookies, params=payload)
    print(r.text)
    print(r.content)
    print(r.content.decode('utf8'))
