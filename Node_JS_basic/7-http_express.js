const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();
const port = 1245;
const file = process.argv[2];

app.get('/', (_, res) => {
  res.type('text/plain').send('Hello Holberton School!');
});

app.get('/students', async (_, res) => {
  res.type('text/plain');
  res.write('This is the list of our students\n');

  const originalLog = console.log;
  console.log = (...args) => {
    res.write(`${args.join(' ')}\n`);
  };

  try {
    await countStudents(file);
    console.log = originalLog;
    res.end();
  } catch {
    res.end('Cannot load the database');
  }
});

app.listen(port, () => {
  console.log(`Server running in http://localhost:${port}`);
});

module.exports = app;
