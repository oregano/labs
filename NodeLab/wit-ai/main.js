const {Wit} = require('node-wit');

const {interactive} = require('node-wit');


const client = new Wit({accessToken: 'F4ND2MUPWC7J2DJL6RFKVADLDX2S4TLT'});
client.message('what is your plan for tomorrow?', {})
.then((data) => {
//   console.log('Yay, got Wit.ai response: ' + JSON.stringify(data));

console.log(data.entities.datetime[0].value);
console.log(data.entities.intent[0].value);

})
.catch(console.error);

interactive(client);