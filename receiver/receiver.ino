/*Incoming signal will eventually be read as ### ## #, where the first three numbers identify the device, next two the appliance, and the last one the state.
Here we only use the last three. 1 means off, 2 means on, because 0 is interpreted as an error (###)
01# is Channel 1
02# is Channel 2
*/
#include <RCSwitch.h>
#include <stdlib.h>
#include <stdio.h>
RCSwitch mySwitch = RCSwitch();
int ch1 = 7;
int ch2 = 6;
int switchPin = 4;
int prevState;
 
void setup() {
  Serial.begin(9600);
  mySwitch.enableReceive(0);  // Receiver on interrupt 0 =&gt; that is pin #2
  pinMode(ch1, OUTPUT); // Channel 1 of Relay
  pinMode(ch2, OUTPUT); // Channel 2 of Relay
  pinMode(13, OUTPUT);
  pinMode(switchPin, INPUT); //Input to check if switch is connected
  digitalWrite(switchPin, HIGH); //pullup resistor
  
  prevState = digitalRead(switchPin);
}
 
void loop() {
  override();
  
  if (mySwitch.available()) { //if message is available and the switch is disconnected (ON/HIGH)
 
    int value = mySwitch.getReceivedValue();
    
    switch (value) {
        case 0: //Error
          Serial.print("Unknown encoding");
          break;
        case 11: //Channel 1 off
          digitalWrite(ch1, LOW);
          break;
        case 12: //Channel 1 on
          digitalWrite(ch1, HIGH);
          break;
        case 21: //Channel 2 off
          digitalWrite(ch2, LOW);
          break;
        case 22: //Channel 2 on
          digitalWrite(ch2, HIGH);
          break;
        default: //Something else? Do nothing.
          break;
      }
    }
    mySwitch.resetAvailable();
}

void override() {
  //if the switch is flipped to on, turn all lights on. if flipped to off, turn all lights off
  
  int readState = digitalRead(switchPin); //off is HIGH, on is LOW. Reads the pin  
  if(prevState != readState){//if the read state is DIFFERENT then the last known statereadState
    Serial.print("Switching \n");
    if(readState == 0){
      digitalWrite(ch1, HIGH);
      digitalWrite(ch2, HIGH);
    }else if(readState == 1){
      digitalWrite(ch1, LOW);
      digitalWrite(ch2, LOW);
    }
    prevState = readState;
  }
}

