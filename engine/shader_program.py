class ShaderProgram:
    def __init__(self, ctx, shader_name='default'):
        self.ctx = ctx
        self.program = self.get_program(shader_name)

    def get_program(self, shader_program_name):
        with open(f'engine/shaders/{shader_program_name}.vert') as file:
            vertex_shader = file.read()

        with open(f'engine/shaders/{shader_program_name}.frag') as file:
            fragment_shader = file.read()

        program = self.ctx.program(vertex_shader=vertex_shader, fragment_shader=fragment_shader)
        return program

    def update_input_variable(self, name: str, value):
        self.program[name].write(value)

    def destroy(self):
        self.program.release()
