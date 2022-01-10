import random

def numbergenerator():
    digits = list(range(10))
    
    d1 = random.randint(0,9)
    digits.remove(d1)
    d2 = random.choice(digits)
    digits.remove(d2)
    d3 = random.choice(digits)

    return str(d1) + str(d2) + str(d3)


if __name__ == "__main__":
    print(numbergenerator())