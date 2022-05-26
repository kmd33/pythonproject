class Parrot:

    def fly(self):
        print("The bird parrot can fly.")

class Penguin:

    def fly(self):
        print("The bird penguin cannot fly.")

def fly_status(bird):
    bird.fly()

parrot = Parrot()
penguin = Penguin()

fly_status(parrot)
fly_status(penguin)