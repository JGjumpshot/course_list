class Course:
    """course class"""
    def __init__(self, course_number, course_name, credit_hr, grade):
        self.course_number = course_number
        self.course_name = course_name
        self.credit_hr = credit_hr
        self.grade = grade

        if isinstance(self.course_number, int) is False :
            raise Exception("Integer required for course number")
        if isinstance(self.course_name, str) is False :
            raise Exception("String required for course name")
        if isinstance(self.credit_hr, float) is False :
            raise Exception("Float required for credit hours")
        if isinstance(self.grade, float) is False :
            raise Exception("Float required for grade")    

    def get_number(self):
        return self.course_number
    
    def get_name(self):
        return self.course_name
    
    def get_credit_hr(self):
        return self.credit_hr

    def get_grade(self):
        if self.grade > 4.0 or self.grade < 0.0:
            raise Exception("Grade range must be between 0.0 and 4.0")
        return self.grade
new_course = Course(2420,'Intro to Algorithms and Data structures',1.0,4.0)
print(f"{new_course.get_number()}, {new_course.get_name()}, {new_course.get_credit_hr()}, {new_course.get_grade()}")
# print(type(new_course.course_number))
        