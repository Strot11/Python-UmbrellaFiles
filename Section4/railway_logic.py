seat = input("Enter the seat type (SLEEPER/AC/GENERAL/LUXUARY) : ").upper()

match seat:
    case "SLEEPER":
        print("Sleeper Coach Opted")
    case "AC":
        print("AC Coach Opted")
    case "GENERAL":
            print("GENERAL Coach Opted")
    case "LUXUARY":
            print("LUXUARY Coach Opted")
    case _:
            print("Invalid Seat Type")
