export default function getListStudentIds(objectList) {
  if (!Array.isArray(objectList)) {
    return [];
  }
  return objectList.map((student) => student.id);
}
