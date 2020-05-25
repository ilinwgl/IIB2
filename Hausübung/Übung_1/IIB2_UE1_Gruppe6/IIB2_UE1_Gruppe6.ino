#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <ArduinoJson.h>  //version 5.1.0
#include <WiFiUdp.h>
#include <NTPClient.h>

#include "DHT.h"
#define DHT11_PIN 13
#define DHTTYPE DHT11
DHT dht(DHT11_PIN, DHTTYPE);

const long utcOffsetInSeconds = 3600;
// A UDP instance to let us send and receive packets over UDP
WiFiUDP ntpUDP;
NTPClient timeClient(ntpUDP, "pool.ntp.org", utcOffsetInSeconds); //wifi nötig

void setup()
{
  // put your setup code here, to run once:
  Serial.begin(9600);
  WiFi.begin("gruppe6", "12345678");
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(1000);
    Serial.println("Connecting..");
  }
  // timeClient.begin();
  Serial.println("Connected to WiFi Network");
}

void loop() {
  while(!timeClient.update()) 
    {timeClient.forceUpdate();}
  if (WiFi.status() == WL_CONNECTED) { //Check WiFi connection status
    float temp = dht.readTemperature();
    float hum = dht.readHumidity();
    Serial.print("Temperature = ");
    Serial.println(dht.readTemperature());
    Serial.print("Humidity = ");
    Serial.println(dht.readHumidity());
    if(!isnan(hum) && hum <= 100)
    {
        StaticJsonBuffer<300> JSONbuffer;   //Declaring static JSON buffer
        JsonObject& JSONencoder = JSONbuffer.createObject();
        JSONencoder["temp"] = temp ;
        JSONencoder["feuch"] = hum ;
        char JSONmessageBuffer[300];
        JSONencoder.prettyPrintTo(JSONmessageBuffer, sizeof(JSONmessageBuffer));
        Serial.println(JSONmessageBuffer);

        HTTPClient http;    //Declare object of class HTTPClient    
        http.begin("http://172.18.19.85:8090/postjson"); //Specify request destination
        http.addHeader("Content-Type", "application/json");  //Specify content-type header
        int httpCode = http.POST(JSONmessageBuffer);   //Send the request
        String payload = http.getString();                                        //Get the response payload
        Serial.println(httpCode);   //Print HTTP return code
        Serial.println(payload);    //Print request response payload
        http.end();  //Close connection
    }
  } else {
    Serial.println("Error in WiFi connection");
  }
  delay(10000);  //Send a request every 10 seconds
}
