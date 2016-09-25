// conversion functions in misc.js

displayMessage("Challenge number one", true);

var ch1_hex = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d";
var ch1_b64 = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t";

var ch1_conv = ascii_to_base64(hex_to_ascii(ch1_hex));
displayMessage("0x" + ch1_hex + " converted in base64 is " + ch1_b64 + "?" );
displayMessage(ch1_conv == ch1_b64);

var ch1_back = ascii_to_hex(base64_to_ascii(ch1_conv));
displayMessage("Converted in hex from base64, " + ch1_conv + " is " + ch1_back+"?");
displayMessage(ch1_back == ch1_hex);
