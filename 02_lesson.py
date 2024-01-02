import typing as t


class MenuItem: ...


class AlcoholItem: ...


class HolidayItem(MenuItem): ...


class RestaurantMenu:

    # Конструктор
    def __init__(self) -> None:
        """
        Постусловие: созданы списки для блюд и отдельно для алкоголя
        """
        self._ordered_items: list[MenuItem] = []
        self._alco_items: list[AlcoholItem] = []

    # Команда
    def add_item(self, item: MenuItem) -> None:
        """
        Постусловие: блюдо из меню добавлено в заказ
        """
        self._ordered_items += item

    def add_alcohol_item(self, item: AlcoholItem) -> None:
        """
        Постусловие: алкоголь из меню добавлен в заказ
        """
        self._ordered_alco_items += item

    # Запрос
    def get_ordered_items(self) -> list[MenuItem]:
        return self._ordered_items

    def get_ordered_alco_items(self) -> list[AlcoholItem]:
        return self._ordered_items


# Расширение родителя-класса
# Добавляем метод для добавления особых празндичных блюд для расширенного меню
class HolidayMenu:

    def add_holiday_item(self, holiday_item: HolidayItem) -> None:
        """
        Постусловие: праздничное блюдо из меню добавлено в заказ
        """
        self._ordered_items += holiday_item


# Сужение родительского класса
# аклоколь не может быть добавлен в детском меню
class ChildrenMenu(RestaurantMenu):

    def add_alcohol_item(self, item: AlcoholItem) -> t.NoReturn:
        pass

    def get_ordered_alco_items(self) -> t.NoReturn:
        pass
