#include "ESPControl.h"

const int pushbuttons[] = { D0, D1, D2, D3};
const int leds[] = {D4, D5, D6, D7};

const String myids[] = {"LED 1 ID", "LED 2 ID", "LED 3 ID", "LED 4 ID"};

const char * ssid = "wifi-ssid";
const char * pass = "wifi-password";

const String rcv_format = "SOS/";
const String snd_format = "C/";

int numIds = 0;

String msg = "";
bool hasMsg = false;

String locations[4];
String ids[4];

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

  numIds = (sizeof(ids) / sizeof(ids[0]));
  for (int i = 0; i < 4; i++)
  {
    pinMode(pushbuttons[i], INPUT);
    pinMode(leds[i], OUTPUT);
  }

  start(ssid, pass);
}

void loop() {
  // put your main code here, to run repeatedly:

  if (CheckNewReq() == 1)
  {
    // Check if there is sos to receive
    String path = getPath();
    path.remove(0, 1); // removes slash
    
    // Checks if there is msg to send
    if (hasMsg == true)
    {
      String data = snd_format + msg;
      Serial.print("Sending ");
      Serial.println(data);
      returnThisStr(data);

      // Reset
      msg = "";
      hasMsg = false;
      return;
    }
    else
    {
      returnThisStr("None");
    }

    // after removing slash we left with SOS/LOCATION/ID
    if (path.length() > 0 && hasMsg == false)
    {
      String loc = path.substring(4, path.lastIndexOf('/'));
      String id = path.substring(path.lastIndexOf('/') + 1);

      for (int i = 0; i < numIds; i++)
      {
        if (id.equalsIgnoreCase(myids[i]))
        {
          // Stores in an array
          locations[i] = loc;
          ids[i] = id;
          
          // lights up corresponding led
          digitalWrite(leds[i], HIGH);
        }
      }
    }

    // for sending back to python
    int bits[4];
    for (int i = 0; i < numIds; i++)
    {
      bits[i] = digitalRead(pushbuttons[i]);
      if (bits[i] == 1)
      {
        // Turns off led
        digitalWrite(leds[i], LOW);
        msg = locations[i] + '/' + ids[i];

        hasMsg = true;

        // Reset
        locations[i] = "";
        ids[i] = "";
        
        Serial.print("Has message: ");
        Serial.println(msg);
        break;
      }
    }
  }
}
