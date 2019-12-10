var app = require('express')();
var express = require('express');
var http = require('http').createServer(app);
var path = require('path');
var port = process.env.PORT || 3000;


app.use(express.static(path.resolve(__dirname,"public")));

app.get('/', function(req, res){
  res.sendFile(__dirname + '/index.html');
 });

http.listen(port, function(){
  console.log('listening on *: ' + port);
});