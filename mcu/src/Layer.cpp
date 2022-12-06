#include "Layer.h"

Layer::Layer(int l_size, Light nodes[]) {
    layer_size = l_size;
    for (int i = 0; i < layer_size; i++) {
        node_vec[i] = nodes[i];
    }
}

void Layer::WriteLayer(int brightness_vec[]) {
    for (int i = 0; i < layer_size; i++) {
        node_vec[i].WriteBrightness(brightness_vec[i]);
    }
}

void Layer::WriteLayerDigital(int brightness_vec[]) {
    for (int i = 0; i < layer_size; i++) {
        node_vec[i].WriteBrightnessDigital(brightness_vec[i]);
    }
}

int MapFromRange(float value, int old_min, int old_max, int new_min, int new_max) {
    if (value <= old_min) {
        return 0;
    }
    float mapped = (value - (float)old_min) * (float)((new_max-new_min)/(old_max-old_min)) + (float)new_min;
    int cast = (int)mapped;
    return cast;
}