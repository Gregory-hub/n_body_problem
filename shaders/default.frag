#version 330 core

uniform vec3 color;

layout (location = 0) out vec4 fragColor;

in vec3 normal;
in vec3 fragPos;

struct Light {
    vec3 pos;
    vec3 ambient_intensity;
    vec3 diffuse_intensity;
    vec3 specular_intensity;
};

uniform Light light;
uniform bool ignore_light = false;

vec3 getLight(vec3 color) {
    // ambient light
    vec3 ambient = light.ambient_intensity;

    // diffuse light
    vec3 normal = normalize(normal);
    vec3 light_direction = normalize(light.pos - fragPos);
    float diff = max(0, dot(light_direction, normal));
    vec3 diffuse = diff * light.diffuse_intensity;

    return color * (ambient + diffuse);
}

void main() {
    if (ignore_light) {
        fragColor = vec4(color, 1.0);
    } else {
        fragColor = vec4(getLight(color), 1.0);
    }
}
