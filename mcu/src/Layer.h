#pragma once

#include "Light.h"

class Layer {
    public:
        Layer(int l_size, Light nodes[]);
        void WriteLayer(int brightness_vec[]);
        void WriteLayerDigital(int brightness_vec[]);
    private:
        Light node_vec[15];
        int layer_size;
};
