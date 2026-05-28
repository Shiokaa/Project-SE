class Entity:
    def __init__(self, name: str, stamina: int, perception: int, age: int, speed: float) -> None :
        self.name = name
        self.stamina = stamina
        self.perception = perception
        self.age = age
        self.speed = speed

class Prey(Entity):
    def __init__(self, name: str, stamina: int, perception: int, age: int, speed: float) -> None :
        super().__init__(name, stamina, perception, age, speed)

class Predator(Entity):
    def __init__(self, name: str, stamina: int, perception: int, age: int, speed: float) -> None :
        super().__init__(name, stamina, perception, age, speed)