# ⚙️ Bab 4: Sistem Komputer

> **Semester Ganjil** | **Fase E** | **Kelas X** | **15 JP**

---

## 📊 Pemetaan Capaian Pembelajaran

| Elemen CP | Deskripsi CP |
|-----------|-------------|
| Sistem Komputer | Memahami peran sistem operasi, komponen hardware, dan software dalam sistem komputer. |
| Teknologi Informasi dan Komunikasi | Mengidentifikasi jenis-jenis perangkat lunak dan kegunaannya. |

---

## 🎯 Tujuan Pembelajaran

- **A.** Hardware: Komponen Fisik Komputer
- **B.** Software: Perangkat Lunak Sistem dan Aplikasi
- **C.** Sistem Operasi: Jembatan Pengguna dan Hardware

## 🗺️ Peta Konsep

```
               ⚙️ SISTEM KOMPUTER
                     |
                     ├── A. Hardware: Komponen Fisik Komputer
                     ├── B. Software: Perangkat Lunak Sistem dan Aplikasi
                     └── C. Sistem Operasi: Jembatan Pengguna dan Hardware
```

## A. Hardware: Komponen Fisik Komputer

### ⚙️ Hardware: Komponen Fisik Komputer

Hardware adalah semua bagian komputer yang **bisa dilihat dan disentuh**. Ibarat tubuh manusia, hardware adalah **anggota badan** — fisik yang bisa diraba.

> 🧩 **Analogi:** Hardware itu seperti **dapur**. Ada kompor (CPU), wajan (motherboard), pisau (mouse/keyboard), talenan (RAM), lemari es (hard disk), dan piring (monitor). Semua alat fisik yang diperlukan untuk memasak.

### Komponen Utama Hardware

```
                 ┌──────────────────────┐
                 │      MONITOR         │
                 │   (Output Visual)    │
                 └──────────┬───────────┘
                            │
      ┌─────────────────────┼─────────────────────┐
      │                     │                     │
      ▼                     ▼                     ▼
┌──────────┐         ┌──────────┐         ┌──────────┐
│ KEYBOARD ├────────►│   CPU    │◄────────│  MOUSE   │
│ (Input)  │         │  (Otak)  │         │ (Input)  │
└──────────┘         └────┬─────┘         └──────────┘
                          │
      ┌───────────────────┼────────────────────┐
      │                   │                    │
      ▼                   ▼                    ▼
┌──────────┐        ┌──────────┐        ┌──────────┐
│   RAM    │        │  HDD/SSD │        │  SPEAKER │
│ Memori   │        │ Storage  │        │ Output   │
│ Sementara│        │ Permanen │        │ Audio    │
└──────────┘        └──────────┘        └──────────┘
```

### Tabel Komponen dan Fungsinya

| Komponen | Fungsi | Analogi |
|----------|--------|---------|
| **CPU** (Prosesor) | Otak komputer — menjalankan perintah | Manajer yang memberi instruksi |
| **RAM** | Memori sementara, cepat tapi hilang saat mati | Meja kerja sementara |
| **Hard Disk / SSD** | Penyimpanan permanen, lambat tapi awet | Lemari arsip |
| **Motherboard** | Papan sirkuit utama penghubung semua komponen | Kerangka tubuh |
| **Power Supply (PSU)** | Sumber listrik | Jantung yang pompa darah (listrik) |
| **GPU / VGA Card** | Mengolah grafis / tampilan | Pelukis digital |

### CPU: Otak Komputer

```
┌─────────────────────────────────┐
│     PROSESOR (CPU)              │
│  ┌─────┐  ┌─────┐  ┌─────┐    │
│  │ ALU │  │ CU  │  │ Cache│    │
│  └─────┘  └─────┘  └─────┘    │
│  • ALU = Arithmetic Logic Unit  │
│  • CU = Control Unit            │
│  • Cache = Memori super cepat   │
└─────────────────────────────────┘
```

### 📌 Contoh Nyata

Spek komputer lab sekolah biasanya: **Intel Core i3 / RAM 4 GB / SSD 256 GB**. Cukup untuk belajar Microsoft Office, browsing, dan coding dasar. Kalau mau gaming atau editing video berat, butuh spek lebih tinggi (i5/i7, RAM 16GB, GPU dedicated).

### 🔍 Cek Pemahaman
1. Sebutkan 5 komponen utama hardware dan fungsinya masing-masing!
2. Apa perbedaan antara RAM dan Hard Disk/SSD?
3. Jelaskan fungsi ALU dan CU dalam prosesor!

### 📋 Studi Kasus
Andi ingin membeli laptop untuk belajar dan desain grafis. Temannya menyarankan laptop dengan RAM 4 GB dan prosesor i3, tapi Andi juga lihat laptop lain dengan RAM 8 GB dan prosesor i5 harganya lebih mahal 2 juta.

**Pertanyaan:**
1. Komponen hardware mana yang paling penting untuk kebutuhan desain grafis?
2. Berdasarkan spek yang berbeda, laptop mana yang sebaiknya dipilih Andi? Jelaskan alasannya!

> 🤔 **Refleksi:** Coba lihat spek HP atau komputermu! Berapa GHz prosesornya? Berapa GB RAM-nya? Catat dan bandingkan dengan temanmu!

> 🤔 **Mari Renungkan:** Apa hal paling menarik yang kamu pelajari dari bagian ini?

---

## B. Software: Perangkat Lunak Sistem dan Aplikasi

### 💿 Software: Perangkat Lunak Sistem dan Aplikasi

Software adalah **program dan data** yang membuat hardware bisa bekerja. Software **tidak bisa disentuh** — dia adalah instruksi logis yang dijalankan komputer.

> 🧩 **Analogi:** Hardware adalah **piano**, software adalah **lembaran musik**. Piano tanpa lembaran musik hanya benda mati. Lembaran musik tanpa piano tidak bisa dimainkan. Keduanya harus bersatu agar tercipta musik yang indah!

### Jenis-Jenis Software

```
                ┌──────────────────────────────┐
                │       SOFTWARE               │
                ├────────────────────┬─────────┤
                │                    │         │
          ┌─────▼──────┐      ┌─────▼──────┐  │
          │  SISTEM OS  │      │  APLIKASI  │  │
          │  (OS)       │      │            │  │
          │  Windows    │      │  Word      │  │
          │  Linux      │      │  Chrome    │  │
          │  macOS      │      │  Canva     │  │
          │  Android    │      │  Scratch   │  │
          └─────────────┘      └────────────┘  │
                │                               │
          ┌─────▼──────┐                       │
          │  UTILITY   │                       │
          │  Antivirus │                       │
          │  Cleaner   │                       │
          └────────────┘                       │
                └──────────────────────────────┘
```

### Perbandingan Software Sistem vs Aplikasi

| Aspek | Software Sistem | Software Aplikasi |
|-------|----------------|-------------------|
| **Tujuan** | Mengelola hardware & software lain | Membantu tugas spesifik pengguna |
| **Pengguna** | Sistem (otomatis) | Langsung oleh user |
| **Contoh** | Windows 11, Android 14 | Word, Excel, Chrome, CapCut |
| **Tanpa OS?** | OS diperlukan agar aplikasi jalan | Tidak bisa jalan tanpa OS |

### Software Aplikasi Populer

| Kategori | Contoh | Fungsi |
|----------|--------|--------|
| **Office** | Microsoft Office, Google Docs | Menulis, spreadsheet, presentasi |
| **Browser** | Chrome, Firefox, Edge | Berselancar di internet |
| **Desain** | Canva, Figma, CorelDRAW | Membuat desain grafis |
| **Editing** | CapCut, Kdenlive, Photoshop | Edit video, foto |
| **Komunikasi** | WhatsApp, Discord, Zoom | Chat, video call |
| **Pendidikan** | Google Classroom, Quizizz | Belajar dan tugas |

### 📌 Contoh Nyata

**Saat kamu membuat laporan:**
- **Sistem Operasi:** Windows 11 menyalakan laptop
- **Aplikasi:** Microsoft Word untuk menulis
- **Browser:** Chrome untuk mencari referensi
- **Cloud:** Google Drive untuk menyimpan & share

### 🔍 Cek Pemahaman
1. Jelaskan perbedaan software sistem dan software aplikasi!
2. Sebutkan 3 contoh software aplikasi untuk desain grafis!
3. Mengapa software aplikasi tidak bisa berjalan tanpa sistem operasi?

### 📋 Studi Kasus
Seorang siswa menginstal 3 sistem operasi berbeda di satu laptop (Windows, Linux, dan macOS) untuk tugas sekolahnya. Dia bingung mengapa beberapa aplikasi Word dan Excel tidak bisa jalan di Linux.

**Pertanyaan:**
1. Mengapa aplikasi tertentu hanya bisa berjalan di sistem operasi tertentu?
2. Menurutmu, sistem operasi apa yang paling cocok untuk seorang pelajar? Jelaskan alasannya!

> 🤔 **Refleksi:** Sebutkan 5 aplikasi yang paling sering kamu pakai dalam sehari! Kategorikan sebagai sistem atau aplikasi!

> 🤔 **Mari Renungkan:** Apa hal paling menarik yang kamu pelajari dari bagian ini?

---

## C. Sistem Operasi: Jembatan Pengguna dan Hardware

### 🔗 Sistem Operasi: Jembatan Pengguna dan Hardware

Sistem Operasi (OS) adalah **software paling penting** di komputer. Dia menjadi jembatan antara pengguna (kamu), aplikasi, dan hardware.

> 🧩 **Analogi:** Sistem Operasi itu seperti **resepsionis** di hotel besar. Kamu (pengguna) datang dan minta sesuatu (buka file, buka browser). Resepsionis (OS) yang mengatur siapa yang melakukan apa — menyuruh petugas kebersihan, bellboy, atau teknisi (hardware) untuk bekerja. Kamu tidak perlu langsung ngomong ke petugasnya!

### Fungsi Utama Sistem Operasi

```
   ┌──────────────────────────────────────────┐
   │            PENGGUNA (USER)               │
   ├──────────────────────────────────────────┤
   │   APLIKASI: Word, Chrome, Game, Canva    │
   ├──────────────────────────────────────────┤
   │     SISTEM OPERASI (Windows/Linux)        │
   │   ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐  │
   │   │CPU   │ │Memory│ │I/O   │ │File  │  │
   │   │Mgmt  │ │Mgmt  │ │Mgmt  │ │Mgmt  │  │
   │   └──────┘ └──────┘ └──────┘ └──────┘  │
   ├──────────────────────────────────────────┤
   │           HARDWARE (CPU, RAM, dll)        │
   └──────────────────────────────────────────┘
```

### Sistem Operasi Populer

| OS | Developer | Perangkat | UI | Kelebihan |
|----|-----------|-----------|-----|-----------|
| **Windows 11** | Microsoft | PC, Laptop | GUI | Banyak software, mudah dipakai |
| **macOS** | Apple | MacBook, iMac | GUI | Desain premium, stabil |
| **Linux (Ubuntu)** | Open-source | PC, Server | GUI/CLI | Gratis, ringan, aman |
| **Android** | Google | Smartphone | Touch | Paling populer di HP |
| **iOS** | Apple | iPhone, iPad | Touch | Keamanan, ekosistem Apple |

### CLI vs GUI

```
┌──────────────────┐    ┌──────────────────┐
│      CLI         │    │      GUI         │
│ (Command Line)   │    │ (Graphical)      │
│                  │    │                  │
│ $ ls -la         │    │  ╔══╗  ┌──┐     │
│ $ cd Documents   │    │  ║  ║  │  │     │
│ $ mkdir Tugas    │    │  ╚══╝  └──┘     │
│ $ python run.py  │    │  Klik, drag,     │
│                  │    │  visual          │
│ Cepat, hemat     │    │ Mudah, ramah     │
│ resource         │    │ pengguna         │
└──────────────────┘    └──────────────────┘
```

### 📌 Contoh Nyata

**Boot process:** Saat kamu tekan tombol power laptop:
1. PSU memberi listrik ke motherboard
2. BIOS/UEFI melakukan pengecekan hardware (POST)
3. BIOS mencari bootloader di SSD/HDD
4. Bootloader memuat Windows/Linux ke RAM
5. Kamu lihat layar login — **selesai booting!**

### 🔍 Cek Pemahaman
1. Sebutkan 4 fungsi utama sistem operasi!
2. Apa perbedaan antara CLI dan GUI? Sebutkan kelebihan masing-masing!
3. Sebutkan 3 sistem operasi populer beserta perangkat yang menggunakannya!

### 📋 Studi Kasus
Laptop seorang siswa tiba-tiba muncul layar biru (Blue Screen of Death) saat sedang mengerjakan tugas. Semua file yang belum disimpan hilang.

**Pertanyaan:**
1. Jelaskan apa yang mungkin terjadi pada sistem operasi berdasarkan gejala di atas!
2. Apa yang seharusnya dilakukan siswa tersebut untuk mencegah kejadian serupa di masa depan?

> 🤔 **Refleksi:** OS apa yang kamu pakai di HP dan laptop? Sebutkan 3 kelebihan dan 3 kekurangan yang kamu rasakan!

> 🤔 **Mari Renungkan:** Apa hal paling menarik yang kamu pelajari dari bagian ini?

---

---
## 🏗️ Proyek Mini: Poster Anatomi Komputer 🖥️

Buat poster yang menampilkan komponen-komponen utama hardware komputer beserta fungsinya. Gambar atau ilustrasi komponen harus diberi label dan penjelasan singkat.

**Alat dan Bahan:**
- Canva / PowerPoint / Kertas gambar
- Referensi gambar komponen komputer

**Langkah-langkah:**
1. Identifikasi minimal 7 komponen hardware: CPU, RAM, HDD/SSD, Motherboard, PSU, GPU, dan satu komponen input/output
2. Cari gambar referensi setiap komponen (bisa dari internet atau gambar tangan)
3. Buat layout poster: susun komponen seperti diagram sistem komputer
4. Beri label nama dan fungsi singkat pada setiap komponen
5. Tambahkan panah alur data: Input → Proses → Output → Storage
6. Buat semenarik mungkin dengan warna yang harmonis

> **Output:** Poster digital (.pdf/.jpg) atau poster fisik ukuran A3

---

## 📝 Rangkuman

- Hardware terdiri dari komponen input, proses (CPU), output, storage (HDD/SSD), dan network — semuanya bekerja sama membentuk sistem komputer.
- Software dibagi menjadi sistem operasi (Windows, Linux), aplikasi (Word, Chrome), dan utility (antivirus).
- Sistem Operasi adalah jembatan antara pengguna, aplikasi, dan hardware — fungsi utamanya mengelola CPU, memori, I/O, dan file.

---

## ✍️ Latihan Soal

### A. Pilihan Ganda

1. Komponen komputer yang disebut sebagai 'otak' komputer adalah...
   a. RAM
   b. Hard Disk
   c. CPU
   d. Motherboard
   e. PSU
   **Kunci Jawaban: C**

2. RAM adalah memori yang bersifat...
   a. Permanen
   b. Sementara dan hilang saat komputer mati
   c. Tidak bisa dihapus
   d. Hanya untuk menyimpan file
   e. Sama seperti hard disk
   **Kunci Jawaban: B**

3. Perangkat lunak yang bertindak sebagai jembatan antara pengguna dan hardware adalah...
   a. Aplikasi
   b. Browser
   c. Sistem Operasi
   d. Driver
   e. Utility
   **Kunci Jawaban: C**

4. Berikut ini yang termasuk perangkat output adalah...
   a. Keyboard
   b. Mouse
   c. Monitor
   d. Scanner
   e. Mikrofon
   **Kunci Jawaban: C**

5. Linux adalah contoh dari...
   a. Aplikasi perkantoran
   b. Browser
   c. Sistem Operasi
   d. Bahasa pemrograman
   e. Game
   **Kunci Jawaban: C**

### B. Uraian

1. Jelaskan fungsi masing-masing: CPU, RAM, Hard Disk/SSD, dan Motherboard dalam sistem komputer!

2. Apa perbedaan antara software sistem dan software aplikasi? Berikan masing-masing 3 contoh!

3. Jelaskan peran sistem operasi sebagai jembatan antara pengguna dan hardware!

4. Apa yang dimaksud dengan GUI dan CLI? Sebutkan 2 kelebihan dan 2 kekurangan masing-masing!

---
## 📋 Rubrik Penilaian Proyek

| Aspek | Kurang | Cukup | Baik |
|-------|--------|-------|------|
| Kelengkapan Komponen | Kurang dari 4 komponen | 5-6 komponen tercantum | 7+ komponen lengkap |
| Ketepatan Fungsi | Fungsi tidak tepat atau salah | Fungsi cukup tepat | Fungsi tepat dan detail |
| Visual & Label | Tidak ada label atau label salah | Ada label, cukup rapi | Label jelas, layout profesional |
| Alur Sistem | Tidak menunjukkan alur data | Alur data ada tapi kurang jelas | Alur data Input→Proses→Output→Storage jelas |

---

## 🚀 Tugas Pengayaan

### Riset Spesifikasi
Cari 3 laptop/PC dengan rentang harga berbeda (5jt, 10jt, 15jt+). Bandingkan spesifikasi CPU, RAM, storage, dan GPU. Tulis rekomendasi untuk: pelajar, desainer grafis, dan gamer.

### Eksplorasi OS
Install Linux Ubuntu di VirtualBox atau coba live USB. Jelaskan perbedaan pengalaman menggunakan Linux vs Windows: tampilan, cara instal aplikasi, dan kecepatan.

---

## 📖 Glosarium

- **CPU (Central Processing Unit)**: Otak komputer yang menjalankan semua perintah dan proses.
- **RAM (Random Access Memory)**: Memori sementara yang cepat tapi hilang saat komputer mati.
- **Storage (HDD/SSD)**: Penyimpanan permanen untuk data dan file.
- **Motherboard**: Papan sirkuit utama yang menghubungkan semua komponen komputer.
- **Sistem Operasi**: Software utama yang menjadi jembatan antara pengguna, aplikasi, dan hardware.
- **GUI (Graphical User Interface)**: Antarmuka pengguna berbasis grafis — ikon, menu, dan jendela.
- **CLI (Command Line Interface)**: Antarmuka pengguna berbasis teks — mengetik perintah.

---
## 📺 Sumber & Media Pembelajaran

| Platform | Sumber | Tautan | Keterangan |
|----------|--------|--------|------------|
| YouTube | Cara Kerja Komputer — Kok Bisa? | `https://youtu.be/...search?q=cara+kerja+komputer+kok+bisa` | Animasi tentang komponen dalam komputer |
| YouTube | Merakit PC untuk Pemula | `https://youtu.be/...search?q=merakit+PC+pemula+indonesia` | Tutorial merakit komputer oleh content creator IT Indonesia |
| Simulasi | PhET Simulation — CPU | `https://phet.colorado.edu/in/simulations/` | Simulasi tentang sirkuit dan logika dasar |
| Website | Zenius — Sistem Komputer | `https://www.zenius.net/` | Materi dan latihan soal sistem komputer |
| YouTube | Kelas IT — Sistem Operasi | `https://youtu.be/...search?q=kelas+IT+sistem+operasi` | Penjelasan fungsi dan jenis sistem operasi |
