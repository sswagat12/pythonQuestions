import random
class User(models.model):
    def __init__(self):
        name = CharField(max=100)
        color = CharField (max=20)
        player_pointer = [0,0]

class Game():
    def __init__(self, nameOfPlayer, color, player_pointer) -> None:
        nameOfPlayer = self.nameOfPlayer
        color = self.color
        player_pointer = self.player_pointer
        user = User(nameOfPlayer, color, player_pointer)
    grid = [[1,2,3,4,5],
            [6,7,8,9,10],
            [11,12,13,14,15],
            [16,17,18,19,20],
            [21,22,23,24,25]]
    player_pointer = models.ForeignKey(User)
    dice_rolled 
    # player_pointer = [0,0]
    # dice_rolled = 5
    def play(self, dice_rolled, player_pointer):
        player_pointer += dice_rolled
        snakes = Snake()
        for each_snake in snakes.snake_coordinates:
            if player_pointer == each_snake[0]:
                player_pointer = each_snake[1]
            elif player_pointer == Ladders.ladder_cordinates[0]:
                player_pointer = Ladders.ladder_cordinates[1]
        if player_pointer == 25:
            return "Win"
        else:
            # switch play
        

class Snake():
    snake_coordinates = [[1,3],[2,4]]

class Ladders():
    ladder_cordinates = [[2,5], [0,4]]

class Dice():
    roll_occurence = IntegerField

    def roll_dice():
        return random.randint(0,6)
    


    """Alex Xu--->System Design"""