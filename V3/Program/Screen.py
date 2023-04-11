class Screen(object):
    def __init__(self, name, size) -> None:
        self.name = name
        self.size = size
        self.commands = []
        self.screen = {(y, x): " " for y in range(self.size-1, -1, -1) for x in range(self.size*3)}
    
    def clear(self):
        self.screen = {coords: " " for coords in self.screen}
    
    def resize(self, new_size):
        self.screen = {(y, x): self.screen.get((y, x), " ") for y in range(new_size-1, -1, -1) for x in range(new_size*3)}


if __name__ == "__main__":
    SCREEN = Screen("Screen one", 2)
    print("SIZE 2 SCREEN: \n", *SCREEN.screen, sep="\n")
    SCREEN.resize(2)
    print("SIZE 4 SCREEN: \n", *SCREEN.screen, sep="\n")
    SCREEN.resize(3)
    print("SIZE 3 SCREEN: \n", *SCREEN.screen, sep="\n")

