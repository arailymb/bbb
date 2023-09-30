# Task 1.1: Print sequence with spaces
def task_1_1():
    sequence = [4, 8, 15, 16, 23, 42]
    print(f"{sequence[0]} {sequence[1]} {sequence[2]} {sequence[3]} {sequence[4]} {sequence[5]}")

# Task 1.2: Print sequence on separate lines
def task_1_2():
    sequence = [4, 8, 15, 16, 23, 42]
    for num in sequence:
        print(f"{num}")

# Task 1.3: User input and next two numbers
def task_1_3():
    try:
        user_input = int(input("Please enter the first number: "))
        print(f"{user_input}")
        print(f"{user_input + 1}")
        print(f"{user_input + 2}")
    except:
        print("Invalid input. Please enter a number.")

# Task 1.4: Input three numbers and print their sum
def task_1_4():
    try:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        c = int(input("Enter the third number: "))
        result = a + b + c
        print(f"{result}")
    except:
        print("Invalid input. Please enter numbers only.")

# Task 1.5: Compute cube's volume and surface area
def task_1_5():
    try:
        edge = int(input("Enter the edge length of the cube: "))
        volume = edge ** 3
        surface_area = 6 * edge ** 2
        print(f"Volume = {volume}")
        print(f"Total surface area = {surface_area}")
    except:
        print("Invalid input. Please enter a valid edge length.")

# ... (Task 1 functions remain as above)

# Task 2.1: Divide tangerines among schoolchildren
def task_2_1():
    try:
        n = int(input("Enter the number of schoolchildren: "))
        k = int(input("Enter the number of tangerines: "))
        print(k // n)  # tangerines each student gets
        print(k % n)  # tangerines remaining
    except:
        print("Invalid input. Please enter valid numbers.")

# Task 2.2: Extract digits from a four-digit number
def task_2_2():
    try:
        number = int(input("Enter a four-digit number: "))
        print(f"The digit in the thousands position is {number // 1000}")
        print(f"The number in the hundreds position is {(number % 1000) // 100}")
        print(f"The digit in the tens position is {(number % 100) // 10}")
        print(f"The digit in the position of units is {number % 10}")
    except:
        print("Invalid input. Please enter a four-digit number.")

# Task 2.3: Calculate survivors after Thanos's snap
def task_2_3():
    try:
        population = int(input("Enter the population of the universe: "))
        survivors = (population + 1) // 2
        print(survivors)
    except:
        print("Invalid input. Please enter a number.")

# Task 2.4: Perform "<<" operation on an input number
def task_2_4():
    try:
        number = int(input("Enter a number: "))
        result = number << 1
        print(f"The result of << is {result}")
    except:
        print("Invalid input. Please enter a number.")

# Task 2.5: Basic calculator using "if" statements
def task_2_5():
    try:
        num1 = float(input("Please enter the first number: "))
        num2 = float(input("Please enter the second number: "))
        operation = input("Please choose the operation (+, -, *, /): ")

        if operation == "+":
            print(num1 + num2)
        elif operation == "-":
            print(num1 - num2)
        elif operation == "*":
            print(num1 * num2)
        elif operation == "/":
            if num2 != 0:
                print(num1 / num2)
            else:
                print("Cannot divide by zero.")
        else:
            print("Invalid operation. Choose +, -, *, or /.")
    except:
        print("Invalid input. Please ensure numbers are entered correctly.")

# Run each task
task_1_1()
task_1_2()
task_1_3()
task_1_4()
task_1_5()
task_2_1()
task_2_2()
task_2_3()
task_2_4()
task_2_5()
