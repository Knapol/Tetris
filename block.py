from settings import *

class Block(pg.sprite.Sprite):
    def __init__(self, tetromino, pos):
        self.tetromino = tetromino
        self.pos = vec(pos) + SPAWN_POS
        self.on_map = True

        super().__init__(tetromino.tetris.sprite_group)
        self.image = pg.Surface([TILE_SIZE, TILE_SIZE])
        pg.draw.rect(self.image, TETROMINOES_COLORS[self.tetromino.shape], (1, 1, TILE_SIZE -2, TILE_SIZE-2), border_radius=8)

        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos * TILE_SIZE

    def is_on_map(self):
        if not self.on_map:
            self.kill()

    def update(self):
        self.is_on_map()
        self.rect.topleft = self.pos * TILE_SIZE

    def collide(self, pos):
        x, y = int(pos.x), int(pos.y)
        return not ( x >= 0 and x < WIDTH and y < HEIGHT and ( y < 0 or not self.tetromino.tetris.board[y][x]))
    
    def rotate(self, rotation_pivot, degree):
        shift = self.pos - rotation_pivot
        x, y = int(shift.x), int(shift.y)
        translation = vec(-y, x) if degree == "90" else vec(y, -x)
        return translation + rotation_pivot