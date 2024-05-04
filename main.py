class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.happiness = 50

    def feed(self):
        self.hunger -= 10
        if self.hunger < 0:
            self.hunger = 0

    def play(self):
        self.happiness += 10
        if self.happiness > 100:
            self.happiness = 100

def main():
    name = input("What would you like to name your pet? ")
    pet = Pet(name)
    while True:
        print(f"\n{pet.name}'s Hunger: {pet.hunger}, Happiness: {pet.happiness}")
        action = input("What would you like to do? (feed, play, quit): ")
        if action == 'feed':
            pet.feed()
        elif action == 'play':
            pet.play()
        elif action == 'quit':
            break
        else:
            print("Invalid action.")
main()
