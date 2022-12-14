import glm
import numpy as np

from engine.model import BaseModel, Triangle, Pyramid, Sphere, Cube
from engine.shader_program import ShaderProgram
from engine.light import LightSource
from solar_system import Sun, Mercury, Venus, Earth, Mars, Jupiter, Saturn, UrAnus, Neptune
from astronomy import AstronomicalSystem


class Scene:
    def __init__(self, engine):
        self.engine = engine
        self.ctx = engine.ctx
        self.objects = {}
        self.create_scene()

    def add(self, obj: BaseModel, name: str):
        self.objects[name] = obj

    def create_scene(self):
        self.engine.light = LightSource(self.engine)
        self.add(self.engine.light.sphere, 'Sphere_0')
        self.add(Sphere(self.engine, pos=(0, 0, 0), color=(0.1, 0.5, 0.3)), 'Sphere_1')
        self.add(Sphere(self.engine, pos=(-6, 3, 0), color=(0.1, 0.6, 0.5)), 'Sphere_2')
        self.add(Sphere(self.engine, pos=(-2, -5, 4), color=(0.8, 0.4, 0.9)), 'Sphere_3')
        self.add(Cube(self.engine, pos=(4, 4, 8)), 'Cube_0')

    def render(self):
        self.update()
        for obj in self.objects.values():
            obj.render()

    def update(self):
        sphere = self.objects.get('Sphere_1')
        x = glm.cos(self.engine.time / 1000) * 8
        z = glm.sin(self.engine.time / 1000) * 8
        sphere.transform(pos=(x, sphere.pos[1], z))

    def destroy(self):
        for obj in self.objects.values():
            obj.destroy()


class NBodySystemScene(Scene):
    def __init__(self, engine):
        super().__init__(engine)

    def create_scene(self):
        solar_system = AstronomicalSystem(
            "Solar System", 
            stars=np.array([Sun]),
            planets=np.array([Mercury, Venus, Earth, Mars, Jupiter, Saturn, UrAnus, Neptune])
        )

        sun = solar_system.stars[0]
        # add light source
        self.engine.light = sun.model
        # add models
        self.add(sun.model.sphere, sun.name)
        for planet in solar_system.planets:
            self.add(planet.model, planet.name)

    def update(self):
        pass
        # sphere = self.objects.get('Sphere_1')
        # x = glm.cos(self.engine.time / 1000) * 8
        # z = glm.sin(self.engine.time / 1000) * 8
        # sphere.transform(pos=(x, sphere.pos[1], z))
