from abc import ABC, abstractmethod

import pandas as pd


class Saver(ABC):
    @abstractmethod
    def save(self) -> None: pass

class CSVSaver(Saver):
    def save(self) -> None: ...

class XLSXSaver(Saver):
    def save(self) -> None: ...

class JSONSaver(Saver):
    def save(self) -> None: ...


class AbstractSalesReport(ABC):
    _DATA_SAVED = 0
    _DATA_NOT_SAVED = 1
    _DATA_S_NIL = 2

    """
    #Конструктор
    def __init__(self, data: pd.DataFrame, save_in_xlsx: bool) -> None:
        self._data = data
        self._saver = saver
        self._save_in_xlsx = save_in_xlsx  # (True или False)

    Предположим, в начале у нас есть только 2 формата для сохранения данных в отчете по продажам
    - .csv или реже .xlsx
    Тода вроде бы логично указать булевый флажок, если нужно конкретно сохранить в .xlsx
    Но этот метод не поддерживает никакие другие методы сохранения, если такие появятся
    Тогда логично создать новую иерархию классов Saver, которые реализуют сохранение отчетов
    """

    # Конструктор
    def __init__(self, data: pd.DataFrame, saver: Saver) -> None:
        self._data = data
        self._saver = saver
        self._save_status = self._DATA_S_NIL

    # Команды
    @abstractmethod
    def save_data(self) -> None: pass

    # Запросы
    @abstractmethod
    def get_saving_status(self) -> int: pass


class SalesReport(AbstractSalesReport):

    # Команды
    def save_data(self) -> None:
        try:
            self._saver.save()
            self._save_status = self._DATA_SAVED
        except Exception as e:
            print(e)
            self._save_status = self._DATA_NOT_SAVED

    # Запросы
    def get_saving_status(self) -> int:
        return self._save_status



