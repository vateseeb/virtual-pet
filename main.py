import os
import json

class Pet:
    def __init__(self, name, hunger, happiness):
        self.name = name
        self.hunger = hunger
        self.happiness = happiness

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
    def __init__(self, name, hunger, happiness):
        super().__init__(name, hunger, happiness)

    def feed(self):
        super().feed()
        print("Mjam Mjam!")

    def play(self):
        super().play()
        print("Woof! Woof!")

def main():
    name_file = "dog_name.txt"
    state_file = "dog_state.json"

    if os.path.exists(name_file):
        with open(name_file, "r") as file:
            name = file.read().strip()
    else:
        name = input("Wie willst du deinen Hund nennen? ")
        with open(name_file, "w") as file:
            file.write(name)

    if os.path.exists(state_file):
        with open(state_file, "r") as file:
            state = json.load(file)
    else:
        state = {"hunger": 50, "happiness": 50}

    dog = Dog(name, state["hunger"], state["happiness"])  
    
    while True:
        print(f"\n{dog.name}'s Hunger: {dog.hunger}, Fröhlichkeit: {dog.happiness}")
        action = input("Was willst du tun? (füttern,spielen,beenden): ")
        if action == 'füttern':
            dog.feed()
        elif action == 'spielen':
            dog.play()
        elif action == 'beenden':
            with open(state_file, "w") as file:
                json.dump({"hunger": dog.hunger, "happiness": dog.happiness}, file)
            print("Bis zum nächsten Mal!")
            break
        else:
            print("Invalid action.")
main()
