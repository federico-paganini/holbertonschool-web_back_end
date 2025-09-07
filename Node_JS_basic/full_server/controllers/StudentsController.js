import { readDatabase } from '../utils';

class StudentsController {
  static async getAllStudents(req, res) {
    const file = process.argv[2];

    try {
      const studentsByField = await readDatabase(file);
      /* eslint-disable */
      const sortedFields = Object.keys(studentsByField).sort((a, b) =>
        a.toLowerCase().localeCompare(b.toLowerCase()),
      );
      /* eslint-disable */

      let message = 'This is the list of our students\n';

      sortedFields.forEach((field) => {
        const listOfNames = studentsByField[field].join(', ');
        message += `Number of students in ${field}: ${studentsByField[field].length}. List: ${listOfNames}\n`;
      });

      return res.status(200).send(message);
    } catch (_err) {
      return res.status(500).send('Cannot load the database');
    }
  }

  static async getAllStudentsByMajor(req, res) {
    const file = process.argv[2];
    const { major } = req.params;

    if (major !== 'CS' && major !== 'SWE') {
      res.status(500).send('Major parameter must be CS or SWE');
    }

    try {
      const data = await readDatabase(file);
      if (!data[major]) {
        return res.status(200).send('List: ');
      }
      return res.status(200).send(`List: ${data[major].join(', ')}`);
    } catch (_err) {
      return res.status(500).send('Cannot load the database');
    }
  }
}

module.exports = StudentsController;
