class Course:
    """course class"""
    def __init__(self,course_number=1100,course_name="",credit_hrs=0.0,grade=0.0,next_node=None):
        """init function"""
        self.course_number = course_number
        self.course_name = course_name
        self.credit_hrs = credit_hrs
        self.grade_pts = grade
        self.next_node = next_node

        if isinstance(self.course_number, int) is False:
            raise ValueError("Integer required for course number")
        if self.course_number < 0:
            raise ValueError("Must be a non-negative course number")
        if isinstance(self.course_name, str) is False :
            raise ValueError("String required for course name")
        if isinstance(self.credit_hrs, float) is False :
            raise ValueError("Float required for credit hours")
        if self.credit_hrs < 0.0:
            raise ValueError("credit hrs should be a non-negative number")
        if isinstance(self.grade_pts, float) is False :
            raise ValueError("Float required for grade")
        if self.grade_pts < 0.0 or self.grade_pts > 4.0:
            raise ValueError("Please enter valid grade points")

    def number(self):
        """return course number"""
        return self.course_number
    def name(self):
        """return name"""
        return self.course_name
    def credit_hr(self):
        """return credit_hr"""
        return self.credit_hrs
    def grade(self):
        """return grade"""
        if self.grade_pts > 4.0 or self.grade_pts < 0.0:
            raise Exception("Grade range must be between 0.0 and 4.0")
        return self.grade_pts
    def __str__(self):
        """return string"""
        return f"cs{self.course_number}{self.course_name}Grade: {self.grade_pts}Credit Hours:{self.credit_hrs}"
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
        