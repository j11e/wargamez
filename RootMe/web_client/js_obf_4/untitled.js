var referenceCipher = "\x71\x11\x24\x59\x8d\x6d\x71\x11\x35\x16\x8c\x6d\x71\x0d\x39\x47\x1f\x36\xf1\x2f\x39\x36\x8e\x3c\x4b\x39\x35\x12\x87\x7c\xa3\x10\x74\x58\x16\xc7\x71\x56\x68\x51\x2c\x8c\x73\x45\x32\x5b\x8c\x2a\xf1\x2f\x3f\x57\x6e\x04\x3d\x16\x75\x67\x16\x4f\x6d\x1c\x6e\x40\x01\x36\x93\x59\x33\x56\x04\x3e\x7b\x3a\x70\x50\x16\x04\x3d\x18\x73\x37\xac\x24\xe1\x56\x62\x5b\x8c\x2a\xf1\x45\x7f\x86\x07\x3e\x63\x47";

// values = [113, 17, 36, 89, 141, 109, 113, 17, 53, 22, 140, 109, 113, 13, 57, 71, 31, 54, 241, 47, 57, 54, 142, 60, 75, 57, 53, 18, 135, 124, 163, 16, 116, 88, 22, 199, 113, 86, 104, 81, 44, 140, 115, 69, 50, 91, 140, 42, 241, 47, 63, 87, 110, 4, 61, 22, 117, 103, 22, 79, 109, 28, 110, 64, 1, 54, 147, 89, 51, 86, 4, 62, 123, 58, 112, 80, 22, 4, 61, 24, 115, 55, 172, 36, 225, 86, 98, 91, 140, 42, 241, 69, 127, 134, 7, 62, 99, 71]
// parity = [1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1]

function XOR(x, y) {
    return x ^ y;
}
function sumOfPowersOf2_goingUp(y) {
    var z = 0;
    for (var i = 0; i < y; i++) {
        z += Math.pow(2, i);
    }
    return z;
}
function sumOfPowersOf2_goingDownFrom8(y) {
    var z = 0;
    for (var i = 8 - y; i < 8; i++) {
        z += Math.pow(2, i);
    }
    return z
}
// the 2 following functions cut x in two parts: the y right/leftmost bits, and the rest
// then these two parts are switched
function switchPartsOfByte_yBitsFromRight(x, y) {
    y = y % 8;
    // keep only the y-th righmost bits of x, then shift 8-y bits to the left
    sum = sumOfPowersOf2_goingUp(y);
    sum = (x & sum) << (8 - y);
    return (sum) + (x >> y);
}
function switchPartsOfByte_yBitsFromLeft(x, y) {
    y = y % 8;
    sum = sumOfPowersOf2_goingDownFrom8(y);
    // keep only the y-th leftmost bits of x, shift them 8-y bits to the right
    sum = (x & sum) >> (8 - y);
    return ((sum) + (x << y)) & 0x00ff;
}
function aliasFor_switchPartsOfByte_yBitsFromLeft(x, y) {
    return switchPartsOfByte_yBitsFromLeft(x, y);
}

function process(mysterious_reference, input_password) {
    result = "";
    result2 = "";
    for (var i = 0; i < mysterious_reference.length; i++) {
        referenceCharCode = mysterious_reference.charCodeAt(i);
// values = [113, 17, 36, 89, 141, 109, 113, 17, 53, 22, 140, 109, 113, 13, 57, 71, 31, 54, 241, 47, 57, 54, 142, 60, 75, 57, 53, 18, 135, 124, 163, 16, 116, 88, 22, 199, 113, 86, 104, 81, 44, 140, 115, 69, 50, 91, 140, 42, 241, 47, 63, 87, 110, 4, 61, 22, 117, 103, 22, 79, 109, 28, 110, 64, 1, 54, 147, 89, 51, 86, 4, 62, 123, 58, 112, 80, 22, 4, 61, 24, 115, 55, 172, 36, 225, 86, 98, 91, 140, 42, 241, 69, 127, 134, 7, 62, 99, 71]
// parity = [1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1]
// len: 98
        if (i != 0) {
            t = result.charCodeAt(i - 1) % 2;
            switch (t) {
            case 0:
                cr = XOR(referenceCharCode, input_password.charCodeAt(i % input_password.length));
                break;
            case 1:
                cr = aliasFor_switchPartsOfByte_yBitsFromLeft(referenceCharCode, input_password.charCodeAt(i % input_password.length));
                break;
            }
        } else {
            cr = XOR(referenceCharCode, input_password.charCodeAt(i % input_password.length));
        }
        result += String.fromCharCode(cr);
    }
    return result;
// result[0] = 113 ^ pass[0] toujours
// 
}
function check(parameter) {
    var n = 0;
    for (var i = 0; i < parameter.length; i++) {
        n += parameter["charCodeAt"](i)
    }
    // sum of char codes at must be == 8932
    if (n == 8932) {
        var res_window = window.open("", "", "\x77\x69\x64\x74\x68\x3d\x33\x30\x30\x2c\x68\x65\x69\x67\x68\x74\x3d\x32\x20\x30");
        res_window.document.write(parameter)
    } else {
        alert("Mauvais mot de passe!")
    }
}
check(process(referenceCipher, prompt("Mot de passe?")));