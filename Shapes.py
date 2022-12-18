import os


def path(path):
    last_slash = path.rfind("/")
    # Find the last forward slash in the input parameter path to seperate the string into name and path on.
    filename = path[last_slash+1:]
    # Grab the filename from the input parameter path.
    path = "Visuals/" + path[:last_slash]
    # Grab the path from the input parameter path and append "Visuals" as all presets will be found the the Visuals folder.
    os.makedirs(path, exist_ok=True)
    return os.path.join(path, filename).replace("\\", "/")


def generate_horizontal_line(char, length, path):
    if length == 0:
        return False
    # Check if LINE contains no values/doesn't contain anything and if so cancel out.
    LINE = "".join([char for _ in range(length)])
    # Make LINE acording to the input parameters.
    with open(path, "w") as f:
        f.write(LINE)
        # Print the line with no extra markup.


def generate_vertical_line(char, length, path):
    if length == 0:
        return False
    # Check if the line will contain no values and if so cancel out.
    with open(path, "w") as f:
        # Open the specified file in the Visuals folder
        for _ in range(length):
            f.write(f"{char}\n")


generate_horizontal_line('#', 5, path("Lines/H-Line.txt"))
generate_vertical_line('#', 5, path("Lines/V-Line.txt"))

