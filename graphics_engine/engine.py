import sys
import pygame as pg

import moderngl as mgl

from graphics_engine.model import *
from graphics_engine.camera import Camera
from graphics_engine.light import Light
from graphics_engine.mesh import Mesh
from graphics_engine.scene import Scene
from graphics_engine.scene_renderer import SceneRenderer


class GraphicsEngine:
    def __init__(self, win_size=(1600, 900), scene: Scene=None):
        self.WIN_SIZE = win_size
        pg.init()

        # set opengl attr
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)

        # create opengl context
        pg.display.set_mode((0, 0), flags=pg.OPENGL | pg.DOUBLEBUF | pg.FULLSCREEN, vsync=1)

        # mouse settings
        pg.event.set_grab(True)
        pg.mouse.set_visible(False)

        # detect and use existing opengl context
        self.ctx = mgl.create_context()
        # self.ctx.front_face = 'cw'
        self.ctx.enable(flags=mgl.DEPTH_TEST | mgl.CULL_FACE)

        self.clock = pg.time.Clock()
        self.time = 0
        self.delta_time = 0

        self.light = Light()
        self.camera = Camera(self)
        self.mesh = Mesh(self)
        self.scene = scene(self)
        self.scene_renderer = SceneRenderer(self)
    
    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.mesh.destroy()
                self.scene_renderer.destroy()
                pg.quit()
                sys.exit()

    def render(self):
        # clear framebuffer
        self.ctx.clear(color=(0.01, 0.01, 0.05))
        # self.ctx.clear(color=(0, 0, 0))
        # render scene
        self.scene_renderer.render()
        # swap buffers
        pg.display.flip()

    def get_time(self):
        self.time = pg.time.get_ticks() * 0.001

    def run(self):
        while True:
            self.get_time()
            self.check_events()
            self.camera.update()
            self.render()
            self.delta_time = self.clock.tick(120)
