from vbo import VBO
from shader_program import ShaderProgram


class VAO:
    def __init__(self, ctx, vbo: VBO, shader_program: ShaderProgram):
        self.ctx = ctx
        self.vbo = vbo
        self.program = shader_program
        self.vao = self.ctx.vertex_array(self.program.program, [(vbo.vbo, vbo.format, *vbo.attrs)])

    def render(self):
        self.vao.render()

    def destroy(self):
        self.vbo.destroy()
        self.program.destroy()
        self.vao.release()
