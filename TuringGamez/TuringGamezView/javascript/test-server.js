
// Simple NodeJS app to test running a python app over a server
/*const express = require('express');
const app = express();

app.get('/', (req, res) => {
    // Spawn child process, run command line args for it
    //var stuff = req.body // this is wrong

    const {spawn} = require ('child_process');
    const pyProg = spawn('python', ['__main__.py', '-h']);
    // Call one overarching python file, it delegates to the correct game file

    pyProg.stdout.on('data', function(data) {
        console.log(data.toString());
        res.write(data);
        res.end('end');
    });
});

app.listen(3000, () => console.log('App listening on port ${port}!'));*/

const express = require('express');
const app = express();
const path = require('path')


const static_path = path.join(__dirname + '/..')
console.log(static_path)
app.use('/home/', express.static(static_path)); //TuringGamezView/ directory
app.get('/', (req, res) => {
    // Default URL redirects to the main page of our program
    //res.redirect(`http://localhost:${port}/TuringGamez.html`);
    res.redirect(`http://localhost:${port}/home/html/TuringGamez.html`);
    res.end();


    /*const {spawn} = require ('child_process');
    const pyProg = spawn('python', ['../../python/__main__.py', '-h']);

    pyProg.stdout.on('data', function(data) {
        console.log(data.toString());
        res.write(data);
        res.end('end');
    });*/
});

app.post(/\w+/, (req, res) => {
    console.log(`A post request occurred on: ${req.url}`)
    console.log(`Request content: ${req.body}`)
});


const port = 3000;
const liveServer = app.listen(port, () => console.log(`Server live on port ${port}.`));
/**
 * These kill the server (or... should.)
 */
/*process.on('SIGTERM', () => {
    liveServer.close(() => {
        console.log(`Server process on port ${port} terminated.`);
    });
});
/*process.on('SIGKILL', () => {
    liveServer.close(() => {
        console.log(`Server process on port ${port} killed.`);
    });
});
*/

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

