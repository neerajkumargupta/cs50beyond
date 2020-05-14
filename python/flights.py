class FLight():
    def __init__(self , capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)


flight = FLight(4)
people = ["Neha", "Neeraj", "Lavanya", "Rishi"]

for person in people:
    success = flight.add_passenger(person)
    if success:
        print(f"success fully added {person}")
    else:
        print(f"Not able to add {person}")
