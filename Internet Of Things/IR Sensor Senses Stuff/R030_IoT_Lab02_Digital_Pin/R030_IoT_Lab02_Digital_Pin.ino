
int sensorPin = A0;
int ledPin = 13; 
int sensorValue = 0;  

void setup() 
{
  Serial.begin(9600);
  pinMode(sensorPin, INPUT);
  pinMode(ledPin, OUTPUT);
}

void loop() 
{

  sensorValue = analogueRead(sensorPin);
  //digitalWrite(ledPin, HIGH);

  Serial.println(sensorValue);

  if (sensorValue == 1)
  {
    digitalWrite(ledPin, LOW);
  }
  else
  {
    digitalWrite(ledPin, HIGH);
  }

}

