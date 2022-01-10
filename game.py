import random

def number_generator():
    digits = list(range(10))
    
    d1 = random.randint(0,9)
    digits.remove(d1)
    d2 = random.choice(digits)
    digits.remove(d2)
    d3 = random.choice(digits)

    return str(d1) + str(d2) + str(d3)


def hb_checker(guess, answer):
    hit = 0
    blow = 0

    for x in range(len(answer)):
        if guess[x] == answer[x]:
            hit += 1
        elif guess[x] == answer[x-1]:
            blow += 1
        elif guess[x] == answer[x-2]:
            blow += 1

    return hit, blow


if __name__ == "__main__":
    num = number_generator()
    print(num)
    h, b = hb_checker('123', num)
    print("Hit: " + str(h))
    print("Blow: " + str(b))
    