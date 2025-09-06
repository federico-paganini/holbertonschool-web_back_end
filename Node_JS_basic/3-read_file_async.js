const fs = require('fs').promises;

function countStudents(path) {
  return fs.readFile(path, 'utf8')
    .then(data => {
      const lines = data.split('\n').filter(line => line.trim() !== '');
      
      if (lines.length === 0) {
        console.log('Number of students: 0');
        return;
      }

      const studentLines = lines.slice(1);

      const students = [];
      studentLines.forEach(line => {
        const cols = line.split(',');
        const student = {
          firstname: cols[0].trim(),
          lastname: cols[1].trim(),
          age: Number(cols[2].trim()),
          field: cols[3].trim()
        };
        students.push(student);
      });

      console.log(`Number of students: ${students.length}`);

      const fields = {};
      students.forEach(student => {
        if (!fields[student.field]) {
          fields[student.field] = [];
        }
        fields[student.field].push(student.firstname);
      });

      for (const field in fields) {
        const names = fields[field];
        console.log(
          `Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`
        );
      }
    })
    .catch(err => {
      throw new Error('Cannot load the database');
    });
}

module.exports = countStudents;
