# flight passenger adding class system
class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True
    
    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(5)
print(flight.open_seats)


people = ["Abel", "Prince", "Denzel", "Myles", "Chris", "Benjamin", "Abraham", "Whales"]


for i in people:
    success = flight.add_passenger(i)
    if success:
        print(f"{i} was added to the flight")
    else:
        print(f"No available seats for {i}")