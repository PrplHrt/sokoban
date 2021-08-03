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
FLOOR = " "
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
    BOX_ON_TARGET:"assets/meriam_sokoban_sprites/box_on_target.jpg",
    PLAYER_ON_TARGET:"assets/meriam_sokoban_sprites/floor.jpg"
}

# Created child class of arcade.Window
class LevelWindow(arc.Window):
    def __init__(self, w: int, h: int, t: str, f = "lvl_3.txt"):
        # Prepare the Window
        super().__init__(w, h, t)
        arc.set_background_color(arc.color.AMARANTH_PURPLE)

        
        f = open("assets/levels/" + f)
        self.level = []
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

    def inside(self, i, j):
        return 0 <= i < HEIGHT and 0 <= j < WIDTH

    def move_player(self, di, dj):
        # Find player first
        pi, pj = -1, -1
        for i in range(len(self.level)):
            for j in range(len(self.level[i])):
                if self.level[i][j] in [PLAYER , PLAYER_ON_TARGET]:
                    pi, pj = i, j
                    break
        
        under_player = FLOOR 
        if self.level[pi][pj] != PLAYER:
            under_player = TARGET

        cell1_i = pi + di
        cell1_j = pj + dj

        if not self.inside(cell1_i, cell1_j):
            return
        
        cell1 = self.level[cell1_i][cell1_j]

        if cell1 == WALL:
            return
        
        if cell1 == FLOOR:
            self.level[pi][pj] = under_player
            self.level[cell1_i][cell1_j] = PLAYER
            return
        
        if cell1 == TARGET:
            self.level[pi][pj] = under_player
            self.level[cell1_i][cell1_j] = PLAYER_ON_TARGET
            return
        
        # if BOX or BOX_ON_TARGET is in cell1
        cell2_i, cell2_j = cell1_i + di, cell1_j + dj
        
        if not self.inside(cell2_i, cell2_j):
            return
        
        cell2 = self.level[cell2_i][cell2_j]

        if cell2 in [BOX, BOX_ON_TARGET, WALL]:
            return

        self.level[pi][pj] = under_player

        if cell1 == BOX_ON_TARGET:
            self.level[cell1_i][cell1_j] = PLAYER_ON_TARGET
        elif cell1 == BOX:
            self.level[cell1_i][cell1_j] = PLAYER

        if cell2 == FLOOR:
            self.level[cell2_i][cell2_j] = BOX
        else:
            self.level[cell2_i][cell2_j] = BOX_ON_TARGET


   
    def on_key_press(self, key: int, modifiers: int):
        if key == arc.key.UP or key == arc.key.W:
            self.move_player(-1, 0)
        if key == arc.key.DOWN or key == arc.key.S:
            self.move_player(1, 0)
        if key == arc.key.RIGHT or key == arc.key.D:
            self.move_player(0, 1)
        if key == arc.key.LEFT or key == arc.key.A:
            self.move_player(0, -1)

def main():
    # Creating game window with width, height, and title
    window = LevelWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arc.run()



if __name__ == '__main__':
    main()