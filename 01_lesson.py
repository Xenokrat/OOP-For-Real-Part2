from abc import ABC, abstractmethod


# Иерархия трудовых договоров
class Contract(ABC):
    """
        Родительский класс
    """

    # Конструктор
    def __init__(self, stake: int) -> None: 
        self._stake = stake

    # Команды

    # Запросы
    @abstractmethod
    def get_stake(self) -> int: pass


class PartTimeContract(Contract):
    """
        Наследование
        Наследуем этот тип договора от родительского класса
    """

    def get_stake() -> int:
        return int(self._stake * 0.5)


class FullTimeContract(Contract):
    """
        Наследование
        Наследуем этот тип договора от родительского класса
    """

    def get_stake() -> int:
        return self._stake


# Иерархия работников
class Emploee(ABC):
    """
        Родительский класс
    """

    # Конструктор
    def __init__(self, working_hours: int, contract: Contract) -> None:
    """
        Композиция
        Класс сотрудника содержит объект класса Contract
    """
        self._hours = working_hours
        self._contract = contract

    # Команды

    # Запросы
    @abstractmethod
    def calculate_salary(self) -> float: pass


class TemporaryEmployee(Emploee): ...
    """
        Наследование
        Наследуем этот тип сотрудника от родительского класса
    """

    def calculate_salary(self) -> float:
        return self._contract.stake * self._hours * 0.8


class StaffEmployee(Emploee): ...
    """
        Наследование
        Наследуем этот тип сотрудника от родительского класса
    """

    def calculate_salary(self) -> float:
        return self._contract.stake * self._hours


if __name__ == "__main__":
    # Полиморфизм - работникам может быть присвоен любой договор из иерархии классов договоров
    empl1 = StaffEmployee(168, PartTimeContract())
    empl2 = StaffEmployee(168, FullTimeContract())
    empl3 = TemporaryEmployee(100, FullTimeContract())

    total_salary = 0

    # Полиморфизм - для расчета ЗП могур использоваться разные объекты из иерархии классов работников
    for empl in (empl1, empl2, empl3):
        total_salary += empl.calculate_salary()

    print(total_salary)

