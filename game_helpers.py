def initialize_game():
    your_name = input("What's your name? ")
    enemy_name = input("What's your enemy's name? ")
    hp = validate_int("How much health should each player have? ")
    weapons = {}
    any_weapons = validate_int("How many weapons do you want each player to have? ")
    for i in range(any_weapons):
        weapon_name = input(f"Name of the weapon #{i + 1}? ")
        weapon_power = validate_int(f"How much power should the {weapon_name} have? ", hp)
        weapons[weapon_name] = weapon_power
    return your_name, enemy_name, hp, weapons

def game_actions(action, playing_player, other_plyer):
    if action in playing_player.list_of_weapons():
        other_plyer.take_damage(playing_player.use_weapon(action))
    elif action == "a":
        other_plyer.take_damage(playing_player.attack())
    elif action == "h":
        playing_player.heal()
    elif action == "x":
        exit()
    else:
        print(f"action {action} is invalid!")

def validate_int(command, ceiling=None):
    while True:
        try:
            value = input(command)
            value = int(value)
            if value <= 0:
                print("Value cannot be less than or equal to 0! Try again.")
            elif ceiling is not None and value > ceiling:
                print(f"Value cannot be higher than {ceiling}! Try again.")
            else:
                return value
        except ValueError:
            print(f"{value} is not a number. Try again.")

def translate_attack(command):
    match command:
        case "a":
            return "Attack"
        case "h":
            return "Heal"
        case _:
            return command