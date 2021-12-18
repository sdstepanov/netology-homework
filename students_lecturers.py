class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lec(self, lec, course, grade):
        if isinstance(lec, Lecturer) and course in self.courses_in_progress and course in lec.courses_attached:
            if course in lec.grades:
                lec.grades[course] += [grade]
            else:
                lec.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _avg_grade(self, sum_grade=0, len_grade=0):
        for course in self.grades:
            for grade in self.grades[course]:
                sum_grade += grade
                len_grade += 1
        res = round(sum_grade / len_grade, 1)
        return res

    def __str__(self):
        res = '\n'.join((
            f'Имя: {self.name}',
            f'Фамилия: {self.surname}',
            f'Средняя оценка за домашнее задание: {self._avg_grade()}',
            f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}',
            f'Завершенные курсы: {", ".join(self.finished_courses)}'))
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            return 'Ошибка'
        else:
            return self._avg_grade() < other._avg_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            return 'Ошибка'
        else:
            return self._avg_grade() == other._avg_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _avg_grade(self, sum_grade=0, len_grade=0):
        for course in self.grades:
            for grade in self.grades[course]:
                sum_grade += grade
                len_grade += 1
        res = round(sum_grade / len_grade, 1)
        return res

    def __str__(self):
        res = '\n'.join((
            f'Имя: {self.name}',
            f'Фамилия: {self.surname}',
            f'Средняя оценка за лекции: {self._avg_grade()}'))
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Ошибка'
        else:
            return self._avg_grade() < other._avg_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return 'Ошибка'
        else:
            return self._avg_grade() == other._avg_grade()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = '\n'.join((
            f'Имя: {self.name}',
            f'Фамилия: {self.surname}'))
        return res


student_1 = Student('Roy', 'Eman', 'your_gender')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['GIT']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Karel', 'Ray', 'your_gender')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Java script']
student_2.finished_courses += ['Введение в программирование']

students_list = [student_1, student_2]

lecturer_1 = Lecturer('Sam', 'Colin')
lecturer_1.courses_attached += ['Python']
lecturer_1.courses_attached += ['GIT']

lecturer_2 = Lecturer('Bob', 'Fisher')
lecturer_2.courses_attached += ['Python']
lecturer_2.courses_attached += ['Java script']

lecturers_list = [lecturer_1, lecturer_2]

reviewer_1 = Reviewer('Some', 'Buddy')
reviewer_1.courses_attached += ['Python']

reviewer_2 = Reviewer('Jack', 'Peterson')
reviewer_2.courses_attached += ['GIT']

reviewer_3 = Reviewer('Tom', 'Miller')
reviewer_3.courses_attached += ['Java script']

reviewer_1.rate_hw(student_1, 'Python', 8)
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_2.rate_hw(student_1, 'GIT', 8)
reviewer_2.rate_hw(student_1, 'GIT', 10)

reviewer_1.rate_hw(student_2, 'Python', 8)
reviewer_1.rate_hw(student_2, 'Python', 10)
reviewer_3.rate_hw(student_2, 'Java script', 10)
reviewer_3.rate_hw(student_2, 'Java script', 10)

student_1.rate_lec(lecturer_1, 'Python', 9)
student_1.rate_lec(lecturer_1, 'Python', 10)
student_1.rate_lec(lecturer_1, 'GIT', 10)
student_1.rate_lec(lecturer_1, 'GIT', 8)
student_2.rate_lec(lecturer_1, 'Python', 10)
student_2.rate_lec(lecturer_1, 'Python', 9)

student_1.rate_lec(lecturer_2, 'Python', 10)
student_1.rate_lec(lecturer_2, 'Python', 8)
student_2.rate_lec(lecturer_2, 'Python', 9)
student_2.rate_lec(lecturer_2, 'Python', 8)
student_2.rate_lec(lecturer_2, 'Java script', 10)
student_2.rate_lec(lecturer_2, 'Java script', 8)


def student_avg_grade(students, course):
    sum_grades = 0
    len_grades = 0
    for student in students:
        if course in student.courses_in_progress:
            for grade in student.grades[course]:
                sum_grades += grade
                len_grades += 1
    res = round(sum_grades / len_grades, 1)
    return res


def lecturer_avg_grade(lecturers, course):
    sum_grades = 0
    len_grades = 0
    for lecturer in lecturers:
        if course in lecturer.courses_attached:
            for grade in lecturer.grades[course]:
                sum_grades += grade
                len_grades += 1
    res = round(sum_grades / len_grades, 1)
    return res


# print(student_1)
# print(student_1.grades)
# print(student_2)
# print(student_2.grades)
# print(lecturer_1)
# print(lecturer_1.grades)
# print(lecturer_2)
# print(lecturer_2.grades)
# print(reviewer_1)
# print(reviewer_2)
# print(student_1 < student_2)
# print(student_1 > student_2)
# print(student_1 == student_2)
# print(lecturer_1 < lecturer_2)
# print(lecturer_1 > lecturer_2)
# print(lecturer_1 == lecturer_2)
# print(f'Средняя оценка за д/з курса "Python": {student_avg_grade(students_list, "Python")}')
# print(f'Средняя оценка за д/з курса "GIT": {student_avg_grade(students_list, "GIT")}')
# print(f'Средняя оценка за д/з курса "Java script": {student_avg_grade(students_list, "Java script")}')
# print(f'Средняя оценка за лекции курса "Python": {lecturer_avg_grade(lecturers_list, "Python")}')
# print(f'Средняя оценка за лекции курса "Python": {lecturer_avg_grade(lecturers_list, "GIT")}')
# print(f'Средняя оценка за лекции курса "Python": {lecturer_avg_grade(lecturers_list, "Java script")}')
