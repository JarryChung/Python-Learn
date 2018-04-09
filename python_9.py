# -*- coding: utf-8 -*-

from types import MethodType


class Students(object):         # 先定义类
    __slots__ = ('name', 'age', '_score', 'set_age', 'set_score')  # 用tuple定义允许绑定的属性方法名称

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


s = Students()
s.name = 'JarryChung'           # 给实例绑定属性
print(dir(s))                   # 查看实例ｓ含有的方法与属性


def set_age(self, age):
    self.age = age


s.set_age = MethodType(set_age, s)  # 给实例绑定方法
print(dir(s))                       # 查看实例ｓ含有的方法与属性


def set_score(self, score):
    self.score = score


Students.set_score = set_age        # 给类绑定方法
print(dir(Students))                # 查看类Students含有的方法与属性


s.score = 99
print(s.score)
