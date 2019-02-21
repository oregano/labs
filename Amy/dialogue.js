module.exports.greeting = function (msg) {
    let name = msg.user.substring(0, msg.user.indexOf('@'));
    switch (msg.text) {
        case 'hi':
            return 'Hi ' + name;
            break;
        case 'hello':
            return 'Hello ' + name;
            break;
        default:
            return 'Hi ' + name;
            break;
    }
}
module.exports.hru = function (msg) {

    let text = msg.text.match(/how are you/i);

    switch (text[0]) {
        case 'how are you':
            return 'I\'m good, thanks, and you?';
            break;
        case 'how r you':
            return 'Good, thanks, how about you?';
            break;
        default:
            return 'good, thank you, hope you are well too!'
            break;
    }
}
module.exports.whois = function (msg) {

    let text = msg.text.match(/do you know/i);
    if (text.length < 0)
        text = msg.text.match(/who is/i);

    switch (text[0]) {
        case '':
            return 'I\'m good, thanks, and you?';
            break;
        case 'how r you':
            return 'Good, thanks, how about you?';
            break;
        default:
            return 'good, thank you, hope you are well too!'
            break;
    }
}