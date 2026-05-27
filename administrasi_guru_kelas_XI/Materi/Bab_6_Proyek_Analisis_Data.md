# 📊 Bab 6: Proyek Analisis Data

> **Semester Genap** | **Fase F** | **Kelas XI** | **25 JP**

---

## 📊 Pemetaan Capaian Pembelajaran

| Elemen CP | Deskripsi CP |
|-----------|-------------|
| Analisis Data (AD) | Menerapkan siklus pengolahan data mulai dari koleksi, pembersihan, analisis, hingga visualisasi |

---

## 🎯 Tujuan Pembelajaran

- **A.** Big Data: Era Data Raksasa
- **B.** Pengolahan Data dengan Tools Digital
- **C.** Visualisasi Data yang Menarik
- **D.** Proyek Analisis Data: Desain
- **E.** Proyek Analisis Data: Implementasi

## 🗺️ Peta Konsep

```
               📊 PROYEK ANALISIS DATA
                     |
                     ├── A. Big Data: Era Data Raksasa
                     ├── B. Pengolahan Data dengan Tools Digital
                     ├── C. Visualisasi Data yang Menarik
                     ├── D. Proyek Analisis Data: Desain
                     └── E. Proyek Analisis Data: Implementasi
```

## A. Big Data: Era Data Raksasa

### 📊 Big Data: Era Data Raksasa
**Big Data** adalah kumpulan data berukuran sangat besar yang tidak bisa diolah dengan cara tradisional.

> 🧩 **Analogi:** Big Data itu seperti **samudra**. Kalau mau ambil segelas air, cukup pakai gelas. Tapi kalau mau memindahkan seluruh samudra, butuh teknologi khusus. Big Data adalah "teknologi khusus" untuk mengelola data raksasa!

### 5V Big Data
```
1. VOLUME  — Ukuran besar (terabyte - petabyte)
2. VELOCITY — Kecepatan data masuk (real-time)
3. VARIETY  — Ragam jenis data (teks, gambar, video, sensor)
4. VERACITY — Ketidakpastian/kualitas data
5. VALUE   — Nilai/manfaat data setelah diolah
```

### Sumber Big Data
| Sumber | Contoh Data | Volume per Hari |
|--------|-------------|----------------|
| **Media Sosial** | Postingan, like, komentar | 500 juta tweet |
| **Sensor IoT** | Suhu, kelembaban, gerakan | Miliaran data point |
| **Transaksi** | Belanja online, transfer bank | Jutaan transaksi |
| **Video** | YouTube, CCTV, streaming | 500 jam video/menit |
| **Kesehatan** | Rekam medis, genome | Terabyte per rumah sakit |

### Big Data di Indonesia
- **Gojek** — memproses jutaan transaksi per hari
- **BPJS Kesehatan** — data 200+ juta peserta
- **Dana** — jutaan transaksi digital per hari
- **E-commerce** — jutaan produk, review, transaksi

> 💬 **Diskusi:** Data apa saja yang kamu hasilkan setiap hari? Berapa kira-kira ukurannya?

### 🔍 Cek Pemahaman
1. Sebutkan dan jelaskan 5V dari Big Data!
2. Berikan 3 contoh sumber Big Data beserta volume data yang dihasilkan setiap hari!
3. Mengapa Big Data di Indonesia seperti Gojek dan BPJS disebut sebagai contoh Big Data?

### 📋 Studi Kasus
Kantin sekolah SMA Merdeka melayani sekitar 500 siswa setiap hari. Setiap transaksi mencatat: nama siswa, makanan yang dibeli, harga, dan waktu pembelian. Selama 1 bulan, terkumpul ribuan data transaksi. Kepala sekolah ingin mengetahui menu apa yang paling laris, jam berapa kantin paling ramai, dan berapa rata-rata pengeluaran siswa per hari.

**Analisis:**
1. Apakah data kantin tersebut sudah bisa disebut Big Data? Jelaskan menggunakan konsep 5V!
2. Data apa saja yang perlu dikumpulkan agar analisisnya lebih akurat?

> 🤔 **Mari Renungkan:** Apa hal paling menarik yang kamu pelajari dari bagian ini?

---

## B. Pengolahan Data dengan Tools Digital

### 🔧 Pengolahan Data dengan Tools Digital
Data mentah tidak berguna tanpa **pengolahan**. Tools digital membantu mengubah data menjadi informasi.

> 🧩 **Analogi:** Data mentah itu seperti **bahan makanan di dapur**. Mentah, belum bisa dimakan. Tapi setelah diolah — dipotong, dimasak, dibumbui — jadilah hidangan lezat. **Pengolahan data = memasak!**

### Tools Pengolahan Data
| Tools | Tingkat Kesulitan | Fungsi Utama |
|-------|------------------|-------------|
| **Microsoft Excel** | 🟢 Mudah | Spreadsheet, formula, pivot table |
| **Google Sheets** | 🟢 Mudah | Spreadsheet online, kolaborasi real-time |
| **Python (Pandas)** | 🔴 Sulit | Analisis data tingkat lanjut |
| **Tableau Public** | 🟡 Sedang | Visualisasi data interaktif |
| **Google Data Studio** | 🟡 Sedang | Dashboard data |

### Siklus Pengolahan Data
```
┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐
│  KOLEKSI │   │  BERSIH- │   │  ANALISIS│   │  VISUA-  │
│  Data    │──►│  KAN     │──►│  Data    │──►│  LISASI  │
│          │   │  (Cleaning)│  │          │   │  & Lapor │
└──────────┘   └──────────┘   └──────────┘   └──────────┘
```

### Studi Kasus: Analisis Data Nilai Kelas
```python
import pandas as pd

data = {
    "nama": ["Andi", "Budi", "Citra", "Dewi"],
    "nilai": [85, 72, 90, 78]
}
df = pd.DataFrame(data)

print(f"Rata-rata: {df['nilai'].mean()}")    # 81.25
print(f"Tertinggi: {df['nilai'].max()}")      # 90
print(f"Terendah: {df['nilai'].min()}")        # 72
print(f"Lulus (>=78): {df[df['nilai'] >= 78]}")
```

> ✍️ **Latihan:** Kumpulkan data tinggi badan 10 teman sekelasmu. Gunakan Excel/Google Sheets untuk: rata-rata, tertinggi, terendah!

### 🔍 Cek Pemahaman
1. Sebutkan 4 tahap dalam siklus pengolahan data!
2. Apa perbedaan antara data mentah dan informasi? Berikan contoh!
3. Tools apa yang paling tepat digunakan untuk analisis data sederhana? Untuk analisis tingkat lanjut?

### 📋 Studi Kasus
Setelah ujian tengah semester, wali kelas XI IPA 2 ingin menganalisis hasil ujian 35 siswa. Data yang tersedia adalah nama siswa dan nilai untuk 5 mata pelajaran. Wali kelas ingin tahu: rata-rata nilai per mapel, siswa dengan nilai tertinggi dan terendah, serta berapa siswa yang tidak lulus (nilai < 70) di setiap mapel.

**Analisis:**
1. Tools apa yang paling tepat digunakan wali kelas? Jelaskan langkah-langkah analisisnya!
2. Buat contoh data sederhana (5 siswa, 3 mapel) dan hitung rata-rata, nilai tertinggi, dan nilai terendah menggunakan Python (Pandas)!

> 🤔 **Mari Renungkan:** Apa hal paling menarik yang kamu pelajari dari bagian ini?

---

## C. Visualisasi Data yang Menarik

### 📈 Visualisasi Data yang Menarik
**Visualisasi data** adalah penyajian data dalam bentuk **grafik, diagram, atau peta** agar mudah dipahami.

> 🧩 **Analogi:** Visualisasi data itu seperti **poster dibandingkan novel**. Novel 300 halaman butuh waktu berhari-hari untuk dibaca. Poster yang bagus bisa menyampaikan pesan dalam 3 detik. **Visualisasi data adalah poster untuk datamu!**

### Jenis Visualisasi
```
📊 BAR CHART — Bandingkan kategori (nilai per mapel)
    ██ 85
    ██████ 90
    ██ 78

📈 LINE CHART — Tren dari waktu ke waktu (nilai per semester)
    ─╱╲──╱╲──╱╲──
    80─85─78─90

🥧 PIE CHART — Proporsi/bagian dari total (%
suara)
    ⬤

🗺️ HEATMAP — Konsentrasi data (daerah rawan)
    🟥🟧🟨🟩

📋 TABLE — Data detail
    Nama │ Nilai
    ─────┼──────
    Andi │ 85
```

### Aturan Visualisasi yang Baik
✅ **Sederhana** — jangan terlalu banyak informasi
✅ **Akurat** — skala sumbu jangan dimanipulasi
✅ **Kontekstual** — beri judul dan label yang jelas
✅ **Warna bijak** — jangan gunakan > 5 warna
❌ **3D chart** — sering menyesatkan persepsi
❌ **Pie chart > 5 kategori** — susah dibaca

### ✍️ Aktivitas
1. Kumpulkan data: jumlah siswa per jurusan di sekolahmu
2. Buat bar chart dan pie chart di Excel/Google Sheets
3. Bandingkan: mana yang lebih mudah dipahami?
4. Presentasikan ke kelas!

### 🔍 Cek Pemahaman
1. Sebutkan 3 jenis visualisasi data dan kapan waktu yang tepat menggunakan masing-masing!
2. Apa aturan visualisasi data yang baik? Sebutkan minimal 3!
3. Mengapa pie chart tidak disarankan untuk lebih dari 5 kategori?

### 📋 Studi Kasus
OSIS sekolah ingin membuat **laporan tahunan** dalam bentuk infografis yang menarik. Data yang dimiliki: jumlah siswa per jurusan (IPA 120, IPS 90, Bahasa 45), tren nilai rata-rata sekolah 3 tahun terakhir (83, 85, 87), dan alokasi dana OSIS (kegiatan 60%, perlengkapan 25%, cadangan 15%). Ketua OSIS meminta bantuanmu memilih visualisasi yang tepat.

**Analisis:**
1. Jenis visualisasi apa yang paling tepat untuk masing-masing data tersebut? Jelaskan alasannya!
2. Buat sketsa infografis sederhana untuk laporan tahunan OSIS tersebut!

> 🤔 **Mari Renungkan:** Apa hal paling menarik yang kamu pelajari dari bagian ini?

---

## D. Proyek Analisis Data: Desain

### 🎯 Proyek Analisis Data: Desain

### Tugas Akhir Bab 6 — Proyek Analisis Data
Lakukan analisis data nyata dari lingkungan sekitarmu!

### Pilih Topik
| Topik | Data yang Dikumpulkan | Sumber Data |
|-------|----------------------|-------------|
| **Polusi Udara** | PM2.5, suhu, kelembaban | Sensor IoT / BMKG |
| **Nilai Ujian** | Nilai per mapel, tren | Data sekolah |
| **Kebiasaan Belajar** | Jam belajar, nilai | Survei teman sekelas |
| **Pengeluaran** | Uang saku, pengeluaran | Survei siswa |
| **Trafik Sekolah** | Jumlah siswa per jam | Observasi/pintu gerbang |

### Template Perencanaan
```
┌──────────────────────────────────────────────────┐
│           PROYEK ANALISIS DATA                   │
├──────────────────────────────────────────────────┤
│                                                    │
│  JUDUL: [judul proyek]                             │
│                                                    │
│  PERTANYAAN: [apa yang ingin diketahui?]           │
│  • Apakah ada hubungan jam belajar & nilai?        │
│  • Bagaimana tren nilai dari semester 1 ke 2?      │
│                                                    │
│  DATA: [data apa yang dikumpulkan?]                │
│  • 50 siswa kelas XI                               │
│  • Variabel: jam belajar, nilai ujian              │
│                                                    │
│  METODE: [tools & teknik]                          │
│  • Google Forms (koleksi data)                     │
│  • Python/Excel (analisis)                         │
│  • Canva/Data Studio (visualisasi)                 │
│                                                    │
│  OUTPUT: [apa yang akan dihasilkan?]               │
│  • Laporan analisis (PDF)                          │
│  • Poster infografis                               │
│  • Presentasi 10 slide                             │
└──────────────────────────────────────────────────┘
```

> 💡 **Pilih data yang MUDAH dikumpulkan** — lebih baik proyek sederhana selesai daripada proyek ambisius tapi tidak selesai!

### 🔍 Cek Pemahaman
1. Sebutkan 5 topik proyek analisis data yang bisa dilakukan di lingkungan sekolah!
2. Apa saja komponen yang harus ada dalam template perencanaan proyek analisis data?
3. Mengapa penting untuk menentukan pertanyaan penelitian sebelum mengumpulkan data?

### 📋 Studi Kasus
Kelompokmu tertarik meneliti **tingkat polusi udara** di sekitar sekolah. Namun, alat sensor PM2.5 harganya mahal. Kalian punya waktu 2 minggu dan anggaran Rp0. Sumber data yang tersedia: data BMKG online, observasi visual (kepadatan kendaraan), dan wawancara warga sekitar.

**Analisis:**
1. Sesuaikan rencana proyek dengan kendala yang ada! Data apa yang bisa dikumpulkan dengan sumber yang tersedia?
2. Buat rancangan proyek singkat: pertanyaan penelitian, data yang dikumpulkan, tools analisis, dan output!

> 🤔 **Mari Renungkan:** Apa hal paling menarik yang kamu pelajari dari bagian ini?

---

## E. Proyek Analisis Data: Implementasi

### 🏁 Proyek Analisis Data: Implementasi

### Tahap Implementasi
```python
# 1. KOLEKSI DATA
# Buat Google Forms, sebarkan ke responden
# Export ke CSV / Google Sheets

# 2. BERSIHKAN DATA (Cleaning)
import pandas as pd
df = pd.read_csv("data_survei.csv")
df = df.dropna()  # Hapus baris kosong
df = df[df['jam_belajar'] > 0]  # Filter data valid

# 3. ANALISIS
rata_jam = df['jam_belajar'].mean()
rata_nilai = df['nilai'].mean()
korelasi = df['jam_belajar'].corr(df['nilai'])
print(f"Korelasi jam belajar & nilai: {korelasi}")

# 4. VISUALISASI
import matplotlib.pyplot as plt
plt.scatter(df['jam_belajar'], df['nilai'])
plt.xlabel('Jam Belajar/hari')
plt.ylabel('Nilai Ujian')
plt.title('Hubungan Jam Belajar & Nilai')
plt.savefig('grafik.png')
```

### Format Laporan
| Bab | Isi |
|-----|-----|
| **1. Pendahuluan** | Latar belakang, pertanyaan penelitian |
| **2. Metode** | Cara pengumpulan data, tools |
| **3. Hasil** | Tabel, grafik, temuan utama |
| **4. Analisis** | Interpretasi data, insight |
| **5. Kesimpulan** | Jawaban pertanyaan, saran |

### Tips Presentasi
1. **Cerita dulu, data kemudian** — mulai dengan narasi
2. **Satu slide = satu pesan** — jangan terlalu penuh
3. **Visual > Teks** — pakai grafik, bukan tabel besar
4. **Panggil insight** — "Ternyata... yang mengejutkan adalah..."

### 🔍 Cek Pemahaman
1. Sebutkan 5 tahap implementasi proyek analisis data!
2. Apa perbedaan antara analisis dan interpretasi data?
3. Sebutkan 4 tips presentasi data yang efektif!

### 📋 Studi Kasus
Setelah berminggu-minggu mengerjakan proyek analisis data tentang **kebiasaan belajar**, kelompokmu menemukan temuan menarik: ternyata siswa yang belajar antara 2-3 jam per hari mendapat nilai lebih tinggi daripada yang belajar lebih dari 5 jam. Temuan ini kontroversial karena bertentangan dengan anggapan umum "makin lama belajar, makin pintar".

**Analisis:**
1. Bagaimana sebaiknya kelompokmu mempresentasikan temuan ini agar tidak disalahpahami? Strategi apa yang harus digunakan?
2. Faktor lain apa yang mungkin mempengaruhi hasil ini (confounding variables)? Sebutkan minimal 3!

---
> 🎉 **Selamat!** Kamu telah menyelesaikan perjalanan Informatika kelas XI! Dari coding, AI, hingga analisis data — kamu punya bekal untuk menjadi **pemecah masalah di era digital**. Tetap belajar dan berkarya! 🚀

> 🤔 **Mari Renungkan:** Apa hal paling menarik yang kamu pelajari dari bagian ini?

---

---
## 🏗️ Proyek Mini: 📈 Dashboard Data Sederhana

Analisis dataset kecil (minimal 30 baris) menggunakan Google Sheets atau Python Pandas, lalu buat dashboard visualisasi interaktif. Tema bebas: kebiasaan belajar, pengeluaran harian, atau data lingkungan sekolah.

**Alat dan Bahan:**
- Google Sheets / Microsoft Excel
- (Opsional) Google Colab dengan Python Pandas + Matplotlib
- Google Data Studio / Canva untuk dashboard
- Data survei (Google Forms)

**Langkah-langkah:**
1. Tentukan topik dan buat pertanyaan penelitian yang ingin dijawab (minimal 2 pertanyaan).
2. Kumpulkan data menggunakan Google Forms (sebarkan ke teman sekelas) — minimal 30 responden.
3. Export data ke Google Sheets atau CSV. Lakukan pembersihan data: hapus baris kosong, perbaiki format.
4. Analisis data: hitung rata-rata, median, nilai maks/min, dan korelasi antar variabel.
5. Buat visualisasi: 1 bar chart, 1 pie chart, dan 1 line chart atau scatter plot.
6. Buat dashboard di Google Data Studio/Canva yang merangkum semua temuan dalam 1 halaman.

> **Output:** File data (CSV) + dashboard visualisasi (PDF/screenshot) + presentasi 5 menit

## 📝 Rangkuman

- **Big Data** memiliki 5V: Volume, Velocity, Variety, Veracity, Value. Contoh di Indonesia: Gojek, BPJS Kesehatan, dan e-commerce memproses data raksasa setiap hari.
- Siklus pengolahan data: **Koleksi → Pembersihan (Cleaning) → Analisis → Visualisasi & Pelaporan**. Tools: Excel, Google Sheets, Python (Pandas), Tableau.
- **Visualisasi data** membantu menyampaikan informasi dengan cepat. Jenis utama: Bar Chart (perbandingan), Line Chart (tren), dan Pie Chart (proporsi).
- Proyek analisis data dimulai dengan **perencanaan** (topik, pertanyaan, metode), dilanjutkan implementasi (koleksi data, cleaning, analisis, visualisasi), dan diakhiri **presentasi**.
- Visualisasi yang baik harus sederhana, akurat, kontekstual, dengan warna bijak maksimal 5 warna. Hindari 3D chart dan pie chart lebih dari 5 kategori.

---
## ✍️ Latihan Soal

### Pilihan Ganda

1. Berikut ini yang **bukan** termasuk 5V Big Data adalah...
   a. Volume
   b. Velocity
   c. Variety
   d. Visibility
   e. Value
   **Kunci Jawaban: D**

2. Library Python yang paling umum digunakan untuk pengolahan data adalah...
   a. NumPy
   b. Pandas
   c. Matplotlib
   d. Scikit-learn
   e. Requests
   **Kunci Jawaban: B**

3. Tahap pertama dalam siklus pengolahan data adalah...
   a. Visualisasi
   b. Analisis
   c. Koleksi data
   d. Pembersihan data
   e. Pelaporan
   **Kunci Jawaban: C**

4. Visualisasi bar chart paling cocok digunakan untuk...
   a. Menunjukkan tren dari waktu ke waktu
   b. Membandingkan nilai antar kategori
   c. Menunjukkan proporsi dari total
   d. Menunjukkan konsentrasi data geografis
   e. Menampilkan data detail dalam tabel
   **Kunci Jawaban: B**

5. Sumber Big Data yang menghasilkan 500 jam konten per menit adalah...
   a. Media sosial (Twitter)
   b. Transaksi e-commerce
   c. Video (YouTube/CCTV)
   d. Sensor IoT
   e. Kesehatan (rekam medis)
   **Kunci Jawaban: C**

### Uraian

1. Jelaskan konsep Big Data dan 5V-nya! Berikan contoh sumber Big Data yang ada di Indonesia!

2. Jelaskan siklus pengolahan data dari koleksi hingga visualisasi! Tools apa saja yang bisa digunakan pada setiap tahap?

3. Apa pentingnya visualisasi data? Sebutkan dan jelaskan 3 jenis visualisasi data serta kapan waktu yang tepat menggunakannya!

4. Buatlah rencana proyek analisis data sederhana tentang topik kebiasaan belajar siswa di sekolahmu! Sertakan: pertanyaan penelitian, data yang dikumpulkan, tools, dan output yang dihasilkan!

---
## 📋 Rubrik Penilaian Proyek

| Aspek | Kurang | Cukup | Baik |
|-------|--------|-------|------|
| Kualitas Data | Data < 20 baris, tidak dibersihkan | Data 20-30 baris, dibersihkan cukup | Data > 30 baris, bersih, siap analisis |
| Analisis & Insight | Tidak ada analisis, hanya tabel mentah | Analisis deskriptif dasar (mean, max, min) | Analisis mendalam termasuk korelasi |
| Visualisasi | Visualisasi asal, tidak sesuai jenis data | Visualisasi tepat untuk 2 jenis data | 3+ visualisasi tepat, menarik, informatif |
| Dokumentasi & Presentasi | Laporan tidak lengkap, presentasi tidak jelas | Laporan lengkap, presentasi cukup jelas | Laporan profesional, presentasi meyakinkan |

---
## 🚀 Tugas Pengayaan

### 📊 Dashboard Data Publik
Kunjungi [data.go.id](https://data.go.id/) (Portal Data Terbuka Indonesia) dan unduh 1 dataset yang menarik bagimu. Gunakan Google Sheets atau Python untuk membuat: 1 bar chart, 1 line chart, dan 1 dashboard sederhana. Tulis 3 insight yang kamu temukan dari data tersebut.

### 🏆 Tantangan Analisis Data
Selesaikan tutorial *'Pandas for Data Analysis'* di [Kaggle](https://www.kaggle.com/learn) atau [Dicoding](https://www.dicoding.com/). Kerjakan latihan yang disediakan dan screenshot hasilnya. Catat: fungsi/library baru apa yang kamu pelajari di luar materi kelas?

---
## 📖 Glosarium

- **Big Data**: Kumpulan data berukuran sangat besar yang tidak dapat diolah dengan metode tradisional.
- **5V Big Data**: Karakteristik Big Data: Volume, Velocity, Variety, Veracity, dan Value.
- **Data Cleaning**: Proses membersihkan data dari kesalahan, duplikasi, atau nilai kosong sebelum dianalisis.
- **Visualisasi Data**: Penyajian data dalam bentuk grafik, diagram, atau peta agar mudah dipahami.
- **Pandas**: Library Python untuk manipulasi dan analisis data yang menyediakan struktur DataFrame.
- **Bar Chart**: Grafik batang untuk membandingkan nilai antar kategori.
- **Line Chart**: Grafik garis untuk menunjukkan tren data dari waktu ke waktu.
- **Pie Chart**: Grafik lingkaran untuk menunjukkan proporsi atau bagian dari keseluruhan.

---
## 📺 Sumber & Media Pembelajaran

| Platform | Sumber | Tautan | Keterangan |
|----------|--------|--------|------------|
| YouTube | Apa itu Big Data? | `youtu.be/search?q=apa+itu+big+data+indonesia` | Penjelasan Big Data dan 5V |
| Website | Google Data Studio | `https://datastudio.google.com/` | Tools visualisasi data gratis dari Google |
| Website | Tableau Public | `https://public.tableau.com/` | Platform visualisasi data interaktif |
| YouTube | Tutorial Python Pandas | `youtu.be/search?q=tutorial+pandas+python+indonesia` | Belajar analisis data dengan Pandas |
| Website | Google Trends | `https://trends.google.com/` | Tools analisis tren pencarian Google |
