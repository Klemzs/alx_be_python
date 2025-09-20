number = int(input("Enter a number to see its multiplication table: "))

for i in range(0,10):
    i += 1
    product = number * i
    print(f"{number} * {i} = {product}")
print()
