var express = require('express/lib/express.js');

var app = express();

app.get('/', function (req, res) {
    
    var sql = require('mssql');

    var config = {
        user: 'sa',
        password: '@pple!23',
        server: 'localhost',
        database: 'NodeLab'
    };
    
    sql.connect(config, function (err) {
        
        if (err) { console.log(err); sql.close(); };

        var request = new sql.Request();

        request.query('select * from employee', function (err, recordset) {

            if (err) { console.log(err); sql.close(); };

            res.send(recordset.Title);
        });
    });
});

var server = app.listen(5000, function () {
    console.log('server is up and running!');
});