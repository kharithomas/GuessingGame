# Implement a guessing game in python

import random


class Game:
    def guess(self):
        max_num = int(input('Set a max: '))
        random_number = random.randint(1, max_num)
        guess = 0

        # loop
        while guess != random_number:
            guess = int(input(f'Guess a number between 1 and {max_num}: '))

            if guess < random_number:
                print('Too low!')
            elif guess > random_number:
                print('Too high!')

        print(f'\nYou win! The number was: {random_number}')


game = Game()
game.guess()
