import unittest

class Screen(object):
    def __init__(self, name, size) -> None:
        self.name = name
        self.size = size
        self.commands = []
        self.screen = {(x, y): " " for y in range(self.size-1, -1, -1) for x in range(self.size*3)}

    def clear(self):
        self.screen = {coords: " " for coords in self.screen}

    def resize(self, new_size):
        self.screen = {(x, y): self.screen.get((x, y), " ") for y in range(new_size-1, -1, -1) for x in range(new_size*3)}

    def write(self, x, y):
        if (x, y) not in self.screen.keys():
            return None
        self.screen.update[(x, y): " "]


class TestScreen(unittest.TestCase):

    def test_resize(self):
        SCREEN = Screen("ResizeTestScreen", 1)
        self.assertTrue(SCREEN.screen.get((0, 3)) == None)
        SCREEN.resize(4)
        self.assertTrue(SCREEN.screen.get((0, 3)) == " ")
        SCREEN.resize(2)
        self.assertTrue(SCREEN.screen.get((0, 3)) == None)

    def test_write(self):
        SCREEN = Screen("ResizeTestScreen", 2)
        self.assertTrue(SCREEN.write(0, 3) == None)
        SCREEN.resize(4)
        self.assertTrue(SCREEN.screen.get((0, 3)) == " ")
        SCREEN.resize(2)
        self.assertTrue(SCREEN.screen.get((0, 3)) == None)


if __name__ == "__main__":
    unittest.main()
    SCREEN = Screen("Screen one", 2)
    print("SIZE 2 SCREEN: \n", *SCREEN.screen, sep="\n")
    SCREEN.resize(4)
    print("SIZE 4 SCREEN: \n", *SCREEN.screen, sep="\n")
    SCREEN.resize(3)
    print("SIZE 3 SCREEN: \n", *SCREEN.screen, sep="\n")
