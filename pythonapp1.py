patient_name = "John Smith"
patient_age = 20
patient_condition = "new"

if patient_name == "John Smith":
  print("Patient is " + patient_name )
  print("Patient's age is:")
  print(patient_age)
  #Input in Python
patient_condition = input("Give me patients condition: ")
#String concatenation
print("Patient's condition is: " + patient_condition)
#IF condition
if patient_condition != "old" :
    print("patient just came in")
    #Change variables types to str(),bool() ,int(),float()
    birth_year = input("enter your birth year: ")
    age = 2024 - int(birth_year)
    print(age)

    first_number = input("give me first number: ")
    float(first_number)
    second_number = input("Give me second number: ")
    int(second_number)
    sum = float(first_number) + int(second_number)
    print("Sum is:")
    print(sum)
#IF elif else
temperature = 30

if temperature > 30 :
    print("It's a nice day today")
elif temperature > 20:
    print("day is ok")
elif temperature > 10:
    print("Its a bit cold")
else:
    print("It's cold")


    #weight exersise
#i use float because input result always is int and i can't do maths with this.

weight = float(input("What's your weight: "))
unit = input("is your weight on (K)g or (L)bs: ")
    #i use unit.upper to change input in upper letter in case the user writes lower case letter.
if unit.upper() == "K":
        converted = weight / 0.45
        #i use str() to convert float number back to str to be able to concatinate.
        print("Weight in  Lbs is: " + str(converted))
elif unit.upper() == "L":
        converted = weight * 0.45
        print ("Your weight in Kg is:" + str(converted))

#WHILE LOOPS

i = 1
while i <= 5:
    print (i * "*")
    i = i+1
#LISTS

names = ["John", "Maria", "Giorgos", "Antonia", "Despina"]
print(names)
#index position ,zero is the first always. if you write negative it will loop from the end
print(names[0])
print(names[-1])
#Change index:
names[o] = "Johnny"
