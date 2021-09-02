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

#########################################################

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


def toys():
    # TODO
    return


if __name__ == "__main__":
    test_scores()
    toys()
