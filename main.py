class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.happiness = 50

    def feed(self):
        self.set_hunger(self.hunger - 10)

    def play(self):
        self.happiness = self.happiness + 10 
        self.set_hunger(self.hunger + 10)
        if self.happiness > 100:
            self.happiness = 100

    def set_hunger(self, hunger):
        self.hunger = hunger
        if self.hunger >= 100:
            self.happiness -= 20
        if self.hunger < 0:
            self.hunger = 0
            self.happiness -= 20

class Dog(Pet):
    def __init__(self, name):
        super().__init__(name)

    def feed(self):
        super().feed()
        print("Woof!")

    def play(self):
        super().play()
        print("Woof! Woof!")

def main():
    name = input("What would you like to name your dog? ")
    dog = Dog(name)
    while True:
        print(f"\n{dog.name}'s Hunger: {dog.hunger}, Happiness: {dog.happiness}")
        action = input("What would you like to do? (feed, play, quit): ")
        if action == 'feed':
            dog.feed()
        elif action == 'play':
            dog.play()
        elif action == 'quit':
            break
        else:
            print("Invalid action.")
main()
