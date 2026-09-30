"""
Simple Calculator App
Author: Байбатча Сұңқар (Baybatcha Sunqar)
Description: A command-line calculator with basic arithmetic,
power, square root, and quadratic equation solving.
"""

def add(number_1, number_2):
    return number_1 + number_2

def subtract(number_1, number_2):
    return number_1 - number_2

def multiply(number_1, number_2):
    return number_1 * number_2

def divide(number_1, number_2):
    if number_2 == 0:
        raise ValueError("Division by zero is not allowed")
    return number_1 / number_2

def power(number_1, number_2):
    return number_1 ** number_2

def square_root(number_1):
    if number_1 < 0:
        raise ValueError("You cannot take the root of a negative number")
    return number_1 ** 0.5

def finding_the_root(a, b, c):
    if a == 0:
        raise ValueError("The coefficient 'a' must not be equal to 0")
    
    d = pow(b, 2) - 4 * a * c

    if d < 0:
        raise ValueError("The discriminant is negative (D < 0). There are no real roots.")
    elif d == 0:
        x_1 = -b / (2 * a)
        return [x_1]
    else:
        x_1 = (-b + d ** 0.5) / (2 * a)
        x_2 = (-b - d ** 0.5) / (2 * a)
        return [x_1, x_2]

OPERATIONS = {
    "1": ("add (+)", add, 2),
    "2": ("subtract (-)", subtract, 2),
    "3": ("multiply (*)", multiply, 2),
    "4": ("divide (/)", divide, 2),
    "5": ("power (^)", power, 2),
    "6": ("square_root (√)", square_root, 1),
    "7": ("finding_the_root (x1,x2)", finding_the_root, 3)
}

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error! Enter only numbers.")

def main():
    print("=" * 40)
    print("         Simple Calculator")
    print("=" * 40)
    while True:
        print("\nAvailable operations:")
        for key, (name, _, _) in OPERATIONS.items():
            print(f"{key}. {name}")
        print("0. Шығу")

        choice = input("\nSelect an operation (0-7): ").strip()

        if choice == "0":
            print("\nThe program has ended. Goodbye!")
            break

        if choice in OPERATIONS:
            name, func, args_count = OPERATIONS[choice]
            print(f"\n--- {name} ---")

            try:
                if args_count == 1:
                    num1 = get_number("Enter a number: ")
                    result = func(num1)
                elif args_count == 2:
                    num1 = get_number("Enter a first number: ")
                    num2 = get_number("Enter a second number: ")
                    result = func(num1, num2)
                elif args_count == 3:
                    print("Enter the coefficients for the equation ax² + bx + c = 0:")
                    a = get_number("Enter a: ")
                    b = get_number("Enter b: ")
                    c = get_number("Enter c: ")
                    result = func(a, b, c)

                print(f"Result: {result}")

            except ValueError as e:
                print(f"Error: {e}")
        else:
            print("Invalid choice! Enter only the number from the list.")

if __name__ == "__main__":
    main()
