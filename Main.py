
class Grid:
    def __init__(self, WIDTH=0, HEIGHT=0):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.screen = self.create_empty_grid()

    def print_grid():
        '''Prints every horizontal row of the grid under each other.'''
        pass

    def create_empty_grid(self):
        '''Creates an array of X size containing multiple arrays of Y size.'''
        pass

    def update_pixel(self, X, Y, new_character):
        '''Changes the character behind a certain X and Y combination.'''
        pass

    def print_attributes(self):
        '''Debug function; Prints the object's Width and Height.'''
        print(self.WIDTH, self.HEIGHT)

    def check_picture_file(self, file):
        '''Checks if the txt file's text has the same width and height as our Grid instance.'''
        pass

    def read_picture_file(self, file):
        '''Converts a txt file containing ascii art into nested arrays containing char values.'''
        pass


def push_up(space):
    '''Prints X amount of newlines so the previous messages get pushed up.'''
    for _ in range(space):
        print()


if __name__ == "__main__":
    MyGrid = Grid(10, 15)
    MyGrid.print_attributes()
    push_up(0)
    MyGrid.print_attributes()
    pass
