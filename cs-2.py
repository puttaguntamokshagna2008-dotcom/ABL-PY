password = input("Enter password: ")
errors = []

if len(password) < 6 or len(password) > 8:
    errors.append("Password must be 6 to 8 characters long.")

if not all(('A' <= ch <= 'Z') or ('0' <= ch <= '9')
           for ch in password):
    errors.append("Use uppercase letters (A-Z) and digits (0-9).")

if not any('0' <= ch <= '9' for ch in password):
    errors.append("Password must contain at least one digit.")

if len(errors) == 0:
    print("Password is valid.")
else:
    print("Password is invalid.")
    for error in errors:
        print("-", error)