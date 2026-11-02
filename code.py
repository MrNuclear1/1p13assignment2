DEBUG = True
import random
import math



#ADD COMMMMMMMENTS


#ADD COMMMMMMMENTS


#ADD COMMMMMMMENTS


def print_signature():
    print("Yusuf Pasha")
    print("400684246, Engineering 1")
    print("ENG 1P13: Integrated Cornerstone Design Projects in Engineering")
    print("Dr. Sam Scott")
    print("Fall 2026")



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


    return suspicion, clue


def side_room(investigate, code):
    suspicion = 0

    
    
    
    if investigate == True:
        luck = random.randint(1,100)
        print("You Stumble Upon a Side Room, Its The Managers Office")
        if luck > 80:
            clue = code
        elif (luck > 30 and luck < 81):
            hundreds = code//100
            tens =(code - (100*hundreds))//10
            clue = (code - (100*hundreds) - (10*tens))
        elif (luck >0 and luck < 31):

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
            
            print("Enter Your Combo Guess Below")
            comboguess = int(input())
            
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
        print("What Action Do You Want To Take? 1 = Run, 2 = Hide, 3 = Shortcut")
        choice = int(input())
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
    again = "Y"
    while again == "Y":
        suspicion = 0
        print(f"Greetings {name}, Welcome To Watch Heist")
        print("Your goal is to break into a luxury watch store, holding the prized Rainbow Daytona Worth 500K USD")
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
        
        print("Choose Your Entry Method, 1-6, Higher is Easier")
        choice = int(input())
        while choice < 1 or choice > 6:
            choice = int(input("Invalid Choice Try Again (1-6)"))

        firstsuspicion, clue1 = enter(choice, code)

        suspicion += firstsuspicion

        print(f"Total Suspicion: {suspicion}")
        if clue1 == (-1):
            print("Combo is between 100-499")
        elif clue1 == (-2):
            print("Combo is between 500-999")
        else:
            print(f"First digit of the code is {clue1}")


        answer = input("Investigate? True or False: ")
        investigate = (answer == "True")

        side_room_suspicion, side_room_clue = side_room(investigate, code)
        suspicion += side_room_suspicion

        if side_room_clue == -1:
            print("No clue found")
        elif side_room_clue < 10:
            print(f"Last digit is {side_room_clue}")
        else:
            print(f"The code is {side_room_clue}")

        print(f"Total Suspicion: {suspicion}")
        
        newsuspicion, correctcode = crack_code(suspicion, code)
        suspicion += newsuspicion
        print(f"Total Suspicion: {suspicion}")

        progress = escape(suspicion)
        if progress >= 10 and correctcode == True:
            print("You Escaped With The Watches!")
        elif progress >= 10:
            print("You Escaped But Didn't Crack The Code")
        else:
            print("You Got Caught!")
        if progress >= 10 and correctcode == True:
            break
        else:
            again = input("Try Again? Y/N: ")


print_signature()

NAME = input("Enter Your Name: ")

heist(NAME)


#ADD COMMMMMMMENTS
