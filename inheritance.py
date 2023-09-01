class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        return f"Name: {self.name}, Age:  {self.age}"


class Student(Person):
    def __init__(self, student_id, name, age):
        super().__init__(name, age)
        self.student_id = student_id
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)

    def list_course(self):
        return self.courses

class Teacher(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.courses_taught = []

    def assign_course(self, course):
        self.courses_taught.append(course)

    def list_courses_taught(self):
        return self.courses_taught

class Course:
    def __init__(self, course_name, course_code):
        self.course_name = course_name
        self.course_code = course_code


student1 = Student("S1", "Mike", 15 )
student2 = Student("S2", "Ian", 12 )

teacher1 = Teacher("Mr Albert", 35, "T1")
teacher2 = Teacher("Mrs Edwinna", 30, "T2")

course1 = Course("Software Engineering", "STDF4")
course2 = Course("Data Science", "DTS3")

student1.enroll(course1)
student1.enroll(course2)
student2.enroll(course2)

teacher1.assign_course(course2)
teacher2.assign_course(course1)

print(f"{student1.name} is enrolled in: {student1.list_course()}")
print(f"{teacher1.name} teaches {teacher1.list_courses_taught()}")

