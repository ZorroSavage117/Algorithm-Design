# 1. Name:
#      Arlo Jolley
# 2. Assignment Name:
#      Lab 10: Numeric Sequence
# 3. Assignment Description:
#      It takes in a number from the user and computes the francois verant of that number.
# 4. What was the hardest part? Be as specific as possible.
#      Remembering what I ment by my psedoucode.
# 5. How long did it take for you to complete the assignment?
#      About an hour.

def francois_number(n):
    francois_sequence = [2, 1]
    if n <= 2:
        return francois_sequence[n-1]
    else:
        for i in range(3, n+1):
            fn = francois_sequence[i-2] + francois_sequence[i-3]
            francois_sequence.append(fn)
        return francois_sequence[-1]

print("Enter a number n to compute the nth François value:")
n = int(input())
francois_value = francois_number(n)
print("The", n, "th François value is:", francois_value)