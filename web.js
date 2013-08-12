var fs = require('fs');
var express = require('express');
var pg = require('pg');


var app = express.createServer(express.logger());
app.use(express.bodyParser());



var buf = fs.readFileSync('index.html', 'utf-8');
var string =buf.toString();
app.get('/', function(request, response)  {
  response.send(string);
});

var connectionString = process.env.DATABASE_URL || "pg://amy:amy@localhost/hbusers";

app.post('/', function(req, res) {
	console.log(req.body);
	var buf2 = fs.readFileSync('thanks.html', 'utf-8');
	var string2 =buf2.toString();

	res.send(string2);
	pg.connect(connectionString, function(err, client, done) {
		if (err) throw err;
		client.query('CREATE TABLE IF NOT EXISTS users(name varchar(255),email varchar(255))');
                client.query('INSERT INTO users VALUES ($1, $2)', [req.body['name'], req.body['email']], function(err, result) {
                        done();
		});
	}); 
});

var port = process.env.PORT || 8080;
app.listen(port, function() {
  console.log("Listening on " + port);
});

