'''
Exercise 20 
Write a function that takes an ordered list of numbers 
(a list where the elements are in order from smallest to largest) and another number. 
The function decides whether or not the given number is inside the list and returns (then prints) 
an appropriate boolean.

Extras:

Use binary search.
'''
import random

a = [1,2,3,4,5,6,7,8,9,10]

def main():
    ''' Find a value in a list '''
    number = random.randint(1,20)
    if number in a:
        print(f"{number} is in the list")
    else:
        print(f"The {number} isn't in the list")
        
        
def binary_search(a_list, start, final, objective, count):
    ''' Find a value en a list trough binary search '''
    middle = round((start + final)/2)
    
    if start > final:
        print("End simulation")
        return False
    elif a_list[middle] == objective:
        print(f"We found the {objective} in {count} times")
        return True 
       
    elif objective > a_list[middle]:
        middle = middle + 1
        return binary_search(a_list, middle, final, objective, count+1)
    else:
        middle = middle - 1    
        return binary_search(a_list, start, middle, objective, count+1)



if __name__ == "__main__":
    main()
    binary_search([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], 1,20,8,0)