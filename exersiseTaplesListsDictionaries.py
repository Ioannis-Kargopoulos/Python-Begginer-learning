#lists and taples exersise

#create list of names and print second index
names = ["John", "Maria", "Amalia"]
print(names[1])

#create list of sports and replace second sport.
sports = ["basketball", "Football", "Baseball"]
sports[1] = "Volleyball"
print(sports[1])

#create number list and delete 5th number from array
numbers_list1 = [1, 2 ,3 ,4 ,5 ,6,7]
print(numbers_list1)
del numbers_list1[4]
print(numbers_list1)

#create two lists of numbers and merge them

list_one = [1, 2 ,3]
list_two = [5, 6, 7]
list_sum = list_one + list_two
print(list_sum)

#create a list of numbers and find lenght ,min and max

list_of_numbers = [1, 2, 3, 6, 9, 10, 11]
len(list_of_numbers)
print(len(list_of_numbers))
print(min(list_of_numbers))
print(max(list_of_numbers))

#create dictionary of students and sxores and print out student's score.

students = {"Avi": 94 , "Jack": 61 , "Anna": 15}
print(students["Avi"])

#create dictionary with key being names and values being ages and delete sexond key/value pair.
#create dicctionary of names with ages and print all keys and values.
print("Dictionary print")
data = {"Rachal": 22 , "John": 38 , "Anna": 27 }
del data["John"]
print(data.keys())
print(data.values())
print(data)

#tuples - create tuple with movies and print items & print items 1&2 - so 0 and 1,not 2:

tup_movies = ("Taken1", "Armagedon", "Gladiator")
print(tup_movies)
print(tup_movies[0:2])



