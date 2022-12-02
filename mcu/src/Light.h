#pragma once
#include <Arduino.h>
class Light {
    public:
        Light() = default;
        Light(int p_id);
        void WriteBrightness(unsigned int new_brightness);
    private:
        unsigned int brightness;
        int position_id;
};
