// libraries
# include <SPI.h>
# include <nRF24L01.h>
# include <RF24.h>

// def radio
RF24 radio(7, 8); //CE, CSN

// user config
bool radioNumber = 0;
bool role = 0;

// constants
const byte address[6] = "00001"

// define own data types
struct rpiTransmit{
	bool resultLEDstatus;
};

void setup() {
	Serial.begin(9600);
	Serial.println(F("*** PRESS 'T' to begin transmitting to arduino node"));
	radio.begin();
	radio.setPALevel(RF24_PA_LOW);

	if (radioNumber){
		radio.openWritingPipe(addresses[1]);
		radio.openReadingPipe(1, addresses[0]);
	}else{
		radio.openWritingPipe(addresses[0]);
		radio.openReadingPipe(1, addresses[1]);
	}

	radio.startListening();
}

void loop() {
	if (role == 0){
		if (radio.available()){
			while (radio.available()){
				radio.read(&transmit, sizeof(transmit));
			}
		}
		radio.stopListening();
		radio.write(&rpiTransmit, sizeof(rpiTransmit));
		radio.startListening();
		Serial.print(F("Sent response");
	}
}
