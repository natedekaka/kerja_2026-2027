# MODUL AJAR INFORMATIKA KELAS X

## AP: FUNGSI DAN PROSEDUR DALAM PYTHON

---

### A. INFORMASI UMUM

| Komponen | Deskripsi |
|---|---|
| Satuan Pendidikan | SMA Negeri 6 Cimahi |
| Mata Pelajaran | Informatika |
| Kelas / Fase | X (Sepuluh) / Fase E |
| Elemen | AP — Algoritma & Pemrograman |
| Tujuan Pembelajaran | TP.7.5: Membuat fungsi untuk program modular |
| Alokasi Waktu | 2 JP (2 × 45 menit) |
| Pertemuan ke- | 4 (empat) |
| Kompetensi Awal | Peserta didik telah memahami variabel, tipe data, percabangan (if-elif-else), dan perulangan (for, while) dalam Python |
| Integrasi 8 Dimensi | Kreativitas, Kemandirian, Penalaran Kritis |
| **Integrasi 7 KAIH** | Gemar Belajar, Bangun Pagi |
| **Pendekatan Deep Learning** | Mindful → Mining → Joyful |
| Sarana & Prasarana | Proyektor/LCD, laptop/komputer, Python IDLE atau Google Colab, papan tulis, spidol, koneksi internet |
| Target Peserta Didik | Reguler (dengan diferensiasi untuk peserta didik yang membutuhkan bimbingan dan percepatan) |
| Model Pembelajaran | Demonstrasi interaktif, praktik coding modular, dan code review |
| Metode | Demonstrasi, praktik mandiri, diskusi, penugasan, studi kasus |
| Sumber Belajar | Buku Informatika Kelas X Bab 7, dokumentasi Python — Functions, W3Schools Python Functions, modul ajar guru |

### B. TUJUAN PEMBELAJARAN
### B.1 PEMAHAMAN BERMAKNA (MEANINGFUL)
Pemrograman adalah cara kita 'berbicara' dengan komputer dan menciptakan solusi digital untuk masalah nyata.


### B.2 PERTANYAAN PEMANTIK (MINDFUL)
1. Apa yang akan terjadi jika...?
2. Bagaimana konsep ini terhubung dengan kehidupan sehari-harimu?
3. Mengapa materi ini penting untuk dipelajari?

#### B.1 Tujuan Pembelajaran
1. Menjelaskan konsep fungsi sebagai blok kode yang dapat digunakan kembali (reusable) dalam pemrograman modular.
2. Mendefinisikan fungsi sendiri (user-defined function) menggunakan keyword def dengan parameter dan return value yang tepat.
3. Membedakan variabel lokal dan global serta memahami ruang lingkupnya dalam fungsi.
4. Membuat program modular yang terdiri dari beberapa fungsi dengan pemanggilan yang terstruktur.
5. Mengaplikasikan fungsi pada studi kasus kalkulator modular dan konversi suhu.

#### B.2 Indikator Keberhasilan
| Indikator | Kriteria |
|---|---|
| 1. Menjelaskan fungsi | Mampu mendefinisikan fungsi dan menyebutkan 3 keuntungan program modular |
| 2. Mendefinisikan fungsi | Fungsi memiliki sintaks yang benar (def, parameter, return, docstring) |
| 3. Ruang lingkup | Mampu membedakan output kode dengan variabel lokal vs global |
| 4. Program modular | Program terdiri dari minimal 4 fungsi yang dipanggil dari menu utama |
| 5. Studi kasus | Fungsi konversi suhu berjalan benar untuk minimal 3 jenis konversi |

#### B.3 Kata Kunci
Fungsi, prosedur, def, parameter, argumen, return value, variabel lokal, variabel global, scope, modular, reusable, docstring, function call, positional argument, keyword argument

### C. KEGIATAN PEMBELAJARAN

| **Fase DL** | **Tahap** | **Waktu** | **Aktivitas Guru** | **Aktivitas Siswa** | **Media/Sumber** |
|---|---|---|---|---|---|
| **MINDFULL** | **Pemanasan** | 10' | Guru membuka kelas dan memantik: "Bayangkan menulis kalkulator — semua kode di satu blok panjang. Ribet kalau error atau mau dipakai ulang. Fungsi solusinya!" Guru menyampaikan TP. | Siswa merespons dan memberikan pendapat tentang pentingnya kode rapi. Siswa menyimak TP. | Proyektor, slide pembuka |
| **MINING FULL** | **Eksplorasi** — Sesi 1** | 20' | Guru menjelaskan konsep fungsi: def nama_fungsi(parameter): — definisi, parameter, return value, scope variabel (lokal vs global). Guru mendemonstrasikan fungsi luas_persegi(panjang, lebar) dan memanggilnya berulang dengan nilai berbeda. | Siswa menyimak dan mencatat. Siswa menulis fungsi sederhana. Siswa bereksperimen memanggil fungsi dengan argumen berbeda. | Python IDLE/Colab, slide fungsi |
| **MINING FULL** | **Eksplorasi** — Sesi 2** | 10' | Guru melakukan demo: fungsi menghitung luas lingkaran, segitiga, dan persegi. Guru menunjukkan penggunaan docstring dan return. Guru menjelaskan perbedaan fungsi yang mengembalikan nilai vs prosedur yang hanya mencetak. | Siswa menulis kode bersama guru. Siswa mencoba memanggil fungsi tanpa return dan mengamati hasil None. | Python IDLE/Colab |
| **MINING FULL** | **Eksplorasi** — Praktik 1** | 20' | Guru memberikan tugas: buat fungsi hitung_luas_lingkaran(r), hitung_luas_segitiga(a,t), hitung_luas_persegi(s). Panggil semua dalam program utama dengan input dari user. Guru berkeliling membantu. | Siswa membuat 3 fungsi luas bangun datar. Siswa menulis program utama yang memanggil ketiga fungsi. Siswa menguji dengan berbagai input. | LKPD, Python IDLE/Colab |
| **MINING FULL** | **Eksplorasi** — Praktik 2** | 15' | Guru memberikan studi kasus kalkulator modular: setiap operasi jadi fungsi sendiri (tambah(), kurang(), kali(), bagi()) → menu memanggil fungsi sesuai pilihan. Guru menekankan pentingnya fungsi bagi() yang menangani pembagian nol. | Siswa membuat program kalkulator modular. Setiap operasi ditulis sebagai fungsi terpisah. Program utama hanya berisi menu dan pemanggilan fungsi. | LKPD, Python IDLE/Colab |
| **JOYFULL** | **Penutup Kreatif** | 15' | Guru melakukan refleksi: "Apa keuntungan program modular?" Guru memberikan tugas: buat program konversi suhu (C→F, C→K, F→C, F→K, K→C, K→F) dengan fungsi. Guru menutup kelas. | Siswa menjawab pertanyaan refleksi. Siswa mencatat tugas. Siswa menyimpulkan manfaat fungsi. Siswa berdoa. | Papan tulis, buku catatan |

### D. ASESMEN

#### D.1 Asesmen Diagnostik (Awal)
| Pertanyaan | Tujuan |
|---|---|
| Apa yang dimaksud dengan kode yang "reusable"? | Mengukur pemahaman awal tentang efisiensi kode |
| Apa kelebihan menulis kode yang terpecah menjadi bagian-bagian kecil? | Mengetahui kesadaran siswa tentang modularitas |
| Sebutkan fungsi bawaan Python yang sudah kalian ketahui! | Mengidentifikasi familiaritas siswa dengan konsep fungsi |

#### D.2 Asesmen Formatif (Proses)
- Observasi: siswa yang berhasil mendefinisikan fungsi dengan sintaks benar pada percobaan pertama.
- Cek hasil praktik 1: apakah fungsi memiliki return value?
- Review kode kalkulator modular: apakah setiap operasi dipisah dalam fungsi?

#### D.3 Asesmen Sumatif (Akhir)
- Produk: kode Python dengan minimal 4 fungsi (praktik 2).
- Tugas rumah: program konversi suhu dengan 6 fungsi konversi.

#### D.4 Rubrik Penilaian Program Modular
| Aspek | SB (4) | B (3) | C (2) | PB (1) |
|---|---|---|---|---|---|
| **Definisi fungsi** | Semua fungsi memiliki definisi lengkap (def, parameter, return, docstring) | Fungsi memiliki parameter dan return, tanpa docstring | Fungsi didefinisikan tetapi ada parameter yang tidak digunakan | Fungsi tidak didefinisikan dengan benar atau tidak ada |
| **Penggunaan return** | Semua fungsi mengembalikan nilai (return) yang digunakan oleh pemanggil | Sebagian besar fungsi menggunakan return | Hanya 1-2 fungsi yang menggunakan return | Tidak ada fungsi yang menggunakan return |
| **Modularitas** | Program terstruktur dengan fungsi-fungsi independen yang dapat dipanggil ulang | Fungsi-fungsi cukup independen dengan sedikit ketergantungan | Fungsi masih tercampur dengan kode utama | Semua kode dalam satu blok tanpa fungsi |
| **Penanganan error** | Fungsi menangani input tidak valid dengan try-except atau kondisional | Menangani beberapa kasus error | Hanya menangani 1 jenis error | Tidak ada penanganan error |

#### D.5 Contoh Soal
**Soal:** Buatlah program Python yang terdiri dari fungsi-fungsi berikut:
1. fungsi is_palindrom(kata) — mengembalikan True jika kata adalah palindrom (kasus: "radar", "makan")
2. fungsi balik_kata(kata) — mengembalikan kata yang dibalik
3. fungsi hitung_vokal(kata) — mengembalikan jumlah huruf vokal dalam kata

Program utama meminta input kalimat dari user dan menampilkan hasil ketiga fungsi tersebut.

### E. LEMBAR KERJA PESERTA DIDIK (LKPD)

**Nama:** __________________________ **Kelas:** X ___

#### E.1 Praktik 1 — Fungsi Luas Bangun Datar (Mudah)
```python
# Fungsi menghitung luas lingkaran
def luas_lingkaran(r):
    """Menghitung luas lingkaran dengan jari-jari r"""
    phi = 3.14
    return phi * r * r

# Fungsi menghitung luas segitiga
def luas_segitiga(a, t):
    """Menghitung luas segitiga dengan alas a dan tinggi t"""
    return 0.5 * a * t

# Fungsi menghitung luas persegi
def luas_persegi(s):
    """Menghitung luas persegi dengan sisi s"""
    return s * s

# Program utama
print("=== PROGRAM LUAS BANGUN DATAR ===")
print("1. Luas Lingkaran")
print("2. Luas Segitiga")
print("3. Luas Persegi")
pilihan = int(input("Pilih bangun (1-3): "))

if pilihan == 1:
    r = float(input("Masukkan jari-jari: "))
    print(f"Luas lingkaran = {luas_lingkaran(r)}")
elif pilihan == 2:
    a = float(input("Masukkan alas: "))
    t = float(input("Masukkan tinggi: "))
    print(f"Luas segitiga = {luas_segitiga(a, t)}")
elif pilihan == 3:
    s = float(input("Masukkan sisi: "))
    print(f"Luas persegi = {luas_persegi(s)}")
else:
    print("Pilihan tidak valid")
```

**Tugas:**
1. Tambahkan fungsi luas_persegi_panjang(p, l)
2. Tambahkan validasi input (r, a, t, s harus > 0)
3. Gunakan perulangan while agar program bisa digunakan berulang kali

#### E.2 Kalkulator Modular (Sedang)
```python
# Fungsi-fungsi operasi
def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        return "Error: pembagian dengan nol"
    return a / b

# Program utama
print("=== KALKULATOR MODULAR ===")
while True:
    print("\n1. Tambah\n2. Kurang\n3. Kali\n4. Bagi\n5. Keluar")
    pilih = int(input("Pilih (1-5): "))
    if pilih == 5:
        break
    a = float(input("Angka pertama: "))
    b = float(input("Angka kedua: "))

    if pilih == 1:
        print(f"Hasil: {tambah(a, b)}")
    elif pilih == 2:
        print(f"Hasil: {kurang(a, b)}")
    elif pilih == 3:
        print(f"Hasil: {kali(a, b)}")
    elif pilih == 4:
        print(f"Hasil: {bagi(a, b)}")
    else:
        print("Pilihan tidak valid")
```

**Pertanyaan Refleksi:**
1. Apa keuntungan memisahkan setiap operasi ke dalam fungsi sendiri?
2. Bagaimana jika suatu saat kita ingin menambahkan operasi modulo (%)? Cukup dengan menambah fungsi baru tanpa mengubah kode yang sudah ada — inilah keunggulan modularitas.

#### E.3 Studi Kasus Konversi Suhu (Sulit — Tugas)
Buatlah program konversi suhu dengan fungsi-fungsi berikut:
1. celcius_to_fahrenheit(c)
2. celcius_to_kelvin(c)
3. fahrenheit_to_celsius(f)
4. fahrenheit_to_kelvin(f)
5. kelvin_to_celsius(k)
6. kelvin_to_fahrenheit(k)

Program utama menampilkan menu konversi dan memanggil fungsi yang sesuai.

### F. DIFERENSIASI PEMBELAJARAN

| Level | Deskripsi |
|---|---|
| **Level 1 (Bimbingan)** | Siswa diberikan template fungsi yang sudah lengkap dan diminta hanya mengubah bagian return. Siswa fokus pada pemanggilan fungsi (function call) terlebih dahulu sebelum mendefinisikan fungsi sendiri. |
| **Level 2 (Reguler)** | Siswa menulis fungsi dari awal sesuai spesifikasi. Siswa menyelesaikan praktik 1 dan 2. Siswa diminta menambahkan docstring pada setiap fungsi. |
| **Level 3 (Percepatan)** | Siswa menyelesaikan semua soal plus membuat program "manajemen data siswa modular" yang terdiri dari fungsi: tambah_siswa(), tampilkan_siswa(), cari_siswa(), hapus_siswa(), hitung_rata_rata(). Data disimpan dalam list of dictionary. |
