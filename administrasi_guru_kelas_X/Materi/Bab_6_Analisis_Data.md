# 📊 Bab 6: Analisis Data

> **Semester Genap** | **Fase E** | **Kelas X** | **15 JP**

---

## 📊 Pemetaan Capaian Pembelajaran

| Elemen CP | Deskripsi CP |
|-----------|-------------|
| Analisis Data | Mengolah dan memvisualisasikan data menggunakan spreadsheet untuk mendukung pengambilan keputusan. |

---

## 🎯 Tujuan Pembelajaran

- **A.** Pengertian Data dan Informasi
- **B.** Pengolahan Data dengan Spreadsheet
- **C.** Visualisasi Data

## 🗺️ Peta Konsep

```
               📊 ANALISIS DATA
                     |
                     ├── A. Pengertian Data dan Informasi
                     ├── B. Pengolahan Data dengan Spreadsheet
                     └── C. Visualisasi Data
```

## A. Pengertian Data dan Informasi

### 📊 Pengertian Data dan Informasi

**Data** adalah fakta mentah yang belum memiliki makna. **Informasi** adalah data yang sudah diolah sehingga bermakna dan berguna.

> 🧩 **Analogi:** Data itu seperti **biji kopi** — masih mentah, belum bisa dinikmati. Informasi adalah **secangkir kopi hangat** — sudah diolah, siap dinikmati, dan memberi manfaat. Proses dari biji ke cangkir disebut **pengolahan data**.

### Perbedaan Data dan Informasi

| Aspek | Data | Informasi |
|-------|------|-----------|
| **Bentuk** | Mentah, belum diolah | Sudah diolah, bermakna |
| **Nilai** | Belum berguna langsung | Berguna untuk pengambilan keputusan |
| **Contoh** | "35°C", "Rp50.000", "Senin" | "Suhu hari ini panas — 35°C", "Uang jajan saya Rp50.000 untuk seminggu" |
| **Hubungan** | Bahan baku | Hasil olahan |

### Contoh: Dari Data ke Informasi

```
                DATA MENTAH
                ┌──────────┐
                │ 85, 90   │
                │ 78, 88   │
                │ 92, 76   │
                │ 80        │ ← Nilai dari 7 siswa
                └──────────┘
                     │
                     ▼ Pengolahan
                ┌──────────────────┐
                │ Rata-rata = 84.1  │
                │ Tertinggi = 92   │
                │ Terendah = 76    │
                │ Lulus semua ✅   │
                └──────────────────┘
                     │
                     ▼
                ┌──────────────────┐
                │ KELAS X-A:       │
                │ Nilai Informatika│
                │ ✅ Rata-rata BAIK│
                │ ★ Nilai terbaik │
                │   = 92 (Lisa)   │
                └──────────────────┘
```

### Karakteristik Informasi yang Baik

1. **Akurat** — Bebas dari kesalahan
2. **Tepat Waktu** — Tersedia saat dibutuhkan
3. **Relevan** — Sesuai dengan kebutuhan
4. **Lengkap** — Tidak setengah-setengah
5. **Jelas** — Mudah dipahami

### 📌 Contoh Nyata

**Gojek:**
1. Data: GPS tracking driver (koordinat setiap 5 detik)
2. Informasi: "Driver kamu sudah dekat, estimasi 2 menit sampai"
3. Keputusan: Kamu siap-siap ke titik jemput

**Sekolah:**
1. Data: Nilai ulangan seluruh siswa
2. Informasi: "Rata-rata kelas 84.1 — bagus! Tapi masih ada 3 siswa perlu remedial"
3. Keputusan: Guru memberikan program remedial

### 🔍 Cek Pemahaman
1. Jelaskan perbedaan antara data dan informasi!
2. Sebutkan 5 karakteristik informasi yang baik!
3. Berikan contoh proses perubahan data menjadi informasi di lingkungan sekolah!

### 📋 Studi Kasus
Seorang wali kelas memiliki data mentah nilai 30 siswa untuk 5 mata pelajaran. la ingin mengetahui siapa siswa yang paling berprestasi, rata-rata nilai kelas per mata pelajaran, dan berapa banyak siswa yang remedial.

**Pertanyaan:**
1. Termasuk data atau informasikah nilai mentah 30 siswa tersebut?
2. Informasi apa saja yang bisa dihasilkan dari data tersebut untuk membantu wali kelas mengambil keputusan?

> 🤔 **Refleksi:** Ambil 3 contoh data di sekitarmu (suhu ruangan, nilai, jadwal pelajaran), lalu ubah menjadi informasi yang bermakna!

> 🤔 **Mari Renungkan:** Apa hal paling menarik yang kamu pelajari dari bagian ini?

---

## B. Pengolahan Data dengan Spreadsheet

### 📈 Pengolahan Data dengan Spreadsheet

Spreadsheet adalah aplikasi yang memungkinkan kita mengolah data dalam bentuk **tabel baris dan kolom**. Contoh: Microsoft Excel, Google Sheets, LibreOffice Calc.

> 🧩 **Analogi:** Spreadsheet itu seperti **papan catur raksasa** dengan 1.048.576 baris dan 16.384 kolom. Setiap kotak (cell) bisa diisi angka, teks, atau rumus. Kalau kamu mengubah satu angka, semua hasil perhitungan akan otomatis menyesuaikan. Ajaib!

### Pengenalan Spreadsheet

```
   ┌───────┬──────┬──────┬──────┬──────┐
   │       │  A   │  B   │  C   │  D   │
   ├───────┼──────┼──────┼──────┼──────┤
   │   1   │ Nama │ Tugas│ UTS  │ UAS  │ ← Header
   ├───────┼──────┼──────┼──────┼──────┤
   │   2   │Andi  │  85  │  78  │  90  │
   ├───────┼──────┼──────┼──────┼──────┤
   │   3   │Budi  │  90  │  88  │  85  │
   ├───────┼──────┼──────┼──────┼──────┤
   │   4   │Cici  │  75  │  80  │  82  │
   ├───────┼──────┼──────┼──────┼──────┤
   │   5   │      │      │      │      │
   ├───────┼──────┼──────┼──────┼──────┤
   │   6   │Rata2 │ =AVERAGE│       │
   └───────┴──────┴──────┴──────┴──────┘
           ↑ Cell A1 (kolom A, baris 1)
```

### Fungsi Dasar Spreadsheet

| Fungsi | Cara Penulisan | Kegunaan |
|--------|---------------|----------|
| **SUM** | `=SUM(A1:A10)` | Menjumlahkan semua angka |
| **AVERAGE** | `=AVERAGE(B2:B10)` | Menghitung rata-rata |
| **MAX** | `=MAX(C2:C10)` | Nilai tertinggi |
| **MIN** | `=MIN(D2:D10)` | Nilai terendah |
| **COUNT** | `=COUNT(A2:A10)` | Menghitung jumlah data (angka) |
| **IF** | `=IF(B2>75,"LULUS","REMEDIAL")` | Percabangan/kondisi |

### Operator Dasar

```
+  Penjumlahan    =A1+B1
-  Pengurangan    =A1-B1
*  Perkalian      =A1*B1
/  Pembagian      =A1/B1
^  Pangkat        =A1^2    (A1 kuadrat)
%  Persen         =A1*10%  (10% dari A1)
```

### Contoh Praktik: Daftar Nilai

| A | B | C | D | E | F |
|---|---|---|---|---|---|
| **Nama** | **Tugas** | **UTS** | **UAS** | **Nilai Akhir** | **Keterangan** |
| Andi | 85 | 78 | 90 | `=B2*0.2+C2*0.3+D2*0.5` | `=IF(E2>75,"LULUS","REMEDIAL")` |
| Budi | 90 | 88 | 85 | `=B3*0.2+C3*0.3+D3*0.5` | `=IF(E3>75,"LULUS","REMEDIAL")` |

**Rumus Nilai Akhir:** Tugas (20%) + UTS (30%) + UAS (50%)

### 📌 Contoh Nyata

**Seorang bendahara OSIS** menggunakan Google Sheets untuk mencatat:
- Pemasukan (iuran, sponsor)
- Pengeluaran (kegiatan, konsumsi)
- Saldo otomatis dengan `=SUM(pemasukan) - SUM(pengeluaran)`
- Semua bisa diakses bersama secara real-time!

### 🔍 Cek Pemahaman
1. Sebutkan 4 fungsi dasar spreadsheet dan kegunaannya!
2. Apa yang dimaksud dengan cell, row, dan column di spreadsheet?
3. Bagaimana cara menulis rumus di spreadsheet? Berikan contoh!

### 📋 Studi Kasus
Sebagai bendahara kelas, kamu diminta membuat laporan keuangan bulanan. Ada pemasukan dari iuran siswa (50 orang × Rp5.000) dan pengeluaran untuk kebersihan kelas (Rp50.000) serta alat tulis (Rp75.000).

**Pertanyaan:**
1. Buatlah rancangan spreadsheet dengan kolom yang sesuai!
2. Tuliskan rumus yang digunakan untuk menghitung total pemasukan, total pengeluaran, dan saldo akhir!

> 🤔 **Refleksi:** Buat spreadsheet sederhana untuk mencatat pengeluaran uang jajanmu selama seminggu! Gunakan rumus SUM untuk total!

> 🤔 **Mari Renungkan:** Apa hal paling menarik yang kamu pelajari dari bagian ini?

---

## C. Visualisasi Data

### 📉 Visualisasi Data

Visualisasi data adalah **penyajian data dalam bentuk gambar** seperti grafik, diagram, atau peta. Tujuannya agar data lebih mudah dipahami dan pola dalam data bisa terlihat jelas.

> 🧩 **Analogi:** Visualisasi data itu seperti **peta**. Bandingkan: teks "Jalan dari sekolah ke rumahku: belok kiri, lurus 500m, belok kanan, sampai" vs peta yang menunjukkan rute secara visual. Jelas lebih mudah dipahami dengan peta! Begitu juga dengan data — grafik membuat data "berbicara".

### Jenis-Jenis Grafik

```
Grafik Batang:        Grafik Garis:        Diagram Lingkaran:
Nilai per siswa       Tren penjualan       Anggaran OSIS
██                    ░░                    ┌─────┐
██ ██                ░░ ▒▒                 │  30%│
██ ██ ██            ░░   ▒▒                │     │
██ ██ ██ ██        ░░     ▒▒               │45%  │
██ ██ ██ ██ ██    ░░       ▒▒              │     │
A  B  C  D  E     Jan-Feb-Mar-Apr          └─────┘
```

### Kapan Menggunakan Grafik Apa?

| Jenis Grafik | Cocok untuk | Contoh |
|-------------|-------------|--------|
| **Batang** | Membandingkan data antar kategori | Nilai per siswa, penjualan per produk |
| **Garis** | Melihat tren/perubahan seiring waktu | Suhu harian, kenaikan pengguna Gojek |
| **Lingkaran** | Proporsi / bagian dari keseluruhan | Persentase anggaran, asal kota siswa |
| **Scatter** | Hubungan antara 2 variabel | Korelasi jam belajar vs nilai |
| **Histogram** | Distribusi frekuensi | Sebaran nilai ulangan |

### Cara Membuat Grafik di Google Sheets

```
Langkah 1: Siapkan data di tabel
┌──────────┬───────┐
│  Bulan   │ Suhu  │
├──────────┼───────┤
│ Jan      │  28   │
│ Feb      │  29   │
│ Mar      │  30   │
│ Apr      │  31   │
└──────────┴───────┘

Langkah 2: Blok data → Insert → Chart
Langkah 3: Pilih "Line chart"
```

### Aturan Visualisasi yang Baik

1. ✅ **Sederhana** — Jangan terlalu ramai
2. ✅ **Label jelas** — Sumbu X, Y, legend, judul
3. ✅ **Warna kontras** — Bisa dibedakan dengan mudah
4. ✅ **Skala sesuai** — Jangan menyesatkan dengan skala yang dipotong
5. ❌ **Jangan 3D tanpa perlu** — 3D sering bikin data sulit dibaca

### 📌 Contoh Nyata

**Gojek memvisualisasikan:**
- Jumlah pesanan per jam (grafik garis → jam sibuk jam 7 pagi & 12 siang)
- Daerah dengan order terbanyak (peta panas → Jakarta, Bandung, Surabaya)
- Persentase jenis layanan (lingkaran → GoRide 45%, GoCar 30%, GoFood 25%)

Dengan visualisasi ini, Gojek bisa memutuskan: di mana harus menambah driver, jam berapa promo makanan, dan sebagainya.

### 🔍 Cek Pemahaman
1. Sebutkan 4 jenis grafik dan kapan waktu yang tepat menggunakannya!
2. Apa aturan visualisasi data yang baik?
3. Mengapa grafik lebih efektif daripada tabel untuk menyampaikan informasi?

### 📋 Studi Kasus
OSIS sekolah ingin menyajikan data penggunaan anggaran tahun ini kepada seluruh siswa dalam acara LDKS. Data mereka: konsumsi 40%, acara 30%, dokumentasi 10%, transportasi 15%, dan cadangan 5%.

**Pertanyaan:**
1. Jenis grafik apa yang paling tepat untuk menyajikan data tersebut? Mengapa?
2. Buatlah visualisasi sederhana menggunakan ASCII art atau deskripsikan bagaimana tampilan grafiknya!

> 🤔 **Refleksi:** Kumpulkan data tinggi badan 10 temanmu, lalu buat grafik batang menggunakan Google Sheets. Pola apa yang kamu lihat?

> 🤔 **Mari Renungkan:** Apa hal paling menarik yang kamu pelajari dari bagian ini?

---

---
## 🏗️ Proyek Mini: Laporan Mini Survei 📊

Lakukan survei kecil kepada 10 teman tentang satu topik (misal: waktu belajar, aplikasi favorit, atau kebiasaan internet). Olah data di Google Sheets/Excel dan buat visualisasi grafik.

**Alat dan Bahan:**
- Google Sheets / Microsoft Excel
- Google Forms (opsional untuk survei)
- 10 teman sebagai responden

**Langkah-langkah:**
1. Tentukan topik survei dan buat 3-4 pertanyaan sederhana
2. Kumpulkan data dari 10 responden (teman sekelas)
3. Masukkan data ke spreadsheet dengan rapi (baris = responden, kolom = pertanyaan)
4. Hitung: jumlah, rata-rata, nilai tertinggi, nilai terendah menggunakan fungsi
5. Buat minimal 2 grafik (batang dan lingkaran) dari data yang ada
6. Tulis kesimpulan: temuan menarik apa yang kamu dapat dari survei ini?

> **Output:** File spreadsheet (.xlsx/.ods) + screenshot grafik + kesimpulan

---

## 📝 Rangkuman

- Data adalah fakta mentah; Informasi adalah data yang sudah diolah sehingga bermakna dan berguna untuk pengambilan keputusan.
- Spreadsheet (Excel/Google Sheets) memudahkan pengolahan data dengan fungsi SUM, AVERAGE, MAX, MIN, COUNT, dan IF.
- Visualisasi data (grafik batang, garis, lingkaran) membuat pola dalam data lebih mudah dipahami daripada tabel angka.

---

## ✍️ Latihan Soal

### A. Pilihan Ganda

1. Data yang sudah diolah sehingga memiliki makna disebut...
   a. Fakta
   b. Informasi
   c. Angka
   d. File
   e. Database
   **Kunci Jawaban: B**

2. Fungsi di spreadsheet untuk menjumlahkan data adalah...
   a. AVERAGE
   b. MAX
   c. SUM
   d. COUNT
   e. MIN
   **Kunci Jawaban: C**

3. Grafik yang paling cocok untuk melihat tren penjualan dari waktu ke waktu adalah...
   a. Batang
   b. Garis
   c. Lingkaran
   d. Scatter
   e. Histogram
   **Kunci Jawaban: B**

4. Nilai tertinggi dari sekumpulan data bisa diketahui dengan fungsi...
   a. MIN
   b. COUNT
   c. MAX
   d. SUM
   e. AVERAGE
   **Kunci Jawaban: C**

5. Fungsi IF di spreadsheet digunakan untuk...
   a. Menjumlahkan data
   b. Menghitung rata-rata
   c. Membuat percabangan kondisi
   d. Mencari nilai tertinggi
   e. Menghitung jumlah data
   **Kunci Jawaban: C**

### B. Uraian

1. Jelaskan perbedaan antara data dan informasi! Berikan 2 contoh di lingkungan sekolah!

2. Sebutkan 4 fungsi dasar spreadsheet (SUM, AVERAGE, MAX, IF) beserta cara penulisan dan kegunaannya!

3. Kapan sebaiknya menggunakan grafik batang, grafik garis, dan diagram lingkaran? Berikan contoh situasi!

4. Seorang ketua OSIS ingin menyajikan data pemasukan dan pengeluaran selama satu tahun. Bantu dia menjelaskan jenis grafik apa yang cocok dan alasannya!

---
## 📋 Rubrik Penilaian Proyek

| Aspek | Kurang | Cukup | Baik |
|-------|--------|-------|------|
| Kualitas Data Survei | Data tidak lengkap atau < 5 responden | Data cukup lengkap (5-7 responden) | Data lengkap (10 responden), rapi |
| Penggunaan Fungsi | Tidak menggunakan fungsi sama sekali | Menggunakan 2-3 fungsi dasar | Menggunakan SUM, AVERAGE, MAX, IF |
| Visualisasi Grafik | Grafik tidak sesuai atau tidak ada | Grafik ada tapi kurang tepat jenisnya | 2 grafik sesuai jenis data, rapi |
| Analisis & Kesimpulan | Tidak ada kesimpulan | Kesimpulan ada tapi umum | Kesimpulan mendalam dan berbasis data |

---

## 🚀 Tugas Pengayaan

### Proyek Data Real
Kumpulkan data nilai ujian 1 mata pelajaran dari 20 siswa (bisa minta ke guru). Hitung rata-rata, median, modus, nilai tertinggi, terendah. Buat 3 grafik berbeda dan tulis 3 temuan menarik.

### Eksplorasi Big Data
Cari artikel atau video tentang bagaimana Gojek/Shopee menggunakan data pengguna untuk meningkatkan layanan. Tulis ringkasan 1 paragraf dan jelaskan etika penggunaan data.

---

## 📖 Glosarium

- **Data**: Fakta mentah yang belum memiliki makna.
- **Informasi**: Data yang sudah diolah sehingga bermakna dan berguna untuk pengambilan keputusan.
- **Spreadsheet**: Aplikasi untuk mengolah data dalam tabel baris dan kolom (Excel, Google Sheets).
- **Visualisasi Data**: Penyajian data dalam bentuk grafik atau diagram agar mudah dipahami.
- **Grafik Batang**: Grafik untuk membandingkan data antar kategori.
- **Grafik Garis**: Grafik untuk melihat tren perubahan data seiring waktu.
- **Diagram Lingkaran**: Grafik untuk menunjukkan proporsi atau persentase.
- **Fungsi IF**: Fungsi di spreadsheet untuk membuat percabangan kondisi (if-then-else).

---
## 📺 Sumber & Media Pembelajaran

| Platform | Sumber | Tautan | Keterangan |
|----------|--------|--------|------------|
| YouTube | Apa itu Data vs Informasi? | `https://youtu.be/...search?q=data+dan+informasi+kelas+10` | Penjelasan perbedaan data dan informasi |
| YouTube | Belajar Google Sheets untuk Pemula | `https://youtu.be/...search?q=belajar+google+sheets+pemula` | Tutorial dasar Google Sheets dalam Bahasa Indonesia |
| Simulasi | PhET — Grafik dan Fungsi | `https://phet.colorado.edu/in/simulations/` | Simulasi untuk memahami visualisasi data dan grafik |
| Website | Google Sheets Training | `https://workspace.google.com/intl/id/training/` | Panduan resmi Google Sheets dari Google |
| YouTube | Cara Bikin Grafik di Excel | `https://youtu.be/...search?q=belajar+grafik+excel+indonesia` | Tutorial visualisasi data dengan Excel/Sheets |
