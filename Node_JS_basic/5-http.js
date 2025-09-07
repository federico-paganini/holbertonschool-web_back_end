const http = require('http');
const countStudents = require('./3-read_file_async');

const database = process.argv[2];

const app = http.createServer((_, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });

  if (_.url === '/') {
    res.end('Hello Holberton School!');
  } else if (_.url === '/students') {
    res.write('This is the list of our students\n');

    const originalLog = console.log;
    console.log = (...args) => {
      res.write(`${args.join(' ')}\n`);
    };

    countStudents(database)
      .then(() => {
        console.log = originalLog;
        res.end();
      })
      .catch(() => {
        res.end('Cannot load the database');
      });
  } else {
    res.end('Hello Holberton School!');
  }
});

app.listen(1245);

module.exports = app;
