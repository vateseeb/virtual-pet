import os
import json
import threading
import time

class Pet:
    def __init__(self, name, hunger, happiness):
        self.name = name
        self.set_hunger(hunger)
        self.set_happiness(happiness)

    def feed(self):
        self.set_hunger(self.hunger - 10)

    def play(self):
        self.set_happiness(self.happiness + 10)
        self.set_hunger(self.hunger + 10)

    def set_hunger(self, hunger):
        self.hunger = hunger
        if self.hunger >= 100:
            self.happiness -= 20
            print(f"{self.name} ist sehr hungrig!")
        if self.hunger < 0:
            self.hunger = 0
            self.happiness -= 20
        if self.hunger >= 150:
            print("GAME OVER!")
            exit()

    def set_happiness(self, happiness):
        self.happiness = happiness
        if self.happiness > 100:
            self.happiness = 100
        if self.happiness < 0:
            self.happiness = 0

class Dog(Pet):
    def __init__(self, name, hunger, happiness):
        super().__init__(name, hunger, happiness)

    def feed(self):
        super().feed()
        print("Mjam Mjam!")

    def play(self):
        super().play()
        print("Woof! Woof!")

def increase_hunger_over_time(pet):
    while True:
        time.sleep(5)  # wait for 60 seconds
        pet.set_hunger(pet.hunger + 10)
        
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

     # Start a new thread that will increase the dog's hunger over time
    threading.Thread(target=increase_hunger_over_time, args=(dog,), daemon=True).start()
    
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
