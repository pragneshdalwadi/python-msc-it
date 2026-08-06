# Missing Roll Number
# Roll numbers should be from 1 to N.
# One roll number is missing.
# Find the missing roll number without sorting.
# Example:
# 1 2 3 5 6
# Output:
# 4

Roll = input("Enter all roll numbers separated by space: ")

present = input("Enter present roll numbers separated by space:")

print("Absent Roll Numbers:")

for r in Roll:
    if r not in present:
        print(r)