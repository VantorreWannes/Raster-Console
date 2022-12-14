import numpy as np


class Grid:
    def __init__(self, WIDTH=0, HEIGHT=0):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT

    def print_horizontal_slice(self):
        '''Prints a horizontal slice of the array from left to right.'''
        pass

    def print_attributes(self):
        '''Debug function; Prints the object's Width and Height.'''
        print(self.WIDTH, self.HEIGHT)


def refresh_screen(space):
    '''Prints a bunch a newlines so the previous messages get pushed up.'''
    for _ in range(space):
        print()


if __name__ == "__main__":
    MyGrid = Grid(10, 15)
    MyGrid.print_attributes()
    refresh_screen(0)
    MyGrid.print_attributes()
    pass
