# Create a program in which the user creates 
# a specific FRC team and store the following variables:
#   Team Number (named team_number)
#   Team Name (named team_name)
#   Location (named location)
#   Rookie Year (named rookie_year)
#   Is Active (named is_active)
# Be sure to store each variable as the correct type!

def main():
    # Team Number
    team_number: int = int(input("What is the Team Number? "))
    # Team Name
    team_name: str = input("What is the Team Name? ")
    # Location
    location: str = input("Where is the Location? ")
    # Rookie Year
    rookie_year: int = int(input("When was the Rookie Year? "))
    # Is Active
    is_active: bool = True if input("Is the team currently active? (y/n) ").lower() == "y" else False
    print(f"The number of team {team_name}"
          + f" is {team_number}"
          + f". The location is {location}"
          + f" and the rookie year was {rookie_year}"
          + ". The team is currently " + ("active." if is_active else "inactive.")
          )


if __name__ == "__main__":
    main()
