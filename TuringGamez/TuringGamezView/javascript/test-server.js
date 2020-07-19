
// Simple NodeJS app to test running a python app over a server
var express = require('express');
var app = express();

app.get('/', (req, res) => {
    // Spawn child process, run command line args for it
    var stuff = req.body // this is wrong

    const {spawn} = require ('child_process');
    const pyProg = spawn('python', ['test-py.py']);
    // Call one overarching python file, it delegates to the correct game file

    pyProg.stdout.on('data', function(data) {
        console.log(data.toString());
        res.write(data);
        res.end('end');
    });
});

var port = 4004
app.listen(port, () => console.log('App listening on port ${port}!'));

/* Example of what our http request body will likely look like. 
This should contain all necessary data about our game (type, inputs, etc.)
Json stuff: http-body
{
    'game-type': 'mad-libs-wiki',
    'inputs':
    {
        'level': '..',
        'song-title': '..',
        'song-artist': '...',
        'wiki-topic': '...',
        'wiki-link-count': '...',
        
    }
} */

