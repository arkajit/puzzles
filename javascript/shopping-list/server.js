var http = require('http');
var static = require('node-static');

var Storage = function() {
  this.items = [];
  this.id = 0;
};

Storage.prototype.add = function(name) {
  var item = {name: name, id: this.id};
  this.items.push(item);
  this.id += 1;
};

var storage = new Storage();
storage.add('Broad beans');
storage.add('Tomatoes');
storage.add('Peppers');

var fileServer = new static.Server('./public');

var server = http.createServer(function(req, res) {
  if (req.method === 'GET' && req.url === '/items') {
    var responseData = JSON.stringify(storage.items);
    res.setHeader('Content-Type', 'application.json');
    res.statusCode = 200;
    res.end(responseData);
  } else if (req.method === 'POST' && req.url === '/items') {
    var item = '';
    req.on('data', function(chunk) {
      item += chunk;
    });
    req.on('end', function() {
      try {
        item = JSON.parse(item);
        storage.add(item.name);
        res.statusCode = 201;
        res.end();
      }
      catch(e) {
        res.statusCode = 400;
        responseData = {'message': 'Invalid JSON'};
        res.end(JSON.stringify(responseData));
      }
    });
  } else {
    fileServer.serve(req, res);
  }
});

server.listen(8080, function() {
  console.log('listening on localhost:8080');
});
