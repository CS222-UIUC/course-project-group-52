#pragma once

#include "vector.h"
#include "Light.h"

class Layer {
    public:
        void WriteLayer(Vector<int> brightness_vec);
    private:
        Vector<Light> node_vec;
};
