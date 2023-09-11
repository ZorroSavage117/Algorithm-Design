# 1. Name:
#      Arlo Jolley
# 2. Assignment Name:
#      Lab 13: Prime Numbers
# 3. Assignment Description:
#      This program will display all the prime numbers at or below a certain value.
# 4. What was the hardest part? Be as specific as possible.
#      rewritting the psedocode into python.
# 5. How long did it take for you to complete the assignment?
#      1 hour

# Loop for ease of video
con = 1
while con == 1:
    # Prompt user for input
    n = int(input("This program will find all the prime numbers at or below N. Select that N: "))

    # Initialize an empty list to store prime numbers
    primes = []

    # Loop through each number from 2 to n
    for num in range(2, n+1):

        # Assume the number is prime until proven otherwise
        is_prime = True
        
        # Check if num is divisible by any number between 2 and num-1
        for divisor in range(2, num):
            if num % divisor == 0:
                is_prime = False
                break
                
        # If the number is prime, add it to the list
        if is_prime:
            primes.append(num)

    # Display the list of prime numbers
    print(f"The prime numbers at or below {n}are: {primes}")

    print()
    con = int(input("continue (0/1): "))