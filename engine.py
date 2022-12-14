import sys

import pygame as pg
import moderngl as mgl

from scene import Scene
from camera import Camera
from light import Light

class GraphicsEngine:
    def __init__(self, win_size: tuple = (1600, 900)):
        self.WIN_SIZE = win_size
        pg.init()

        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)

        pg.display.set_mode(self.WIN_SIZE, flags=pg.OPENGL | pg.DOUBLEBUF) # | pg.FULLSCREEN, vsync=1)

        # pg.event.set_grab(True)
        # pg.mouse.set_visible(False)

        self.ctx = mgl.create_context()
        self.ctx.enable(flags=mgl.DEPTH_TEST)

        self.camera = Camera(self)
        self.light = Light()
        self.clock = pg.time.Clock()
        self.time = 0
        self.delta_time = 0

        self.scene = Scene(self)

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.scene.destroy()
                pg.quit()
                sys.exit()

    def render(self):
        self.ctx.clear(color=(0, 0, 0.05))
        self.scene.render()
        pg.display.flip()

    def update_time(self):
        self.time = pg.time.get_ticks() # * 0.001

    def run(self):
        while True:
            self.check_events()
            self.update_time()
            self.camera.update()
            self.render()
            self.delta_time = self.clock.tick(60)
