
#simple input

name = input("What is your name? ")
color = input ("what is your favourite color? ")
print(name + " likes " + color)

#simple input + convert to int  | int(variable) , float(var) ,str(var) , bool(var) & type or var,

birth_year = input("What year you were born? ")
print(type(birth_year))  #printing type of variable birth_year
age = 2024 - int(birth_year)
print(age)

# Formated String

first = "John"
second = "Mitsis"
#give me message  " John  [Mitsis] is a coder" with f string :
msg = first + " ["+ second + "]" + " is a coder"
message = f"{first} [{second}] is a coder" # here
print(message)
print("this should be the message: "+ msg)

# String methods:  len function in strings:

var_23 = "This is a string"
print(var_23)
print("The lenght of this text is: ")
print (len(var_23))

#upper & lower methods case strings:

print(var_23.upper())
print(var_23.lower())
print(var_23)
#find the index of the character in string var_23:
print(var_23.find("i"))
#find the replace of the character in string var_23:
print(var_23.replace("string", "small string"))

#Check if something exists in a string with boolean true or false:
print("Is phrase 'This' in this string ? ")
print ("This" in var_23)


#Arithmetic

print(10 + 3)
print(10*30)
print(10 / 3) #. this gives us float
print(10 // 3) #this gives us int
print(10 % 3) #reminder of the division
print (10 ** 3) #to the power

x = 10
x = x + 3
# or you write
x += 3
print(x)


# Round arithmetics
print("Round number of 2.9 is:")
x = 2.9
print(round(x))
# absolut arithmetics
print(abs(x))



# If statment exersises


is_hot = False
is_cold = True

if is_hot :
    print("I'ts a hot day")
    print("drink alot of water")
elif is_cold:
    print("It's a cold day")
    print("wear warm clothes")
else:
    print("It's a lovely day")

# If statment exersises 2
price = 1000000
has_good_credit = True

if has_good_credit :
    down_payment = 0.1 * price

else:
    down_payment = 0.2 * price
print(f"down payment: $ {down_payment}")

#Logical Operations:
#If he has high income & good credit he is eligible for loan.

has_high_income = True
has_good_credit = True

if has_high_income and has_good_credit:
    print("Eligible for loan")
#Logical Operations:
#If he has  good credit and NOT criminal record he is eligible for loan.

criminal_record = False
has_good_credit = True

if  has_good_credit and not criminal_record:
    print("Eligible for loan")

#Comparison  Operators

name = "John"

if len(name) < 3 :
    print("Name must be at least 3 characters")
elif len(name) > 50:
    print("Name must be maximum of 50 characters")
else:
    print("name looks ok")



# Weight converter programm

weight_1 =  int(input("Weight "))
unit_1 = input( "(L)bs or (K)g : ")
if unit_1.upper() == "L" :  #i do it upper letter with .upper
   converted_weight = weight_1 * 0.45
   print(f"You are {converted_weight} kilos")
else:
    converted_weight = weight_1 / 0.45  # with / you get float number , with // you get int number
    print(f"You are {converted_weight} pounds")
