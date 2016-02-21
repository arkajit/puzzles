var Cache = require('./cache');
var fs    = require('fs');
var url   = require('url');
var zlib  = require('zlib');

/** A static file server which caches gzipped files by filename. */
function CacheServer(directory) {
  this.directory = directory;
}

CacheServer.prototype.serve = function(req, res) {
  var pathname = url.parse(req.url).pathname;
  var filename = this.directory + pathname;
  console.log('Serving file: ' + filename);

  if (Cache.store.hasOwnProperty(filename)) {
    console.log('Serving from cache.');
    zlib.unzip(Cache.store[filename], function(err, buffer) {
      if (!err) {
        res.end(buffer);
      }
    });
  } else {
    console.log('Serving from disk.');
    var cache = new Cache({key: filename});
    var fstream = fs.createReadStream(filename)
      .on('error', function(e) {
        console.error(e);
        res.statusCode = 404;
        res.end('Not Found');
      })

    fstream
      .pipe(zlib.createGzip())
      .pipe(cache)

    fstream
      .pipe(res)

    cache.on('finish', function() {
      console.log('Cached a new file: ', Object.keys(Cache.store));
    });
  }

};

module.exports = CacheServer;