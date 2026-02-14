import random

class FlashCard:
    def __init__ (self):
        self.fruits = {
            "Banana":"yellow",
            "Strawberries":"pink",
            "Watermelon":"green",
            "Apple":"red",
            "Grapes":"purple",
        }
    
    def play (self):
        print("WELCOME TO THE GAME")
        while True:
            fruit, color = random.choice(list(self.fruits.items()))
            user_input = input(f"What is the colour of the {fruit}? ")
            if user_input == color:
                print("Correct")
            else:
                print("Wrong!")

            ask = int(input("Enter 0 to play again! "))
            if ask != 0:
                break

f1 = FlashCard()
f1.play()


