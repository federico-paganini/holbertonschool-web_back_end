const express = require('express');
const app = express();
const port = 1245;

app.get('/', (_, res) => {
  res.type('text/plain').send('Hello Holberton School!');
});

app.listen(port, () => {
  console.log(`Server running in http://localhost:${port}`);
});

module.exports = app;
