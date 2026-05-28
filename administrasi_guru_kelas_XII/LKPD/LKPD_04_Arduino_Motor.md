# LKPD - Motor Servo, Motor DC, dan Driver L298N
**Mata Pelajaran:** Informatika
**Kelas/Semester:** XII / Ganjil
**Materi Pokok:** Bab 2 – Mikrokontroler – Motor Servo, Motor DC, Driver L298N
**Alokasi Waktu:** 5 JP

## A. Tujuan Pembelajaran
1. Peserta didik mampu mengontrol sudut putar motor servo SG90 menggunakan sinyal PWM.
2. Peserta didik mampu mengontrol kecepatan dan arah motor DC menggunakan driver L298N.
3. Peserta didik mampu menggabungkan servo dan motor DC dalam satu proyek.
4. Peserta didik memahami prinsip PWM (Pulse Width Modulation) pada kontrol motor.

## B. Alat dan Bahan
- 1x Arduino Uno + kabel USB
- 1x Breadboard
- 1x Motor servo SG90 (atau MG995)
- 1x Motor DC 3-6V
- 1x Driver motor L298N
- 1x Potensiometer 10k ohm (opsional)
- 1x Baterai 9V atau power supply eksternal (untuk motor DC)
- Kabel jumper secukupnya
- PC/Laptop dengan Arduino IDE

## C. Langkah Kerja

### Bagian 1: Mengenal PWM (15 menit)

PWM (Pulse Width Modulation) adalah teknik mengatur lebar pulsa untuk mengontrol daya.

```
PWM 0%   : ████____________________
PWM 25%  : ████████________________
PWM 50%  : ████████████____________
PWM 75%  : ████████████████████____
PWM 100% : █████████████████████████
```

Pada Arduino Uno, pin dengan simbol `~` mendukung PWM: **3, 5, 6, 9, 10, 11**.
Nilai PWM: 0 (mati) – 255 (maksimum).

### Bagian 2: Motor Servo SG90 (60 menit)

**Teori:** Servo menerima sinyal PWM dengan periode 20 ms. Lebar pulsa 1–2 ms menentukan sudut 0°–180°.

```
0°   : ██__________________________   (pulsa 1 ms)
90°  : ████________________________   (pulsa 1.5 ms)
180° : ██████______________________   (pulsa 2 ms)
```

1. Buat rangkaian berikut:

```
Servo SG90:
  Kabel coklat  → GND
  Kabel merah   → +5V
  Kabel orange  → Pin 9
```

**Diagram Breadboard:**

```
      +---------------------------+
      |                           |
      |  Arduino Uno              |
      |                           |
      |  Pin 9 ----[orange]----- Servo
      |  +5V  ----[merah]------ Servo
      |  GND  ----[coklat]----- Servo
      +---------------------------+
      
      [SG90]
      Coklat (GND)  ┐
      Merah (+5V)   ├── 3 kabel
      Orange (Sinyal)┘
```

2. Gunakan library `Servo.h` (bawaan Arduino IDE).

```c
#include <Servo.h>

Servo myservo;
int pos = 0;

void setup() {
  myservo.attach(9);
  Serial.begin(9600);
  Serial.println("Motor Servo Siap");
}

void loop() {
  // Gerak dari 0 ke 180 derajat
  for (pos = 0; pos <= 180; pos += 1) {
    myservo.write(pos);
    delay(15);
  }

  // Gerak dari 180 ke 0 derajat
  for (pos = 180; pos >= 0; pos -= 1) {
    myservo.write(pos);
    delay(15);
  }
}
```

3. Upload dan amati pergerakan servo.
4. **Tantangan:** Gunakan potensiometer di A0 untuk mengontrol sudut servo.

```c
#include <Servo.h>

Servo myservo;
int potPin = A0;
int nilaiPot;
int sudut;

void setup() {
  myservo.attach(9);
}

void loop() {
  nilaiPot = analogRead(potPin);
  sudut = map(nilaiPot, 0, 1023, 0, 180);
  myservo.write(sudut);
  delay(15);
}
```

### Bagian 3: Motor DC dengan Driver L298N (75 menit)

**Teori:** L298N adalah driver H-bridge yang memungkinkan kontrol arah dan kecepatan motor DC.

**Pin L298N:**
- `ENA` → Enable/kecepatan (PWM)
- `IN1`, `IN2` → Kontrol arah
- `OUT1`, `OUT2` → Ke motor DC
- `+12V` → Power motor (baterai)
- `GND` → Ground bersama Arduino
- `+5V` → Output 5V (opsional)

1. Buat rangkaian:

```
Arduino Uno          L298N              Motor DC
-----------         -------            --------
Pin 10     ------> ENA (PWM)
Pin 9      ------> IN1
Pin 8      ------> IN2
GND        ------> GND
                       OUT1 ------> + Motor
                       OUT2 ------> - Motor
                       +12V <------ Baterai 9V (+)
                       GND  <------ Baterai 9V (-)
```

**Diagram Rangkaian:**

```
      +---------------------------+
      |                           |
      |  Arduino Uno              |
      |  Pin 10 ---- ENA          |
      |  Pin 9  ---- IN1          |   L298N
      |  Pin 8  ---- IN2          |   +----+
      |  GND    ---- GND          |   |    |
      |                           |   +----+
      +---------------------------+    |
                                       | OUT1 ---- Motor DC (+)
                                       | OUT2 ---- Motor DC (-)
                                       |
                                   Baterai 9V
                                   (+)---- +12V
                                   (-)---- GND
```

2. Tulis program:

```c
// Pin kontrol L298N
int enA = 10;  // PWM
int in1 = 9;
int in2 = 8;

void setup() {
  pinMode(enA, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);

  Serial.begin(9600);
  Serial.println("Driver Motor L298N Siap");
}

void loop() {
  // Motor maju (kecepatan 50%)
  Serial.println("Maju 50%");
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);
  analogWrite(enA, 128);
  delay(3000);

  // Motor berhenti
  Serial.println("Berhenti");
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);
  analogWrite(enA, 0);
  delay(2000);

  // Motor mundur (kecepatan 75%)
  Serial.println("Mundur 75%");
  digitalWrite(in1, LOW);
  digitalWrite(in2, HIGH);
  analogWrite(enA, 191);
  delay(3000);

  // Motor berhenti
  Serial.println("Berhenti");
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);
  analogWrite(enA, 0);
  delay(2000);

  // Motor maju (kecepatan 100%)
  Serial.println("Maju 100%");
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);
  analogWrite(enA, 255);
  delay(3000);

  // Motor berhenti
  Serial.println("Berhenti");
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);
  analogWrite(enA, 0);
  delay(2000);
}
```

### Bagian 4: Kontrol Kecepatan Bertahap (30 menit)

Buat program yang mengubah kecepatan motor DC secara bertahap dari 0 ke 255 lalu turun lagi:

```c
int enA = 10;
int in1 = 9;
int in2 = 8;

void setup() {
  pinMode(enA, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);
  Serial.begin(9600);
}

void loop() {
  // Naikkan kecepatan
  for (int speed = 0; speed <= 255; speed += 5) {
    analogWrite(enA, speed);
    Serial.print("Kecepatan: ");
    Serial.println(speed);
    delay(100);
  }

  // Turunkan kecepatan
  for (int speed = 255; speed >= 0; speed -= 5) {
    analogWrite(enA, speed);
    Serial.print("Kecepatan: ");
    Serial.println(speed);
    delay(100);
  }
}
```

### Bagian 5: Proyek Gabungan (30 menit)

Gabungkan servo dan motor DC:
- Servo bergerak ke 0° → motor DC maju 3 detik
- Servo bergerak ke 90° → motor DC berhenti 2 detik
- Servo bergerak ke 180° → motor DC mundur 3 detik

Tulis program sendiri berdasarkan kode dari bagian 2 dan 3.

## D. Tabel Hasil/Data Pengamatan

### Data Servo
| Sudut (derajat) | Nilai PWM (analogWrite) | Lebar Pulsa (ms) | Posisi Fisik |
|----------------|------------------------|-------------------|-------------|
| 0              | -                      | 1.0               |             |
| 45             | -                      | 1.25              |             |
| 90             | -                      | 1.5               |             |
| 135            | -                      | 1.75              |             |
| 180            | -                      | 2.0               |             |

### Data Motor DC
| IN1 | IN2 | ENA (PWM) | Arah | Kecepatan |
|-----|-----|-----------|------|-----------|
| LOW | LOW | 0         |      |           |
| HIGH| LOW | 128       |      |           |
| HIGH| LOW | 255       |      |           |
| LOW | HIGH| 128       |      |           |
| LOW | HIGH| 255       |      |           |

## E. Diskusi dan Analisis

1. Apa perbedaan fungsi `digitalWrite()` dan `analogWrite()` pada Arduino? Pin mana saja yang mendukung `analogWrite()`?
2. Pada motor servo, mengapa kita menggunakan `delay(15)` di dalam perulangan for? Apa yang terjadi jika delay dihilangkan?
3. Jelaskan prinsip kerja H-bridge pada driver L298N! Bagaimana IN1 dan IN2 menentukan arah putaran motor?
4. Jika motor DC tidak berputar padahal program sudah benar, apa saja kemungkinan penyebabnya? (sebutkan minimal 3)
5. Pada proyek gabungan (Bagian 5), bagaimana cara memastikan servo dan motor DC bekerja secara berurutan tanpa konflik daya?

## F. Kesimpulan

Tulis kesimpulan mengenai prinsip PWM, kontrol servo dengan `Servo.h`, kontrol motor DC dengan driver L298N, dan pentingnya power supply terpisah untuk motor.

## G. Penilaian

| Aspek | Bobot | Skor (1-4) | Nilai |
|-------|-------|------------|-------|
| Rangkaian servo | 15% | | |
| Program servo (sweep) | 15% | | |
| Rangkaian L298N + motor DC | 20% | | |
| Program motor DC (maju/mundur) | 20% | | |
| Program kecepatan bertahap | 15% | | |
| Proyek gabungan | 15% | | |
| **Total** | **100%** | | |
