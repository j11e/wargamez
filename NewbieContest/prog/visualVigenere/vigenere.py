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


def modify_pixel(image, pixel_coords, index_to_change, value):
    pixel = image[pixel_coords]
    pixel = list(pixel)
    pixel[index_to_change] = value
    pixel = tuple(pixel)

    image[pixel_coords] = pixel


def decrypt_images():
    img = Image.open("image")
    img_pixels = img.load()
    size_h, size_v = img.size

    clear = Image.new('RGB', img.size)
    clear_pixels = clear.load()

    v_shifts = Image.open("shifts_v")
    v_shifts_pixels = v_shifts.load()
    h_shifts = Image.open("shifts_h")
    h_shifts_pixels = h_shifts.load()

    for i in range(size_h):
        for j in range(size_v):
            # # go look for the RGB components where they ended up
            comp_coords = [[i, j], [i, j], [i, j]]
            shift_h = h_shifts_pixels[0, j]

            r_h_shift = (i + shift_h[0]) % size_h
            g_h_shift = (i + shift_h[1]) % size_h
            b_h_shift = (i + shift_h[2]) % size_h

            comp_coords[0][0] = r_h_shift
            comp_coords[1][0] = g_h_shift
            comp_coords[2][0] = b_h_shift
            
            r_v_shift = (j + v_shifts_pixels[r_h_shift, 0][0]) % size_v
            g_v_shift = (j + v_shifts_pixels[g_h_shift, 0][1]) % size_v
            b_v_shift = (j + v_shifts_pixels[b_h_shift, 0][2]) % size_v

            comp_coords[0][1] = r_v_shift
            comp_coords[1][1] = g_v_shift
            comp_coords[2][1] = b_v_shift
            
            recomposed_pixel_value = []
            recomposed_pixel_value.append(img_pixels[comp_coords[0][0], comp_coords[0][1]][0])
            recomposed_pixel_value.append(img_pixels[comp_coords[1][0], comp_coords[1][1]][1])
            recomposed_pixel_value.append(img_pixels[comp_coords[2][0], comp_coords[2][1]][2])

            clear_pixels[i,j] = tuple(recomposed_pixel_value)

    # todo: split the image because tesseract sucks ass
    # need at least to have the 2nd line in its own PNG to read it as french,
    # whereas the first line must ignore dictionaries to avoid bad results

    # need the .png extension because otherwise tesseract does not recognize PNG?
    clear.save("image_clear.png", "PNG")

def read_dem_words():
    words = []

    p = subprocess.Popen(['tesseract', '-psm', '3', 'image_clear.png', 'stdout'], stdout=subprocess.PIPE)
    (output, err) = p.communicate()
    print(output)

    p = subprocess.Popen(['tesseract', '-psm', '3', 'image_clear_key.png', 'stdout'], stdout=subprocess.PIPE)
    (output, err) = p.communicate()
    print(output)

    # 
    # return output.split(" ")


def decrypt_words(cipher, key):
    # todo: map tesseract's bad recognition of numbers to their actual value
    tesseract_translation = {
        "Ey": 3,
        "todo": 0
    }

    return ["to", "do"]


if __name__ == '__main__':
    #get_images()
    #decrypt_images()

    read_dem_words()
    # content = read_dem_words()

    # cleartext = decrypt_words(content[:5], content[5])

    # password = content[content[6]]

    # r = requests.get(url_out, cookies=cookies, params={ "solution": password })
    # print(r.text)
