# LKPD - MIT App Inventor
**Mata Pelajaran:** Informatika
**Kelas/Semester:** XI / Genap
**Materi Pokok:** Bab 5 - Aplikasi Mobile (MIT App Inventor: Desain UI dan Blok Logika)
**Alokasi Waktu:** 5 JP

## A. Tujuan Pembelajaran
1. Mendesain antarmuka pengguna (UI) aplikasi Android sederhana di MIT App Inventor
2. Menyusun blok logika untuk menjalankan fungsionalitas aplikasi
3. Membuat aplikasi kuis interaktif dengan skor dan umpan balik
4. Menguji aplikasi menggunakan AI Companion atau emulator

## B. Alat dan Bahan
1. Komputer/laptop dengan koneksi internet
2. Browser web (Chrome/Firefox/Edge)
3. Akun Google (untuk login ke MIT App Inventor)
4. Smartphone Android (opsional, untuk pengujian dengan MIT AI2 Companion)
5. Link: https://ai2.appinventor.mit.edu

## C. Langkah Kerja

### Langkah 1: Persiapan MIT App Inventor
1. Buka browser, kunjungi https://ai2.appinventor.mit.edu
2. Login dengan akun Google
3. Klik **Start New Project**
4. Nama project: `KuisInformatikaXI`
5. Klik **OK**

### Langkah 2: Desain UI (Screen / Layar)
**Atur Properties Screen1:**
- Title: "Kuis Informatika"
- ScreenOrientation: Portrait
- BackgroundColor: pilih warna bebas (misal: Light Blue)

**Tambahkan komponen berikut** (dari Palette ke Viewer):

**Palette > User Interface:**
1. **Label** (`lblSoal`) - Text: "Soal akan muncul di sini" - FontSize: 18 - TextAlignment: center
2. **Label** (`lblNomor`) - Text: "Soal 1/5" - FontSize: 14 - TextColor: Gray
3. **Label** (`lblSkor`) - Text: "Skor: 0" - FontSize: 14 - TextColor: Dark green

4. **Button** (`btnPilihanA`) - Text: "Pilihan A"
5. **Button** (`btnPilihanB`) - Text: "Pilihan B"
6. **Button** (`btnPilihanC`) - Text: "Pilihan C"
7. **Button** (`btnPilihanD`) - Text: "Pilihan D"

   Atur Width masing-masing button ke "Fill parent" dan Height ke 40px

8. **Label** (`lblUmpanBalik`) - Text: "" - FontSize: 16 - TextAlignment: center
9. **Button** (`btnNext`) - Text: "Soal Selanjutnya" - Enabled: false
10. **Button** (`btnRestart`) - Text: "Ulangi Kuis" - Visible: false

**Palette > Layout:**
- **HorizontalArrangement** (untuk lblNomor dan lblSkor sebaris)
   - Masukkan lblNomor dan lblSkor ke dalamnya

### Langkah 3: Blok Logika - Variabel Global
Beralih ke tab **Blocks**.

Buat variabel global:
1. Klik **Variables** → **initialize global name** → ganti `name` jadi `soalList`
2. Klik **Variables** → **initialize global name** → ganti jadi `indexSoal`
3. Klik **Variables** → **initialize global name** → ganti jadi `skor`
4. Klik **Variables** → **initialize global name** → ganti jadi `jawabanBenar`

**Isi variabel global:**

Klik `initialize global soalList`:
```blocks
initialize global soalList as
create empty list
```

Klik kanan pada block → **Show as Blocks**. Gambaran isi list (dibuat dengan blok):
```
( list "
  "Apa kepanjangan CPU?", "Central Processing Unit",
  "Central Program Unit", "Computer Personal Unit",
  "Central Power Unit", "Central Processing Unit"
)
```

(Untuk memudahkan, buat list dengan 5 soal seperti tabel di bawah)

### Langkah 4: Blok Prosedur Inisialisasi
Buat prosedur `inisialisasiKuis`:

**Prosedures** → **to procedure** → beri nama `inisialisasiKuis`

Isi prosedur:
```blocks
set global soalList to:
( list
  "Apa kepanjangan CPU?"
  "Central Processing Unit"
  "Central Program Unit"
  "Computer Personal Unit"
  "Central Power Unit"
  "Central Processing Unit"
  ---
  "Manakah yang termasuk perangkat input?"
  "Monitor"
  "Keyboard"
  "Printer"
  "Speaker"
  "Keyboard"
  ---
  "Apa fungsi RAM pada komputer?"
  "Menyimpan data permanen"
  "Menyimpan data sementara"
  "Memproses grafik"
  "Menampilkan gambar"
  "Menyimpan data sementara"
  ---
  "Apa singkatan dari HTTP?"
  "HyperText Transfer Protocol"
  "High Tech Transfer Protocol"
  "HyperText Transmission Process"
  "Home Tool Transfer Protocol"
  "HyperText Transfer Protocol"
  ---
  "Bahasa pemrograman yang sering digunakan untuk AI adalah..."
  "HTML"
  "Java"
  "Python"
  "CSS"
  "Python"
)
```

Setelah itu buat prosedur `tampilSoal` yang mengambil soal dari list berdasarkan index.

### Langkah 5: Blok Screen.Initialize
```blocks
when Screen1.Initialize
do
  call inisialisasiKuis
  set global indexSoal to 1
  set global skor to 0
  call tampilSoal
```

### Langkah 6: Blok Prosedur tampilSoal
```blocks
when Screen1.Initialize
do
  call inisialisasiKuis
  set global indexSoal to 0
  set global skor to 0
  update display
```

Buat prosedur `updateDisplay`:
```blocks
to procedure updateDisplay
  set lblNomor.Text to join "Soal " (global indexSoal + 1) "/5"
  set lblSoal.Text to select list item
    list: global soalList
    index: (global indexSoal * 6) + 1
  set btnPilihanA.Text to select list item
    list: global soalList
    index: (global indexSoal * 6) + 2
  set btnPilihanB.Text to select list item
    list: global soalList
    index: (global indexSoal * 6) + 3
  set btnPilihanC.Text to select list item
    list: global soalList
    index: (global indexSoal * 6) + 4
  set btnPilihanD.Text to select list item
    list: global soalList
    index: (global indexSoal * 6) + 5
  set global jawabanBenar to select list item
    list: global soalList
    index: (global indexSoal * 6) + 6
  set lblUmpanBalik.Text to ""
  set btnNext.Enabled to false
```

### Langkah 7: Blok Pilihan Jawaban
Buat blok untuk setiap tombol pilihan (A, B, C, D). Contoh untuk btnPilihanA:

```blocks
when btnPilihanA.Click
do
  if call (btnPilihanA.Text) = (global jawabanBenar)
  then
    set lblUmpanBalik.Text to "✅ Benar!"
    set lblUmpanBalik.TextColor to GREEN
    set global skor to (global skor + 20)
    set lblSkor.Text to join "Skor: " (global skor)
  else
    set lblUmpanBalik.Text to "❌ Salah! Jawaban: " (global jawabanBenar)
    set lblUmpanBalik.TextColor to RED
  set btnNext.Enabled to true
```

> **Catatan Buat Guru/Siswa:** Buat blok serupa untuk btnPilihanB, btnPilihanC, dan btnPilihanD dengan mengganti `btnPilihanA.Text` sesuai tombol masing-masing.

### Langkah 8: Blok Tombol Soal Selanjutnya
```blocks
when btnNext.Click
do
  if (global indexSoal) < 4
  then
    set global indexSoal to (global indexSoal + 1)
    call updateDisplay
  else
    set lblSoal.Text to join "Kuis selesai! Skor kamu: " (global skor)
    set btnPilihanA.Visible to false
    set btnPilihanB.Visible to false
    set btnPilihanC.Visible to false
    set btnPilihanD.Visible to false
    set btnNext.Visible to false
    set btnRestart.Visible to true
```

### Langkah 9: Blok Tombol Ulangi Kuis
```blocks
when btnRestart.Click
do
  set global indexSoal to 0
  set global skor to 0
  set btnPilihanA.Visible to true
  set btnPilihanB.Visible to true
  set btnPilihanC.Visible to true
  set btnPilihanD.Visible to true
  set btnNext.Visible to true
  set btnNext.Enabled to false
  set btnRestart.Visible to false
  call updateDisplay
```

### Langkah 10: Uji Coba Aplikasi
1. Klik **Connect > AI Companion**
2. Di smartphone, buka aplikasi **MIT AI2 Companion** (install dari Play Store)
3. Scan QR code yang muncul
4. Uji coba aplikasi:
   - Jawab setiap soal
   - Perhatikan perubahan skor
   - Klik "Soal Selanjutnya"
   - Setelah selesai, klik "Ulangi Kuis"

## D. Tabel Hasil/Data Pengamatan

| No | Soal | Jawaban Kamu | Benar/Salah | Skor Akumulasi |
|----|------|-------------|-------------|----------------|
| 1 | Apa kepanjangan CPU? | | | |
| 2 | Manakah yang termasuk perangkat input? | | | |
| 3 | Apa fungsi RAM pada komputer? | | | |
| 4 | Apa singkatan dari HTTP? | | | |
| 5 | Bahasa pemrograman AI? | | | |
| **Total Skor Akhir** | | | | |

## E. Diskusi dan Analisis
1. Jelaskan fungsi dari variabel global `soalList`, `indexSoal`, `skor`, dan `jawabanBenar`.
2. Mengapa struktur data list digunakan untuk menyimpan soal dan jawaban? Apa alternatif lain?
3. Bagaimana cara kerja blok percabangan (if/else) saat mengecek jawaban? Jelaskan alurnya.
4. Apa yang terjadi jika pemain tidak memilih jawaban dan langsung mengklik "Soal Selanjutnya"? Bagaimana cara mencegahnya?
5. Buatlah saran pengembangan: fitur apa yang bisa ditambahkan agar aplikasi kuis ini lebih menarik?

## F. Kesimpulan
Tuliskan kesimpulan dari praktikum ini minimal 3 poin.

## G. Penilaian

| Aspek | Bobot | Skor (1-4) | Nilai |
|-------|-------|------------|-------|
| Desain UI sesuai ketentuan | 20% | | |
| Variabel dan list tersusun benar | 20% | | |
| Blok logika berfungsi | 25% | | |
| Aplikasi berjalan di pengujian | 20% | | |
| Jawaban diskusi | 15% | | |
| **Total** | **100%** | | |
