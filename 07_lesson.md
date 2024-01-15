# Приведите пример кода с комментариями, где применяется динамическое связывание. 

```python
class Report:
    # Родительский класс для отчетов
    def __init__(self, data: list[tuple]) -> None: pass
    def make_report(self) -> list[tuple]: pass


class WeeklyReport(Report):
    # Класс переопределяет метод создания отчета для еженедельного отчета (т.е. специализирует Report)
    def make_report(self) -> None: ...


class MonthlyReport(Report):
    # Класс переопределяет метод создания отчета для ежемесячного отчета (т.е. специализирует Report)
    def make_report(self) -> None: ...


if __name__ == "__main__":
    # Где-то получаем данные (data)
    ...

    while True:
        report_type = input("Input 'monthly' or 'weekly':...")
        if report_type not in ('monthly', 'weekly'):
            break
        print("Wrong type")

    # Тип отчета определяется в рантайме, нам не важно какой очет будет в итоге
    # мы в любом случае сможем вызать метод make_report
    # report всегда обладает всеми методами родительского класса Report
    report: Report = MonthlyReport(data) if report_type == 'monthly' else WeeklyReport(data)

    report.make_report()
```
