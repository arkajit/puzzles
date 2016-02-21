/**
 * A simple progress bar which counts by one from `opts.start` to
 * `opts.limit`.
 *
 * It emits the following events:
 *   - `start`: when the task starts
 *   - `progress`: on every `opts.every` ticks (an increment in progress)
 *   - `end`: when the task ends
 */
function ProgressBar(task, opts) {
  this.task = task;
  var opts = opts || {};

  this.count = opts.start || 1;
  this.limit = opts.limit || 100;
  this.every = opts.every || 10;

  this.callbacks = {
    'start':    null,
    'progress': null,
    'end':      null
  };
};

ProgressBar.prototype.on = function(evt, callback) {
  if (this.callbacks.hasOwnProperty(evt)) {
    console.log('Registered callback for event: ' + evt);
    this.callbacks[evt] = callback;
  } else {
    console.log('Unrecognized event: ' + evt);
  }

  return this;
};

ProgressBar.prototype.tick = function() {
  if (this.count === this.limit) {
    if (this.callbacks['end']) {
      this.callbacks['end']();
    }
  } else {
    this.count += 1;
    if (this.count % this.every === 0) {
      if (this.callbacks['progress']) {
        var pct = (this.count / this.limit) * 100;
        this.callbacks['progress'](this.count, pct);
      }
    }

    this.tick();
  }
};

ProgressBar.prototype.start = function() {
  if (this.callbacks['start']) {
    this.callbacks['start']();
  }
  this.tick();
};

var bar = new ProgressBar('Download', {limit: 150, every: 13});
bar
  .on('start', function() {
    console.log('Task ' + bar.task + ' has started.');
  })
  .on('progress', function(count, pct) {
    console.log('Task ' + bar.task + ' is ' + pct.toFixed(2) + '% finished.');
  })
  .on('end', function() {
    console.log('Task ' + bar.task + ' has finished.');
  });

bar.start();

