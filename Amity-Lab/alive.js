const express = require('express');

const app = express();

app.get('/', (req, res) => {
    return res.send('Hi, I am a web server...');
})

app.get('/getdetails', (req, res) => {
    return res.send(`This is ${req.query.name} and I am ${req.query.age} old.`);
})

app.listen(4000, (err) => {
    console.log('I\'m listening');
});