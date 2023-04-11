import unittest
from Logging import Log, LogLevel

class Screen(object):
    def __init__(self, name, size, log=Log("Screen", LogLevel.ERROR)) -> None:
        self.name = name
        self.size = size
        self.commands = []
        self.screen = {(x, y): " " for y in range(self.size, -1, -1) for x in range(self.size*3)}
        self.log = log

    def clear(self):
        self.screen = {coords: " " for coords in self.screen}

    def resize(self, new_size):
        self.screen = {(x, y): self.screen.get((x, y), " ") for y in range(new_size, -1, -1) for x in range(new_size*3)}

    def write(self, char, x, y):
        if (x, y) not in self.screen.keys():
            self.log.error("Target key not found. Coordinates out of bound.")
            return IndexError("Target key not found. Coordinates out of bound.")
        self.screen.update({(x, y): char})


class TestScreen(unittest.TestCase):

    def test_resize(self):
        SCREEN = Screen("ResizeTestScreen", 1, Log("ScreenResizeTest", LogLevel.QUIET))
        self.assertTrue(SCREEN.screen.get((0, 3)) == None)
        SCREEN.resize(4)
        self.assertTrue(SCREEN.screen.get((0, 3)) == " ")
        SCREEN.resize(2)
        self.assertTrue(SCREEN.screen.get((0, 3)) == None)

    def test_write(self):
        SCREEN = Screen("WriteTestScreen", 2, Log("ScreenResizeTest", LogLevel.QUIET))
        with IndexError("Target key not found. Coordinates out of bound."):
            self.assertRaises(SCREEN.write("x", 0, 3))
        self.assertIsNone(SCREEN.write("x", 0, 2))
        self.assertEqual(SCREEN.screen.get((0, 2)), "x")


if __name__ == "__main__":
    #unittest.main()
    SCREEN = Screen("Screen one", 2)
    print("SIZE 2 SCREEN: \n", *SCREEN.screen, sep="\n")
    SCREEN.resize(4)
    print("SIZE 4 SCREEN: \n", *SCREEN.screen, sep="\n")
    SCREEN.resize(3)
    print("SIZE 3 SCREEN: \n", *SCREEN.screen, sep="\n")
