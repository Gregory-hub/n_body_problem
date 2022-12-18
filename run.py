from engine import engine
from scene import NBodySystemScene


if __name__ == "__main__":
    scene = NBodySystemScene(engine, step_size=2)
    # scene = Scene(engine)
    engine.set_scene(scene)
    engine.run()
