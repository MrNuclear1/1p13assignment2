import time
import random
import math

   # choice = int(input("Enter Which Entry Option You Wish to Use: "))
#reuse above lines in the heist function cuz they go there not here :/
def enter(choice, code):
    suspicion = 0

    guard1 = random.randint(1,6)
    guard2 = random.randint(1,6)
    guard3 = random.randint(1,6)

    if guard1 > choice:
        suspicion += 1
    if guard2 > choice:
        suspicion += 1 
    if guard3 > choice:
            suspicion += 1

    print (f"{suspicion} Guards Were Alerted")

    if (choice >= 4 and code < 500):
        clue = -1
    elif (choice >= 4 and code >= 500):
        clue = -2
    else:
        clue = code//100

#   print (clue)
#  print (suspicion)
    return suspicion, clue
#Test case...
#enter(4, random.randint(100,999))

def side_room(investigate, code):
    suspicion = 0

    
    luck = random.randint(1,100)
    print("You Stumble Upon a Side Room, Its The Managers Office")
    answer = input("Investigate? True or False: ")
    investigate = (answer == "True")
    if luck > 80:
        clue = code
    elif (luck > 30 and luck < 81):
        hundreds = code//100
        tens =(code - (100*hundreds))//10
        clue = (code - (100*hundreds) - (10*tens))
    elif (luck >0 and luck < 31):
    #        print("Unlucky You Found nothing")
        clue = -1
        suspicion = math.ceil(luck / 20)
    else:
        print("You Saw a Side Room, But You Choose To Skip Past Striaght to The Vault")
        clue = -1

    return suspicion, clue

def crack_code(suspicion, code):
    maxattempts = 10 - suspicion
    newsuspicion = 0
    attemptnumber = 1
    correct = False
    print(f"You Have {maxattempts} Guesses")
    while (maxattempts > 0 and correct == False):
            
            comboguess = int(input("Enter Your Combo Guess: "))
            
            if comboguess != code:
                newsuspicion += 1
                maxattempts -= 1
                print(f"Attempt {attemptnumber}: Guess = {comboguess}, incorrect")            
            elif comboguess == code:
                print(f"Attempt {attemptnumber}: Guess = {comboguess}, Correct!!!")
                correct = True   
            attemptnumber += 1  
    if correct == False:
        newsuspicion += 3
    return newsuspicion, correct



def escape(suspicion):
    danger = suspicion // 3
    progress = 0
    
    while (danger < 10 and progress < 10):
        choice = int(input("What Action Do You Want To Take? 1 = Run, 2 = Hide, 3 = Shortcut: "))
        if choice == 1:
            gamble = random.randint(1,100)    
            if gamble <= 60:
                progress += 1
                print(f"You Run and No One See's You! Progress = {progress}, Danger = {danger}")
            else:
                progress += 1
                danger += 1
                print(f"You Run But Someone Hears You, Theyre on Your Tail! Progress = {progress}, Danger = {danger}")
        elif choice == 2:
            gamble = random.randint(1,100)    
            if gamble <= 80:
                progress += 1
                print(f"You Hide and No One See's You! Progress = {progress}, Danger = {danger}")
            else:
                danger += 2
                print(f"You Hide But Someone Is Investigating The Room! Progress = {progress}, Danger = {danger}")
        elif choice == 3:    
            gamble = random.randint(1,100)    
            if gamble <= 50:
                progress += 3
                print(f"You Take a Shortcut and it Pays Off! Progress = {progress}, Danger = {danger}")
            else:
                danger += 3
                print(f"You Take a Shortcut But Its a Deadend! Progress = {progress}, Danger = {danger}")
        else:
            print("Invalid Input, You can only enter 1,2,3")
    return progress

def heist(name):
    suspicion = 0
    print(f"Greetings {name}, Welcome To Watch Heist")
    code = random.randint(100,999)
    if DEBUG == True:
        print(code)
    print("Lets Begin")
    
    print("Option 1: Sewer") 
    print("Option 2: Vents") 
    print("Option 3: Roof Top")
    print("Option 4: Windows") 
    print("Option 5: Side Door") 
    print("Option 6: Front Door") 
    
    choice = int(input("Choose Your Entry Method, 1-6, Higher is Easier"))

    firstsuspicion, clue1 = enter(choice, code)

    suspicion += firstsuspicion

    

    investigate = input("You find a side room, do you wish to investigate? (True or False)")

    side_room_suspicion, side_room_clue = side_room(investigate, code)
    suspicion += side_room_suspicion

    print(f"Total Suspicion: {suspicion}")
    crack_code(suspicion, code)

    escape(suspicion)



