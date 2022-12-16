HEIGHT = 4
WIDTH = 14

def verify_picture_file(X, Y, screen):
        '''Checks if the screen will fit in our grid instance.'''
        if len(screen) + Y <= HEIGHT:
            if len(screen[0]) + X <= WIDTH:
                return True
        return False

print(verify_picture_file(12, 2, [[' ']*2 for _ in range(2)]))

print(len("              "))