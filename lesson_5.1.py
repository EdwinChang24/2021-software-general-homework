# Make a class for a robot! This robot can only drive in a straight line on a field 7 meters long.
# The robot has a drive base and an arm that can move up and down.
# Imagine that the arm can pick up and score cubes for 5 points each. Your robot should have these variables:
#   Position
#   Arm position
#   Whether or not it has a cube
#   Score from scoring cubes
# The robot class should also have methods to:
#   Move
#   Raise/lower arm
#   Pick up a cube
#   Score a cube
# Rules/information:
#   The robot starts at position 0 with no cubes and the arm 0 inches off the ground.
#   A cube can only be picked up when:
#       The robot is at space 3 (aka 3 meters from starting position)
#       The arm is 0 inches off the ground
#       The robot does not already have a cube
#   The robot must be holding a cube 10 inches in the air at space 7 to score it.
#
# Once you have this class created, make a way for the user to control the robot! Use loops and input.
# Every time the robot does something, make sure to print out information on its position,
# etc. so the user doesn’t get confused.
#
# This is a pretty big assignment, so don’t be afraid to ask any questions!

class Robot:
    position: int = 0
    arm_position: int = 0
    has_cube: bool = False
    score: int = 0

    def move(self, distance: int) -> int:
        """
        Move the robot some number of spaces.
        :param distance: The distance to move the robot in meters. Forward if positive, backwards if negative.
        :return: The new location of the robot.
        """
        if self.position + distance > 7:
            self.position = 7
            return 7
        elif self.position + distance < 0:
            self.position = 0
            return 0
        else:
            self.position += distance
            return self.position

    def move_arm(self, height: int) -> int:
        """
        Raise or lower the robot arm.
        :param height: How high to raise the robot arm, in inches. Up if positive, down if negative.
        :return: The new robot arm position.
        """
        if self.arm_position + height < 0:
            self.arm_position = 0
            return 0
        else:
            self.arm_position += height
            return self.arm_position

    def pick_up_cube(self) -> bool:
        """
        Picks up a cube. Well, only if it can.
        :return: Whether the cube was successfully picked up.
        """
        if self.position == 3 and self.arm_position == 0 and not self.has_cube:
            self.has_cube = True
            return True
        return False

    def score_cube(self) -> int:
        """
        Scores a cube, if possible.
        :return: The new score, even if the scoring was unsuccessful.
        """
        if self.has_cube and self.arm_position == 10 and self.position == 7:
            self.score += 5
            return self.score
        return self.score
