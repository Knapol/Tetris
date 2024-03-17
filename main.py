import sys
from settings import *

from tetris import Tetris

class App:
    def __init__(self):
        pg.init()
        pg.display.set_caption('Tetris')
        self.screen = pg.display.set_mode(GAME_RES)
        self.clock = pg.time.Clock()
        self.tetris = Tetris(self)

        self.is_running = True
        self.force_down = False

    def update(self):
        self.tetris.update()

    def draw(self):
        self.screen.fill(pg.Color('black'))
        self.tetris.draw()
        pg.display.flip()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                self.tetris.control(event.key)
    
    def run(self):
        ticks_counter = 0
        while True:
            ticks_counter += 1
            self.force_down = ticks_counter == 15

            self.check_events()
            self.update()
            self.draw()

            if self.force_down:
                ticks_counter = 0

            self.clock.tick(FPS)
            
if __name__ == '__main__':
    app = App()
    app.run()