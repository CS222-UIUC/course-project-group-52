#include <Arduino.h>
#include "Layer.h"
#include "Light.h"

int led1 = 3;
int led2 = 6;
int led3 = 9;
int led4 = 10;

const int in_layer_size = 1;
const int hidden_layer_size = 2;
const int out_layer_size = 1;

Light led_1(led1);
Light led_2(led2);
Light led_3(led3);
Light led_4(led4);

Light in_led_layer[1] = {led_1};
Light hidden_led_layer[2] = {led_2, led_3};
Light out_led_layer[1] = {led_4};

Layer in(in_layer_size, in_led_layer);
Layer hidden(hidden_layer_size, hidden_led_layer);
Layer out(out_layer_size, out_led_layer);

int in_vec[in_layer_size];
int hidden_vec[hidden_layer_size];
int out_vec[out_layer_size];


   
void setup() {
    Serial.begin(9600);
    // pinMode(led1, OUTPUT);
    // pinMode(led2, OUTPUT);
    // pinMode(led3, OUTPUT);
    // pinMode(led4, OUTPUT);
    
    // digitalWrite(led1, LOW);
    // digitalWrite(led2, LOW);
    // digitalWrite(led3, LOW);
    // digitalWrite(led4, LOW);
    in_vec[0] = 40;
    hidden_vec[0] = 64;
    hidden_vec[1] = 64;
    out_vec[0] = 20;
}

void loop() {
    // digitalWrite(led1, HIGH);
    // delay(400);
    // digitalWrite(led2, HIGH);
    // digitalWrite(led3, HIGH);
    // delay(400);
    // digitalWrite(led4, HIGH);
    // delay(400);
    // digitalWrite(led1, LOW);
    // delay(400);
    // digitalWrite(led2, LOW);
    // digitalWrite(led3, LOW);
    // delay(400);
    // digitalWrite(led4, LOW);
    // delay(400);

    /* 
    ^
    |   No PWM, only brightens and dims LEDs
    |
    Comment lower section or upper section out.
    |
    |   PWM, brightens and dims LEDs based on a numerical range from 0-255
    V
    */
   in.WriteLayer(in_vec);
   delay(100);
   hidden.WriteLayer(hidden_vec);
   delay(100);
   out.WriteLayer(out_vec);
   delay(100);

   /* Purely for testing Purposes */
   for (int& i: in_vec) {;
    i += 100;
    if (i > 255) {
        i = 0;
    }
   }
   for (int& i : hidden_vec) {
    i += 50;
    if (i > 255) {
        i = 0;
    }
   }
   for (int& i : out_vec) {
    i += 20;
    if (i > 255) {
        i = 0;
    }
   }
    // analogWrite(led1, 10);
    // delay(400);
    // analogWrite(led2, 15);
    // analogWrite(led3, 64);
    // delay(400);
    // analogWrite(led4, 20);
    // delay(400);
    // analogWrite(led1, 0);
    // delay(400);
    // analogWrite(led2, 0);
    // analogWrite(led3, 0);
    // delay(400);
    // analogWrite(led4, 0);
    // delay(400);
}
