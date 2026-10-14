from arrow import arrow 

brewing_time = arrow.utcnow()

brewing_time = brewing_time.to("Europe/Rome")

print(f"Brewing time: {brewing_time.format('YYYY-MM-DD HH:mm:ss ZZ')}")

from collections import namedtuple

from collections import namedtuple

# 1. Define the structure (Give it a name and its fields)
User = namedtuple("User", ["name", "age", "role"])

# 2. Create an instance
user = User(name="Alice", age=30, role="Admin")

# 3. Access data cleanly using dot notation (.)
print(user.age)   # Output: 30
print(user.name)  # Output: "Alice"

#A namedtuple is a regular Python tuple that allows you to access 
# elements using readable names instead of confusing index numbers (like [0] or [1])


