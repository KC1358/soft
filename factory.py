from abc import ABC, abstractmethod

# 1. Product Interface
class Coffee(ABC):
    @abstractmethod
    def prepare(self):
        pass

# 2. Concrete Products
class Espresso(Coffee):
    def prepare(self):
        return "☕ Serving a rich, strong Espresso!"

class Cappuccino(Coffee):
    def prepare(self):
        return "☕ Serving a frothy Cappuccino!"

# 3. Factory Class
class CoffeeFactory:
    @staticmethod
    def get_coffee(coffee_type: str) -> Coffee:
        if coffee_type.lower() == "espresso":
            return Espresso()
        elif coffee_type.lower() == "cappuccino":
            return Cappuccino()
        else:
            raise ValueError("Unknown coffee type request")

# --- Testing Factory Pattern ---
factory = CoffeeFactory()

cup1 = factory.get_coffee("espresso")
print(cup1.prepare())

cup2 = factory.get_coffee("cappuccino")
print(cup2.prepare())