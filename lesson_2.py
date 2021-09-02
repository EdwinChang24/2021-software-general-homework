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
            print("Whooops, that's not a number! Try again.")
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


if __name__ == "__main__":
    test_scores()
    toys()
