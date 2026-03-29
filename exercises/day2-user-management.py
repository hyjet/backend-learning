users = [
    {"name": "Kevin", "age": 30},
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 17},
    {"name": "Charlie", "age": 9},
]

def get_adults(users):
    return [user for user in users if user["age"] >= 21]


def get_minors(users):
    return [user for user in users if user["age"] < 21]


def get_average_age(users):
    return sum(user["age"] for user in users) / len(users)


def find_oldest_user(users):
    return max(users, key=lambda user: user["age"])


def find_user_by_name(users, name):
    for user in users:
        if user["name"] == name:
            return user
    return None

if __name__ == "__main__":
    adults = get_adults(users)
    minors = get_minors(users)
    average_age = get_average_age(users)
    oldest_user = find_oldest_user(users)
    user_named_bob = find_user_by_name(users, "Bob")

    print("Adults:")
    for user in adults:
        print(f"{user['name']} is an adult.")

    print("\nMinors:")
    for user in minors:
        print(f"{user['name']} is a minor.")

    print(f"\nAverage age: {average_age:.2f}")
    print(f"Oldest user: {oldest_user['name']} ({oldest_user['age']} years old)")
    if user_named_bob:
        print(f"Found user: {user_named_bob['name']} ({user_named_bob['age']} years old)")
    else:
        print("User named Bob not found.")