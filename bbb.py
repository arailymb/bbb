# Task 1

# Task 1.1
def task_1_1():
    try:
        sequence = [4, 8, 15, 16, 23, 42]
        formatted_sequence = ' '.join(map(str, sequence))
        print(f"{formatted_sequence}")
    except Exception as e:
        print(f"An error occurred: {e}")


# Task 1.2
def task_1_2():
    try:
        sequence = [4, 8, 15, 16, 23, 42]
        for number in sequence:
            print(f"{number}")
    except Exception as e:
        print(f"An error occurred: {e}")


# Task 1.3
def task_1_3():
    try:
        user_input = int(input("Please enter the first number: "))
        print(user_input)
        print(user_input + 1)
        print(user_input + 2)
    except ValueError as ve:
        print(f"An error occurred: {ve}")


# Task 1.4
def task_1_4():
    try:
        numbers = [int(input(f"Enter integer {i+1}: ")) for i in range(3)]
        print(sum(numbers))
    except ValueError as ve:
        print(f"An error occurred: {ve}")


# Task 1.5
def task_1_5():
    try:
        edge_length = int(input("Enter the edge length of the cube: "))
        volume = edge_length**3
        surface_area = 6 * (edge_length**2)
        print(f"Volume = {volume}")
        print(f"Total surface area = {surface_area}")
    except ValueError as ve:
        print(f"An error occurred: {ve}")


# Task 2

# Task 2.1
def task_2_1():
    try:
        n = int(input("Enter the number of schoolchildren: "))
        k = int(input("Enter the number of tangerines: "))
        print(k // n)
        print(k % n)
    except ValueError as ve:
        print(f"An error occurred: {ve}")


# Task 2.2
def task_2_2():
    try:
        number = int(input("Enter a four-digit number: "))
        if 999 < number < 10000:
            print(f"The digit in the thousands position is {number // 1000}")
            print(f"The digit in the hundreds position is {(number % 1000) // 100}")
            print(f"The digit in the tens position is {(number % 100) // 10}")
            print(f"The digit in the position of units is {number % 10}")
        else:
            print("The entered number is not a four-digit number.")
    except ValueError as ve:
        print(f"An error occurred: {ve}")


# Task 2.3
def task_2_3():
    try:
        population = int(input("Enter the population of the universe: "))
        survivors = (population + 1) // 2
        print(survivors)
    except ValueError as ve:
        print(f"An error occurred: {ve}")


# Task 2.4
def task_2_4():
    try:
        number = int(input("Enter a number: "))
        result = number << 1
        if result == 0:
            print("The result of << is 0. Warning: Result is zero!")
        else:
            print(f"The result of << is {result}")
    except ValueError as ve:
        print(f"An error occurred: {ve}")


# Task 2.5
def task_2_5():
    try:
        num1 = float(input("Please enter the first number: "))
        num2 = float(input("Please enter the second number: "))
        operation = input("Please choose the operation (+, -, *, /): ")

        if operation == '+':
            print(f"{num1} + {num2} = {num1 + num2}")
        elif operation == '-':
            print(f"{num1} - {num2} = {num1 - num2}")
        elif operation == '*':
            print(f"{num1} * {num2} = {num1 * num2}")
        elif operation == '/':
            if num2 != 0:
                print(f"{num1} / {num2} = {num1 / num2:.3f}")
            else:
                print("Error: Division by zero!")
        else:
            print("Invalid operation entered!")
    except ValueError as ve:
        print(f"An error occurred: {ve}")


# Driver code to execute each task
if __name__ == "__main__":
    tasks = [task_1_1, task_1_2, task_1_3, task_1_4, task_1_5, task_2_1, task_2_2, task_2_3, task_2_4, task_2_5]
    
    for i, task in enumerate(tasks, 1):
        print(f"Executing Task {i}:\n{'-'*20}")
        task()
        print('\n')

