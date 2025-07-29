#include <Arduino.h>

// Kanały i piny GPIO dla CH1–CH6
const int pwmPins[6] = {13, 12, 14, 27, 26, 25};
int pwmChannels[6] = {0, 1, 2, 3, 4, 5};

void setup() {
  Serial.begin(115200);

  // Konfiguracja PWM (50 Hz, 12-bit)
  for (int i = 0; i < 6; i++) {
    ledcSetup(pwmChannels[i], 50, 12);        // Częstotliwość 50 Hz, rozdzielczość 12-bit
    ledcAttachPin(pwmPins[i], pwmChannels[i]);
    ledcWrite(pwmChannels[i], 0);             // Start z zerowym wypełnieniem
  }
}

void loop() {
  if (Serial.available()) {
    String line = Serial.readStringUntil('\n');
    line.trim();  // Usuń zbędne spacje, znaki CR itp.

    int values[6] = {0};
    int i = 0;
    char* token = strtok((char*)line.c_str(), ",");

    while (token != nullptr && i < 6) {
      values[i++] = atoi(token);
      token = strtok(nullptr, ",");
    }

    if (i == 6) {
      for (int j = 0; j < 6; j++) {
        int us = map(values[j], -100, 100, 1000, 2000);      // mapowanie do µs
        int duty = map(us, 0, 20000, 0, 4095);                // okres 20ms przy 50Hz
        ledcWrite(pwmChannels[j], duty);
      }
    }
  }
}
