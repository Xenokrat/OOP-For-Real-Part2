# Занятие 20 - Примеры категорий наследования-2

## Наследования вариаций

### Наследование с функциональной вариацией (functional variation inheritance)

Пример: бэкэнд программист и фротнэнд программист - наследники класса программист, однако каждый из них переопределяет метод
написания кода.

```python
class Programmer:
    def write_code(self):
        print("Writes code")

class BackendProgrammer(Programmer):
    @override
    def write_code(self):
        print("Writes backend code")

class FronendProgrammer(Programmer):
    @override
    def write_code(self):
        print("Writes frontend code")
```

### Наследование с вариацией типа (type variation inheritance)

Классический пример, разница при расчете площади для различных фигур, которые наследуют от общего предка Shape.
(p.s. линтеру в Python не нравится переопределение сигнатуры функции, и я не нашел способ переубедить его в обратном).

```python
class Shape:
    def get_square(self) -> None:
        pass

class Circle(Shape):

    @override
    def get_square(self, radius: float) -> None:
        return 3.14 * radius**2

class Rectangle(Shape):

    @override
    def get_square(self, height: float, width) -> None:
        return height * width
```

## Наследование с конкретизацией (reification inheritance)

Пример: имеем абстрактный класс для Клиента Баз данных, который не содержит реализаций методов подключения и выполнения запросов.
От него можно наследовать уже конкретные клиенты, с реализованными методами, специфичными для каждой БД.

```python
class AbstractDBClient(ABC):
    @abstractmethod
    def connect(self) -> None:
        pass

    @abstractmethod
    def execute_query(self, query: str) -> None:
        pass


class PostgreSQLClient(AbstractDBClient):
    def connect(self) -> None:
        # реализация
        ...

    def execute_query(self, query: str) -> None:
        # реализация
        ...

class MySQLClient(AbstractDBClient):
    def connect(self) -> None:
        # реализация
        ...

    def execute_query(self, query: str) -> None:
        # реализация
        ...
```

## Структурное наследование

Пример из документации к Django, который активно использует миксины, чтобы реализовать ту или иную функциональность:

- `SingleObjectMixin` добавляет механизм, который позволяет ассоциировать объект с текущим HTTP-запросом.
- `View` базовый класс для создания вью в Django.

```python
class RecordInterestView(SingleObjectMixin, View):
    model = Author

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        return HttpResponseRedirect(
            reverse("author-detail", kwargs={"pk": self.object.pk})
        )
```
