function getEmployeesData(employeesNames) {
    const employeesData = [];

    for (const nameEmployee of employeesNames) {
        employeesData.push({
            name: nameEmployee,
            number: nameEmployee.length
        });
    }
    employeesData.forEach((employee) =>
        console.log(`Name: ${employee.name} -- Personal Number: ${employee.number}`));
}

getEmployeesData([
    'Silas Butler',
    'Adnaan Buckley',
    'Juan Peterson',
    'Brendan Villarreal'
])

getEmployeesData([
    'Samuel Jackson',
    'Will Smith',
    'Bruce Willis',
    'Tom Holland'
])