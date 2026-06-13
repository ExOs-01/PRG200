TAX_RATE = 0.13  

def apply_discount(price, percent):
    discount_amount = price * (percent / 100)
    return price - discount_amount

def apply_tax(price):
    return price + (price * TAX_RATE)

def final_price(price, discount_pct):
    after_discount = apply_discount(price, discount_pct)
    after_tax      = apply_tax(after_discount)
    return after_tax