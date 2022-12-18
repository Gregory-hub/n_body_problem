from engine import engine
from scene import NBodySystemScene


if __name__ == "__main__":
    scene = NBodySystemScene(engine, step_size=10, update_period=1)
    engine.setup(scene)
    engine.run()
