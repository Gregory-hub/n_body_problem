import numpy as np

from engine import engine
from engine.model import Sphere
from engine.light import LightSource
from astronomy import Star, Planet


SCALE_RATIO = 2
DISTANCE_RATIO = 3
QUALITY = 1.6


# initial data for 00:00 1 Jan 2022
# distance in astronomical units
# velocity in au per day
sun_init_pos = np.array([0, 0, 0])
sun_init_v = np.array([0, 0, 0])

mercury_init_pos = np.array([0.3590263039200, -0.0229458780572, -0.0494704545935])
mercury_init_v = np.array([-0.0022692079504, 0.0257700545646, 0.0140014950319])

venus_init_pos = np.array([-0.0678814025257, 0.6514805708508, 0.2974322037225])
venus_init_v = np.array([-0.0202047774015, -0.0023048192363, 0.0002413085411])

earth_init_pos = np.array([-0.1746675687485, 0.8878826973429, 0.3848945796490])
earth_init_v = np.array([-0.0172179458030, -0.0028624618993, -0.0012400661907])

moon_init_pos = np.array([-0.17528096,  0.88577673,  0.38392321])
moon_init_v = np.array([-0.01660511, -0.00297692, -0.00134978])

mars_init_pos = np.array([-0.8667639099172, -1.1620088222984, -0.5096020231611])
mars_init_v = np.array([0.0120799162865, -0.0059678982168, -0.0030632775140])

jupiter_init_pos = np.array([4.6580839119399, -1.6079842796591, -0.8026120479031])
jupiter_init_v = np.array([0.0026255239604, 0.0068288077571, 0.0028631090151])

saturn_init_pos = np.array([6.9600794880566, -6.4221819669368, -2.9523453929819])
saturn_init_v = np.array([0.0036673089657, 0.0036725811771, 0.0013591340670])

uranus_init_pos = np.array([14.3976311704513, 12.4207826542699, 5.2362778149696])
uranus_init_v = np.array([-0.0027147204414, 0.0024550008067, 0.0011134711530])

nuptune_init_pos = np.array([29.6332690545131, -3.5149104192983, -2.1764797008247])
nuptune_init_v = np.array([0.0004116004817, 0.0029073350314, 0.0011798561193])


Sun = Star(
    name="Sun",
    mass=1,
    pos=np.array(sun_init_pos),
    velocity=np.array(sun_init_v),
    model=LightSource(engine, pos=sun_init_pos * DISTANCE_RATIO, sphere_color=[0.95, 1, 0.25], scale=0.25 * SCALE_RATIO, quality=int(10 * QUALITY))
)

Mercury = Planet(
    name="Mercury",
    mass=1.6601e-7,
    pos=np.array(mercury_init_pos),
    velocity=np.array(mercury_init_v),
    model=Sphere(engine, pos=mercury_init_pos * DISTANCE_RATIO, color=[0.3, 0.3, 0.3], scale=0.05 * SCALE_RATIO, quality=int(10 * QUALITY))
)

Venus = Planet(
    name="Venus",
    mass=2.4478383e-6,
    pos=np.array(venus_init_pos),
    velocity=np.array(venus_init_v),
    model=Sphere(engine, pos=venus_init_pos * DISTANCE_RATIO, color=[0.9, 0.8, 0.7], scale=0.08 * SCALE_RATIO, quality=int(10 * QUALITY))
)

Earth = Planet(
    name="Earth",
    mass=3.00348959632e-6,
    pos=np.array(earth_init_pos),
    velocity=np.array(earth_init_v),
    model=Sphere(engine, pos=earth_init_pos * DISTANCE_RATIO, color=[0.18, 0.4, 0.6], scale=0.1 * SCALE_RATIO, quality=int(10 * QUALITY))
)

Moon = Planet(
    name="Moon",
    mass=3.694154394167924e-08,
    pos=np.array(moon_init_pos),
    velocity=np.array(moon_init_v),
    # model=Sphere(engine, pos=moon_init_pos * DISTANCE_RATIO, color=[0.3 , 0.27 , 0.26], scale=0.02 * SCALE_RATIO, quality=int(10 * QUALITY))
    model=Sphere(engine, pos=moon_init_pos * DISTANCE_RATIO, color=[0.9 , 0.9 , 0.9], scale=0.05 * SCALE_RATIO, quality=int(10 * QUALITY))
)

Mars = Planet(
    name="Mars",
    mass=3.227151e-7,
    pos=np.array(mars_init_pos),
    velocity=np.array(mars_init_v),
    model=Sphere(engine, pos=mars_init_pos * DISTANCE_RATIO, color=[0.6, 0.24, 0], scale=0.09 * SCALE_RATIO, quality=int(10 * QUALITY))
)

Jupiter = Planet(
    name="Jupiter",
    mass=9.5479194e-4,
    pos=np.array(jupiter_init_pos),
    velocity=np.array(jupiter_init_v),
    model=Sphere(engine, pos=jupiter_init_pos * DISTANCE_RATIO, color=[0.69, 0.5, 0.2], scale=0.3 * SCALE_RATIO, quality=int(10 * QUALITY))
)

Saturn = Planet(
    name="Saturn",
    mass=2.858860e-4,
    pos=np.array(saturn_init_pos),
    velocity=np.array(saturn_init_v),
    model=Sphere(engine, pos=saturn_init_pos * DISTANCE_RATIO, color=[0.69, 0.56, 0.21], scale=0.25 * SCALE_RATIO, quality=int(10 * QUALITY))
)

UrAnus = Planet(
    name="Uranus",
    mass=4.366244e-5,
    pos=np.array(uranus_init_pos),
    velocity=np.array(uranus_init_v),
    model=Sphere(engine, pos=uranus_init_pos * DISTANCE_RATIO, color=[0.33, 0.5, 0.66], scale=0.4 * SCALE_RATIO, quality=int(10 * QUALITY))
)

Neptune = Planet(
    name="Neptune",
    mass=5.151389e-5,
    pos=np.array(nuptune_init_pos),
    velocity=np.array(nuptune_init_v),
    model=Sphere(engine, pos=nuptune_init_pos * DISTANCE_RATIO, color=[0.21, 0.4, 0.58], scale=0.5 * SCALE_RATIO, quality=int(10 * QUALITY))
)

BigBrother = Planet(
    name="Big Brother",
    mass=0.5,
    pos=np.array([4, 0, 0]),
    velocity=np.array([-0.002, -0.005, 0.0001]),
    model=Sphere(engine, pos=np.array([5, 1, -5]) * DISTANCE_RATIO, color=[0.9, 0.2, 0.3], scale=0.5 * SCALE_RATIO, quality=int(10 * QUALITY))
)
