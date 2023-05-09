import random,time
# Define a class called Slot
class Slot:
    # Define a function to print the result of the game
    def prtresult(self,cash,temp,x,y):
        # If the cash is equal to the initial amount, print that the user didn't gain or lose money
        print("Calculating",end="")
        for i in range(6):
            print(".",end="")
            time.sleep(0.3)
        print()
        if cash == temp:
            print("total no. of spins :",x)
            print("total no. of spins won :", y)
            print("You didn't gain and You didn't loose money !","😒")
            print("the remaining cash is :",cash,"$")
        # If the cash is greater than the initial amount, print how much the user gained
        elif cash > temp:
            print("total no. of spins :", x)
            print("total no. of spins won :", y)
            print("You gain :",cash - temp,"$","🍾")
            print("the remaining cash is :", cash,"$")
        # If the cash is less than the initial amount, print how much the user lost
        elif cash < temp:
            print("total no. of spins :", x)
            print("total no. of spins won :", y)
            print("You loose :", temp - cash,"$","😶‍🌫️")
            print("the remaining cash is :", cash,"$")

    # Define a function to print a line of emojis
    def pline(self,x):
        sleep=time.sleep
        print("\n[",end=" ")
        sleep(0.75)
        print(f"{digits[x[0]][0]}",end=" ")
        sleep(0.75)
        print(f"| {digits[x[1]][0]}",end=" ")
        sleep(0.75)
        print(f"| {digits[x[2]][0]}", end=" ]\n")
        sleep(0.75)
        print()

    # Define a function to randomly select emojis for the slot machine
    def sspin(self,digits):
        l = []
        for _ in range(random.randrange(3, 7)):
            c = random.choice(digits)
            if c not in l:
                l.append(c)
        return l

    # Define a function to spin the slot machine
    def spin(self,x):
        l = []
        for i in range(3):
            l.append(random.choice(x))
        return l

    # Define a function to play the game
    def play(self,digits,cash,temp):
        rounds_won = 0
        total_rounds = 0
        while True:
            # Ask the user to spin or cash out
            user=input(fr"Press <enter> to spin (or) 'c' to cashout: ").lower()
            # If the user has money left, continue playing
            if cash != 0 and cash>0:
                # If the user chooses to spin
                if user == "":
                    # Spin the slot machine
                    line=self.spin(self.sspin(list(digits.keys())))
                    # Print the line of emojis
                    self.pline(line)
                    # If all three emojis are the same, the user wins
                    if len(set(line))==1:
                        won=digits[line[0]][1]
                        cash+=won
                        rounds_won+=1
                        print(fr"you won {won}$ !, Balance = {cash}$ 👍👌")
                    # If the emojis are not the same, the user loses 1 dollar
                    else:
                        cash -= 1
                        print(fr"you loose 1$ !, Balance = {cash}$ 👎")
                    total_rounds+=1
                # If the user chooses to cash out, print the result and end the game
                elif user == "c":
                    self.prtresult(cash,temp,total_rounds,rounds_won)
                    break
                # If the user enters an invalid input, print an error message
                else:
                    print("Give only right option !!!")
            # If the user has no money left, print the result and end the game
            else:
                self.prtresult(cash, temp, total_rounds, rounds_won)
                print("can't play with 0 $ balance")
                break
        print("Thank You !!!")

# Define a dictionary of emojis and their corresponding values
digits = {"snake": ("🐍", 100),
          "money": ("💰", 50),
          "skull": ("💀", 3),
          "lemon": ("🍋", 1),
          "cherry": ("🍒", 20),
          "eball": ("🎱", 8),
          "seven": ("7️⃣", 77)}

# Ask the user to enter the amount they want to bet
print("enter only in digits!!! and we will be accept only Dollars $")
try:
    user_input = input("Enter the amount you want to bet: ")
    # If the user enters a valid input, start the game
    if user_input:
        cash = int(user_input)
        temp = cash
        Slot().play(digits, cash, temp)
    # If the user enters an invalid input, print an error message
    else:
        print("Invalid input !!!")
        print("Please enter a number.")
# If an exception occurs, print an error message
except Exception as e:
    print(e, "Invalid input. Please enter a number.")
