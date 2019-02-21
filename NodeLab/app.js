var fs = require('fs')
var d = require('./emp.json')

console.log(d.age)

fs.readFile('./emp.json', 'utf-8',(err, data) => {

    var d = JSON.parse(data)
    console.log(d.name)
})