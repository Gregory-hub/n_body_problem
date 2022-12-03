from numpy import array as vector

G = 6.67430151515e-11


class AstronomicalObject:
	def __init__(self, name: str, mass: float, coords: vector, init_velocity: vector):
		if len(coords) != 2:
			raise ValueError(f"dimensions number is 2, not {len(coords)}")
		self.name = name
		self.mass = mass
		self.pos = coords
		self.v = init_velocity
	
	def __repr__(self):
		return f'<AstronomicalObject("{self.name}", position={self.pos}, v={self.v})>'
	
	def a(self, objects: vector):
		return sum([(G * obj.mass * (obj.pos - self.pos) / abs((obj.pos - self.pos)**3)) for obj in objects if obj is not self])


class AstronomicalSystem:
	def __init__(self, name: str, objects: vector = vector([])):
		self.objects = objects


