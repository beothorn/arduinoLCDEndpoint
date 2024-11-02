#include <LiquidCrystal.h>

#include <LiquidCrystal.h>
const int RS = 8;
const int EN = 9;
const int d4 = 4;
const int d5 = 5;
const int d6 = 6;
const int d7 = 7;
const int pin_BL = 10; // arduino pin wired to LCD backlight circuit
LiquidCrystal lcd( RS,  EN,  d4,  d5,  d6,  d7);

void setup() {
  // Set up the LCD's number of columns and rows:
  lcd.begin(16, 2);
  
  // Start serial communication at 9600 bps:
  Serial.begin(9600);
}

void loop() {
  // Check if data is available on serial port
  if (Serial.available() > 0) {
    // Read incoming string from serial
    String message = Serial.readString();
    
    // Clear the LCD screen
    lcd.clear();
    
    // Set cursor to the first row and first column
    lcd.setCursor(0, 0);
    
    // Print the message on the LCD
    lcd.print(message);
  }
}
