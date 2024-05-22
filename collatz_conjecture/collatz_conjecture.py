"""
The Collatz, or 3n + 1 conjecture, is a mathematical sequence defined as follows:

* start with a number, n
* if n is even:
  * produce n / 2
* otherwise, n is odd:
  * produce 3 * n + 1
* repeat until n is 1

Write a python program which takes a numeric input and shows how many steps it takes until the Collatz
sequence reaches 1.
"""

def calculate_collatz_conjecture_steps(n):
    steps = 0
    while n != 1:
        # check if n is even
        if (n % 2) == 0:
            n = n // 2
        # n is odd
        else:
            n = 3 * n + 1
            
        steps += 1
        
    return steps

def get_user_input():
    
    num = int(input("Please enter a whole number: "))
    
    # num has to be greater than 0, cannot be 0 or not negative value
    if num <= 0:
        raise ValueError("Please enter a positive number which is greater than 0")
    
    return num

def main():
    try:
        num = get_user_input()
        steps = calculate_collatz_conjecture_steps(num)
        print(f"For the given number {num}, it took {steps} steps for the Collatz sequence to reach 1")
    except ValueError as e:
        print(e)
        
if __name__ == "__main__":
    main()
    


