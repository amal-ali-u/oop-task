class Student:
    def __init__(self, student_name):
        self.student_name = student_name
        print(f"Student name:{student_name}")

class Teacher:
    def __init__(self, teacher_name):
        self.teacher_name = teacher_name
        print(f"Teacher name:{teacher_name}")

class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        print(f"Course name:{course_name}")
class School(Student, Teacher, Course):
    def __init__(self, student_name, teacher_name, course_name, school_name):
        super().__init__(student_name)
        self.school_name = school_name
        print(f"School name :{school_name}")
school = School( "Mohamed",'amal' ,"Programming", "Hope School")
