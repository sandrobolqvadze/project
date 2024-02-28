# Check for number input
def check_input_number(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
    
 # # # ეს ფუნქცია ამოწმებს რომ მივიღოდ რიცხვი Int ან float

# # # ---------------   

# function for add operation
def add(x, y):
    return x + y

# function for minus operation
def minus(x, y):
    return x - y

# function for multiply operation
def multiply(x, y):
    return x * y

# function for divide operation
def divide(x, y):
    if y != 0:
        return x / y
    else:
        raise ZeroDivisionError("Error: ნულზე გაყოფა არ შეიება!")   


#პირველი და მეორე რიცხვის მიღება / შემოწმება ( სანამ რიცხვს არ მიიღებს ატრიალებს ციკლში)
number_1 = input("Please input first number: ")
while not check_input_number(number_1):
    print("Error: Please input a valid number!")
    number_1 = input("Please input first number: ")

number_2 = input("Please input second number: ")
while not check_input_number(number_2):
    print("Error: Please input a valid number!")
    number_2 = input("Please input second number: ")

## შესასრულებელი ოპერაციის შემოწმება ( სანამ 4 მისაღები ვარიანტიდან ერთ-ერთს არ აირჩევს იტრიალებს ციკლში)
while True:
    try:
        qmedeba = input("Please choose operation (+, -, *, /): ")

        if qmedeba == '+':
            res = add(float(number_1), float(number_2))
        elif qmedeba == '-':
            res = minus(float(number_1), float(number_2))
        elif qmedeba == '*':
            res = multiply(float(number_1), float(number_2))
        elif qmedeba == '/':
            res = divide(float(number_1), float(number_2))
        else:
            print("Error: Choose the right operation.")
            continue
        break            # # # სასურველი ნიშნის მიღების შემდეგ გამოდის ციკლიდან

    except KeyboardInterrupt as ex:
        print("\nProgramm closed by user (Ctrl+C)")
        break

#ტერმინალში შედეგის დაბეჭდვა
print(f"total = {res}")
