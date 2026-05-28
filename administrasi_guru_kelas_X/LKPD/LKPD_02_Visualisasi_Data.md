# LKPD - Visualisasi Data dengan Diagram
**Mata Pelajaran:** Informatika
**Kelas/Semester:** X / Ganjil
**Materi Pokok:** Bab 6 – Analisis Data (Visualisasi Data)
**Alokasi Waktu:** 2 JP (1 JP = 45 menit)

## A. Tujuan Pembelajaran
1. Peserta didik mampu menginput data survei ke dalam spreadsheet.
2. Peserta didik mampu membuat diagram lingkaran (pie chart), diagram batang (bar chart), dan diagram garis (line chart) menggunakan Google Sheets / MS Excel.
3. Peserta didik mampu membaca dan menginterpretasikan informasi dari diagram.
4. Peserta didik mampu memilih jenis diagram yang tepat untuk suatu data.

## B. Alat dan Bahan
1. Komputer/laptop dengan koneksi internet.
2. Browser (Chrome/Edge/Firefox).
3. Akun Google (untuk Google Sheets) atau MS Excel.

## C. Langkah Kerja

### Tahap 1: Menyiapkan Data Survei
1. Buka **Google Sheets** (sheets.new) atau **MS Excel**.
2. Buat tabel data survei **"Kegemaran Siswa"** seperti berikut:

   | No | Nama Siswa | Jenis Kelamin | Hobi | Waktu Belajar (jam/minggu) | Nilai Informatika |
   |----|------------|---------------|------|---------------------------|-------------------|
   | 1 | Siswa 1 | L | Olahraga | 5 | 85 |
   | 2 | Siswa 2 | P | Membaca | 7 | 90 |
   | 3 | Siswa 3 | L | Game | 3 | 70 |
   | 4 | Siswa 4 | P | Musik | 6 | 88 |
   | 5 | Siswa 5 | L | Olahraga | 4 | 78 |
   | 6 | Siswa 6 | P | Membaca | 8 | 92 |
   | 7 | Siswa 7 | L | Game | 2 | 65 |
   | 8 | Siswa 8 | P | Musik | 5 | 80 |

3. Isi data sesuai kelas masing-masing (bisa lebih dari 8 siswa).

### Tahap 2: Membuat Diagram Lingkaran (Pie Chart) — Hobi
1. Blok/sorot kolom **Hobi** (termasuk header).
2. Klik menu **Insert** → **Chart** (di Google Sheets) atau **Insert** → **Pie Chart** (Excel).
3. Di **Chart editor** (Google Sheets), pastikan **Chart type** = **Pie chart**.
4. Atur **Data range** agar hanya mencakup kolom Hobi.
5. Centang **Aggregate** → otomatis akan dihitung jumlah per hobi.
6. Beri judul diagram: **"Diagram Hobi Siswa"**.
7. Aktifkan **Data labels** agar muncul persentase.

### Tahap 3: Membuat Diagram Batang (Bar Chart) — Rata-rata Nilai per Hobi
1. Buat tabel ringkasan di samping data utama:

   | Hobi | Rata-rata Nilai |
   |------|----------------|
   | Olahraga | =AVERAGEIF(...) |
   | Membaca | =AVERAGEIF(...) |
   | Game | =AVERAGEIF(...) |
   | Musik | =AVERAGEIF(...) |

   *Gunakan fungsi `=AVERAGEIF(C2:C9;F2:F9;A2)` — sesuaikan range.*
2. Blok tabel ringkasan → **Insert** → **Chart** → pilih **Bar chart**.
3. Beri judul: **"Rata-rata Nilai Informatika Berdasarkan Hobi"**.
4. Beri label sumbu X: **Hobi**, sumbu Y: **Nilai Rata-rata**.

### Tahap 4: Membuat Diagram Garis (Line Chart) — Waktu Belajar
1. Siapkan data urutan siswa berdasarkan nomor absen dan waktu belajarnya.
2. Blok kolom **Nama Siswa** dan **Waktu Belajar** → **Insert** → **Chart** → pilih **Line chart**.
3. Beri judul: **"Waktu Belajar per Minggu"**.
4. Beri label sumbu X: **Siswa**, sumbu Y: **Jam/Minggu**.

### Tahap 5: Menyimpan dan Mengekspor
1. Simpan file dengan nama **"Visualisasi_Data_Kelas_X"**.
2. Ekspor sebagai PDF: **File** → **Download** → **PDF**.
3. Screenshot masing-masing diagram dan tempelkan di lembar jawaban.

## D. Tabel Hasil Pengamatan

| Jenis Diagram | Data yang Digunakan | Judul Diagram | Informasi yang Dapat Dibaca |
|---------------|---------------------|---------------|----------------------------|
| Pie Chart | | | |
| Bar Chart | | | |
| Line Chart | | | |

## E. Diskusi dan Analisis
1. Mengapa diagram lingkaran cocok untuk data hobi tetapi kurang cocok untuk data waktu belajar?
2. Informasi apa yang bisa kamu simpulkan dari diagram batang rata-rata nilai?
3. Apakah ada hubungan antara waktu belajar dan nilai Informatika? Jelaskan berdasarkan line chart!
4. Diagram mana yang paling mudah dipahami? Mengapa?
5. Berikan contoh data lain di kehidupan sehari-hari yang cocok divisualisasikan dengan pie chart, bar chart, dan line chart!

## F. Kesimpulan
Tuliskan kesimpulan tentang pentingnya visualisasi data dan bagaimana memilih jenis diagram yang tepat!

## G. Penilaian

| Aspek | Skor Maks |
|-------|-----------|
| Kelengkapan data survei | 15 |
| Pie Chart (format, judul, label) | 20 |
| Bar Chart (rumus ringkasan, format) | 25 |
| Line Chart (format, interpretasi) | 20 |
| Tabel pengamatan & jawaban diskusi | 20 |
| **Total** | **100** |
