# MODUL AJAR INFORMATIKA KELAS X

## AP: STRUKTUR PERULANGAN (LOOPING) DALAM PYTHON

---

### A. INFORMASI UMUM

| Komponen | Deskripsi |
|---|---|
| Satuan Pendidikan | SMA Negeri 6 Cimahi |
| Mata Pelajaran | Informatika |
| Kelas / Fase | X (Sepuluh) / Fase E |
| Elemen | AP — Algoritma & Pemrograman |
| Tujuan Pembelajaran | TP.7.4: Menerapkan perulangan (for, while) dalam Python |
| Alokasi Waktu | 2 JP (2 × 45 menit) |
| Pertemuan ke- | 3 (tiga) |
| Kompetensi Awal | Peserta didik telah memahami konsep nilai, variabel, tipe data, input-output, dan struktur percabangan if-elif-else dalam Python |
| Integrasi 8 Dimensi | Kreativitas, Penalaran Kritis, Kemandirian |
| **Integrasi 7 KAIH** | Gemar Belajar, Bangun Pagi |
| **Pendekatan Deep Learning** | Mindful → Mining → Joyful |
| Sarana & Prasarana | Proyektor/LCD, laptop/komputer, Python IDLE atau Google Colab, papan tulis, spidol warna |
| Target Peserta Didik | Reguler (dengan diferensiasi untuk peserta didik yang membutuhkan bimbingan dan percepatan) |
| Model Pembelajaran | Demonstrasi interaktif, praktik coding, dan tantangan pemrograman (Gamification) |
| Metode | Demonstrasi, tanya jawab, praktik individu, kompetisi coding, code review |
| Sumber Belajar | Buku Informatika Kelas X Bab 7, dokumentasi Python, W3Schools Python Loops, modul ajar guru |

### B. TUJUAN PEMBELAJARAN
### B.1 PEMAHAMAN BERMAKNA (MEANINGFUL)
Pemrograman adalah cara kita 'berbicara' dengan komputer dan menciptakan solusi digital untuk masalah nyata.


### B.2 PERTANYAAN PEMANTIK (MINDFUL)
1. Apa yang akan terjadi jika...?
2. Bagaimana konsep ini terhubung dengan kehidupan sehari-harimu?
3. Mengapa materi ini penting untuk dipelajari?

#### B.1 Tujuan Pembelajaran
1. Menjelaskan konsep perulangan (looping) dan perbedaan antara for loop dan while loop.
2. Menerapkan for loop dengan fungsi range() untuk iterasi dengan jumlah yang pasti.
3. Menerapkan while loop dengan kondisi boolean untuk iterasi dengan syarat tertentu.
4. Menggunakan nested loop (perulangan bersarang) untuk menyelesaikan masalah pola (pattern).
5. Memilih jenis perulangan yang tepat berdasarkan karakteristik masalah yang dihadapi.

#### B.2 Indikator Keberhasilan
| Indikator | Kriteria |
|---|---|
| 1. Menjelaskan perulangan | Mampu menyebutkan 3 perbedaan antara for dan while loop |
| 2. For loop | Program mencetak deret 1-10, tabel perkalian, dan menjumlah deret menggunakan for |
| 3. While loop | Program tebak angka berjalan dengan benar dan berhenti saat kondisi terpenuhi |
| 4. Nested loop | Menampilkan pola bintang segitiga dengan jumlah baris sesuai input pengguna |
| 5. Pemilihan jenis loop | Mampu menjelaskan alasan memilih for atau while pada studi kasus yang diberikan |

#### B.3 Kata Kunci
Perulangan, loop, iterasi, for, while, range(), nested loop, infinite loop, break, continue, kondisi berhenti, counter, akumulator

### C. KEGIATAN PEMBELAJARAN

| **Fase DL** | **Tahap** | **Waktu** | **Aktivitas Guru** | **Aktivitas Siswa** | **Media/Sumber** |
|---|---|---|---|---|---|
| **MINDFULL** | **Pemanasan** | 10' | Guru membuka kelas dan memantik: "Coba tulis angka 1 sampai 100 tanpa loop..." — siswa menyadari bahwa menulis manual tidak efisien. Guru mendemonstrasikan betapa repotnya tanpa loop. Guru menyampaikan TP dan manfaat perulangan. | Siswa mencoba membayangkan atau menulis beberapa angka. Siswa menyadari pentingnya loop. Siswa menyimak TP. | Proyektor, papan tulis |
| **MINING FULL** | **Eksplorasi** — Sesi 1** | 15' | Guru menjelaskan for loop: for i in range(n) — analogi "antrian tiket: untuk setiap orang, lakukan X". Guru menjelaskan variasi range(start, stop, step). Guru memberikan contoh mencetak bilangan genap 2-20. | Siswa menyimak dan mencatat. Siswa menulis kode for loop pertama mereka. Siswa mencoba mengubah parameter range. | Python IDLE/Colab, slide materi |
| **MINING FULL** | **Eksplorasi** — Sesi 2** | 15' | Guru menjelaskan while loop: while kondisi — analogi "isi galon sampai penuh". Guru menjelaskan risiko infinite loop dan cara menghindarinya. Guru demonstrasi program hitung mundur 10-1. | Siswa menyimak dan menulis kode while loop. Siswa sengaja membuat infinite loop lalu menghentikannya untuk memahami konsep. | Python IDLE/Colab, slide |
| **MINING FULL** | **Eksplorasi** — Praktik 1** | 15' | Guru memberikan 3 tantangan for loop: (1) deret 1-n, (2) tabel perkalian 1-10, (3) jumlah deret 1+2+...+n. Guru berkeliling membantu. | Siswa menyelesaikan 3 tantangan for loop secara individu. Siswa menguji dengan berbagai nilai n. | LKPD, Python IDLE/Colab |
| **MINING FULL** | **Eksplorasi** — Praktik 2** | 20' | Guru memberikan tantangan while loop: program tebak angka (komputer punya angka rahasia 1-100, user menebak sampai benar dengan petunjuk "lebih besar" atau "lebih kecil"). Guru memfasilitasi kompetisi. | Siswa membuat program tebak angka. Siswa saling mencoba program teman. Siswa yang selesai pertama mendapat apresiasi. | LKPD, Python IDLE/Colab |
| **MINING FULL** | **Eksplorasi** — Nested Loop** | 10' | Guru menjelaskan nested loop dengan contoh pola bintang segitiga. Guru menunjukkan bagaimana outer loop mengontrol baris dan inner loop mengontrol kolom. | Siswa menulis nested loop untuk pola bintang. Siswa bereksperimen dengan pola berbeda (segitiga siku, segitiga sama sisi, persegi). | Python IDLE/Colab, papan tulis |
| **JOYFULL** | **Penutup Kreatif** | 15' | Guru memberikan tugas: program mencetak bilangan prima dari 1-100 menggunakan loop. Guru menyimpulkan perbedaan for dan while. Guru menutup kelas. | Siswa mencatat tugas. Siswa membuat mindmap perbedaan for dan while. Siswa berdoa. | Papan tulis, buku catatan |

### D. ASESMEN

#### D.1 Asesmen Diagnostik (Awal)
| Pertanyaan | Tujuan |
|---|---|
| Apa yang dimaksud dengan iterasi? | Mengetahui pemahaman awal tentang konsep pengulangan |
| Bagaimana cara menulis angka 1 sampai 10 tanpa mengetik satu per satu? | Mengukur kemampuan berpikir efisien |
| Sebutkan contoh perulangan dalam kehidupan sehari-hari! | Mengidentifikasi kemampuan analogi siswa |

#### D.2 Asesmen Formatif (Proses)
- Observasi: guru memantau progress praktik 1, 2, dan nested loop.
- Hasil program tebak angka: apakah program berjalan tanpa infinite loop?
- Kuis singkat: perbedaan for dan while dengan contoh.

#### D.3 Asesmen Sumatif (Akhir)
- Produk: minimal 3 program Python (for, while, nested loop).
- Tugas rumah: program bilangan prima 1-100.

#### D.4 Rubrik Penilaian Program Perulangan
| Aspek | SB (4) | B (3) | C (2) | PB (1) |
|---|---|---|---|---|---|
| **Penggunaan for loop** | Menggunakan for loop dengan range() yang tepat, variasi step, dan manipulasi string/number | For loop berfungsi dengan range() dasar | For loop berfungsi tetapi ada error minor | Tidak menggunakan atau for loop error |
| **Penggunaan while loop** | While loop memiliki kondisi berhenti yang jelas, tidak ada infinite loop, menggunakan break/continue dengan tepat | While loop berfungsi dengan kondisi sederhana | While loop berfungsi tetapi ada risiko infinite loop | Tidak menggunakan atau while loop error |
| **Nested loop** | Pola bintang sempurna dengan input dinamis, bisa membuat 2+ variasi pola | Pola bintang berfungsi dengan input statis | Nested loop berfungsi tetapi pola tidak sesuai | Tidak berhasil membuat nested loop |
| **Logika dan efisiensi** | Kode efisien, tidak ada pengulangan yang tidak perlu, mudah dibaca | Kode cukup efisien dengan sedikit redundansi | Kode berjalan tetapi boros iterasi | Kode tidak efisien atau tidak berfungsi |

#### D.5 Contoh Soal
**Soal:** Buatlah program Python yang menerima input n (bilangan bulat positif) dan menampilkan:
- Deret bilangan genap dari 2 sampai n (menggunakan for)
- Faktorial dari n (menggunakan while)
- Pola bintang segitiga siku-siku dengan n baris (menggunakan nested loop)

### E. LEMBAR KERJA PESERTA DIDIK (LKPD)

**Nama:** __________________________ **Kelas:** X ___

#### E.1 Tantangan For Loop (Mudah)
```python
# Tantangan 1: Deret 1 sampai n
n = int(input("Masukkan n: "))
for i in range(1, n + 1):
    print(i, end=" ")
```
**Soal:** Modifikasi kode di atas untuk mencetak hanya bilangan ganjil dari 1 sampai n!

```python
# Tantangan 2: Tabel Perkalian 1-10
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")
    print("---")
```

#### E.2 Program Tebak Angka (Sedang)
```python
import random

# Program Tebak Angka
angka_rahasia = random.randint(1, 100)
tebakan = 0
percobaan = 0

print("Saya punya angka rahasia antara 1-100. Tebak!")

while tebakan != angka_rahasia:
    tebakan = int(input("Masukkan tebakan Anda: "))
    percobaan += 1

    if tebakan < angka_rahasia:
        print("Lebih besar!")
    elif tebakan > angka_rahasia:
        print("Lebih kecil!")
    else:
        print(f"Selamat! Anda menebak dalam {percobaan} percobaan.")
```

**Tugas Pengembangan:**
1. Tambahkan batas maksimal percobaan (misal 7 kali)
2. Jika percobaan habis, tampilkan angka rahasia dan pesan "Game Over"
3. Simpan riwayat tebakan dalam sebuah list dan tampilkan saat game selesai

#### E.3 Pola Bintang Nested Loop (Sulit)
```python
# Pola segitiga siku-siku
n = int(input("Masukkan jumlah baris: "))
for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()
```

**Tantangan:** Buatlah pola berikut menggunakan nested loop:
```
    *
   **
  ***
 ****
*****
```
*(segitiga siku rata kanan)*

**Tantangan Tambahan:** Buat pola belah ketupat (diamond) dengan input n baris!

#### E.4 Program Bilangan Prima (Tugas)
Buat program yang mencetak semua bilangan prima dari 1 sampai 100. Petunjuk: gunakan nested loop — loop luar untuk iterasi angka, loop dalam untuk mengecek faktor pembagi.

### F. DIFERENSIASI PEMBELAJARAN

| Level | Deskripsi |
|---|---|
| **Level 1 (Bimbingan)** | Siswa diberikan kode jadi dan diminta mengubah nilai parameter (n, step, kondisi) untuk mengamati perubahan output. Guru mendampingi step-by-step. Template kode disediakan dengan komentar petunjuk. |
| **Level 2 (Reguler)** | Siswa menyelesaikan seluruh LKPD secara mandiri. Siswa menulis kode dari awal. Siswa diminta menambahkan minimal 1 fitur pengembangan pada program tebak angka. |
| **Level 3 (Percepatan)** | Siswa menyelesaikan semua tantangan plus membuat program "simulasi ATM" (tarik tunai: while loop untuk menu berulang, for loop untuk mencetak struk, nested if untuk validasi PIN). Siswa juga mempelajari list comprehension sebagai alternatif loop. |

### G. REFLEKSI GURU

| Aspek Refleksi | Catatan |
|---|---|
| Apakah siswa dapat membedakan kapan menggunakan for vs while? | |
| Apakah ada siswa yang mengalami infinite loop dan bagaimana penanganannya? | |
| Apakah tantangan pola bintang cukup menantang untuk level reguler? | |
| Bagian mana yang memerlukan pengulangan penjelasan di pertemuan berikutnya? | |

### H. BAHAN BACAAN UNTUK GURU

- **Buku Informatika Kelas X, Bab 7** — Penerbit Kemdikbudristek
- **Python Official Documentation — More Control Flow Tools (for, while, break, continue)** — https://docs.python.org/3/tutorial/controlflow.html
- **"Automate the Boring Stuff with Python" oleh Al Sweigart** — Bab 2 (Flow Control) — sumber praktis untuk pengajaran loop
- **GeeksforGeeks Python Loops** — https://www.geeksforgeeks.org/loops-in-python/
- **Python Tutor (Loop Visualization)** — https://pythontutor.com/ — alat bantu visual untuk menunjukkan iterasi loop step-by-step kepada siswa

---


---

### G. REFLEKSI PEMBELAJARAN (DEEP LEARNING + 7 KAIH)

#### Refleksi Guru:
| Aspek | Catatan |
|-------|---------|
| Apakah pendekatan Mindful \u2192 Mining \u2192 Joyful berjalan efektif? | |
| Apakah siswa aktif berpartisipasi? | |
| Apakah integrasi 7 KAIH terlaksana? | |
| Apa yang perlu diperbaiki? | |
| Tindak lanjut: remedial/pengayaan? | |

#### Refleksi Siswa:
| Pertanyaan | Jawaban |
|------------|---------|
| **Mindful:** Apa yang aku pelajari hari ini? | |
| **Meaningful:** Bagaimana ini berguna untuk kehidupanku? | |
| **Joyful:** Hal paling menyenangkan dari pembelajaran hari ini? | |
| **7 KAIH:** Kebiasaan baik apa yang aku praktikkan hari ini? | |
| **Dimensi:** Dimensi Profil Lulusan mana yang terasah? | |


---

### G. REFLEKSI PEMBELAJARAN (DEEP LEARNING + 7 KAIH)

#### Refleksi Guru:
| Aspek | Catatan |
|-------|---------|
| Apakah pendekatan Mindful \u2192 Mining \u2192 Joyful berjalan efektif? | |
| Apakah siswa aktif berpartisipasi? | |
| Apakah integrasi 7 KAIH terlaksana? | |
| Apa yang perlu diperbaiki? | |
| Tindak lanjut: remedial/pengayaan? | |

#### Refleksi Siswa:
| Pertanyaan | Jawaban |
|------------|---------|
| **Mindful:** Apa yang aku pelajari hari ini? | |
| **Meaningful:** Bagaimana ini berguna untuk kehidupanku? | |
| **Joyful:** Hal paling menyenangkan dari pembelajaran hari ini? | |
| **7 KAIH:** Kebiasaan baik apa yang aku praktikkan hari ini? | |
| **Dimensi:** Dimensi Profil Lulusan mana yang terasah? | |

Mengetahui,  
Kepala Sekolah

_________________________

Guru Mata Pelajaran,

Daniarsyah, S.Kom.
NIP. 198004052022211004
