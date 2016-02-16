var http   = require('http');
var _      = require('lodash');
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

/**
 * Removes the item with the given id, if it exists, and returns it.
 * If the item doesn't exist, returns `undefined` and removes nothing.
 *
 */
Storage.prototype.remove = function(id) {
  var removed = _.remove(this.items, function(item) {
    return item.id === id;
  });

  return removed[0];
};

/**
 * Updates the item with the given id to have a new name, if it exists.
 * Otherwise, creates a new item with this name and id.
 */
Storage.prototype.update = function(item) {
  var matching = _.find(this.items, function(el) {
    return el.id === item.id;
  });
  if (matching) {
    matching.name = item.name;
    return matching;
  } else {
    this.items.push(item);
    // Start incrementing ids from this `id` if it
    // skipped past the next available id.s
    this.id = Math.max(this.id, item.id+1);
    return item;
  }
}

var storage = new Storage();
storage.add('Broad beans');
storage.add('Tomatoes');
storage.add('Peppers');

var fileServer = new static.Server('./public');

var tryParse = function(req) {
  var item = '';

  req.on('data', function(chunk) {
    item += chunk;
  });
};

var server = http.createServer(function(req, res) {
  console.log('Received request: ' + req.method + ' ' + req.url);

  var body = '';
  req.on('data', function(chunk) {
    body += chunk;
  });

  if (req.method === 'GET' && req.url === '/items') {

    var responseData = JSON.stringify(storage.items);
    res.setHeader('Content-Type', 'application.json');
    res.statusCode = 200;
    res.end(responseData);

  } else if (req.method === 'POST' && req.url === '/items') {

    req.on('end', function() {
      try {
        var item = JSON.parse(body);
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

  } else if (req.method === 'DELETE' && req.url.indexOf('/items') === 0) {

    var tokens = req.url.split('/');
    var itemId = parseInt(tokens[2]);  // maybe NaN
    if (itemId) {
      var removedItem = storage.remove(itemId);
      if (removedItem) {
        var response = JSON.stringify(removedItem);
        res.statusCode = 200;
        res.end(response);
      } else {
        var response = {'message': 'Item with id ' + itemId + ' does not exist.'};
        res.statusCode = 400;
        res.end(JSON.stringify(response));
      }
    } else {
      var response = {'message': 'Invalid item id.'};
      res.statusCode = 400;
      res.end(JSON.stringify(response));
    }

  } else if (req.method === 'PUT' && req.url.indexOf('/items') === 0) {

    var tokens = req.url.split('/');
    var itemId = parseInt(tokens[2]);  // maybe NaN
    if (!itemId) {
      var response = {'message': 'Invalid item id.'};
      res.statusCode = 400;
      res.end(JSON.stringify(response));
      return;
    }

    req.on('end', function() {
      try {
        var item = JSON.parse(body);
        var updated = storage.update(item);
        res.statusCode = 200;
        res.end(JSON.stringify(updated));
      } catch(e) {
        res.statusCode = 400;
        var response = {'message': 'Invalid JSON'};
        res.end(JSON.stringify(response));
      }
    });

  } else {
    fileServer.serve(req, res);
  }
});

server.listen(8080, function() {
  console.log('listening on localhost:8080');
});
