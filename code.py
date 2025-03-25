def get_input():
    num = int(input("Enter a number: "))
    print(f"Step 1: The input number is {num}")
    return num

def is_prime(num):
    if num < 2:
        print("Step 2: Numbers less than 2 are not prime.")
        return False
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(f"Step 3: {num} is divisible by {i}, so it is not a prime number.")
            return False
    
    print(f"Step 4: {num} is not divisible by any number from 2 to {int(num ** 0.5)}, so it is prime.")
    return True

def main():
    number = get_input()
    result = is_prime(number)
    
    if result:
        print(f"Final Result: {number} is a prime number.")
    else:
        print(f"Final Result: {number} is NOT a prime number.")

# Run the program
main()
