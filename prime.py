## Program that displays all prime numbers from 1 to 250 and stores the results in results.txt
## A prime number is a number divisible only by 1 and itself

def primeCheck(number):

    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                print(f'{number} is NOT prime.')
                break
        else:
            print(f'{number} is prime.')
        
def prime(lower,upper):
    parameter = range(lower,upper+1)
    for i in parameter:
        primeCheck(i)

prime(1,250)


