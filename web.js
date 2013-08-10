var fs = require('fs');
var express = require('express');
var pg = require('pg');

var app = express.createServer(express.logger());
var buf = fs.readFileSync('index.html', 'utf-8');
var string =buf.toString();
app.get('/', function(request, response)  {
  response.send(string);
});

var connectionString = process.env.DATABASE_URL || "pg://amy:amy@localhost/hbUsers";

app.post('/', function(req, res) {
	console.log(req.body);
	pg.connect(connectionString, function(err, client, done) {
                client.query('INSERT INTO users VALUES ($1, $2)', [eq.body['name'], req.body['email']], function(err, result) {
                        done();
		});
	});
});

var port = process.env.PORT || 8080;
app.listen(port, function() {
  console.log("Listening on " + port);
});

