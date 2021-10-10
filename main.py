"""main module"""
import random
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
    # random.seed(0)
    # cl = CourseList()
    # for _ in range(37):
    #     cl.insert(Course(random.randrange(1000, 7000), "test", 1.0, 2.0))
    # iter_linked_list = linked_list.__iter__()
    # print(iter_linked_list.__next__())
    # print(linked_list.get_size())
    my_list = linked_list
    print(my_list)
    # for i in my_list:
    #     print(i)

if __name__ == "__main__":
    main()
