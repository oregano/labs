var agent = require('superagent');

const key = 'f7062f01c1a4f3a56374f39ab8afa7e6';
const city = 'Hyderabad, India';
var url = `http://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${key}`

agent.get(url, (err, res) =>{
    if(err) throw err;

    var data = JSON.parse(res.text);
    console.log(data.main.temp - 273.15);
})