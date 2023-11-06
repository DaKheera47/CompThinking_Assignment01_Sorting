import random


def generateRandomNumber(numDigits, elements):
    # generate a random number with numDigits digits
    # and repeat this process elements times
    # return a list of random numbers
    randomNumbers = []
    # 10 ** 3 = 1000
    minNum = 10 ** (numDigits - 1)
    # 10 ** 4 = 10000 - 1 = 9999
    maxNum = (10**numDigits) - 1

    for i in range(elements):
        randomNumber = random.randint(minNum, maxNum)
        randomNumbers.append(randomNumber)

    return randomNumbers
