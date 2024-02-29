# Занятие 22 - Примеры категорий наследования-4

## Наследование вида

Скажем, что у нас есть отчеты для клиентов.
При этом эти отчеты могут быть нескольких типов:

- Отчеты по продажам
- Отчеты по доступности товаров
- Отчеты по поисковой выдаче

При этом, независимо от типа отчета, отчеты также могут быть:

- Ежедневные
- Еженедельные

Затруднительно выбрать главный признак (хотя интуитивно это скорее тип отчета, а не гранулярность).
Итоговая схема:

Отчет:
    - Тип отчета
    - Гранулярность отчета
    - Потенциально, другие шаги при обработке отчета, например сохранение в требуемый формат файла (под это будет выделена отдельная иерархия).

```python
"""
Иерархия Типов отчетов
"""
class ReportType(ABC):
    _QUERY = None

    def __init__(self) -> None:
        self._data = None

    @abstractmethod
    def process_type_data(self) -> None: pass

    def get_proccesed_data(self) -> pd.DataFrame: 
        return self._data


class SalesReportType(ReportType):
    _QUERY = sales_query

    def process_type_data(self) -> None:
        """Реализация обработки отчета по продажам"""


class AvailabilityReportType(ReportType):
    _QUERY = availability_query

    def process_type_data(self) -> None:
        """Реализация обработки отчета по доступности товаров"""


class SearchReportType(ReportType):
    _QUERY = search_query

    def process_type_data(self) -> None:
        """Реализация обработки отчета по поисковой выдаче"""

"""
Иерархия Гранулярности отчетов
"""

class ReportDateGranularity:

    def aggregate_report_data(self, data: pd.DataFrame) -> pd.DataFrame:


class DailyReportDateGranularity(ReportDateGranularity):

    def aggregate_report_data(self, data: pd.DataFrame) -> pd.DataFrame:
        """Реализация группировки данных по дням"""


class DailyReportDateGranularity(ReportDateGranularity):

    def aggregate_report_data(self, data: pd.DataFrame) -> pd.DataFrame:
        """Реализация группировки данных по неделям"""


"""
Основной класс
Обрабатывает отчет в соответствии с переданными параметрами
"""

class Report:
    def __init__(self, report_type: ReportType, 
                       report_granularity: ReportDateGranularity) -> None:
        self._report_type = report_type
        self._report_granularity = report_granularity

    def process_report(self) -> pd.DataFrame:
        self._report_type.process_type_data()
        raw_report = self._report_type.get_proccesed_data()
        return self._report_granularity.aggregate_report_data(raw_report)
```
