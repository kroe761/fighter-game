def game_actions(action, playing_player, other_plyer):
    if action in playing_player.list_of_weapons():
        other_plyer.take_damage(playing_player.use_weapon(action))
    elif action == "attack":
        other_plyer.take_damage(playing_player.attack())
    elif action == "heal":
        playing_player.heal()
    elif action == "x":
        exit()
    else:
        print(f"action {action} is invalid!")