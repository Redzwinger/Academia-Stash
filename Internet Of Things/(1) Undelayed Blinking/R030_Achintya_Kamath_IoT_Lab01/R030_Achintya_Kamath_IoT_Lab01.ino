const int ledPin = LED_BUILTIN;  // the number of the LED pin

void setup() {
  // set the digital pin as output:
  pinMode(ledPin, OUTPUT);
}

void loop() 
{
  int i = 0;

  while (i < 11)
  {
    i++;
    if (i !=10) 
    {
      digitalWrite(ledPin, HIGH);
      delay(700);
      digitalWrite(ledPin, LOW);
      delay(300);
    }
    else
    {
      while(1);
      {
        // Infinite Loop :)
      }
    }
  }
}


