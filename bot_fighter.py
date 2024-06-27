import random
from fighter import Fighter

class BotFighter(Fighter):
    def choose_action(self, list_of_actions):
        return random.choice(list_of_actions)
