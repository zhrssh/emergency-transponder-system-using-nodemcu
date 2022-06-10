
#include "ESP_MICRO.h"

int but = D2;
int rLed = D0;
int wLed = D1;

void setup() {
 pinMode(but, INPUT_PULLUP);
 pinMode(rLed,OUTPUT);
 pinMode(wLed,OUTPUT);
 
 Serial.begin(9600);
 start("NOVA_AE40","pain6769");
 
}

void loop() {
  waitUntilNewReq();
  int butState = digitalRead(but);

  Serial.println(!butState);
  if(!butState == HIGH)
  {
    
    digitalWrite(rLed,HIGH);
    digitalWrite(wLed,LOW);
    delay(1000);
    digitalWrite(rLed,LOW);
    digitalWrite(wLed,HIGH);
    delay(1000);
    digitalWrite(rLed,HIGH);
    digitalWrite(wLed,LOW);
    delay(1000);
    digitalWrite(rLed,LOW);
    digitalWrite(wLed,HIGH);
    delay(1000);
    digitalWrite(rLed,HIGH);
    digitalWrite(wLed,LOW);
    delay(1000);
    digitalWrite(rLed,LOW);
    digitalWrite(wLed,HIGH);
    delay(1000);
    digitalWrite(rLed,LOW);
    digitalWrite(wLed,LOW);
  }
  else
  {
    digitalWrite(rLed,LOW);
    digitalWrite(wLed,LOW);
    delay(1000);
  }
  returnThisInt(!butState);
}
