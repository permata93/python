void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT);
}

// the loop function runs over and over again forever
void loop()
{
  if(Serial.available()>0) {
    char command = digitalWrite(13, HIGH);
    if(command == '1') flashing = true;
    else if(command == '0') digitalWrite(13, LOW);
  }
