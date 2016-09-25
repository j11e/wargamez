function XOR(bytes1, bytes2) {
    var res = [];
    var xored_byte;

    for (var i=0; i<bytes1.length; i++) {
        xored_byte = bytes1[i%bytes1.length] ^ bytes2[i%bytes2.length];
        res.push(xored_byte);
    }
    
    return res;
}

displayMessage("Challenge number two", true);

var ch2_hex1 = "1c0111001f010100061a024b53535009181c";
var ch2_hex2 = "686974207468652062756c6c277320657965";
var ch2_expected = "746865206b696420646f6e277420706c6179";

var ch2_bytes1 = hex_to_bytes(ch2_hex1);
var ch2_bytes2 = hex_to_bytes(ch2_hex2);

var ch2_result = XOR(ch2_bytes1, ch2_bytes2);
ch2_result = bytes_to_hex(ch2_result);

displayMessage(ch2_hex1);
displayMessage('XOR');
displayMessage(ch2_hex2);
displayMessage('=');
displayMessage(ch2_result);
displayMessage('expected: ');
displayMessage(ch2_expected);
displayMessage('Match: ' + (ch2_result == ch2_expected));