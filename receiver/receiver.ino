/*
  RF_Sniffer
 
  Hacked from http://code.google.com/p/rc-switch/
 
  by @justy to provide a handy RF code sniffer
*/
 
#include <RCSwitch.h>
#include <stdlib.h>
#include <stdio.h>
RCSwitch mySwitch = RCSwitch();
 
void setup() {
  Serial.begin(9600);
  mySwitch.enableReceive(0);  // Receiver on inerrupt 0 =&gt; that is pin #2
  pinMode(7, OUTPUT);
  Serial.print("I'm working");
}
 
void loop() {
  if (mySwitch.available()) {
 
    int value = mySwitch.getReceivedValue();
 
    if (value == 0) {
      Serial.print("Unknown encoding");
    } else {
     Serial.print("Received ");
      Serial.print( mySwitch.getReceivedValue() );
      if(value == 2){
        digitalWrite(7, HIGH);
        Serial.print(" Switching ON");
      }else if(value == 1){
        digitalWrite(7, LOW);
        Serial.print(" Switching OFF");
      }
      Serial.print(" / ");
      Serial.print( mySwitch.getReceivedBitlength() );
      Serial.print("bit ");
      Serial.print("Protocol: ");
      Serial.println( mySwitch.getReceivedProtocol() );
    }
 
    mySwitch.resetAvailable();
 
  }
}
