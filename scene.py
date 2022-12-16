import glm
import numpy as np

from engine.model import BaseModel, Triangle, Pyramid, Sphere, Cube
from engine.shader_program import ShaderProgram
from engine.light import LightSource
from solar_system import Sun, Mercury, Venus, Earth, Mars, Jupiter, Saturn, UrAnus, Neptune, DISTANCE_RATIO
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
        x = glm.sin(self.engine.time / 1000) / glm.cos(self.engine.time / 1000) * 8
        y = glm.sin(self.engine.time / 1000) / glm.cos(self.engine.time / 1000) * 8
        z = glm.sin(self.engine.time / 1000) / glm.cos(self.engine.time / 1000) * 8
        sphere.transform(pos=(x, y, z))

    def destroy(self):
        for obj in self.objects.values():
            obj.destroy()


class NBodySystemScene(Scene):
    def __init__(self, engine, step_size: float):
        super().__init__(engine)
        self.step_size = step_size

    def create_scene(self):
        # self.solar_system = AstronomicalSystem(
        #     "Solar System", 
        #     stars=np.array([Sun]),
        #     planets=np.array([Mercury, Venus, Earth, Mars, Jupiter, Saturn, UrAnus, Neptune])
        # )
        self.solar_system = AstronomicalSystem(
            "Solar System", 
            stars=np.array([Sun]),
            planets=np.array([Jupiter])
        )

        sun = self.solar_system.stars['Sun']
        # add light source
        self.engine.light = sun.model
        # add models
        self.add(sun.model.sphere, sun.name)
        for planet in self.solar_system.planets.values():
            self.add(planet.model, planet.name)

    def update(self):
        self.solar_system.update(self.step_size)
        center_of_mass = self.solar_system.get_center_of_mass()
        for obj in self.solar_system.objects:
            model = self.objects[obj.name]
            pos = obj.pos
            model.transform(pos=(pos - center_of_mass))

    def destroy(self):
        super().destroy()
        self.solar_system.destroy()
