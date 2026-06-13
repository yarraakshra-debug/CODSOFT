import random
import string

print("=== PASSWORD GENERATOR ===")

length = int(input("Enter the desired password length: "))

if length < 4:
    print("Password length should be at least 4.")
else:
    lowercase = random.choice(string.ascii_lowercase)
    uppercase = random.choice(string.ascii_uppercase)
    digit = random.choice(string.digits)
    special = random.choice(string.punctuation)

    remaining = length - 4

    all_characters = (
        string.ascii_lowercase +
        string.ascii_uppercase +
        string.digits +
        string.punctuation
    )

    password_list = [lowercase, uppercase, digit, special]

    for _ in range(remaining):
        password_list.append(random.choice(all_characters))

    random.shuffle(password_list)

    password = "".join(password_list)

    print("\nGenerated Password:")
    print(password)