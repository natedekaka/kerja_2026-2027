# LKPD - Sensor Suhu (LM35) dan Sensor Jarak (HC-SR04)
**Mata Pelajaran:** Informatika
**Kelas/Semester:** XII / Ganjil
**Materi Pokok:** Bab 2 – Mikrokontroler – Sensor Analog & Digital
**Alokasi Waktu:** 5 JP

## A. Tujuan Pembelajaran
1. Peserta didik mampu membaca data sensor suhu LM35 menggunakan ADC Arduino.
2. Peserta didik mampu mengkonversi nilai ADC menjadi suhu dalam satuan Celsius.
3. Peserta didik mampu menggunakan sensor ultrasonik HC-SR04 untuk mengukur jarak.
4. Peserta didik mampu menampilkan data sensor ke Serial Monitor.
5. Peserta didik mampu menganalisis akurasi dan presisi data sensor.

## B. Alat dan Bahan
- 1x Arduino Uno + kabel USB
- 1x Breadboard
- 1x Sensor suhu LM35
- 1x Sensor ultrasonik HC-SR04
- Kabel jumper secukupnya
- PC/Laptop dengan Arduino IDE
- Penggaris (untuk kalibrasi jarak)

## C. Langkah Kerja

### Bagian 1: Membaca Sensor Suhu LM35 (60 menit)

**Teori:** LM35 mengeluarkan tegangan 10 mV per °C. Rumus konversi:
```
Suhu (°C) = (ADC_value × 5.0 / 1023.0) × 100
```

1. Buat rangkaian berikut:

```
LM35:
  Pin 1 (kiri)  → +5V
  Pin 2 (tengah) → A0
  Pin 3 (kanan)  → GND
```

**Diagram Breadboard:**

```
      +---------------------------+
      |                           |
      |  Arduino Uno              |
      |                           |
      |  +5V ----[kabel]---- Pin 1 LM35
      |  A0   ----[kabel]---- Pin 2 LM35
      |  GND  ----[kabel]---- Pin 3 LM35
      +---------------------------+
      
        [LM35 - tampak datar]
        +-----+
        |1 2 3|   1 = +5V
        +-----+   2 = Vout (ke A0)
       [____]     3 = GND
```

2. Tulis program berikut:

```c
int sensorLM35 = A0;
float suhu = 0;
int nilaiADC = 0;

void setup() {
  Serial.begin(9600);
  Serial.println("Pengukuran Suhu LM35");
  Serial.println("--------------------");
}

void loop() {
  nilaiADC = analogRead(sensorLM35);
  suhu = (nilaiADC * 5.0 / 1023.0) * 100.0;

  Serial.print("ADC: ");
  Serial.print(nilaiADC);
  Serial.print(" | Tegangan: ");
  Serial.print(nilaiADC * 5.0 / 1023.0, 3);
  Serial.print(" V | Suhu: ");
  Serial.print(suhu, 2);
  Serial.println(" C");

  delay(1000);
}
```

3. Upload dan buka Serial Monitor (Ctrl+Shift+M, baud 9600).
4. Amati suhu ruangan. Catat selama 5 menit (5 data).
5. **Uji kalibrasi:**
   - Pegang sensor dengan jari (panas tubuh) → catat suhu
   - Dekatkan sensor ke es batu (hati-hati jangan kena air) → catat suhu

### Bagian 2: Membaca Sensor Jarak HC-SR04 (60 menit)

**Teori:** HC-SR04 mengirim gelombang ultrasonik dan mengukur waktu pantul.
```
Jarak (cm) = (waktu_pantul / 2) × 0.0343
```

1. Buat rangkaian berikut:

```
HC-SR04:
  Vcc  → +5V
  Trig → Pin 9
  Echo → Pin 10
  Gnd  → GND
```

**Diagram Breadboard:**

```
      +---------------------------+
      |                           |
      |  Arduino Uno              |
      |                           |
      |  +5V  ----[kabel]---- Vcc  (HC-SR04)
      |  Pin 9 ----[kabel]---- Trig
      |  Pin 10 ----[kabel]---- Echo
      |  GND  ----[kabel]---- Gnd
      +---------------------------+
      
      [HC-SR04]
      +------------------+
      |   Vcc Trig Echo Gnd |
      |   [TT]  [RR]        |
      +------------------+
      TT = Transmitter (pemancar)
      RR = Receiver (penerima)
```

2. Tulis program berikut:

```c
#define trigPin 9
#define echoPin 10

long durasi;
float jarak;

void setup() {
  Serial.begin(9600);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  Serial.println("Pengukuran Jarak HC-SR04");
  Serial.println("-------------------------");
}

void loop() {
  // Kirim trigger pulse (10 us)
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  // Baca durasi pantulan
  durasi = pulseIn(echoPin, HIGH);

  // Konversi ke cm (kecepatan suara 343 m/s)
  jarak = (durasi / 2.0) * 0.0343;

  Serial.print("Durasi: ");
  Serial.print(durasi);
  Serial.print(" us | Jarak: ");
  Serial.print(jarak, 2);
  Serial.println(" cm");

  delay(500);
}
```

3. Upload dan buka Serial Monitor.
4. **Uji pengukuran:**
   - Tempatkan benda di depan sensor pada jarak 5 cm, 10 cm, 20 cm, 50 cm
   - Bandingkan dengan hasil ukur penggaris
   - Catat ke tabel pengamatan

### Bagian 3: Kalibrasi dan Akurasi (30 menit)

1. Tempelkan penggaris di meja.
2. Letakkan benda (buku/kardus) pada jarak tertentu.
3. Bandingkan hasil sensor dengan penggaris.
4. Hitung error:

```
Error (%) = |Jarak Sensor - Jarak Nyata| / Jarak Nyata × 100%
```

### Bagian 4: Program Gabungan (45 menit)

Buat program yang membaca kedua sensor sekaligus:

```c
int sensorLM35 = A0;
#define trigPin 9
#define echoPin 10

float suhu;
float jarak;
long durasi;
int nilaiADC;

void setup() {
  Serial.begin(9600);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}

void loop() {
  // Baca suhu
  nilaiADC = analogRead(sensorLM35);
  suhu = (nilaiADC * 5.0 / 1023.0) * 100.0;

  // Baca jarak
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  durasi = pulseIn(echoPin, HIGH);
  jarak = (durasi / 2.0) * 0.0343;

  // Tampilkan ke Serial Monitor
  Serial.print("Suhu: ");
  Serial.print(suhu, 1);
  Serial.print(" C | Jarak: ");
  Serial.print(jarak, 1);
  Serial.println(" cm");

  delay(1000);
}
```

## D. Tabel Hasil/Data Pengamatan

### Data Sensor Suhu LM35
| No | Nilai ADC | Tegangan (V) | Suhu (°C) | Kondisi |
|----|-----------|-------------|-----------|---------|
| 1  |           |             |           | Ruangan |
| 2  |           |             |           | Ruangan |
| 3  |           |             |           | Ruangan |
| 4  |           |             |           | Pegang  |
| 5  |           |             |           | Es/Dingin|

### Data Sensor Jarak HC-SR04
| No | Jarak Nyata (cm) | Durasi (us) | Jarak Sensor (cm) | Error (%) |
|----|------------------|-------------|-------------------|-----------|
| 1  | 5                |             |                   |           |
| 2  | 10               |             |                   |           |
| 3  | 20               |             |                   |           |
| 4  | 30               |             |                   |           |
| 5  | 50               |             |                   |           |

## E. Diskusi dan Analisis

1. Mengapa LM35 tidak memerlukan library tambahan, sementara sensor lain seperti DHT11 membutuhkan?
2. Faktor apa saja yang mempengaruhi akurasi pengukuran jarak HC-SR04? Bagaimana pengaruh suhu ruangan?
3. Jika HC-SR04 digunakan untuk mengukur jarak di dalam air, apakah hasilnya akurat? Jelaskan!
4. Pada program gabungan, mengapa pembacaan jarak kadang menampilkan nilai 0? Bagaimana cara mengatasinya?
5. Buatlah grafik hubungan antara jarak nyata (sumbu X) dengan jarak sensor (sumbu Y) berdasarkan data pengamatan. Apakah hubungannya linear?

## F. Kesimpulan

Buat kesimpulan tentang cara kerja ADC pada Arduino, prinsip pengukuran suhu dengan LM35, prinsip sonar pada HC-SR04, serta pentingnya kalibrasi dalam pengukuran sensor.

## G. Penilaian

| Aspek | Bobot | Skor (1-4) | Nilai |
|-------|-------|------------|-------|
| Rangkaian LM35 | 15% | | |
| Rangkaian HC-SR04 | 15% | | |
| Program LM35 (ADC → suhu) | 20% | | |
| Program HC-SR04 (pulseIn) | 20% | | |
| Program gabungan | 15% | | |
| Data pengamatan & analisis | 15% | | |
| **Total** | **100%** | | |
