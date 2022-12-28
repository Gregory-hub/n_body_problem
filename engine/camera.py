import glm
import pygame as pg


FOV = 60
NEAR = 0.1
FAR = 1000
SENSITIVITY = 0.2
SPEED = 1


class Camera:
    def __init__(self, engine, pos=(0, 0, -40), yaw=90, pitch=0):
        self.engine = engine
        self.aspect_ratio = self.engine.WIN_SIZE[0] / self.engine.WIN_SIZE[1]
        self.up = glm.vec3(0, 1, 0)
        self.pos = glm.vec3(pos)
        self.dist = (self.pos.x**2 + self.pos.y**2 + self.pos.z**2)**(1/2)
        self.yaw = yaw
        self.pitch = max(-89, min(89, pitch))
        self.view_matrix = self.get_view_matrix()
        self.proj_matrix = self.get_protjection_matrix()
        self.update_camera_vectors()

    def get_protjection_matrix(self):
        return glm.perspective(glm.radians(FOV), self.aspect_ratio, NEAR, FAR)

    def get_view_matrix(self):
        return glm.lookAt(self.pos, glm.vec3(0), self.up)

    def move(self):
        keys = pg.key.get_pressed()
        sensitivity = SENSITIVITY * self.engine.frame_timedelta.microseconds // 1000

        if keys[pg.K_LCTRL]:
            velocity = SPEED * self.engine.frame_timedelta.microseconds // 100
        else:
            velocity = SPEED * self.engine.frame_timedelta.microseconds // 1000

        if keys[pg.K_w]:
            self.dist -= velocity / 60
            self.dist = max(3, self.dist)
            self.update_camera_vectors()

        if keys[pg.K_s]:
            self.dist += velocity / 60
            self.dist = max(3, self.dist)
            self.update_camera_vectors()

        if keys[pg.K_a]:
            self.yaw += sensitivity
            self.update_camera_vectors()

        if keys[pg.K_d]:
            self.yaw -= sensitivity
            self.update_camera_vectors()

        if keys[pg.K_SPACE]:
            self.pitch += sensitivity / 2
            self.pitch = max(-89, min(89, self.pitch))
            self.update_camera_vectors()

        if keys[pg.K_LSHIFT]:
            self.pitch -= sensitivity / 2
            self.pitch = max(-89, min(89, self.pitch))
            self.update_camera_vectors()

    def update_camera_vectors(self):
        yaw, pitch = glm.radians(self.yaw), glm.radians(self.pitch)
        x = self.dist * glm.cos(yaw) * glm.cos(pitch)
        y = self.dist * glm.sin(pitch)
        z = self.dist * glm.sin(yaw) * glm.cos(pitch)
        self.pos = glm.vec3(x, y, z)

    def update(self):
        self.move()
        self.view_matrix = self.get_view_matrix()
