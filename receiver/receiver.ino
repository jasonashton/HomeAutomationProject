/*Incoming signal will eventually be read as ### ## #, where the first three numbers identify the device, next two the appliance, and the last one the state.
Here we only use the last three. 1 means off, 2 means on, because 0 is interpreted as an error (###)
01# is Channel 1
02# is Channel 2
*/
#include <RCSwitch.h>
#include <stdlib.h>
#include <stdio.h>
RCSwitch mySwitch = RCSwitch();
 
void setup() {
  Serial.begin(9600);
  mySwitch.enableReceive(0);  // Receiver on interrupt 0 =&gt; that is pin #2
  pinMode(7, OUTPUT); // Channel 1 of Relay
  pinMode(6, OUTPUT); // Channel 2 of Relay
}
 
void loop() {
  if (mySwitch.available()) {
 
    int value = mySwitch.getReceivedValue();
    
    switch (value) {
      case 0: //Error
        Serial.print("Unknown encoding");
        break;
      case 11: //Channel 1 off
        digitalWrite(7, LOW);
        break;
      case 12: //Channel 1 on
        digitalWrite(7, HIGH);
        break;
      case 21: //Channel 2 off
        digitalWrite(6, LOW);
        break;
      case 22: //Channel 2 on
        digitalWrite(6, HIGH);
        break;
      default: //Something else? Do nothing.
        break;
    }
    mySwitch.resetAvailable();
  }
}
