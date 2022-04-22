''' 
Odd Or Even 
Exercise 2 

Ask the user for a number. Depending on whether the number is even or odd, 
print out an appropriate message to the user. 
Hint: how does an even / odd number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
'''

def main():
    print("Hello welcome, to even or odd")
    enter = int(input("Please, tell us a number: "))
    number = enter%2
    four = enter%4
    if number == 0:
        print(f"\nYou chose an even number")
    if four == 0:
        print("You chose a number that is a multiple of four")
    else:
        print("You chose an odd number")

def run():
    print(f"\nNow, please give us two numbers")
    num = int(input("tell us the first number: "))
    check = int(input("tell us the second number: "))
    test = num%check
    if test == 0:
        print("Your first number divides evenly into the second")
    else:
        print("Your first number doesn't divides evenly into the second")
        

if __name__ == "__main__":
    main()
    run()