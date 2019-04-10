const Botkit = require('Botkit/lib/Botkit.js');
const com = require('./common.js');
const dialog = require('./dialogue.js')
const xml = require('@xmpp/xml');

var wit = require('botkit-middleware-witai')({
    token: 'F4ND2MUPWC7J2DJL6RFKVADLDX2S4TLT'
});

var controller = Botkit.jabberbot({
    json_file_store: './jabberbot/'
});

controller.middleware.receive.use(wit.receive);

var bot = controller.spawn({
    client: {
        jid: 'amy@abc.inc',
        password: '1234',
        host: "10.10.20.17",
        port: 5222
    }
});

function ExtractMentionJids(message) {
    let direct_mention_reg = /href="xmpp:\s?(\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+)\s?"/ig;
    let email_reg = /\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+/i;
    let match = message.stanza.toString().match(direct_mention_reg);
    let mention_jids = [];
    if (match) {
        for (let i = 0; i < match.length; i++) {
            let jid_match = match[i].match(email_reg);
            if (jid_match) {
                let jid = jid_match[0];
                if (jid != bot.client_jid) {
                    mention_jids.push(jid);
                }
            }
        }
    }
    return mention_jids;
}

function toUTCDateTimeString(date) {
    var yyyy = date.getUTCFullYear();
    var mm = date.getUTCMonth() < 9 ? "0" + (date.getUTCMonth() + 1) : (date.getUTCMonth() + 1); // getMonth() is zero-based
    var dd = date.getUTCDate() < 10 ? "0" + date.getUTCDate() : date.getUTCDate();
    var hh = date.getUTCHours() < 10 ? "0" + date.getUTCHours() : date.getUTCHours();
    var min = date.getUTCMinutes() < 10 ? "0" + date.getUTCMinutes() : date.getUTCMinutes();
    var ss = date.getUTCSeconds() < 10 ? "0" + date.getUTCSeconds() : date.getUTCSeconds();
    return "".concat(yyyy).concat('-').concat(mm).concat('-').concat(dd).concat('T').concat(hh).concat(':').concat(min).concat(':').concat(ss);
};

controller.on('listening', ['direct_mention', 'direct_message', 'message_received'], wit.hears, function (bot, message) {

    bot.startConversation(message, function (err, convo) {

        let reply = com.jabfy(message, dialog.greeting(message));
        console.log(message.entities.intent);
        // console.log('pizza type:' + message.entities.pizza_type);
        // convo.say(reply);

    });
});


controller.on('conversationStarted', function (bot, convo) {
    console.log('Conversation started with ', convo.context.user);
});

controller.on('conversationEnded', function (bot, convo) {
    console.log('Conversation stopped with ', convo.context.user);
})