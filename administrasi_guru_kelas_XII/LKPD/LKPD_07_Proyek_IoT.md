# LKPD - Proyek IoT: Smart Monitor atau Otomasi Relay
**Mata Pelajaran:** Informatika
**Kelas/Semester:** XII / Genap
**Materi Pokok:** Bab 6 – Proyek IoT – Smart Monitor & Otomasi
**Alokasi Waktu:** 5 JP

## A. Tujuan Pembelajaran
1. Peserta didik mampu merencanakan proyek IoT sederhana secara mandiri.
2. Peserta didik mampu merakit rangkaian DHT11 + LCD atau relay otomasi.
3. Peserta didik mampu memprogram Arduino/ESP32 untuk membaca sensor dan mengontrol aktuator.
4. Peserta didik mampu menguji dan memvalidasi sistem yang dibuat.
5. Peserta didik mampu membuat laporan proyek yang sistematis.

## B. Alat dan Bahan

### Opsi A: Smart Monitor (DHT11 + LCD)
| No | Komponen | Jumlah |
|----|----------|--------|
| 1  | Arduino Uno / ESP32 | 1 |
| 2  | Sensor DHT11 | 1 |
| 3  | LCD 16×2 + I2C | 1 |
| 4  | Breadboard | 1 |
| 5  | Kabel jumper | secukupnya |
| 6  | Kabel USB | 1 |

### Opsi B: Otomasi Relay
| No | Komponen | Jumlah |
|----|----------|--------|
| 1  | Arduino Uno / ESP32 | 1 |
| 2  | Modul Relay 1/2 channel | 1 |
| 3  | Lampu DC / LED 12V | 1 |
| 4  | Push button | 2 |
| 5  | Sensor LDR (opsional) | 1 |
| 6  | Breadboard | 1 |
| 7  | Kabel jumper & power supply | secukupnya |

## C. Langkah Kerja

### Bagian 1: Perencanaan Proyek (30 menit)

1. Pilih salah satu opsi proyek (A atau B).
2. Buatlah perencanaan dengan format:

```
Nama Proyek     : 
Tujuan          : 
Komponen        : 
Cara Kerja      : 
Diagram Blok    : (gambar manual / digital)
```

### Bagian 2A: Smart Monitor (DHT11 + LCD) — 120 menit

**Diagram Rangkaian:**

```
DHT11:
  Pin 1 (VCC)  → +5V
  Pin 2 (DATA) → Pin 7
  Pin 4 (GND)  → GND

LCD I2C:
  VCC → +5V
  GND → GND
  SDA → A4 (Uno) / Pin 21 (ESP32)
  SCL → A5 (Uno) / Pin 22 (ESP32)
```

**Diagram Breadboard:**

```
      +--------------------------------------+
      |                                      |
      |  Arduino Uno                         |
      |                                      |
      |  +5V  ---- DHT11(VCC) ---- LCD(VCC) |
      |  GND  ---- DHT11(GND) ---- LCD(GND) |
      |  Pin 7 ---- DHT11(DATA)             |
      |  A4    ---- LCD(SDA)                |
      |  A5    ---- LCD(SCL)                |
      +--------------------------------------+
      
      [DHT11]
      +----+
      |    |  (depan / grill)
      | 1234|  1=VCC  2=DATA  3=NC  4=GND
      +----+
```

**Kode Program:**

```c
#include <DHT.h>
#include <LiquidCrystal_I2C.h>

#define DHTPIN 7
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);
LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {
  Serial.begin(9600);
  dht.begin();

  lcd.init();
  lcd.backlight();
  lcd.setCursor(0, 0);
  lcd.print("Smart Monitor");
  delay(2000);
  lcd.clear();
}

void loop() {
  float suhu = dht.readTemperature();
  float kelembaban = dht.readHumidity();

  if (isnan(suhu) || isnan(kelembaban)) {
    Serial.println("Gagal membaca DHT11!");
    lcd.setCursor(0, 0);
    lcd.print("Sensor Error!");
    delay(1000);
    return;
  }

  // Tampilkan di Serial Monitor
  Serial.print("Suhu: ");
  Serial.print(suhu);
  Serial.print(" C | Kelembaban: ");
  Serial.print(kelembaban);
  Serial.println("%");

  // Tampilkan di LCD
  lcd.setCursor(0, 0);
  lcd.print("Suhu: ");
  lcd.print(suhu, 1);
  lcd.print("C");

  lcd.setCursor(0, 1);
  lcd.print("RH:   ");
  lcd.print(kelembaban, 1);
  lcd.print("%");

  delay(2000);
}
```

**Catatan:** Jika LCD I2C tidak muncul, coba alamat `0x3F` atau `0x27`. Jalankan I2C Scanner jika perlu.

### Bagian 2B: Otomasi Relay — 120 menit

**Diagram Rangkaian:**

```
Relay:
  VCC → +5V
  GND → GND
  IN1 → Pin 8
  IN2 → Pin 9 (jika relay 2 ch)

LED/Lampu:
  COM (Relay) → +5V
  NO (Relay)  → (+) LED/Lampu
  GND         → (-) LED/Lampu

Button:
  Pin 2 (button1) → +5V (dengan pull-down 10k)
  Pin 3 (button2) → +5V (dengan pull-down 10k)
```

**Diagram Breadboard:**

```
      +--------------------------------------+
      |                                      |
      |  Arduino Uno                         |
      |                                      |
      |  +5V  ---- Relay(VCC) ---- Button   |
      |  GND  ---- Relay(GND) ---- LED(-)   |
      |  Pin 8 ---- Relay(IN1)              |
      |  Pin 2 ---- Button1 (via 10k ke GND)|
      |  Pin 3 ---- Button2 (via 10k ke GND)|
      +--------------------------------------+
      
      [Relay Module]
      +-------------+
      | VCC GND IN1 |
      | COM NO NC   |
      +-------------+
      COM = Common, NO = Normally Open, NC = Normally Closed
```

**Kode Program:**

```c
#define RELAY1 8
#define RELAY2 9
#define BUTTON1 2
#define BUTTON2 3

bool relay1State = false;
bool relay2State = false;
int lastButton1 = LOW;
int lastButton2 = LOW;

void setup() {
  pinMode(RELAY1, OUTPUT);
  pinMode(RELAY2, OUTPUT);
  pinMode(BUTTON1, INPUT);
  pinMode(BUTTON2, INPUT);

  digitalWrite(RELAY1, LOW);
  digitalWrite(RELAY2, LOW);

  Serial.begin(9600);
  Serial.println("Sistem Otomasi Relay Siap");
}

void loop() {
  int btn1 = digitalRead(BUTTON1);
  int btn2 = digitalRead(BUTTON2);

  // Button 1: toggle relay 1
  if (btn1 == HIGH && lastButton1 == LOW) {
    relay1State = !relay1State;
    digitalWrite(RELAY1, relay1State);
    Serial.print("Relay 1: ");
    Serial.println(relay1State ? "ON" : "OFF");
    delay(50);
  }

  // Button 2: toggle relay 2
  if (btn2 == HIGH && lastButton2 == LOW) {
    relay2State = !relay2State;
    digitalWrite(RELAY2, relay2State);
    Serial.print("Relay 2: ");
    Serial.println(relay2State ? "ON" : "OFF");
    delay(50);
  }

  // Otomasi suhu: jika menggunakan DHT11, relay 1 ON saat suhu > 30°C
  // (modifikasi sesuai komponen yang ada)

  lastButton1 = btn1;
  lastButton2 = btn2;
  delay(10);
}
```

### Bagian 3: Pengujian Sistem (30 menit)

1. Upload program ke Arduino/ESP32.
2. Uji setiap fitur:
   - **Opsi A:** Apakah suhu dan kelembaban terbaca di LCD dan Serial Monitor?
   - **Opsi B:** Apakah relay menyala/mati saat tombol ditekan?
3. Jika ada error, lakukan debugging:
   - Periksa koneksi kabel
   - Periksa alamat I2C (untuk LCD)
   - Baca pesan error di Serial Monitor
   - Periksa library yang digunakan (install jika belum)

### Bagian 4: Dokumentasi dan Laporan (60 menit)

Buat laporan proyek dengan format berikut:

---

## TEMPLATE LAPORAN PROYEK IoT

### 1. Judul Proyek
...

### 2. Latar Belakang
(Jelaskan mengapa proyek ini dibuat, masalah apa yang ingin diselesaikan)

### 3. Tujuan
...

### 4. Diagram Sistem

Gambar diagram blok sistem:

```
+------------------+      +------------------+      +------------------+
|   INPUT          |      |   PROSES         |      |   OUTPUT         |
| - Sensor DHT11   | ---> | - Arduino/ESP32  | ---> | - LCD 16x2      |
| - Button         |      | - Logika kontrol |      | - Relay/Lampu   |
| - LDR            |      |                  |      | - Serial Monitor|
+------------------+      +------------------+      +------------------+
                                  |
                           +------------------+
                           |   KOMUNIKASI     |
                           | - Serial (USB)   |
                           | - WiFi/Cloud     |
                           +------------------+
```

### 5. Alat dan Bahan
| No | Nama Komponen | Spesifikasi | Jumlah |
|----|---------------|-------------|--------|
| 1  |               |             |        |
| 2  |               |             |        |
| 3  |               |             |        |

### 6. Skema Rangkaian
(Gambar skema rangkaian / foto rangkaian asli)

### 7. Kode Program
(Salin kode program yang dibuat)

### 8. Cara Kerja
(Jelaskan alur kerja sistem step by step)

### 9. Hasil Pengujian
| No | Skenario Uji | Input | Output yang Diharapkan | Output Aktual | Status |
|----|-------------|-------|----------------------|--------------|--------|
| 1  |             |       |                      |              |        |
| 2  |             |       |                      |              |        |

### 10. Analisis dan Pembahasan
(3–5 paragraf analisis)

### 11. Kesimpulan dan Saran
(2–3 paragraf kesimpulan + saran pengembangan)

---

## D. Tabel Hasil/Data Pengamatan

### Pengujian Smart Monitor (Opsi A)
| No | Waktu (menit ke-) | Suhu (°C) | Kelembaban (%) | Keterangan |
|----|------------------|-----------|---------------|------------|
| 1  | 0                |           |               |            |
| 2  | 2                |           |               |            |
| 3  | 4                |           |               |            |
| 4  | 6                |           |               |            |
| 5  | 8                |           |               |            |
| 6  | 10               |           |               |            |

### Pengujian Otomasi Relay (Opsi B)
| No | Tombol | Aksi | Status Relay 1 | Status Relay 2 | LED/Lampu |
|----|--------|------|----------------|----------------|-----------|
| 1  | Button1 | Tekan |                | -              |           |
| 2  | Button1 | Tekan lg |                | -              |           |
| 3  | Button2 | Tekan | -              |                |           |
| 4  | Button2 | Tekan lg | -              |                |           |

## E. Diskusi dan Analisis

1. Apa kendala terbesar yang Anda hadapi selama pengerjaan proyek? Bagaimana cara mengatasinya?
2. Bandingkan penggunaan Arduino Uno dengan ESP32 untuk proyek IoT! Kapan sebaiknya menggunakan masing-masing?
3. Jika proyek Smart Monitor dikembangkan dengan koneksi internet (IoT Cloud), fitur apa saja yang bisa ditambahkan?
4. Pada proyek otomasi relay, bagaimana cara menambahkan sensor cahaya (LDR) agar relay menyala otomatis saat gelap?
5. Jelaskan potensi pengembangan proyek ini menjadi produk yang bermanfaat di lingkungan sekolah atau rumah!

## F. Kesimpulan

Tulis kesimpulan yang mencakup:
- Pengalaman merencanakan dan mengerjakan proyek IoT dari awal hingga akhir
- Pemahaman tentang integrasi sensor, aktuator, dan mikrokontroler
- Refleksi terhadap kesulitan dan solusi yang ditemukan
- Rencana pengembangan proyek ke depan

## G. Penilaian

| Aspek | Bobot | Skor (1-4) | Nilai |
|-------|-------|------------|-------|
| Perencanaan proyek | 10% | | |
| Rangkaian elektronika | 15% | | |
| Kode program | 20% | | |
| Fungsionalitas sistem | 20% | | |
| Pengujian dan debugging | 10% | | |
| Laporan proyek | 20% | | |
| Presentasi/demonstrasi | 5% | | |
| **Total** | **100%** | | |
