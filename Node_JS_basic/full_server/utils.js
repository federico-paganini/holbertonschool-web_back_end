const fs = require('fs').promises;

async function readDatabase(filePath) {
  try {
    const data = await fs.readFile(filePath, 'utf-8');
    const lines = data.trim().split('\n');

    const studentsByField = {};

    for (let i = 1; i < lines.length; i++) {
      const fields = lines[i].split(',');
      const firstname = fields[0].trim();
      const field = fields[3].trim();

      if (!studentsByField[field]) {
        studentsByField[field] = [];
      }
      studentsByField[field].push(firstname);
    }

    return studentsByField;
  } catch (err) {
    return Promise.reject(err);
  }
}

module.exports = { readDatabase };
