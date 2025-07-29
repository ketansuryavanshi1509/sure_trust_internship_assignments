import re

def password_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if re.search(r'[A-Z]', password):
        score += 1
    if re.search(r'[a-z]', password):
        score += 1
    if re.search(r'\d', password):
        score += 1
    if re.search(r'[!@#$%^&*()\-_=+]', password):
        score += 1

    if score == 5:
        return 'Strong'
    elif score >= 3:
        return 'Moderate'
    else:
        return 'Weak'

# Example
# pwd = input("Enter password: ")
# print("Strength:", password_strength(pwd))
