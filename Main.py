import numpy as np


class Grid:
    def __init__(self, WIDTH=0, HEIGHT=0):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT

    def print_grid():
        ''''''
        pass
    
    def update_pixel(self, X, Y, new_character):
        '''Changes the character behind a certain X and Y combination.'''
        pass
    
    def create_empty_grid(self, width, height):
        '''Creates an array of X size containing multiple arrays of Y size.'''
        pass

    def print_horizontal_slice(self):
        '''Prints a horizontal slice of the array from left to right.'''
        pass

    def print_attributes(self):
        '''Debug function; Prints the object's Width and Height.'''
        print(self.WIDTH, self.HEIGHT)


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
