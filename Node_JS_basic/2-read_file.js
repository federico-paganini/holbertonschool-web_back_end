// 2-read_file.js
const fs = require('fs');

function countStudents(path) {
  let data;
  try {
    data = fs.readFileSync(path, 'utf8');
  } catch (err) {
    throw new Error('Cannot load the database');
  }

  const lines = data.split('\n').filter((line) => line.trim() !== '');

  if (lines.length === 0) {
    console.log('Number of students: 0');
    return;
  }

  const students = lines.slice(1);

  const fields = {};

  students.forEach((student) => {
    const cols = student.split(',');
    const firstname = cols[0].trim();
    const field = cols[3].trim();
    if (!fields[field]) fields[field] = [];
    fields[field].push(firstname);
  });

  const total = students.length;
  console.log(`Number of students: ${total}`);

  for (const [field, names] of Object.entries(fields)) {
    console.log(
      `Number of students in ${field}: ${names.length}. List: ${names.join(
        ', '
      )}`
    );
  }
}

module.exports = countStudents;
