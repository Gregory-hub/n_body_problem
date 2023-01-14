import sys
from datetime import datetime as dt
from datetime import timedelta

import pygame as pg
import moderngl as mgl

from engine.camera import Camera


class GraphicsEngine:
    def __init__(self, win_size: tuple = (1600, 900), fullscreen: bool = False):
        self.WIN_SIZE = win_size
        pg.init()

        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)

        if fullscreen:
            pg.display.set_mode((0, 0), flags=pg.OPENGL | pg.DOUBLEBUF | pg.FULLSCREEN, vsync=1)
        else:
            pg.display.set_mode(self.WIN_SIZE, flags=pg.OPENGL | pg.DOUBLEBUF)

        pg.event.set_grab(True)
        pg.mouse.set_visible(False)

        self.ctx = mgl.create_context()
        self.ctx.enable(flags=mgl.DEPTH_TEST)

        self.camera = Camera(self, pos=(0, 0, -40))
        self.clock = pg.time.Clock()
        self.time = dt.now()
        self.frame_timedelta = timedelta()

        self.scene = None
        self.update_period = None
        self.update_timedelta = timedelta()

    def setup(self, scene):
        # updates system every period seconds
        self.scene = scene
        self.update_period = timedelta(microseconds=self.scene.update_period)
        self.frame_timedelta = self.update_period

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.quit()

    def render(self):
        self.ctx.clear(color=(0, 0, 0))
        self.scene.render()
        pg.display.flip()

    def update_time(self):
        now = dt.now()
        self.frame_timedelta = now - self.time
        self.update_timedelta += self.frame_timedelta
        self.time = now

    def quit(self):
        if self.scene is not None:
            self.scene.destroy()
            self.on_exit()
            pg.quit()
            sys.exit()
        else:
            raise AttributeError("Trying to run with no scene. Run set_scene(scene) before run()")

    def on_exit(self):
        print(f"System update time range: from {self.min_step_time}s to {self.max_step_time}s")

    def run(self):
        step = 1
        self.max_step_time = 0
        self.min_step_time = 10
        if self.scene is None:
            self.quit()
        while True:
            self.check_events()
            self.update_time()
            self.camera.update()
            if self.update_timedelta >= self.update_period:
                start = dt.now()

                self.scene.update()
                self.update_timedelta = timedelta()

                step += 1
                end = dt.now()
                step_time = (end - start)
                step_time = step_time.seconds + step_time.microseconds / 1000000
                print(f"System update time at step {step}: {step_time:<8f}s")
                if step_time > self.max_step_time:
                    self.max_step_time = step_time
                if step_time < self.min_step_time:
                    self.min_step_time = step_time
            self.render()
            self.clock.tick(60)    # framerate
