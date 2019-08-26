int determinar_estado(int n){
  if (digitalRead(n) == LOW){
    return 0;
  }
  return 1;
}

void setup() {
  pinMode(7,INPUT); // a
  pinMode(8,INPUT); // b
  pinMode(9,INPUT); // c
  pinMode(10,INPUT); // d
  pinMode(4,OUTPUT); // S o salida
}

void loop() {
  // 0 = low
  // 1 = high
  int a,b,c,d,total;
  a = determinar_estado(7);
  b = determinar_estado(8);
  c = determinar_estado(9);
  d = determinar_estado(10);
  if (d == 1 && (a == 0 && b == 0 && c == 0)){
    digitalWrite(4,HIGH); // caso de seguridad
  }else{
    total = a + b + c + d;
    if (total < 2){
      digitalWrite(4,LOW); // si una o ninguna esta activa: no enciende
    }else{
      if (total == 2){
        digitalWrite(4,HIGH); // caso de exactamente 2
      }else{
        digitalWrite(4,HIGH); // 3 o 4 enciende
      }
    }
  }
}
