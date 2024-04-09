import random
#Emily Suranie
#Dice Lab

#dice results
def rolling_dice():
    #finding the dice roll
    total_roll = random.randint(2,12)
    return total_roll

#getting dice results
def rolling_results(total_iterations):
    #starting count at 0
    dice_roll2 = 0
    dice_roll3 = 0
    dice_roll4 = 0
    dice_roll5 = 0
    dice_roll6 = 0
    dice_roll7 = 0
    dice_roll8 = 0
    dice_roll9 = 0
    dice_roll10 = 0
    dice_roll11 = 0
    dice_roll12 = 0

    #finding the total roll
    count = int(total_iterations)
    for i in range(count):
        total_roll = rolling_dice()
        if total_roll > 1:
            count -= 1
        if total_roll == 2:
            dice_roll2 = dice_roll2 + 1
        elif total_roll == 3:
            dice_roll3 = dice_roll3 + 1
        elif total_roll == 4:
            dice_roll4 = dice_roll4 + 1
        elif total_roll == 5:
            dice_roll5 = dice_roll5 + 1
        elif total_roll == 6:
            dice_roll6 = dice_roll6 + 1
        elif total_roll == 7:
            dice_roll7 = dice_roll7 + 1
        elif total_roll == 8:
            dice_roll8 = dice_roll8 + 1
        elif total_roll == 9:
            dice_roll9 = dice_roll9 + 1
        elif total_roll == 10:
            dice_roll10 = dice_roll10 + 1
        elif total_roll == 11:
            dice_roll11 = dice_roll11 + 1
        else:
            dice_roll12 = dice_roll12 + 1

    #making the rows
    print("number\t" + "rolls\t" + "percent\t" + "expectations\t" + "differences")

    #finding the percent, expectations, differences
    if dice_roll2 > 0:
        percent = round(dice_roll2 / int(total_iterations), 2)
        expectation = round(1 / 11, 2)
        difference = round(expectation - percent, 2)
        print( "2\t" + str(dice_roll2) + "\t" + str(percent) + "\t" + str(expectation) + "\t\t" + str(difference))
    if dice_roll3 > 0:
        percent = round(dice_roll3 / int(total_iterations), 2)
        expectation = round(1 / 11, 2)
        difference = round(expectation - percent, 2)
        print( "3\t" + str(dice_roll3) + "\t" + str(percent) + "\t" + str(expectation) + "\t\t" + str(difference))
    if dice_roll4 > 0:
        percent = round(dice_roll4 / int(total_iterations), 2)
        expectation = round(1 / 11, 2)
        difference = round(expectation - percent, 2)
        print( "4\t" + str(dice_roll4) + "\t" + str(percent) + "\t" + str(expectation) + "\t\t" + str(difference))
    if dice_roll5 > 0:
        percent = round(dice_roll5 / int(total_iterations), 2)
        expectation = round(1 / 11, 2)
        difference = round(expectation - percent, 2)
        print( "5\t" + str(dice_roll5) + "\t" + str(percent) + "\t" + str(expectation) + "\t\t" + str(difference))
    if dice_roll6 > 0:
        percent = round(dice_roll6 / int(total_iterations), 2)
        expectation = round(1 / 11, 2)
        difference = round(expectation - percent, 2)
        print( "6\t" + str(dice_roll6) + "\t" + str(percent) + "\t" + str(expectation) + "\t\t" + str(difference))
    if dice_roll7 > 0:
        percent = round(dice_roll7 / int(total_iterations), 2)
        expectation = round(1 / 11, 2)
        difference = round(expectation - percent, 2)
        print( "7\t" + str(dice_roll7) + "\t" + str(percent) + "\t" + str(expectation) + "\t\t" + str(difference))
    if dice_roll8 > 0:
        percent = round(dice_roll8 / int(total_iterations), 2)
        expectation = round(1 / 11, 2)
        difference = round(expectation - percent, 2)
        print( "8\t" + str(dice_roll8) + "\t" + str(percent) + "\t" + str(expectation) + "\t\t" + str(difference))
    if dice_roll9 > 0:
        percent = round(dice_roll9 / int(total_iterations), 2)
        expectation = round(1 / 11, 2)
        difference = round(expectation - percent, 2)
        print( "9\t" + str(dice_roll9) + "\t" + str(percent) + "\t" + str(expectation) + "\t\t" + str(difference))
    if dice_roll10 > 0:
        percent = round(dice_roll10 / int(total_iterations), 2)
        expectation = round(1 / 11, 2)
        difference = round(expectation - percent, 2)
        print( "10\t" + str(dice_roll10) + "\t" + str(percent) + "\t" + str(expectation) + "\t\t" + str(difference))
    if dice_roll11 > 0:
        percent = round(dice_roll11 / int(total_iterations), 2)
        expectation = round(1 / 11, 2)
        difference = round(expectation - percent, 2)
        print( "11\t" + str(dice_roll11) + "\t" + str(percent) + "\t" + str(expectation) + "\t\t" + str(difference))
    if dice_roll12 > 0:
        percent = round(dice_roll12 / int(total_iterations), 2)
        expectation = round(1 / 11, 2)
        difference = round(expectation - percent, 2)
        print( "12\t" + str(dice_roll12) + "\t" + str(percent) + "\t" + str(expectation) + "\t\t" + str(difference))

#main function - calls other functions
def main():
    total_iterations = input('how many time would you like to roll the dice?: ')
    print('total iterations: ' + total_iterations)
    rolling_results(total_iterations)

#calling main
if __name__ == '__main__':
    main()
