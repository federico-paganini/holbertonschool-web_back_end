export default function createReportObject(employeesList) {
  data = {
    allEmployees: employeesList,

    getNumberOfDepartments() {
      return Object.keys(this.allEmployees).length;
    },
  };
}
