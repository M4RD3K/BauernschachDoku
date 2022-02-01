"""Figure base class for the chess game
"""


class Figure:
    """Figure base class for the chess game
    """

    def __init__(self, pos_x, pos_y, color):
        """Arguments:
            pos_x {int} -- start pos of pwan
            pos_y {int} -- start pos of pwan
            color {String} -- COLOR_BLACK or COLOR_WHITE
        """
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color

    def move_to(self, new_x, new_y, is_occupied):
        """Move figure to new position
        Arguments:
            new_x {int} -- new position
            new_y {int} -- new position
            is_occupied {bool} -- is new position occupied?

        Return:
            True if move was made
            False if move could not be made
        """

        if is_occupied is True:
            return False

        self.pos_x = new_x
        self.pos_y = new_y
        return True


    def get_position(self):
        """Get position as tuple

        Return:
            Position as tuple (x, y)
        """
        return self.pos_x, self.pos_y

    def get_color(self):
        """Gets the color of the Figure

        Return:
            COLOR_BLACK or COLOR_WHITE
        """
        return self.color
