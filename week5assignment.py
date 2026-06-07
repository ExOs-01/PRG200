# # Question 1 - Bank Account Manager


# class BankAccount:
#     def __init__(self, name, account_number, balance=0):
#         self.name = name
#         self.account_number = account_number
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance = self.balance + amount

#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Insufficient funds")
#         else:
#             self.balance = self.balance - amount

#     def get_balance(self):
#         print(f"{self.name} - Balance: NPR {self.balance}")


# accounts = [
#     ("Ramesh Thapa", "A001", 5000),
#     ("Sunita Karki", "A002", 0),
#     ("Bikash Rai",   "A003", 12000),
# ]

# a001 = BankAccount(accounts[0][0], accounts[0][1], accounts[0][2])
# a002 = BankAccount(accounts[1][0], accounts[1][1], accounts[1][2])
# a003 = BankAccount(accounts[2][0], accounts[2][1], accounts[2][2])

# print("===== Bank Operations =====")

# amount = float(input("Enter amount to deposit into A002: "))
# a002.deposit(amount)
# print(f"Deposited NPR {amount} into A002")

# amount = float(input("Enter amount to withdraw from A003: "))
# a003.withdraw(amount)

# amount = float(input("Enter amount to withdraw from A001: "))
# a001.withdraw(amount)

# print("\n===== Final Balances =====")
# a001.get_balance()
# a002.get_balance()
# a003.get_balance()


# Question 2 - Student Report Card

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def average(self):
#         total = 0
#         for mark in self.marks:
#             total = total + mark
#         return total / len(self.marks)

#     def grade(self):
#         avg = self.average()
#         if avg >= 80:
#             return "A"
#         elif avg >= 65:
#             return "B"
#         elif avg >= 50:
#             return "C"
#         elif avg >= 40:
#             return "D"
#         else:
#             return "F"

#     def display(self):
#         avg = self.average()
#         if avg >= 40:
#             result = "Pass"
#         else:
#             result = "Fail"
#         print(f"Name: {self.name}")
#         print(f"Average: {avg:.1f}")
#         print(f"Grade: {self.grade()}")
#         print(f"Result: {result}")
#         print("_" * 30)


# students = [
#     ("Aarav",  [78, 85, 60, 90, 72]),
#     ("Sita",   [45, 50, 38, 60, 55]),
#     ("Bishal", [30, 25, 40, 35, 28]),
#     ("Priya",  [90, 88, 95, 92, 87]),
# ]

# s1 = Student(students[0][0], students[0][1])
# s2 = Student(students[1][0], students[1][1])
# s3 = Student(students[2][0], students[2][1])
# s4 = Student(students[3][0], students[3][1])

# print("\n===== Student Report Card =====")
# s1.display()
# s2.display()
# s3.display()
# s4.display()


# Question 3 - Food Delivery App

# class DeliveryPartner:
#     def __init__(self, name, partner_id, deliveries):
#         self.name = name
#         self.partner_id = partner_id
#         self.deliveries = deliveries

#     def total_earning(self):
#         return 0

#     def display(self):
#         print(f"Name: {self.name}")
#         print(f"Deliveries: {self.deliveries}")
#         print(f"Total Earning: NPR {self.total_earning()}")
#         print("_" * 30)


# class BikeRider(DeliveryPartner):
#     def __init__(self, name, partner_id, deliveries, km_travelled):
#         super().__init__(name, partner_id, deliveries)
#         self.km_travelled = km_travelled

#     def total_earning(self):
#         return (80 * self.deliveries) + (5 * self.km_travelled)


# class Walker(DeliveryPartner):
#     def __init__(self, name, partner_id, deliveries, rainy_deliveries):
#         super().__init__(name, partner_id, deliveries)
#         self.rainy_deliveries = rainy_deliveries

#     def total_earning(self):
#         return (60 * self.deliveries) + (50 * self.rainy_deliveries)


# class CarDriver(DeliveryPartner):
#     def __init__(self, name, partner_id, deliveries, fuel_cost):
#         super().__init__(name, partner_id, deliveries)
#         self.fuel_cost = fuel_cost

#     def total_earning(self):
#         return (120 * self.deliveries) - self.fuel_cost


# partners = [
#     BikeRider("Santosh Rai",   "B-01", 15, 42),
#     Walker("Kabita Maharjan",  "W-01", 18, 5),
#     CarDriver("Roshan KC",     "C-01", 20, 850),
# ]

# print("\n===== Delivery Partners =====")
# for partner in partners:
#     partner.display()

# highest = partners[0]
# for partner in partners:
#     if partner.total_earning() > highest.total_earning():
#         highest = partner

# print(f"Highest Earning Partner: {highest.name} - NPR {highest.total_earning()}")


# Question 4 - Bus Ticket Booking (Sajha Yatayat)

class Bus:
    def __init__(self, route, total_seats):
        self.route = route
        self.total_seats = total_seats
        self.booked = []

    def book_seat(self, seat_number, passenger_name):
        for booking in self.booked:
            if booking[0] == seat_number:
                print(f"Seat {seat_number} already booked")
                return
        self.booked.append((seat_number, passenger_name))
        print(f"Seat {seat_number} booked for {passenger_name}")

    def available_seats(self):
        return self.total_seats - len(self.booked)

    def passenger_list(self):
        print(f"\nRoute: {self.route}")
        print("Booked Seats:")
        for seat_number, passenger_name in self.booked:
            print(f"  Seat {seat_number} - {passenger_name}")


bus = Bus("Kathmandu - Pokhara", 10)

bookings = [
    (3, "Ramila Shrestha"),
    (7, "Deepak Gurung"),
    (3, "Anita Rai"),
    (1, "Prakash Magar"),
    (7, "Suman Tamang"),
]

print("\n===== Bus Ticket Booking =====")
for seat_number, passenger_name in bookings:
    bus.book_seat(seat_number, passenger_name)

print(f"\nAvailable Seats: {bus.available_seats()}")
bus.passenger_list()
