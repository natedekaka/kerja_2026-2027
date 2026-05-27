# 🤖 Bab 7: Algoritma dan Pemrograman

> **Semester Genap** | **Fase E** | **Kelas X** | **20 JP**

---

## 📊 Pemetaan Capaian Pembelajaran

| Elemen CP | Deskripsi CP |
|-----------|-------------|
| Algoritma dan Pemrograman | Menyusun algoritma, membuat flowchart, dan mengimplementasikannya dalam bahasa pemrograman visual berbasis blok. |
| Berpikir Komputasional | Menerapkan logika boolean dan struktur kontrol dalam pemrograman. |

---

## 🎯 Tujuan Pembelajaran

- **A.** Logika dan Algoritma Dasar
- **B.** Flowchart: Memvisualisasikan Algoritma
- **C.** Pengenalan Scratch sebagai Alat Pemrograman
- **D.** Proyek: Program Sederhana dengan Scratch

## 🗺️ Peta Konsep

```
               🤖 ALGORITMA DAN PEMROGRAMAN
                     |
                     ├── A. Logika dan Algoritma Dasar
                     ├── B. Flowchart: Memvisualisasikan Algoritma
                     ├── C. Pengenalan Scratch sebagai Alat Pemrograman
                     └── D. Proyek: Program Sederhana dengan Scratch
```

## A. Logika dan Algoritma Dasar

### 🤖 Logika dan Algoritma Dasar

**Logika** adalah ilmu tentang **penalaran yang benar**. **Algoritma** adalah **langkah-langkah sistematis** untuk menyelesaikan masalah. Tanpa algoritma yang baik, program tidak akan berjalan dengan benar.

> 🧩 **Analogi:** Algoritma itu seperti **resep mie instan**. Langkah-langkahnya jelas, urut, dan terbatas: (1) Buka bungkus, (2) Rebus air, (3) Masukkan mie, (4) Masukkan bumbu, (5) Sajikan. Kalau langkahnya diacak — misalnya bumbu dimasukkan sebelum air mendidih — hasilnya tidak maksimal. Sama seperti program!

### Logika Dasar: AND, OR, NOT

Dalam pemrograman, kita sering menggunakan logika **boolean** (true/false):

```
AND    = semua harus benar (✅ AND ✅ = ✅)
OR     = salah satu benar (✅ OR ❌ = ✅)
NOT    = kebalikan (NOT ✅ = ❌)
```

| Nilai A | Nilai B | A AND B | A OR B | NOT A |
|---------|---------|---------|--------|-------|
| ✅ | ✅ | ✅ | ✅ | ❌ |
| ✅ | ❌ | ❌ | ✅ | ❌ |
| ❌ | ✅ | ❌ | ✅ | ✅ |
| ❌ | ❌ | ❌ | ❌ | ✅ |

**Contoh dalam kehidupan:**
- "Kamu boleh main game **JIKA** PR sudah selesai **DAN** sudah maghrib"
- "Kamu dapat nilai A **JIKA** UTS >= 80 **ATAU** UAS >= 85"
- "Kamu **TIDAK** boleh keluar kelas tanpa izin"

### Ciri-Ciri Algoritma yang Baik

| Ciri | Penjelasan | Contoh Buruk | Contoh Baik |
|------|-----------|-------------|-------------|
| **Input** | Ada data yang diproses | — | Masukkan 2 angka |
| **Output** | Menghasilkan hasil | — | Tampilkan jumlah |
| **Definitif** | Setiap langkah jelas | "Masak sampai matang" | "Rebus 5 menit" |
| **Finite** | Berhenti | "Ulang terus" | "Ulang 10 kali" |
| **Efektif** | Bisa dijalankan | "Terbang ke bulan" | "Hitung luas segitiga" |

### Contoh Algoritma Sederhana

**Algoritma Membeli Gojek:**
```
1. Buka aplikasi Gojek
2. Pilih GoRide
3. Masukkan lokasi jemput (otomatis) dan tujuan
4. Pilih driver yang tersedia
5. Tunggu driver datang
6. Naik dan sampai tujuan
7. Bayar (cash/GoPay)
8. Selesai
```

### 📌 Contoh Nyata

**Algoritma TikTok FYP:**
1. Kamu menonton video kucing
2. Sistem mencatat: durasi tonton = 30 detik (lama = suka)
3. Sistem mencari pola: "pengguna yang suka kucing juga suka..."
4. TikTok menampilkan lebih banyak video kucing
5. Kamu jadi betah berjam-jam di TikTok!
6. **Ini adalah algoritma!**

### 🔍 Cek Pemahaman
1. Jelaskan perbedaan logika AND, OR, dan NOT! Berikan contoh masing-masing!
2. Sebutkan 5 ciri algoritma yang baik!
3. Apa perbedaan antara algoritma yang definitif dan yang tidak? Berikan contoh!

### 📋 Studi Kasus
Sebuah aplikasi Gojek ingin menambahkan fitur baru: jika saldo GoPay cukup, pembayaran otomatis menggunakan GoPay. Jika tidak, tampilkan pilihan metode pembayaran lain.

**Pertanyaan:**
1. Tuliskan algoritma sederhana untuk fitur tersebut menggunakan logika IF-THEN-ELSE!
2. Logika boolean apa yang digunakan dalam kasus "Saldo cukup DAN lokasi tujuan valid"?

> 🤔 **Refleksi:** Tuliskan algoritma "Bangun pagi dan berangkat sekolah" dalam 8 langkah. Tukarkan dengan temanmu, apakah langkahnya sudah jelas?

> 🤔 **Mari Renungkan:** Apa hal paling menarik yang kamu pelajari dari bagian ini?

---

## B. Flowchart: Memvisualisasikan Algoritma

### 📐 Flowchart: Memvisualisasikan Algoritma

Flowchart adalah **diagram yang menggambarkan alur algoritma** menggunakan simbol-simbol standar. Flowchart membuat algoritma lebih mudah dipahami daripada teks.

> 🧩 **Analogi:** Flowchart itu seperti **peta jalan**. Bayangkan algoritma "Pergi ke rumah teman" ditulis dalam teks: belok kiri, lurus, belok kanan... Lebih mudah dipahami pakai peta, kan? Flowchart adalah "peta" untuk program!

### Simbol Flowchart

```
    ┌──────────┐      ┌──────────────┐      ┌──────────┐
    │  START/  │      │   PROSES     │      │  INPUT/  │
    │  END     │      │  (Kegiatan)  │      │  OUTPUT  │
    └──────────┘      └──────────────┘      └──────────┘
    (Terminator)      (Process)            (Input/Output)

    ┌──────────┐      ┌──────┐       ┌──────────────────┐
    │ KONDISI  │      │      │       │                  │
    │ Ya / Tidak├──────► ◄───────       ► PREPARATION    │
    └──────────┘      └──────┘       │ (Inisialisasi)   │
    (Decision)         (Connector)    └──────────────────┘
```

### Contoh Flowchart: Menentukan Kelulusan

```
                ┌──────────┐
                │  START   │
                └────┬─────┘
                     ▼
                ┌──────────┐
                │ Input    │
                │ Nilai    │
                └────┬─────┘
                     ▼
                ┌──────────┐
                │ Nilai    │
             ┌──┤ >= 75?   ├──┐
             │  └────┬─────┘  │
             │       │ Ya    Tidak
             ▼       ▼       ▼
        ┌────────┐      ┌──────────┐
        │ LULUS  │      │ REMEDIAL │
        └───┬────┘      └────┬─────┘
            │                │
            └────────┬───────┘
                     ▼
                ┌──────────┐
                │  END     │
                └──────────┘
```

### Contoh Flowchart: Menghitung Luas Persegi

```
                ┌──────────┐
                │  START   │
                └────┬─────┘
                     ▼
      ┌──────────────────────────┐
      │ Input sisi (s)           │
      └────────────┬─────────────┘
                   ▼
      ┌──────────────────────────┐
      │ Hitung luas = s × s      │
      └────────────┬─────────────┘
                   ▼
      ┌──────────────────────────┐
      │ Tampilkan luas           │
      └────────────┬─────────────┘
                   ▼
                ┌──────────┐
                │  END     │
                └──────────┘
```

### 📌 Contoh Nyata

**Flowchart Login Gojek:**
1. START → Buka Aplikasi Gojek
2. Input nomor HP
3. Apakah nomor terdaftar?
   - Ya → Kirim OTP
   - Tidak → Tampilkan "Daftar dulu"
4. Input OTP
5. Apakah OTP benar?
   - Ya → Masuk ke halaman utama
   - Tidak → "OTP salah, coba lagi"
6. END

### 🔍 Cek Pemahaman
1. Sebutkan 4 simbol flowchart beserta fungsinya!
2. Apa perbedaan antara simbol Process dan Decision dalam flowchart?
3. Mengapa flowchart lebih mudah dipahami daripada algoritma dalam bentuk teks?

### 📋 Studi Kasus
Seorang siswa diminta membuat flowchart untuk program "Cek Suhu Tubuh". Aturannya: jika suhu >= 38°C maka tampilkan "DEMAM", jika kurang tampilkan "SEHAT".

**Pertanyaan:**
1. Buatlah flowchart dalam bentuk teks (gunakan ASCII atau deskripsi langkah) untuk program tersebut!
2. Bagaimana jika ditambahkan kondisi: jika suhu >= 38°C DAN ada batuk, tampilkan "SEGERA KE DOKTER"?

> 🤔 **Refleksi:** Buatlah flowchart untuk algoritma "Membeli pulsa" atau "Membuat kopi" menggunakan simbol-simbol yang benar!

> 🤔 **Mari Renungkan:** Apa hal paling menarik yang kamu pelajari dari bagian ini?

---

## C. Pengenalan Scratch sebagai Alat Pemrograman

### 🧩 Pengenalan Scratch sebagai Alat Pemrograman

**Scratch** adalah bahasa pemrograman **visual berbasis blok** yang dikembangkan oleh MIT Media Lab. Cocok untuk pemula karena tidak perlu menulis kode teks — cukup **seret dan susun blok-blok** seperti menyusun LEGO!

> 🧩 **Analogi:** Scratch itu seperti **LEGO**: setiap blok adalah perintah (misal: "gerak 10 langkah", "putar 15 derajat", "katakan Halo"). Kamu tinggal menyusun blok-blok itu seperti menyusun balok LEGO — tanpa perlu lem (coding teks)! Hasilnya? Program yang bisa jalan!

### Tampilan Scratch

```
  ┌─────────────────────────────────────────────────────────┐
  │ Scratch 3.0                             [File] [Edit]  │
  ├──────────┬──────────────────────────┬──────────────────┤
  │          │                          │                  │
  │  BLOCKS  │      PROGRAM AREA        │     STAGE       │
  │  (Kode)  │   (Susun blok di sini)   │  (Hasil/layar)  │
  │          │                          │                  │
  │  Motion  │  when ▢ clicked          │  ┌──────────┐   │
  │  Looks   │  move 10 steps           │  │  Kucing  │   │
  │  Sound   │  say [Halo!] for 2 secs  │  │  🐱      │   │
  │  Events  │  wait 1 seconds          │  │          │   │
  │  Control │  forever                 │  └──────────┘   │
  │  Sensing │    next costume          │                  │
  │  ...     │                          │                  │
  ├──────────┴──────────────────────────┴──────────────────┤
  │ SPRITES  │  Backdrops  │  Sound                        │
  └────────────────────────────────────────────────────────┘
```

### Kategori Blok Scratch

| Kategori | Warna | Fungsi | Contoh Blok |
|----------|-------|--------|-------------|
| **Motion** | 🔵 Biru | Menggerakkan sprite | `move 10 steps`, `turn 15 degrees` |
| **Looks** | 🟣 Ungu | Mengubah tampilan | `say [Halo]`, `switch costume` |
| **Sound** | 🟣 Pink | Memutar suara | `play sound`, `change volume` |
| **Events** | 🟡 Kuning | Memicu kode | `when flag clicked`, `when key pressed` |
| **Control** | 🟠 Oranye | Mengatur alur | `wait`, `forever`, `if then else` |
| **Sensing** | 🔵 Biru Muda | Mendeteksi sesuatu | `touching mouse`, `ask and wait` |
| **Operators** | 🟢 Hijau | Operasi matematika | `+`, `-`, `*`, `/`, `>` |
| **Variables** | 🟠 Oranye | Membuat variabel | `set score to 0`, `change score` |

### Contoh Kode di Scratch

```blocks
Ketika bendera hijau diklik
ulang terus
    jika (senter menyentuh Kucing?) maka
        katakan Aduh! selama 2 detik
        mainkan suara Meow
    jika tidak
        jalan 10 langkah
        jika di pinggir, pantulkan
    akhir
akhir
```

### 📌 Contoh Nyata

Banyak game sederhana dibuat dengan Scratch oleh siswa SMP/SMA di seluruh dunia. Di Indonesia, Scratch sering digunakan untuk:
- Membuat kuis interaktif
- Animasi cerita pendek
- Game sederhana (T-Rex run, Flappy Bird clone)
- Simulasi fisika (gravitasi, gerak parabola)

**Kunjungi** https://scratch.mit.edu untuk mencoba langsung secara online — **gratis!**

### 🔍 Cek Pemahaman
1. Apa itu Scratch dan siapa yang mengembangkannya?
2. Sebutkan 5 kategori blok di Scratch beserta warna dan fungsinya!
3. Mengapa Scratch cocok untuk pemula belajar pemrograman?

### 📋 Studi Kasus
Di kelas X, guru memberikan tugas membuat animasi sederhana dengan Scratch. Seorang siswa ingin membuat animasi kucing yang berjalan dan mengeong ketika disentuh oleh pointer mouse.

**Pertanyaan:**
1. Kategori blok apa saja yang diperlukan untuk membuat animasi tersebut?
2. Tuliskan urutan blok yang kira-kira diperlukan (dalam bentuk deskripsi)!

> 🤔 **Refleksi:** Apa perbedaan pemrograman blok (Scratch) dengan pemrograman teks (C++, Python)? Mana yang lebih mudah menurutmu?

> 🤔 **Mari Renungkan:** Apa hal paling menarik yang kamu pelajari dari bagian ini?

---

## D. Proyek: Program Sederhana dengan Scratch

### 🎮 Proyek: Program Sederhana dengan Scratch

Saatnya **membuat program sungguhan**! Dengan Scratch, kamu bisa membuat game, animasi, atau cerita interaktif hanya dengan menyusun blok-blok.

> 🧩 **Analogi:** Proyek ini seperti **membangun rumah dari LEGO**. Kamu sudah tahu fungsi setiap blok (motion, looks, control, dll). Sekarang saatnya merancang dan membangun sesuatu yang **nyata** — bukan sekadar latihan!

### 💡 Ide Proyek (Pilih Salah Satu)

#### 1. 🎯 Game Kuis Interaktif
```
Konsep: Pemain menjawab pertanyaan Informatika
Fitur:
✅ Pertanyaan muncul acak
✅ Skor bertambah jika benar
✅ Timer 10 detik per soal
✅ Suara "benar" 🎉 dan "salah" 😢

Blok yang digunakan: Events, Sensing, Variables, Control, Looks
```

#### 2. 🐱 Game Kejar-Kejaran
```
Konsep: Kucing mengejar tikus, dikendalikan mouse
Fitur:
✅ Kucing mengikuti pointer mouse
✅ Tikus menghindar secara otomatis
✅ Skor bertambah jika kucing menyentuh tikus
✅ Level semakin cepat

Blok yang digunakan: Motion, Control, Sensing, Variables
```

#### 3. 🌟 Animasi Cerita "Liburan ke Bandung"
```
Konsep: Animasi interaktif 2-3 menit
Fitur:
✅ Karakter bicara dengan speech bubble
✅ Latar berubah (rumah → jalan → tujuan)
✅ Klik untuk lanjut ke scene berikutnya
✅ Efek suara dan musik

Blok yang digunakan: Looks, Events, Control, Sound
```

### Langkah-Langkah Proyek

```
┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐
│  Tentukan │   │  Desain  │   │  Susun   │   │   Uji    │
│  Ide     │──►│  Karakter│──►│  Blok    │──►│  & Debug │
└──────────┘   └──────────┘   └──────────┘   └────┬─────┘
                                                   │
                                            ┌──────────┐
                                            │ Presentasi│
                                            │ & Kumpul  │
                                            └──────────┘
```

### Rubrik Penilaian

| Aspek | Skor 4 | Skor 3 | Skor 2 | Skor 1 |
|-------|--------|--------|--------|--------|
| **Fungsionalitas** | Program berjalan sempurna | Berjalan dengan bug kecil | Berjalan sebagian | Tidak bisa jalan |
| **Kreativitas** | Konsep unik & menarik | Cukup kreatif | Biasa saja | Tidak ada kreativitas |
| **Kompleksitas** | Banyak blok & interaksi | Beberapa blok | Blok minimal | Sangat sederhana |
| **Estetika** | Tampilan & suara menarik | Cukup rapi | Kurang rapi | Acak-acakan |

### 📌 Contoh Nyata

**Proyek siswa SMA N 6 Cimahi tahun lalu:** Mereka membuat game "Petualangan Si Oncom" — sebuah game edukasi tentang sejarah Bandung. Karakter utama (Oncom, kucing lucu) harus mengumpulkan informasi sejarah sambil menghindari rintangan. Game ini dipresentasikan di acara class meeting!

```blocks
Ketika bendera hijau diklik
set skor ke 0
tanyakan [Siapa nama kamu?] dan tunggu
katakan (gabung [Selamat datang, ] (jawaban)) selama 2 detik
forever
    if <touching [musuh v] ?> then
        change skor by (-1)
        say [Aduh!] for 1 seconds
    end
end
```

Selamat berkarya! 🚀

### 🔍 Cek Pemahaman
1. Sebutkan 3 ide proyek yang bisa dibuat dengan Scratch!
2. Apa saja 4 aspek penilaian dalam rubrik proyek Scratch?
3. Jelaskan langkah-langkah pengerjaan proyek Scratch dari awal hingga akhir!

### 📋 Studi Kasus
Sebuah kelompok memilih proyek "Game Kuis Informatika" dengan Scratch. Setelah seminggu, mereka baru membuat 3 soal, skor belum berfungsi, dan tampilan masih berantakan. Deadline tinggal 3 hari lagi.

**Pertanyaan:**
1. Apa yang salah dengan perencanaan proyek kelompok tersebut?
2. Buatkan jadwal 3 hari yang efektif agar proyek mereka selesai tepat waktu!

> 🤔 **Refleksi:** Setelah proyek selesai, tuliskan (1) Hal paling seru, (2) Kesulitan terbesar, (3) Satu hal yang akan kamu tingkatkan!

> 🤔 **Mari Renungkan:** Apa hal paling menarik yang kamu pelajari dari bagian ini?

---

---
## 🏗️ Proyek Mini: Game Sederhana di Scratch 🎮

Buat game atau animasi interaktif menggunakan Scratch. Pilih salah satu: Game Tebak Angka, Kuis Interaktif, atau Animasi Cerita Pendek. Minimal menggunakan 3 kategori blok berbeda.

**Alat dan Bahan:**
- Scratch (https://scratch.mit.edu) — online atau offline
- Laptop/komputer dengan koneksi internet

**Langkah-langkah:**
1. Tentukan ide: Game Tebak Angka / Kuis Informatika / Animasi Cerita
2. Buat flowchart sederhana alur program kamu
3. Pilih sprite (karakter) dan backdrop (latar) yang sesuai
4. Susun blok-blok program: events, control, motion/looks, variables
5. Uji coba program — cari dan perbaiki bug (debugging)
6. Tambahkan fitur tambahan: skor, timer, suara, atau level
7. Simpan dan kumpulkan file .sb3 beserta dokumentasi

> **Output:** File Scratch (.sb3) + flowchart + dokumentasi singkat

---

## 📝 Rangkuman

- Algoritma adalah langkah-langkah sistematis untuk menyelesaikan masalah. Logika dasar meliputi AND, OR, dan NOT.
- Flowchart memvisualisasikan algoritma menggunakan simbol standar: terminator, proses, decision, dan input/output.
- Scratch adalah bahasa pemrograman visual berbasis blok dari MIT — cocok untuk pemula belajar konsep coding tanpa menulis teks.
- Proyek Scratch bisa berupa game kuis, game kejar-kejaran, atau animasi cerita — melatih kreativitas dan logika pemrograman.

---

## ✍️ Latihan Soal

### A. Pilihan Ganda

1. Logika AND akan menghasilkan nilai benar (true) jika...
   a. Salah satu benar
   b. Keduanya benar
   c. Keduanya salah
   d. Minimal satu benar
   e. Tidak ada yang benar
   **Kunci Jawaban: B**

2. Flowchart adalah...
   a. Bahasa pemrograman
   b. Diagram yang menggambarkan alur algoritma
   c. Software untuk coding
   d. Jenis komputer
   e. Alat input
   **Kunci Jawaban: B**

3. Simbol flowchart berbentuk belah ketupat digunakan untuk...
   a. Start/End
   b. Proses
   c. Decision/kondisi
   d. Input/Output
   e. Konektor
   **Kunci Jawaban: C**

4. Scratch adalah bahasa pemrograman...
   a. Teks tingkat tinggi
   b. Visual berbasis blok
   c. Mesin tingkat rendah
   d. Database
   e. Markup
   **Kunci Jawaban: B**

5. Blok berwarna kuning di Scratch termasuk kategori...
   a. Motion
   b. Control
   c. Events
   d. Looks
   e. Sound
   **Kunci Jawaban: C**

### B. Uraian

1. Jelaskan apa yang dimaksud dengan algoritma dan sebutkan minimal 4 ciri algoritma yang baik!

2. Buatlah flowchart sederhana untuk menentukan apakah seorang siswa lulus atau remedial (nilai >= 75 lulus)!

3. Jelaskan perbedaan dan kegunaan blok Motion, Looks, Control, dan Events di Scratch!

4. Buatlah algoritma dalam 8-10 langkah untuk 'Memesan tiket bioskop melalui aplikasi online'!

---
## 📋 Rubrik Penilaian Proyek

| Aspek | Kurang | Cukup | Baik |
|-------|--------|-------|------|
| Fungsionalitas Program | Program tidak berjalan | Program berjalan dengan bug | Program berjalan sempurna |
| Kompleksitas Blok | Hanya 1-2 kategori blok | 3 kategori blok digunakan | 4+ kategori blok, ada variabel/logika |
| Kreativitas & Desain | Sprite default, tidak ada desain | Ada modifikasi sprite/latar | Desain unik, menarik, sesuai tema |
| Dokumentasi | Tidak ada dokumentasi | Dokumentasi minimal | Dokumentasi lengkap: flowchart + deskripsi |

---

## 🚀 Tugas Pengayaan

### Scratch Tingkat Lanjut
Buat game yang lebih kompleks di Scratch: game platformer (lompat rintangan) atau game shooting. Gunakan cloning, variabel global, dan message broadcasting.

### Eksplorasi Python
Coba buat program sederhana dengan Python di https://replit.com/ atau Google Colab. Program: kalkulator sederhana atau konversi suhu. Bandingkan dengan Scratch!

---

## 📖 Glosarium

- **Algoritma**: Langkah-langkah sistematis dan logis untuk menyelesaikan masalah.
- **Flowchart**: Diagram yang menggambarkan alur algoritma menggunakan simbol-simbol standar.
- **Scratch**: Bahasa pemrograman visual berbasis blok yang dikembangkan oleh MIT.
- **Logika Boolean**: Sistem logika dengan dua nilai: benar (true) dan salah (false).
- **Variabel**: Tempat penyimpanan data yang nilainya bisa berubah selama program berjalan.
- **Sprite**: Karakter atau objek dalam Scratch yang bisa diprogram.
- **Loop (Perulangan)**: Blok perintah yang menjalankan kode secara berulang (forever, repeat).

---
## 📺 Sumber & Media Pembelajaran

| Platform | Sumber | Tautan | Keterangan |
|----------|--------|--------|------------|
| YouTube | Belajar Algoritma dan Flowchart | `https://youtu.be/...search?q=algoritma+dan+flowchart+indonesia` | Video belajar algoritma dasar dan flowchart |
| YouTube | Pemrograman Scratch untuk Pemula | `https://youtu.be/...search?q=tutorial+scratch+bahasa+indonesia` | Tutorial Scratch dari dasar oleh kreator Indonesia |
| Simulasi | Scratch MIT — Coba Online | `https://scratch.mit.edu/` | Platform pemrograman visual blok — gratis! |
| Website | Blockly Games | `https://blockly.games/` | Game coding visual untuk latihan logika |
| YouTube | Sekolahmu — Algoritma Pemrograman | `https://youtu.be/...search?q=sekolahmu+algoritma+pemrograman` | Materi algoritma dari Sekolahmu channel |
