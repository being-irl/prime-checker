## Program that displays all prime numbers from 1 to 250 and stores the results in results.txt

## Sub-function
## Check if a number is prime, return Boolean value
def primeCheck(number):
    isPrime = False
    if number == 2:
        isPrime = True
    if number > 2 and number % 2 != 0:    # Primes must be greater than 1 and not even
        for i in range(2, (number//2)):   # Any number greater than half the prime cannot be its factor
            if (number % i) == 0:         # Disregard if number is divisible by any value besides 1 and itself
                break
        else:
            isPrime = True
    return isPrime                        # Confirms if value is prime or not, passes Boolean value to prime()

## Main function
## Checks if numbers in specified range are prime, then writes primes to results.txt
def prime(lower,upper):
    parameter = range(lower,upper+1)      # Initialize range of numbers to check
    primeList = []                        # Initialize empty list for primes
    primeFile = open("results.txt", "wt") # Initialize empty text file
    for i in parameter:                   # For every number in range, append to primeList if prime
        if primeCheck(i) == True:
            primeList.append(i)
    for element in primeList:             # Write every item in primeList to text file
        primeFile.write(str(element) + ", ")
    primeFile.close()
    print("Primes have been saved to results.txt. They are as follows: ")
    print(primeList)



