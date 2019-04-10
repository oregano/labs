const agent = require('superagent');
const util = require('util');

const key = 'f7062f01c1a4f3a56374f39ab8afa7e6';
const place = 'Chelmsford, GB';
const url = `http://api.openweathermap.org/data/2.5/weather?q=${place}&appid=${key}`

agent.get(url, (err, res) => {

    if (err) throw err;

    var data = JSON.parse(res.text);

    var temp = data.main.temp - 273.15 // converting into celsius
    var type = data.weather[0].description;
    console.log(`Current temperature is ${temp} celsius with ${type}.`);
})