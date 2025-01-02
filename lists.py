#LISTS

names = ["John", "Maria", "Giorgos", "Antonia", "Despina"]
print(names)
#index position ,zero is the first always. if you write negative it will loop from the end
print(names[0])
print(names[-1])
print(names[-2])
print(names[2])
print(names[1])
#change indexe's name to another name:
print("Change index of listin position 1 from Maria to :")
names[1] = "Alex"
print(names[1])

#print elements- indexes from 0 till 2 index - without 3:
print(names[0:3])

#append function in list
numbers= [1,2,3,4,5,6]
print(numbers)
numbers.append(7)
print(numbers)

#Insert method Python command & p to check what it expects me to insert

numbers.insert(2,15)
print("new numbers list with insert method is:")
print(numbers)
#Remove method Python
print("Remove index 4 from numbers:")
numbers.remove(4)
print(numbers)
#Clear list with clear method:

print("Clear numbers list with clear method:")
numbers.clear()
print(numbers)


#Let's check if a value exists in a list: (True or False result)

list_1 = [1,2,3,4,5,6]
print( 6 in list_1)
print(10 in list_1)

#Lenght in a list
list_2 = [2,3,4,5,6,7,8]
print(len(list_2))

#Loop in lists (For loop)

list_3 = [1,2,3,4,5,6]
for item in list_3:
    print(item)
#Loop in lists (While  loop)

i=0
while i < len(list_3):
    print(list_3[i])
    i = i + 1

