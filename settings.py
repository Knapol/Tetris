import pygame as pg

vec = pg.math.Vector2

WIDTH, HEIGHT = 10, 20
TILE_SIZE = 45

FPS = 60
GAME_RES = (WIDTH * TILE_SIZE, HEIGHT * TILE_SIZE)

ANIM_TIME_INTERVAL = 150

SPAWN_POS = vec(5, 0)

MOVE_DIRECTIONS = {
    'LEFT': vec(-1, 0),
    'RIGHT': vec(1, 0),
    'DOWN': vec(0, 1)
}

TETROMINOES = {
    'O': [(0,0), (0,-1), (-1, 0), (-1, -1)],
    "J": [(0,0), (-1, 0), (-1, -1), (1, 0)],
    "L": [(0,0), (-1, 0), (1,0), (1,-1)],
    "I": [(0,0), (-1,0), (-2,0), (1,0)],
    "Z": [(0,0), (0,-1), (-1, -1), (1, 0)],
    "S": [(0,0), (0,-1), (1,-1), (-1, 0)],
    "T": [(0,0), (0, -1), (-1,0), (1,0)]
}

TETROMINOES_COLORS = {
    'O': 'orange',
    "J": 'blue',
    "L": 'yellow',
    "I": 'cyan',
    "Z": 'red',
    "S": 'green',
    "T": 'purple' 
}