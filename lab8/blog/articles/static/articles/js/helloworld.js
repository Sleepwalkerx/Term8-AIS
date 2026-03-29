const groupmates = [
    {
        name: "Данила",
        group: "720-2",
        age: 22,
        marks: [2, 4, 3, 3, 5]
    },
    {
        name: "Анна",
        group: "720-1",
        age: 34,
        marks: [5, 5, 5, 5, 5]
    },
    {
        name: "Евгений",
        group: "720-2",
        age: 20,
        marks: [4, 3, 4, 4, 4]
    },
    {
        name: "Андрей",
        group: "720-3",
        age: 42,
        marks: [2, 2, 3, 3, 2]
    },
    {
        name: "Светлана",
        group: "720-1",
        age: 23,
        marks: [4, 5, 3, 4, 5]
    }
];

function rpad(str, length) {
    str = String(str);

    while (str.length < length) {
        str += " ";
    }

    return str;
}

function printStudents(students) {
    console.log(
        rpad("Имя студента", 15),
        rpad("Группа", 10),
        rpad("Возраст", 10),
        rpad("Оценки", 20)
    );

    for (let i = 0; i < students.length; i++) {
        console.log(
            rpad(students[i].name, 15),
            rpad(students[i].group, 10),
            rpad(students[i].age, 10),
            rpad(students[i].marks.join(", "), 20)
        );
    }

    console.log("\n");
}

function filterStudentsByGroup(students, groupName) {
    const result = [];

    for (let i = 0; i < students.length; i++) {
        if (students[i].group === groupName) {
            result.push(students[i]);
        }
    }

    return result;
}

console.log("Все студенты:");
printStudents(groupmates);

console.log("Студенты группы 912-1:");
printStudents(filterStudentsByGroup(groupmates, "720-1"));