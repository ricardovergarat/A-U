#define data 2
#define clock 3
byte num = B01111110;
void setup() {
  pinMode(clock, OUTPUT);
  pinMode(data, INPUT);
}

void loop() {
  shiftOut(data, clock, LSBFIRST, num);
  delay(500);
}
