
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
        for y in range(self.HEIGHT): 
            # Loop over every row saving the current level as y
            row = list() 
            # Initialise our list acting as a collection of all the characters on a single horizontal slice.
            for coloumn in self.screen:
                row.append(coloumn[y]) 
            # Loop over every value containing a list in self.screen and saving the y'th value into the row collection
            print(*row, sep = "")
            # Print every value in

    def create_empty_grid(self):
        '''Creates an array of X size containing multiple arrays of Y size.'''
        return [['*'] * self.HEIGHT] * self.WIDTH 
        # Initialise the main width array every slot stores a vertical row of the grid.

    def update_pixel(self, X, Y, new_character):
        '''Changes the character behind a certain X and Y combination.'''
        pass

    def check_picture_file(self, file):
        '''Checks if the txt file's text has the same width and height as our Grid instance.'''
        pass

    def read_picture_file(self, file):
        '''Converts a txt file containing ascii art into nested arrays containing char values. Also removes buggy characters such as newlines'''
        pass


def push_up(space):
    '''Prints X amount of newlines so the previous messages get pushed up.'''
    for _ in range(space):
        print()


if __name__ == "__main__":
    MyGrid = Grid(12, 4)
    MyGrid.print_grid()
    pass
