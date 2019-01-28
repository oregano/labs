const http = require('http');
const url = require('url');

const port = 3000;

// main handler
function handler(req, res) {

    const path = url.parse(req.url).pathname;
    const query = url.parse(req.url).query;

    const uri = url.parse(req.url);

 console.log(JSON.parse(uri.query.name));

    if (path === '/') {
        res.writeHead(200, { 'Content-Type': 'text/plain' })
        res.write('Hi, you are home!');
        res.end();
    }
    else if (path === '/getdetails') {
        var id = query.name;
console.log(query.name);
        if (!id) {
            res.writeHead(400, { 'Content-Type': 'text/plain' })
            res.write('sorry, could not find.');
            return res.end();
        }

        res.writeHead(200, { 'Content-Type': 'text/plain' })
        res.write(`your id is ${id}`);
        res.end();
    }
    else {
        res.writeHead(404, { 'Content-Type': 'text/plain' })
        res.write('sorry, could not find.');
        res.end();
    }

}

// main listener
function listener(err) {
    console.log('I am alive.');

    if (err) console.log(err);
}


const server = http.createServer(handler);

server.listen(port, listener);