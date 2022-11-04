#pragma once

class Light {
    public:
        void WriteBrightness(unsigned int new_brightness);
    private:
        unsigned int brightness;
        int position_id;
};
