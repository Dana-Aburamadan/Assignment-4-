number1 = input("enter the first number: ")
check = number1.isdigit() or number1.isdecimal()
if check == True:
    print("1_ +")
    print("2_ -")
    print("3_ *")
    print("4_ /")
    print("5_ ^")
    print("6_ %")

    choice = input("enter your choice: ")

    number2 = input("enter the second number: ")
    check2 = number2.isdigit() or number2.isdecimal()
    if check2 == True:
        if choice == "1" or choice == "+":
            The_result = float(number1) + float(number2)
            print(The_result)
        elif choice == "2" or choice == "-":
            The_result = float(number1) - float(number2)
            print(The_result)
        elif choice == "3" or choice == "*":
            The_result = float(number1) * float(number2)
            print(The_result)
        elif choice == "4" or choice == "/":
            The_result = float(number1) / float(number2)
            print(The_result)
        elif choice == "5" or choice == "^":
            The_result = int(number1) ^ int(number2)
            print(The_result)
        elif choice == "6" or choice == "%":
            The_result = float(number1) % float(number2)
            print(The_result)

        print("A. normal round")
        print("B. round up")
        print("C. round down")
        print("D. The number without decimmal point")
        print("E. Exit")

        The_next_step = input("enter any choice: ")
        if The_next_step == "A":
            print(The_result.__round__())
        elif The_next_step == "B":
            print(The_result.__ceil__())
        elif The_next_step == "C":
            print(The_result.__floor__())
        elif The_next_step == "D":
            print(int(The_result))
        elif The_next_step == "E":
            print(The_result)
    else:
        print("Try again and please, make sure that you entered a number")

 
else:
    print("Try again and please, make sure that you entered a number")








