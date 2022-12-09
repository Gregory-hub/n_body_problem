import glm

from graphics_engine.model import Cube, MovingCube, Cat


class Scene:
    def __init__(self, app):
        self.app = app
        self.objects = []
        self.load()

    def add_object(self, obj):
        self.objects.append(obj)

    def load(self): ...

    def update(self): ...


class SystemSimulationScene(Scene):
    def __init__(self, app):
        super().__init__(app)

    def load(self):
        for y in range(-30, 30):
            for x in range(-30, 30):
                self.add_object(Cube(self.app, 'cube', tex_id=0, pos=(x * 2, -3, y * 2)))
        # moving cube
        self.moving_cube = MovingCube(self.app, pos=(0, 9, 8), scale=(2, 3, 6), tex_id=2)
        self.add_object(self.moving_cube)

    def update(self):
        self.moving_cube.rot.xyz = self.app.time
