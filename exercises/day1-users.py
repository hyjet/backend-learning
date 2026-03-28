users = [
    {"name": "Kevin", "age": 30},
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 17},
    {"name": "Charlie", "age": 9},
    ]

def filter_adults(users):
    """Return a list of users who are 21 or older."""
    return [user for user in users if user["age"] >= 21]

if __name__ == "__main__":
    adults = filter_adults(users)
    for user in adults:        print(f"{user['name']} is an adult.")