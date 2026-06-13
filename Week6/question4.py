# Shopping Discount (own module)

from discount import final_price, TAX_RATE

products = [
    ("Laptop",     85000, 10),
    ("Headphones",  4500, 15),
    ("Phone Case",   800,  5),
    ("USB Cable",    600,  0),
]

print(f"TAX_RATE imported from discount.py: {TAX_RATE}")
print()
print("===== Shopping Bill =====")
for name, price, discount in products:
    total = final_price(price, discount)
    print(f"{name:15} | Original: NPR {price:6} | Final: NPR {total:.2f}")