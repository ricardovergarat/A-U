void setup() {
  pinMode(8,INPUT); // izquierda
  pinMode(9,INPUT); // L
  pinMode(10,INPUT); // derecha
  pinMode(4,OUTPUT); // S o salida
}

void loop() {
  // 0 = low
  // 1 = high
  if ((digitalRead(8)== LOW && digitalRead(10)== LOW) || (digitalRead(8)== HIGH && digitalRead(10)== HIGH)){
    if (digitalRead(9) == HIGH){
      digitalWrite(4,HIGH);  
    }else{
      digitalWrite(4,LOW);
    }
  }else{
    if (digitalRead(10)== HIGH){
      digitalWrite(4,HIGH);
    }else{
      digitalWrite(4,LOW);
    }
  }
}
