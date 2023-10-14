number = int(input("Enter a number to generate a multiplication table: "))

print("Multiplication table for",number,":")

for i in range(0, 10):
    prod = number * (i+1)
    print(number,"x",i+1,"=",prod)