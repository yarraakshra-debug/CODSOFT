num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Choose operation")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5.Exit")
choice = input("Enter choice (1/2/3/4/5): ")
if choice == "1":
    print("Result =", num1 + num2)
elif choice == "2":
    print("Result =", num1 - num2)
elif choice == "3":
    print("Result =", num1 * num2)
elif choice == "4":
    if num2 != 0:
        print("Result =", num1 / num2)
    else:
        print("Cannot divide by zero")
elif choice =="5":
    print("Thank you!")
    exit()
else:
    print("Invalid choice")
