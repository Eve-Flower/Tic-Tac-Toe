import math
import random

class Player:
    def __init__(self, letter):
        # letter is x or o
        self.letter = letter
    #we want all palyers to get their next move given a game
    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8):')
            #incorporate checks
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError # raises value error if false move
                valid_square = True #if successful, then yay we have a move
            except ValueError:
                print('Invalid square. Please try again.')

        return val
       