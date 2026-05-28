# LKPD - Rangkaian LED dengan Arduino Uno
**Mata Pelajaran:** Informatika
**Kelas/Semester:** XII / Ganjil
**Materi Pokok:** Bab 2 – Mikrokontroler (Arduino Uno) – LED, Button, Running LED
**Alokasi Waktu:** 5 JP

## A. Tujuan Pembelajaran
1. Peserta didik mampu menjelaskan cara kerja LED dan resistor pada rangkaian elektronika.
2. Peserta didik mampu membuat program blink LED pada Arduino Uno.
3. Peserta didik mampu membuat program running LED (LED berjalan).
4. Peserta didik mampu membuat program LED yang dikendalikan tombol (button).
5. Peserta didik mampu membaca dan memahami diagram rangkaian.

## B. Alat dan Bahan
- 1x Arduino Uno + kabel USB
- 1x Breadboard
- 5x LED (warna merah, kuning, hijau)
- 5x Resistor 220 ohm
- 1x Push button / tactile switch
- 1x Resistor 10k ohm (pull-down)
- Kabel jumper secukupnya
- PC/Laptop dengan Arduino IDE

## C. Langkah Kerja

### Bagian 1: Rangkaian LED Sederhana – Blink (30 menit)

1. Siapkan breadboard dan Arduino Uno.
2. Buat rangkaian berikut:

```
         +5V
          |
         (Arduino Uno)
          |
        Pin 13 ----[220R]---->|---- GND
                           LED Merah
```

**Diagram Breadboard:**

```
      +---------------------------+
      |                           |
      |  Arduino Uno              |
      |                           |
      |  GND ----[kabel]---- GND  |
      |  Pin 13 --[kabel]------  |
      |         |                |
      |      [220 ohm]           |
      |         |                |
      |      [LED] (anoda ke 13) |
      |         |                |
      |       GND                |
      +---------------------------+
```

3. Tulis program berikut di Arduino IDE:

```c
int ledPin = 13;

void setup() {
  pinMode(ledPin, OUTPUT);
}

void loop() {
  digitalWrite(ledPin, HIGH);
  delay(1000);
  digitalWrite(ledPin, LOW);
  delay(1000);
}
```

4. Upload program ke Arduino Uno.
5. Amati LED: menyala 1 detik, mati 1 detik (blink).
6. Ubah nilai `delay` menjadi 200 ms dan 2000 ms. Amati perubahannya.

### Bagian 2: Running LED (tiga LED bergantian) (45 menit)

1. Tambahkan 2 LED lagi ke breadboard:

```
Pin 11 ----[220R]---->|---- GND    (LED 1 - Merah)
Pin 12 ----[220R]---->|---- GND    (LED 2 - Kuning)
Pin 13 ----[220R]---->|---- GND    (LED 3 - Hijau)
```

**Diagram Breadboard:**

```
      +---------------------------+
      |                           |
      |  Arduino Uno              |
      |                           |
      |  Pin 11 --[220R]-- [LED] -+-- GND
      |  Pin 12 --[220R]-- [LED] -+-- GND
      |  Pin 13 --[220R]-- [LED] -+-- GND
      +---------------------------+
```

2. Tulis program berikut:

```c
int ledPins[] = {11, 12, 13};
int jumlahLED = 3;

void setup() {
  for (int i = 0; i < jumlahLED; i++) {
    pinMode(ledPins[i], OUTPUT);
  }
}

void loop() {
  // LED menyala bergantian dari kiri ke kanan
  for (int i = 0; i < jumlahLED; i++) {
    digitalWrite(ledPins[i], HIGH);
    delay(300);
    digitalWrite(ledPins[i], LOW);
  }

  // LED menyala bergantian dari kanan ke kiri
  for (int i = jumlahLED - 1; i >= 0; i--) {
    digitalWrite(ledPins[i], HIGH);
    delay(300);
    digitalWrite(ledPins[i], LOW);
  }
}
```

3. Upload dan amati pola nyala LED (running LED / efek lampu berjalan).

### Bagian 3: LED dengan Tombol (Button) (45 menit)

1. Tambahkan push button ke rangkaian:

```
        +5V
         |
       [button]
         |
Pin 7 --+----[10kR]---- GND
```

**Diagram Breadboard:**

```
      +---------------------------+
      |                           |
      |  Arduino Uno              |
      |                           |
      |  Pin 7 ---+----[10kR]--- GND
      |           |
      |        [button]
      |           |
      |        +5V
      |                           |
      |  Pin 13 ----[220R]--[LED]-+-- GND
      +---------------------------+
```

2. Tulis program berikut:

```c
int buttonPin = 7;
int ledPin = 13;
int buttonState = 0;

void setup() {
  pinMode(ledPin, OUTPUT);
  pinMode(buttonPin, INPUT);
  Serial.begin(9600);
}

void loop() {
  buttonState = digitalRead(buttonPin);

  if (buttonState == HIGH) {
    digitalWrite(ledPin, HIGH);
    Serial.println("Tombol ditekan - LED ON");
  } else {
    digitalWrite(ledPin, LOW);
    Serial.println("Tombol lepas - LED OFF");
  }

  delay(50);
}
```

3. Upload dan uji: tekan tombol, LED menyala. Lepas, LED mati.
4. Modifikasi: buat LED toggle (tekan sekali nyala, tekan sekali lagi mati).

**Kode toggle (tantangan):**

```c
int buttonPin = 7;
int ledPin = 13;
boolean ledState = false;
int lastButtonState = LOW;

void setup() {
  pinMode(ledPin, OUTPUT);
  pinMode(buttonPin, INPUT);
}

void loop() {
  int currentButtonState = digitalRead(buttonPin);

  if (currentButtonState == HIGH && lastButtonState == LOW) {
    ledState = !ledState;
    digitalWrite(ledPin, ledState);
    delay(50);
  }

  lastButtonState = currentButtonState;
}
```

### Bagian 4: Eksperimen Mandiri (30 menit)

Buat program yang menggabungkan:
- 3 LED (merah, kuning, hijau) seperti lampu lalu lintas
- 1 tombol untuk mode darurat (semua LED blink cepat saat tombol ditekan)

## D. Tabel Hasil/Data Pengamatan

### Percobaan Blink LED
| Delay (ms) | Pengamatan |
|------------|------------|
| 200        |            |
| 1000       |            |
| 2000       |            |

### Percobaan Running LED
| Mode | Urutan Nyala | Waktu (dtk) |
|------|-------------|-------------|
| Kiri ke kanan | 11→12→13 |             |
| Kanan ke kiri | 13→12→11 |             |

### Percobaan Button LED
| Kondisi Tombol | LED | Serial Monitor |
|----------------|-----|----------------|
| Ditekan        |     |                |
| Dilepas        |     |                |

## E. Diskusi dan Analisis

1. Apa fungsi resistor 220 ohm yang dipasang seri dengan LED? Apa yang terjadi jika resistor tidak dipasang?
2. Mengapa pada rangkaian tombol diperlukan resistor pull-down (10k ohm ke GND)?
3. Jelaskan perbedaan penggunaan `pinMode(pin, INPUT)` dengan `pinMode(pin, INPUT_PULLUP)`!
4. Pada program running LED, bagaimana cara membuat efek "knight rider" (LED mundur-balik tanpa jeda di ujung)?
5. Jika ingin menyalakan LED dengan kecerahan yang dapat diatur (PWM), pin mana saja yang bisa digunakan pada Arduino Uno?

## F. Kesimpulan

Buatlah kesimpulan mengenai prinsip kerja digital output (digitalWrite), digital input (digitalRead), dan penggunaan komponen pasif (resistor) dalam rangkaian Arduino.

## G. Penilaian

| Aspek | Bobot | Skor (1-4) | Nilai |
|-------|-------|------------|-------|
| Ketepatan rangkaian | 20% | | |
| Kode blink LED | 15% | | |
| Kode running LED | 20% | | |
| Kode button LED | 20% | | |
| Tugas mandiri (traffic light) | 15% | | |
| Laporan dan analisis | 10% | | |
| **Total** | **100%** | | |
