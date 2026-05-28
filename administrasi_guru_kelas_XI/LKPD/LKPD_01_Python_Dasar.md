# LKPD - Python Dasar
**Mata Pelajaran:** Informatika
**Kelas/Semester:** XI / Ganjil
**Materi Pokok:** Bab 2 - Dasar Pemrograman Python (Variabel, Tipe Data, Input/Output, Operator)
**Alokasi Waktu:** 5 JP

## A. Tujuan Pembelajaran
1. Menjelaskan konsep variabel dan tipe data dalam Python
2. Menggunakan input/output untuk interaksi dengan pengguna
3. Menerapkan operator aritmatika, perbandingan, dan logika
4. Membuat program sederhana (hitung luas, konversi suhu)

## B. Alat dan Bahan
1. Komputer/laptop dengan sistem operasi Windows/Linux/macOS
2. Python 3.x terinstal (cek dengan `python --version`)
3. Teks editor (VS Code, IDLE, atau Thonny)
4. *Atau akses* ke Google Colab (colab.research.google.com)

## C. Langkah Kerja

### Langkah 1: Cek Instalasi Python
Buka terminal/command prompt, ketik:
```bash
python --version
```
Pastikan muncul versi Python 3.x.

### Langkah 2: Program Pertama - Hello World
Buat file `hello.py`, tulis kode berikut:
```python
# Program pertama
print("Hello, Selamat Belajar Python!")
print("Informatika Kelas XI")
```

Jalankan:
```bash
python hello.py
```

### Langkah 3: Variabel dan Tipe Data
Buat file `variabel.py`:
```python
# Variabel dan Tipe Data
nama = "Alex"          # string
umur = 17              # integer
tinggi = 165.5         # float
siswa_aktif = True     # boolean

print("Nama:", nama)
print("Tipe data nama:", type(nama))
print("Umur:", umur)
print("Tipe data umur:", type(umur))
print("Tinggi:", tinggi)
print("Tipe data tinggi:", type(tinggi))
print("Siswa aktif:", siswa_aktif)
print("Tipe data siswa_aktif:", type(siswa_aktif))
```

### Langkah 4: Input dari Pengguna
Buat file `input_data.py`:
```python
# Input Data Diri
nama = input("Masukkan nama kamu: ")
umur = int(input("Masukkan umur kamu: "))
tinggi = float(input("Masukkan tinggi badan (cm): "))

print("\n--- Data Diri ---")
print(f"Nama  : {nama}")
print(f"Umur  : {umur} tahun")
print(f"Tinggi: {tinggi} cm")
print(f"Tahun depan umurmu {umur + 1} tahun")
```

### Langkah 5: Operator Aritmatika
Buat file `operator.py`:
```python
# Operator Aritmatika
a = int(input("Masukkan bilangan pertama: "))
b = int(input("Masukkan bilangan kedua: "))

print(f"\n{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} x {b} = {a * b}")
print(f"{a} : {b} = {a / b}")
print(f"{a} // {b} = {a // b}  (pembagian bulat)")
print(f"{a} ^ {b}  = {a ** b}  (pangkat)")
print(f"{a} mod {b} = {a % b}  (sisa bagi)")
```

### Langkah 6: Program Hitung Luas Bangun Datar
Buat file `hitung_luas.py`:
```python
# Program Hitung Luas Bangun Datar
print("=== PROGRAM HITUNG LUAS ===")
print("1. Luas Persegi")
print("2. Luas Persegi Panjang")
print("3. Luas Segitiga")
print("4. Luas Lingkaran")

pilihan = int(input("Pilih bangun (1-4): "))

# Luas Persegi
sisi = int(input("Masukkan sisi: "))
luas = sisi * sisi
print(f"Luas persegi (sisi={sisi}) = {luas}")

# TODO: siswa melengkapi pilihan 2, 3, 4 sendiri
```

### Langkah 7: Program Konversi Suhu
Buat file `konversi_suhu.py`:
```python
# Program Konversi Suhu
print("=== KONVERSI SUHU ===")
celcius = float(input("Masukkan suhu dalam Celcius: "))

fahrenheit = (celcius * 9/5) + 32
reamur = celcius * 4/5
kelvin = celcius + 273.15

print(f"{celcius}°C = {fahrenheit:.2f}°F")
print(f"{celcius}°C = {reamur:.2f}°R")
print(f"{celcius}°C = {kelvin:.2f}K")
```

## D. Tabel Hasil/Data Pengamatan

| No | Program | Input | Output | Keterangan |
|----|---------|-------|--------|------------|
| 1 | hello.py | - | | |
| 2 | variabel.py | - | | |
| 3 | input_data.py | nama, umur, tinggi | | |
| 4 | operator.py | a=10, b=3 | | |
| 5 | konversi_suhu.py | 100°C | | |

## E. Diskusi dan Analisis
1. Apa perbedaan tipe data `int`, `float`, dan `str`? Berikan contoh masing-masing.
2. Mengapa saat menggunakan `input()` hasilnya perlu dikonversi dengan `int()` atau `float()` untuk operasi matematika?
3. Pada program konversi suhu, apa yang terjadi jika input berupa huruf? Mengapa?
4. Jelaskan perbedaan operator `/` (pembagian biasa) dan `//` (pembagian bulat) dengan contoh.
5. Buatlah variasi program konversi suhu yang menerima input dalam Fahrenheit dan mengonversi ke Celcius.

## F. Kesimpulan
Tuliskan kesimpulan dari praktikum ini minimal 3 poin.

## G. Penilaian

| Aspek | Bobot | Skor (1-4) | Nilai |
|-------|-------|------------|-------|
| Ketepatan menulis sintaks | 25% | | |
| Program berjalan dengan benar | 25% | | |
| Kelengkapan tabel pengamatan | 20% | | |
| Jawaban diskusi dan analisis | 20% | | |
| Kesimpulan | 10% | | |
| **Total** | **100%** | | |
