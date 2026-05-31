# Question 1 - Small Shop Billing and Inventory System

# inventory = {
#     "rice":  {"price": 120, "stock": 20},
#     "milk":  {"price": 90,  "stock": 10},
#     "bread": {"price": 60,  "stock": 15},
#     "eggs":  {"price": 15,  "stock": 30}
# }

# cart = {
#     "rice": 2,
#     "milk": 3,
#     "eggs": 12
# }

# def process_order(inventory, cart):
#     grand_total = 0
#     bill_items = []

#     for item, quantity in cart.items():

#         if item in inventory:
#             stock = inventory[item]["stock"]
#             price = inventory[item]["price"]

#             if quantity <= stock:
#                 item_total = price * quantity
#                 grand_total = grand_total + item_total
#                 bill_items.append((item, quantity, item_total))
#                 inventory[item]["stock"] = stock - quantity

#             else:
#                 print(f"Sorry, not enough stock for {item}")

#         else:
#             print(f"Sorry, {item} is not available in the shop")

#     print("\n---- Bill ----")
#     for item, quantity, item_total in bill_items:
#         print(f"{item} x{quantity} = NPR {item_total}")

#     print(f"Grand Total: NPR {grand_total}")
#     print("--------------")

#     print("\nUpdated stock:", end=" ")
#     stock_parts = []
#     for item in bill_items:
#         item_name = item[0]
#         stock_parts.append(f"{item_name}={inventory[item_name]['stock']}")
#     print(", ".join(stock_parts))

# process_order(inventory, cart)


# Question 2 - Water Level Alert System (Koshi River)

# sensors = [
#     ("Chatara",         2.8),
#     ("Tribeni Ghat",    5.4),
#     ("Koshi Barrage",   4.1),
#     ("Sunsari Bridge",  1.9),
#     ("Saptakoshi Camp", 6.0),
# ]

# def check_water_level(location, level_metres):
#     if level_metres < 3:
#         return "Safe"
#     elif level_metres <= 5:
#         return "Warning — Alert nearby villages"
#     else:
#         return "DANGER — Evacuate immediately!"

# for location, level in sensors:
#     status = check_water_level(location, level)
#     print(f"{location} ({level} m): {status}")


# Question 3 - Date Converter for Nepal Bank System (BS <-> AD)

# bs_months = [
#     "Baisakh", "Jestha", "Ashadh", "Shrawan", "Bhadra", "Ashwin",
#     "Kartik", "Mangsir", "Poush", "Magh", "Falgun", "Chaitra"
# ]

# def convert_date(date_str, from_cal, to_cal):
#     if from_cal == to_cal:
#         return date_str

#     parts = date_str.split("-")
#     year  = int(parts[0])
#     month = int(parts[1])
#     day   = int(parts[2])

#     if from_cal == "AD" and to_cal == "BS":
#         year = year + 56
#     elif from_cal == "BS" and to_cal == "AD":
#         year = year - 56

#     converted_date = f"{year}-{parts[1]}-{parts[2]}"
#     return converted_date

# def format_date(date_str, calendar, style, bs_months):
#     parts = date_str.split("-")
#     year  = int(parts[0])
#     month = int(parts[1])
#     day   = int(parts[2])

#     if style == "iso":
#         return f"{date_str} {calendar}"

#     elif style == "full":
#         month_name = bs_months[month - 1] if calendar == "BS" else [
#             "January", "February", "March", "April", "May", "June",
#             "July", "August", "September", "October", "November", "December"
#         ][month - 1]

#         if day % 10 == 1 and day != 11:
#             suffix = "st"
#         elif day % 10 == 2 and day != 12:
#             suffix = "nd"
#         elif day % 10 == 3 and day != 13:
#             suffix = "rd"
#         else:
#             suffix = "th"

#         return f"{day}{suffix} {month_name}, {year} {calendar}"

#     elif style == "nepali":
#         month_name = bs_months[month - 1] if calendar == "BS" else ""
#         return f"{day} {month_name} {year} {calendar}"

#     else:
#         return date_str

# customers = [
#     {"name": "Ramesh Thapa",  "date": "1985-06-24", "cal": "AD", "need": "BS", "style": "full"},
#     {"name": "Sunita Karki",  "date": "2055-09-10", "cal": "BS", "need": "AD", "style": "iso"},
#     {"name": "Bikash Rai",    "date": "1998-11-30", "cal": "AD", "need": "BS", "style": "nepali"},
#     {"name": "Anjali Gurung", "date": "2040-01-05", "cal": "BS", "need": "AD", "style": "full"},
# ]

# for customer in customers:
#     original_date = customer["date"]
#     from_cal = customer["cal"]
#     to_cal = customer["need"]
#     style = customer["style"]

#     converted_raw = convert_date(original_date, from_cal, to_cal)
#     converted_str = format_date(converted_raw, to_cal, style, bs_months)

#     print(f"{customer['name']} | Original: {original_date} {from_cal} | Converted: {converted_str}")


# Question 4 - Word Frequency Counter

# def word_frequency(text):
#     text = text.lower()

#     cleaned = ""
#     for char in text:
#         if char.isalpha() or char == " " or char == "\n":
#             cleaned = cleaned + char
#         else:
#             cleaned = cleaned + " "

#     words = cleaned.split()

#     counts = {}
#     for word in words:
#         if word in counts:
#             counts[word] = counts[word] + 1
#         else:
#             counts[word] = 1

#     sorted_words = sorted(counts, key=counts.get, reverse=True)

#     top3 = sorted_words[:3]

#     print("Top 3 words:")
#     for word in top3:
#         print(f"{word} — {counts[word]} times")

# text = """
# Nepal is a beautiful country. Nepal has Mount Everest.
# Everest is the highest mountain in the world. Many tourists
# visit Nepal every year to see Everest and other mountains.
# Nepal is known for its mountains and natural beauty.
# """

# word_frequency(text)


# Question 5 - Simple ATM Simulator

accounts = {
    "A001": {"name": "Ramesh Thapa", "balance": 15000, "pin": "1234"},
    "A002": {"name": "Sunita Karki", "balance": 8500,  "pin": "5678"},
    "A003": {"name": "Bikash Rai",   "balance": 22000, "pin": "9012"}
}

def atm(account_id, pin, action, amount=0):

    if account_id not in accounts:
        print("Account not found")
        return

    account = accounts[account_id]

    if account["pin"] != pin:
        print("Incorrect PIN")
        return

    name    = account["name"]
    balance = account["balance"]

    if action == "balance":
        print(f"Account holder: {name}")
        print(f"Current balance: NPR {balance}")

    elif action == "deposit":
        account["balance"] = balance + amount
        print(f"NPR {amount} deposited successfully.")
        print(f"New balance: NPR {account['balance']}")

    elif action == "withdraw":
        if amount > balance:
            print("Insufficient funds")
        else:
            account["balance"] = balance - amount
            print(f"NPR {amount} withdrawn successfully.")
            print(f"New balance: NPR {account['balance']}")

    else:
        print("Invalid action. Use: balance, deposit, or withdraw")


atm("A001", "1234", "balance")
print()
atm("A002", "0000", "withdraw", 2000)
print()
atm("A002", "5678", "deposit", 3000)
print()
atm("A003", "9012", "withdraw", 25000)
print()
atm("A004", "1111", "balance")
