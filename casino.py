import random
import time

print("Welcome to the Bottega Casino! Here we are playing high ot low. Best odds in the house.")

time.sleep(3)

print("In this game we will be using your age as the base number, then you choose if your age will be highter or lower than the number called.")

usernumber = input("How old are you?")
print("Perfect I got")
print(usernumber)


userchoice = input("Choose High or Low")
print("Perfect I got")
print(userchoice)

userbet = input("How much would you like to bet?")
print("Perfect I got")
print(userbet)

print("Your pay will be 5 to one")

total_winnings = (int(userbet)*5)

print("now we will run the random number generaton to see if you are correct")

time.sleep(3)
print("Generating Random Number ")
time.sleep(3)



new_user_number = (int(usernumber) * 2)


computer = random.randint(1,new_user_number)
print(computer) 

time.sleep(2)

if userchoice == "low":
  if int(usernumber) < int(computer):
    print("Sorry Try Again!")
  else:
    print("Winner! Your winning are")
    print(total_winnings)

elif userchoice == "high":
  if int(usernumber) > int(computer):
    print("Sorry Try Again!")
  else:
    print("Winner! Your winning are")
    print(total_winnings)
    
    