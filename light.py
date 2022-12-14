import glm


class Light:
    def __init__(self, pos: tuple = (0, 0, 0), color: tuple = (1, 1, 1)):
        self.pos = glm.vec3(pos)
        self.color = glm.vec3(color)

        self.ambient_intensity = 0.1 * self.color
        self.diffuse_intensity = 0.8 * self.color
        self.specular_intensity = 1 * self.color
