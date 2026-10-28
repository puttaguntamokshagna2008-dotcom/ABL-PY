def read_int(prompt, low, high):

    while True:

        try:

            value = int(input(prompt))

            if low <= value <= high:

                return value

            print(f"Enter a whole number from {low} to {high}.")

        except ValueError:

            print("Enter a whole number.")


def read_gpa(prompt):

    while True:

        try:

            value = float(input(prompt))

            if 0 <= value <= 10:

                return value

            print("Enter a GPA from 0 to 10.")

        except ValueError:

            print("Enter a number.")


rooms = read_int("Available hostel rooms: ", 0, 100)

count = read_int("Number of applicants: ", 1, 100)

eligible = []


for i in range(count):

    name = input(f"Applicant {i + 1} name: ").strip()

    distance = read_int("Home distance from campus in km: ", 0, 100000)

    gpa = read_gpa("GPA (0-10): ")

    if distance >= 50 and gpa >= 5.0:

        eligible.append({"name": name, "distance": distance, "gpa": gpa})


eligible.sort(key=lambda student: (-student["distance"],

                                   -student["gpa"],

                                   student["name"].lower()))

allocated = eligible[:rooms]

not_allocated = eligible[rooms:]


print("Hostel room allocation:")

if allocated:

    for room_number, student in enumerate(allocated, start=1):

        print(f"Room {room_number}: {student['name']} - "

              f"{student['distance']} km, GPA {student['gpa']:.1f}")

else:

    print("No rooms allocated.")


print("Eligible but not allocated:")

if not_allocated:

    for student in not_allocated:

        print(f"{student['name']} - {student['distance']} km, "

              f"GPA {student['gpa']:.1f}")

else:

    print("None")

