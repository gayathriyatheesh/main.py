n = int(input("Enter number of students: "))

marks = [0] * n
valid = 0
failed = 0

for i in range(n):
    marks[i] = int(input("Enter mark: "))

for mark in marks:
    if mark < 0 or mark > 100:
        result = "Invalid"
    elif mark >= 90:
        result = "Excellent"
        valid += 1
    elif mark >= 75:
        result = "Very Good"
        valid += 1
    elif mark >= 60:
        result = "Good"
        valid += 1
    elif mark >= 40:
        result = "Average"
        valid += 1
    else:
        result = "Fail"
        valid += 1
        failed += 1

    print("Mark:", mark, "->", result)

print("Final Summary:")
print("Total Valid Students:", valid)
print("Total Failed Students:", failed)
