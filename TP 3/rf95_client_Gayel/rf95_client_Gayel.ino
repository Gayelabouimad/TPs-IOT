#include <SPI.h>
#include <RH_RF95.h>

// Singleton instance of the radio driver
RH_RF95 rf95;

float frequency = 868.3;

void setup()
{

  Serial.begin(115200);
  while (!Serial) ; // Wait for serial port to be available
//  Serial.println("initialization");
  if (!rf95.init())
    Serial.println("init failed");
  // Defaults after init are 434.0MHz, 13dBm, Bw = 125 kHz, Cr = 4/5, Sf = 128chips/symbol, CRC on

  rf95.setFrequency(frequency);
  // Setup Power,dBm
  rf95.setTxPower(13);

  // Setup Spreading Factor (6 ~ 12)
  rf95.setSpreadingFactor(9);

rf95.setSignalBandwidth(125000);
  
  // Setup Coding Rate:5(4/5),6(4/6),7(4/7),8(4/8) 
  rf95.setCodingRate4(5);

}

void loop()
{   
  
  int averageWait = 5000;
  
  for (int i = 0; i < 100; i++){
    String data = "IOT2019#"+String(i);
    uint8_t buf[12];
    data.toCharArray(buf, 12);
    rf95.send(buf, sizeof(buf));
    rf95.waitPacketSent();
    Serial.println(data);
    delay(averageWait);
  }
}
