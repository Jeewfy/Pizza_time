# 1. Класс продукта — Пицца
class Pizza:
    def __init__(self):
        self.dough = "Unknown"
        self.sauce = "Unknown"
        self.topping = "Unknown"
        self.cooking_time = 0  # в минутах

    def __str__(self):
        return f"Пицца:\n" \
               f"Тесто: {self.dough}\n" \
               f"Соус: {self.sauce}\n" \
               f"Начинка: {self.topping}\n" \
               f"Время выпечки: {self.cooking_time} мин\n"


# 2. Абстрактный класс строителя
class PizzaBuilder:
    def set_dough(self, dough):
        pass

    def set_sauce(self, sauce):
        pass

    def set_topping(self, topping):
        pass

    def set_cooking_time(self, time):
        pass

    def get_result(self):
        pass


# 3. Конкретный строитель — Итальянская пицца
class ItalianPizzaBuilder(PizzaBuilder):
    def __init__(self):
        self.pizza = Pizza()

    def set_dough(self, dough):
        self.pizza.dough = dough

    def set_sauce(self, sauce):
        self.pizza.sauce = sauce

    def set_topping(self, topping):
        self.pizza.topping = topping

    def set_cooking_time(self, time):
        self.pizza.cooking_time = time

    def get_result(self):
        return self.pizza


# 4. Директор — управляет процессом сборки
class PizzaDirector:
    def make_margherita(self, builder):
        builder.set_dough("тонкое")
        builder.set_sauce("томатный")
        builder.set_topping("моцарелла, базилик")
        builder.set_cooking_time(12)

    def make_pepperoni(self, builder):
        builder.set_dough("толстое")
        builder.set_sauce("томатный")
        builder.set_topping("моцарелла, пепперони, оливки")
        builder.set_cooking_time(15)


# 5. Клиентский код
if __name__ == "__main__":
    builder = ItalianPizzaBuilder()
    director = PizzaDirector()

    print("Готовим пиццу Маргариту:")
    director.make_margherita(builder)
    pizza = builder.get_result()
    print(pizza)

    print("Готовим пиццу Пепперони:")
    builder = ItalianPizzaBuilder()  # создаём нового строителя
    director.make_pepperoni(builder)
    pizza2 = builder.get_result()
    print(pizza2)
