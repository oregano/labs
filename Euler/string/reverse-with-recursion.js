"use strict";
var str = "apple";

function reverse(ch) {
    if (ch == "")
        return "";
    console.log(ch);
    return reverse(ch.substr(1)) + ch.charAt(0);
}
console.log(reverse(str));

