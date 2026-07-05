# MODUL AJAR INFORMATIKA KELAS X

## AD: SIKLUS PENGOLAHAN DATA (TP.6.3)

---

### A. INFORMASI UMUM

| Komponen | Deskripsi |
|---|---|
| Satuan Pendidikan | SMA Negeri 6 Cimahi |
| Mata Pelajaran | Informatika |
| Kelas / Fase | X (Sepuluh) / Fase E |
| Elemen | AD — Analisis Data |
| Tujuan Pembelajaran | TP.6.3: Menerapkan siklus pengolahan data dari berbagai sumber |
| Alokasi Waktu | 2 JP (2 × 45 menit) |
| Pertemuan ke- | 19 |
| Kompetensi Awal | Peserta didik telah memahami konsep data, informasi, pengetahuan (DIKW) dan privasi data. Peserta didik telah membawa data mentah (1 minggu pengeluaran jajan atau data pilihan sendiri) dari pertemuan sebelumnya. |
| Integrasi 8 Dimensi | Kemandirian (mengelola data sendiri), Kreativitas (menyajikan data hasil olahan), Penalaran Kritis (memutuskan metode pembersihan dan transformasi), Kolaborasi (polling kelas dan kerja kelompok) |
| **Integrasi 7 KAIH** | Makan Sehat, Tidur Cepat |
| **Pendekatan Deep Learning** | Mindful → Mining → Joyful |
| Sarana & Prasarana | Komputer/lab dengan Google Sheets/Excel, akses internet, Google Forms, data mentah bawaan siswa, proyektor, koneksi internet |
| Target Peserta Didik | Reguler (dengan diferensiasi 3 tingkat) |
| Model Pembelajaran | Praktik Langsung |
| Metode | Praktik berbasis proyek: membuat form → mengumpulkan data → membersihkan → mentransformasi → mengekspor |
| Sumber Belajar | Buku Informatika Kemendikbud Bab 6, dokumentasi Google Forms & Sheets, tutorial "Data Cleaning in Spreadsheets" |
| Pertemuan ke- | 19 |

### B. TUJUAN PEMBELAJARAN
### B.1 PEMAHAMAN BERMAKNA (MEANINGFUL)
Data adalah 'minyak baru' di era digital. Kemampuan menganalisis data membuka peluang karir dan membantu pengambilan keputusan yang lebih baik.


### B.2 PERTANYAAN PEMANTIK (MINDFUL)
1. Apa yang akan terjadi jika...?
2. Bagaimana konsep ini terhubung dengan kehidupan sehari-harimu?
3. Mengapa materi ini penting untuk dipelajari?

#### B.1 Tujuan Pembelajaran

1. Mengumpulkan data melalui Google Forms sebagai simulasi pengumpulan data digital.
2. Menerapkan teknik pembersihan data: menghapus duplikat, memperbaiki format, menangani missing values.
3. Melakukan transformasi data: grouping, sorting, filtering, dan formula dasar.
4. Mengekspor data ke berbagai format (CSV, PDF) dan mengimpor data dari CSV ke spreadsheet.

#### B.2 Indikator Keberhasilan

| Indikator | Kriteria |
|---|---|
| Membuat Google Forms dengan minimal 5 pertanyaan dengan tipe yang bervariasi | Form memiliki 5+ pertanyaan dengan 3+ tipe berbeda |
| Mengisi form dan melihat data di Sheets | Data masuk dengan benar ke Sheets |
| Membersihkan data dari duplikat dan format salah | Duplikat terhapus, format diperbaiki |
| Melakukan sorting, filtering, dan grouping dengan benar | Sorting + filtering + 1 grouping berhasil |
| Mengekspor data ke CSV dan mengimpor data dari CSV | Ekspor & impor berhasil diverifikasi |

#### B.3 Kata Kunci

Google Forms, data collection, data cleaning, deduplication, missing values, data transformation, sorting, filtering, grouping, formula, CSV, PDF, ekspor, impor, ETL (Extract, Transform, Load)

### C. KEGIATAN PEMBELAJARAN

| **Fase DL** | **Tahap** | **Waktu** | **Aktivitas Guru** | **Aktivitas Siswa** | **Media/Sumber** |
|---|---|---|---|---|---|
| **MINDFULL** | **Pemanasan** | 15 menit | 1) Salam dan doa. 2) Cek kehadiran. 3) Orientasi: "Minggu lalu kalian disuruh bawa data mentah — sekarang kita olah bersama!" 4) Mengecek siapa yang sudah membawa data. 5) Bagi yang belum bawa: data polling kelas akan digunakan sebagai alternatif. 6) Apersepsi: "Setelah data terkumpul, apa langkah selanjutnya?" 7) Menyampaikan TP | 1) Menjawab salam dan berdoa. 2) Menunjukkan data yang dibawa. 3) Menyimak alternatif. 4) Menjawab apersepsi. 5) Mencatat TP | Proyektor, data siswa, slide |
| **MINING FULL** | **Eksplorasi** — Pengumpulan Data** | 20 menit | 1) Mendemonstrasikan membuat Google Forms: judul, deskripsi, pertanyaan. 2) Membimbing siswa membuat form untuk polling kelas — topik pilihan: hobi, warna favorit, makanan favorit, jam belajar per hari, transportasi ke sekolah. 3) Tipe pertanyaan: multiple choice, checkbox, short answer, linear scale. 4) Setelah form jadi, membagikan link ke kelas. 5) Semua siswa mengisi form teman sekelas | 1) Membuat Google Forms. 2) Menambahkan 5 pertanyaan dengan tipe variatif. 3) Mengirim link form ke teman. 4) Mengisi form teman. 5) Melihat data masuk di Sheets | Google Forms, Google Sheets, komputer, HP |
| **MINING FULL** | **Eksplorasi** — Pembersihan Data** | 15 menit | 1) Membuka tab Responses → Link to Sheets. 2) Menjelaskan 3 masalah umum data: (a) Duplikat — baris yang sama dua kali, (b) Format tidak konsisten — ada "Senin" dan "senin", (c) Missing values — ada sel kosong. 3) Mendemonstrasikan: Data → Data cleanup → Remove duplicates. 4) Mendemonstrasikan: =UPPER() / =LOWER() / =PROPER() untuk merapikan teks. 5) Mendemonstrasikan: =COUNTIF() untuk cek missing values | 1) Membuka Sheets. 2) Menghapus duplikat. 3) Merapikan format teks dengan formula. 4) Mengecek missing values. 5) Mencatat jumlah data valid | Google Sheets, proyektor |
| **MINING FULL** | **Eksplorasi** — Transformasi Data** | 20 menit | 1) Sorting: urutkan data berdasarkan kolom tertentu (A-Z, Z-A). 2) Filter: tampilkan hanya data dengan kondisi tertentu (misal: hobi = olahraga). 3) Grouping: gunakan Pivot Table untuk mengelompokkan frekuensi — berapa siswa suka warna merah? Berapa hobi olahraga? 4) Formula: =COUNTIF, =SUMIF, =AVERAGE untuk meringkas data. 5) Membuat kolom baru dengan formula: misal konversi jam belajar ke kategori (ringan/sedang/berat) | 1) Mempraktikkan sorting. 2) Mengaktifkan filter dan menyaring data. 3) Membuat Pivot Table sederhana. 4) Menggunakan formula COUNTIF, SUMIF. 5) Membuat kolom baru | Google Sheets, proyektor, panduan formula |
| **MINING FULL** | **Eksplorasi** — Ekspor & Impor** | 10 menit | 1) Mendemonstrasikan ekspor data: File → Download → Comma Separated Values (.CSV). 2) Membuka file CSV di Notepad — lihat perbedaan format dengan Sheets. 3) Mendemonstrasikan impor data CSV ke Sheets: File → Import → Upload → CSV. 4) Menjelaskan kapan menggunakan CSV (transfer data antar aplikasi) dan kapan PDF (laporan final) | 1) Mengekspor data ke CSV. 2) Membuka CSV di Notepad. 3) Mengimpor CSV baru ke Sheets. 4) Menyimpan sebagai PDF | Google Sheets, CSV, Notepad |
| **JOYFULL** | **Penutup Kreatif** | 10 menit | 1) Refleksi: "Mana yang paling tidak enak — ngumpulin, bersihin, atau ngolah data?" 2) Diskusi singkat: kenapa data cleaning adalah tahap paling memakan waktu di dunia nyata (data scientist menghabiskan 60-80% waktu untuk cleaning). 3) Penguatan: siklus yang sudah dipraktekkan hari ini adalah fondasi analisis data. 4) Doa | 1) Refleksi dan diskusi. 2) Menyimak penguatan. 3) Berdoa | Lembar refleksi |

### D. ASESMEN

#### D.1 Asesmen Diagnostik

1. Apa yang dimaksud dengan data mentah?
2. Pernahkah kalian mengolah data di Excel/Sheets? Fitur apa yang pernah digunakan?
3. Masalah apa yang sering muncul saat bekerja dengan data?

#### D.2 Asesmen Formatif

Ceklist keterampilan: guru memantau dan menandai siswa yang berhasil melakukan setiap langkah (buat form, hapus duplikat, sorting, filtering, pivot, ekspor). Ceklist diisi selama praktik.

#### D.3 Asesmen Sumatif

1. Hasil polling kelas yang telah dibersihkan & ditransformasi (produk individu)
2. File CSV hasil ekspor (produk individu)
3. Lembar ceklist keterampilan praktik

#### D.4 Rubrik Penilaian

| Aspek | SB = 4 (Sangat Baik) | B = 3 (Baik) | C = 2 (Cukup) | PB = 1 (Perlu Bimbingan) |
|---|---|---|---|---|---|
| Membuat Google Forms | 5+ pertanyaan, 3+ tipe, rapi, link berfungsi | 5 pertanyaan, 2 tipe | 3-4 pertanyaan | < 3 pertanyaan |
| Pembersihan Data | Duplikat terhapus, format rapi, missing values teratasi | Duplikat terhapus, format rapi | Duplikat terhapus | Tidak dibersihkan |
| Transformasi (Sort, Filter, Group) | Sorting + filter + pivot table + 2 formula | Sorting + filter + pivot table | Sorting + filter | Hanya sorting |
| Ekspor & Impor | CSV terekspor + terbukti di Notepad + impor berhasil | CSV terekspor + diverifikasi | CSV terekspor | Tidak bisa ekspor |

#### D.5 Contoh Soal/Tugas

"Soal: Berikut adalah data mentah nilai siswa: ['Andi', 'andi', 'Budi', 'Budi', 'Citra', '', 'Dedi']. Terapkan 3 teknik pembersihan data: (1) Hapus duplikat, (2) Rapikan kapitalisasi (Andi vs andi), (3) Tangani missing value (sel kosong). Jelaskan formula/langkah yang digunakan!"

### E. LEMBAR KERJA PESERTA DIDIK (LKPD)

**LKPD 19.1 — Siklus Pengolahan Data**

Nama: _____________ Kelas: _____________ Tanggal: _____________

**Bagian A: Google Forms**

Topik polling kelas: ________
Tautan form: ________

| No | Pertanyaan | Tipe | Contoh Jawaban |
|---|---|---|---|
| 1 | ________ | ________ | ________ |
| 2 | ________ | ________ | ________ |
| 3 | ________ | ________ | ________ |
| 4 | ________ | ________ | ________ |
| 5 | ________ | ________ | ________ |

**Bagian B: Pembersihan Data**

Jumlah data sebelum dibersihkan: ________ baris
Duplikat yang ditemukan: ________ baris
Missing values yang ditemukan: ________ sel
Jumlah data setelah dibersihkan: ________ baris

Formulas yang digunakan:
- Merapikan teks: =________
- Cek duplikat: =________
- Hitung total: =________

**Bagian C: Hasil Transformasi**

**Pertanyaan Refleksi:**
1. Dari 5 tahap (kumpul → bersihkan → transformasi → analisis → visualisasi), mana yang paling menantang? Kenapa?
2. Dalam dunia kerja, data scientist menghabiskan 60-80% waktu untuk data cleaning. Setelah praktik ini, apakah kalian setuju? Jelaskan!

**Tantangan Bertingkat:**
- Level Dasar (C): Buat form 4 pertanyaan + hapus duplikat + sorting
- Level Menengah (B): Buat form 5 pertanyaan + hapus duplikat + sorting + filter + pivot table
- Level Mahir (A): Buat form 5+ pertanyaan + selesaikan semua tahap + buat kolom baru dengan formula IF (misal: kategorikan umur atau skor) + berikan insight dari data yang diolah

### F. DIFERENSIASI PEMBELAJARAN

1. **Level Dasar (C):** Siswa mendapat template Google Forms yang sudah jadi — tinggal memodifikasi. Panduan pembersihan data dengan screenshot langkah demi langkah. Tidak perlu pivot table.
2. **Level Menengah (B):** Membuat form dari awal dengan panduan minimal. Melakukan semua tahap pembersihan dan transformasi standar.
3. **Level Mahir (A):** Membuat form dari awal dengan pertanyaan yang lebih kompleks (bersyarat/logika). Transformasi lanjutan: membuat kolom baru dengan nested IF, VLOOKUP untuk menggabungkan data dari sheet berbeda. Membuat dashboard mini dengan conditional formatting.

### G. REFLEKSI GURU

1. Apakah semua siswa berhasil membuat Google Forms? Apakah ada kendala teknis (akun Google, internet)?
2. Tahap mana yang paling sulit bagi siswa — pembersihan atau transformasi?
3. Apakah siswa memahami pentingnya data cleaning setelah praktik? Atau masih menganggapnya sepele?
4. Apakah durasi 20 menit untuk pembuatan form cukup? Atau perlu persiapan template sebelumnya?
5. Bagaimana kualitas hasil pivot table siswa? Apakah perlu latihan tambahan?

### H. BAHAN BACAAN UNTUK GURU

1. **ETL (Extract, Transform, Load):** Dalam dunia data engineering, siklus pengolahan data dikenal sebagai ETL. Extract: mengambil data dari sumber (database, API, file). Transform: membersihkan, memformat, menggabungkan, menghitung. Load: memasukkan ke data warehouse atau sistem target. Tools ETL populer: Apache NiFi, Talend, Pentaho. Di tingkat pemula, Google Sheets + Forms sudah cukup untuk memperkenalkan konsep ETL.
2. **Data Cleaning Techniques:** Teknik pembersihan data meliputi: (a) Handling missing values — bisa dihapus (listwise deletion) atau diisi (imputation: mean, median, mode). (b) Standardizing formats — tanggal, alamat, nomor telepon. (c) Removing outliers — data yang jauh dari mayoritas. (d) Deduplication — baris rangkap. (e) Validation — memastikan data sesuai aturan (email valid, umur positif). Di Google Sheets: =TRIM(), =CLEAN(), =UNIQUE(), =FILTER().
3. **Data Quality Dimensions:** Kualitas data diukur dari: (1) Accuracy — seberapa akurat data mencerminkan kenyataan. (2) Completeness — seberapa lengkap data (tidak ada missing values). (3) Consistency — data konsisten antar sumber. (4) Timeliness — data masih relevan waktunya. (5) Uniqueness — tidak ada duplikat. (6) Validity — data sesuai format yang ditentukan. Prinsip GIGO (Garbage In, Garbage Out) — analisis terbaik pun akan sia-sia jika data masukannya buruk.
4. **Spreadsheet untuk Analisis Data:** Google Sheets dan Excel memiliki fitur yang cukup untuk analisis data tingkat dasar hingga menengah: Pivot Table (ringkasan data interaktif), Conditional Formatting (sorot data berdasarkan kondisi), Data Validation (batasi input), Named Ranges (referensi sel bernama), Scenario Analysis (What-If Analysis). Untuk kebutuhan lebih lanjut, siswa bisa beralih ke Python (pandas) atau R (tidyverse) di kelas yang lebih tinggi.

---

Mengetahui,
Kepala Sekolah

_________________________

Guru Mata Pelajaran,

Daniarsyah, S.Kom.
NIP. 198004052022211004

_________________________
