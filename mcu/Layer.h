#pragma once

#include <vector>
#include "Light.h"

class Layer {
    public:
        void WriteLayer(std::vector<int> brightness_vec);
    private:
        std::vector<Light> node_vec;
};
