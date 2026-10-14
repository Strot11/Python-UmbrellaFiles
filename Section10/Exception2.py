# Try Except else and finally

chai ={"masala": 100, "ginger": 80}

try:
    chai["clove"]
except KeyError:
    print("Key not found")

print("Program continues")

# Complex

def serve_chai(flavor):
    try:
        print(f"Preparing {flavor} chai...")
        if flavor == "unknown":
            raise ValueError("Flavor not available")
    except ValueError as e:
        print(f"Error: {e}")
    else:
        print(f"{flavor} chai is ready!")
    finally:
        print("Thank you for your order!")

serve_chai("masala")
serve_chai("unknown")