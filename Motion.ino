//Defining pins

int buzz = 9;
int pir = 2;

void setup()
{

  // Sets the buzzer as an OUTPUT & PIR sensor as an INPUT
  pinMode(buzz, OUTPUT);
  pinMode(pir, INPUT);
  
  
// Serial Communication is starting with 9600 of baudrate speed
  Serial.begin(9600);
}

void loop()
{
  //Read data from the sensor
  int status = digitalRead(pir);
  
  
// check data from sensor if there is motion,
// if will execute otherwise else will execute
  if(status == HIGH)
  {
    Serial.println("Motion Detected");
    tone(buzz,1000,700);
    delay(2000);
  }
  else
  {
    Serial.println("No one is there");
    delay(1000);
  }
 
}
