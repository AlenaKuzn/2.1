a2 = int(input("Enter number of tithes "))
a1 = int(input("Enter the number of units "))
b = int(input("Enter a single digit "))
n = a2 + (a1 + b) // 10
m = (a1 + b) % 10
print("Result", n, m)