from typing import TypeVar

# Базовые классы
class Beverage:
    def serve(self) -> None:
        print("Serving some beverage")

class Tea(Beverage):
    def serve(self) -> None:
        print("Serving tea")

class Coffee(Beverage):
    def serve(self) -> None:
        print("Serving coffee")

# Полиморфная функция
def serve_beverage(beverage: Beverage):
    print(beverage.serve())

# Создаем объекты
tea = Tea()
coffee = Coffee()

# Демонстрация полиморфизма
serve_beverage(tea)     # Печатает: Serving tea
serve_beverage(coffee)  # Печатает: Serving coffee

T_co = TypeVar('T_co', covariant=True)

class BeverageFactory[T_co]:
    def get_beverage(self) -> T_co:
        ...

class TeaFactory(BeverageFactory[Tea]):
    def get_beverage(self) -> Tea:
        return Tea()

class CoffeeFactory(BeverageFactory[Coffee]):
    def get_beverage(self) -> Coffee:
        return Coffee()

# Демонстрация ковариантного вызова
coffee_factory: BeverageFactory[Coffee] = CoffeeFactory()
print(coffee_factory.get_beverage().serve())  # Печать: Serving coffee

tea_factory: BeverageFactory[Tea] = TeaFactory()
print(tea_factory.get_beverage().serve())  # Печать: Serving tea
