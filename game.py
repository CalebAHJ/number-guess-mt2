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

def game():
    answer = number_generator()

    for x in range(6):
        print("Guess a number: ")
        guess = input()
        hit, blow = hb_checker(guess, answer)
        print("Hit: " + str(hit))
        print("Blow: " + str(blow))

        if hit == 3:
            print("Congrats you win!")
            break
        if x == 5 and hit < 3:
            print("You Lose. The answer was " + answer)


if __name__ == "__main__":
    game()
    
    