export default function updateStudentGradeByCity(students, city, newGrades) {
  let studentsByCity = students.filter((student) => student.location === city);
  let updatedStudents = studentsByCity.map((student) => {
    return {
      ...student,
      grade: student.id in newGrades ? newGrades[student.id] : "N/A",
    };
  });
  return updatedStudents;
}
