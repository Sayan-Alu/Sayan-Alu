
 # Define a lambda function to check if a number is prime
is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))





def Sayans_twin_primes(n):                                             # Define a function that prints all twin primes less than a given number
    print("Expected result is.... ")   
                                              

    twin_prime = lambda x: is_prime(x) and is_prime(x + 2)               # Use a lambda function to check if two consecutive numbers are twin primes
    
    # Iterate over all odd numbers from 3 to n (excluding n)
    for i in range(3, n, 2):
        if twin_prime(i):                            # Checking if i and i + 2 are twin primes
           
            print(f"\n({i}, {i + 2})")                 # Printing the twin primes as a tuple


Sayans_twin_primes(20)                  #Calling the function