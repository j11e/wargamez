/*
*   Function that display a message on the HTML page and in the console
*/

messagesContainer = null;

function displayMessage(message, isTitle) {
    console.log(message);

    if ( ! messagesContainer) {
        messagesContainer = document.getElementById('output');
    }

    if (isTitle) {
        message = "<h2>" + message + "</h2>";
    } else {
        message += "<br/>";
    }

    messagesContainer.innerHTML += message.replace(/\n/g, '<br/>');;
}

/*
*   Conversion functions
*   Probably more than needed, but they could be useful
*/
function ascii_to_hex(str) {
    var hexStr = "";
    for (var i=0; i<str.length; i++) {
        hexStr += str.charCodeAt(i).toString(16);
    }

    return hexStr;
}

function hex_to_ascii(hex) {
    var hexVals = hex.match(/../g);
    var str = "";
    for (var i=0; i<hexVals.length;i++) {
        str += String.fromCharCode(parseInt(hexVals[i], 16));
    }

    return str;
}

function hex_to_bytes(string) {
    var chars = string.match(/.{1,2}/g);
    var byteValues = [];
    for (var i=0; i<chars.length; i++) {
        byteValues.push(parseInt(chars[i], 16));
    }

    return byteValues;
}

function bytes_to_hex(values) {
    var hexStr = "";
    var current;

    for (var i=0; i<values.length; i++) {
        current = values[i].toString(16);

        if (current.length == 1) { 
            current = '0' + current;
        }

        hexStr += current;
    }

    return hexStr;
}

function ascii_to_bytes(str) {
    var byteValues = [];
    for (var i=0; i<str.length; i++) {
        byteValues.push(str.charCodeAt(i));
    }

    return byteValues;
}

function bytes_to_ascii(values) {
    var res = "";

    for (var i=0; i<values.length; i++) {
        res += String.fromCharCode(values[i]);
    }

    return res;
}

function base64_to_ascii(base64) {
    return atob(base64);
}

function ascii_to_base64(string) {
    return btoa(string);
}
