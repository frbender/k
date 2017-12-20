#include <Adafruit_NeoPixel.h>
#ifdef __AVR__
#include <avr/power.h>
#endif


//Led strip
#define strip_pin 6
#define ledAmount 60
Adafruit_NeoPixel strip = Adafruit_NeoPixel(ledAmount, strip_pin, NEO_GRB + NEO_KHZ800);


//Stuff for Serial communication

//Number of bytes ariving over serial in one package.
//This is for one LED each.
#define INPUT_BUFFER_SIZE 8

//Input ring buffer
int input[INPUT_BUFFER_SIZE] = {0}; //Serial input will be buffered here



#define bautrate 115200



void setup() {

  Serial.begin(bautrate);
  // Serial.setTimeout(10);


  pinMode(13, OUTPUT);


  strip.begin();
  strip.show(); // Initialize all pixels to 'off'


//  pushBuffer(255);  useBuffer();
//  pushBuffer(255);  useBuffer();
//  pushBuffer(255);  useBuffer();
//  pushBuffer(255);  useBuffer();
//  pushBuffer(0);  useBuffer();
//  pushBuffer(255);  useBuffer();
//  pushBuffer(0);  useBuffer();
//  pushBuffer(255);  useBuffer();
//
//  
//
//  pushBuffer(255);  useBuffer();
//  pushBuffer(255);  useBuffer();
//  pushBuffer(255);  useBuffer();
//  pushBuffer(255);  useBuffer();
//  pushBuffer(254);  useBuffer();
//  pushBuffer(0);  useBuffer();
//  pushBuffer(0);  useBuffer();
//  pushBuffer(0);  useBuffer();


}


void pushBuffer(int b) {
  //Advance conveor band
  for (int i = INPUT_BUFFER_SIZE - 1; i > 0; i--) {
    input[i] = input[i - 1];
  }

  //Write new byte
  input[0] = b;
}


void useBuffer() {
//  Serial.println("Use Buffer...");
//  Serial.println(String(input[7]) + " " + String(input[6]) + " " + String(input[5]) + " " + String(input[4]) + " " + String(input[3]) + " " + String(input[2]) + " " + String(input[1]) + " " + String(input[0]) + " ");
//


  //Validate Input:
  //FF FF FF FF N R G B

  if(input[7] != 0xFF ||
     input[6] != 0xFF ||
     input[5] != 0xFF ||
     input[4] != 0xFF) {
    return; //Not beginning of message
  }

  if(input[3] == 0xFF) {
    return; //Body must not look like beginning of message
  }


  // Serial.println("Got valid input:");

  //Input seems valid. Decide what to do...
  //N = 0...199 :      SET PIXEL
  //N = 200     :      SET ALL
  //N = 201     :      BLACK OUT
  //N = 254     :      UPDATE STRIP

  if (input[3] < 200) {
    set_pixel(input[3], input[2], input[1], input[0]);
    // Serial.println("SET LED");
  }
  else if (input[3] == 200) {
    set_all_pixels(input[2], input[1], input[0]);
    // Serial.println("SET ALL");
  }
  else if (input[3] == 201) {
    set_all_pixels(0, 0, 0);
    // Serial.println("BLACKOUT");
  }
  else if (input[3] == 254) {
    // Serial.println("UPDATE");
    strip.show(); 
  }

}



void set_pixel(int n, int r, int g, int b) {
  strip.setPixelColor(n, r, g, b);
}


void set_all_pixels(int r, int g, int b) {
  for (int i = 0; i < ledAmount; i++) {
    strip.setPixelColor(i, r, g, b);
  }
}

void loop() {
  int inp = Serial.read();
  if (inp > -1) {
    pushBuffer(inp);
    useBuffer();
  }
}


