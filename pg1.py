n = int(input("Enter the val = "))
prod = 1
s = ""
for i in range(1, n + 1):
    prod *= i
    s += str(i) + "*"
print("Factorial of {0} is {1} = {2}".format(n, s[:-1], prod))
