void setup() {
Serial.begin(230400);
pinMode(3, OUTPUT);
}
void loop() {
  digitalWrite(3, HIGH);
   Serial.println(analogRead(A0));
  digitalWrite(3, LOW);
}
