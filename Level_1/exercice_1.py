'''  
Character Input

Exercise 1 
Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they will turn 100 years old. 
Note: for this exercise, the expectation is that you explicitly write out the year 
(and therefore be out of date the next year). 

Extras:

Add on to the previous program by asking the user for another number 
and printing out that many copies of the previous message. 
(Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. 
(Hint: the string "\n is the same as pressing the ENTER button)
'''
import datetime

def main():
    print("Hello welcome, here we will tell you when you will be 100 years old")
    name = input("Please, tell me your name: ")
    age = int(input("and, how old are you?: "))
    initial_time = datetime.date.today().year
    final_year = (100-age) + initial_time
    print(f"Well {name}, you will we celebreting your 100 aniversary in the year {final_year} \n")
    run()

def run():    
    choice = int(input("Please, if you want to enter another age choice 1, otherwise choice 2: "))
    if choice == 1:
        print(f"\n")
        main()
    if choice == 2:
        print(f"\nThanks for stoping by!")
    
    
if __name__ == "__main__":
    main()
    