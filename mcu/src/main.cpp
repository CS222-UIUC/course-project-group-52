#include <Arduino.h>
#include "Layer.h"
#include "Light.h"

int led1 = 6;
int led2 = 3;
int led3 = 5;

void setup() {
    pinMode(led1, OUTPUT);
    pinMode(led2, OUTPUT);
    pinMode(led3, OUTPUT);
    
    digitalWrite(led1, LOW);
    digitalWrite(led2, LOW);
    digitalWrite(led3, LOW);
}

void loop() {
    digitalWrite(led1, HIGH);
    delay(400);
    digitalWrite(led2, HIGH);
    delay(400);
    digitalWrite(led3, HIGH);
    delay(400);
    digitalWrite(led1, LOW);
    delay(400);
    digitalWrite(led2, LOW);
    delay(400);
    digitalWrite(led3, LOW);
    delay(400);
}
