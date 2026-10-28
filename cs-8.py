def read_nonnegative_int(prompt):

    while True:

        try:

            value = int(input(prompt))

            if value >= 0:

                return value

            print("Enter zero or a positive whole number.")

        except ValueError:

            print("Enter a whole number.")


while True:

    try:

        team_count = int(input("Number of teams: "))

        if 2 <= team_count <= 30:

            break

        print("Enter a number from 2 to 30.")

    except ValueError:

        print("Enter a whole number.")


teams = []

for i in range(team_count):

    name = input(f"Team {i + 1} name: ").strip()

    wins = read_nonnegative_int("Wins: ")

    draws = read_nonnegative_int("Draws: ")

    losses = read_nonnegative_int("Losses: ")

    goals_for = read_nonnegative_int("Goals for: ")

    goals_against = read_nonnegative_int("Goals against: ")


    points = wins * 3 + draws

    goal_difference = goals_for - goals_against

    teams.append({"name": name, "points": points,

                  "goal_difference": goal_difference,

                  "goals_for": goals_for, "wins": wins})


teams.sort(key=lambda team: (-team["points"],

                             -team["goal_difference"],

                             -team["goals_for"],

                             team["name"].lower()))


print("Final tournament ranking:")

for rank, team in enumerate(teams, start=1):

    print(f"{rank}. {team['name']} - {team['points']} points, "

          f"GD {team['goal_difference']}, GF {team['goals_for']}")

