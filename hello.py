import os

name = os.getenv("WHO_TO_GREET", "World")

print(f"Hello {name}!")
print("This program is running inside GitHub Actions.")