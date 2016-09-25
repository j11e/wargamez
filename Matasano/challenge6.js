function count_ones(byteValue) {
    // count the number of ones in the binary representation of byteValue
    var byteStr = byteValue.toString(2);
    var len1 = byteStr.length;
    var len2 = byteStr.replace(/1/g, '').length;

    return len1-len2;
}

function hammingDistance(bytes1, bytes2) {
    var xor = XOR(bytes1, bytes2);
    var hammingDist = 0;

    for (var i=0; i<xor.length; i++) {
        hammingDist += count_ones(xor[i]);
    }

    return hammingDist;
}

function reconstructPlaintext(parts) {
    var letter;
    var reconstructed = "";

    for (var i=0; i<parts[0].length; i++) {
        for (var j=0; j<parts.length; j++) {
            letter = parts[j][i];
            if (letter) {
                reconstructed += letter;
            }
        }        
    }

    return reconstructed;
}

displayMessage("Challenge number six", true);

var ch6_cipher_b64 = "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";
var ch6_cipher_bytes = ascii_to_bytes(base64_to_ascii(ch6_cipher_b64));
    
var ch6_KEYSIZE;

// b.
displayMessage('Hamming distance between "this is a test" and "wokka wokka!!!": ');
displayMessage(hammingDistance(ascii_to_bytes("this is a test"), ascii_to_bytes("wokka wokka!!!")));

// c.
var ch6_first_part;
var ch6_second_part;
var ch6_hammingDistances = [];
var ch6_numberOfPairsTested = 42;
var ch6_hamDist;
var ch6_offset;

for (ch6_KEYSIZE=2; ch6_KEYSIZE<42; ch6_KEYSIZE++) {
    ch6_hamDist = 0;

    for (var i=0; i<ch6_numberOfPairsTested; i++) {
        ch6_offset = i * ch6_KEYSIZE;

        ch6_first_part = ch6_cipher_bytes.slice(ch6_offset, ch6_offset + ch6_KEYSIZE);
        ch6_second_part = ch6_cipher_bytes.slice(ch6_offset + ch6_KEYSIZE, ch6_offset + 2*ch6_KEYSIZE);    

        ch6_hamDist += hammingDistance(ch6_first_part, ch6_second_part);
    }

    ch6_hamDist /= ch6_KEYSIZE; // normalization
    ch6_hamDist /= ch6_numberOfPairsTested; // average

    ch6_hammingDistances.push({
        keysize: ch6_KEYSIZE, 
        distance: ch6_hamDist
    });
}

ch6_hammingDistances.sort(function(dist1, dist2) {
    return dist1.distance - dist2.distance;
});

displayMessage('The three most likely key sizes are: ');
displayMessage('   * ' + ch6_hammingDistances[0].keysize + '(average distance: '+ch6_hammingDistances[0].distance+')'); // 29
displayMessage('   * ' + ch6_hammingDistances[1].keysize + '(average distance: '+ch6_hammingDistances[1].distance+')'); // 15
displayMessage('   * ' + ch6_hammingDistances[2].keysize + '(average distance: '+ch6_hammingDistances[2].distance+')'); // 11

// let's assume the first result, 29, is the correct one.

// split cipher into blocks
ch6_KEYSIZE = 29;
var ch6_blocks = [];
var ch6_curBlockIdx;
for (var i=0; i<ch6_cipher_bytes.length; i++) {
    ch6_curBlockIdx = Math.floor(i/ch6_KEYSIZE);
    if (!ch6_blocks[ch6_curBlockIdx]) {
        ch6_blocks[ch6_curBlockIdx] = [];
    }

    ch6_blocks[ch6_curBlockIdx].push(ch6_cipher_bytes[i]);
}

// blocks transposition
var ch6_transposedBlocks = [];
for (var i=0; i<ch6_KEYSIZE; i++) {
    ch6_transposedBlocks.push([]);
}

for (var i=0; i<ch6_blocks.length; i++) {
    for (var j=0; j<ch6_KEYSIZE; j++) {
        if (typeof ch6_blocks[i][j] !== "undefined") {
            ch6_transposedBlocks[j].push(ch6_blocks[i][j]);
        }
    }
}

// decrypt each block individually
var ch6_curBlock;
var ch6_curXoredBlock;
var ch6_bestScores = [];
var ch6_curScores = [];

for (var i=0; i<ch6_KEYSIZE; i++) {
    ch6_curBlock = ch6_transposedBlocks[i];
    ch6_curScores = [];

    for (var key=0; key<256; key++) {
        ch6_curXoredBlock = XOR(ch6_curBlock, [key]);
        ch6_score = scoreEnglishPlaintext(bytes_to_ascii(ch6_curXoredBlock));

        ch6_curScores.push({
            key: key, 
            score: ch6_score,
            plaintext: bytes_to_ascii(ch6_curXoredBlock)
        });
    }

    ch6_curScores.sort(function(score1, score2) {
        return score2.score - score1.score;
    });

    ch6_bestScores.push(ch6_curScores);
}

// reconstruct plaintext
displayMessage('Assuming a key length of '+ch6_KEYSIZE+", result is: ");

var ch6_key = "";
for (var i=0; i<ch6_KEYSIZE; i++) {
    ch6_key += String.fromCharCode(ch6_bestScores[i][0].key); // taking the best result for each transposed block
}

displayMessage("key: "+ch6_key);


var ch6_parts = [];
for (var i=0; i<ch6_KEYSIZE; i++) {
    ch6_parts.push(ch6_bestScores[i][0].plaintext); // taking the best result for each transposed block
}

var ch6_reconstructedPlaintext = reconstructPlaintext(ch6_parts);
displayMessage(ch6_reconstructedPlaintext);
