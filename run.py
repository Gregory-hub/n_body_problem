from engine import engine
from scene import NBodySystemScene, Scene


if __name__ == "__main__":
    scene = NBodySystemScene(engine, step_size=0.5)
    # scene = Scene(engine)
    engine.set_scene(scene)
    engine.run()
