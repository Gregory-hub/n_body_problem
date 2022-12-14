from math import sqrt, pi

import numpy as np
import glm

from vbo import VBO
from shader_program import ShaderProgram
from vao import VAO


class BaseModel:
    def __init__(self, engine, shader_name: str = 'default', pos: tuple = (0, 0, 0), scale: tuple = (1, 1, 1)):
        self.pos = pos
        self.model_matrix = glm.translate(glm.mat4(), self.pos)
        self.scale = scale
        self.model_matrix = glm.scale(self.model_matrix, self.scale)

        self.engine = engine
        self.ctx = engine.ctx

        self.vertex_data, self.vbo_format, self.vbo_attrs = self.get_vbo_data()
        self.vbo = VBO(self.ctx, self.vertex_data, self.vbo_format, self.vbo_attrs)
        self.shader_program = ShaderProgram(self.ctx, shader_name)
        self.vao = VAO(self.ctx, self.vbo, self.shader_program)

        self.shader_program.update_input_variable('light.pos', self.engine.light.pos)
        self.shader_program.update_input_variable('light.ambient_intensity', self.engine.light.ambient_intensity)
        self.shader_program.update_input_variable('light.diffuse_intensity', self.engine.light.diffuse_intensity)
        self.shader_program.update_input_variable('proj_matrix', self.engine.camera.proj_matrix)
        self.shader_program.update_input_variable('view_matrix', self.engine.camera.view_matrix)
        self.shader_program.update_input_variable('model_matrix', self.model_matrix)

    def get_vbo_data(self): ...

    def render(self):
        self.update()
        self.vao.render()

    def update(self):
        pass
        self.shader_program.update_input_variable('view_matrix', self.engine.camera.view_matrix)
    
    def destroy(self):
        self.shader_program.destroy()


class Triangle(BaseModel):
    def __init__(self, engine, shader_name: str = 'default', pos: tuple = (0, 0, 0), color: tuple = (0.95, 0.95, 0.95), scale: tuple = (1, 1, 1)):
        super().__init__(engine, shader_name, pos, scale)
        self.color = glm.vec3(color)
        self.shader_program.update_input_variable('color', self.color)
    
    def get_vbo_data(self):
        vbo_format = '3f 3f'
        vbo_attrs = ['in_position', 'in_normal']
        vertices = np.array([
            (-0.5, -0.5, 0.0),
            (0.5, -0.5, 0.0),
            (0.0, 0.5, 0.0)], dtype='f4')

        normals = np.array([
            (0, 0, 1),
            (0, 0, 1),
            (0, 0, -1),
        ], dtype='f4')

        vertex_data = np.hstack([vertices, normals])

        return vertex_data, vbo_format, vbo_attrs


class Pyramid(BaseModel):
    def __init__(self, engine, shader_name: str = 'default', pos: tuple = (0, 0, 0), color: tuple = (0.95, 0.95, 0.95), scale: tuple = (1, 1, 1)):
        super().__init__(engine, shader_name, pos, scale)
        self.color = glm.vec3(color)
        self.shader_program.update_input_variable('color', self.color)

    def get_vbo_data(self):
        vbo_format = '3f'
        vbo_attrs = ['in_position']
        vertices = np.array([
            (-1, -2/3*((2/3)**(1/2)), 3**(1/2)/3),
            (1, -2/3*((2/3)**(1/2)), 3**(1/2)/3),
            (0.0, ((2/3)**(1/2)), 0.0),
            (0.0, -2/3*((2/3)**(1/2)), -3**(1/2)*2/3)]) / 2

        triangles = np.array([
            (0, 1, 2),
            (1, 3, 2),
            (1, 3, 0),
            (3, 0, 2)])
        
        vertex_data = np.array([vertices[i] for triangle in triangles for i in triangle], dtype='f4')

        return vertex_data, vbo_format, vbo_attrs


class Sphere(BaseModel):
    def __init__(self, engine, shader_name: str = 'default', pos: tuple = (0, 0, 0), color: tuple = (0.9, 0.9, 0.9), scale: int = 1, quality: int = 10):
        self.quality = quality
        super().__init__(engine, shader_name, pos, scale=(scale, scale, scale))
        self.color = glm.vec3(color)
        self.shader_program.update_input_variable('color', self.color)

    def get_vbo_data(self):
        # vbo_format = '3f'
        # vbo_attrs = ['in_position']
        vbo_format = '3f 3f'
        vbo_attrs = ['in_position', 'in_normal']

        vertices = []
        step = pi / 4 / self.quality    # affects number of triangles
        period = int(2 * pi / step)     # number of vertices at each circle
        for i in range(period):
            for j in range(period):
                yaw = i * step
                pitch = j * step
                x = glm.cos(yaw) * glm.cos(pitch)
                y = glm.sin(pitch)
                z = glm.sin(yaw) * glm.cos(pitch)
                vertices.append(np.array((x, y, z)))

        normals = []
        triangles = []
        for j in range(period - 1):
            start_point = j * period
            for i in range(period // 4 - 1):
                current_point = start_point + i
                triangle_1 = (current_point, current_point + 1, period + current_point)
                triangle_2 = (current_point + 1, current_point + period + 1, current_point + period)
                triangles.extend([
                        triangle_1,
                        triangle_2,
                    ])
                normal = self._get_normal(vertices[triangle_1[1]], vertices[triangle_2[2]])
                normals.extend([normal] * 6)

            # upper triangles
            triangle = (start_point + period // 4 - 1, start_point + period // 4, start_point + period + period // 4 - 1)
            triangles.extend([
                triangle,
            ])
            normal = self._get_normal(vertices[triangle[1]], (vertices[triangle[0]] + vertices[triangle[2]]) / 2)
            normals.extend([normal] * 3)

        # triangles between last period and 0
        start_point = period * period - period
        for i in range(period // 4 - 1):
            current_point = start_point + i
            triangle_1 = (current_point, current_point + 1, i)
            triangle_2 = (current_point + 1, i + 1, i)
            triangles.extend([
                    triangle_1,
                    triangle_2,
                ])
            normal = self._get_normal(vertices[triangle_1[1]], vertices[triangle_2[2]])
            normals.extend([normal] * 6)

        triangle = (period // 4 - 1 + start_point, period // 4 + start_point, period // 4 - 1)
        triangles.extend([
            triangle,
        ])
        normal = self._get_normal(vertices[triangle[1]], (vertices[triangle[0]] + vertices[triangle[2]]) / 2)
        normals.extend([normal] * 3)

        vertex_data = [vertices[i] for triangle in triangles for i in triangle]
        vertex_data.extend([-vertices[i] for triangle in triangles for i in triangle[::-1]])

        normals.extend([-normal for normal in normals])

        vertex_data = np.hstack([vertex_data, normals])
        vertex_data = np.array(vertex_data, dtype='f4')
        return vertex_data, vbo_format, vbo_attrs

    def _get_normal(self, point_1: np.array, point_2: np.array):
        normal = np.array([point_1[0] + point_2[0], point_1[1] + point_2[1], point_1[2] + point_2[2]]) / 2
        return normal


class Cube(BaseModel):
    def __init__(self, engine, shader_name: str = 'default', pos: tuple = (0, 0, 0), color: tuple = (0.9, 0.9, 0.9), scale: int = 1, quality: int = 8):
        self.quality = quality
        super().__init__(engine, shader_name, pos, scale=(scale, scale, scale))
        self.color = glm.vec3(color)
        self.shader_program.update_input_variable('color', self.color)

    @staticmethod
    def get_data(vertices, triangles):
        data = [vertices[ind] for triangle in triangles for ind in triangle]
        return np.array(data, dtype='f4')

    def get_vbo_data(self):
        vbo_format = '3f 3f'
        vbo_attrs = ['in_position', 'in_normal']

        vertices = [(-1, -1, 1), ( 1, -1,  1), (1,  1,  1), (-1, 1,  1),
                    (-1, 1, -1), (-1, -1, -1), (1, -1, -1), ( 1, 1, -1)]

        triangles = [(0, 2, 3), (0, 1, 2),
                   (1, 7, 2), (1, 6, 7),
                   (6, 5, 4), (4, 7, 6),
                   (3, 4, 5), (3, 5, 0),
                   (3, 7, 4), (3, 2, 7),
                   (0, 6, 1), (0, 5, 6)]
        vertex_data = self.get_data(vertices, triangles)

        normals = [( 0, 0, 1) * 6,
                   ( 1, 0, 0) * 6,
                   ( 0, 0,-1) * 6,
                   (-1, 0, 0) * 6,
                   ( 0, 1, 0) * 6,
                   ( 0,-1, 0) * 6,]

        normals = np.array(normals, dtype='f4').reshape(36, 3)

        vertex_data = np.hstack([vertex_data, normals])

        return vertex_data, vbo_format, vbo_attrs
