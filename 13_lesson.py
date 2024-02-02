class Car:
    _REPAIR_OK = 1
    _REPAIR_ERR = 2

    def __init__(self, model: str) -> None:
        self._model = model

    # 1. метод публичен в родительском классе А и публичен в его потомке B;
    def get_model(self) -> str:
        return self._model

    # 4. метод скрыт в родительском классе А и скрыт в его потомке B. 
    def _do_tech_inspection(self) -> None:
        print("Doing tech inspection")

    # 4. метод скрыт в родительском классе А и скрыт в его потомке B. 
    def _do_change_oil(self) -> None:
        print("Changine the oil")

    # 1. метод публичен в родительском классе А и публичен в его потомке B;
    def repare(self) -> None:
        self._do_tech_inspection()
        self._do_change_oil()


class RaceCar(Car):
    # Унаследует get_model как условно "публичный" метод
    # Унаследует _do_tech_inspection, _do_change_oil как условно "приватные" (protected) методы
    pass

# Методы 2, 3
#     - 2. метод публичен в родительском классе А и скрыт в его потомке B;
#     - 3. метод скрыт в родительском классе А и публичен в его потомке B;
# не поддерживаются в Python, как и вообще концепция приватности в "нормальном" виде
# _method не обязывает его использование, как приватного, __method "переименовывает" под капотом название, не меняя сути
# при наследовании
