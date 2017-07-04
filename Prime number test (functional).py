def testforprime(number):
    for divisor in range(2, number):
        if number/divisor == 1.0*number/divisor:
            return False
    return True
for number in range(2, 101):
    if testforprime(number) == True:
        print number
        print