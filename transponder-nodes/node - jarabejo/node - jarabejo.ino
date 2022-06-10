#include "ESP_MICRO.h"
int pushButton = D5;
int output = 0;

int ledPin[2] = {D0,D1};
int i=0;
int value;

void setup() {
  Serial.begin(9600);
  start ("SSX Tricky","TechDeck");
  pinMode(pushButton, INPUT_PULLUP);
  for (i=0; i<2; i++){
        pinMode(ledPin[i], OUTPUT);
  } 
}

void loop() {
  waitUntilNewReq();
  int buttonState = digitalRead(pushButton);
  Serial.println(buttonState);
  if(buttonState == HIGH){
    output = 1;
  }
  if(buttonState == LOW){
    output = 0;
  }
  for (i=0; i<2; i++){
    if(buttonState == HIGH){
        digitalWrite(ledPin[i], HIGH);
        delay(100);
        digitalWrite(ledPin[i], LOW);
        delay(100);
    }
  }
  returnThisInt(output);
}
