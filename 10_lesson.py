"""
Вариант 1

Используя ключевое слово `final` из модуля `typing`.
Плюсы: Легко использовать
Минусы: Не запрещает перегрузку в рантайме, лишь помогает линтеру указать на ошибку.
"""

from typing import final


class Animal:
    @final
    def eat(self) -> None: ...


class Cat(Animal):
    def eat(self) -> None: ...
    # Method "eat" cannot override final method defined in class Animal


"""
Вариант 2

Используя метакласс
Плюсы: Вызовет ошибку в рантайме при попытке перезаписи
Минусы: много дополнительного когда, не "питоновский" подход
запрещающий перезапись
"""

def non_overridable(f):
    f.non_overridable = True
    return f


def get_non_overridables(bases):
    ret = []
    for source in bases:
        for name, attr in source.__dict__.items():
            if getattr(attr, "non_overridable", False):
                ret.append(name)
        ret.extend(get_non_overridables(source.__bases__))
    return ret


class NonOverridable(type):
    def __new__(cls, name, bases, dct):
        non_overridables = get_non_overridables(bases)
        for name in dct:
            if name in non_overridables:
                raise Exception("You can not override %s, it is non-overridable" % name)
        return type.__new__(cls, name, bases, dct)


class Employee(metaclass=NonOverridable):
    @non_overridable
    def pay_salary(self) -> None: ...


class Programmer(Employee):
    def pay_salary(self) -> None: ...
    # Вызовет исключение 
    # Exception: You can not override pay_salary, it is non-overridable
