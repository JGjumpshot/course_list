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


# new_course = Course(1,'2',1.0,1.0)
# print(type(new_course.course_number))
        