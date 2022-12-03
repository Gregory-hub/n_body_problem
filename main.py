from astronomy import AstronomicalObject, AstronomicalSystem, vector


# initial data for 00:00 1 Jan 2022
# distance in astronomical units
# velocity in au per day
Sun = AstronomicalObject(
    name="Sun",
    mass=1,
    init_pos=vector([0, 0, 0]),
    init_velocity=vector([0, 0, 0])
)

Mercury = AstronomicalObject(
    name="Mercury",
    mass=1.6601e-7,
    init_pos=vector([0.3590263039200, -0.0229458780572, -0.0494704545935]),
    init_velocity=vector([-0.0022692079504, 0.0257700545646, 0.0140014950319])
)

Venus = AstronomicalObject(
    name="Venus",
    mass=2.4478383e-6,
    init_pos=vector([-0.0678814025257, 0.6514805708508, 0.2974322037225]),
    init_velocity=vector([-0.0202047774015, -0.0023048192363, 0.0002413085411])
)

Earth = AstronomicalObject(
    name="Earth",
    mass=3.00348959632e-6,
    init_pos=vector([-0.1746675687485, 0.8878826973429, 0.3848945796490]),
    init_velocity=vector([-0.0172179458030, -0.0028624618993, -0.0012400661907])
)

Mars = AstronomicalObject(
    name="Mars",
    mass=3.227151e-7,
    init_pos=vector([-0.8667639099172, -1.1620088222984, -0.5096020231611]),
    init_velocity=vector([0.0120799162865, -0.0059678982168, -0.0030632775140])
)

Jupiter = AstronomicalObject(
    name="Jupiter",
    mass=9.5479194e-4,
    init_pos=vector([4.6580839119399, -1.6079842796591, -0.8026120479031]),
    init_velocity=vector([0.0026255239604, 0.0068288077571, 0.0028631090151])
)

Saturn = AstronomicalObject(
    name="Saturn",
    mass=2.858860e-4,
    init_pos=vector([6.9600794880566, -6.4221819669368, -2.9523453929819]),
    init_velocity=vector([0.0036673089657, 0.0036725811771, 0.0013591340670])
)

UrAnus = AstronomicalObject(
    name="UrAnus",
    mass=4.366244e-5,
    init_pos=vector([14.3976311704513, 12.4207826542699, 5.2362778149696]),
    init_velocity=vector([-0.0027147204414, 0.0024550008067, 0.0011134711530])
)

Neptune = AstronomicalObject(
    name="Neptune",
    mass=5.151389e-5,
    init_pos=vector([29.6332690545131, -3.5149104192983, -2.1764797008247]),
    init_velocity=vector([0.0004116004817, 0.0029073350314, 0.0011798561193])
)

system = AstronomicalSystem("Solar System", vector([Sun, Mercury, Venus, Earth, Mars, Jupiter, Saturn, UrAnus, Neptune]))
print(system.get_center_of_mass())
for i in range(10000):
    system.update(h=1 / 24)   # 1 hour

print(system.get_center_of_mass())
