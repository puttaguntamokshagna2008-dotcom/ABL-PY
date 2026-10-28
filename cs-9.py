def read_int(prompt, low, high):

    while True:

        try:

            value = int(input(prompt))

            if low <= value <= high:

                return value

            print(f"Enter a value from {low} to {high}.")

        except ValueError:

            print("Enter a whole number.")


places = read_int("Scholarship places: ", 0, 100)

count = read_int("Number of applicants: ", 1, 100)

eligible = []


for i in range(count):

    name = input(f"Applicant {i + 1} name: ").strip()

    score = read_int("Entrance score (0-100): ", 0, 100)

    income = read_int("Annual family income in rupees: ", 0, 100000000)

    if score >= 80 and income <= 500000:

        eligible.append({"name": name, "score": score, "income": income})


eligible.sort(key=lambda student: (-student["score"],

                                   student["income"],

                                   student["name"].lower()))

awarded = eligible[:places]

not_selected = eligible[places:]


print("Scholarship awards:")

if awarded:

    for rank, student in enumerate(awarded, start=1):

        print(f"{rank}. {student['name']} - score {student['score']}, "

              f"income Rs {student['income']}")

else:

    print("No scholarships awarded.")


print("Eligible but not selected:")

if not_selected:

    for student in not_selected:

        print(f"{student['name']} - score {student['score']}, "

              f"income Rs {student['income']}")

else:

    print("None")