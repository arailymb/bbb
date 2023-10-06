#task 1.1 
def task_1_1():
    numbs = [4, 8, 15, 16, 23, 42]
    for num in numbs:
        print(num, end=" ")
    print()

#task 1.2 
def task_1_2():
    numbs = [4, 8, 15, 16, 23, 42]
    for num in numbs:
        print(f"{num}")

#task 1.3 
def task_1_3():
    try:
        user_input = int(input('three consecutive numbers: '))
        print(f"{user_input}")
        print(f"{user_input + 1}")
        print(f"{user_input + 2}")
    except:
        print("Invalid input.")

#task 1.4 
def task_1_4():
    try:
        a = int(input('three integers: '))
        b = int(input())
        c = int(input())
        result = a + b + c
        print(f"{result}")
    except:
        print("Invalid input.")

#task 1.5
def task_1_5():
    try:
        edge = int(input('volume of a cube and the area of its full surface: '))
        volume = edge ** 3
        surface_area = 6 * edge ** 2
        print(f"Volume = {volume}")
        print(f"Total surface area = {surface_area}")
    except:
        print("Invalid input.")


#task 2.1
def task_2_1():
    try:
        n = int(input('children: '))
        k = int(input('tangerines: '))
        print(k // n) 
        print(k % n)  
    except:
        print("Invalid input.")

#task 2.2 
def task_2_2():
    try:
        number = int(input('four-digit number: '))
        print(f"The digit in the thousands position is {number // 1000}")
        print(f"The number in the hundreds position is {(number % 1000) // 100}")
        print(f"The digit in the tens position is {(number % 100) // 10}")
        print(f"The digit in the position of units is {number % 10}")
    except:
        print("Invalid input.")

#task 2.3
def task_2_3():
    try:
        population = int(input('population: '))
        survivors = (population + 1) // 2
        print(survivors)
    except:
        print("Invalid input.")

#task 2.4 
def task_2_4():
    try:
        number = int(input('number<<: '))
        result = number << 1
        print(f"The result of << is {result}")
    except:
        print("Invalid input.")

#task 2.5 
def task_2_5():
    try:
        num1 = float(input('number: '))
        num2 = float(input('number: '))
        operation = input("choose the operation (+, -, *, /): ")

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
            print("Invalid operation.")
    except:
        print("Invalid input.")

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
