if __name__ == '__main__':
    number_of_students = int(input())
    assert type(number_of_students) == int, "Number of students is not an integer."
    assert 2 <= number_of_students <= 5, "Number of students is not between 2 and 5"

    students = []

    for s in range(number_of_students):
        thisStudent = []
        name = input()
        assert type(name) == str, "Name is not a string."
        score = float(input())
        assert type(score) == float, "Score is not a float."
        thisStudent.append(score)
        thisStudent.append(name)
        students.append(thisStudent)

    scoresOnly = set()
    for ss in range(0, len(students)):
        for cc in range(0, 1):
            scoresOnly.add(students[ss][cc])
    scoresOnly = list(scoresOnly)
    scoresOnly.sort()
    secondLowestGrade = scoresOnly[1]

    studentsWithSecondLowest = []
    for ss in range(0, len(students)):
        for cc in range(0, 1):
            if students[ss][cc] == secondLowestGrade:
                studentsWithSecondLowest.append(students[ss][cc+1])

    studentsWithSecondLowest.sort()
    for hh in range(0, len(studentsWithSecondLowest)):
        print((studentsWithSecondLowest[hh]))
