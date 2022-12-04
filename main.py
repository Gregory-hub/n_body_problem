from screeninfo import get_monitors

from solar_system import system
from graphics_engine.engine import GraphicsEngine
from graphics_engine.scene import SystemSimulationScene


if __name__ == "__main__":
    monitor = get_monitors()[0]
    engine = GraphicsEngine(win_size=(monitor.width, monitor.height), scene=SystemSimulationScene)
    engine.run()

    print(system.get_center_of_mass())
    for i in range(10000):
        system.update(h=1 / 24)   # 1 hour
