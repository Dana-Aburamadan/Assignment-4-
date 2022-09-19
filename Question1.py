name = input("Enter your name: ")
age = int(input("Enter your age: "))
address = input("Enter your address: ")

if name == "" or age == "" or address == "":
    print("Error, please fill all spaces")

else:
    print("Hello Mr/Ms " + name + " age " + str(age) + " located in " + address + "." +
      " Thanks for being one of our community,   Enjoy")
