from settings import *
from block import Block
import random

class Tetromino:
    def __init__(self, tetris):
        self.tetris = tetris
        self.shape = random.choice(list(TETROMINOES.keys()))
        self.blocks = [Block(self, pos) for pos in TETROMINOES[self.shape]]
        self.landed = False

    def collide(self, block_positions):
        return any(map(Block.collide, self.blocks, block_positions))

    def move(self, direction):
        move_direction = MOVE_DIRECTIONS[direction]
        new_block_positions = [block.pos + move_direction for block in self.blocks]
        is_collide = self.collide(new_block_positions)

        if not is_collide:
            for block in self.blocks:
                block.pos += move_direction
        elif direction == "DOWN":
            self.landed = True
    
    def rotate(self, degree):
        rotation_pivot = self.blocks[0].pos
        new_block_positions = [block.rotate(rotation_pivot, degree) for block in self.blocks]
        is_collide = self.collide(new_block_positions)

        if not is_collide:
            for i in range(4):
                self.blocks[i].pos = new_block_positions[i]
                
    def update(self):
        self.move('DOWN')
    
    def is_above_limit(self):  
        for block in self.blocks:
            if int(block.pos.y) < 1:
                return True
        return False
    
    def teleport_down(self):
        while not self.landed:
            self.move("DOWN")