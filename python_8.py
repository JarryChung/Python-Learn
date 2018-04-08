# -*- coding: utf-8 -*-


class Student(object):

    name = 'Student'        # 类属性

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

        def get_name(self):
            return self.__name

        def get_score(self):
            return self.__score

        def set_score(self, score):
            if 0 <= score <= 100:
                self.__score = score
            else:
                raise ValueError('bad score')

    def print_score(self):
        print('%s : %s' % (self.__name, self.__score))

    def get_grade(self):
        if self.__score > 90:
            print('A')
        elif self.__score > 60:
            print('B')
        else:
            print('C')




stu = Student('Zhaung', 99)
stu.print_score()
stu.get_grade()
