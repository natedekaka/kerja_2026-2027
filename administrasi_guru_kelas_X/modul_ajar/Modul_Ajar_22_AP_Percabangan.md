# MODUL AJAR INFORMATIKA KELAS X

## AP: STRUKTUR PERCABANGAN DALAM PYTHON

---

### A. INFORMASI UMUM

| Komponen | Deskripsi |
|---|---|
| Satuan Pendidikan | SMA Negeri 6 Cimahi |
| Mata Pelajaran | Informatika |
| Kelas / Fase | X (Sepuluh) / Fase E |
| Elemen | AP — Algoritma & Pemrograman |
| Tujuan Pembelajaran | TP.7.3: Menerapkan struktur percabangan dalam Python |
| Alokasi Waktu | 2 JP (2 × 45 menit) |
| Pertemuan ke- | 2 (dua) |
| Kompetensi Awal | Peserta didik telah memahami konsep notasi algoritma (pseudocode dan flowchart) dan telah menulis program sederhana di Python (input, output, variabel, tipe data) |
| Integrasi 8 Dimensi | Kreativitas, Penalaran Kritis, Kemandirian |
| **Integrasi 7 KAIH** | Gemar Belajar, Bangun Pagi |
| **Pendekatan Deep Learning** | Mindful → Mining → Joyful |
| Sarana & Prasarana | Proyektor/LCD, laptop/komputer, Python IDLE atau Google Colab/Replit, koneksi internet, papan tulis |
| Target Peserta Didik | Reguler (dengan diferensiasi untuk peserta didik yang membutuhkan bimbingan dan percepatan) |
| Model Pembelajaran | Demonstrasi interaktif dan praktik coding (Pair Programming) |
| Metode | Demonstrasi, tanya jawab, praktik berpasangan, pemecahan masalah, error hunting |
| Sumber Belajar | Buku Informatika Kelas X Bab 7, dokumentasi Python resmi (docs.python.org), tutorial W3Schools Python, modul ajar guru |

### B. TUJUAN PEMBELAJARAN
### B.1 PEMAHAMAN BERMAKNA (MEANINGFUL)
Pemrograman adalah cara kita 'berbicara' dengan komputer dan menciptakan solusi digital untuk masalah nyata.


### B.2 PERTANYAAN PEMANTIK (MINDFUL)
1. Apa yang akan terjadi jika...?
2. Bagaimana konsep ini terhubung dengan kehidupan sehari-harimu?
3. Mengapa materi ini penting untuk dipelajari?

#### B.1 Tujuan Pembelajaran
1. Menjelaskan konsep percabangan (decision-making) dalam pemrograman dan analoginya dalam kehidupan sehari-hari.
2. Menerapkan struktur if, if-else, if-elif-else, dan nested if dalam bahasa Python dengan sintaks yang benar.
3. Membuat program yang menggunakan percabangan untuk menyelesaikan masalah dengan kondisi bersyarat.
4. Mengidentifikasi dan memperbaiki error yang umum terjadi dalam penulisan struktur percabangan.
5. Menguji program percabangan dengan berbagai skenario input untuk memvalidasi kebenaran logika.

#### B.2 Indikator Keberhasilan
| Indikator | Kriteria |
|---|---|
| 1. Menjelaskan percabangan | Mampu menjelaskan perbedaan if, if-else, dan if-elif-else dengan analogi yang tepat |
| 2. Menulis sintaks percabangan | Kode Python menggunakan indentasi yang benar, tanda titik dua (:) setelah kondisi, dan struktur yang rapi |
| 3. Membuat program percabangan | Program mengandung minimal 2 jenis struktur percabangan dan berfungsi sesuai spesifikasi |
| 4. Error hunting | Menemukan minimal 4 dari 5 error yang sengaja ditanamkan dalam waktu 10 menit |
| 5. Pengujian program | Menguji program dengan minimal 3 skenario input berbeda dan mencatat hasilnya |

#### B.3 Kata Kunci
Percabangan, if, else, elif, nested if, kondisi boolean, operator perbandingan (==, !=, <, >, <=, >=), operator logika (and, or, not), indentasi, seleksi kondisi, decision making

### C. KEGIATAN PEMBELAJARAN

| **Fase DL** | **Tahap** | **Waktu** | **Aktivitas Guru** | **Aktivitas Siswa** | **Media/Sumber** |
|---|---|---|---|---|---|
| **MINDFULL** | **Pemanasan** | 10' | Guru membuka kelas, mengecek kehadiran. Guru memantik dengan pertanyaan: "Program yang cuma jalan lurus tidak berguna. Program pintar harus bisa mengambil keputusan — bagaimana caranya?" Guru mereview program input-output sederhana. | Siswa merespons dan menjawab pertanyaan guru. Siswa mengingat kembali cara menulis program input-output di Python. | Proyektor, slide pembuka |
| **MINING FULL** | **Eksplorasi** — Sesi 1** | 15' | Guru menjelaskan konsep percabangan if, if-else, if-elif-else, dan nested if dengan analogi lampu lalu lintas (if merah → stop, if hijau → jalan, if kuning → hati-hati). Guru menuliskan sintaks dasar di papan tulis disertai contoh. | Siswa menyimak, mencatat sintaks, dan mengajukan pertanyaan. Siswa secara bergantian menyebutkan analogi percabangan lain dari kehidupan sehari-hari. | Papan tulis, slide sintaks Python |
| **MINING FULL** | **Eksplorasi** — Sesi 2** | 15' | Guru melakukan demo coding: program lulus/tidak lulus. Guru menulis kode if nilai >= 75: print("Lulus") else: print("Tidak lulus") sambil siswa menulis ulang di komputer masing-masing (code along). | Siswa menulis kode yang didemokan guru. Siswa mencoba mengubah nilai input dan mengamati perubahan output. | Python IDLE/Colab, proyektor |
| **MINING FULL** | **Eksplorasi** — Praktik 1** | 15' | Guru memberikan tugas: buat program penentu kelulusan dengan tiga kategori (lulus >= 75, remidi 60-74, tidak lulus < 60). Guru berkeliling membantu siswa yang kesulitan. | Siswa menulis program penentu kelulusan secara berpasangan. Siswa menguji program dengan nilai 80, 65, dan 50. | LKPD, Python IDLE/Colab |
| **MINING FULL** | **Eksplorasi** — Praktik 2** | 20' | Guru memberikan studi kasus "Kalkulator Sederhana": program menerima 2 angka dan pilihan operasi (+, -, *, /) menggunakan if-elif-else. Guru menekankan penanganan pembagian dengan nol. | Siswa membuat kalkulator sederhana secara mandiri. Siswa menguji setiap operasi dan mencatat hasil. Siswa mempresentasikan kode di depan kelas. | LKPD, Python IDLE/Colab |
| **MINING FULL** | **Eksplorasi** — Sesi 3** | 10' | Guru memberikan kode yang mengandung 5 error (indentasi, missing colon, salah operator, typo variabel) — siswa berlomba mencari dan memperbaiki error (error hunting). | Siswa mencari dan memperbaiki error secara individu. Siswa yang pertama menemukan semua error mendapat apresiasi. | Kode error di proyektor, Python IDLE |
| **JOYFULL** | **Penutup Kreatif** | 15' | Guru memberikan tugas: program "tiket bioskop" — input umur (anak < 13, dewasa 13-59, lansia >= 60) dengan harga tiket berbeda. Guru menyimpulkan materi dan menutup kelas. | Siswa mencatat tugas. Siswa menyimpulkan 3 hal penting tentang percabangan. Siswa berdoa. | Papan tulis, buku catatan |

### D. ASESMEN

#### D.1 Asesmen Diagnostik (Awal)
| Pertanyaan | Tujuan |
|---|---|
| Apa fungsi tanda titik dua (:) dalam Python? | Mengetahui pemahaman tentang sintaks dasar Python |
| Apa perbedaan antara = dan == dalam Python? | Mengidentifikasi kesalahan konsep assignment vs perbandingan |
| Sebutkan operator perbandingan yang kalian ketahui! | Mengetahui sejauh mana siswa mengenal operator relasional |

#### D.2 Asesmen Formatif (Proses)
- Observasi guru selama praktik coding: mencatat siswa yang berhasil menyelesaikan praktik 1 dan 2.
- Hasil error hunting: jumlah error yang ditemukan setiap siswa.
- Cek hasil pengujian program (minimal 3 skenario input).

#### D.3 Asesmen Sumatif (Akhir)
- Produk Python: program kalkulator sederhana (Praktik 2) — dinilai dengan rubrik.
- Tugas rumah: program tiket bioskop dengan percabangan.

#### D.4 Rubrik Penilaian Program Percabangan
| Aspek | SB (4) | B (3) | C (2) | PB (1) |
|---|---|---|---|---|---|
| **Struktur percabangan** | Menggunakan minimal 3 jenis struktur (if, if-else, if-elif-else) dengan benar | Menggunakan 2 jenis struktur dengan benar | Hanya menggunakan if-else, struktur kurang bervariasi | Hanya menggunakan if tanpa else |
| **Sintaks dan indentasi** | Tidak ada error sintaks, indentasi rapi dan konsisten (4 spasi) | 1 error sintaks minor, indentasi sebagian rapi | 2 error sintaks, indentasi tidak rapi | Banyak error sintaks, tidak ada indentasi |
| **Fungsionalitas** | Semua fitur berjalan sesuai spesifikasi dan telah diuji dengan 3 skenario | Sebagian besar fitur berjalan, 1 fitur tidak berfungsi | Beberapa fitur tidak berfungsi | Program tidak dapat dijalankan |
| **Penanganan error** | Menangani input tidak valid (pembagian nol, input huruf) | Menangani sebagian kasus error | Hanya menangani 1 jenis error | Tidak ada penanganan error |

#### D.5 Contoh Soal
**Soal:** Buatlah program Python yang menerima input nilai ujian (0-100) dan menentukan grade nilai:
- A: 86-100
- B: 71-85
- C: 56-70
- D: 41-55
- E: 0-40

Program juga harus menangani input nilai di luar rentang (kurang dari 0 atau lebih dari 100) dengan menampilkan pesan "Nilai tidak valid".

### E. LEMBAR KERJA PESERTA DIDIK (LKPD)

**Nama:** __________________________ **Kelas:** X ___

#### E.1 Praktik 1 — Program Penentu Kelulusan (Mudah)
Buatlah program Python yang menerima input nilai siswa dan menentukan status:

```python
# Program Penentu Kelulusan
# Input: nilai siswa (0-100)
# Output: Lulus (>=75), Remidi (60-74), Tidak Lulus (<60)

nilai = int(input("Masukkan nilai siswa: "))

# Tulis kode percabangan Anda di sini
if nilai >= 75:
    print("Lulus")
elif nilai >= 60:
    print("Remidi")
else:
    print("Tidak Lulus")
```

**Kembangkan program di atas agar:**
1. Menampilkan pesan error jika nilai < 0 atau > 100
2. Menambahkan kategori "Lulus dengan Pujian" jika nilai >= 90

#### E.2 Praktik 2 — Kalkulator Sederhana (Sedang)
```python
# Kalkulator Sederhana
print("=== KALKULATOR SEDERHANA ===")
a = float(input("Masukkan angka pertama: "))
b = float(input("Masukkan angka kedua: "))
print("Pilih operasi:")
print("1. Penjumlahan (+)")
print("2. Pengurangan (-)")
print("3. Perkalian (*)")
print("4. Pembagian (/)")
pilihan = int(input("Masukkan pilihan (1-4): "))

# Tulis struktur percabangan di sini
if pilihan == 1:
    hasil = a + b
    print(f"Hasil: {a} + {b} = {hasil}")
elif pilihan == 2:
    hasil = a - b
    print(f"Hasil: {a} - {b} = {hasil}")
elif pilihan == 3:
    hasil = a * b
    print(f"Hasil: {a} * {b} = {hasil}")
elif pilihan == 4:
    if b != 0:
        hasil = a / b
        print(f"Hasil: {a} / {b} = {hasil}")
    else:
        print("Error: Pembagian dengan nol tidak diperbolehkan!")
else:
    print("Pilihan tidak valid!")
```

**Tugas:** Modifikasi program di atas sehingga pengguna bisa memilih untuk menghitung ulang atau keluar setelah satu perhitungan selesai.

#### E.3 Error Hunting (Sulit)
Perbaiki 5 error dalam kode berikut:

```python
# Program menentukan hari libur
hari = input("Masukkan nama hari: ")

if hari = "Sabtu" or "Minggu":   # Error 1 & 2
print("Hari ini libur!")          # Error 3
elif hari = "Jumat":              # Error 4
    print("Hari ini setengah libur")
else
    print("Hari ini belajar")     # Error 5
```

**Jawaban:**
1. _____ 2. _____ 3. _____ 4. _____ 5. _____

### F. DIFERENSIASI PEMBELAJARAN

| Level | Deskripsi |
|---|---|
| **Level 1 (Bimbingan)** | Siswa diberikan template kode yang sudah berisi struktur dasar. Siswa hanya perlu mengisi bagian kondisi (if, else) pada titik-titik yang disediakan. Guru mendampingi secara langsung saat praktik. |
| **Level 2 (Reguler)** | Siswa mengerjakan seluruh LKPD secara mandiri atau berpasangan. Siswa menulis kode dari awal tanpa template. |
| **Level 3 (Percepatan)** | Siswa menyelesaikan semua soal plus tantangan tambahan: buat program "BMI Calculator" dengan kategori (kurus, normal, gemuk, obesitas) menggunakan percabangan bersarang (nested if). Siswa juga diminta menambahkan fitur penyimpanan riwayat perhitungan ke dalam file teks. |

### G. REFLEKSI GURU

| Aspek Refleksi | Catatan |
|---|---|
| Apakah siswa memahami konsep percabangan dengan analogi yang diberikan? | |
| Seberapa banyak siswa yang berhasil menyelesaikan praktik 2 (kalkulator)? | |
| Apakah error hunting efektif untuk meningkatkan pemahaman sintaks? | |
| Bagian mana yang paling banyak menyebabkan error pada siswa? | |

### H. BAHAN BACAAN UNTUK GURU

- **Buku Informatika Kelas X, Bab 7** — Penerbit Kemdikbudristek
- **Python Official Documentation — Control Flow Tools** — https://docs.python.org/3/tutorial/controlflow.html
- **"Think Python: How to Think Like a Computer Scientist" oleh Allen B. Downey** — Bab 5 (Conditionals and Recursion)
- **W3Schools Python If...Else Tutorial** — https://www.w3schools.com/python/python_conditions.asp
- **Python Tutor (Visualizer)** — https://pythontutor.com/ — alat bantu visual untuk melacak eksekusi kode percabangan baris per baris

---
