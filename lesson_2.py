# A student has taken 3 tests in a class, and wants to know their current grade 
# (which is only calculated by these tests). 

# Ask the user to input all three of the test scores for the student, one by one. 

# The program should then calculate the average test score (average is adding all three 
# test scores together then dividing by 3), and then print the student's letter grade 
# (as well as the average score as a number).

#########################################################

# Gregory wants to know how many toys they can buy at Toys'N'Us

# They prioritize buying the most expensive toys first (For ejm. If Gregory had $50 
# they'd end up buying 2 Jumbo Baby Yoda Plushies, 1 Beyblade, and 5 Sticky Hands with 
# a remainder of $0.30 left)

# Have the user input how much money Gregory has then print how many of each 
# toy they can afford, as well as how much money they'd have remaining

# The toys and their prices are as follows:
# Jumbo Baby Yoda Plush - $20
# Beyblades - $7.20
# Sticky Hands - $0.50

#########################################################

# Ryan is doing his math homework, but the (x!) key on Ryan’s calculator is broke, you wanting to show off your
# programming skills so you told him that you will code something to help him do that. Your program will only accept
# an integer that is between 0 and 10; if the number is less or equal to 0, you will tell him that he broke the
# program and the program will now shut down. If the number is more or equals to 10 and is an even number,
# you will tell him that he overflood the program and print out the infinity inside the math library,
# math.inf. Otherwise just print “error”. If he entered a valid number, you will then use the factorial fabs()
# function inside the math library to calculate the factorial. If this calculated factorial is below 100,
# print out this number. If it is over 100, square it, print it out, and then ask Ryan if this seems correct. If he
# guessed right, send him a congrats, but if he guessed it wrong, tell him that his computer doesn’t like him anymore
# and print out a bunch of random letters.

#########################################################

import math as m


def test_scores() -> None:
    """
    Queries the user for three test scores then prints their average and letter grade.
    """
    try:
        score_1: int = int(input("Enter the first test score:\n"))
        score_2: int = int(input("Enter the second test score:\n"))
        score_3: int = int(input("Enter the third test score:\n"))
    except:
        print("Whoops, that doesn't look like an integer!")
        return
    avg: float = (score_1 + score_2 + score_3) / 3
    print("Average Test Score: " + str(avg))
    print(
        "Letter Grade: " + (
            "A" if 90 <= avg
            else "B" if 80 <= avg < 90
            else "C" if 70 <= avg < 80
            else "D" if 60 <= avg < 70
            else "F" if avg < 60
            else "Could not determine"
        )
    )
    return


def toys() -> None:
    """
    Asks the user how much money they have, then displays how much of each item can be purchased at Toys 'N' Us with
    that money.
    """
    prices: dict = {
        "plush": 20.00,
        "beyblade": 7.20,
        "sticky_hands": 0.50
    }
    money: float = 0.0
    while True:
        try:
            money: float = float(input("Enter how much money you currently have, in dollars: "))
            break
        except:
            print("Whoops, that's not a number! Try again.")
            continue
    print("Here's how much of each toy you can afford: ", end="")
    plush_count: int = m.floor(money / prices["plush"])
    money %= prices["plush"]
    print(str(plush_count) + " Jumbo Baby Yoda Plushies, ", end="")
    beyblade_count: int = m.floor(money / prices["beyblade"])
    money %= prices["beyblade"]
    print(str(beyblade_count) + " Beyblades, and ", end="")
    sticky_hands_count: int = m.floor(money / prices["sticky_hands"])
    money %= prices["sticky_hands"]
    print(str(sticky_hands_count) + " Sticky Hands.")
    print("Your remaining money after these purchases: $" + str(round(money, ndigits=2)))  # floats are imprecise
    return


def factorials() -> None:
    """
    TODO
    """
    x: int = 1
    while True:
        try:
            x = int(input("Enter a number from 1 through 9 to take the factorial of: "))
            break
        except:
            print("That doesn't look like an integer, try again!")
            continue
    if x <= 0:
        print("Oh no, you broke the entire program! Shutting down...")
        return
    elif x >= 10 and x % 2 == 0:
        print("Oh no, looks like you overflooded the program!")
        print("Your answer is: ", end="")
        print(m.inf)
        return
    elif x >= 10:
        print("error :(")
        return
    x_factorial: int = int(m.factorial(x))
    guess: str = input("Your answer is: " + str(x_factorial ** 2 if x_factorial > 100 else x_factorial)
                       + ".\nDoes this seem right? (y/n) ")
    if ((guess.lower() == "y" or guess.lower() == "yes") and x_factorial > 100)\
            or (x_factorial <= 100 and not (guess.lower() == "y" or guess.lower() == "yes")):
        print("Incorrect! Your computer no longer likes you.\n"
              + "owheufwejoidsnjbxfxjdwmqnebfuroejnsde\n"
              + "xvnjnxjoeijxdkcvnxjkcneomskdokwmenrhb\n"
              + "cixovhubxdkefnrgbudojfdxjnrdexjnjcdjv\n"
              + "uicxuvbdwajienuvhfbhjfrhujdhuixvjiodr\n"
              )
    else:
        print("Congrats, you are not an idiot!")
    return


if __name__ == "__main__":
    test_scores()
    toys()
    factorials()
