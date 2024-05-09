class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.happiness = 50
        self.poopies = 0

    def feed(self):
        self.hunger -= 10
        self.poopies += 20
        if self.hunger < 0:
            self.hunger = 0

    def play(self):
        self.happiness += 10
        if self.happiness > 100:
            self.happiness = 100

    def poop(self):
        self.poopies = 0
        print("💩")

class Dog(Pet):
    def __init__(self, name):
        super().__init__(name)
        
    def play(self):
        super().play()
        print("Wuff Wuff")

    def feed(self):
        super().feed()
        print("Schmatz Schmatz")
    
def main():
    name = input("Wie willst du deinen Hund nennen? ")
    pet = Dog(name)
    while True:
        print(f"\n{pet.name}'s Hunger: {pet.hunger}, Stimmung: {pet.happiness}, Kot: {pet.poopies}")
        action = input("Was möchtest du machen? (füttern, spielen, rauslassen, beenden): ")
        if action == 'füttern':
            pet.feed()
        elif action == 'spielen':
            pet.play()
        elif action == 'beenden':
            break
        elif action == 'rauslassen':
            pet.poop()
        else:
            print("ungültge Aktion.")
main()
