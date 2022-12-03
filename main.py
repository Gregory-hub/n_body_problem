from astronomy import AstronomicalObject, AstronomicalSystem, vector


Sun = AstronomicalObject("Sun", 1, vector([0, 0]), 0)
Earth = AstronomicalObject("Earth", 3.00348959632e-6, vector([1000, 2000]), 30000)
UrAnus = AstronomicalObject("UrAnus", 4.366244*1e-5, vector([-1000000000000000, -432000000000]), 30000)
objects = [Sun, Earth, UrAnus]
print(Sun)
print(Sun.a(objects))
