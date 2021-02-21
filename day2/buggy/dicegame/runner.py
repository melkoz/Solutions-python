from .die import Die
from .utils import i_just_throw_an_exception

class GameRunner:

    def __init__(self, c = 0, loss = 0):
        
        self.c = c 
        self.loss = loss
        self.dice = Die.create_dice(5)
        
        if c == 0 :
            self.reset()
        else:
            self.round = self.c + 1
            self.wins = self.c - self.loss 
            self.loses = self.loss

    def reset(self):
        self.round = 1
        self.wins = 0
        self.loses = 0

    def answer(self):
        total = 0

        for die in self.dice:
            total += die.value
        return total

    @classmethod
    def run(cls):
        # Probably counts wins or something.
        # Great variable name, 10/10.
        
        c = 0
        loss = 0
        while True:
            runner = cls(c, loss)

            print("Round {}\n".format(runner.round))

            for die in runner.dice:
                print(die.show())

            
            
            while True:
                try:
                    guess = int(input("Sigh. What is your guess?: "))
                except ValueError:
                    print('This is not an integer. Please try again.')
                    continue
                else:
                    break

            if guess == runner.answer():
                print("Congrats, you can add like a 5 year old...")
                runner.wins += 1
                runner.c += 1
            else:
                print("Sorry that's wrong")
                print("The answer is: {}".format(runner.answer()))
                print("Like seriously, how could you mess that up")
                runner.loses += 1
                runner.c += 1
                runner.loss += 1
            print("Wins: {} Loses {}".format(runner.wins, runner.loses))
            runner.round += 1

            if runner.c == 6:
                print("You won... Congrats...")
                print("The fact it took you so long is pretty sad")
                break

            while True:
                prompt = input("Would you like to play again?[Y/n]: ")
                if prompt == 'Y' or prompt == 'y':
                    c = runner.c
                    loss = runner.loss
                    break
                elif prompt == 'n' or prompt == 'N':
                    quit() 
                elif prompt != 'Y' or prompt != 'y' or  prompt != 'n' or prompt != 'N':  
                    print('This is not Y or n. Please try again.')
                    continue
