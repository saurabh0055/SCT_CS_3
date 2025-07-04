import re

def check_password_strength(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    errors = {
        "Too short (min 8 characters)": length_error,
        "Missing digit": digit_error,
        "Missing uppercase letter": uppercase_error,
        "Missing lowercase letter": lowercase_error,
        "Missing special character": symbol_error,
    }

    score = 5 - sum(errors.values())

    if score == 5:
        strength = "Very Strong"
    elif score >= 4:
        strength = "Strong"
    elif score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"

    return strength, errors

if __name__ == "__main__":
    password = input("Enter your password: ")
    strength, issues = check_password_strength(password)

    print(f"\nPassword Strength: {strength}\n")
    print("Details:")
    for issue, failed in issues.items():
        if failed:
            print(f" - {issue}")