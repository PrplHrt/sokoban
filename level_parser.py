import arcade as arc

# Sizes of elements on the screen
SPRITE_NATIVE_SIZE = 128
SPRITE_SCALAR = 0.25
SPRITE_SIZE = int(SPRITE_NATIVE_SIZE * SPRITE_SCALAR)

# Number of cells for each level
WIDTH = 30
HEIGHT = 20

# Screen sizes and title
SCREEN_WIDTH = SPRITE_SIZE * WIDTH
SCREEN_HEIGHT = SPRITE_SIZE * HEIGHT
SCREEN_TITLE = "Sokoban"

# Symbol parsing
FLOOR = " "
WALL = "#"
PLAYER = "@"
TARGET  = "."
BOX = "$"
BOX_ON_TARGET = "*"
PLAYER_ON_TARGET = "+"

SPRITES1 = {
    FLOOR : "assets/meriam_sokoban_sprites/floor.jpg",
    WALL: "assets/meriam_sokoban_sprites/wall.png",
    PLAYER: "assets/meriam_sokoban_sprites/player.png",
    TARGET: "assets/meriam_sokoban_sprites/target.png",
    BOX: "assets/meriam_sokoban_sprites/box.png",
    BOX_ON_TARGET:"assets/meriam_sokoban_sprites/box_on_target.png",
}

# Created child class of arcade.Window
class MyWindow(arc.Window):
    def __init__(self, w: int, h: int, t: str):
        # Prepare the Window
        super().__init__(w, h, t)
        arc.set_background_color(arc.color.AMARANTH_PURPLE)

        self.get_level()

    def get_level(self, file_name = "levels/lvl_1.txt"):
        f = open("levels/lvl_1.txt")
        self.level = []
        self.num_boxes = 0
        for line in f:
            # Getting numbe of boxes in level
            for char in line:
                if char == BOX or char == BOX_ON_TARGET:
                    self.num_boxes += 1

            # Creating list of character lists, excluding the newline character
            self.level.append(list(line[:-1]))
        f.close()

    # Refreshes the screen
    def on_draw(self):
        arc.start_render()
        # Create sprite by getting the sprite image
        self.player = arc.Sprite("player.png", SPRITE_SCALAR)
        # Place the sprite at (100,100)
        self.player.center_x = 700
        self.player.center_y = 100
        # Draw the sprite
        self.player.draw()

        # Can create many sprites at the same time using a sprite list
        self.boxes = arc.SpriteList()

        for i in range(self.num_boxes):
            box = arc.Sprite("assets/meriam_sokoban_sprites/box.png", SPRITE_SCALAR)
            box.center_x = 70 * (i+1)
            box.center_y = 50 * (i+1)
            self.boxes.append(box)
        
        self.boxes.draw()


        

def main():
    # Creating game window with width, height, and title
    window = MyWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_HEIGHT)
    arc.run()



if __name__ == '__main__':
    main()