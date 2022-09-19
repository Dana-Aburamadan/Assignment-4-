List_of_Numbers = []

while len(List_of_Numbers) < 5:
    numbers = float(input("enter any number: "))
    List_of_Numbers.append(numbers)

print(List_of_Numbers)
print(max(List_of_Numbers))
print(min(List_of_Numbers))