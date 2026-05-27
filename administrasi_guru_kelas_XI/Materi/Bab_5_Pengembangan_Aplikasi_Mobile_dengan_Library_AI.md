# 📱 Bab 5: Pengembangan Aplikasi Mobile dengan Library AI

> **Semester Genap** | **Fase F** | **Kelas XI** | **35 JP**

---

## 📊 Pemetaan Capaian Pembelajaran

| Elemen CP | Deskripsi CP |
|-----------|-------------|
| Algoritma dan Pemrograman (AP) | Mengembangkan aplikasi mobile dengan mengintegrasikan library AI untuk menyelesaikan masalah nyata |

---

## 🎯 Tujuan Pembelajaran

- **A.** Pengantar Aplikasi Mobile
- **B.** Membangun UI dengan App Inventor
- **C.** Navigasi & Penyimpanan Data
- **D.** Integrasi Library AI ke Aplikasi
- **E.** Image Classification & Speech Recognition
- **F.** Proyek Aplikasi AI: Perencanaan
- **G.** Proyek Aplikasi AI: Implementasi & Presentasi

## 🗺️ Peta Konsep

```
               📱 PENGEMBANGAN APLIKASI MOBILE DENGAN LIBRARY AI
                     |
                     ├── A. Pengantar Aplikasi Mobile
                     ├── B. Membangun UI dengan App Inventor
                     ├── C. Navigasi & Penyimpanan Data
                     ├── D. Integrasi Library AI ke Aplikasi
                     ├── E. Image Classification & Speech Recognition
                     ├── F. Proyek Aplikasi AI: Perencanaan
                     └── G. Proyek Aplikasi AI: Implementasi & Presentasi
```

## A. Pengantar Aplikasi Mobile

### 📱 Pengantar Aplikasi Mobile
Aplikasi mobile adalah program yang berjalan di perangkat bergerak (smartphone/tablet). Ada 3 jenis utama.

> 🧩 **Analogi:** Aplikasi mobile itu seperti **toko**. Ada toko yang khusus untuk iPhone (native iOS), khusus Android (native Android), dan toko online yang bisa diakses dari HP mana pun (web app / hybrid).

### Jenis Aplikasi Mobile
```
┌──────────────────────────────────────────────────────┐
│                  JENIS APLIKASI MOBILE               │
├──────────────┬──────────────┬────────────────────────┤
│  Native iOS  │ Native       │ Hybrid / Cross-platform│
│              │ Android      │                        │
│  Bahasa:     │ Bahasa:      │ Bahasa:                │
│  Swift       │ Kotlin/Java  │ Flutter, React Native  │
│  Toko:       │ Toko:        │ Satu kode untuk semua  │
│  App Store   │ Play Store   │ platform               │
│              │              │                        │
│  ✅ Performa │ ✅ Performa  │ ✅ Hemat waktu         │
│  ❌ Mahal    │ ❌ Mahal     │ ❌ Performa kurang     │
└──────────────┴──────────────┴────────────────────────┘
```

### App Inventor — Cara Mudah Buat Aplikasi!
**MIT App Inventor** adalah platform **drag-and-drop** untuk membuat aplikasi Android tanpa coding rumit.

```python
# Di App Inventor, kamu "coding" dengan memblok visual:
# ┌─────────────────────────┐
# │ when Button1.Click     │
# │   do set Label1.Text   │
# │      to "Halo Dunia!"  │
# └─────────────────────────┘
```

| Komponen | Fungsi | Seperti di Coding |
|----------|--------|-------------------|
| **Button** | Tombol yang bisa diklik | Event handler |
| **Label** | Teks yang ditampilkan | Variable output |
| **TextBox** | Input teks dari user | Input |
| **Notifier** | Pesan pop-up | Alert/Toast |
| **TinyDB** | Simpan data lokal | Database lokal |

### 🔍 Cek Pemahaman
1. Sebutkan 3 jenis aplikasi mobile! Apa kelebihan dan kekurangan masing-masing?
2. Apa itu MIT App Inventor? Mengapa platform ini cocok untuk pemula?
3. Komponen App Inventor apa yang berfungsi seperti "variable output" dalam pemrograman teks?

### 📋 Studi Kasus
OSIS SMA ingin membuat **aplikasi informasi sekolah** yang bisa diakses semua siswa. Aplikasi ini harus menampilkan jadwal pelajaran, pengumuman, dan daftar ekstrakurikuler. Ketua OSIS bertanya padamu apakah sebaiknya aplikasi dibuat native Android (Kotlin), iOS (Swift), atau menggunakan App Inventor.

**Analisis:**
1. Platform mana yang paling tepat untuk proyek ini? Pertimbangkan biaya, waktu, dan keahlian tim!
2. Fitur apa saja yang bisa dibuat dengan App Inventor untuk aplikasi informasi sekolah ini?

> 🤔 **Mari Renungkan:** Apa hal paling menarik yang kamu pelajari dari bagian ini?

---

## B. Membangun UI dengan App Inventor

### 🎨 Membangun UI dengan App Inventor

### Designer — Tampilan Aplikasi
Di App Inventor, ada 2 bagian utama: **Designer** (tampilan) dan **Blocks** (logika).

```
┌────────────────────────────────────────────────────┐
│              APP INVENTOR DESIGNER                 │
├────────────────────────────────────────────────────┤
│                                                    │
│   ┌──────────────────────────────┐                 │
│   │       JUDUL APLIKASI         │ ← Label        │
│   ├──────────────────────────────┤                 │
│   │                              │                 │
│   │  [ Masukkan nama kamu ]      │ ← TextBox      │
│   │                              │                 │
│   │   ┌──────────────────────┐   │                 │
│   │   │     SAYA HALO!       │   │ ← Button       │
│   │   └──────────────────────┘   │                 │
│   │                              │                 │
│   │   ┌──────────────────────┐   │                 │
│   │   │   Halo, Dani!        │   │ ← Label (hasil) │
│   │   └──────────────────────┘   │                 │
│   └──────────────────────────────┘                 │
│                                                    │
├────────────────────────────────────────────────────┤
│ Palette: Button, Label, TextBox, ListView, ...    │
└────────────────────────────────────────────────────┘
```

### Komponen Dasar UI
| Komponen | Letak di Palette | Fungsi |
|----------|-----------------|--------|
| **Button** | User Interface | Tombol interaktif |
| **Label** | User Interface | Teks statis/dinamis |
| **TextBox** | User Interface | Input teks |
| **Image** | User Interface | Tampilkan gambar |
| **ListView** | User Interface | Daftar pilihan |
| **HorizontalArrangement** | Layout | Atur komponen horizontal |
| **VerticalArrangement** | Layout | Atur komponen vertikal |
| **Notifier** | User Interface | Pesan pop-up |

### 📝 Tugas: Buat Aplikasi "Perkenalan"
**Fitur:** Input nama → Klik tombol → Muncul "Halo, [nama]!"

> ✍️ **Langkah:** 1) Seret Label, TextBox, Button, Label (hasil). 2) Atur properti (teks, warna, ukuran). 3) Buat blok: when Button.Click → set LabelHasil.Text ke "Halo, " + TextBox.Text

### 🔍 Cek Pemahaman
1. Sebutkan 5 komponen UI dasar di App Inventor dan fungsinya!
2. Apa perbedaan antara HorizontalArrangement dan VerticalArrangement?
3. Jelaskan cara membuat aplikasi "Halo, [nama]!" menggunakan App Inventor!

### 📋 Studi Kasus
Kamu diminta membuat **aplikasi perpustakaan sekolah** sederhana. Aplikasi harus memiliki: judul "Perpustakaan SMA", kolom pencarian buku, tombol "Cari", dan area hasil pencarian. Temanmu sudah membuat desain di kertas, dan kamu perlu mewujudkannya di App Inventor.

**Analisis:**
1. Komponen UI apa saja yang diperlukan untuk membuat aplikasi tersebut? Gambarkan tata letaknya!
2. Buatlah blok logika sederhana untuk tombol "Cari" — ketika diklik, tampilkan "Mencari..." di label hasil!

> 🤔 **Mari Renungkan:** Apa hal paling menarik yang kamu pelajari dari bagian ini?

---

## C. Navigasi & Penyimpanan Data

### 🔄 Navigasi & Penyimpanan Data

### Navigasi Antar Screen
Aplikasi biasanya punya lebih dari 1 layar. App Inventor mendukung **multi-screen**.

```
Screen1 (Menu)          Screen2 (Detail)
┌──────────────────┐    ┌──────────────────┐
│  📱 Aplikasi Ku  │    │  Detail Item     │
│                  │    │                  │
│  [☰ Lihat Data]──────►│  Nama: Andi      │
│  [➕ Tambah]     │    │  Kelas: XI       │
│  [ℹ️ Tentang]    │    │  [◀ Kembali]──────►│
└──────────────────┘    └──────────────────┘
```

```blocks
# Blok untuk pindah screen
when ButtonLihat.Click
    do open another screen screenName "Screen2"
```

### Menyimpan Data dengan TinyDB
**TinyDB** adalah database lokal yang menyimpan data **key-value** (seperti kamus/dictionary di Python).

```python
# Konsep TinyDB seperti dictionary Python:
data = {"nama": "Andi", "kelas": "XI"}

# Di App Inventor:
# ┌──────────────────────────────────────┐
# │ call TinyDB1.StoreValue              │
# │   tag     "nama"                     │ ── Simpan
# │   valueToStore "Andi"                │
# └──────────────────────────────────────┘
# ┌──────────────────────────────────────┐
# │ call TinyDB1.GetValue                │
# │   tag     "nama"                     │ ── Ambil
# │   valueIfTagNotThere ""              │
# └──────────────────────────────────────┘
```

| Screen | Fungsi | Data yang Disimpan | 
|--------|--------|-------------------|
| **Screen1** | Form input | Nama, kelas ke TinyDB |
| **Screen2** | Tampilkan data | Baca dari TinyDB |

> ✍️ **Latihan:** Buat aplikasi catatan harian dengan TextBox untuk input dan TinyDB untuk menyimpan!

### 🔍 Cek Pemahaman
1. Bagaimana cara pindah dari Screen1 ke Screen2 di App Inventor?
2. Apa perbedaan TinyDB dengan variabel biasa? Kapan sebaiknya menggunakan TinyDB?
3. Jelaskan konsep penyimpanan key-value pada TinyDB menggunakan analogi kamus!

### 📋 Studi Kasus
Seorang siswa bernama Fajar ingin membuat **aplikasi catatan harian (diary)**. Aplikasi memiliki 2 screen: Screen1 untuk menulis catatan dengan TextBox dan tombol "Simpan", Screen2 untuk menampilkan daftar semua catatan yang sudah disimpan. Fajar bingung bagaimana menyimpan catatan agar tidak hilang saat aplikasi ditutup.

**Analisis:**
1. Komponen App Inventor apa yang sebaiknya Fajar gunakan untuk menyimpan catatan? Mengapa?
2. Buatlah alur logika (pseudocode/blocks) untuk proses: tulis catatan → simpan → tampilkan di Screen2!

> 🤔 **Mari Renungkan:** Apa hal paling menarik yang kamu pelajari dari bagian ini?

---

## D. Integrasi Library AI ke Aplikasi

### 🤖 Integrasi Library AI ke Aplikasi
**Library AI** adalah kumpulan fungsi siap pakai untuk menambahkan **kecerdasan buatan** ke aplikasi.

> 🧩 **Analogi:** Library AI itu seperti **indera buatan** untuk aplikasimu. Mau aplikasi bisa melihat? Tambahkan library computer vision. Mau bisa mendengar? Tambahkan library speech recognition. Mau bisa bicara? Tambahkan text-to-speech. **Aplikasi jadi punya "panca indera" digital!**

### Library AI di App Inventor
App Inventor punya **extension** (tambahan) untuk AI:

| Library AI | Kemampuan | Seperti Indera |
|-----------|-----------|---------------|
| **LookExtension** | Mengenali objek di gambar | Mata 👁️ |
| **SoundExtension** | Mengenali suara | Telinga 👂 |
| **TranslateExtension** | Menerjemahkan teks | Otak bahasa 🧠 |
| **TextToSpeech** | Membacakan teks | Mulut 🗣️ |
| **PersonalImageClassifier** | Belajar mengenali gambar sendiri | Belajar 🎓 |

### Cara Menambahkan Extension
```
1. Di App Inventor, buka menu Palette
2. Scroll ke bawah → Extension
3. Klik "Import extension"
4. Upload file .aix (extension file)
5. Extension siap digunakan!
```

### Contoh: Integrasi AI Look
```blocks
# Saat tombol ditekan, kamera aktif dan AI mengenali objek
when ButtonFoto.Click
    do call LookExtension1.Detect
            imageData Camera1.Picture

when LookExtension1.Detected
    # Hasil deteksi muncul di Label,
    # misal: "Saya melihat: mobil (95%)"
```

> 🔑 **Konsep Penting:** AI bukan magic — dia **belajar dari data**. Makin banyak data training, makin akurat hasilnya!

### 🔍 Cek Pemahaman
1. Apa yang dimaksud dengan Library AI? Berikan 3 contoh library AI di App Inventor!
2. Bagaimana cara menambahkan extension di App Inventor?
3. Mengapa AI membutuhkan data training yang banyak untuk bisa akurat?

### 📋 Studi Kasus
Dalam pelajaran Biologi, kelas XI mendapat tugas **mengidentifikasi tanaman obat** di sekitar sekolah. Ada 20 jenis tanaman yang harus dikenali. Seorang siswa bernama Dewi ingin membuat aplikasi yang bisa mengenali tanaman obat hanya dengan memotretnya menggunakan HP.

**Analisis:**
1. Library AI apa yang paling tepat untuk aplikasi Dewi? Jelaskan cara kerjanya!
2. Jika aplikasi sering salah mengenali tanaman, apa yang perlu dilakukan? Jelaskan alasannya!

> 🤔 **Mari Renungkan:** Apa hal paling menarik yang kamu pelajari dari bagian ini?

---

## E. Image Classification & Speech Recognition

### 🖼️ Image Classification & Speech Recognition
Dua kemampuan AI yang paling populer: **mengenali gambar** dan **mengenali suara**.

### Image Classification — AI Melihat
**Cara Kerja:**
```
[Input Gambar] → [AI Model] → [Hasil Klasifikasi]
     ↓              ↓                ↓
Foto kucing    CNN (Convolutional    "Kucing"
dari kamera    Neural Network)        (confidence: 95%)
```

### Aktivitas: Klasifikasi Gambar
1. Ambil foto 3 benda berbeda (buku, botol, pensil)
2. Gunakan LookExtension untuk mendeteksi
3. Catat: apakah AI benar? Seberapa yakin?

| Benda | Hasil Deteksi | Confidence | Benar/Salah |
|-------|--------------|------------|-------------|
| Buku tulis | "Book" | 92% | ✅ |
| Botol minum | "Water bottle" | 87% | ✅ |
| Pensil | "Pencil" | 76% | ✅ |

### Speech Recognition — AI Mendengar
**Cara Kerja:**
```
[Suara] → [Speech-to-Text] → [Teks]
"Halo, apa kabar?"           "Halo apa kabar"
```

### Aktivitas: Aplikasi Voice Note
Buat aplikasi yang bisa:
1. Merekam suara (klik tombol → bicara)
2. Mengubah suara menjadi teks
3. Menyimpan teks ke TinyDB

```blocks
when ButtonRekam.Click
    do call SoundExtension1.Recognize

when SoundExtension1.AfterRecognize
    do set LabelHasil.Text to result
       call TinyDB1.StoreValue tag "catatan" value result
```

> 💡 **Tahukah Kamu?** Siri, Google Assistant, dan Alexa menggunakan teknologi yang sama — Speech Recognition + NLP!

### 🔍 Cek Pemahaman
1. Jelaskan cara kerja Image Classification menggunakan CNN!
2. Bagaimana Speech Recognition mengubah suara menjadi teks?
3. Apa yang dimaksud dengan "confidence score" dalam hasil deteksi AI? Mengapa penting?

### 📋 Studi Kasus
Di sekolah kamu ada seorang siswa tunanetra bernama Bagas yang kesulitan mencatat pelajaran. Kamu ingin membuat **aplikasi voice note** yang bisa merekam penjelasan guru, mengubahnya menjadi teks, dan menyimpannya. Ini akan sangat membantu Bagas dan teman-teman lain.

**Analisis:**
1. Fitur AI apa saja yang diperlukan untuk aplikasi voice note tersebut? Jelaskan alurnya!
2. Jika guru menjelaskan dalam 3 bahasa (Indonesia, Inggris, Jawa), tantangan apa yang mungkin muncul? Bagaimana solusinya?

> 🤔 **Mari Renungkan:** Apa hal paling menarik yang kamu pelajari dari bagian ini?

---

## F. Proyek Aplikasi AI: Perencanaan

### 📋 Proyek Aplikasi AI: Perencanaan

### Tugas Akhir Bab 5
Buatlah **aplikasi mobile berbasis AI** untuk menyelesaikan masalah nyata di sekitar sekolah/rumah!

### Ide Proyek
| Proyek | Fitur AI | Masalah yang Diselesaikan |
|--------|----------|--------------------------|
| **Pengenal Tanaman Obat** | Image Classification | Tanaman obat sulit dikenali |
| **Penerjemah Bahasa Daerah** | Text Translation | Melestarikan bahasa daerah |
| **Pengingat Tugas Sekolah** | Text-to-Speech + TinyDB | Suka lupa tugas |
| **Detektor Sampah Organik** | Image Classification | Sulit memilah sampah |
| **Aplikasi Belajar Bahasa Inggris** | Speech Recognition | Latihan pronunciation |

### Rencana Proyek (Template)
| Aspek | Isian |
|-------|-------|
| **Nama Aplikasi** | ... |
| **Anggota Tim** | ... |
| **Masalah** | ... |
| **Fitur Utama** | 1. ... 2. ... 3. ... |
| **AI Library yang Digunakan** | ... |
| **Desain UI** | (sketsa/layout) |
| **Pembagian Tugas** | ... |
| **Target Selesai** | ... |

> 💡 **Tips Memilih Proyek:** Pilih masalah yang kamu ALAMI sendiri — kamu akan lebih termotivasi menyelesaikannya!

### 🔍 Cek Pemahaman
1. Sebutkan 3 ide proyek aplikasi AI yang bisa dibuat dengan App Inventor!
2. Apa saja komponen yang harus ada dalam rencana proyek aplikasi?
3. Mengapa penting memilih masalah yang kamu alami sendiri sebagai topik proyek?

### 📋 Studi Kasus
Kelompokmu (5 orang) mendapat tugas proyek aplikasi AI. Setiap anggota memiliki ide berbeda: Andi ingin membuat aplikasi pengenal sampah organik, Budi ingin membuat penerjemah bahasa Sunda, Citra ingin membuat pengingat tugas sekolah, Dewi ingin membuat detektor kemacetan, dan Eko ingin membuat aplikasi belajar Bahasa Inggris.

**Analisis:**
1. Bantulah kelompokmu memilih SATU ide proyek yang paling layak! Pertimbangkan: waktu (2 minggu), keahlian, data yang tersedia, dan dampak!
2. Buatlah rencana proyek lengkap untuk ide yang terpilih (nama, fitur, AI library, pembagian tugas)!

> 🤔 **Mari Renungkan:** Apa hal paling menarik yang kamu pelajari dari bagian ini?

---

## G. Proyek Aplikasi AI: Implementasi & Presentasi

### 🚀 Proyek Aplikasi AI: Implementasi & Presentasi

### Tahap Implementasi
```python
# Pseudocode alur implementasi:

# 1. SETUP
- Buka App Inventor
- Buat project baru
- Import extension AI yang dibutuhkan

# 2. DESIGNER
- Buat Screen1 (input/utama)
- Buat Screen2 (hasil)
- Tambahkan komponen: Button, Label, Camera, dll

# 3. BLOCKS (logika)
- when Button.Click → aktifkan fitur AI
- when AI.Detected → tampilkan hasil
- Simpan data ke TinyDB

# 4. TESTING
- Uji coba di emulator/smartphone
- Catat bug dan perbaiki

# 5. FINAL
- Build APK
- Siapkan slide presentasi
```

### Rubrik Penilaian Proyek
| Aspek | Bobot | Kriteria |
|-------|-------|----------|
| **Fungsionalitas** | 30% | Aplikasi berjalan tanpa error |
| **Fitur AI** | 25% | AI berfungsi dengan baik |
| **UI/UX** | 15% | Tampilan rapi, mudah digunakan |
| **Dokumentasi** | 15% | Laporan lengkap |
| **Presentasi** | 15% | Demo lancar, menjelaskan dengan baik |

### Tips Presentasi
1. **Mulai dengan masalah** — kenapa aplikasi ini penting?
2. **Demo langsung** — tunjukkan aplikasi bekerja (bukan slide!)
3. **Ceritakan kendala** — jujur tentang kesulitan dan bagaimana mengatasinya
4. **Refleksikan pembelajaran** — apa yang paling berkesan dari proyek ini?

> 🎯 **Ingat:** Proyek ini bukan cuma soal nilai. Ini **portofolio pertamamu** sebagai developer! Simbaik baik-baik untuk bekal masa depan.

### 🔍 Cek Pemahaman
1. Sebutkan 5 tahap implementasi proyek aplikasi AI!
2. Apa saja aspek yang dinilai dalam rubrik penilaian proyek? Mana yang bobotnya paling besar?
3. Mengapa penting untuk memulai presentasi dengan "masalah" bukan dengan "fitur aplikasi"?

### 📋 Studi Kasus
Hari presentasi proyek tiba. Kelompok Rina membuat aplikasi "EcoScan" — pendeteksi jenis sampah menggunakan Image Classification. Saat demo di depan kelas, aplikasi tiba-tiba crash saat memotret sampah plastik. Rina panik dan tidak tahu harus berbuat apa.

**Analisis:**
1. Apa yang sebaiknya Rina lakukan saat demo mengalami error? Berikan strategi menghadapi situasi tersebut!
2. Setelah presentasi, bagaimana cara Rina memperbaiki aplikasinya? Langkah debugging apa yang harus dilakukan?

> 🤔 **Mari Renungkan:** Apa hal paling menarik yang kamu pelajari dari bagian ini?

---

---
## 🏗️ Proyek Mini: 🤖 Prototipe Aplikasi AI

Buat aplikasi Android sederhana di MIT App Inventor yang mengintegrasikan 1 fitur AI (LookExtension untuk klasifikasi gambar, SoundExtension untuk pengenal suara, atau TextToSpeech). Aplikasi harus menyelesaikan masalah nyata.

**Alat dan Bahan:**
- MIT App Inventor (ai2.appinventor.mit.edu)
- Akun Gmail (untuk login)
- Smartphone Android (untuk uji coba)
- AI Extension (.aix): LookExtension / SoundExtension / TextToSpeech

**Langkah-langkah:**
1. Tentukan masalah nyata yang akan diselesaikan (misal: aplikasi pengenal tanaman obat, atau voice note untuk tunanetra).
2. Buka MIT App Inventor, buat project baru, dan impor extension AI yang dibutuhkan (.aix).
3. Desain UI: buat screen utama dengan Button, Label, Kamera, dan komponen lain yang diperlukan.
4. Buat blok logika: tombol aktifkan AI → tangkap gambar/rekam suara → panggil extension → tampilkan hasil.
5. Uji coba aplikasi di smartphone Android — catat bug dan perbaiki.
6. Build APK, presentasikan aplikasi ke kelas — tunjukkan fitur AI bekerja secara real-time.

> **Output:** File project (.aia) + file APK + presentasi demo 5-7 menit

## 📝 Rangkuman

- Aplikasi mobile terdiri dari 3 jenis: **Native iOS** (Swift), **Native Android** (Kotlin/Java), dan **Hybrid/Cross-platform** (Flutter, React Native).
- **MIT App Inventor** adalah platform drag-and-drop untuk membuat aplikasi Android dengan dua bagian utama: **Designer** (tampilan) dan **Blocks** (logika).
- **Library AI** seperti LookExtension, SoundExtension, dan TextToSpeech memungkinkan aplikasi memiliki ‘panca indera digital’ — melihat, mendengar, dan berbicara.
- **Image Classification** menggunakan CNN untuk mengenali objek di gambar, sedangkan **Speech Recognition** mengubah suara menjadi teks.
- Proyek akhir bab ini adalah membuat **aplikasi mobile berbasis AI** untuk menyelesaikan masalah nyata — mulai dari perencanaan, implementasi di App Inventor, hingga presentasi.

---
## ✍️ Latihan Soal

### Pilihan Ganda

1. MIT App Inventor adalah platform untuk membuat aplikasi...
   a. iOS native
   b. Android native dengan drag-and-drop
   c. Web app dengan JavaScript
   d. Desktop app dengan Python
   e. Hybrid app dengan React Native
   **Kunci Jawaban: B**

2. Komponen App Inventor yang berfungsi menyimpan data lokal secara key-value adalah...
   a. Notifier
   b. TextBox
   c. TinyDB
   d. ListView
   e. Balloon
   **Kunci Jawaban: C**

3. Library AI pada App Inventor yang berfungsi mengenali objek di gambar adalah...
   a. TextToSpeech
   b. TranslateExtension
   c. SoundExtension
   d. LookExtension
   e. PersonalImageClassifier
   **Kunci Jawaban: D**

4. CNN dalam konteks AI adalah singkatan dari...
   a. Central Neural Network
   b. Convolutional Neural Network
   c. Computer Network Node
   d. Complex Numerical Notation
   e. Continuous Natural Network
   **Kunci Jawaban: B**

5. Extension App Inventor memiliki ekstensi file...
   a. .apk
   b. .aix
   c. .app
   d. .aia
   e. .exe
   **Kunci Jawaban: B**

### Uraian

1. Jelaskan perbedaan antara aplikasi mobile native (iOS/Android) dengan aplikasi hybrid/cross-platform! Apa kelebihan dan kekurangan masing-masing?

2. Bagaimana cara membangun aplikasi sederhana dengan MIT App Inventor? Jelaskan langkah-langkah dari Designer hingga Blocks!

3. Apa yang dimaksud dengan Library AI? Jelaskan 3 library AI yang tersedia di App Inventor dan fungsinya masing-masing!

4. Jelaskan cara kerja Image Classification dan Speech Recognition! Bagaimana kedua teknologi ini dapat diterapkan dalam aplikasi mobile?

---
## 📋 Rubrik Penilaian Proyek

| Aspek | Kurang | Cukup | Baik |
|-------|--------|-------|------|
| Fungsionalitas Aplikasi | Aplikasi crash atau tidak jalan | Aplikasi berjalan dengan bug minor | Aplikasi berjalan sempurna, stabil |
| Fitur AI | Fitur AI tidak berfungsi | Fitur AI berfungsi tapi kurang akurat | Fitur AI akurat dan responsif |
| UI/UX Design | Tampilan berantakan, sulit digunakan | Tampilan cukup rapi, mudah digunakan | Tampilan profesional, intuitif, estetis |
| Presentasi Demo | Tidak bisa demo, tidak siap | Demo berjalan, penjelasan cukup | Demo lancar, menjelaskan dengan percaya diri |

---
## 🚀 Tugas Pengayaan

### 📱 Eksplorasi Extension AI App Inventor
Jelajahi halaman [MIT App Inventor Extensions](https://appinventor.mit.edu/extensions) dan cari 3 extension AI yang belum dibahas di kelas. Untuk setiap extension, tulis: nama, fungsi, cara kerja, dan 1 ide aplikasi yang bisa dibuat menggunakan extension tersebut.

### 🤖 Tutorial AI untuk Pemula
Tonton video YouTube *'Cara Kerja Neural Network'* dan *'Apa itu CNN?'* (cari dengan bahasa Indonesia). Buat mind map konsep AI yang mencakup: Neural Network, CNN, Training Data, Confidence Score, dan contoh penerapan di kehidupan sehari-hari.

---
## 📖 Glosarium

- **Native App**: Aplikasi yang dibuat khusus untuk satu platform (iOS/Android) menggunakan bahasa spesifik platform.
- **Hybrid App**: Aplikasi multi-platform yang dibuat dengan satu basis kode untuk berbagai sistem operasi.
- **MIT App Inventor**: Platform drag-and-drop untuk membuat aplikasi Android tanpa coding rumit.
- **TinyDB**: Database lokal pada App Inventor yang menyimpan data dalam format key-value.
- **Library AI**: Kumpulan fungsi siap pakai untuk menambahkan kecerdasan buatan ke dalam aplikasi.
- **CNN**: Convolutional Neural Network — arsitektur jaringan saraf tiruan untuk pengenalan gambar.
- **Image Classification**: Teknologi AI yang mengenali dan mengklasifikasikan objek dalam gambar.
- **Speech Recognition**: Teknologi yang mengubah suara manusia menjadi teks.

---
## 📺 Sumber & Media Pembelajaran

| Platform | Sumber | Tautan | Keterangan |
|----------|--------|--------|------------|
| Website | MIT App Inventor | `https://appinventor.mit.edu/` | Platform resmi MIT App Inventor |
| YouTube | Tutorial App Inventor Pemula | `youtu.be/search?q=tutorial+app+inventor+indonesia` | Panduan membuat aplikasi dengan App Inventor |
| YouTube | Apa itu AI? Pengenalan AI | `youtu.be/search?q=apa+itu+AI+indonesia` | Konsep dasar kecerdasan buatan |
| YouTube | Image Classification dengan AI | `youtu.be/search?q=image+classification+AI` | Cara kerja klasifikasi gambar dengan CNN |
| Website | AI Extension App Inventor | `https://appinventor.mit.edu/extensions` | Koleksi extension AI untuk App Inventor |
