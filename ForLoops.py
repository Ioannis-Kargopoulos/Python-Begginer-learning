#ForLoops

for item in ["John", "Giorgios", "Maria"]:
    print(item)



for item_3 in range(5, 10, 2):  #range from 5 to 10 with step 2
    print(item_3)

#calculate total cost of shopping cart

prices = [10, 20 ,30]
total = 0

for price in prices:
    total += price #total + price
    print(f"Total is: {total}")

#NestedLoops
for x in range(4):
    for y in range(3):
        print(f"({x} , {y})")

#nested exersise with list

numbers = [ 5, 2, 5, 2, 2]

for x_count in numbers:   #  print("x" * x_count)
    output = ''
    for count in range(x_count):
        output += 'x'
        print(output)

