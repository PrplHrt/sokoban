import arcade as arc

# Sizes of elements on the screen
SPRITE_NATIVE_SIZE = 128
SPRITE_SCALAR = 0.3
SPRITE_SIZE = int(SPRITE_NATIVE_SIZE * SPRITE_SCALAR)

# Number of cells for each level
WIDTH = 30
HEIGHT = 20

# Screen sizes and title
SCREEN_WIDTH = SPRITE_SIZE * WIDTH
SCREEN_HEIGHT = SPRITE_SIZE * HEIGHT
SCREEN_TITLE = "Sokoban"

# Symbol parsing
FLOOR = "-"
WALL = "#"
PLAYER = "@"
TARGET  = "."
BOX = "$"
BOX_ON_TARGET = "*"
PLAYER_ON_TARGET = "+"

SPRITES = {
    FLOOR : "assets/meriam_sokoban_sprites/floor.jpg",
    WALL: "assets/meriam_sokoban_sprites/wall.png",
    PLAYER: "assets/meriam_sokoban_sprites/player.png",
    TARGET: "assets/meriam_sokoban_sprites/target.png",
    BOX: "assets/meriam_sokoban_sprites/box.png",
    BOX_ON_TARGET:"assets/meriam_sokoban_sprites/box_on_target.png",
    PLAYER_ON_TARGET:"assets/meriam_sokoban_sprites/floor.jpg"
}

# Created child class of arcade.Window
class MyWindow(arc.Window):
    def __init__(self, w: int, h: int, t: str):
        # Prepare the Window
        super().__init__(w, h, t)
        arc.set_background_color(arc.color.AMARANTH_PURPLE)

        self.get_level()

    def get_level(self, file_name = "assets/levels/lvl_1.txt"):
        f = open(file_name)
        self.level = []
        self.num_boxes = 0
        for line in f:
            # Creating list of character lists, excluding the newline character
            self.level.append(list(line[:-1].replace("\t", "")))
        f.close()

    # Refreshes the screen
    def on_draw(self):
        arc.start_render()
        # Create all the sprites and render the level based on the level matrix
        sprites = arc.SpriteList()
        for i in range(HEIGHT):
            for j in range(WIDTH):
                floor = self.make_sprite(FLOOR, i, j)
                sprites.append(floor)

                if self.level[i][j] == FLOOR:
                    continue


                sprite = self.make_sprite(self.level[i][j], i, j)
                sprites.append(sprite)

                if self.level[i][j] == PLAYER_ON_TARGET:
                    sprite = self.make_sprite(PLAYER, i, j)
                    sprites.append(sprite)

        sprites.draw()

    # Helper function to create a sprite on specific coordinates
    def make_sprite(self, cell, i, j):
        sprite = arc.Sprite(SPRITES[cell], SPRITE_SCALAR)
        sprite.center_x = j * SPRITE_SIZE + (SPRITE_SIZE // 2)
        sprite.center_y = (HEIGHT - 1 - i) * SPRITE_SIZE + (SPRITE_SIZE // 2)
        return sprite

def main():
    # Creating game window with width, height, and title
    window = MyWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arc.run()



if __name__ == '__main__':
    main()