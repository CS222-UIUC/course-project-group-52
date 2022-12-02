#include "Light.h"

Light::Light(int p_id) {
    position_id = p_id;
    pinMode(position_id, OUTPUT);
    brightness = 0;
}

void Light::WriteBrightness(unsigned int new_brightness) {
    brightness = new_brightness;
    analogWrite(position_id, brightness);
}