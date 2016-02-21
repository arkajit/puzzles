var events = require('events');

var bar = new events.EventEmitter();

bar.on('start', function(task) {
  console.log('Starting progress bar for ' + task + '.');
});

bar.on('progress', function(task, pct) {
  console.log('Task: ' + task + '(' + pct.toFixed(2) + '%)');
});

bar.on('end', function() {
  console.log('Finished.');
});

bar.on('end', function(task) {
  console.log('Task finished: ' + task);
});

bar.emit('start', 'Download');
bar.emit('progress', 'Download', 31.2524);
bar.emit('progress', 'Download', 72.1351);

bar.removeAllListeners('progress');

bar.emit('progress', 'Download', 95.923);
bar.emit('end', 'Download');
