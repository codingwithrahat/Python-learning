class Enemy:
    type_of_enemy: str
    health_ptn: int = 10
    attack_damage: int = 1


e = Enemy()

e.type_of_enemy = "zombie"

print(f'{e.type_of_enemy} has {e.health_ptn} health points and can do an attack of {e.attack_damage}')