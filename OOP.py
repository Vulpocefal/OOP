class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        """Средняя оценка лектора"""
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def calculate_average_grade(self):
        """Средняя оценка студента"""
        all_grades = []
        for course in self.grades:
            all_grades.extend(self.grades[course])
        return round(sum(all_grades) / len(all_grades), 1) if all_grades else 0

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.calculate_average_grade() < other.calculate_average_grade()

    def __le__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.calculate_average_grade() <= other.calculate_average_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.calculate_average_grade() == other.calculate_average_grade()

    def __str__(self):
        average_grade = self.calculate_average_grade()
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        return (f'Имя: {self.name}\nФамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {average_grade}\n'
                f'Курсы в процессе изучения: {courses_in_progress}\n'
                f'Завершенные курсы: {finished_courses}')

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        average_grade = self.calculate_average_grade()
        return (f'Имя: {self.name}\nФамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {average_grade}')

    def calculate_average_grade(self):
        """Средняя оценка лекторов"""
        all_grades = []
        for course in self.grades:
            all_grades.extend(self.grades[course])
        return round(sum(all_grades) / len(all_grades), 1) if all_grades else 0

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.calculate_average_grade() < other.calculate_average_grade()

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.calculate_average_grade() <= other.calculate_average_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.calculate_average_grade() == other.calculate_average_grade()

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

# Студенты, лекторы, проверяющие
student1 = Student('Алёхина', 'Ольга', 'Ж')
student2 = Student('Александр', 'Александров', 'М')

lecturer1 = Lecturer('Иван', 'Иванов')
lecturer2 = Lecturer('Пётр', 'Петров')

reviewer1 = Reviewer('Some', 'Buddy')
reviewer2 = Reviewer('John', 'Doe')

# Курсы
student1.courses_in_progress += ['Python', 'Git']
student2.courses_in_progress += ['Python', 'Git']

student1.finished_courses += ['Введение в программирование']
student2.finished_courses += ['Введение в программирование']

lecturer1.courses_attached += ['Python', 'Git']
lecturer2.courses_attached += ['Python', 'Git']

reviewer1.courses_attached += ['Python', 'Git']
reviewer2.courses_attached += ['Python', 'Git']

# Оценки за лекции
student1.rate_lecture(lecturer1, 'Python', 7)
student1.rate_lecture(lecturer1, 'Python', 8)
student1.rate_lecture(lecturer1, 'Python', 9)

student2.rate_lecture(lecturer2, 'Python', 6)
student2.rate_lecture(lecturer2, 'Python', 7)
student2.rate_lecture(lecturer2, 'Python', 8)

# Оценки за д.з.
reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Git', 8)

reviewer2.rate_hw(student2, 'Python', 7)
reviewer2.rate_hw(student2, 'Python', 8)
reviewer2.rate_hw(student2, 'Git', 9)

print(student1)
print(student2)
print(lecturer1)
print(lecturer2)
print(reviewer1)
print(reviewer2)

students = [student1, student2]
lecturers = [lecturer1, lecturer2]

def calculate_average_homework_grade(students, course):
    """Средняя оценка за д.з. по всему курсу"""
    all_grades = []
    for student in students:
        if course in student.grades:
            all_grades.extend(student.grades[course])
    return round(sum(all_grades) / len(all_grades), 1) if all_grades else 0

def calculate_average_lecture_grade(lecturers, course):
    """Средняя оценка за лекции по всему курсу"""
    all_grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            all_grades.extend(lecturer.grades[course])
    return round(sum(all_grades) / len(all_grades), 1) if all_grades else 0

print(f'Средняя оценка за домашние задания по курсу "Python": {calculate_average_homework_grade(students, "Python")}')
print(f'Средняя оценка за лекции по курсу "Python": {calculate_average_lecture_grade(lecturers, "Python")}')