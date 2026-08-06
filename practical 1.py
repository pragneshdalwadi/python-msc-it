# Consecutive Duplicate Detector
# Accept N integers.
# Display only those numbers that appear consecutively more than once.
# Input:
# 1 2 2 3 4 4 4 5
# Output:
# 2
# 4

N = str(int(input("Enter The N : ")))

ls = []

for i in N:
    count = N.count(i)

    if count > 1 and i not in ls:
        ls.append(i)
    else:
        continue

print(ls)