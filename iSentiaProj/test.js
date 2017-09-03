var PythonShell = require('python-shell');


var options = {
	
	/* 
		arguments for WEB application: 	
		the options take 6 parameters for setting up the test environment
		and the sequence is args: [APPLICATION, OS, OS_VERSION, BROWSER, BROWSER_VERSION, HOST("http://www.isentia.com" if empty)] 
	*/
		
	args: ['Web', 'Windows', '8', 'Chrome', '', '']	// Chrome latest, windows 8
	//args: ['Web', 'Windows', '8', 'IE', '10', ''] // IE 10, Windows 8
	//args: ['Web', 'OS X', 'Sierra', 'Safari', '', ''] // Safari latest, Mac OS latest
	
	/* 
		arguments for MOBILE application: 	
		the options take 5 parameters for setting up the test environment
		and the sequence is args: [APPLICATION, OS, DEVICE, REAL_MOBILE, APPIUM_VERSION, HOST("http://www.isentia.com" if empty)]
	*/

	//args: ['Mobile', 'Android', 'Samsung Galaxy S6', 'true', '1.4.16', ''] // Android 

	
};

PythonShell.run('TestRunner.py', options, function (err, results) {
  if (err) throw err;
  
  console.log('results: %j', results);
});