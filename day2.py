class GameData:
    def __init__(self, game_string):
        self.game_id, sets_data = game_string.split(": ")
        self.game_title = self.game_id.split()
        self.game_id = int(self.game_title[-1])
        self.sets = [x.split(", ") for x in sets_data.split("; ")]
        self.game_dict = {}
        self._get_highest_quantities()

    def _get_highest_quantities(self):
        self.highest_quantities = {}
        for hand in self.sets:
            for item in hand:
                quantity, color = item.split()
                quantity = int(quantity)
                if color not in self.highest_quantities or quantity > self.highest_quantities[color]:
                    self.highest_quantities[color] = quantity

    def isPossible(self, challenge):
        for key, value in self.highest_quantities.items():
            if challenge[key] < self.highest_quantities[key]:
                print(challenge[key], self.highest_quantities[key])
                return False
        return True


def answer(file, challenge):
    sum = 0
    with open(file, 'r') as file:
        for line in file:
            game = GameData(line)
            if game.isPossible(challenge):
                sum = sum + game.game_id
            else: 
                print(sum)

def answer2(file):
    total=0
    with open(file, 'r') as file:
        for line in file:
            product = 1
            game = GameData(line)
            for key, value in game.highest_quantities.items():
                product = game.highest_quantities[key] * product
            total = total + product
        print(total)


answer("/home/luc1d/AdventOfCode/day2/input.txt", {"red":12, "green": 13, "blue": 14})
answer2("/home/luc1d/AdventOfCode/day2/input.txt")
