import numpy as np

from engine.model import Sphere
from engine.light import LightSource

G = 6.67430151515e-11

RUNGE_KUTTA = False
EULER = True        # semi-implicit


class AstronomicalObject:
    def __init__(self, name: str, mass: float, pos: np.array, velocity: np.array):
        if len(pos) != 3 or len(velocity) != 3:
            raise ValueError(f"dimensions number is 3 (pos len is {len(pos)}, velocity is {len(velocity)}")
        self.name = name
        self.mass = mass
        self.pos = pos
        self.v = velocity

    def __repr__(self):
        return f'<AstronomicalObject("{self.name}", position={self.pos}, v={self.v})>'

    def a(self, objects: np.array) -> np.array:
        a = sum([(G * obj.mass * (obj.pos - self.pos) / abs((obj.pos - self.pos)**3)) for obj in objects if obj is not self])
        return a


class Planet(AstronomicalObject):
    def __init__(self, name: str, mass: float, pos: np.array, velocity: np.array, model: Sphere):
        super().__init__(name, mass, pos, velocity)
        if not isinstance(model, Sphere):
            raise ValueError("Invalid model type: planet model must be of type Sphere")

        self.model = model

    def __repr__(self):
        return f'<Planet("{self.name}", position={self.pos}, v={self.v}, model={self.model})>'


class Star(AstronomicalObject):
    def __init__(self, name: str, mass: float, pos: np.array, velocity: np.array, model: LightSource):
        if not isinstance(model, LightSource):
            raise ValueError("Invalid model type: star model must be of type LightSource")

        super().__init__(name, mass, pos, velocity)
        self.model = model

    def __repr__(self):
        return f'<Planet("{self.name}", position={self.pos}, v={self.v}, model={self.model})>'


class AstronomicalSystem:
    def __init__(self, name: str, stars: np.array = np.array([]), planets: np.array = np.array([])):
        for star in stars:
            if not isinstance(star, Star):
                raise ValueError("Invalid star type: stars must be of type Star")
        for planet in planets:
            if not isinstance(planet, Planet):
                raise ValueError("Invalid planet type: planets must be of type Planet")

        self.stars = stars
        self.planets = planets
        self.objects = np.hstack([stars, planets])
        self.simulation_time = 0

    def update(self, step: float):
        if RUNGE_KUTTA:
            pass
        else:
            for obj in self.objects:
                obj.v = obj.v + step * obj.a(self.objects)
            for obj in self.objects:
                obj.pos = obj.pos + step * obj.v
        
        self.simulation_time += step

    # def get_center_of_mass(self):
    #     system_mass = 0
    #     center_of_mass = np.array([0, 0, 0])
    #     for obj in self.objects:
    #         center_of_mass = center_of_mass + obj.mass * obj.pos
    #         system_mass += obj.mass

    #     return center_of_mass / system_mass
