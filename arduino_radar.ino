#include <Servo.h>

#define TRIG_PIN 5
#define ECHO_PIN 6
#define SERVO_PIN 11

Servo radarServo;

void setup() {
  Serial.begin(9600);
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
  radarServo.attach(SERVO_PIN);
}

float readDistanceCM() {
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);

  long duration = pulseIn(ECHO_PIN, HIGH);
  float distance = duration * 0.034 / 2;
  return distance;
}

void loop() {
  for (int angle = 0; angle <= 120; angle++) {
    radarServo.write(angle);
    delay(100); // Allow servo to settle
    float distance = readDistanceCM();
    Serial.print("Angle: ");
    Serial.print(angle);
    Serial.print(", Distance: ");
    Serial.print(distance);
    Serial.println(" cm");
  }
  for (int angle = 120; angle >= 0; angle--) {
    radarServo.write(angle);
    delay(100);
    float distance = readDistanceCM();
    Serial.print("Angle: ");
    Serial.print(angle);
    Serial.print(", Distance: ");
    Serial.print(distance);
    Serial.println(" cm");
  }
}
