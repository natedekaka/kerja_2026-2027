# MODUL AJAR INFORMATIKA KELAS X

## AP: DEBUGGING DAN PENGUJIAN PROGRAM

---

### A. INFORMASI UMUM

| Komponen | Deskripsi |
|---|---|
| Satuan Pendidikan | SMA Negeri 6 Cimahi |
| Mata Pelajaran | Informatika |
| Kelas / Fase | X (Sepuluh) / Fase E |
| Elemen | AP — Algoritma & Pemrograman |
| Tujuan Pembelajaran | TP.7.6: Debugging & error handling |
| Alokasi Waktu | 2 JP (2 × 45 menit) |
| Pertemuan ke- | 5 (lima) |
| Kompetensi Awal | Peserta didik telah mampu menulis program Python dengan variabel, percabangan, perulangan, dan fungsi |
| Integrasi 8 Dimensi | Kemandirian, Penalaran Kritis, Kreativitas |
| **Integrasi 7 KAIH** | Gemar Belajar, Bangun Pagi |
| **Pendekatan Deep Learning** | Mindful → Mining → Joyful |
| Sarana & Prasarana | Proyektor/LCD, laptop/komputer, Python IDLE atau Google Colab, papan tulis, kertas soal error, timer untuk lomba debugging |
| Target Peserta Didik | Reguler (dengan diferensiasi untuk peserta didik yang membutuhkan bimbingan dan percepatan) |
| Model Pembelajaran | Problem Based Learning, Gamification (Lomba Debugging) |
| Metode | Demonstrasi, studi kasus, problem solving, kompetisi, diskusi, praktik mandiri |
| Sumber Belajar | Buku Informatika Kelas X Bab 7, dokumentasi Python — Errors and Exceptions, Python Tutor, modul ajar guru |

### B. TUJUAN PEMBELAJARAN
### B.1 PEMAHAMAN BERMAKNA (MEANINGFUL)
Pemrograman adalah cara kita 'berbicara' dengan komputer dan menciptakan solusi digital untuk masalah nyata.


### B.2 PERTANYAAN PEMANTIK (MINDFUL)
1. Apa yang akan terjadi jika...?
2. Bagaimana konsep ini terhubung dengan kehidupan sehari-harimu?
3. Mengapa materi ini penting untuk dipelajari?

#### B.1 Tujuan Pembelajaran
1. Mengidentifikasi dan membedakan jenis-jenis error dalam Python: SyntaxError, NameError, TypeError, ValueError, IndexError, ZeroDivisionError, dan LogicError.
2. Membaca dan memahami pesan error (traceback) yang ditampilkan Python untuk menemukan lokasi dan jenis error.
3. Menerapkan teknik debugging sistematis: membaca error message, melacak variabel, dan mengisolasi blok kode yang bermasalah.
4. Menggunakan struktur try-except-finally untuk menangani error agar program tetap berjalan (error handling).
5. Menguji program dengan berbagai skenario input termasuk kasus batas (edge case) untuk memvalidasi kebenaran program.

#### B.2 Indikator Keberhasilan
| Indikator | Kriteria |
|---|---|
| 1. Mengidentifikasi error | Mampu menyebutkan minimal 5 jenis error Python dengan contoh masing-masing |
| 2. Membaca traceback | Mampu menentukan baris error dan jenis error dari pesan traceback dalam 2 menit |
| 3. Debugging | Menemukan dan memperbaiki 5 dari 5 error dalam kode yang diberikan dalam 15 menit |
| 4. Error handling | Program menggunakan try-except untuk menangani minimal 3 jenis error berbeda |
| 5. Pengujian | Menguji program dengan 3 skenario: input normal, input batas, input error |

#### B.3 Kata Kunci
Debugging, error handling, SyntaxError, NameError, TypeError, ValueError, IndexError, ZeroDivisionError, LogicError, traceback, exception, try, except, finally, raise, bug, testing, edge case

### C. KEGIATAN PEMBELAJARAN

| **Fase DL** | **Tahap** | **Waktu** | **Aktivitas Guru** | **Aktivitas Siswa** | **Media/Sumber** |
|---|---|---|---|---|---|
| **MINDFULL** | **Pemanasan** | 10' | Guru membuka kelas, mengecek kehadiran. Guru memantik: "Program tidak pernah benar di percobaan pertama. Debugging adalah skill paling penting seorang programmer!" Guru menyampaikan TP. | Siswa merespons. Siswa berbagi pengalaman pernah mengalami error saat coding. Siswa menyimak TP. | Proyektor, slide pembuka |
| **MINING FULL** | **Eksplorasi** — Sesi 1** | 20' | Guru menjelaskan 7 jenis error Python dengan contoh kode langsung: SyntaxError (lupa titik dua), NameError (variabel belum didefinisikan), TypeError (operasi tipe beda), ValueError (input salah), IndexError (indeks di luar range), ZeroDivisionError (pembagian nol), LogicError (program jalan tapi hasil salah). | Siswa menulis setiap contoh error di komputer. Siswa mengamati pesan error yang muncul. Siswa mencatat ciri-ciri setiap jenis error. | Python IDLE/Colab, slide 7 jenis error |
| **MINING FULL** | **Eksplorasi** — Sesi 2** | 10' | Guru mengajarkan cara membaca error message (traceback): "Error message adalah teman, bukan musuh." Guru menunjukkan bagaimana traceback menunjukkan file, baris, dan jenis error. | Siswa membaca traceback dan mengidentifikasi informasi penting (file, line number, exception type, error message). | Proyektor, kode error |
| **MINING FULL** | **Eksplorasi** — Praktik 1** | 20' | Guru memberikan kode yang mengandung 5 error. Siswa mencari dan memperbaiki satu per satu. Guru berkeliling memberikan petunjuk tanpa memberi jawaban langsung. | Siswa mengidentifikasi dan memperbaiki setiap error. Siswa menuliskan jenis error dan perbaikannya di LKPD. | LKPD soal error, Python IDLE/Colab |
| **MINING FULL** | **Eksplorasi** — Praktik 2** | 15' | Guru menjelaskan try-except-finally: program tetap jalan meskipun error. Guru memberi contoh program pembagian dengan try-except ZeroDivisionError dan ValueError. | Siswa menulis program dengan try-except. Siswa menguji program dengan input normal dan error. | Python IDLE/Colab, slide try-except |
| **MINING FULL** | **Eksplorasi** — Lomba Debugging** | 10' | Guru memberikan 3 kode error secara bertahap. Siapa paling cepat perbaiki semua error? Guru memfasilitasi dan memberikan apresiasi. | Siswa berlomba memperbaiki error. Siswa pertama yang selesai mendapat apresiasi. | Soal lomba di proyektor |
| **JOYFULL** | **Penutup Kreatif** | 15' | Guru memberikan tugas: buat program sendiri lalu "tanamkan" 3 error — tukar dengan teman untuk diperbaiki. Guru menyimpulkan jenis-jenis error dan pentingnya debugging. | Siswa mencatat tugas. Siswa membuat kesimpulan tentang debugging. Siswa berdoa. | Papan tulis, buku catatan |

### D. ASESMEN

#### D.1 Asesmen Diagnostik (Awal)
| Pertanyaan | Tujuan |
|---|---|
| Apa yang terjadi saat program Python mengalami error? | Mengetahui pengalaman siswa dengan error |
| Bagaimana reaksi kalian saat muncul error merah? | Mengukur sikap siswa terhadap error |
| Sebutkan error yang paling sering kalian temui saat coding! | Mengidentifikasi pengalaman debugging siswa |

#### D.2 Asesmen Formatif (Proses)
- Hasil identifikasi error pada praktik 1 (5 error).
- Kecepatan dan ketepatan dalam lomba debugging.
- Program try-except: apakah menangani minimal 2 jenis error.

#### D.3 Asesmen Sumatif (Akhir)
- Produk: kode hasil debugging + program dengan try-except (praktik 2).
- Tugas: program dengan 3 error yang ditanam (beserta kunci jawaban).

#### D.4 Rubrik Penilaian Debugging dan Error Handling
| Aspek | SB (4) | B (3) | C (2) | PB (1) |
|---|---|---|---|---|---|
| **Identifikasi error** | Mengidentifikasi semua jenis error dengan tepat beserta penyebabnya | Mengidentifikasi 4 dari 5 error dengan tepat | Mengidentifikasi 3 dari 5 error | Mengidentifikasi kurang dari 3 error |
| **Perbaikan error** | Semua error diperbaiki dengan solusi yang tepat dan efisien | 4 error diperbaiki dengan benar | 3 error diperbaiki dengan benar | Kurang dari 3 error diperbaiki |
| **Error handling (try-except)** | Menggunakan try-except untuk 3+ jenis error, ada finally, dan pesan error informatif | Try-except untuk 2 jenis error | Try-except hanya untuk 1 jenis error | Tidak menggunakan try-except |
| **Pengujian program** | Menguji dengan 3+ skenario (normal, batas, error) dan mencatat semua hasil | Menguji dengan 2 skenario | Menguji hanya dengan skenario normal | Tidak melakukan pengujian |

#### D.5 Contoh Soal
**Soal:** Berikut adalah kode Python yang memiliki 4 error. Identifikasi jenis error, lokasi (baris), dan tuliskan perbaikannya!

```python
# Program menghitung rata-rata
jumlah = 0
data = [85, 90, 78, "92", 88]
for i in range(len(data)):
    jumlah = jumlah + data[i]
rata_rata = jumlah / len(data
print("Rata-rata:", rata-rata)
```

### E. LEMBAR KERJA PESERTA DIDIK (LKPD)

**Nama:** __________________________ **Kelas:** X ___

#### E.1 Praktik 1 — Cari dan Perbaiki 5 Error! (Mudah)
Kode berikut mengandung 5 error. Identifikasi jenis error, baris, dan perbaikannya!

```python
# Program menghitung diskon
print("Program Diskon Belanja")

total = input("Masukkan total belanja: ")
if total > 100000:
    diskon = total * 0.1
    print("Anda mendapat diskon 10%")
elif total > 50000
    diskon = total * 0.05
    print("Anda mendapat diskon 5%")
else
    diskon = 0
print(f"Total yang dibayar: {total - diskon}")
```

**Tabel Identifikasi Error:**
| No | Baris | Jenis Error | Perbaikan |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |

#### E.2 Praktik 2 — Error Handling dengan try-except (Sedang)
```python
# Program pembagian dengan error handling
def bagi_angka():
    while True:
        try:
            a = float(input("Masukkan pembilang: "))
            b = float(input("Masukkan penyebut: "))
            hasil = a / b
            print(f"Hasil: {a} / {b} = {hasil}")
            break
        except ZeroDivisionError:
            print("Error: Penyebut tidak boleh nol. Coba lagi!")
        except ValueError:
            print("Error: Input harus berupa angka. Coba lagi!")
        except KeyboardInterrupt:
            print("\nProgram dihentikan oleh user.")
            break

bagi_angka()
```

**Tugas Pengembangan:**
1. Tambahkan except untuk menangani OverflowError
2. Tambahkan blok finally yang mencetak "Program selesai dijalankan"
3. Buat versi kalkulator lengkap (+, -, *, /) yang menggunakan try-except di setiap operasi

#### E.3 Lomba Debugging — 3 Kode Error (Sulit)
**Soal 1:** Perbaiki program faktorial berikut:
```python
n = int(input("Masukkan n: "))
for i in range(1, n)
    faktorial *= i
print(f"Faktorial = {faktorial}")
```

**Soal 2:** Perbaiki program mencari nilai maksimum:
```python
angka = [12, 45, 7, 89, 23]
maks = 0
for i in range(len(angka))
    if angka[i] > maks
    maks = angka[1]
print("Nilai maks:", maks)
```

**Soal 3:** Perbaiki program menyapa pengguna:
```python
nama = input("Siapa nama Anda? ")
umur = input("Berapa umur Anda? ")
tahun_sekarang = 2026
tahun_lahir = tahun_sekarang - umur
print(f"Halo {nama}, kamu lahir tahun {tahun_lahir}")
```

### F. DIFERENSIASI PEMBELAJARAN

| Level | Deskripsi |
|---|---|
| **Level 1 (Bimbingan)** | Siswa diberikan kode error dengan petunjuk berupa komentar "ERROR DI SINI" atau tanda panah. Guru mendampingi siswa membaca pesan error dan melacak baris yang bermasalah. |
| **Level 2 (Reguler)** | Siswa mengerjakan seluruh LKPD secara mandiri. Siswa diharapkan dapat menyelesaikan praktik 1 dan 2 dalam waktu yang disediakan. |
| **Level 3 (Percepatan)** | Siswa menyelesaikan semua soal plus tantangan: membuat program "bank sederhana" (setor, tarik, cek saldo) yang dilengkapi error handling untuk saldo tidak mencukupi, input negatif, dan input non-angka. Siswa juga diminta menulis minimal 3 test case. |

### G. REFLEKSI GURU

| Aspek Refleksi | Catatan |
|---|---|
| Apakah siswa masih takut dengan pesan error merah setelah pembelajaran ini? | |
| Error jenis apa yang paling sulit diidentifikasi siswa? | |
| Apakah lomba debugging efektif meningkatkan motivasi siswa? | |
| Apakah siswa mampu menerapkan try-except pada program mereka sendiri? | |
