'''
List Ends

Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) 
and makes a new list of only the first and last elements of the given list. 

For practice, write this code inside a function.
'''
a = [5, 10, 15, 20, 25]

def main():
    b = [a[0],a[-1]]
    print(b)
    
    
if __name__ == "__main__":
    main()