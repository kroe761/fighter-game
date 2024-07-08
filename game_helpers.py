def initialize_game() -> tuple:
    your_name = input("What's your name? ")
    enemy_name = input("What's your enemy's name? ")
    hp = validate_int("How much health should each player have? ")
    weapons = {}
    any_weapons = validate_int("How many weapons do you want each player to have? ", floor=-1)
    for i in range(any_weapons):
        weapon_name = input(f"Name of the weapon #{i + 1}? ")
        weapon_power = validate_int(f"How much power should the {weapon_name} have? ", ceiling=hp)
        weapons[weapon_name] = weapon_power
    print("####################################")
    print("### Let's GO! (type 'x' to exit) ###")
    print("####################################")
    return your_name, enemy_name, hp, weapons

def game_actions(action, playing_player, other_plyer) -> None:
    if action in playing_player.list_of_weapons():
        other_plyer.take_damage(playing_player.use_weapon(action))
    elif action.lower() == "a":
        other_plyer.take_damage(playing_player.attack())
    elif action.lower() == "h":
        playing_player.heal()
    elif action.lower() == "x":
        exit()
    else:
        print(f"action {action} is invalid!")

def validate_int(command, floor=0, ceiling=None) -> int:
    while True:
        try:
            value = input(command)
            value = int(value)
            if value <= floor:
                print("Value cannot be less than or equal to 0! Try again.")
            elif ceiling is not None and value > ceiling:
                print(f"Value cannot be higher than {ceiling}! Try again.")
            else:
                return value
        except ValueError:
            print(f"{value} is not a number. Try again.")

def action_translator(command) -> str:
    match command:
        case "a":
            return "Attack"
        case "h":
            return "Heal"
        case _:
            return command