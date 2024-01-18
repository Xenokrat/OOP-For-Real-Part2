from typing import Callable, Sequence, TypeVar

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
emploee = Emploee('Ivan')

# Ковариативность 
#    - это нормально создать "контейнер" для работников, который поддерживает любые подтипы Employee

T_co = TypeVar('T_co', covariant=True)

class PeopleList[T_co]:
    def __init__(self, _list: list[T_co]) -> None:
        self._list = _list


list_of_emploees1: PeopleList[Emploee] = PeopleList([programmer, accountant])

# в этой ситуации уже некорректно добавлять в список программистов более общий тип Emploee
list_of_emploees2: PeopleList[Programmer] = PeopleList([emploee, programmer])

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
