var PythonShell = require('python-shell');

var options = {
  args: ['Windows', '8', 'Chrome', '', '']
};

PythonShell.run('TestRunner.py', options, function (err, results) {
  if (err) throw err;
  
  console.log('results: %j', results);
});