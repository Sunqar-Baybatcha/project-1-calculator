"""
Simple Calculator App
Автор: Байбатча Сұңқар
Сипаттама: Терминалда жұмыс істейтін қарапайым калькулятор.
Қосу, азайту, көбейту, бөлу, дәрежеге шығару және түбір алу амалдарын қолдайды.
"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Нөлге бөлуге болмайды!")
    return a / b


def power(a, b):
    return a ** b


def square_root(a):
    if a < 0:
        raise ValueError("Теріс саннан түбір алуға болмайды!")
    return a ** 0.5


OPERATIONS = {
    "1": ("Қосу (+)", add, 2),
    "2": ("Азайту (-)", subtract, 2),
    "3": ("Көбейту (*)", multiply, 2),
    "4": ("Бөлу (/)", divide, 2),
    "5": ("Дәрежеге шығару (^)", power, 2),
    "6": ("Квадрат түбір (√)", square_root, 1),
}


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Қате! Тек сан енгізіңіз.")


def main():
    print("=" * 40)
    print("       ҚАРАПАЙЫМ КАЛЬКУЛЯТОР")
    print("=" * 40)

    while True:
        print("\nАмалды таңдаңыз:")
        for key, (name, _, _) in OPERATIONS.items():
            print(f"  {key}. {name}")
        print("  0. Шығу")

        choice = input("\nТаңдау: ").strip()

        if choice == "0":
            print("Сау болыңыз!")
            break

        if choice not in OPERATIONS:
            print("Қате таңдау, қайта көріңіз.")
            continue

        name, func, arg_count = OPERATIONS[choice]

        try:
            if arg_count == 2:
                a = get_number("Бірінші сан: ")
                b = get_number("Екінші сан: ")
                result = func(a, b)
            else:
                a = get_number("Сан: ")
                result = func(a)

            print(f"\n>>> Нәтиже: {result}")

        except ValueError as e:
            print(f"Қате: {e}")


if __name__ == "__main__":
    main()