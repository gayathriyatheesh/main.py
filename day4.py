data = []

n = int(input("Enter number of elements: "))

for i in range(n):
    value = input("Enter element: ")
    data.append(value)

number_list = []
string_list = []

total_numbers = 0
total_strings = 0

for element in data:
    if element == "":
        continue

    is_number = True
    dot_count = 0

    for ch in element:
        if ch == ".":
            dot_count = dot_count + 1
        elif ch < "0" or ch > "9":
            is_number = False

    if is_number == True and dot_count <= 1:
        number_list.append(element)
        total_numbers = total_numbers + 1
    else:
        string_list.append(element)
        total_strings = total_strings + 1


name = input("Enter your name: ")

if len(name) % 2 == 0:
    if len(number_list) > 0:
        number_list.pop(0)
    if len(string_list) > 0:
        string_list.pop(0)
else:
    if len(number_list) > 0:
        number_list.pop()
    if len(string_list) > 0:
        string_list.pop()


print("Numbers List:", number_list)
print("Strings List:", string_list)
print("Total Numbers:", total_numbers)
print("Total Strings:", total_strings)
