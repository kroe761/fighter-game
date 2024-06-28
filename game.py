from fighter import Fighter
from bot_fighter import BotFighter
import game_helpers

def game_loop(you, enemy):
    base_actions = ["attack", "heal"]
    while you.is_alive() and enemy.is_alive():
        print(f"{you.name} Health: {you.health}")
        print(f"{enemy.name} Health: {enemy.health}")

        list_of_weapons_len = len(you.list_of_weapons())
        if list_of_weapons_len > 0:
            command = f"Choose action: Attack (attack), Heal (heal), or use a weapon ({you.list_of_weapons()}): "
        else:
            command = f"Choose action: Attack (attack) or Heal (heal): "
        action = input(command).lower()
        game_helpers.game_actions(action, you, enemy)

        enemey_action = enemy.choose_action(base_actions + enemy.list_of_weapons())
        print(f"Enemey used {enemey_action}!")
        game_helpers.game_actions(enemey_action, enemy, you)

        if not you.is_alive():
            print(f"{you.name} is dead! Oh no!")
        elif not enemy.is_alive():
            print(f"{enemy.name} is dead! You did it!")

def main():
    weapons = { "brick": 20, "ninja star": 10 }
    hero = Fighter("Kevin", 100, weapons.copy())
    enemy = BotFighter("Bad Guy", 100, weapons.copy())
    game_loop(hero, enemy)

if __name__ == "__main__":
    main()
