# Donaven Bruce
# This program gets five validated judge scores, drops the highest 
# and lowest, and then calculates the contestant’s final score as the average of the remaining three.


def getJudgeData():
    # Get and validate one judge score
    while True:
        try:
            score = float(input("Enter judge score between 0 and 10: "))
            while score < 0 or score > 10:
                print("Score should be >=0 or <= 10")
                score = float(input("Enter judge score between 0 and 10: "))
            break
        except:
            print("Invalid entry")
    return score


def findLowest(score1, score2, score3, score4, score5):
    # Find smallest score value
    lowest = score1
    if score2 < lowest:
        lowest = score2
    if score3 < lowest:
        lowest = score3
    if score4 < lowest:
        lowest = score4
    if score5 < lowest:
        lowest = score5
    return lowest


def findHighest(score1, score2, score3, score4, score5):
    # Find largest score value
    highest = score1
    if score2 > highest:
        highest = score2
    if score3 > highest:
        highest = score3
    if score4 > highest:
        highest = score4
    if score5 > highest:
        highest = score5
    return highest


def calcScore(score1, score2, score3, score4, score5):
    # Drop one highest and one lowest then average middle three
    lowest = findLowest(score1, score2, score3, score4, score5)
    highest = findHighest(score1, score2, score3, score4, score5)
    total = score1 + score2 + score3 + score4 + score5
    remainingTotal = total - lowest - highest
    finalScore = remainingTotal / 3
    return finalScore


def main():
    # Get all five judge scores
    score1 = getJudgeData()
    score2 = getJudgeData()
    score3 = getJudgeData()
    score4 = getJudgeData()
    score5 = getJudgeData()

    finalScore = calcScore(score1, score2, score3, score4, score5)

    # Show final formatted result
    print("Final score for the contestant is: {:.2f}".format(finalScore))


main()
