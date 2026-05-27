# 🧠 Bab 3: Berpikir Komputasional dan Algoritma Pemrograman

> **Semester Ganjil** | **Fase F** | **Kelas XII** | **35 JP**

---

---
## 📊 Pemetaan Capaian Pembelajaran

| Elemen CP | Deskripsi CP |
|-----------|-------------|
| Berpikir Komputasional | Peserta didik mampu menerapkan berpikir komputasional (dekomposisi, pengenalan pola, abstraksi, algoritma) untuk memecahkan masalah sehari-hari. |
| Algoritma dan Pemrograman | Peserta didik mampu menulis program dalam bahasa C untuk Arduino yang mencakup variabel, percabangan, perulangan, array, dan fungsi. |

## 🎯 Tujuan Pembelajaran

- **A.** Mengapa Berpikir Komputasional?
- **B.** Dasar Pemrograman C untuk Arduino
- **C.** Struktur Dasar Program C
- **D.** Percabangan & Perulangan
- **E.** Array: Kumpulan Data
- **F.** Fungsi & Library Arduino
- **G.** Proyek: Kontrol Otomatis

## 🗺️ Peta Konsep

```
               🧠 BERPIKIR KOMPUTASIONAL DAN ALGORITMA PEMROGRAMAN
                     |
                     ├── A. Mengapa Berpikir Komputasional?
                     ├── B. Dasar Pemrograman C untuk Arduino
                     ├── C. Struktur Dasar Program C
                     ├── D. Percabangan & Perulangan
                     ├── E. Array: Kumpulan Data
                     ├── F. Fungsi & Library Arduino
                     └── G. Proyek: Kontrol Otomatis
```

## A. Mengapa Berpikir Komputasional?

### 🧠 Mengapa Berpikir Komputasional?
Berpikir Komputasional (BK) adalah **cara berpikir untuk memecahkan masalah** dengan menerapkan **konsep dan logika ilmu komputer**.

> 🧩 **Analogi:** BK itu seperti resep masakan. Kalau kamu punya resep yang jelas, langkah demi langkah, siapa pun bisa memasak hidangan yang sama. BK memberi kita resep untuk memecahkan masalah!

### 4 Pilar Berpikir Komputasional
```
  ┌──────────────────────────────────────────────┐
  │        BERPIKIR KOMPUTASIONAL                │
  ├──────────────────┬───────────────────────────┤
  │  1. DEKOMPOSISI  │ Memecah masalah besar     │
  │                  │ menjadi bagian kecil      │
  ├──────────────────┼───────────────────────────┤
  │  2. PENGENALAN   │ Mencari pola/kesamaan     │
  │     POLA         │ dari masalah              │
  ├──────────────────┼───────────────────────────┤
  │  3. ABSTRAKSI    │ Fokus pada yang penting,  │
  │                  │ abaikan yang tidak perlu  │
  ├──────────────────┼───────────────────────────┤
  │  4. ALGORITMA    │ Membuat langkah-langkah   │
  │                  │ penyelesaian              │
  └──────────────────┴───────────────────────────┘
```

### Contoh Sehari-hari
**Masalah:** Mau masak nasi goreng untuk 5 orang.
1. **Dekomposisi:** Beli bahan -> siapkan bumbu -> masak -> sajikan
2. **Pola:** Sama seperti masak mie goreng, cuma beda bahan
3. **Abstraksi:** Ukuran wajan, warna panci tidak penting; yang penting api, bumbu, nasi
4. **Algoritma:** Langkah 1: Panaskan minyak. 2: Tumis bumbu. 3: Masukkan nasi...

### 🔍 Cek Pemahaman
1. Sebutkan 4 pilar berpikir komputasional!
2. Terapkan 4 pilar BK untuk masalah "Bangun pagi dan berangkat sekolah"!
3. Mengapa abstraksi penting dalam pemecahan masalah?

### 📋 Studi Kasus
**Memecahkan Masalah Parkir Sekolah**

Setiap pagi, terjadi kemacetan di pintu gerbang SMA Harapan karena banyak mobil dan motor parkir sembarangan. OSIS diminta membantu mencari solusi. Mereka menggunakan berpikir komputasional:
- **Dekomposisi:** masalah parkir → jumlah kendaraan, luas lahan, jadwal kedatangan
- **Pola:** kendaraan datang paling banyak pukul 06.30-07.00
- **Abstraksi:** fokus pada pengaturan alur masuk, bukan pada warna kendaraan
- **Algoritma:** buat sistem parkir bergilir per kelas

*Pertanyaan:*
1. Jelaskan bagaimana setiap pilar BK diterapkan dalam kasus ini!
2. Usulkan solusi algoritma yang lebih detail untuk masalah parkir sekolah!

> 🤔 **Mari Renungkan:** Apa hal paling menarik yang kamu pelajari dari bagian ini?

---

## B. Dasar Pemrograman C untuk Arduino

### 💻 Dasar Pemrograman C untuk Arduino
Bahasa C adalah **bahasa pemrograman level menengah** yang cepat, efisien, dan sangat cocok untuk Arduino.

> 🧩 **Analogi:** Bahasa C itu seperti bahasa isyarat untuk Arduino. Kamu memberi instruksi dengan kode-kode tertentu, dan Arduino menjalankannya tanpa bertanya lagi.

### Struktur Program Arduino
```cpp
void setup() {
  // Kode di sini jalan SEKALI saat Arduino dinyalakan
  pinMode(13, OUTPUT);  // Set pin 13 sebagai output
}
void loop() {
  // Kode di sini jalan TERUS-MENERUS
  digitalWrite(13, HIGH);
  delay(1000);
  digitalWrite(13, LOW);
  delay(1000);
}
```

### Penjelasan
| Bagian | Fungsi | Analogi |
|--------|--------|---------|
| `void setup()` | Persiapan awal (1x) | Seperti menyiapkan meja sebelum masak |
| `void loop()` | Program utama (berulang) | Seperti kegiatan rutin harian |
| `pinMode(pin, mode)` | Set fungsi pin | Menentukan mana saklar, mana lampu |
| `digitalWrite(pin, value)` | Output ON/OFF | Menyalakan/mematikan saklar |
| `delay(ms)` | Jeda waktu | Berhenti sejenak (1000 = 1 detik) |

### 🔍 Cek Pemahaman
1. Sebutkan 2 fungsi utama dalam setiap program Arduino!
2. Apa perbedaan `setup()` dan `loop()`?
3. Fungsi apa yang digunakan untuk memberikan jeda 2 detik?

### 📋 Studi Kasus
**Lampu Kedip Morse**

Daffa ingin membuat lampu LED mengirim pesan SOS dalam kode Morse menggunakan Arduino (S = tiga kedip pendek, O = tiga kedip panjang). Ia menggunakan kombinasi `digitalWrite` dan `delay` dengan durasi berbeda. Kode SOS sudah ditentukan: pendek 200ms, panjang 600ms.

*Pertanyaan:*
1. Tulis kode Arduino untuk menghasilkan 1 kali kedip pendek (200ms)!
2. Bagaimana cara membuat urutan SOS (3 pendek, 3 panjang, 3 pendek)?

> 🤔 **Mari Renungkan:** Apa hal paling menarik yang kamu pelajari dari bagian ini?

---

## C. Struktur Dasar Program C

### 📋 Struktur Dasar Program C

### 1. Variabel — Tempat Menyimpan Data
```cpp
int umur = 17;           // Bilangan bulat
float suhu = 28.5;       // Bilangan desimal
char inisial = 'D';      // Satu karakter
boolean menyala = true;  // true/false
String nama = "Dani";    // Teks
```

### 2. Tipe Data
| Tipe | Ukuran | Simpan | Contoh |
|------|--------|--------|--------|
| `byte` | 1 byte | 0 - 255 | `byte nilai = 100;` |
| `int` | 2 byte | -32.768 - 32.767 | `int jumlah = 500;` |
| `long` | 4 byte | -2M - 2M | `long waktu = 60000;` |
| `float` | 4 byte | Desimal | `float pi = 3.14;` |
| `boolean` | 1 bit | true/false | `boolean ok = true;` |

### 3. Operator Dasar
```cpp
int a = 10, b = 3;
int hasil = a + b;    // 13  (penjumlahan)
hasil = a - b;         // 7   (pengurangan)
hasil = a * b;         // 30  (perkalian)
hasil = a / b;         // 3   (pembagian BULAT)
hasil = a % b;         // 1   (sisa bagi / modulo)
boolean cek = (a > b);  // true
```

### 🔍 Cek Pemahaman
1. Sebutkan 3 tipe data dalam C dan contohnya!
2. Apa yang dimaksud dengan operator modulo (`%`)? Berikan contoh!
3. Berapa nilai dari `10 / 3` dalam pembagian bilangan bulat (int)?

### 📋 Studi Kasus
**Kalkulator Nilai Rata-rata**

Anita ingin membuat program Arduino yang menghitung rata-rata dari 3 nilai ulangannya: 85, 92, dan 78. Ia menggunakan variabel `int` untuk menyimpan nilai, lalu menjumlahkannya dan membagi dengan 3. Namun hasilnya selalu bilangan bulat, padahal nilai aslinya mengandung koma.

*Pertanyaan:*
1. Tipe data apa yang seharusnya digunakan Anita agar hasil rata-rata akurat?
2. Tulis kode C yang benar untuk menghitung rata-rata 85, 92, dan 78!

> 🤔 **Mari Renungkan:** Apa hal paling menarik yang kamu pelajari dari bagian ini?

---

## D. Percabangan & Perulangan

### 🔀 Percabangan & Perulangan

### A. Percabangan: if / else if / else
Digunakan kalau ada kondisi (pilihan).
```cpp
int nilai = 85;
if (nilai >= 90) {
  Serial.println("A — Istimewa!");
} else if (nilai >= 78) {
  Serial.println("B — Baik!");
} else if (nilai >= 65) {
  Serial.println("C — Cukup");
} else {
  Serial.println("D — Remedial");
}
```

### B. Perulangan: for & while
**for** — dipakai kalau sudah tahu berapa kali ulang:
```cpp
for (int i = 0; i < 5; i++) {
  Serial.print("Halo ke-");
  Serial.println(i);
  delay(500);
}
```

**while** — dipakai kalau tidak tahu kapan berhenti:
```cpp
while (digitalRead(2) == HIGH) {
  digitalWrite(13, HIGH);
}
```

> 🧩 **Analogi:** `for` itu seperti daftar belanja — kamu tahu ada 5 barang yang harus dibeli. `while` itu seperti mengaduk mie sampai matang — kamu tidak tahu berapa kali harus aduk, yang penting sampai matang!

### 🔍 Cek Pemahaman
1. Kapan sebaiknya menggunakan `if` dibanding `else if`?
2. Kapan menggunakan `for` dan kapan menggunakan `while`?
3. Buat kode `for` untuk mencetak angka 1 sampai 10!

### 📋 Studi Kasus
**Sistem Penyiraman Tanaman Otomatis**

Sinta membuat penyiram tanaman otomatis dengan Arduino. Sensor kelembaban tanah membaca nilai: jika < 300 (kering), pompa air menyala. Jika >= 300 (basah), pompa mati. Setelah menyiram, program menunggu 5 detik sebelum membaca sensor lagi (menggunakan `while` untuk menunggu).

*Pertanyaan:*
1. Struktur percabangan apa yang tepat untuk logika di atas? Tulis kodenya!
2. Mengapa perlu jeda 5 detik setelah menyiram?

> 🤔 **Mari Renungkan:** Apa hal paling menarik yang kamu pelajari dari bagian ini?

---

## E. Array: Kumpulan Data

### 📦 Array: Kumpulan Data
Array adalah **variabel yang bisa menyimpan banyak data sekaligus**, dengan tipe yang sama.

> 🧩 **Analogi:** Array itu seperti rak sepatu. Satu rak bisa menyimpan banyak sepatu, dan setiap sepatu punya nomor rak (indeks). **Indeks array mulai dari 0!**

### Deklarasi Array
```cpp
int angka[] = {10, 20, 30, 40, 50};
int suhu[7];  // Bisa simpan 7 suhu
suhu[0] = 28;
suhu[1] = 29;
String namaHari[] = {"Senin", "Selasa", "Rabu"};
```

### Cara Kerja Array
```
        indeks:   0     1     2     3     4
               ┌─────┬─────┬─────┬─────┬─────┐
        angka: │ 10  │ 20  │ 30  │ 40  │ 50  │
               └─────┴─────┴─────┴─────┴─────┘
  int x = angka[0];    // x = 10
  angka[2] = 100;      // Ubah indeks 2 jadi 100
```

### Contoh: LED Berjalan (Cylon)
```cpp
int ledPins[] = {2, 3, 4, 5, 6, 7};
void setup() {
  for (int i = 0; i < 6; i++) pinMode(ledPins[i], OUTPUT);
}
void loop() {
  for (int i = 0; i < 6; i++) { digitalWrite(ledPins[i], HIGH); delay(200); digitalWrite(ledPins[i], LOW); }
  for (int i = 5; i >= 0; i--) { digitalWrite(ledPins[i], HIGH); delay(200); digitalWrite(ledPins[i], LOW); }
}
```

### 🔍 Cek Pemahaman
1. Apa itu array dan mengapa kita membutuhkannya?
2. Dari indeks berapa array dimulai?
3. Buat array untuk menyimpan 7 hari dalam seminggu!

### 📋 Studi Kasus
**Lampu Hias 8 LED untuk Class Meeting**

Class meeting akan datang! Dimas ingin membuat lampu hias dengan 8 LED yang menyala bergantian. Ia menggunakan array `int ledPins[] = {2,3,4,5,6,7,8,9}` dan perulangan `for` untuk menyalakan LED satu per satu. Pola yang diinginkan: LED menyala dari kiri ke kanan, lalu kanan ke kiri, berulang terus.

*Pertanyaan:*
1. Tulis kode perulangan `for` untuk menyalakan 8 LED dari kiri ke kanan!
2. Bagaimana cara membuat efek "pantul" (kiri→kanan→kiri)?

> 🤔 **Mari Renungkan:** Apa hal paling menarik yang kamu pelajari dari bagian ini?

---

## F. Fungsi & Library Arduino

### 📚 Fungsi & Library Arduino

### A. Fungsi — Memecah Program Jadi Bagian Kecil
Fungsi adalah blok kode yang bisa dipanggil berulang kali. Ini membuat program lebih rapi.

> 🧩 **Analogi:** Fungsi itu seperti tombol di remote TV. Kamu tidak perlu tahu rangkaian elektronik di dalamnya. Tinggal tekan, dan TV ganti channel.

### Cara Membuat Fungsi
```cpp
void nyalakanLED(int pin, int durasi) {
  digitalWrite(pin, HIGH);
  delay(durasi);
  digitalWrite(pin, LOW);
}
float konversiKeCelcius(int nilaiAnalog) {
  float volt = nilaiAnalog * 5.0 / 1024.0;
  return volt * 100;
}
void loop() {
  nyalakanLED(13, 1000);
  int baca = analogRead(A0);
  float suhu = konversiKeCelcius(baca);
  Serial.println(suhu);
}
```

### B. Library Arduino
Library adalah kumpulan fungsi siap pakai. Kamu tinggal pakai, tidak perlu buat dari nol.

| Library | Fungsi | Contoh |
|---------|--------|--------|
| `LiquidCrystal` | Mengontrol LCD | Tampilkan teks di LCD |
| `Servo` | Mengontrol motor servo | Gerakkan lengan robot |
| `DHT` | Baca sensor suhu & kelembaban | DHT11/DHT22 |
| `WiFi` (ESP32) | Koneksi WiFi | IoT, kirim data ke internet |

```cpp
#include <Servo.h>
Servo myservo;
void setup() { myservo.attach(9); }
void loop() {
  myservo.write(0); delay(1000);
  myservo.write(90); delay(1000);
  myservo.write(180); delay(1000);
}
```

> 💡 **Tips:** Cari library di **Library Manager** Arduino IDE: Sketch > Include Library > Manage Libraries

### 🔍 Cek Pemahaman
1. Apa itu fungsi dalam pemrograman?
2. Sebutkan 3 library Arduino dan fungsinya!
3. Apa keuntungan menggunakan library dibanding menulis kode dari nol?

### 📋 Studi Kasus
**Robot Arm Sederhana**

Tim robotik SMA menggunakan servo motor untuk membuat lengan robot sederhana. Mereka menggunakan library `Servo.h` agar lebih mudah mengontrol servo. Tanpa library, mereka harus mengatur pulsa PWM secara manual — sangat rumit! Dengan `myservo.write(90)`, servo langsung bergerak ke posisi 90 derajat.

*Pertanyaan:*
1. Apa library yang digunakan dan mengapa?
2. Tulis kode untuk menggerakkan servo dari 0° → 90° → 180° dengan jeda 1 detik!

> 🤔 **Mari Renungkan:** Apa hal paling menarik yang kamu pelajari dari bagian ini?

---

## G. Proyek: Kontrol Otomatis

### 🏗️ Proyek: Kontrol Otomatis

**Tugas Akhir Bab 3:** Buatlah program Arduino yang menggabungkan semua konsep: variabel, percabangan, perulangan, array, fungsi, dan library!

### 💡 Ide Proyek (Pilih satu)
1. **🌡️ Smart Fan** — Kipas otomatis menyala kalau suhu > 30°C
2. **🚦 Lampu Lalu Lintas** — 3 LED hijau/kuning/merah dengan timer
3. **💧 Penyiram Tanaman** — Siram otomatis kalau tanah kering
4. **🚪 Sistem Keamanan** — Buzzer bunyi kalau ada gerakan (PIR sensor)

### Format Laporan
| Bagian | Isi |
|--------|----|
| Judul | Nama proyek |
| Tujuan | Masalah apa yang diselesaikan? |
| Alat & Bahan | Komponen yang digunakan |
| Rangkaian | Diagram/skema |
| Kode Program | Dengan komentar |
| Hasil | Video/foto/gambar |
| Refleksi | Kesulitan & pembelajaran |

### 🔍 Cek Pemahaman
1. Sebutkan 4 ide proyek yang bisa dipilih untuk tugas akhir Bab 3!
2. Apa saja yang harus ada dalam laporan proyek?
3. Mengapa refleksi penting dalam sebuah proyek?

### 📋 Studi Kasus
**Smart Fan untuk Kamar Adik**

Kakak beradik kelas XII membuat kipas otomatis yang menyala saat suhu > 30°C. Mereka menggunakan sensor DHT11, relay, dan kipas DC bekas komputer. Mereka menerapkan fungsi `bacaSuhu()` untuk membaca sensor, dan percabangan `if (suhu > 30)` untuk menyalakan kipas. Hasilnya: adik mereka tidak perlu bangun untuk menyalakan kipas saat malam panas.

*Pertanyaan:*
1. Identifikasi semua konsep Bab 3 yang digunakan dalam proyek ini!
2. Perbaikan apa yang bisa ditambahkan untuk membuat proyek ini lebih baik?

> 🤔 **Mari Renungkan:** Apa hal paling menarik yang kamu pelajari dari bagian ini?

---

---
## 🏗️ Proyek Mini: 🚦 Program Arduino: Traffic Light

Buat program traffic light (lampu lalu lintas) sederhana menggunakan 3 LED (merah, kuning, hijau) di Arduino/Tinkercad. Proyek ini melatih pemahaman tentang perulangan, fungsi, dan timing dalam pemrograman Arduino.

**Alat dan Bahan:**
- Arduino Uno
- LED Merah, Kuning, Hijau
- Resistor 220 Ohm (x3)
- Kabel Jumper
- Breadboard
- Tinkercad Circuits (alternatif simulator)

**Langkah-langkah:**
1. Rangkai 3 LED ke pin digital 10 (merah), 9 (kuning), 8 (hijau) masing-masing dengan resistor 220 Ohm
2. Buat fungsi `nyalakanLED(int merah, int kuning, int hijau)` untuk mengatur nyala/mati LED dengan parameter ON/OFF
3. Buat fungsi `trafficLightCycle()` dengan urutan: Hijau 5 detik → Kuning 2 detik → Merah 5 detik → Kuning 2 detik
4. Panggil `trafficLightCycle()` di dalam `loop()`
5. Upload program ke Arduino atau jalankan di simulator
6. Uji coba: pastikan urutan dan durasi LED sesuai yang diharapkan

> **Output:** Simulasi traffic light 3 LED berjalan dengan urutan dan timing yang benar

## 📝 Rangkuman

1. Berpikir komputasional memiliki 4 pilar: Dekomposisi (memecah masalah), Pengenalan Pola, Abstraksi (fokus pada hal penting), dan Algoritma (langkah penyelesaian).
2. Struktur program Arduino terdiri dari setup() yang dijalankan sekali dan loop() yang berjalan terus-menerus.
3. Variabel menyimpan data dengan berbagai tipe: int, float, boolean, char, String — dan operator aritmatika serta logika digunakan untuk mengolahnya.
4. Percabangan (if/else) digunakan untuk pengambilan keputusan; perulangan (for/while) untuk mengulang eksekusi kode.
5. Array adalah struktur data yang menyimpan banyak nilai dengan tipe yang sama dan diakses menggunakan indeks (mulai dari 0).
6. Fungsi membuat program lebih terstruktur dengan memecah kode menjadi blok yang bisa dipanggil berulang; library menyediakan fungsi siap pakai seperti LiquidCrystal, Servo, dan DHT.

---

## ✍️ Latihan Soal

### A. Pilihan Ganda

1. Memecah masalah besar menjadi bagian-bagian kecil adalah pilar berpikir komputasional yang disebut…
   a. Pengenalan Pola
   b. Abstraksi
   c. Algoritma
   d. Dekomposisi
   e. Evaluasi
   **Jawaban: Dekomposisi**

2. Struktur program Arduino terdiri dari…
   a. input() dan output()
   b. start() dan end()
   c. setup() dan loop()
   d. begin() dan run()
   e. init() dan process()
   **Jawaban: setup() dan loop()**

3. Perhatikan kode berikut:

int a = 10, b = 3;
int hasil = a % b;

Nilai dari variabel `hasil` adalah…
   a. 3
   b. 7
   c. 1
   d. 10
   e. 13
   **Jawaban: 1**

4. Perulangan `for` cocok digunakan ketika…
   a. Tidak tahu kapan berhenti
   b. Sudah tahu berapa kali akan mengulang
   c. Hanya mengulang sekali
   d. Tidak perlu mengulang
   e. Ingin mengulang tanpa syarat
   **Jawaban: Sudah tahu berapa kali akan mengulang**

5. Fungsi dalam pemrograman berguna untuk…
   a. Memperlambat program
   b. Memecah program jadi bagian kecil yang bisa dipanggil berulang
   c. Menghapus variabel
   d. Mengganti nama file
   e. Mengulang program tanpa henti
   **Jawaban: Memecah program jadi bagian kecil yang bisa dipanggil berulang**

### B. Uraian

1. Jelaskan 4 pilar berpikir komputasional dan berikan contoh penerapannya dalam kehidupan sehari-hari!

2. Apa perbedaan antara `for` dan `while` dalam pemrograman C? Kapan sebaiknya menggunakan masing-masing?

3. Buatlah program Arduino sederhana menggunakan array untuk menyalakan 6 LED secara bergantian!

4. Jelaskan manfaat penggunaan fungsi dan library dalam pemrograman Arduino! Berikan contoh library yang sering digunakan!

---
## 📋 Rubrik Penilaian Proyek

| Aspek | Kurang | Cukup | Baik |
|-------|--------|-------|------|
| Perangkaian Hardware | Rangkaian traffic light salah | Rangkaian benar tapi kurang rapi | Rangkaian rapi, LED terpasang dengan benar |
| Kebenaran Program | Program tidak sesuai logika traffic light | Program berjalan dengan kesalahan timing | Program benar, timing tepat, menggunakan fungsi |
| Fungsionalitas Alat | Traffic light tidak berfungsi | Traffic light berfungsi tapi ada jeda tidak sesuai | Traffic light berfungsi sempurna: hijau5→kuning2→merah5→kuning2 |
| Dokumentasi | Tidak ada dokumentasi | Dokumentasi ada tapi kurang lengkap | Dokumentasi lengkap (foto, video, kode program) |

---
## 🚀 Tugas Pengayaan

### 🚦 Traffic Light dengan Pedestrian Crossing
Kembangkan program traffic light sederhana menjadi sistem lalu lintas lengkap dengan pedestrian crossing. Tambahkan 2 LED tambahan (merah & hijau) untuk pejalan kaki, dan sebuah push button sebagai tombol penyeberangan. Gunakan interrupt atau polling untuk mendeteksi tombol. Buat laporan singkat berisi kode program dan penjelasan logika kerjanya.

---
## 📖 Glosarium

- **Berpikir Komputasional**: Cara berpikir untuk memecahkan masalah dengan menerapkan konsep dan logika ilmu komputer.
- **Dekomposisi**: Memecah masalah besar menjadi bagian-bagian kecil yang lebih mudah dikelola.
- **Algoritma**: Langkah-langkah sistematis untuk menyelesaikan suatu masalah.
- **Abstraksi**: Memfokuskan pada informasi penting dan mengabaikan yang tidak relevan.
- **Variabel**: Tempat menyimpan data dalam program komputer.
- **Array**: Struktur data yang menyimpan banyak nilai dengan tipe yang sama dalam satu variabel.
- **Fungsi**: Blok kode yang bisa dipanggil berulang kali untuk menjalankan tugas tertentu.
- **Library**: Kumpulan fungsi siap pakai yang bisa digunakan dalam program.

---
## 📺 Sumber & Media Pembelajaran

| Platform | Sumber | Tautan | Keterangan |
|----------|--------|--------|------------|
| YouTube | Berpikir Komputasional | `youtu.be/search?q=berpikir+komputasional+indonesia` | Penjelasan 4 pilar BK oleh guru Indonesia |
| YouTube | Belajar Pemrograman C untuk Pemula | `youtu.be/search?q=belajar+pemrograman+C+arduino+pemula` | Tutorial bahasa C dari dasar |
| Simulasi | Wokwi Arduino Simulator | `https://wokwi.com/` | Simulator Arduino online dengan berbagai komponen |
| Website | Kelas Terbuka — Algoritma | `https://www.kelasterbuka.com/` | Video belajar algoritma dan pemrograman |
| Website | Programiz C Programming | `https://www.programiz.com/c-programming` | Tutorial interaktif bahasa C |
