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
    # iter_linked_list = linked_list.__iter__()
    # print(iter_linked_list.__next__())
    # print(linked_list.get_size())
    my_list = linked_list
    # print(my_list.__iter__().head.name())
    # print(my_list.__iter__().head.name())
    # print(my_list.__iter__().head.name())
    for i in my_list:
        print(i)
if __name__ == "__main__":
    main()
