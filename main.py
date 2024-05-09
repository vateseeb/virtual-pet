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
    name = input("Wie willst du deinen Hund nennen? ")
    pet = Pet(name)
    while True:
        print(f"\n{pet.name}'s Hunger: {pet.hunger}, Stimmung: {pet.happiness}")
        action = input("Was möchtest du machen? (füttern, spielen, beenden): ")
        if action == 'füttern':
            pet.feed()
        elif action == 'spielen':
            pet.play()
        elif action == 'beenden':
            break
        else:
            print("ungültge Aktion.")
main()
