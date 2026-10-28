menu = {
    "S": {"name": "Sandwich", "price": 60, "stock": 5},
    "J": {"name": "Juice", "price": 30, "stock": 8},
    "I": {"name": "Idli plate", "price": 40, "stock": 6},
}
print("Menu:")
for code, item in menu.items():
    print(f"{code}: {item['name']} - Rs {item['price']} (stock {item['stock']})")
while True:
   try:
      lines = int(input("Number of order lines: "))
      if lines >= 0:
        break
      print("Enter zero or a positive number.")
   except ValueError:
      print("Enter a whole number.")
total = 0
for i in range(lines):
    code = input(f"Item code for line {i + 1}: ").strip().upper()
    if code not in menu:
         print("Rejected: unknown item code.")
         continue
    try:
       quantity = int(input("Quantity: "))
    except ValueError:
        print("Rejected: quantity must be a whole number.")
        continue
    if quantity <= 0:
        print("Rejected: quantity must be positive.")
    elif quantity > menu[code]["stock"]:
         print(f"Rejected: only {menu[code]['stock']} available.")
    else:
         item = menu[code]
         cost = quantity * item["price"]
         item["stock"] -= quantity
         total += cost
         print(f"Added {quantity} {item['name']}: Rs {cost}")
print(f"Bill total: Rs {total}")
print("Remaining stock:")
for code, item in menu.items():
             print(f"{item['name']}: {item['stock']}")