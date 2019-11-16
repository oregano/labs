function isPalindrome(num) {
    var reverse = parseInt(reverseString(num.toString()));

    return num == reverse ? true : false;
}

function reverseString(str) {

    return str.split("").reverse().join("");
}

var palin = [];

for (i = 1; i <= 999; i++) {
    for (j = 999; j >= 1; j--) {
        if (isPalindrome(j * i))
            palin.push(i * j);
    }
}

palin.sort(function (a, b) { return b - a; });

console.log(`max palindrome is ${palin[0]}`)