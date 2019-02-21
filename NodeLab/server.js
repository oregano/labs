var http = require("http");
var log = require('./log.js');

var hostname = "127.0.0.1";

var port = 3000;

var server = http.createServer(function(req,res){
    res.statusCode = 200;
    res.setHeader('content-type','text/plain');
    res.end('Hello Kaifee');
});

server.listen(port, hostname, function(){
    log.error('i\'m alive');
});