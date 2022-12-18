#version 330 core

struct Light {
    vec3 pos;
    vec3 ambient_intensity;
    vec3 diffuse_intensity;
    vec3 specular_intensity;
};

layout (location = 0) out vec4 fragColor;

in vec3 normal;
in vec3 fragPos;
uniform vec3 color;
uniform Light light;
uniform bool ignore_light = false;
uniform vec3 camPos;


vec3 getLight(vec3 color) {
    vec3 normal = normalize(normal);

    // ambient light
    vec3 ambient = light.ambient_intensity;

    // diffuse light
    vec3 light_direction = normalize(light.pos - fragPos);
    float diff = max(0, dot(light_direction, normal));
    vec3 diffuse = diff * light.diffuse_intensity;

    // specular light
    vec3 view_direction = normalize(camPos - fragPos);
    vec3 reflection_direction = reflect(-light_direction, normal);
    vec3 specular = pow(max(dot(view_direction, reflection_direction), 0), 32) * light.specular_intensity;

    return color * (ambient + diffuse + specular);
}


void main() {
    if (ignore_light) {
        fragColor = vec4(color, 1.0);
    } else {
        fragColor = vec4(getLight(color), 1.0);
    }
}
