
class Grid:
    def __init__(self, WIDTH=0, HEIGHT=0):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.screen = self.create_empty_grid()

    def print_attributes(self):
        '''Debug function; Prints the object's Width and Height.'''
        print(self.WIDTH, self.HEIGHT)

    def print_grid(self):
        '''Prints every horizontal row of the grid under each other.'''
        for row in self.screen:
            print(*row, sep="")
        # Print every row's values in the self.screen array with no extra makeup.

    def create_empty_grid(self):
        '''Creates an array of Y size containing multiple arrays of X size.'''
        return [['#'] * self.WIDTH for _ in range(self.HEIGHT)]
        # Initialise the main width array every slot stores a vertical row of the grid.

    def update_pixel(self, X, Y, new_character):
        '''Changes the character behind a certain X and Y combination.'''
        real_y = len(self.screen) - (Y + 1)
        # Convert the inputed Y value to adjust for index 0 always being the first row and first element.
        self.screen[real_y][X] = new_character

    def verify_picture_file(self, screen):
        '''Checks if the screen text has the same width and height as our Grid instance.'''
        pass

    def load_picture_file(self, file):
        '''Converts a txt file containing ascii art into nested arrays containing char values. Also removes buggy characters such as newlines'''
        pass


def push_up(space):
    '''Prints X amount of newlines so the previous messages get pushed up.'''
    for _ in range(space):
        print()


if __name__ == "__main__":
    MyGrid = Grid(12, 4)
    MyGrid.update_pixel(0, 0, '0')
    MyGrid.update_pixel(0, 1, '1')
    MyGrid.print_grid()
    pass
