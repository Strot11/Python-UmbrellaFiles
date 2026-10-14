# Generators Yield

# def count_up_to(limit):
   # count = 1
    # while count <= limit:
       #  yield count  # Pauses execution and returns the value
        # count += 1   # Resumes here on the next call

# Initialize the generator object
# counter = count_up_to(3)

# Accessing values one by one
# print(next(counter))  # Output: 1
# print(next(counter))  # Output: 2
# print(next(counter))  # Output: 3
# Calling next() again will raise a StopIteration exception automatically.

def infinite_chai(limit):
    count = 1
    while count<=limit:
        yield f"Refill #{count}"
        count+=1

refill = infinite_chai(5)
user2 = infinite_chai(6);

for _ in range(3):
    print(next(refill)) #The next() function manually requests the next single item from an iterator or generator.

for _ in range(3):
    print(next(user2))