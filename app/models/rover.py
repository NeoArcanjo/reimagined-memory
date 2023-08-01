class Rover:
    x: int = 0
    y: int = 0
    direction: str = "N"

    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        
    def run(self, instructions, plateau_x, plateau_y) -> None:
        """
        Run the given instructions on the mars rover.

        Parameters:
            instructions (list): A list of instructions to be executed by the 
            mars rover.
            plateau_x (int): The maximum x-coordinate of the plateau.
            plateau_y (int): The maximum y-coordinate of the plateau.

        Returns:
            None
        """
        for instruction in instructions:
            match instruction:
                case 'M':
                    self.move(plateau_x, plateau_y)
                case 'L':
                    self.rotate_left()
                case 'R':
                    self.rotate_right()
                case _:
                    pass

    def move(self, plateau_x, plateau_y):
        """
        Moves the object in the specified direction on a plateau.

        Args:
            plateau_x (int): The maximum x-coordinate of the plateau.
            plateau_y (int): The maximum y-coordinate of the plateau.

        Returns:
            None

        Raises:
            None
        """
        if self.direction == "N":
            if self.y < plateau_y:
                self.y += 1
        elif self.direction == "S":
            if self.y > 0:
                self.y -= 1
        elif self.direction == "E":
            if self.x < plateau_x:
                self.x += 1
        elif self.direction == "W":
            if self.x > 0:
                self.x -= 1

    def rotate_left(self):
        """
        Rotates the object to the left.

        This function sets the direction of the object to
        'W' (west) and 'E' (east) in order to rotate it to the left.

        Parameters:
            self (object): The current instance of the object.

        Returns:
            None: This function does not return any value.
        """
        self._set_direction("W", "E")

    def rotate_right(self):
        """
        Rotate the object to the right.

        This function updates the direction of the object by rotating it 90
        degrees clockwise. The direction is updated based on the current
        direction of the object.

        Parameters:
            None

        Returns:
            None
        """
        self._set_direction("E", "W")

    def _set_direction(self, arg0, arg1):
        """
        Set the direction of the object based on the given arguments.

        Parameters:
            arg0 (type): The first argument.
            arg1 (type): The second argument.

        Returns:
            None
        """
        directions = ["N", arg0, "S", arg1]
        current_index = directions.index(self.direction)
        self.direction = directions[(current_index + 1) % 4]
