# LKPD - Mail Merge Surat Undangan
**Mata Pelajaran:** Informatika
**Kelas/Semester:** X / Ganjil
**Materi Pokok:** Bab 3 – Teknologi Informasi dan Komunikasi (Mail Merge)
**Alokasi Waktu:** 2 JP (1 JP = 45 menit)

## A. Tujuan Pembelajaran
1. Peserta didik mampu menjelaskan fungsi Mail Merge dalam pembuatan dokumen massal.
2. Peserta didik mampu membuat data penerima menggunakan spreadsheet (Excel/Google Sheets).
3. Peserta didik mampu membuat dokumen induk (surat) dan menggabungkannya dengan data penerima.
4. Peserta didik mampu mencetak atau menyimpan hasil Mail Merge.

## B. Alat dan Bahan
1. Komputer/laptop dengan MS Office (Word + Excel) **atau** akses Google Docs + Google Sheets.
2. Proyektor/LCD (opsional untuk demonstrasi guru).
3. Jaringan internet (jika menggunakan Google Workspace).

## C. Langkah Kerja

### Tahap 1: Membuat Data Penerima di Spreadsheet
1. Buka **MS Excel** (atau **Google Sheets**).
2. Buat tabel dengan kolom berikut pada **baris pertama (header)**:
   - `No`
   - `Nama`
   - `Alamat`
   - `Kota`
   - `Keperluan`
3. Isi **minimal 5 baris data** penerima undangan. Contoh:

   | No | Nama | Alamat | Kota | Keperluan |
   |----|------|--------|------|-----------|
   | 1 | Andi Pratama | Jl. Merdeka No. 10 | Jakarta | Rapat OSIS |
   | 2 | Siti Rahma | Jl. Kenanga No. 5 | Bandung | Pelatihan |
   | 3 | Budi Santoso | Jl. Mangga III/7 | Surabaya | Sosialisasi |
   | 4 | Dewi Lestari | Jl. Anggrek 12 | Semarang | Rapat |
   | 5 | Rizky Hidayat | Jl. Melati 8 | Medan | Workshop |

4. **Simpan file** dengan nama `Data_Undangan.xlsx` (atau di Google Sheets beri judul "Data Undangan").
5. **Catat** nama sheet-nya (default: `Sheet1`), karena akan digunakan di Mail Merge.

### Tahap 2: Membuat Dokumen Induk (Surat Undangan)
1. Buka **MS Word** (atau **Google Docs**).
2. Buat dokumen surat undangan seperti berikut:
   ```
   [Tempat], [Tanggal]

   Kepada Yth.
   «Nama»
   «Alamat»
   «Kota»

   Perihal: Undangan «Keperluan»

   Dengan hormat,

   Kami mengundang Saudara «Nama» untuk hadir pada acara «Keperluan» yang akan diselenggarakan pada:

   Hari/Tanggal : Sabtu, 15 November 2025
   Waktu        : 09.00 WIB
   Tempat       : Aula Sekolah

   Demikian undangan ini disampaikan. Atas perhatiannya, kami ucapkan terima kasih.

   Hormat kami,
   Ketua Panitia
   ```
3. **Jangan** tuliskan `«...»` secara manual — itu akan diganti dengan *merge field* nanti.

### Tahap 3: Mail Merge di MS Word
1. Klik tab **Mailings** → **Start Mail Merge** → **Letters**.
2. Klik **Select Recipients** → **Use an Existing List**.
3. Pilih file `Data_Undangan.xlsx` → pilih sheet yang berisi data (misal `Sheet1$`) → OK.
4. Tempatkan kursor di posisi setelah "Kepada Yth." lalu tekan **Enter**.
5. Klik **Insert Merge Field** → pilih **Nama**. Tekan Enter, lalu pilih **Alamat**, Enter, lalu **Kota**.
6. Di baris "Perihal: Undangan ...", klik **Insert Merge Field** → pilih **Keperluan**.
7. Di dalam paragraf surat, klik setelah "Saudara" lalu **Insert Merge Field** → **Nama**. Lakukan juga untuk **Keperluan** di kalimat berikutnya.
8. Klik **Preview Results** untuk melihat hasil gabungan. Gunakan tombol panah untuk melihat data satu per satu.
9. Jika sudah sesuai, klik **Finish & Merge** → **Print Documents** atau **Edit Individual Documents**.

### Tahap 3 Alternatif: Mail Merge di Google Docs
1. Buka **Google Docs**, buat dokumen surat seperti langkah Tahap 2.
2. Buka menu **Extensions** → **Add-ons** → **Get add-ons**.
3. Cari dan instal **"Mail Merge with Attachments"** (atau ekstensi sejenis).
4. Buka kembali **Extensions** → pilih ekstensi Mail Merge → **Start Mail Merge**.
5. Hubungkan ke **Google Sheets** yang sudah dibuat.
6. Pilih sheet → petakan kolom ke *placeholder* `{{Nama}}`, `{{Alamat}}`, `{{Kota}}`, `{{Keperluan}}`.
7. Klik **Send emails** atau **Merge & Save** untuk menghasilkan dokumen akhir.

## D. Tabel Hasil Pengamatan

| No | Nama Penerima | Alamat Lengkap | Keperluan | Hasil Mail Merge (Sesuai/Tidak) |
|----|---------------|----------------|-----------|----------------------------------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |

**Petunjuk:** Isi kolom hasil dengan "Sesuai" jika data berhasil digabungkan dengan benar, atau "Tidak" jika ada kesalahan.

## E. Diskusi dan Analisis
1. Apa keuntungan menggunakan Mail Merge dibandingkan mengetik surat satu per satu?
2. Bagaimana cara menghindari kesalahan data saat Mail Merge?
3. Apa yang terjadi jika jumlah kolom di spreadsheet tidak sesuai dengan *merge field* di dokumen induk?
4. Jelaskan perbedaan Mail Merge menggunakan MS Office dengan Google Workspace!
5. Selain surat undangan, berikan 2 contoh dokumen lain yang dapat dibuat dengan Mail Merge!

## F. Kesimpulan
Tuliskan kesimpulan tentang apa itu Mail Merge, langkah-langkahnya, dan manfaatnya dalam kehidupan sehari-hari!

## G. Penilaian

| Aspek | Skor Maks |
|-------|-----------|
| Kelengkapan data spreadsheet (min 5 data) | 20 |
| Kesesuaian format dokumen induk | 20 |
| Keberhasilan Mail Merge (semua field terisi) | 30 |
| Tabel hasil pengamatan terisi lengkap | 15 |
| Jawaban diskusi dan kesimpulan | 15 |
| **Total** | **100** |
