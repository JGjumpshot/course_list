class Course:
    """course class"""
    def __init__(self, course_number=1200, course_name="Partying", credit_hrs=2.0, grade=4.0, next_node=None):
        self.course_number = course_number
        self.course_name = course_name
        self.credit_hrs = credit_hrs
        self.grade = grade
        self.next_node = next_node

        if isinstance(self.course_number, int) is False :
            raise Exception("Integer required for course number")
        if isinstance(self.course_name, str) is False :
            raise Exception("String required for course name")
        if isinstance(self.credit_hrs, float) is False :
            raise Exception("Float required for credit hours")
        if isinstance(self.grade, float) is False :
            raise Exception("Float required for grade")    

    def get_number(self):
        return self.course_number
    
    def get_name(self):
        return self.course_name
    
    def get_credit_hrs(self):
        return self.credit_hrs

    def get_grade(self):
        if self.grade > 4.0 or self.grade < 0.0:
            raise Exception("Grade range must be between 0.0 and 4.0")
        return self.grade
    def __str__(self):
        return f"cs{self.course_number} {self.course_name} Grade: {self.grade} Credit Hours: {self.credit_hrs}"
    # def get_next(self):
    #     self.next_node
    # def set_next(self, next_node):
    #     self.next_node = next_node

# new_course = Course(2420,'Intro to Algorithms and Data structures',1.0,4.0)
# print(new_course)
# test = open("data.txt", "r")
# print(test.readlines())
# print(new_course.__str__())
# print(type(new_course.course_number))
        