# LKPD - Game Interaktif dengan Scratch
**Mata Pelajaran:** Informatika
**Kelas/Semester:** X / Ganjil
**Materi Pokok:** Bab 7 – Algoritma dan Pemrograman (Scratch: Game Interaktif)
**Alokasi Waktu:** 2 JP (1 JP = 45 menit)

## A. Tujuan Pembelajaran
1. Peserta didik mampu membuat game interaktif sederhana menggunakan Scratch.
2. Peserta didik mampu menggunakan **Variables** untuk skor dan timer.
3. Peserta didik mampu menggunakan blok **Sensing** untuk mendeteksi tumbukan.
4. Peserta didik mampu menggunakan blok **Broadcast** untuk komunikasi antar sprite.

## B. Alat dan Bahan
1. Komputer/laptop dengan koneksi internet.
2. Browser (Chrome/Edge/Firefox).
3. Akun Scratch (opsional) atau mode online di scratch.mit.edu.

## C. Langkah Kerja

### Tahap 1: Membuat Game Tangkap Objek (Falling Objects)

#### a. Persiapan Stage dan Sprite
1. Buka https://scratch.mit.edu → **Create**.
2. Hapus sprite kucing default.
3. Tambahkan sprite **Bowl** (mangkuk) dari library — sprite ini sebagai penangkap.
4. Tambahkan sprite **Apple** (apel) — sebagai objek yang jatuh.
5. Pilih backdrop **Neon Tunnel** atau **Space** atau polos.

#### b. Membuat Variabel
1. Klik **Variables** (Variabel) → **Make a Variable**.
2. Buat variabel **`skor`** (untuk semua sprite).
3. Buat variabel **`waktu`** (untuk semua sprite).
4. Centang kotak di samping nama variabel agar muncul di Stage.

#### c. Kode untuk Sprite Bowl (Mangkuk)

```
Ketika [bendera hijau] diklik
set ukuran ke 80%
pergi ke x: (0) y: (-150)
set [skor] ke (0)
set [waktu] ke (30)
ulang (30) kali  // timer mundur
    tunggu (1) detik
    ubah [waktu] oleh (-1)
akhir
siarkan [gameover] dan tunggu
```

```
Ketika [bendera hijau] diklik
selamanya
    jika (tombol [panah kanan] ditekan?) maka
        ubah x oleh (10)
    akhir
    jika (tombol [panah kiri] ditekan?) maka
        ubah x oleh (-10)
    akhir
akhir
```

#### d. Kode untuk Sprite Apple (Apel)

```
Ketika [bendera hijau] diklik
selamanya
    pergi ke x: (angka acak antara (-220) dan (220)) y: (180)
    ulang (sampai (posisi y) < (-170))
        jika (menyentuh [Bowl]?) maka
            ubah [skor] oleh (1)
            berhenti [script ini]
        akhir
        ubah y oleh (-5)
        tunggu (0.05) detik
    akhir
    tunggu (0.5) detik
akhir
```

*Penjelasan:* Apel muncul di posisi acak atas, jatuh perlahan. Jika menyentuh Bowl, skor +1.

#### e. Menambahkan Efek Game Over

1. Buat sprite baru (atau gunakan sprite teks) untuk menampilkan "Game Over".
2. Buat script:

```
Ketika saya menerima [gameover]
tampilkan
pergi ke x: (0) y: (0)
set ukuran ke 200%
```

3. Atur sprite ini agar **tersembunyi** saat game dimulai:

```
Ketika [bendera hijau] diklik
sembunyikan
```

### Tahap 2: Menambahkan Level Kesulitan
1. Duplikat sprite Apple (klik kanan → duplicate) sehingga ada 2 atau 3 apel.
2. Atur kecepatan jatuh yang berbeda (misal ubah `ubah y oleh (-5)` menjadi -8 untuk lebih cepat).
3. Jalankan game. Skor akan bertambah setiap berhasil menangkap apel.

### Tahap 3: Membuat Game Kuis Sederhana (Pengayaan)
Jika waktu memungkinkan, buat game kuis interaktif:

1. Tambahkan sprite **Think** atau sprite karakter yang bertanya.
2. Buat variabel **`jawaban`**.
3. Script kuis:

```
Ketika [bendera hijau] diklik
set [skor] ke (0)
tanya [Berapakah 7 + 8?] dan tunggu
jika (jawaban) = (15) maka
    ucapkan [Benar! ✓] selama (2) detik
    ubah [skor] oleh (10)
jika tidak
    ucapkan [Salah! ✗ Jawabannya: 15] selama (2) detik
akhir
tunggu (1) detik
tanya [Apa ibukota Indonesia?] dan tunggu
jika (jawaban) = [Jakarta] maka
    ucapkan [Benar!] selama (2) detik
    ubah [skor] oleh (10)
jika tidak
    ucapkan [Salah!] selama (2) detik
akhir
```

### Tahap 4: Menyimpan Proyek
1. Klik **File** → **Save to your computer**.
2. Simpan dengan nama **"Game_Tangkap_atau_Kuis_[Nama].sb3"**.

## D. Tabel Hasil Pengamatan

| No | Fitur Game | Blok Utama yang Digunakan | Berfungsi? (Ya/Tidak) |
|----|------------|--------------------------|-----------------------|
| 1 | Bowl bergerak dengan panah | | |
| 2 | Apel jatuh dari atas | | |
| 3 | Deteksi tumbukan Bowl-Apel | | |
| 4 | Skor bertambah saat menangkap | | |
| 5 | Timer mundur (30 detik) | | |
| 6 | Game over saat timer habis | | |
| 7 | Multiple apel / level | | |
| 8 | Kuis interaktif (pengayaan) | | |

## E. Diskusi dan Analisis
1. Jelaskan fungsi variabel `skor` dan `waktu` dalam game ini!
2. Bagaimana cara kerja blok `repeat until` pada script apel? Apa kondisi yang menghentikan perulangan?
3. Apa yang dimaksud dengan **broadcast** (`siarkan`) dan bagaimana cara kerjanya dalam game ini?
4. Jika ingin apel jatuh lebih cepat seiring waktu, bagaimana cara mengubah script-nya?
5. Apa perbedaan algoritma game **tangkap objek** dengan **game kuis**? Mana yang lebih kompleks?

## F. Kesimpulan
Tuliskan kesimpulan tentang proses pembuatan game interaktif dengan Scratch serta penerapan konsep variabel, perulangan, percabangan, dan event!

## G. Penilaian

| Aspek | Skor Maks |
|-------|-----------|
| Bowl bergerak (kontrol keyboard) | 10 |
| Objek jatuh dari atas | 15 |
| Deteksi tumbukan dan skor | 20 |
| Timer dan game over | 15 |
| Multiple sprite / level | 10 |
| Kuis interaktif (pengayaan) | 10 |
| Proyek tersimpan (.sb3) | 5 |
| Tabel hasil & jawaban diskusi | 15 |
| **Total** | **100** |
