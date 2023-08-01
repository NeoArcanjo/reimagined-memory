import pytest

from app.models.rover import Rover


def test_rover_move_within_plateau():
    """
    Test the functionality of the `move` method of the Rover class within the 
    plateau.

    This function creates a new instance of the Rover class with initial 
    coordinates (1, 2) and direction "N".
    It then calls the `move` method of the rover object, passing in the 
    maximum coordinates of the plateau as arguments.
    After the rover has moved, it asserts that the x-coordinate of the rover 
    is still 1 and the y-coordinate is incremented to 3.

    This function does not have any parameters.

    This function does not return anything.
    """
    rover = Rover(1, 2, "N")
    rover.move(5, 5)
    assert rover.x == 1
    assert rover.y == 3

def test_rover_move_outside_plateau():
    """
    Test case to verify the functionality of the Rover class when attempting 
    to move the rover outside the plateau.

    This test case initializes a Rover object with initial position (1, 2) 
    and facing direction "N". Then, it attempts to move the rover to position 
    (2, 2) within a plateau size of 2x2. Since the move is outside the 
    plateau, the rover's position should remain unchanged.

    The expected behavior is that the rover's x-coordinate remains at 1 and 
    the y-coordinate remains at 2.

    This test case uses the assert statements to validate that the rover's 
    x-coordinate and y-coordinate are equal to the expected values.

    Parameters:
    - None

    Return Type:
    - None
    """
    rover = Rover(1, 2, "N")
    rover.move(2, 2)  # plateau size is 2x2
    assert rover.x == 1
    assert rover.y == 2


def test_rover_rotate_left():
    """
    Test the `rotate_left` method of the `Rover` class.

    This test function creates a new instance of the `Rover` class with the
    coordinates (1, 2) and a direction of "N". Then it calls the `rotate_left`
    method of the `Rover` instance. Finally, it asserts that the `direction`
    attribute of the `Rover` instance is equal to "W".

    This test ensures that the `rotate_left` method correctly rotates the
    `Rover` instance to the left.

    Parameters:
        None

    Returns:
        None
    """
    rover = Rover(1, 2, "N")
    rover.rotate_left()
    assert rover.direction == "W"


def test_rover_rotate_right():
    """
    Test the rotate_right method of the Rover class.

    This function creates a Rover object with initial position (1, 2) and 
    direction "N".
    It then calls the rotate_right method of the Rover object.
    Finally, it asserts that the direction of the Rover object is now "E".
    """
    rover = Rover(1, 2, "N")
    rover.rotate_right()
    assert rover.direction == "E"
