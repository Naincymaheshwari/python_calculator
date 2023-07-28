def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise Exception("Cannot divide by zero.")
    return x / y

def mod(x,y):
    return x % y

def pow(x,y):
    return x ** y

def calculator():
    print("Simple Calculator")
    print("Options:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Remainder")
    print("6. Power")
    print("7. Exit")

    while True:
        choice = input("Enter your choice (1/2/3/4/5/6/7): ")

        if choice == '7':
            print("Exiting the calculator.")
            break

        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == '1':
                result = add(num1, num2)
            elif choice == '2':
                result = subtract(num1, num2)
            elif choice == '3':
                result = multiply(num1, num2)
            elif choice == '4':
                result = divide(num1, num2)
            elif choice == '5':
                result = mod(num1, num2)
            elif choice == '6':
                result = pow(num1, num2)
            else:
                print("Invalid input. Please try again.")
                continue

            print("Result:", result)

        except Exception as ve:
            print("Error:", ve)
        except Exception as e:
            print("An error occurred:", e)

if __name__ == "__main__":
    calculator()
