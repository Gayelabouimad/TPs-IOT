#include <SPI.h>
#include <RH_RF95.h>

// Singleton instance of the radio driver
RH_RF95 rf95;

float frequency = 866.7;
int spreadingFactor = 7;

void setup()
{
  Serial.begin(115200);
  while (!Serial) ; // Wait for serial port to be available
  if (!rf95.init())
    Serial.println("init failed");

  rf95.setFrequency(frequency);
  // Setup Power,dBm
  rf95.setTxPower(13);

  rf95.setSpreadingFactor(spreadingFactor);
  
  // Setup BandWidth, option: 7800,10400,15600,20800,31250,41700,62500,125000,250000,500000
  //Lower BandWidth for longer distance.
  rf95.setSignalBandwidth(125000);
  
  // Setup Coding Rate:5(4/5),6(4/6),7(4/7),8(4/8) 
  rf95.setCodingRate4(5);
}

void loop()
{
  int myGroupID = 16;
  int averageWait = 5000;
  for (int i = 0; i < 100; i++){
    String data = "Sender#"+String(myGroupID)+".1"+":"+String(i)+":"+"Hello World";
    uint8_t tableau[30];
    data.toCharArray(tableau, 30);
    rf95.send(tableau, sizeof(tableau));
    rf95.waitPacketSent();
    Serial.print(data);
    delay(averageWait);
  }
}
