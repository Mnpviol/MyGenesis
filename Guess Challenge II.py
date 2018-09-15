#PLEASE THIS IS NOT MY MAJOR PROJECT I JUST WANT TO SUBMIT ONE OF THE  EARLIER WORKS I DID MYSELF DURING THE TRAINING IN CASE I DON'T BEAT SUNDAY'S DEADLINE....
#PRESENTLY I'M TRYING TO DO TIC-TAC-TOE WITH A GUI INTERFACE.. THANKS!

#GUESS CHALLENGE 



import sys, time, random
def print_slow(t):# For this part: It's a code I learnt online... I want to print-out my work slowly.
    for l in t:     
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*0.05)#I'm using a random time multipled by 0.05 in secs.
        
#This line is to create a kinda pause before moving to the next line        
from time import sleep 

print_slow("Welcome! \nThis is a Guess Challenge. \nIn this challenge, the computer picks a random number between 0 and 100.\nAfterwards, you'll be asked to predict the number.")#My welcome message
sleep(2.0)#I told it to pause for two seconds as per line 16 above
print_slow("\nDo you want to take up the challenge? \nKindly press \"y\" for \"yes\", \"n\" for \"no\" :")
ans = None
while ans not in ("y","n"):
    ans = str(input())
    if ans == "y":
        #Here I want user to enter his/her name and it must not above 6 digits
        enter_name_again = None 
        while enter_name_again != "x":
            print_slow("\nPlease enter your user name: ")
            user_name = str(input())
            while len(user_name) >= 0:
                if len(user_name) == 0:
                    print_slow("You've not entered any thing.\n")
                    print_slow("Enter a username: ")
                    user = str(input())
                    user_name = user
                elif 0 < len(user_name) <= 6:
                    print_slow(user_name + " we are glad to have you here!")
                    sleep(3.0)
                    try_again = None
                    while try_again != "n":
                        #HERE'S THE MAIN CODE!
                        from random import randint
                        random_num = (randint(0,100))
                        print_slow("\nGoodluck!\n\n" )
                        #print(random_num) Please you can remove the '#' symbol to that the computer's choice is.
                        x = None
                        while x != random_num:
                            print_slow("\nPredict the secret number: ")
                            x = int(input())
                            if x == random_num:
                                random_num = str(random_num)
                                sleep(3.0)
                                print_slow("\nWOW! Such a genius... Congratulations " + user_name + " you won the game.")
                                print_slow("\nThe correct number is " + random_num)
                                sleep(1.0)
                                print_slow("\nWould you like to try again?\nEnter\"n\" for \"no\" or any other key for \"yes\" :")
                                try_again = str(input())
                                sleep(3.0)
                                break
                            
                            #THIS HAPPENS IF HE'S IS 5 UNITS CLOSE
                            elif(x + 5) >= random_num >= (x + 1) or (x - 5) <= random_num <= (x - 1):
                                sleep(3.0)
                                print_slow("You are so close! Please try again")
                            #WHEN HE MISSES IT
                            else:
                                random_num = str(random_num)
                                sleep(3.0)
                                print_slow("\nSorry! You missed it... " + "The correct number was: " + random_num)
                                print_slow("\nWould you like to try again?\nEnter\"n\" for \"no\" or any other key for \"yes\" : ")
                                try_again = str(input())
                                sleep(3.0)
                                break
                    break
               
            
                else:
                    print_slow("Please your username should not exceed six letters: ")
                    user = str(input())
                    user_name = user

            
            print_slow("\nPress any key to enter as new user or press \"x\" to exit: ")    
            enter_name_again = str(input())
            
        
    elif ans == "n":
        print_slow("Ok! Thanks for coming!")
        sleep(3.0)
        break
     #IF HE/ SHE ENTERS UPPERCASE 'Y' AND 'N'                
    elif ((ans == "Y") or (ans == "N")):
        print_slow("\nPlease make sure your CAPSLOCK is OFF")
        print_slow("\nPress lowercase \"y\" for \"yes\" and lowercase \"n\" for \"no\": ")
        ans = ans
                   
    else: #IF HE/SHE ENTERS ANYTHING OUTSIDE LOWER AND UPPER CASE 'Y' AND 'N'
        print_slow("\nPlease input \"y\" for \"yes\"  or \"n\" for \"no\": ")
        ans = ans
