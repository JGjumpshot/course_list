"""main module"""
from course import Course
from courselist import CourseList

def main():
    """main function"""
    linked_list = CourseList()
    test = open("data.txt", "r", encoding='utf-8')
    for i in test.readlines():
        course = i.strip().split(',')
        course = Course(int(course[0]), course[1], float(course[2]), float(course[3]))
        linked_list.insert(course)
    my_list = linked_list
    print(my_list)
    print(f"\n\n Cumulative GPA: {round(my_list.calculate_gpa(), 3)}")

if __name__ == "__main__":
    main()
