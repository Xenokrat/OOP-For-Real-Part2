from typing import Callable, Sequence

class Emploee:
    def __init__(self, name: str) -> None:
        self._name = name

    def get_salary(self) -> None:
        ...


class Programmer(Emploee):
    def write_program(self) -> None: ...


class Accountant(Emploee):
    def calc_salary(self) -> int: ...

programmer = Programmer('Vasya')
accountant = Accountant('Lena')

# Ковариативность 
#    - это нормально создать "контейнер" для работников, который поддерживает любые подтипы Employee
list_of_emploees: Sequence[Emploee] = [programmer, accountant]

# Контрвариативность
def assign_task_to_programmer(
    task: Callable[[Programmer], None],
    programmer: Programmer
) -> None:
    task(programmer)

def task_write_program(person: Programmer) -> None:
    person.write_program()

def task_get_salary(person: Emploee) -> None:
    person.get_salary()

def task_calc_salary(person: Accountant) -> None:
    person.calc_salary()

# нормально, что мы можем дать программисту задачу для работника, потому что "все программисты - работники"
# поэтому программист может выполнять все, что выполняет работник, но не наоборот
assign_task_to_programmer(task_write_program, programmer)
assign_task_to_programmer(task_get_salary, programmer)

# здесь уже будет ошибка, т.к. программисты не обладают ВСЕМИ методами бухгалтеров
assign_task_to_programmer(task_calc_salary, programmer)