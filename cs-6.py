def read_hour(prompt):
    while True:
       try:
           value = int(input(prompt))
           if 0 <= value <= 23:
               return value
           print("Use an hour from 0 to 23.")
       except ValueError:
           print("Enter a whole-number hour.")
while True:
   try:
      count = int(input("Number of classes: "))
      if 1 <= count <= 30:
         break
      print("Enter a number from 1 to 30.")
   except ValueError:
      print("Enter a whole number.")
classes = []
for i in range(count):
     name = input(f"Class {i + 1} course name: ").strip()
     day = input("Day (for example, Monday): ").strip().lower()
     while True:
        start = read_hour("Start hour: ")
        end = read_hour("End hour: ")
        if end > start:
           break
        print("End hour must be later than start hour.")
        classes.append({"name": name, "day": day, "start": start, "end": end})
conflicts = []
for i in range(len(classes)):
    for j in range(i + 1, len(classes)):
       first, second = classes[i], classes[j]
       same_day = first["day"] == second["day"]
       overlap = (first["start"] < second["end"]
              and second["start"] < first["end"])
       if same_day and overlap:
           conflicts.append((first["name"], second["name"], first["day"]))
if conflicts:
     print("Conflicts found:")
     for first, second, day in conflicts:
         print(f"{first} and {second} on {day}")
else:
     print("No timetable conflicts.")