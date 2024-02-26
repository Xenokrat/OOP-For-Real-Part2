# Анализ занятия 20

Ошибся при "Type variation inheritance" в плане того, как можно использовать декоратор `@overload`.
Корректный пример:

```python
class Product:
    def __init__(self, price: float, count: int) -> None:
        self._price = price

    def calcutate_sales(self, count: int) -> float:
        return self._price * count

class ProductByWeight(Product):
    @overload
    def calcutate_sales(self) -> float: ...

    def calcutate_sales(self, count: int | float) -> float:
        return self._price * count
```

На заметку, хороший пример струкрурного наследования в Python, наследование от `TypeDict`.
