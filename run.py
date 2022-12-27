from engine import engine
from scene import NBodySystemScene


if __name__ == "__main__":
    scene = NBodySystemScene(engine, step_size=1, update_period=0.01, method="euler")   # max working update_period is 0.017
    engine.setup(scene)
    engine.run()
