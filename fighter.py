import random

class Fighter:
    def __init__(self, name, health, weapons) -> None:
        self.name = name
        self.health = health
        self.weapons = weapons

    def name(self) -> str:
        return self.name

    def take_damage(self, damage) -> None:
        self.health -= damage

    def heal(self) -> None:
        self.health += random.randint(5, 15)

    def attack(self) -> int:
        return random.randint(5, 15)

    def is_alive(self) -> bool:
        return self.health > 0

    def list_of_weapons(self) -> list:
        return list(self.weapons.keys())
    
    def use_weapon(self, weapon) -> int:
        damage = self.weapons[weapon]
        self.weapons.pop(weapon)
        return damage
