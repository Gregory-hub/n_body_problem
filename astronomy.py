import numpy as np

from engine.model import Sphere
from engine.light import LightSource

G = 2.95912208286e-4


class AstronomicalObject:
    def __init__(self, name: str, mass: float, pos: list, velocity: list):
        if len(pos) != 3 or len(velocity) != 3:
            raise ValueError(f"dimensions number is 3 (pos len is {len(pos)}, velocity is {len(velocity)}")
        self.name = name
        self.mass = mass
        self.pos = np.array(pos, dtype=np.float64)
        self.v = np.array(velocity, dtype=np.float64)

    def __repr__(self):
        return f'<AstronomicalObject("{self.name}", position={self.pos}, v={self.v})>'

    def a(self, objects: np.array) -> np.array:
        a = np.array([0, 0, 0], dtype=np.float64)
        for obj in objects:
            if obj is not self:
                if np.linalg.norm(self.pos - obj.pos) != 0:
                    a -= G * obj.mass * (self.pos - obj.pos) / (np.linalg.norm(self.pos - obj.pos) ** 3)
        return a


class Planet(AstronomicalObject):
    def __init__(self, name: str, mass: float, pos: list, velocity: list, model: Sphere):
        super().__init__(name, mass, pos, velocity)
        if not isinstance(model, Sphere):
            raise ValueError("Invalid model type: planet model must be of type Sphere")

        self.model = model

    def __repr__(self):
        return f'<Planet("{self.name}", position={self.pos}, v={self.v}, model={self.model})>'


class Star(AstronomicalObject):
    def __init__(self, name: str, mass: float, pos: list, velocity: list, model: LightSource):
        if not isinstance(model, LightSource):
            raise ValueError("Invalid model type: star model must be of type LightSource")

        super().__init__(name, mass, pos, velocity)
        self.model = model

    def __repr__(self):
        return f'<Planet("{self.name}", position={self.pos}, v={self.v}, model={self.model})>'


class AstronomicalSystem:
    def __init__(self, name: str, stars: list, planets: list, method: str = "euler"):
        for star in stars:
            if not isinstance(star, Star):
                raise ValueError("Invalid star type: stars must be of type Star")
        for planet in planets:
            if not isinstance(planet, Planet):
                raise ValueError("Invalid planet type: planets must be of type Planet")
        available_methods = ["euler"]
        if method not in available_methods:
            raise ValueError(f"Invalid method: method must be one of {available_methods}")

        self.stars = {}
        for star in stars:
            self.stars[star.name] = star
        self.planets = {}
        for planet in planets:
            self.planets[planet.name] = planet

        stars = np.array(stars)
        planets = np.array(planets)
        self.objects = np.hstack([stars, planets])
        self.simulation_time = 0

        self.file = open('simulation.txt', 'w');

    def update(self, step: float):
        for obj in self.objects:
            obj.v = obj.v + step * obj.a(self.objects)
        for obj in self.objects:
            obj.pos = obj.pos + step * obj.v

        self.simulation_time += step
        self.record(step)

    def get_center_of_mass(self):
        mass = 0
        mr = np.array([0, 0, 0], dtype=np.float64)
        for obj in self.objects:
            mass += obj.mass
            mr += obj.mass * obj.pos

        return mr / mass

    def record(self, step):
        self.file.write(f'SIMULATION TIME = {str(self.simulation_time)}, step size = {step}\n')
        for obj in self.objects:
            line = f'{obj.name:<10}: pos={str(obj.pos):<50} v={str(obj.v):<50} a={str(obj.a(self.objects)):<50}\n'
            self.file.write(line)
        self.file.write('\n')

    def destroy(self):
        self.file.close()
