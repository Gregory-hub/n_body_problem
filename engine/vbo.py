class VBO:
    def __init__(self, ctx, vertex_data: list, vbo_format: str, attrs: list):
        self.ctx = ctx
        self.vertex_data = vertex_data
        self.vbo = self.ctx.buffer(self.vertex_data)
        self.format = vbo_format
        self.attrs = attrs

    def destroy(self):
        self.vbo.release()
