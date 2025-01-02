#While Loops :
i = 1
while i <= 5:
    print("*" * i)
    i = i + 1
print("done")

#Guesh game with While loop: user gives number he has 3 choises to find number.

secret_number = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit :   #guess counts <=3
   guess = int(input("Guess: ")).  #user makes a guess
   guess_count += 1
   if guess == secret_number:
       print("You won!")
       break #Stopping the code.
else:         #else for while loop not for if
    print("Sorry you failed")

# Car Game with While loop -

command = ""
started = False
while True :   #command != "quit" with a few words.It will stop only when we write quit.
    command = input("> ").lower() #instead of writing in all command.lower to give me lower letters
    if command == "start":
        if started:  #here, if started is True we print...
            print("Car is already started")
        else:
            started = True  #here we make started = True
        print("Car started..ready to go!")
    elif command == "stop":
        if not started:
            print("Car already stopped")
        else:
            started = False
        print("The car stopped")
    elif command == "help":   #for multiple lines i write """ """" x3
        print("""         
Start - to start the car
stop - to stop the car
quit - to quit
        """)
    elif command == "quit":
        break
    else:
        print( " I don't understand that")


#FOR LOOPS
