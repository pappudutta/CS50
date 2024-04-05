# class Point():
#     def __init__(self, input1, input2):
#         self.x = input1
#         self.y = input2

# p = Point(2, 8)

# print(f"Value of input1 {p.x}")
# print(f"Value of input2 {p.y}")

class Flight(): # create a class Flight
    def __init__(self, capacity): # Define function
        self.capacity = capacity # Define capacity
        self.passsangers = [] # Define an empty list
    
    def add_passanger(self, name): # Define function
        if not self.open_seats(): # Define conditions
            return False
        self.passsangers.append(name)
        return True

    def open_seats(self): 
        return self.capacity - len(self.passsangers)

flight = Flight(3)

people = ["Neerav", "Bikash", "Priyanshi", "Ajoy"]

for person in people:
    success = flight.add_passanger(person)

    if success:
        print(f"Added {person} to flight successfully")
    else:
        print(f"No seats available for {person}")
