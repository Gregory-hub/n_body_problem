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
        self.pos = np.array(pos)
        self.v = np.array(velocity)

    def __repr__(self):
        return f'<AstronomicalObject("{self.name}", position={self.pos}, v={self.v})>'

    def a(self, objects: np.array) -> np.array:
        a = np.array([0, 0, 0], dtype='f8')
        for obj in objects:
            if obj is not self:
                a += G * obj.mass * (obj.pos - self.pos) / abs((obj.pos - self.pos)**3)
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

        self.stars = {}
        for star in stars:
            self.stars[star.name] = star
        self.planets = {}
        for planet in planets:
            self.planets[planet.name] = planet

        self.objects = np.hstack([stars, planets])
        self.simulation_time = 0

        self.file = open('simulation.txt', 'w');

    def update(self, step: float):
        if RUNGE_KUTTA:
            pass
        else:
            for obj in self.objects:
                obj.v = obj.v + step * obj.a(self.objects)
            for obj in self.objects:
                obj.pos = obj.pos + step * obj.v

        self.simulation_time += step
        self.record(step)

    def record(self, step):
        self.file.write(f'SIMULATION TIME = {str(self.simulation_time)}, step size = {step}\n')
        for obj in self.objects:
            self.file.write(f'{obj.name}: position = {str(obj.pos)}, velocity = {str(obj.v)}\n')
        self.file.write('\n')

    def destroy(self):
        self.file.close()
