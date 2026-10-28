name = input("Enter consumer name: ")
units = float(input("Enter units consumed: "))

if units < 0:
    print("Invalid units consumed!")

else:
    if units <= 100:
        bill = units * 2
    elif units <= 200:
        bill = (100 * 2) + (units - 100) * 3
    elif units <= 300:
        bill = (100 * 2) + (100 * 3) + (units - 200) * 5
    else:
        bill = (100 * 2) + (100 * 3) + (100 * 5) + (units - 300) * 7

    print("Consumer Name:", name)
    print("Units Consumed:", units)
    print("Total Bill: Rs.", round(bill, 2))
