#include <Arduino.h>
#include <SD.h>
#include "Layer.h"
#include "Light.h"

// 10 Regular Pins
int i_pin1 = 26;
int i_pin2 = 27;
int i_pin3 = 30;
int i_pin4 = 31;
int i_pin5 = 32;
int i_pin6 = 34;
int i_pin7 = 35;
int i_pin8 = 38;
int i_pin9 = 39;
int i_pin10 = 40;

// 25 PWM Pins
int h_pin1 = 0;
int h_pin2 = 1;
int h_pin3 = 2;
int h_pin4 = 3;
int h_pin5 = 4;
int h_pin6 = 5;
int h_pin7 = 6;
int h_pin8 = 7;
int h_pin9 = 8;
int h_pin10 = 9;

int o_pin1 = 15;
int o_pin2 = 18;
int o_pin3 = 19;
int o_pin4 = 22;
int o_pin5 = 23;
int o_pin6 = 24;
int o_pin7 = 25;
int o_pin8 = 28;
int o_pin9 = 29;
int o_pin10 = 33;

const int in_layer_size = 10;
const int hidden_layer_size = 10;
const int out_layer_size = 10;

Light i_led1(i_pin1);
Light i_led2(i_pin2);
Light i_led3(i_pin3);
Light i_led4(i_pin4);
Light i_led5(i_pin5);
Light i_led6(i_pin6);
Light i_led7(i_pin7);
Light i_led8(i_pin8);
Light i_led9(i_pin9);
Light i_led10(i_pin10);

Light h_led1(h_pin1);
Light h_led2(h_pin2);
Light h_led3(h_pin3);
Light h_led4(h_pin4);
Light h_led5(h_pin5);
Light h_led6(h_pin6);
Light h_led7(h_pin7);
Light h_led8(h_pin8);
Light h_led9(h_pin9);
Light h_led10(h_pin10);

Light o_led1(o_led1);
Light o_led2(o_led2);
Light o_led3(o_led3);
Light o_led4(o_led4);
Light o_led5(o_led5);
Light o_led6(o_led6);
Light o_led7(o_led7);
Light o_led8(o_led8);
Light o_led9(o_led9);
Light o_led10(o_led10);

Light in_led_layer[10] = {i_led1, i_led2, i_led3, i_led4, i_led5, i_led6, i_led7, i_led8, i_led9, i_led10};
Light hidden_led_layer[10] = {h_led1, h_led2, h_led3, h_led4, h_led5, h_led6, h_led7, h_led8, h_led9, h_led10};
Light out_led_layer[10] = {o_led1, o_led2, o_led3, o_led4, o_led5, o_led6, o_led7, o_led8, o_led9, o_led10};

Layer in(in_layer_size, in_led_layer);
Layer hidden(hidden_layer_size, hidden_led_layer);
Layer out(out_layer_size, out_led_layer);

int in_vec[in_layer_size];
int hidden_vec[hidden_layer_size];
int out_vec[out_layer_size];


   
void setup() {
    Serial.begin(9600);
    if (!SD.begin(BUILTIN_SDCARD)) {
        Serial.println("Card failed, or not present");
        // don't do anything more:
        while (1);
        return;
    }
    Serial.println("card initialized.");
    
   File dataFile = SD.open("network.csv", FILE_READ);
   String file_line = "";
   int line_num = 1;
   while (dataFile.available()) {
    file_line = dataFile.readStringUntil('\n', 2000000);
    if (line_num % 5 != 1 && line_num % 5 != 2 && line_num % 5 != 3) {
        delay(50);
        in.WriteLayerDigital(in_vec);
        hidden.WriteLayer(out_vec);
        out.WriteLayer(out_vec);
        line_num++;
        continue;
    }
    Serial.println(line_num);
    String temp = "";
    int pos = 0;
    for (auto x : file_line) {
        if (x != ',') {
            temp += x;
        } else {
            if (line_num % 5 == 1) {
                in_vec[pos] = MapFromRange(temp.toFloat(), -1, 1, 0, 255);
            } else if (line_num % 5 == 2) {
                hidden_vec[pos] = MapFromRange(temp.toFloat(), -2, 5, 0, 255);
            } else if (line_num % 5 == 3) {
                out_vec[pos] = MapFromRange(temp.toFloat(), 0, 1, 0, 255);
            }
            pos++;
            temp = "";
        }
    }
    
    if (line_num % 5 == 1) {
        in_vec[pos] = MapFromRange(temp.toFloat(), -1, 1, 0, 255);
    } else if (line_num % 5 == 2) {
        hidden_vec[pos] = MapFromRange(temp.toFloat(), -2, 5, 0, 255);
    } else if (line_num % 5 == 3) {
        out_vec[pos] = MapFromRange(temp.toFloat(), 0, 1, 0, 255);
        Serial.println(temp.toFloat());
    }
    pos++;
    temp = "";
    line_num++;
   }
}

void loop() {
    /* 
    ^
    |   No PWM, only brightens and dims LEDs
    |
    Comment lower section or upper section out.
    |
    |   PWM, brightens and dims LEDs based on a numerical range from 0-255
    V
    */

}
