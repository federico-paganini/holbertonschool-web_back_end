export default function updateStudentGradeByCity(students, city, newGrades) {
  let studentsByCity = students.filter((student) => student.location === city);
  let updatedStudents = studentsByCity.map((student) => {
    const studentNewGrade = newGrades.find(
      (grade) => grade.studentId === student.id
    );
    return {
      ...student,
      grade: studentNewGrade ? studentNewGrade.grade : "N/A",
    };
  });
  return updatedStudents;
}
