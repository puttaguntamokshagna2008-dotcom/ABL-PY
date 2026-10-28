food_prepared = float(input("Enter food prepared (in kg): "))
food_wasted = float(input("Enter food wasted (in kg): "))
if food_prepared <= 0:
   print("Invalid quantity of food prepared!")
elif food_wasted < 0 or food_wasted > food_prepared:
   print("Invalid quantity of food wasted!")
else:
   food_consumed = food_prepared - food_wasted
   waste_percentage = (food_wasted / food_prepared) * 100
   print("Food Prepared:", food_prepared, "kg")
   print("Food Consumed:", food_consumed, "kg")
   print("Food Wasted:", food_wasted, "kg")
   print("Waste Percentage:", round(waste_percentage, 2), "%")
if waste_percentage <= 10:
   print("Status: Good! Food waste is low.")
elif waste_percentage <= 25:
   print("Status: Moderate food waste.")
   print("Suggestion: Prepare food according to demand.")
else:
   print("Status: High food waste!")
   print("Suggestion: Reduce excess food preparation.")
