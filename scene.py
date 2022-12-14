import glm

from model import BaseModel, Triangle, Pyramid, Sphere, Cube
from shader_program import ShaderProgram


class Scene:
    def __init__(self, engine):
        self.engine = engine
        self.ctx = engine.ctx
        self.objects = []
        self.create_scene()

    def add(self, obj: BaseModel):
        self.objects.append(obj)

    def create_scene(self):
        # self.add(Pyramid(self.engine, pos=(2, 1, 5)))
        self.add(Sphere(self.engine, pos=(1, 2, -2), color=(1, 1, 0.2), scale=1, quality=0.5))
        self.add(Sphere(self.engine, pos=(9, -2, 5), color=(0.1, 0.5, 0.3)))
        self.add(Sphere(self.engine, pos=(-6, 3, 0), color=(0.1, 0.6, 0.5)))
        self.add(Sphere(self.engine, pos=(-2, -5, 4), color=(0.8, 0.4, 0.9)))
        self.add(Cube(self.engine, pos=(4, 4, 8)))

    def render(self):
        self.update()
        for obj in self.objects:
            obj.render()

    def update(self):
        pass
        # triangle = self.objects[0]
        # model_matrix = glm.rotate(self.objects[0].model_matrix, self.objects[0].engine.time / 1000, glm.vec3(0, 1, 0))
        # self.objects[0].shader_program.update_input_variable('model_matrix', model_matrix)

    def destroy(self):
        for obj in self.objects:
            obj.destroy()
