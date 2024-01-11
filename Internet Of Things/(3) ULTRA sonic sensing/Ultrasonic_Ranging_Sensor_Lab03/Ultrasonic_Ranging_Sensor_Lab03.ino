int Greene = 10;
int Reed = 11;
int Yell = 12;
int echo = 2;
int trigger = 4;

long TimePulse(int trigger, int echo)
{
  digitalWrite(trigger, LOW);
  delayMicroseconds(2);

  digitalWrite(trigger, HIGH);
  delayMicroseconds(10);

  digitalWrite(trigger, LOW);
  return pulseIn(echo, HIGH);
}

void setup() 
{
  Serial.begin(9600);
  pinMode(Greene, OUTPUT);
  pinMode(Reed, OUTPUT);
  pinMode(Yell, OUTPUT);
  pinMode(trigger, OUTPUT);
  pinMode(echo, INPUT);
}

void loop()
{
  int distance = 0.01715 * TimePulse(trigger, echo);

  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.print(" cm.");

  if(distance>50)
  {
    Green();
  }
  else if(distance < 50 && distance > 25)
  {
    Yellow();
  }
  else if(distance < 25)
  {
    Red();
  }

}

void Green()
{
  digitalWrite(Greene, HIGH);
  digitalWrite(Reed, LOW);
  digitalWrite(Yell, LOW);
  delay(100);
}

void Red()
{
  digitalWrite(Greene, LOW);
  digitalWrite(Reed, HIGH);
  digitalWrite(Yell, LOW);
  delay(100);
}

void Yellow()
{
  digitalWrite(Greene, LOW);
  digitalWrite(Reed, LOW);
  digitalWrite(Yell, HIGH);
  delay(100);
}

