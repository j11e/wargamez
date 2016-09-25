displayMessage("<span style='text-decoration: line-through'>Mambo</span> Challenge number five", true);

var ch5_plaintext = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal";
var ch5_key = "ICE";
var ch5_expected = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f";

var ch5_plain_bytes = ascii_to_bytes(ch5_plaintext);
var ch5_key_bytes = ascii_to_bytes(ch5_key);

var ch5_cipher_bytes = XOR(ch5_plain_bytes, ch5_key_bytes);

displayMessage(ch5_plaintext);
displayMessage('XOR');
displayMessage(ch5_key);
displayMessage('=');
displayMessage('0x'+bytes_to_hex(ch5_cipher_bytes));
displayMessage('Expected: ');
displayMessage('0x'+ch5_expected);
displayMessage('Match: ' + (bytes_to_hex(ch5_cipher_bytes) == ch5_expected))
