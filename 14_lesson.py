from typing import Generic, TypeVar, Self, Type
# from .general import Any


T = TypeVar('T')

class Void: pass

class Vector(Generic[T]):

    # Конструктор
    def __init__(self, values: list[Self | T]) -> None:
        self._vals = values

    # Запросы
    def __len__(self) -> int:
        return len(self._vals)

    def get_values(self) -> list[T | Self]:
        return self._vals

    # Реализация сложения 
    def __add__(self, other: Self) -> Self | Type[Void]:
        if type(other) != type(self):
            return Void
        if len(self) != len(other):
            return Void
        if len(self) == len(other) == 0:
            return Vector([])

        vals: list[Self | T] = []
        for (x, y) in zip(self.get_values(), other.get_values()):
            # Если T может складываться, то 
            if hasattr(x, '__add__') and hasattr(y, '__add__'):
                vals.append(x + y)
            # Иначе, делаем конкатенацию строкового представления
            else:
                vals.append(str(x) + str(y))

        return Vector(vals)

# In [1]: x1 = Vector([1,2])
# 
# In [2]: x2 = Vector([1,2])
# 
# In [3]: y1 = Vector([3,4])
# 
# In [5]: y2 = Vector([3,4])
# 
# In [6]: x = x1 + x2
# 
# In [7]: y = y1 + y2
# 
# In [8]: y
# Out[8]: <__main__.Vector at 0x7f771e01be10>
# 
# In [9]: y.get_values()
# Out[9]: [6, 8]
# 
# In [10]: z = x + y
# 
# In [11]: z.get_values()
# Out[11]: [8, 12]
# 

