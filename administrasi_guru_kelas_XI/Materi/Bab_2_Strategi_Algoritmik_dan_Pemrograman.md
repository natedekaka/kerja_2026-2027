# ⚙️ Bab 2: Strategi Algoritmik dan Pemrograman

> **Semester Ganjil** | **Fase F** | **Kelas XI** | **36 JP**

---

## 📊 Pemetaan Capaian Pembelajaran

| Elemen CP | Deskripsi CP |
|-----------|-------------|
| Algoritma dan Pemrograman (AP) | Menerapkan strategi algoritmik (rekursi, greedy, pemrograman dinamis) dan membandingkan efisiensinya dalam pemrograman |

---

## 🎯 Tujuan Pembelajaran

- **A.** Dasar Pemrograman Python
- **B.** Proses Pemrograman & Efisiensi Algoritma
- **C.** Rekursi: Fungsi yang Memanggil Dirinya Sendiri
- **D.** Algoritma Greedy: Pilihan Terbaik Saat Ini
- **E.** Pemrograman Dinamis: Optimasi dengan Subproblem
- **F.** Array, String, dan Manipulasi Data
- **G.** Perbandingan Strategi Algoritmik

## 🗺️ Peta Konsep

```
               ⚙️ STRATEGI ALGORITMIK DAN PEMROGRAMAN
                     |
                     ├── A. Dasar Pemrograman Python
                     ├── B. Proses Pemrograman & Efisiensi Algoritma
                     ├── C. Rekursi: Fungsi yang Memanggil Dirinya Sendiri
                     ├── D. Algoritma Greedy: Pilihan Terbaik Saat Ini
                     ├── E. Pemrograman Dinamis: Optimasi dengan Subproblem
                     ├── F. Array, String, dan Manipulasi Data
                     └── G. Perbandingan Strategi Algoritmik
```

## A. Dasar Pemrograman Python

### 🐍 Mengenal Python

Python adalah bahasa pemrograman **level tinggi, interpretatif, dan serbaguna**. Python dipilih karena:

| Kelebihan | Penjelasan |
|-----------|------------|
| **Mudah dibaca** | Sintaks mirip bahasa Inggris, tidak perlu titik koma atau kurung kurawal |
| **Serbaguna** | Bisa untuk web, data sains, AI, game, dan otomatisasi |
| **Komunitas besar** | Banyak pustaka, tutorial, dan forum diskusi |
| **Edukasi** | Bahasa paling populer untuk belajar pemrograman di sekolah/universitas |

> 🔧 **Persiapan:** Install Python 3 dari [python.org](https://www.python.org/) atau gunakan editor online seperti [Replit](https://replit.com/), [Google Colab](https://colab.research.google.com/), atau VS Code dengan ekstensi Python.

---

### A.1 Variabel, Tipe Data, Input/Output

#### 📦 Variabel
Variabel adalah **tempat menyimpan data**. Python tidak perlu deklarasi tipe data — cukup tulis nama dan nilainya.

```python
nama = "Budi"        # String (teks)
umur = 17            # Integer (bilangan bulat)
tinggi = 165.5       # Float (bilangan desimal)
apakah_siswa = True  # Boolean (True/False)
```

> 💡 **Aturan Penamaan Variabel:** Gunakan huruf, angka, dan underscore. Diawali huruf/underscore. **Case-sensitive** (`nama` ≠ `Nama`).

#### 🔢 Tipe Data Dasar
| Tipe | Contoh | Keterangan |
|------|--------|------------|
| `int` | `17`, `2024`, `-5` | Bilangan bulat |
| `float` | `3.14`, `2.5` | Bilangan desimal |
| `str` | `"Halo"`, `'Informatika'` | Teks (pakai `"` atau `'`) |
| `bool` | `True`, `False` | Nilai kebenaran |

#### ⌨️ Input & Output
```python
# Output — menampilkan ke layar
print("Selamat datang di Python!")
print("Nama:", nama)
print(f"Umur saya {umur} tahun")       # f-string (format string)

# Input — membaca dari keyboard
nama_user = input("Siapa nama kamu? ")
print(f"Halo, {nama_user}! Senang bertemu!")
```

> ⚠️ `input()` selalu mengembalikan **string**! Kalau mau angka, konversi dulu: `angka = int(input("Masukkan angka: "))`

#### ✍️ Latihan Singkat A.1
1. Buat variabel untuk menyimpan nama, kelas, dan nilai favoritmu. Tampilkan dengan `print()`!
2. Minta pengguna memasukkan dua angka, lalu tampilkan hasil penjumlahan!

---

### A.2 Percabangan (if / elif / else)

#### 🚦 Logika Percabangan
Program bisa **mengambil keputusan** berdasarkan kondisi:

```python
nilai = 85

if nilai >= 75:
    print("Lulus! 🎉")
else:
    print("Remedial, semangat! 💪")
```

#### elif — Banyak Kondisi
```python
if nilai >= 90:
    predikat = "A (Sangat Baik)"
elif nilai >= 75:
    predikat = "B (Baik)"
elif nilai >= 60:
    predikat = "C (Cukup)"
else:
    predikat = "D (Perlu Bimbingan)"

print(f"Predikat: {predikat}")
```

#### 🔗 Operator Perbandingan & Logika
| Operator | Arti | Operator Logika | Arti |
|----------|------|-----------------|------|
| `==` | Sama dengan | `and` | Keduanya benar |
| `!=` | Tidak sama | `or` | Salah satu benar |
| `>` | Lebih besar | `not` | Membalikkan |
| `<` | Lebih kecil | | |
| `>=` | Lebih besar/sama | | |
| `<=` | Lebih kecil/sama | | |

```python
usia = 17
lulus = True

if usia >= 16 and lulus:
    print("Boleh ikut lomba coding!")
```

#### ✍️ Latihan Singkat A.2
Buat program yang menerima **nilai ujian** (0-100) dan menampilkan predikat: A (≥90), B (≥75), C (≥60), D (<60).

---

### A.3 Perulangan (for / while)

#### 🔄 Perulangan `for` — Jumlah Iterasi Pasti
```python
# Ulang 5 kali
for i in range(5):
    print(f"Perulangan ke-{i+1}")

# Iterasi list
buah = ["apel", "mangga", "pisang"]
for b in buah:
    print(f"Saya suka {b}")

# Range dengan awal dan akhir
for angka in range(1, 11):      # 1 sampai 10
    print(angka, end=" ")        # Output: 1 2 3 4 5 6 7 8 9 10
```

#### ♻️ Perulangan `while` — Selama Kondisi Terpenuhi
```python
tebak = ""
while tebak != "python":
    tebak = input("Tebak kata rahasia: ")
print("Benar! 🎉")
```

```python
# Contoh: Hitung mundur
hitungan = 5
while hitungan > 0:
    print(f"{hitungan}...")
    hitungan -= 1
print("Go! 🚀")
```

#### 🔧 break dan continue
```python
for i in range(10):
    if i == 5:
        break                # Berhenti saat i = 5
    if i % 2 == 0:
        continue             # Skip bilangan genap
    print(i)                 # Output: 1, 3
```

> 💡 **Kapan pakai yang mana?** Gunakan `for` kalau sudah tahu berapa kali ulang. Gunakan `while` kalau berulang **selama kondisi tertentu** (misal sampai user mengetik "exit").

#### ✍️ Latihan Singkat A.3
1. Cetak **tabel perkalian 5** (5×1 sampai 5×10) menggunakan `for`!
2. Buat program **tebak angka** (1-10) dengan `while` — beri petunjuk "terlalu besar" atau "terlalu kecil"!

---

### A.4 Fungsi (def)

#### 🧩 Mengapa Fungsi?
Fungsi adalah **blok kode yang bisa dipakai ulang**. Bayangkan fungsi seperti **resep masakan** — kita simpan resepnya, dan panggil kapan pun mau!

```python
def sapa(nama):
    """Fungsi untuk menyapa pengguna"""
    return f"Halo, {nama}! Selamat belajar Python!"

# Panggil fungsi
print(sapa("Budi"))     # Output: Halo, Budi! Selamat belajar Python!
print(sapa("Siti"))     # Output: Halo, Siti! Selamat belajar Python!
```

#### 📥 Parameter dan 📤 Return
```python
def luas_persegi(panjang, lebar):
    """Menghitung luas persegi panjang"""
    luas = panjang * lebar
    return luas

# Panggil
hasil = luas_persegi(5, 3)
print(f"Luas: {hasil}")     # Output: Luas: 15
```

#### 🏗️ Fungsi dengan Nilai Default
```python
def sapa_siswa(nama, kelas="XI"):
    return f"{nama} dari kelas {kelas}"

print(sapa_siswa("Budi"))           # Output: Budi dari kelas XI
print(sapa_siswa("Ani", "XII"))     # Output: Ani dari kelas XII
```

#### ✍️ Latihan Singkat A.4
1. Buat fungsi `cek_ganjil_genap(angka)` yang mengembalikan "Ganjil" atau "Genap"!
2. Buat fungsi `hitung_rata_rata(daftar_nilai)` yang menerima list angka dan mengembalikan rata-rata!

---

### A.5 Studi Kasus Mini: 📊 Kalkulator Nilai

Gabungkan semua konsep di atas dalam satu program!

```python
def hitung_nilai(uts, uas, tugas):
    """Menghitung nilai akhir"""
    return (uts * 0.3) + (uas * 0.4) + (tugas * 0.3)

def predikat(nilai):
    """Menentukan predikat berdasarkan nilai"""
    if nilai >= 90:
        return "A (Sangat Baik)"
    elif nilai >= 75:
        return "B (Baik)"
    elif nilai >= 60:
        return "C (Cukup)"
    else:
        return "D (Perlu Bimbingan)"

# Program utama
print("=== KALKULATOR NILAI ===")
nama = input("Nama siswa: ")
uts = float(input("Nilai UTS: "))
uas = float(input("Nilai UAS: "))
tugas = float(input("Nilai Tugas: "))

nilai_akhir = hitung_nilai(uts, uas, tugas)
print(f"\n{nama} — Nilai Akhir: {nilai_akhir:.1f}")
print(f"Predikat: {predikat(nilai_akhir)}")
```

> 🎯 **Output yang diharapkan:** Program menerima input, memproses dengan fungsi, dan menampilkan hasil dengan predikat.

---

### 🔍 Rangkuman A
| Konsep | Inti |
|--------|------|
| Variabel & Tipe Data | Wadah data: `int`, `float`, `str`, `bool` |
| Input/Output | `input()` untuk baca, `print()` dan f-string untuk tampil |
| Percabangan | `if/elif/else` — ambil keputusan |
| Perulangan | `for` (pasti), `while` (kondisi) |
| Fungsi | `def` — blok kode reusable |

> 🚀 **Selanjutnya:** Setelah menguasai dasar Python, kita siap mempelajari **strategi algoritmik** yang semuanya akan diimplementasikan dalam Python!

---

## B. Proses Pemrograman & Efisiensi Algoritma

### ⚙️ Proses Pemrograman & Efisiensi Algoritma

### 4 Tahap Pemrograman
```
  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐
  │ ANALISIS │   │ DESAIN   │   │ IMPLEMEN-│   │ PENGUJIAN│
  │ Masalah  │──►│ Algoritma│──►│ TASI     │──►│ & DEBUG  │
  │          │   │          │   │ (Coding) │   │          │
  └──────────┘   └──────────┘   └──────────┘   └────┬─────┘
                                                     │
                                                (loop back)
```

> 🧩 **Analogi:** Ini seperti **resep masakan**. Kamu analisis mau masak apa (analisis), tentukan bahan dan langkahnya (desain), masak (coding), lalu cicipi — kalau asin tambah gula (debug).

### Efisiensi Algoritma
Algoritma yang baik harus **efisien** — cepat dan tidak boros memori.

| Algoritma | Waktu untuk 1000 data | Waktu untuk 1 juta data |
|-----------|---------------------|------------------------|
| **Linear Search** | 0,001 detik | 1 detik |
| **Binary Search** | 0,00001 detik | 0,00001 detik |
| **Bubble Sort** | 0,001 detik | 1000 detik (~17 menit!) |
| **Merge Sort** | 0,0001 detik | 0,1 detik |

> 🔑 **Big O Notation** adalah cara mengukur efisiensi. O(1) = konstan (paling cepat), O(n) = linear, O(n²) = kuadratik (lambat untuk data besar).

### ✍️ Latihan
Mana yang lebih efisien untuk mencari nomor telepon di buku telepon dengan 10.000 nama?
- **Linear Search**: Cek satu per satu dari halaman pertama
- **Binary Search**: Buka halaman tengah, lalu cari di kiri/kanan

### 🔍 Cek Pemahaman
1. Sebutkan 4 tahap dalam proses pemrograman! Mengapa tahap analisis penting dilakukan pertama?
2. Apa perbedaan antara O(1), O(n), dan O(n²)? Berikan contoh algoritma untuk masing-masing!
3. Untuk data 1 juta item, mengapa Binary Search (O(log n)) jauh lebih cepat dari Linear Search (O(n))?

### 📋 Studi Kasus
Perpustakaan SMA Nusantara memiliki 10.000 buku. Selama ini, siswa mencari buku dengan cara melihat satu per satu rak. Seorang siswa bernama Dimas mengusulkan program pencarian buku digital agar lebih efisien.

**Analisis:**
1. Algoritma pencarian mana yang paling tepat untuk program yang diusulkan Dimas? Jelaskan alasannya!
2. Jika data buku bertambah menjadi 100.000, apakah pilihan algoritmamu masih tetap sama? Mengapa?

> 🤔 **Mari Renungkan:** Apa hal paling menarik yang kamu pelajari dari bagian ini?

---

## C. Rekursi: Fungsi yang Memanggil Dirinya Sendiri

### 🔄 Rekursi: Fungsi yang Memanggil Dirinya Sendiri
Rekursi adalah teknik di mana sebuah **fungsi memanggil dirinya sendiri** untuk menyelesaikan masalah.

> 🧩 **Analogi:** Rekursi itu seperti **cermin yang berhadapan dengan cermin lain** — kamu melihat pantulan yang terus berulang. Atau seperti **boneka Matryoshka Rusia** — di dalam boneka besar ada boneka lebih kecil, dan seterusnya.

### Struktur Rekursi
```python
def faktorial(n):
    # BASE CASE: kondisi berhenti
    if n <= 1:
        return 1
    # RECURSIVE CASE: panggil diri sendiri
    return n * faktorial(n - 1)

print(faktorial(5))  # Output: 120
```

### Cara Kerja
```
faktorial(5) = 5 × faktorial(4)
             = 5 × 4 × faktorial(3)
             = 5 × 4 × 3 × faktorial(2)
             = 5 × 4 × 3 × 2 × faktorial(1)
             = 5 × 4 × 3 × 2 × 1
             = 120
```

### Rekursi vs Iterasi
| Aspek | Rekursi | Iterasi (for/while) |
|-------|---------|---------------------|
| **Kode** | Lebih pendek, elegan | Lebih panjang |
| **Mudah dibaca** | Untuk masalah tertentu (pohon, fractal) | Untuk masalah umum |
| **Memori** | Lebih boros (stack) | Lebih hemat |
| **Kecepatan** | Agak lambat | Cepat |

### Contoh: Fibonacci
```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))  # Output: 55
```

> 💡 **Tips:** Selalu pastikan ada **base case** (kondisi berhenti) — kalau tidak, program akan error "stack overflow"!

### 🔍 Cek Pemahaman
1. Apa perbedaan antara base case dan recursive case dalam fungsi rekursif?
2. Mengapa rekursi Fibonacci tanpa DP sangat lambat untuk n = 50?
3. Kapan sebaiknya menggunakan rekursi dibandingkan iterasi? Berikan contoh masalah!

### 📋 Studi Kasus
Dalam pelajaran seni, Dimas mendapat tugas membuat gambar **pohon fractal** menggunakan prinsip rekursif. Setiap cabang pohon bercabang menjadi 2 cabang yang lebih kecil, dan seterusnya. Dimas ingin pohonnya memiliki kedalaman 5 tingkat (5 kali percabangan).

**Analisis:**
1. Gambarkan bagaimana pola rekursif bekerja pada pohon fractal tersebut! Berapa total cabang yang terbentuk?
2. Apa yang terjadi jika Dimas lupa memberikan base case (kedalaman 0) pada programnya?

> 🤔 **Mari Renungkan:** Apa hal paling menarik yang kamu pelajari dari bagian ini?

---

## D. Algoritma Greedy: Pilihan Terbaik Saat Ini

### 🎯 Algoritma Greedy: Pilihan Terbaik Saat Ini
Greedy = **rakus** = algoritma yang selalu mengambil pilihan **terbaik pada saat itu juga** (lokal optimal) dengan harapan menghasilkan solusi terbaik secara keseluruhan (global optimal).

> 🧩 **Analogi:** Greedy itu seperti **jalan-jalan ke pasar malam**. Kamu punya uang Rp50.000 dan harus memilih makanan terbaik. Kamu beli yang paling kamu suka duluan — tanpa mikirin nanti bisa kehabisan uang atau tidak. **Pokoknya sekarang yang paling enak dulu!**

### Contoh: Coin Change
**Masalah:** Kembalian Rp4.700 dengan koin minimal. Koin yang tersedia: Rp1.000, Rp500, Rp200, Rp100.

```
Strategi Greedy: Ambil koin terbesar yang bisa diambil.

Rp4.700 → ambil Rp1.000 (sisa Rp3.700)
        → ambil Rp1.000 (sisa Rp2.700)
        → ambil Rp1.000 (sisa Rp1.700)
        → ambil Rp1.000 (sisa Rp700)
        → ambil Rp500  (sisa Rp200)
        → ambil Rp200  (sisa Rp0)

Total: 6 koin (4×1000 + 1×500 + 1×200) ✅
```

### Contoh: Activity Selection
**Masalah:** Dalam satu ruangan, jadwalkan kegiatan sebanyak mungkin yang tidak bertabrakan.

```
Kegiatan:                        Pilih yang selesai paling awal!
─── 1. ────── 08:00-09:00 ✓           ────
───── 2. ─── 08:30-09:30              ───
─── 3. ─── 09:00-10:00 ✓                    ────
───── 4. ─ 10:30-10:45 ✓                          ──
```

> 💡 **Kunci Greedy:** Pilih yang **selesai paling awal** = bisa muat lebih banyak kegiatan!

### Kapan Greedy Tepat?
✅ Kalau pilihan lokal terbukti menghasilkan solusi global optimal
❌ Tidak semua masalah bisa diselesaikan dengan Greedy

```python
# Contoh: Coin Change dengan Greedy di Python
koin = [1000, 500, 200, 100]
sisa = 4700
hasil = []
for k in koin:
    while sisa >= k:
        hasil.append(k)
        sisa -= k
print(hasil)  # [1000, 1000, 1000, 1000, 500, 200]
```

### 🔍 Cek Pemahaman
1. Jelaskan prinsip utama algoritma Greedy dengan kata-katamu sendiri!
2. Dalam kasus Activity Selection, mengapa memilih kegiatan yang selesai paling awal adalah strategi Greedy yang tepat?
3. Kapan algoritma Greedy **tidak** tepat digunakan? Berikan contoh!

### 📋 Studi Kasus
Saat bazar sekolah, Dita memiliki uang Rp25.000 untuk membeli makanan. Berikut harga makanan yang tersedia: Siomay Rp5.000, Batagor Rp7.000, Risol Rp3.000, Cireng Rp4.000, dan Es Buah Rp6.000. Dita ingin mendapatkan **sebanyak mungkin jenis makanan** dengan uang yang ada.

**Analisis:**
1. Jika Dita menggunakan strategi Greedy, makanan apa yang pertama kali dibelinya? Apakah strategi Greedy menghasilkan solusi optimal untuk kasus ini?
2. Coba gunakan strategi berbeda dan bandingkan hasilnya dengan strategi Greedy!

> 🤔 **Mari Renungkan:** Apa hal paling menarik yang kamu pelajari dari bagian ini?

---

## E. Pemrograman Dinamis: Optimasi dengan Subproblem

### 📊 Pemrograman Dinamis: Optimasi dengan Subproblem
**Dynamic Programming (DP)** adalah teknik menyelesaikan masalah dengan **memecahnya menjadi sub-masalah kecil**, menyimpan hasilnya, dan menggunakan kembali hasil tersebut.

> 🧩 **Analogi:** DP itu seperti **belajar naik sepeda**. Kamu tidak perlu belajar dari nol setiap kali naik sepeda — otakmu sudah menyimpan "cara naik sepeda" (memoisasi) dan tinggal menggunakannya lagi.

### DP vs Rekursi Biasa
```
FIBONACCI dengan REKURSI biasa:       FIBONACCI dengan DP (Memoization):

fib(5)                                  fib(5)
├── fib(4)                              ├── fib(4) → simpan di cache
│   ├── fib(3)                          │   ├── fib(3) → simpan
│   │   ├── fib(2)                      │   │   ├── fib(2) → simpan
│   │   │   ├── fib(1) ✅               │   │   │   ├── fib(1) ✅
│   │   │   └── fib(0) ✅               │   │   │   └── fib(0) ✅
│   │   └── fib(1) ✅                   │   │   └── (pakai cache fib(1))
│   └── fib(2) → HITUNG LAGI! ❌        │   └── (pakai cache fib(2))
└── fib(3) → HITUNG LAGI! ❌            └── (pakai cache fib(3))
```

### Implementasi DP
```python
# Tanpa DP — lambat untuk n besar
def fib_rekursif(n):
    if n <= 1: return n
    return fib_rekursif(n-1) + fib_rekursif(n-2)  # O(2^n)

# Dengan DP (Memoization) — cepat!
cache = {}
def fib_dp(n):
    if n <= 1: return n
    if n not in cache:
        cache[n] = fib_dp(n-1) + fib_dp(n-2)
    return cache[n]  # O(n)

print(fib_dp(50))  # Output: 12586269025 (LANGSUNG!)
```

| n | fib(n) | Rekursi biasa | DP (Memoization) |
|---|--------|--------------|------------------|
| 10 | 55 | 0,001 detik | 0,001 detik |
| 30 | 832040 | 0,5 detik | 0,001 detik |
| 50 | 12.586.269.025 | ~600 tahun! | 0,001 detik |

> 🔑 **2 Kunci DP:** 1) **Overlapping Subproblems** — sub-masalah yang berulang, 2) **Optimal Substructure** — solusi optimal dari sub-masalah membentuk solusi optimal keseluruhan.

### 🔍 Cek Pemahaman
1. Jelaskan perbedaan utama antara rekursi biasa dan Dynamic Programming!
2. Apa yang dimaksud dengan Memoization? Bagaimana cara kerjanya?
3. Mengapa fib(50) dengan rekursi biasa memakan waktu ~600 tahun, tapi dengan DP hanya 0,001 detik?

### 📋 Studi Kasus
Seorang siswa bernama Adi ingin menabung untuk mengikuti study tour ke Yogyakarta seharga Rp1.500.000 dalam waktu 6 bulan (180 hari). Setiap hari ia bisa menabung Rp5.000, Rp10.000, atau Rp20.000. Ia ingin tahu berapa banyak cara yang bisa dilakukan untuk mencapai target tersebut.

**Analisis:**
1. Mengapa masalah ini cocok diselesaikan dengan DP daripada rekursi biasa?
2. Konsep DP apa (Overlapping Subproblems / Optimal Substructure) yang muncul dalam masalah tabungan Adi? Jelaskan!

> 🤔 **Mari Renungkan:** Apa hal paling menarik yang kamu pelajari dari bagian ini?

---

## F. Array, String, dan Manipulasi Data

### 📦 Array, String, dan Manipulasi Data

### Array — Kumpulan Data Terindeks
```python
nilai = [85, 92, 78, 90, 88]  # Array 5 elemen
# Indeks: 0   1   2   3   4
print(nilai[0])    # 85
print(nilai[-1])   # 88 (indeks negatif = dari belakang)
print(len(nilai))  # 5 (panjang array)
```

> 🧩 **Analogi:** Array seperti **loker di sekolah**. Setiap loker punya nomor (indeks) dan isi (data). Nomor dimulai dari 0!

### Operasi Dasar Array
```python
angka = [3, 1, 4, 1, 5]
angka.append(9)       # Tambah di akhir → [3,1,4,1,5,9]
angka.sort()          # Urutkan → [1,1,3,4,5,9]
angka.reverse()       # Balik → [9,5,4,3,1,1]
angka.pop()           # Ambil & hapus terakhir → 1
print(angka.index(4)) # Cari posisi angka 4 → 2
```

### String — Teks juga Kumpulan Data!
```python
teks = "Informatika"
print(teks[0])        # 'I'
print(teks[:4])       # 'Info' (dari 0 sampai 3)
print(teks[-3:])      # 'ika' (3 karakter terakhir)
print(teks.upper())   # 'INFORMATIKA'
print(teks.count('a')) # 2 (huruf 'a' muncul 2x)
```

### Pattern Matching Sederhana
```python
teks = "Hari ini belajar Python di kelas XI"
cari = "Python"
if cari in teks:
    print(f"'{cari}' ditemukan!")

# Cari posisi
posisi = teks.find("kelas")
print(f"Dimulai dari indeks: {posisi}")  # Output: 23
```

> ✍️ **Latihan:** Buat program yang menerima 7 nama teman sekelas, simpan dalam array, urutkan secara alfabet, lalu tampilkan!

### 🔍 Cek Pemahaman
1. Apa perbedaan indeks positif dan negatif dalam array Python? Berikan contoh!
2. Jelaskan fungsi `append()`, `sort()`, dan `pop()` pada array!
3. Bagaimana cara mencari kata tertentu di dalam sebuah string menggunakan Python?

### 📋 Studi Kasus
Ketua kelas XI IPA 1 ingin membuat aplikasi **presensi kehadiran** sederhana. Setiap hari, guru mencatat siapa saja yang hadir. Selama seminggu, data kehadiran dikumpulkan dalam sebuah array. Dari 35 siswa, ternyata rata-rata 3 siswa tidak hadir setiap hari.

**Analisis:**
1. Buat array Python sederhana yang menyimpan data kehadiran 5 siswa selama 1 minggu! Bagaimana cara menentukan siswa dengan kehadiran terbanyak?
2. Jika data kehadiran disimpan sebagai string panjang, bagaimana cara menghitung jumlah siswa yang hadir setiap hari?

> 🤔 **Mari Renungkan:** Apa hal paling menarik yang kamu pelajari dari bagian ini?

---

## G. Perbandingan Strategi Algoritmik

### ⚖️ Perbandingan Strategi Algoritmik

Setiap strategi punya **kelebihan dan kekurangan**. Mari bandingkan!

### Tabel Perbandingan
| Aspek | Rekursif | Iteratif | Greedy | Dynamic Programming |
|-------|----------|----------|--------|-------------------|
| **Prinsip** | Panggil diri sendiri | Ulang dengan loop | Pilih terbaik lokal | Simpan sub-masalah |
| **Mudah?** | Untuk masalah tertentu | Umum | Konsep sederhana | Konsep sulit |
| **Efisiensi** | Lambat (tanpa DP) | Cepat | Cepat | Cepat |
| **Memori** | Boros stack | Hemat | Hemat | Cukup besar |
| **Cocok untuk** | Tree, fractal | Masalah umum | Optimasi sederhana | Optimasi kompleks |

### Kapan Pakai Yang Mana?
```
┌──────────────────────────────────────────────────┐
│              PERTANYAAN KUNCI                    │
├──────────────────────────────────────────────────┤
│                                                   │
│  Apakah subproblem berulang?                      │
│     ├── Ya → Apakah solusi lokal = global?        │
│     │         ├── Ya → GREEDY ✅                  │
│     │         └── Tidak → DP ✅                   │
│     └── Tidak → Apakah masalah bisa dipecah?      │
│               ├── Ya → REKURSI ✅                 │
│               └── Tidak → ITERASI ✅              │
└──────────────────────────────────────────────────┘
```

### Contoh: Menghitung Uang Kembalian
| Strategi | Cara | Hasil |
|----------|------|-------|
| **Greedy** | Ambil koin terbesar dulu | 6 koin (4×1000+500+200) ✅ |
| **DP** | Cari kombinasi minimal | 6 koin (sama, karena koin standar) |
| **Rekursi** | Coba semua kemungkinan | 6 koin, tapi lambat |
| **Iterasi** | Loop dari koin terbesar | 6 koin, sederhana |

> 💡 **Insight:** Tidak ada strategi "paling baik" untuk semua masalah — **pilih yang paling sesuai** dengan karakteristik masalah!

### 🔍 Cek Pemahaman
1. Sebutkan 4 strategi algoritmik yang dibahas! Jelaskan prinsip dasar masing-masing!
2. Kapan waktu yang tepat menggunakan algoritma Greedy? Kapan waktu yang tepat menggunakan DP?
3. Buatlah diagram alir (flowchart) sederhana untuk memilih strategi algoritmik!

### 📋 Studi Kasus
SMA Bangsa mengadakan lomba **Hackathon** antarkelas. Setiap tim mendapat masalah yang berbeda: Tim A mendapat masalah mencari jalur terpendek pengiriman makanan, Tim B mendapat masalah menyusun jadwal pelajaran tanpa tabrakan, dan Tim C mendapat masalah mencari kata dalam kamus raksasa.

**Analisis:**
1. Strategi algoritmik apa yang paling cocok untuk masing-masing tim? Jelaskan alasannya!
2. Jika Tim A mencoba menggunakan rekursi sederhana untuk masalah pengiriman makanan, apa yang akan terjadi?

> 🤔 **Mari Renungkan:** Apa hal paling menarik yang kamu pelajari dari bagian ini?

---

---
## 🏗️ Proyek Mini: ⚡ Kuis Interaktif Algoritma

Buat program Python sederhana yang membandingkan 2 strategi algoritmik (misal: Linear Search vs Binary Search, atau rekursi biasa vs DP Fibonacci). Program harus menampilkan waktu eksekusi dan perbandingan efisiensi.

**Alat dan Bahan:**
- Python 3 (IDLE / VS Code / Google Colab)
- Modul time untuk mengukur kecepatan
- Buku catatan untuk analisis

**Langkah-langkah:**
1. Pilih 2 algoritma yang akan dibandingkan (contoh: rekursi Fibonacci vs DP Fibonacci, atau Linear Search vs Binary Search).
2. Implementasikan kedua algoritma dalam fungsi Python yang terpisah.
3. Gunakan modul `time` untuk mengukur waktu eksekusi masing-masing algoritma dengan berbagai ukuran input.
4. Buat tabel sederhana yang menampilkan perbandingan waktu eksekusi untuk n = 10, 100, 1000, 10000.
5. Tambahkan komentar pada kode untuk menjelaskan cara kerja setiap algoritma.
6. Demo program ke kelas dan jelaskan mengapa algoritma yang lebih efisien lebih unggul.

> **Output:** File Python (.py) + tabel perbandingan eksekusi + demo lisan

## 📝 Rangkuman

- **Dasar Python:** variabel (`int`, `float`, `str`, `bool`), percabangan (`if/elif/else`), perulangan (`for`/`while`), dan fungsi (`def`) adalah fondasi penting sebelum menerapkan strategi algoritmik.
- Proses pemrograman terdiri dari 4 tahap: **Analisis → Desain → Implementasi → Pengujian**. Efisiensi algoritma diukur dengan **Big O Notation**.
- **Rekursi** adalah fungsi yang memanggil dirinya sendiri, terdiri dari base case dan recursive case. Cocok untuk masalah bertingkat seperti pohon dan fractal.
- **Algoritma Greedy** mengambil pilihan terbaik saat ini (lokal optimal) dengan harapan menghasilkan solusi global optimal — contoh: Coin Change dan Activity Selection.
- **Dynamic Programming** menyimpan hasil sub-masalah (Memoization) untuk menghindari perhitungan ulang — sangat efektif untuk masalah dengan overlapping subproblems.
- **Array** adalah struktur data untuk menyimpan kumpulan nilai terindeks, dimulai dari indeks 0. String juga bisa diperlakukan seperti array karakter.

---
## ✍️ Latihan Soal

### Pilihan Ganda

1. Kompleksitas algoritma O(n²) berarti waktu eksekusi berbanding lurus dengan...
   a. Konstanta, tidak tergantung data
   b. Jumlah data (n)
   c. Kuadrat jumlah data (n²)
   d. Logaritma jumlah data (log n)
   e. Eksponensial jumlah data (2ⁿ)
   **Kunci Jawaban: C**

2. Dalam fungsi rekursif, kondisi yang menghentikan pemanggilan diri sendiri disebut...
   a. Recursive case
   b. Base case
   c. Loop condition
   d. Stack frame
   e. Infinite recursion
   **Kunci Jawaban: B**

3. Algoritma greedy selalu mengambil pilihan...
   a. Terbaik secara keseluruhan (global optimal)
   b. Terbaik pada saat itu (lokal optimal)
   c. Pilihan acak
   d. Pilihan yang paling rumit
   e. Pilihan yang paling sederhana
   **Kunci Jawaban: B**

4. Teknik menyimpan hasil sub-masalah untuk digunakan kembali disebut...
   a. Rekursi
   b. Iterasi
   c. Memoisasi (Memoization)
   d. Branching
   e. Sorting
   **Kunci Jawaban: C**

5. Dalam array Python, indeks elemen pertama adalah...
   a. -1
   b. 0
   c. 1
   d. 2
   e. Tergantung panjang array
   **Kunci Jawaban: B**

### Uraian

1. Jelaskan perbedaan antara Rekursi dan Iterasi! Kapan sebaiknya menggunakan Rekursi dan kapan menggunakan Iterasi? Berikan contoh masing-masing!

2. Apa yang dimaksud dengan algoritma Greedy? Jelaskan dengan contoh kasus Activity Selection atau Coin Change!

3. Bagaimana Dynamic Programming (DP) dapat mengoptimalkan kinerja program? Jelaskan konsep Memoization dengan contoh kasus Fibonacci!

4. Bandingkan kelebihan dan kekurangan dari Algoritma Greedy, Dynamic Programming, Rekursi, dan Iterasi! Kapan waktu yang tepat menggunakan masing-masing?

---
## 📋 Rubrik Penilaian Proyek

| Aspek | Kurang | Cukup | Baik |
|-------|--------|-------|------|
| Kebenaran Program | Program error atau tidak jalan | Program jalan dengan sedikit bug | Program jalan sempurna, tidak ada error |
| Perbandingan Algoritma | Tidak ada perbandingan yang jelas | Ada perbandingan tapi kurang detail | Perbandingan lengkap dengan tabel dan analisis |
| Dokumentasi Kode | Tanpa komentar, sulit dibaca | Ada komentar di beberapa bagian | Kode rapi, komentar jelas, struktur baik |
| Presentasi & Demo | Demo gagal, tidak bisa menjelaskan | Demo berjalan, penjelasan cukup jelas | Demo lancar, menjelaskan konsep dengan baik |

---
## 🚀 Tugas Pengayaan

### ⚡ Tantangan Coding di HackerRank
Selesaikan minimal 5 soal algoritma di [HackerRank](https://www.hackerrank.com/) pada kategori *Problem Solving* (mulai dari level Easy). Screenshot hasil submission yang accepted dan catat pendekatan yang kamu gunakan untuk setiap soal. Bandingkan kompleksitas algoritma yang kamu tulis dengan solusi optimal.

### 🔄 Visualisasi Algoritma di Visualgo
Kunjungi [Visualgo.net](https://visualgo.net/) dan pelajari visualisasi dari 3 algoritma: Binary Search, Greedy (Activity Selection), dan Dynamic Programming (Knapsack). Tuliskan penjelasan bagaimana masing-masing algoritma bekerja berdasarkan animasi yang kamu lihat.

---
## 📖 Glosarium

- **Python:** Bahasa pemrograman level tinggi, interpretatif, dengan sintaks yang mudah dibaca. Banyak digunakan dalam data science, AI, dan edukasi.
- **Variabel:** Tempat menyimpan data dalam program. Python menggunakan dynamic typing (tipe ditentukan otomatis dari nilai).
- **Fungsi (`def`):** Blok kode yang dapat dipanggil berulang kali, bisa menerima parameter dan mengembalikan nilai.
- **Big O Notation**: Notasi yang mengukur efisiensi algoritma berdasarkan pertumbuhan waktu eksekusi terhadap ukuran input.
- **Rekursi**: Fungsi yang memanggil dirinya sendiri, terdiri dari base case dan recursive case.
- **Algoritma Greedy**: Strategi algoritmik yang mengambil pilihan terbaik pada saat ini (lokal optimal).
- **Dynamic Programming**: Teknik optimasi dengan menyimpan hasil sub-masalah (memoization) untuk menghindari perhitungan ulang.
- **Array**: Struktur data yang menyimpan kumpulan nilai dengan tipe data sama, diakses menggunakan indeks.
- **Base Case**: Kondisi berhenti dalam fungsi rekursif untuk mencegah infinite loop.
- **Memoization**: Teknik menyimpan hasil perhitungan sub-masalah agar tidak dihitung ulang.

---
## 📺 Sumber & Media Pembelajaran

| Platform | Sumber | Tautan | Keterangan |
|----------|--------|--------|------------|
| YouTube | Big O Notation dalam 5 Menit | `youtu.be/search?q=Big+O+Notation+indonesia` | Penjelasan efisiensi algoritma |
| Simulasi | Visualgo — Visualisasi Algoritma | `https://visualgo.net/` | Simulasi visual berbagai algoritma |
| YouTube | Apa itu Rekursi? | `youtu.be/search?q=rekursi+algoritma` | Penjelasan rekursi dengan animasi |
| YouTube | Dynamic Programming untuk Pemula | `youtu.be/search?q=dynamic+programming+pemula` | Konsep DP dengan contoh sederhana |
| Website | HackerRank | `https://www.hackerrank.com/` | Platform latihan soal algoritma dan coding |
| Website | W3Schools Python Tutorial | `https://www.w3schools.com/python/` | Tutorial interaktif dasar Python (EN) |
| Website | Belajar Python — DataCamp | `https://www.datacamp.com/courses/intro-to-python-for-data-science` | Kursus pengantar Python gratis |
