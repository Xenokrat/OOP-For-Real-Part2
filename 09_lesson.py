from abc import ABC, abstractmethod
from typing import Self, Type
from copy import deepcopy
import pickle


class General(ABC):
    """
    Укажем как унаследованный от Object для наглядности,
    хотя в современном Python обычно опускают это
    """

    # Клонирование
    def _copy(self, other) -> Self: 
        # ничего лучше не придумал
        other.__dict__ = deepcopy(self.__dict__)

    # Клонирование
    def _clone(self) -> Self:
        return deepcopy(self)

    # Сравнение
    def __eq__(self, other) -> bool: return self == other
    def __lt__(self, other) -> bool: return self <  other
    def __le__(self, other) -> bool: return self <= other
    def __gt__(self, other) -> bool: return self >  other
    def __ge__(self, other) -> bool: return self >= other

    # Печать
    def __repr__(self) -> str: return f"{self.__class__}"

    # Сериализация
    def serialize(self) -> bytes:
        return pickle.dumps(self)

    def deserialize(self, bts: bytes) -> Self:
        return pickle.loads(bts)

    # Проверка типа
    def __instancecheck__(self, instance) -> bool:
        return isinctanse(self, instance)

    # получение реального типа объекта
    def _get_class(self) -> Type[Self]:
        # Специального дандр метода под это врое бы нет в Python
        return self.__class__


class Any(General): pass
