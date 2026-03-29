groupmates = [
    {
        "name": "Данила",
        "group": "720-2",
        "age": 22,
        "marks": [2, 4, 3, 3, 5]
    },
    {
        "name": "Анна",
        "group": "720-1",
        "age": 34,
        "marks": [5, 5, 5, 5, 5]
    },
    {
        "name": "Евгений",
        "group": "720-2",
        "age": 20,
        "marks": [4, 3, 4, 4, 4]
    },
    {
        "name": "Андрей",
        "group": "720-3",
        "age": 42,
        "marks": [2, 2, 3, 3, 2]
    },
    {
        "name": "Светлана",
        "group": "720-1",
        "age": 23,
        "marks": [4, 5, 3, 4, 5]
    }
]

def print_students(students):
    print(
        f'{"Имя студента":15}',
        f'{"Группа":8}',
        f'{"Возраст":8}',
        f'{"Оценки":20}'
    )

    for student in students:
        print(
            f"{student["name"]:15}",
            f"{student["group"]:8}",
            f"{str(student["age"]):8}",
            f"{str(student["marks"]):20}"
        )
    print()

def filter_students_by_avg_mark(students, min_avg_mark):
    result = []

    for student in students:
        avg = sum(student["marks"]) / len(student["marks"])

        if avg >= min_avg_mark:
            result.append(student)

    return result
     
print_students(groupmates)
print_students(filter_students_by_avg_mark(groupmates, 4))