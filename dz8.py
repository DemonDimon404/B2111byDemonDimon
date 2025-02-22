import time


class Sim:
    def __init__(self, name):
        self.name = name
        self.happiness = 50
        self.hunger = 50
        self.energy = 50
        self.log = []

    def change_happiness(self, change):
        self.happiness += change
        self.log_event(f"{self.name} changed happiness to {self.happiness}")

    def change_hunger(self, change):
        self.hunger += change
        self.log_event(f"{self.name} changed hunger level to {self.hunger}")

    def change_energy(self, change):
        self.energy += change
        self.log_event(f"{self.name} changed energy level to {self.energy}")

    def log_event(self, event):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.log.append(f"[{timestamp}] {event}")

    def show_log(self):
        print(f"Log for {self.name}:")
        for entry in self.log:
            print(entry)


# Create a few Sims and change their states
sim1 = Sim("Max")
sim1.change_happiness(10)
sim1.change_hunger(-5)
sim1.change_energy(-10)

sim2 = Sim("Olga")
sim2.change_happiness(-15)
sim2.change_hunger(20)

# Show the logs
sim1.show_log()
sim2.show_log()