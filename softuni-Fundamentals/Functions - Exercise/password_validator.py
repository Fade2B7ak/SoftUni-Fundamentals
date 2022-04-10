def validator(password):

    is_true = True

    if 10 > len(password) < 6:
        is_true = False
        print("Password must be between 6 and 10 characters")
    if not str.isalnum(password) and not str.isalpha(password):
        is_true = False
        print("Password must consist only of letters and digits")

    if sum(map(str.isdigit, password)) < 2:
        is_true = False
        print("Password must have at least 2 digits")

    if is_true:
        print("Password is valid")

passa = input()
validator(passa)