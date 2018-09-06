# For this part: It's a codeI learnt online... I wanted to make print
#-Out my work slowly when u run it ull understand.

import sys, time, random
def print_slow(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*0.05)#I'm using a random time multipled by 0.3 in secs.
        
#This line is to create a kinda pause before moving to the next line        
from time import sleep 

print_slow("Welcome! \nThis is a Guess Challenge")#My welcome message
sleep(2.0)#I told it to pause for two seconds as per line 12 above

#Here I want user to enter his/her name and it must not above 6 digits
enter_name_again = None 
while enter_name_again != "x":
    user_name = str(input("\nPlease enter your user name:"))
    while len(user_name) >= 0:
        if len(user_name) == 0:
            print_slow("You've not entered any thing")
            break
        if 0 < len(user_name) <= 6:
            print_slow(user_name + " we are glad to have you here! \nIn this challenge, the computer picks a random number between 0 and 100.\nThen, you're asked to predict the number.")
            sleep(3.0)
            try_again = None
            while try_again != "n":
                ans = None
                while ans not in ("y","n"):
                    ans = str(input("\nSo, are you ready to take the challenge? \n(Kindly press \"y\" for \"yes\", \"n\" for \"no\") :"))
                    if ans == "y":
                        #HERE'S THE MAIN CODE!
                        print_slow("\nGoodluck " + user_name + "!")
                        from random import randint
                        random_num = (randint(0,100))
                        
                        x = None
                        while x != random_num:
                            x = int(input("\nPlease predict the secret number:"))
                            if x == random_num:
                                random_num = str(random_num)
                                sleep(3.0)
                                print_slow("\nWOW! Such a genius... Congratulations " + user_name + " you won the game.")
                                print_slow("\nThe correct number is " + random_num)
                                try_again = str(input("\nWould you like to try again?\nEnter\"n\" for \"no\" or any other key for \"yes\" :"))
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
                                try_again = str(input("\nWould you like to try again?\nEnter\"n\" for \"no\" or any other key for \"yes\" : "))
                                sleep(3.0)
                                break
                            break
                        break
                    #JUST TRY TO UNDERSTAND THE LOOP
                    elif ans == "n":
                        print_slow("Ok! Thanks for coming!")
                        sleep(2.0)
                        try_again = str(input("\nWould you like to try again?\nEnter\"n\" for \"no\" or any other key for \"yes\" : "))
                        sleep(3.0)
                        break
                    if ((ans == "Y") or (ans == "N")):
                        print_slow("Please make sure your CAPSLOCK is OFF")
                    
                    else:
                        print_slow("Please input \"y\" for \"yes\"  or \"n\" for \"no\" ")
                    
                    break
                break

                
            enter_name_again = str(input("\nPress any key to enter as new user or press \"x\" to exit:"))
            break
        else:
            print_slow("Please your username should not exceed six letters")
            break
    
