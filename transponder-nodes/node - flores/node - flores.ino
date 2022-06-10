#include "ESP_MICRO.h"

int but = D3;
int rLed = D1;
int wLed = D2;

void setup() {
 pinMode(but, INPUT_PULLUP);
 pinMode(rLed,OUTPUT);
 pinMode(wLed,OUTPUT);
 
 Serial.begin(9600);
 start("TEAMYORDANFLORES","IRGXSRI@13");
 
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
