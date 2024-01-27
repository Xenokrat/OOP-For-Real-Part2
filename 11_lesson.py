from abc import ABC
from typing import Self, Type, final, TypeVar
from copy import deepcopy
import pickle


_T = TypeVar('_T')


class General(ABC):
    _COPY_NIL = 0
    _COPY_OK  = 1
    _COPY_ERR = 2

    # Вспомогательные
    def __get_not_status_attrs(self) -> set[str]:
        return set(
            attr for attr in dir(self)
            if not attr.endswith('status')
        )

    # Конструктор
    def __init__(self, *args, **kwargs) -> None:
        self._copy_status = self._COPY_NIL

    # Команды
    @final
    def copy_to(self, other: _T) -> None: 
        fields_to_copy = self.__get_not_status_attrs()
        if not all((hasattr(a, other) for a in fields_to_copy)):
            self._copy_status = self._COPY_ERR
            return

        for a in fields_to_copy:
            setattr(other, a, deepcopy(getattr(self, a)))

        self._copy_status = self._COPY_OK

    # Запросы
    # Клонирование
    @final
    def clone(self) -> Self:
        return deepcopy(self)

    # Сравнение
    @final
    def __eq__(self, other) -> bool:
        return self.__dict__ == other.__dict__

    # Печать
    @final
    def __repr__(self) -> str: return f"{self.__class__}"

    # Сериализация
    @final
    def serialize(self) -> bytes:
        return pickle.dumps(self)

    @final
    @classmethod
    def deserialize(cls, bts: bytes) -> Self:
        return pickle.loads(bts)

    # Проверка типа
    @final
    def __instancecheck__(self, instance) -> bool:
        return isinstance(self, instance)

    # получение реального типа объекта
    @final
    def get_class(self) -> Type[Self]:
        return self.__class__


class Any(General): pass


class Employee(Any):
    def get_salary(self) -> None: ...


class Programmer(Employee):
    def write_program(self) -> None: ...


class Accountant(Employee):
    def calc_salary(self) -> int: ...


class Manager(Employee):
    def add_task_to_backlog(self) -> None: ...


class Void(Programmer, Accountant, Manager): ...


if __name__ == "__main__":
    manager = Manager()
    accountant = Accountant()
    programmer = Programmer()

    list_of_employees: list[Employee] = [manager, accountant, programmer]

    # Предположим, что программиста уволили
    programmer = Void

    # Обратим внимание, что линтер не выдает ошибок здесь, так как programmer все еще наследник Programmer
    # и список работников корректен
    # хотя программист равен теперь типу Void;

    # Получение ЗП
    for emp in list_of_employees:
        if emp != Void:
            emp.get_salary()

