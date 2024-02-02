from abc import ABC
from typing import Self, Type, final, TypeVar
from copy import deepcopy
import pickle


_T = TypeVar('_T')

class Void: ...

class General(ABC):
    _COPY_NIL = 0
    _COPY_OK  = 1
    _COPY_ERR = 2

    # Попытка присваивания (Команда)
    @classmethod
    def assigment_attempt(cls, target: object, source: bytes) -> Self | Type[Void]:
        if isinstance(target, cls) and isinstance(source, cls):
            target.value = source.value
            return target
        return Void


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
