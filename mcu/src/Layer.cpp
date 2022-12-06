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
        node_vec[i].WriteBrightness(brightness_vec[i]);
    }
}