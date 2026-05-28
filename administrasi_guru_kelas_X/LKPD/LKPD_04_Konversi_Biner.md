# LKPD - Konversi Bilangan Biner, Desimal, Heksadesimal
**Mata Pelajaran:** Informatika
**Kelas/Semester:** X / Ganjil
**Materi Pokok:** Bab 4 – Sistem Bilangan (Biner, Desimal, Heksadesimal, ASCII, RGB)
**Alokasi Waktu:** 2 JP (1 JP = 45 menit)

## A. Tujuan Pembelajaran
1. Peserta didik mampu menjelaskan konsep bilangan biner, desimal, dan heksadesimal.
2. Peserta didik mampu mengonversi bilangan biner ke desimal dan sebaliknya.
3. Peserta didik mampu mengonversi bilangan desimal ke heksadesimal dan sebaliknya.
4. Peserta didik mampu membaca kode ASCII dan mengonversi ke karakter.
5. Peserta didik mampu menjelaskan representasi warna RGB dalam heksadesimal.

## B. Alat dan Bahan
1. Alat tulis (pulpen, pensil, kalkulator).
2. Tabel ASCII (disediakan guru atau dicari di internet).
3. Komputer/laptop (untuk mengecek hasil konversi).

## C. Langkah Kerja

### Tahap 1: Konversi Biner ke Desimal
1. Pelajari nilai tempat bilangan biner (basis 2):

   | 2⁷ | 2⁶ | 2⁵ | 2⁴ | 2³ | 2² | 2¹ | 2⁰ |
   |----|----|----|----|----|----|----|----|
   | 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |

2. Konversikan bilangan biner berikut ke desimal dengan cara menjumlahkan nilai tempat yang bernilai 1.

   Contoh: `1011₂` = 1×8 + 0×4 + 1×2 + 1×1 = 8 + 0 + 2 + 1 = **11₁₀**

   Kerjakan:
   a) `1101₂` = ...
   b) `10010₂` = ...
   c) `11111₂` = ...
   d) `101010₂` = ...
   e) `1100110₂` = ...

### Tahap 2: Konversi Desimal ke Biner
1. Gunakan metode pembagian berulang dengan 2. Catat sisa (remainder) dari bawah ke atas.

   Contoh: `25₁₀` → 25÷2=12 sisa **1**, 12÷2=6 sisa **0**, 6÷2=3 sisa **0**, 3÷2=1 sisa **1**, 1÷2=0 sisa **1** → dibaca dari bawah = **11001₂**

   Kerjakan:
   a) `15₁₀` = ...₂
   b) `42₁₀` = ...₂
   c) `99₁₀` = ...₂
   d) `128₁₀` = ...₂
   e) `255₁₀` = ...₂

### Tahap 3: Konversi Heksadesimal (Basis 16)
1. Pelajari digit heksadesimal: 0,1,2,...9,A(10),B(11),C(12),D(13),E(14),F(15).

2. **Desimal → Heksadesimal:** Bagi bilangan dengan 16, catat sisa.

   Contoh: `254₁₀` → 254÷16=15 sisa **14(E)**, 15÷16=0 sisa **15(F)** → **FE₁₆**

   a) `30₁₀` = ...₁₆
   b) `100₁₀` = ...₁₆
   c) `255₁₀` = ...₁₆

3. **Heksadesimal → Desimal:** Kalikan setiap digit dengan 16ⁿ.

   Contoh: `A5₁₆` = 10×16 + 5×1 = 160+5 = **165₁₀**

   a) `1A₁₆` = ...₁₀
   b) `FF₁₆` = ...₁₀
   c) `B3₁₆` = ...₁₀

### Tahap 4: Membaca Kode ASCII
1. Gunakan tabel ASCII berikut:

   | Desimal | Biner | Karakter |
   |---------|-------|----------|
   | 65 | 1000001 | A |
   | 66 | 1000010 | B |
   | 97 | 1100001 | a |
   | 98 | 1100010 | b |
   | 48 | 0110000 | 0 |
   | 49 | 0110001 | 1 |

2. Konversikan kode ASCII berikut ke karakter:
   a) `72` = ...
   b) `101` = ...
   c) `108` = ...
   d) `108` = ...
   e) `111` = ...

3. Karakter apa yang terbentuk dari no 2? Tuliskan kata yang dihasilkan: **.........**

### Tahap 5: Warna RGB dalam Heksadesimal
1. Warna RGB direpresentasikan sebagai `#RRGGBB` dalam heksadesimal.
   - RR = intensitas merah (00-FF)
   - GG = intensitas hijau (00-FF)
   - BB = intensitas biru (00-FF)

2. Contoh: `#FF0000` = Merah murni (R=255, G=0, B=0).

3. Konversikan kode warna berikut ke nilai RGB desimal:

   | Kode Heksa | R (des) | G (des) | B (des) | Warna |
   |------------|---------|---------|---------|-------|
   | #00FF00 | 0 | 255 | 0 | Hijau |
   | #0000FF | | | | |
   | #FFFFFF | | | | |
   | #000000 | | | | |
   | #FF8800 | | | | |

## D. Tabel Hasil

| No | Jenis Konversi | Soal | Hasil | Cek (Benar/Salah) |
|----|----------------|------|-------|-------------------|
| 1 | Biner → Desimal | 1101₂ | | |
| 2 | Biner → Desimal | 101010₂ | | |
| 3 | Desimal → Biner | 42₁₀ | | |
| 4 | Desimal → Biner | 255₁₀ | | |
| 5 | Desimal → Heksa | 100₁₀ | | |
| 6 | Heksa → Desimal | FF₁₆ | | |
| 7 | ASCII → Karakter | 72 101 108 108 111 | | |
| 8 | RGB Heksa → Des | #FF8800 | | |

## E. Diskusi dan Analisis
1. Mengapa komputer menggunakan sistem biner (basis 2) dan bukan desimal (basis 10)?
2. Dalam kehidupan sehari-hari, di mana saja kita menemukan sistem heksadesimal?
3. Apa hubungan antara ASCII dan pengkodean teks di komputer?
4. Jika warna merah penuh adalah `#FF0000` dan biru penuh adalah `#0000FF`, bagaimana cara membuat warna ungu (`#....`) dan kuning (`#....`)?
5. Berapa jumlah maksimum warna yang dapat direpresentasikan dengan 6 digit heksadesimal? Jelaskan!

## F. Kesimpulan
Tuliskan kesimpulan tentang pentingnya sistem bilangan dalam komputer dan bagaimana kaitannya dengan ASCII dan RGB!

## G. Penilaian

| Aspek | Skor Maks |
|-------|-----------|
| Ketepatan konversi biner↔desimal | 25 |
| Ketepatan konversi heksadesimal | 20 |
| Ketepatan pembacaan ASCII | 15 |
| Ketepatan konversi RGB | 15 |
| Jawaban diskusi | 15 |
| Kerapihan penulisan | 10 |
| **Total** | **100** |
