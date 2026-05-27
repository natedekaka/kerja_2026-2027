# 💻 Bab 2: Sistem Komputer

> **Semester Ganjil** | **Fase F** | **Kelas XII** | **35 JP**

---

---
## 📊 Pemetaan Capaian Pembelajaran

| Elemen CP | Deskripsi CP |
|-----------|-------------|
| Sistem Komputer | Peserta didik mampu memahami arsitektur sistem komputer, perbedaan SBC dan mikrokontroler, serta mampu menggunakan platform Arduino untuk membuat sistem elektronik sederhana. |

## 🎯 Tujuan Pembelajaran

- **A.** SBC vs Mikrokontroler
- **B.** Kenalan dengan Arduino
- **C.** Instalasi IDE Arduino
- **D.** Komponen Penunjang Arduino
- **E.** Simulator Arduino
- **F.** Praktik: LED & Sensor
- **G.** Proyek Mini: Monitoring Suhu

## 🗺️ Peta Konsep

```
               💻 SISTEM KOMPUTER
                     |
                     ├── A. SBC vs Mikrokontroler
                     ├── B. Kenalan dengan Arduino
                     ├── C. Instalasi IDE Arduino
                     ├── D. Komponen Penunjang Arduino
                     ├── E. Simulator Arduino
                     ├── F. Praktik: LED & Sensor
                     └── G. Proyek Mini: Monitoring Suhu
```

## A. SBC vs Mikrokontroler

### 🖥️ SBC vs Mikrokontroler
**SBC (Single Board Computer)** dan **Mikrokontroler** adalah dua jenis perangkat yang sering tertukar. Mari bedakan!

```
   ┌───────────────────────┬──────────────────────────┐
   │   SBC (Computer)      │   Mikrokontroler         │
   │                       │                          │
   │  • Seperti komputer    │  • Seperti otak alat     │
   │    mini                │    elektronik            │
   │  • Bisa pakai OS      │  • Tidak pakai OS        │
   │  • Contoh: Raspberry  │  • Contoh: Arduino       │
   │    Pi, Orange Pi      │    ESP32, STM32          │
   │  • Untuk tugas berat  │  • Untuk tugas spesifik  │
   └───────────────────────┴──────────────────────────┘
```

| Aspek | SBC (Raspberry Pi) | Mikrokontroler (Arduino) |
|-------|-------------------|------------------------|
| **OS** | Bisa Linux/Windows IoT | Tidak ada OS, program langsung jalan |
| **Konektivitas** | WiFi, Bluetooth, USB, HDMI | GPIO, I2C, SPI, Serial |
| **Konsumsi Daya** | 5-15 watt | 0.1-0.5 watt |
| **Kecepatan** | 1-2 GHz | 16-240 MHz |
| **Cocok untuk** | Server mini, media center, IoT hub | Sensor, robot, kontrol otomatis |

> 💡 **Intinya:** SBC itu seperti laptop mini, mikrokontroler itu seperti otak yang khusus untuk satu tugas spesifik (misal: nyalakan LED kalau suhu panas).

### 🔍 Cek Pemahaman
1. Apa perbedaan utama SBC dan mikrokontroler dalam hal sistem operasi?
2. Mana yang lebih cocok untuk membuat server mini? Mengapa?
3. Mana yang lebih hemat daya? SBC atau mikrokontroler?

### 📋 Studi Kasus
**Raspberry Pi untuk Absensi Sekolah**

SMA Nusantara ingin membuat sistem absensi digital. Tim IT sekolah mempertimbangkan dua opsi: menggunakan Raspberry Pi (SBC) atau Arduino (mikrokontroler). Sistem absensi perlu: kamera untuk foto siswa, database untuk menyimpan data, dan layar monitor untuk menampilkan informasi.

*Pertanyaan:*
1. Manakah yang lebih tepat untuk proyek ini, SBC atau mikrokontroler? Mengapa?
2. Sebutkan komponen SBC yang dibutuhkan untuk menjalankan sistem ini!

> 🤔 **Mari Renungkan:** Apa hal paling menarik yang kamu pelajari dari bagian ini?

---

## B. Kenalan dengan Arduino

### 🔌 Kenalan dengan Arduino
Arduino adalah **platform prototyping elektronik open-source** yang berbasis mikrokontroler. Dibuat di Italia, namanya diambil dari Bar di Ivrea.

> 🧩 **Analogi:** Arduino itu seperti papan sirkuit ajaib. Kamu tinggal colokkan sensor, lampu LED, motor, lalu beri perintah lewat kode program, dan Arduino akan menjalankannya. Ini cara termudah belajar elektronika & coding!

### Kenapa Arduino?
1. ✅ **Murah** — Mulai Rp70.000-an
2. ✅ **Mudah** — Bahasa C yang disederhanakan
3. ✅ **Komunitas besar** — Tutorial melimpah di internet
4. ✅ **Open-source** — Skema dan software bebas dimodifikasi
5. ✅ **Banyak sensor** — Ribuan sensor kompatibel

### Jenis Arduino
| Model | Prosesor | GPIO | Cocok untuk |
|-------|----------|------|-------------|
| **Uno** | ATmega328P | 14 pin | Pemula, proyek dasar |
| **Nano** | ATmega328P | 14 pin | Proyek kecil, portable |
| **Mega** | ATmega2560 | 54 pin | Proyek besar, banyak sensor |
| **ESP32** | Dual-core | 25 pin | IoT + WiFi + Bluetooth |

### 🔍 Cek Pemahaman
1. Mengapa Arduino cocok untuk pemula yang belajar elektronika?
2. Sebutkan 3 jenis Arduino dan kegunaannya!
3. Apa kepanjangan dari ESP32 dan apa kelebihannya dibanding Arduino Uno?

### 📋 Studi Kasus
**Proyek Lampu Otomatis untuk Kamar Kos**

Dimas, mahasiswa rantau, ingin membuat lampu kamar kosnya menyala otomatis saat gelap. Ia memilih Arduino Uno karena murah (Rp75.000) dan mudah diprogram. Ia membeli sensor LDR (cahaya) dan modul relay. Dalam semalam, Dimas berhasil membuat prototipe lampu otomatis pertamanya berkat tutorial dari komunitas Arduino di YouTube.

*Pertanyaan:*
1. Mengapa Dimas memilih Arduino Uno dan bukan Raspberry Pi?
2. Komponen apa saja yang digunakan Dimas dan apa fungsi masing-masing?

> 🤔 **Mari Renungkan:** Apa hal paling menarik yang kamu pelajari dari bagian ini?

---

## C. Instalasi IDE Arduino

### ⚙️ Instalasi IDE Arduino
IDE (Integrated Development Environment) Arduino adalah software untuk menulis, meng-compile, dan mengupload program ke papan Arduino.

### Langkah Instalasi (Linux)
```bash
# 1. Download dari https://www.arduino.cc/en/software
# 2. Ekstrak file tar.gz
tar -xvf arduino-*.tar.xz
# 3. Jalankan installer
cd arduino-*
./install.sh
# 4. Beri akses port serial
sudo usermod -a -G dialout $USER
# 5. Instal selesai! Jalankan Arduino IDE
arduino
```

### Tampilan Arduino IDE
```
  ┌─────────────────────────────────────────┐
  │  sketch_oct01a | Arduino IDE 2.x       │
  ├─────────────────────────────────────────┤
  │ [File] [Edit] [Sketch] [Tools] [Help]  │
  ├─────────────────────────────────────────┤
  │ 1  void setup() {                       │
  │ 2    pinMode(13, OUTPUT);               │ ← Area menulis kode
  │ 3  }                                     │   (Editor)
  │ 4                                        │
  │ 5  void loop() {                         │
  │ 6    digitalWrite(13, HIGH);             │
  │ 7    delay(1000);                        │
  │ 8    digitalWrite(13, LOW);              │
  │ 9    delay(1000);                        │
  │ 10 }                                     │
  ├─────────────────────────────────────────┤
  │ ✅ Compilation complete.                │
  └─────────────────────────────────────────┘
```

### ✍️ Program Pertamamu: BLINK!
```cpp
void setup() {
  pinMode(13, OUTPUT);  // Set pin 13 sebagai OUTPUT
}
void loop() {
  digitalWrite(13, HIGH);  // Nyalakan LED
  delay(1000);              // Tunggu 1 detik
  digitalWrite(13, LOW);   // Matikan LED
  delay(1000);              // Tunggu 1 detik
}
```

> 🔑 **Struktur Dasar:** setiap program Arduino punya **setup()** (dijalankan sekali) dan **loop()** (dijalankan terus-menerus).

### 🔍 Cek Pemahaman
1. Apa kepanjangan dari IDE?
2. Sebutkan fungsi dari `setup()` dan `loop()` dalam program Arduino!
3. Apa fungsi `pinMode(13, OUTPUT)` dan `digitalWrite(13, HIGH)`?

### 📋 Studi Kasus
**Gagal Upload Program Pertama**

Rani baru pertama kali menggunakan Arduino IDE. Ia sudah menulis kode LED blink, tapi saat mencoba upload, muncul error "port not found". Ternyata ia lupa memberi akses port serial dengan perintah `sudo usermod -a -G dialout $USER`. Setelah restart komputer dan menjalankan perintah tersebut, program berhasil di-upload.

*Pertanyaan:*
1. Apa penyebab error yang dialami Rani?
2. Langkah apa yang harus dilakukan setelah memberi akses port serial?

> 🤔 **Mari Renungkan:** Apa hal paling menarik yang kamu pelajari dari bagian ini?

---

## D. Komponen Penunjang Arduino

### 🧩 Komponen Penunjang Arduino
Arduino tidak bekerja sendiri. Dia butuh teman-teman berikut:

### 1. Sensor — Alat yang mendeteksi perubahan lingkungan
| Sensor | Mendeteksi | Contoh Penggunaan |
|--------|------------|-------------------|
| **LM35/DHT11** | Suhu & kelembaban | Termometer digital |
| **LDR** | Cahaya | Lampu otomatis |
| **HC-SR04** | Jarak (ultrasonik) | Parking sensor mobil |
| **PIR** | Gerakan manusia | Lampu otomatis saat ada orang |
| **MQ-series** | Gas (asap, LPG) | Detektor kebocoran gas |

### 2. Aktuator — Alat yang melakukan aksi fisik
- **LED** — Lampu indikator
- **Motor DC** — Memutar roda/mekanik
- **Servo** — Menggerakkan lengan robot
- **Buzzer** — Menghasilkan bunyi
- **LCD 16x2** — Menampilkan teks

### 3. Komponen Pendukung
- **Breadboard** — Papan tempat merangkai tanpa solder
- **Kabel Jumper** — Kabel penghubung (male-male, male-female, female-female)
- **Resistor** — Menahan arus (biasanya 220 Ohm untuk LED)
- **Power Supply** — Sumber listrik (USB 5V atau baterai 9V)

> 🧩 **Analogi:** Sensor itu seperti **indera** (mata, telinga, hidung manusia), aktuator itu seperti **otot** (tangan, kaki), dan Arduino adalah **otak**-nya.

### 🔍 Cek Pemahaman
1. Apa perbedaan fungsi sensor dan aktuator?
2. Sebutkan 3 contoh sensor dan apa yang dideteksinya!
3. Apa fungsi breadboard dalam merangkai komponen Arduino?

### 📋 Studi Kasus
**Membuat Alarm Kebakaran Sederhana**

Siswa kelas XII ingin membuat alarm kebakaran untuk laboratorium komputer. Mereka menggunakan sensor MQ-2 (pendeteksi asap), buzzer sebagai aktuator, dan Arduino Uno. Saat sensor mendeteksi konsentrasi gas di atas ambang batas, buzzer akan berbunyi nyaring dan LED merah menyala.

*Pertanyaan:*
1. Identifikasi mana sensor dan mana aktuator dalam sistem ini!
2. Komponen pendukung apa saja yang dibutuhkan untuk merangkai sistem ini?

> 🤔 **Mari Renungkan:** Apa hal paling menarik yang kamu pelajari dari bagian ini?

---

## E. Simulator Arduino

### 🎮 Simulator Arduino
Tidak punya Arduino fisik? **Tidak masalah!** Kamu bisa pakai simulator online GRATIS untuk belajar merangkai dan memprogram Arduino.

### 🏆 Rekomendasi Simulator
| Simulator | Kelebihan | Link |
|-----------|-----------|------|
| **Wokwi** | Cepat, banyak komponen, integrasi GitHub | wokwi.com |
| **Tinkercad** | Visual 3D, cocok pemula | tinkercad.com |
| **SimulIDE** | Offline, ringan | simufor.com |

### Contoh di Wokwi
```
  ┌──────────────────────────────────────────────┐
  │  Wokwi Online Simulator  [Run] [Save]       │
  ├──────────────┬───────────────────────────────┤
  │              │                               │
  │  [ARDUINO]   │  void setup() {               │
  │   UNO        │    pinMode(2, OUTPUT);        │
  │              │  }                            │
  │  ┌─┐ ┌─┐    │  void loop() {                │
  │  │█│ │█│    │    digitalWrite(2, HIGH);     │
  │  └─┘ └─┘    │    delay(500);                │
  │  LED LED    │    digitalWrite(2, LOW);      │
  │              │    delay(500);                │
  │  [GND] [5V] │  }                             │
  ├──────────────┴───────────────────────────────┤
  │  ✅ LED menyala berkedip setiap 500ms        │
  └──────────────────────────────────────────────┘
```

> 💡 **Tips:** Gunakan simulator untuk eksperimen! Kalau salah rangkai, tinggal undo — tidak ada komponen yang meledak 😄

### 🔍 Cek Pemahaman
1. Sebutkan 3 simulator Arduino yang bisa digunakan!
2. Apa kelebihan menggunakan simulator dibanding Arduino fisik?
3. Mana yang lebih cocok untuk pemula, Wokwi atau Tinkercad? Mengapa?

### 📋 Studi Kasus
**Belajar Arduino Tanpa Modal**

Dika ingin belajar Arduino tapi tidak punya uang untuk membeli perangkat. Temannya menyarankan untuk menggunakan Wokwi (simulator online gratis). Dika bisa merangkai LED, menulis kode, dan melihat hasilnya langsung — semua dari browser laptop sekolah. Dalam seminggu, Dika sudah bisa membuat 5 proyek berbeda tanpa merogoh kocek sepeser pun.

*Pertanyaan:*
1. Apa keuntungan belajar Arduino dengan simulator menurut kasus Dika?
2. Apakah ada kekurangan belajar hanya dengan simulator? Jelaskan!

> 🤔 **Mari Renungkan:** Apa hal paling menarik yang kamu pelajari dari bagian ini?

---

## F. Praktik: LED & Sensor

### 🔦 Praktik: LED & Sensor Sederhana

### Praktik 1: LED Berkedip
**Alat:** Arduino, LED, Resistor 220 Ohm, Kabel Jumper, Breadboard

**Rangkaian:**
```
        Arduino UNO
    ┌──────────────────┐
    │                  │
    │  Pin 13 ──► LED(+)│
    │                  │        ┌──────┐
    │          LED(-)──┼────────┤220Ω  ├──► GND
    │                  │        └──────┘
    │  GND  ──────────┤
    └──────────────────┘
```

**Program:**
```cpp
void setup() {
  pinMode(13, OUTPUT);
}
void loop() {
  digitalWrite(13, HIGH);
  delay(1000);
  digitalWrite(13, LOW);
  delay(1000);
}
```

### Praktik 2: Baca Sensor Suhu LM35
**Alat:** Arduino, LM35, Breadboard, Kabel Jumper

**Program:**
```cpp
void setup() {
  Serial.begin(9600);  // Mulai komunikasi serial
}
void loop() {
  int nilai = analogRead(A0);
  float suhu = (nilai * 5.0 / 1024.0) * 100;
  Serial.print("Suhu: ");
  Serial.print(suhu);
  Serial.println(" °C");
  delay(1000);
}
```

> 🔑 **Catatan:** `analogRead()` membaca nilai 0-1023 dari pin analog. Kita konversi ke suhu dengan rumus: Suhu = (nilai x 5V / 1024) x 100

### 🔍 Cek Pemahaman
1. Apa fungsi resistor 220 Ohm pada rangkaian LED?
2. Rumus apa yang digunakan untuk mengkonversi nilai analog ke suhu?
3. Apa perbedaan `digitalWrite()` dan `analogRead()`?

### 📋 Studi Kasus
**Suhu Lab Komputer Terlalu Panas**

Laboratorium komputer SMA Merdeka sering terasa panas karena 30 komputer menyala bersamaan. Tim informatika ingin memonitor suhu ruangan secara real-time. Mereka menggunakan Arduino + sensor LM35 untuk membaca suhu dan menampilkannya di Serial Monitor. Data suhu dicatat setiap 5 menit selama seminggu untuk mengetahui pola kenaikan suhu.

*Pertanyaan:*
1. Komponen apa saja yang dibutuhkan untuk proyek monitoring suhu ini?
2. Bagaimana cara menghubungkan LM35 ke Arduino?

> 🤔 **Mari Renungkan:** Apa hal paling menarik yang kamu pelajari dari bagian ini?

---

## G. Proyek Mini: Monitoring Suhu

### 🌡️ Proyek Mini: Sistem Monitoring Suhu

**Tujuan:** Membuat alat yang bisa mengukur suhu ruangan dan menyalakan LED berbeda sesuai rentang suhu.

**Alat & Bahan:** Arduino Uno, Sensor LM35/DHT11, LED (Hijau, Kuning, Merah), Resistor 220 Ohm (x3), Breadboard & Kabel Jumper

**Cara Kerja:**
```
  Suhu < 28°C  →  LED HIJAU nyala (sejuk)
  28°C - 33°C  →  LED KUNING nyala (normal)
  Suhu > 33°C  →  LED MERAH nyala (panas!)
```

**Program:**
```cpp
int ledHijau = 9, ledKuning = 10, ledMerah = 11;
void setup() {
  Serial.begin(9600);
  pinMode(ledHijau, OUTPUT);
  pinMode(ledKuning, OUTPUT);
  pinMode(ledMerah, OUTPUT);
}
void loop() {
  int nilai = analogRead(A0);
  float suhu = (nilai * 5.0 / 1024.0) * 100;
  Serial.print("Suhu: "); Serial.println(suhu);
  if (suhu < 28) {
    digitalWrite(ledHijau, HIGH);
    digitalWrite(ledKuning, LOW);
    digitalWrite(ledMerah, LOW);
  } else if (suhu <= 33) {
    digitalWrite(ledHijau, LOW);
    digitalWrite(ledKuning, HIGH);
    digitalWrite(ledMerah, LOW);
  } else {
    digitalWrite(ledHijau, LOW);
    digitalWrite(ledKuning, LOW);
    digitalWrite(ledMerah, HIGH);
  }
  delay(1000);
}
```

> 💡 **Kembangkan!** Tambahkan buzzer yang berbunyi kalau suhu > 35°C!

### 🔍 Cek Pemahaman
1. Berapa rentang suhu untuk LED hijau, kuning, dan merah pada proyek ini?
2. Apa yang terjadi jika suhu melebihi 33°C?
3. Bagaimana cara menambahkan buzzer ke proyek ini?

### 📋 Studi Kasus
**Greenhouse Anggrek Sekolah**

SMA Tani Mandiri memiliki greenhouse anggrek yang membutuhkan suhu stabil 25-30°C. Siswa kelas XII membuat sistem monitoring suhu menggunakan Arduino dan sensor DHT11. Jika suhu di bawah 25°C, kipas pemanas menyala. Jika suhu di atas 30°C, kipas pendingin menyala. Semua data terekam di komputer selama 24 jam.

*Pertanyaan:*
1. Modifikasi apa yang perlu dilakukan dari proyek mini monitoring suhu biasa untuk kasus greenhouse ini?
2. Mengapa penting menjaga suhu stabil untuk tanaman anggrek?

> 🤔 **Mari Renungkan:** Apa hal paling menarik yang kamu pelajari dari bagian ini?

---

---
## 🏗️ Proyek Mini: 💡 Rangkaian Arduino: Lampu Otomatis

Buat rangkaian LED yang menyala otomatis saat gelap menggunakan sensor cahaya (LDR) dan Arduino. Proyek ini mengajarkan konsep input sensor, logika percabangan, dan output aktuator. Rangkaian bisa disimulasikan di Tinkercad jika tidak punya Arduino fisik.

**Alat dan Bahan:**
- Arduino Uno
- Sensor LDR
- LED 5mm
- Resistor 220 Ohm dan 10k Ohm
- Kabel Jumper
- Breadboard
- Tinkercad Circuits (alternatif simulator)

**Langkah-langkah:**
1. Rangkai sensor LDR dengan resistor 10k Ohm membentuk voltage divider, hubungkan ke pin A0
2. Rangkai LED dengan resistor 220 Ohm, hubungkan anoda ke pin 9 dan katoda ke GND
3. Tulis program: baca nilai analog dari LDR pakai `analogRead(A0)`, jika nilai < 500 (gelap) LED nyala, jika >= 500 (terang) LED mati
4. Upload program ke Arduino atau jalankan di simulator
5. Uji coba: tutup sensor LDR dengan tangan — LED harus menyala; buka — LED harus mati
6. Dokumentasikan rangkaian dan hasil pengujian dalam bentuk foto/video

> **Output:** Rangkaian LED otomatis fungsional + dokumentasi (foto/video + kode program)

## 📝 Rangkuman

1. SBC (Single Board Computer) seperti Raspberry Pi bisa menjalankan OS dan cocok untuk tugas berat, sedangkan mikrokontroler seperti Arduino lebih hemat daya untuk tugas spesifik.
2. Arduino adalah platform prototyping elektronik open-source yang mudah dipelajari, murah, dan memiliki komunitas besar.
3. IDE Arduino adalah software untuk menulis, meng-compile, dan mengupload program — struktur dasarnya terdiri dari setup() dan loop().
4. Komponen penunjang Arduino meliputi sensor (mendeteksi), aktuator (melakukan aksi), dan komponen pendukung seperti breadboard, kabel jumper, dan resistor.
5. Simulator seperti Wokwi dan Tinkercad memungkinkan belajar Arduino tanpa hardware fisik — cocok untuk eksperimen awal.
6. Praktik dasar meliputi menyalakan LED dan membaca sensor suhu LM35 dengan rumus konversi Suhu = (nilai × 5V / 1024) × 100.

---

## ✍️ Latihan Soal

### A. Pilihan Ganda

1. Perbedaan utama antara SBC (Single Board Computer) dan Mikrokontroler adalah…
   a. SBC lebih murah
   b. SBC bisa menjalankan OS, mikrokontroler tidak
   c. Mikrokontroler lebih cepat
   d. SBC tidak punya GPIO
   e. Mikrokontroler punya HDMI
   **Jawaban: SBC bisa menjalankan OS, mikrokontroler tidak**

2. Arduino Uno menggunakan mikrokontroler jenis…
   a. ESP32
   b. ATmega328P
   c. ATmega2560
   d. STM32
   e. Raspberry Pi
   **Jawaban: ATmega328P**

3. Fungsi `pinMode(13, OUTPUT)` dalam program Arduino digunakan untuk…
   a. Membaca data dari pin 13
   b. Mengatur pin 13 sebagai output
   c. Menyalakan LED di pin 13
   d. Mematikan pin 13
   e. Mengirim data serial
   **Jawaban: Mengatur pin 13 sebagai output**

4. Komponen yang berfungsi mendeteksi perubahan lingkungan seperti suhu atau cahaya disebut…
   a. Aktuator
   b. Resistor
   c. Breadboard
   d. Sensor
   e. Kabel jumper
   **Jawaban: Sensor**

5. Fungsi `analogRead(A0)` pada Arduino menghasilkan nilai antara…
   a. 0–1
   b. 0–255
   c. 0–1023
   d. 0–5000
   e. 1–100
   **Jawaban: 0–1023**

### B. Uraian

1. Bandingkan SBC (Single Board Computer) dengan mikrokontroler dari segi OS, konsumsi daya, dan kegunaan!

2. Jelaskan langkah-langkah membuat program LED berkedip di Arduino! Mulai dari rangkaian hingga kode program.

3. Apa fungsi sensor LM35 dan bagaimana cara membaca nilainya di program Arduino? Jelaskan dengan rumus konversinya!

4. Jelaskan perbedaan antara sensor dan aktuator. Berikan 3 contoh masing-masing!

---
## 📋 Rubrik Penilaian Proyek

| Aspek | Kurang | Cukup | Baik |
|-------|--------|-------|------|
| Perangkaian Hardware | Rangkaian salah, komponen tidak terpasang benar | Rangkaian benar tapi kurang rapi | Rangkaian rapi dan benar sesuai skema |
| Kebenaran Program | Program tidak sesuai spesifikasi, error | Program berjalan dengan beberapa bug | Program benar, efisien, dan bebas error |
| Fungsionalitas Alat | Alat tidak berfungsi sama sekali | Alat berfungsi sebagian atau kadang error | Alat berfungsi sempurna sesuai spesifikasi |
| Dokumentasi | Tidak ada dokumentasi | Dokumentasi ada tapi kurang lengkap | Dokumentasi lengkap (foto, video, kode program) |

---
## 🚀 Tugas Pengayaan

### 🔧 Proyek Tambahan: Alarm Suhu dengan Buzzer
Kembangkan rangkaian lampu otomatis dengan menambahkan buzzer yang berbunyi jika suhu melebihi 35°C. Gunakan sensor suhu LM35/DHT11 dan buzzer piezo. Buat 3 level: suhu normal (LED hijau), waspada (LED kuning), bahaya (LED merah + buzzer). Dokumentasikan dalam bentuk video singkat.

---
## 📖 Glosarium

- **SBC (Single Board Computer)**: Komputer lengkap dalam satu papan sirkuit, seperti Raspberry Pi.
- **Mikrokontroler**: Chip tunggal yang berfungsi sebagai pengontrol sistem elektronik, seperti Arduino.
- **Arduino**: Platform prototyping elektronik open-source berbasis mikrokontroler.
- **IDE Arduino**: Lingkungan pengembangan terintegrasi untuk menulis dan mengupload kode ke Arduino.
- **GPIO**: General Purpose Input Output — pin pada SBC/mikrokontroler untuk koneksi komponen eksternal.
- **Sensor**: Komponen yang mendeteksi perubahan fisik (suhu, cahaya, gerak) dan mengubahnya menjadi sinyal listrik.
- **PWM**: Pulse Width Modulation — teknik mengatur daya dengan variasi lebar pulsa.

---
## 📺 Sumber & Media Pembelajaran

| Platform | Sumber | Tautan | Keterangan |
|----------|--------|--------|------------|
| YouTube | Apa itu Arduino? | `youtu.be/search?q=pengenalan+arduino+indonesia` | Pengenalan Arduino oleh komunitas Indonesia |
| Simulasi | Tinkercad Circuits | `https://www.tinkercad.com/circuits` | Simulator Arduino online gratis |
| Website | Arduino Project Hub | `https://projecthub.arduino.cc/` | Koleksi proyek Arduino dari seluruh dunia |
| YouTube | Belajar C untuk Arduino | `youtu.be/search?q=dasar+program+C+arduino` | Tutorial dasar pemrograman Arduino |
| Website | Random Nerd Tutorials | `https://randomnerdtutorials.com/` | Tutorial Arduino dan ESP8266/ESP32 |
