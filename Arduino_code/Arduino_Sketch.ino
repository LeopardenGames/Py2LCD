#include <LiquidCrystal.h>
LiquidCrystal lcd(8, 9, 4, 5, 6, 7);
String inputText = "";
void setup() {
    lcd.begin(16, 2);
    Serial.begin(9600);
    lcd.clear();
    delay(300);
    lcd.print("Py2LCD   V1.0");
    lcd.setCursor(0, 1);
    lcd.blink();
    lcd.print("by LivedLeopard");
    delay(6000);
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.noBlink();
    lcd.print("Wait for Input..");
}
void loop() {
    if (Serial.available()) {
        char incomingChar = Serial.read();
        if (incomingChar == '\n') { 
            processCommand(inputText);
            inputText = "";
        } else {
            inputText += incomingChar;
        }
    }
}
void processCommand(String command) {
    if (command.startsWith("text:")) {
        String text = command.substring(5);
        displayText(text);
    } else if (command.startsWith("scroll:")) {
        String text = command.substring(7);
        scrollText(text);
    } else {
        lcd.clear();
        lcd.print("Invalid cmd");
    }
}
void displayText(String text) {
    lcd.clear();
    lcd.print(text);
}
void scrollText(String text) {
    lcd.clear();
    for (int i = 0; i <= text.length(); i++) {
        lcd.clear();
        lcd.setCursor(16 - i, 0);
        lcd.print(text.substring(0, i));
        delay(300);
    }
}

