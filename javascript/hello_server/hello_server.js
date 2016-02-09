var http = require('http');

var server = http.createServer(function(request, response) {
  response.setHeader('Content-Type', 'application/json');
  if (request.url == '/headers') {
    response.write(JSON.stringify(request.headers));
  } else if (request.url == '/version') {
    response.write(request.httpVersion);
  } else if (request.url.indexOf('/headers/') == 0) {
    // NOTE: not very robust to parsing errors.
    var headerName = request.url.split('/')[2];
    var headerValue = request.headers[headerName] || 'Not Set';
    response.write(headerValue);
  }
  response.end();
});

server.listen(8080);
