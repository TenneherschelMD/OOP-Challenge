class Pet:
    def __init__(self, name):  # Make sure this line has "name"
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5

    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} ate. Hunger: {self.hunger}, Happiness: {self.happiness}")

    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} slept. Energy: {self.energy}")

    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"{self.name} played! Energy: {self.energy}, Happiness: {self.happiness}, Hunger: {self.hunger}")
        else:
            print(f"{self.name} is too tired to play. Let them sleep.")

    def get_status(self):
        print(f"\n--- {self.name}'s Status ---")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")



my_pet = Pet("Jaggadathree")


while True:
    print("\nWhat would you like to do?")
    print("1. Feed")
    print("2. Sleep")
    print("3. Play")
    print("4. Check Status")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        my_pet.eat()
    elif choice == '2':
        my_pet.sleep()
    elif choice == '3':
        my_pet.play()
    elif choice == '4':
        my_pet.get_status()
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")