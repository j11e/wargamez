import requests
import subprocess
from PIL import Image


url_in = "https://www.newbiecontest.org/epreuves/prog/prog11.php"
url_out = "https://www.newbiecontest.org/epreuves/prog/verifpr11.php"

cookies = {
    "PHPSESSID": "0f5a68209c4d3306a80b40f70536937f",
    "SMFCookie89": "a%3A4%3A%7Bi%3A0%3Bs%3A5%3A%2266929%22%3Bi%3A1%3Bs%3A40%3A%228aa08e09e0976cb352be5a6eff657591f1b75e5e%22%3Bi%3A2%3Bi%3A1705080948%3Bi%3A3%3Bi%3A0%3B%7D"
}


def get_images():
    print("Downloading and splitting images")

    r = requests.get(url_in, cookies=cookies)
    full_data = r.content


    # split the binary data in three PNG images by looking for the magic numbers
    # don't even look at the first or last bytes because we know it's not there
    offsets = []
    for index in range(5, len(full_data)-10):
        if full_data[index+1:index+4] == b'PNG':
            offsets.append(index)

    f = open("image", "wb")
    f.write(full_data[:offsets[0]])
    f.close
    
    f = open("shifts_h", "wb")
    f.write(full_data[offsets[0]:offsets[1]])
    f.close
    
    f = open("shifts_v", "wb")
    f.write(full_data[offsets[1]:])
    f.close
    
    print("Image retrieval done.")
    return


def decrypt_images():
    img = Image.open("image")
    

def read_dem_words():
    words = []

    p = subprocess.Popen(['gocr', '-i', 'image__clear.png'], stdout=subprocess.PIPE)
    (output, err) = p.communicate()
    print(output)

    return output.split(" ")


def decrypt_words(cipher, key):
    return ["to", "do"]


if __name__ == '__main__':
    get_images()
    decrypt_images()

    content = read_dem_words()

    cleartext = decrypt_words(content[:5], content[5])

    password = content[content[6]]

    r = requests.get(url_out, cookies=cookies, params={ "solution": password })
    print(r.text)
