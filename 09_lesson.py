from abc import ABC, abstractmethod
from typing import Self


class General(ABC):
    """
    Укажем как унаследованный от Object для наглядности,
    хотя в современном Python обычно опускают это
    """

    def _copy(self) -> Self: 
        

    def _clone(sefl) -> Self: pass

    # Сравнение
    def __eq__(self, other) -> bool: return self == other
    def __lt__(self, other) -> bool: return self <  other
    def __le__(self, other) -> bool: return self <= other
    def __gt__(self, other) -> bool: return self >  other
    def __ge__(self, other) -> bool: return self >= other

    # Печать
    def __repr__(self) -> str: return f"{self.__class__}"
    def __str__(self) -> str: return f"{self.__class__}"


    # Проверка типа
    def __instancecheck__(self, instance) -> bool:
        return isinctanse(self, instance)

    # получение реального типа объекта
    def _get_class(self) -> Self:
        # Специального дандр метода под это врое бы нет в Python
        return self.__class__


class Any(General): pass
