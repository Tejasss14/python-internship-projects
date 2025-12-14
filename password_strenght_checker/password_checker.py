import re

def check_password_strength(password):
    if len(password) < 8:
        return "Weak password: must be at least 8 characters long"

    if not re.search(r"[A-Z]", password):
        return "Weak password: must contain at least one uppercase letter"

    if not re.search(r"[0-9]", password):
        return "Weak password: must contain at least one number"

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Weak password: must contain at least one special character"

    return "Strong password"


user_password = input("Enter your password: ")
result = check_password_strength(user_password)
print(result)
