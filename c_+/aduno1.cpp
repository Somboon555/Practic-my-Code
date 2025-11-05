const int led_red = 10;
const int led_yellow = 9;
const int led_green = 8;
const int button = 2;
const int delay_time =100;

void setup() {
  pinMode(button, INPUT_PULLUP);
  pinMode(led_red, OUTPUT);
  pinMode(led_yellow, OUTPUT);
  pinMode(led_green, OUTPUT);

}

void loop() {
  if(digitalRead(button) == LOW){
  digitalWrite(led_red, LOW);
  digitalWrite(led_yellow, LOW); 
  digitalWrite(led_green, HIGH);
  delay(delay_time);
  digitalWrite(led_red, LOW);
  digitalWrite(led_yellow, HIGH);
  digitalWrite(led_green, LOW);
  delay(delay_time);
  digitalWrite(led_red, HIGH);
  digitalWrite(led_yellow, LOW);
  digitalWrite(led_green, LOW);
  delay(delay_time);
  }
}