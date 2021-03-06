# HW1 by Sungin Jung
# This program converts Fahrenheit to Celsius.
# The textbook says Fahrenheit = 9/5 * celsius + 32.
# Thus, Celsius = (Fahrenheit - 32) * 5/9

def main():
    # Introduction
    print("**********************************************")
    print("*        Welcome to the                      *")
    print("*           Temperature Converter            *")
    print("*                by Sungin Jung              *")
    print("**********************************************")
    print()
    print("This will convert Fahrenheit to Celsius")
    print()

    # Ask user to enter Fahrenheit
    fahrenheit = eval(input("Enter Fahrenheit degree: "))
    print()

    # Convert it to celsius using the formula stated in the comment
    celsius = (fahrenheit-32) * (5/9)
    celsius_round = round(celsius,2)

    # Print outcome
    print(fahrenheit, "fahrenheit degree is", celsius_round, "celsius degree.")

main()
