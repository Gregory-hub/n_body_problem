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
        # axes
        self.add_object(Cube(self.app, 'cube', pos=(0, 0, 0), scale=(100, 0.05, 0.05), shade=False))

        self.add_object(Cube(self.app, 'cube', pos=(0, 0, 0), scale=(0.05, 100, 0.05), shade=False))

        self.add_object(Cube(self.app, 'cube', pos=(0, 0, 0), scale=(0.05, 0.05, 100), shade=False))

        self.add_object(Cube(self.app, 'cube', pos=(0, -3, 0), scale=(50, 1, 50), shade=False))

        # moving cube
        self.moving_cube = MovingCube(self.app, pos=(10, 10, 20), scale=(2, 2, 2), tex_id=2)
        self.add_object(self.moving_cube)

        self.add_object(Cube(self.app, 'cube', pos=(20, 3, 20)))

    def update(self):
        self.moving_cube.rot.xyz = self.app.time
