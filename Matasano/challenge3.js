// source: http://www.macfreek.nl/memory/Letter_Distribution
var englishLetterFrequencies = {
        ' ': 18.28846265,
        e: 10.26665037,
        t: 7.51699827,
        a: 6.53216702,
        o: 6.15957725,
        n: 5.71201113,
        i: 5.66844326,
        s: 5.31700534,
        r: 4.98790855,
        h: 4.97856396,
        l: 3.31754796,
        d: 3.28292310,
        u: 2.27579536,
        c: 2.23367596,
        m: 2.02656783,
        f: 1.98306716,
        w: 1.70389377,
        g: 1.62490441,
        p: 1.50432428,
        y: 1.42766662,
        b: 1.25888074,
        v: 0.79611644,
        k: 0.56096272,
        x: 0.14092016,
        j: 0.09752181,
        q: 0.08367550,
        z: 0.05128469
};

function scoreEnglishPlaintext(plaintext) {
    // naive scoring algorithm: 
    // every letter's score is its frequency of apparition in english
    // including the probability of whitespace.
    var score = 0;
    var letter;
    var letterValue;

    for (var i=0; i<plaintext.length; i++) {
        letter = plaintext[i].toLowerCase();
        letterValue = englishLetterFrequencies[letter] ? englishLetterFrequencies[letter] : 0;
        score += letterValue;
    }

    return score;
}

displayMessage("Challenge number three", true);

var ch3_encoded = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736";
var ch3_encodedBytes = hex_to_bytes(ch3_encoded);
var ch3_key;
var ch3_plaintext;

for (var i=0; i<256; i++) {
    ch3_plaintext = XOR(ch3_encodedBytes, [i]);
    //console.log(i + ": "+ bytes_to_ascii(ch3_plaintext));
}

// a key of 88 gives "Cooking MC's like a pound of bacon"
displayMessage('key: 88, plaintext: ')
displayMessage(bytes_to_ascii(XOR(ch3_encodedBytes, [88])));
// it's the only key that gives an english plaintext 

// now let's automate this:
var ch3_results = [];

for (var i=0; i<256; i++) {
    ch3_plaintext = XOR(ch3_encodedBytes, [i]);
    ch3_plaintext = bytes_to_ascii(ch3_plaintext);

    ch3_results.push({
    	score: scoreEnglishPlaintext(ch3_plaintext), 
    	key: i,
    	plaintext: ch3_plaintext
    });
}

ch3_results.sort(function(res1, res2) { // sort the results by their score
    return res2.score - res1.score; 
});

// let's see the result that got the best score
displayMessage('Best result of automated decryption: ')
displayMessage(ch3_results[0].plaintext);