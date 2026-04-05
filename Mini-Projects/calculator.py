def get_number(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


def add():
    a = get_number("Enter first number: ")
    b = get_number("Enter second number: ")
    print(f"Result: {a} + {b} = {a + b}")


def subtract():
    a = get_number("Enter first number: ")
    b = get_number("Enter second number: ")
    print(f"Result: {a} - {b} = {a - b}")


def multiply():
    a = get_number("Enter first number: ")
    b = get_number("Enter second number: ")
    print(f"Result: {a} * {b} = {a * b}")


def divide():
    a = get_number("Enter first number: ")
    b = get_number("Enter second number (non-zero): ")
    if b == 0:
        print("Error: Division by zero is not allowed.")
        return
    print(f"Result: {a} / {b} = {a / b}")


def show_menu():
    print("\n=== Python Calculator ===")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")


def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add()
        elif choice == "2":
            subtract()
        elif choice == "3":
            multiply()
        elif choice == "4":
            divide()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a number from 1 to 5.")


if __name__ == "__main__":
    main()

