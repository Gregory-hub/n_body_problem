#version 330 core

layout (location = 0) in vec3 in_position;
layout (location = 1) in vec3 in_normal;

out vec3 normal;
out vec3 fragPos;

uniform mat4 proj_matrix;
uniform mat4 view_matrix;
uniform mat4 model_matrix;

void main() {
    fragPos = vec3(model_matrix * vec4(in_position, 1.0));
    normal = mat3(transpose(inverse(model_matrix))) * normalize(in_normal);
    gl_Position = proj_matrix * view_matrix * model_matrix * vec4(in_position, 1.0);
}
