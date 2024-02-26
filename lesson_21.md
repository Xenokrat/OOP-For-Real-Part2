# Занятие 21 - Примеры категорий наследования-3

## Пример наследования реализации

```python
from abc import ABC
from typing import Protocol


class Data(ABC): ...


class Client(Protocol):

    def execute(self, query: str, data: Data): ...


class PostgreSQLClient(Client):

    def execute(self, query: str, data: Data): 
        pass


class Queriable:

    def __init__(self, data: Data) -> None:
        self._data = data
        self._client: Client | None = None

    def execute_query(self, query: str) -> None:
        try:
            self._client.execute(query, self._data)
        except:
            print(e)
            print("This client does not support 'execute' operation")


class PostgresClient(Queriable):
    """
    Наследует от Queriable реализацию выполнения запросов,
    использует собственный клиент БД PostgreSQL
    """

    def __init__(self, data: Data) -> None:
        super().__init__(data)
        self._client = PostgreSQLClient()

```

## Пример льготного наследования


```python
import datetime


class Logger:
    """
    Базовый класс задает реализацию метода отправки логов и метод output, который должен быть
    реализован в частных подклассах
    """

    def log(self, message):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        formatted_message = f"{timestamp} - {message}"
        self.output(formatted_message)

    def output(self, message):
        raise NotImplementedError("Subclasses must implement this method.")


class ConsoleLogger(Logger):
    """
    Выводит в консоль лог
    """

    def output(self, message):
        print(f"Console: {message}")


class FileLogger(Logger):
    """
    Выводит в заданный файл
    """

    def __init__(self, file_path):
        self.file_path = file_path

    def output(self, message):
        with open(self.file_path, "a") as file:
            file.write(f"{message}\n")


class NetworkLogger(Logger):
    """
    Отправляет сообщение в сервер
    """

    def __init__(self, server_url):
        self.server_url = server_url

    def output(self, message):
        # Симулирует отправку сообщения на сервер
        print(f"Sending '{message}' to server at {self.server_url}")
```
