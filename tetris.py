from settings import *

from tetromino import Tetromino

class Tetris:
    def __init__(self, app):
        self.app = app
        self.sprite_group = pg.sprite.Group()
        self.tetromino = Tetromino(self)
        self.board = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]

    def update_rows(self):
        row = HEIGHT - 1

        for y in range(HEIGHT-1, -1, -1):
            for x in range(WIDTH):
                self.board[row][x] = self.board[y][x]

                if self.board[y][x]:
                    self.board[row][x].pos = vec(x, y)
            
            if sum(map(bool, self.board[y])) < WIDTH:
                row -= 1
            else:
                for x in range(WIDTH):
                    self.board[row][x].on_map = False
                    self.board[row][x] = 0

    def check_tetromino_status(self):
        if self.tetromino.landed:
            self.save_tetromino_on_board()
            if self.tetromino.is_above_limit():
                self.app.is_running = False
                return
            self.tetromino = Tetromino(self)

    def save_tetromino_on_board(self):
        for block in self.tetromino.blocks:
            x, y = int(block.pos.x), int(block.pos.y)
            self.board[y][x] = block

    def update(self):
        if self.app.force_down and self.app.is_running:
            self.tetromino.update()
            self.check_tetromino_status()
            self.update_rows()
        self.sprite_group.update()

    def draw(self):
        self.draw_grid()
        self.sprite_group.draw(self.app.screen)

    def draw_grid(self):
        for x in range(WIDTH):
            for y in range(HEIGHT):
                pg.draw.rect(self.app.screen, (40, 40, 40), (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)

    def control(self, pressed_key):
        if pressed_key == pg.K_LEFT:
            self.tetromino.move("LEFT")
        elif pressed_key == pg.K_RIGHT:
            self.tetromino.move("RIGHT")
        elif pressed_key == pg.K_z:
            self.tetromino.rotate("90")
        elif pressed_key == pg.K_UP:
            self.tetromino.rotate("270")
        elif pressed_key == pg.K_DOWN:
            self.tetromino.move("DOWN")
        elif pressed_key == pg.K_SPACE:
            self.tetromino.teleport_down()