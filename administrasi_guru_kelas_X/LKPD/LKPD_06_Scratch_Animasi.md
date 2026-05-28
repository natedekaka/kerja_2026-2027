# LKPD - Animasi Sederhana dengan Scratch
**Mata Pelajaran:** Informatika
**Kelas/Semester:** X / Ganjil
**Materi Pokok:** Bab 7 – Algoritma dan Pemrograman (Scratch: Animasi)
**Alokasi Waktu:** 2 JP (1 JP = 45 menit)

## A. Tujuan Pembelajaran
1. Peserta didik mampu menjelaskan konsep sprite, backdrop, dan block script di Scratch.
2. Peserta didik mampu membuat program animasi sederhana menggunakan Scratch.
3. Peserta didik mampu menggunakan blok **Motion**, **Looks**, **Events**, dan **Control**.
4. Peserta didik mampu menambahkan interaksi keyboard pada animasi.

## B. Alat dan Bahan
1. Komputer/laptop dengan koneksi internet.
2. Browser (Chrome/Edge/Firefox).
3. Akun Scratch (opsional, bisa pakai mode offline/online di scratch.mit.edu).

## C. Langkah Kerja

### Tahap 1: Mengenal Antarmuka Scratch
1. Buka https://scratch.mit.edu → Klik **Create** (atau "Buat").
2. Kenali 4 area utama:
   - **Blok Palette** (kiri) — kumpulan blok perintah berwarna.
   - **Script Area** (tengah) — tempat menyusun blok.
   - **Stage** (kanan atas) — tempat animasi berjalan.
   - **Sprite List** (kanan bawah) — daftar karakter/sprite.
3. Catat nama dan warna masing-masing kategori blok:
   - Motion (biru tua)
   - Looks (biru)
   - Sound (ungu)
   - Events (kuning)
   - Control (oranye)
   - Sensing (biru muda)
   - Operators (hijau)
   - Variables (oranye tua)

### Tahap 2: Membuat Animasi Sprite Bergerak
1. Hapus sprite kucing default (klik ikon tempat sampah).
2. Tambahkan sprite baru:
   - Klik ikon **Choose a Sprite** (icon kucing +) → pilih **Pikachu** atau **Cat Flying** atau sprite favorit.
3. Tambahkan backdrop:
   - Klik **Choose a Backdrop** → pilih **Blue Sky** atau **Savanna**.
4. Susun kode untuk **sprite** agar bergerak dari kiri ke kanan:

   ```
   Ketika [bendera hijau] diklik
   set ukuran ke 50%
   pergi ke x: (-200) y: (0)
   ulang (20) kali
       geser (1) detik ke x: (posisi x + 20) y: (0)
       tunggu (0.1) detik
   akhir
   ```

   **Catatan:** Gunakan blok berikut dari palette:
   - `when green flag clicked` (Events)
   - `set size to 50 %` (Looks)
   - `go to x: -200 y: 0` (Motion)
   - `repeat 20` (Control)
   - `glide 1 secs to x: ... y: ...` (Motion)
   - `wait 0.1 seconds` (Control)

5. Klik bendera hijau untuk menjalankan. Sprite akan meluncur ke kanan.

### Tahap 3: Menambahkan Animasi Berputar
1. Tambahkan sprite kedua (misalnya **Butterfly** atau **Ball**).
2. Buat kode untuk sprite kedua:

   ```
   Ketika [bendera hijau] diklik
   set ukuran ke 30%
   pergi ke x: (100) y: (100)
   selamanya
       putar (15) derajat
       tunggu (0.1) detik
   akhir
   ```

3. Jalankan dengan bendera hijau. Sprite kedua akan berputar terus.

### Tahap 4: Menambahkan Interaksi Keyboard
1. Pilih sprite pertama (yang bergerak).
2. Buat script baru yang merespon tombol panah:

   ```
   Ketika [spasi] ditekan
   set (kecepatan) ke (10)
   ulang (5) kali
       ubah x oleh (kecepatan)
       tunggu (0.05) detik
   akhir
   ```

3. Tambahkan script untuk tombol panah kiri:

   ```
   Ketika [panah kiri] ditekan
   ubah x oleh (-20)
   ```

4. Coba tekan **spasi** dan **panah kiri** untuk menggerakkan sprite.

### Tahap 5: Animasi Berubah Warna
1. Pilih sprite mana pun.
2. Buat script:

   ```
   Ketika [bendera hijau] diklik
   selamanya
       ubah efek [warna] sebesar (25)
       tunggu (0.5) detik
   akhir
   ```

3. Jalankan. Sprite akan berubah-ubah warna.

### Tahap 6: Menyimpan Proyek
1. Klik **File** → **Save to your computer**.
2. Simpan dengan nama **"Animasi_Kelas_X_[Nama]_[NoAbsen].sb3"**.

## D. Tabel Hasil Pengamatan

| No | Fitur | Blok yang Digunakan | Berfungsi? (Ya/Tidak) | Keterangan |
|----|-------|---------------------|-----------------------|------------|
| 1 | Sprite bergerak kiri→kanan | | | |
| 2 | Sprite berputar | | | |
| 3 | Interaksi keyboard (spasi) | | | |
| 4 | Interaksi keyboard (panah) | | | |
| 5 | Efek berubah warna | | | |

## E. Diskusi dan Analisis
1. Apa fungsi blok `repeat` dan `forever`? Apa perbedaannya?
2. Jika ingin sprite bergerak ke kiri, perubahan nilai x-nya positif atau negatif? Jelaskan!
3. Bagaimana cara membuat sprite memantul saat menyentuh tepi stage?
4. Blok apa yang digunakan untuk merespon input dari keyboard? Sebutkan minimal 2!
5. Jika ingin sprite berbicara "Halo!" saat disentuh sprite lain, blok apa saja yang diperlukan?

## F. Kesimpulan
Tuliskan kesimpulan tentang bagaimana Scratch digunakan untuk membuat animasi dan bagaimana kaitannya dengan konsep algoritma!

## G. Penilaian

| Aspek | Skor Maks |
|-------|-----------|
| Sprite bergerak dari kiri ke kanan | 20 |
| Animasi berputar (sprite kedua) | 15 |
| Interaksi keyboard (spasi & panah) | 20 |
| Efek perubahan warna | 10 |
| Proyek tersimpan (.sb3) | 10 |
| Tabel hasil & jawaban diskusi | 25 |
| **Total** | **100** |
