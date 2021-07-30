import arcade as arc

class game():
    def __init__(self):
        f = open("levels/lvl_1.txt")
        self.level = []
        for line in f:
            # Creating list of character lists, excluding the newline character
            self.level.append(list(line[:-1]))
        f.close()

    