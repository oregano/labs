const express = require('express');
const app = express();

app.use(express.static('./gallery/jpeg'));

app.use('/gifs', express.static('./gallery/gif'));

const data = require('./data/leads.json');

app.get('/', (req, res) => {
    res.json(data);
});

app.get('/leads/:id', (req, res, next) => {
    console.log(req.params.id);

    res.send(data[req.params.id]);
    next();
}, (req, res) => {
    console.log('I am next.');
});

app.listen(3000, (err) => {
    console.log('app is running...');
})