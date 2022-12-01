#include <Arduino.h>
#include "Layer.h"
#include "Light.h"

int led1 = 3;
int led2 = 6;
int led3 = 9;
int led4 = 10;

void setup() {
    pinMode(led1, OUTPUT);
    pinMode(led2, OUTPUT);
    pinMode(led3, OUTPUT);
    pinMode(led4, OUTPUT);
    
    digitalWrite(led1, LOW);
    digitalWrite(led2, LOW);
    digitalWrite(led3, LOW);
    digitalWrite(led4, LOW);
}

void loop() {
    digitalWrite(led1, HIGH);
    delay(400);
    digitalWrite(led2, HIGH);
    digitalWrite(led3, HIGH);
    delay(400);
    digitalWrite(led4, HIGH);
    delay(400);
    digitalWrite(led1, LOW);
    delay(400);
    digitalWrite(led2, LOW);
    digitalWrite(led3, LOW);
    delay(400);
    digitalWrite(led4, LOW);
    delay(400);

    /* 
    ^
    |   No PWM, only brightens and dims LEDs
    |
    Comment lower section or upper section out.
    |
    |   PWM, brightens and dims LEDs based on a numerical range from 0-255
    V
    */
    analogWrite(led1, 255);
    delay(400);
    analogWrite(led2, 255);
    analogWrite(led3, 255);
    delay(400);
    analogWrite(led4, 255);
    delay(400);
    analogWrite(led1, 0);
    delay(400);
    analogWrite(led2, 0);
    analogWrite(led3, 0);
    delay(400);
    analogWrite(led4, 0);
    delay(400);
}
