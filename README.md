# Emergency Transponder System using NodeMCU Platform

**Description:**
Multiple remote emergency transponders powered by a NODEMCU device can transmit “SOS” messages over the the cloud towards a “base” that can then respond via command buttons.

**Group 5 Members:**
1. Baltazar, Rendell Jay
2. Capricho Jr., Arthur
3. Flores, Jayvee
4. Jarabejo, Joshua
5. Mayordo, Zherish Galvin

# How to use or build the "Emergency Transponder System using NodeMCU Platform":

**Base:**
1. Use the schematic provided to build the "base" circuit.
2. Connect the NodeMCU to your WiFi by changing both "wifi-ssid" and "wifi-password" with your WiFi's credentials.
3. Input ids in the myids[] array (e.g. student numbers). The indices will determine which LED will correspond to your member (e.g. myids[0] is the student number of member 1). 
4. Upload the code to your NodeMCU.
5. Power up the NodeMCU without connecting the 3V and GND to the circuit. This will allow time for the NodeMCU to connect to your WiFi.
6. Once connected to the WiFi, connect the 3V and GND to the circuit.
7. Get your NodeMCU's IP address and input it in the url of the python program.
8. Run the python program, and you're ready to send responses and receive SOS from your members.

**Nodes:**
1. Use the schematic provided to build the "node" circuit.
2. Connect the NodeMCU to your WiFi by inputting both SSID and password of your WiFi.
3. Power up the NodeMCU without connecting the 3V and GND to the circuit. This will allow time for the NodeMCU to connect to your WiFi.
4. Once connected to the WiFi, connect the 3V and GND to the circuit.
5. Get your NodeMCU's IP address and input it in the url of the python program.
6. Run the python program, and you're ready to send SOS and receive responses from the base.
