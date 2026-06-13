# Bill Splitter (random module)

import random
random.seed(42)

friends    = ["Ramesh", "Sunita", "Bikash", "Anjali", "Dipak"]
total_bill = 3750

def split_bill(friends, total):
    return total / len(friends)

def pick_lucky(friends):
    return random.choice(friends)

def final_summary(friends, total):
    share = split_bill(friends, total)
    lucky = pick_lucky(friends)         

    print("===== Bill Summary =====")
    for person in friends:
        print(f"{person} pays: NPR {share:.2f}")

    lucky_total = share + 50            
    print(f"\nLucky tax picked: {lucky}")
    print(f"{lucky} pays extra NPR 50 | Total: NPR {lucky_total:.2f}")

final_summary(friends, total_bill)