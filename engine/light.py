import glm

from engine.model import Sphere


class Light:
    def __init__(self, pos: tuple = (0, 0, 0), color: tuple = (1, 1, 1)):
        self.pos = glm.vec3(pos)
        self.color = glm.vec3(color)

        self.ambient_intensity = 0.1 * self.color
        self.diffuse_intensity = 0.8 * self.color
        self.specular_intensity = 0.5 * self.color


class LightSource(Light):
    def __init__(self, engine, pos: tuple = (0, 0, 0), sphere_color: tuple = (1, 1, 0.2), light_color: tuple = (1, 1, 1), scale: int = 1, quality: int = 10):
        super().__init__(pos, light_color)
        self.engine = engine
        self.engine.light = self

        self.scale = scale
        self.quality = quality
        self.sphere = Sphere(self.engine, pos=pos, color=sphere_color, scale=self.scale, quality=self.quality)
        self.sphere.shader_program.update_input_variable('ignore_light', bytes(True))
