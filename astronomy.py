from numpy import array as vector

G = 6.67430151515e-11

RUNGE_KUTTA = False
EULER = True        # semi-implicit


class AstronomicalObject:
    def __init__(self, name: str, mass: float, init_pos: vector, init_velocity: vector):
        if len(init_pos) != 3 or len(init_velocity) != 3:
            raise ValueError(f"dimensions number is 3 (init_pos len is {len(init_pos)}, init_velocity is {len(init_velocity)}")
        self.name = name
        self.mass = mass
        self.pos = init_pos
        self.v = init_velocity

    def __repr__(self):
        return f'<AstronomicalObject("{self.name}", position={self.pos}, v={self.v})>'

    def a(self, objects: vector) -> vector:
        return sum([(G * obj.mass * (obj.pos - self.pos) / abs((obj.pos - self.pos)**3)) for obj in objects if obj is not self])


class AstronomicalSystem:
    def __init__(self, name: str, objects: vector = vector([])):
        self.objects = objects

    def update(self, h: float):
        if RUNGE_KUTTA:
            pass
        else:
            for obj in self.objects:
                obj.v = obj.v + h * obj.a(self.objects)
            for obj in self.objects:
                obj.pos = obj.pos + h * obj.v
