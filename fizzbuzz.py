
def checkPrime(num):
    if num > 1:
        #Check for factors
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print("prime")

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
        checkPrime(i)
        continue
    elif i % 3 == 0:
        print("Fizz")
        checkPrime(i)
        continue
    elif i % 5 == 0 :
        print("Buzz")
        checkPrime(i)
        continue
    else:
        print(i)
        checkPrime(i)


