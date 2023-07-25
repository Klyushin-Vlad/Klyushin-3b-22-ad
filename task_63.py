class CardProduct:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def decrease_quantity(self, amount):
        if amount > 0:
            if self.quantity >= amount:
                self.quantity -= amount
                print("Количество товара: ", self.quantity)
            else:
                print("Товара меньше ", amount)
                print("Количество товара:", self.quantity)
        else:
            print("Количество уменьшаемого товара должно быть положительным")

    def change_price(self, amount):
        if self.price >= -amount:
            self.price += amount
            print("Стоимость товара: ", self.price)
        else:
            print("Стоимость товара не может быть отрицательной")
            print("Стоимость товара: ", self.price)