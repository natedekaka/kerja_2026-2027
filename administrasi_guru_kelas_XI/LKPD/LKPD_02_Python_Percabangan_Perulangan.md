# LKPD - Python Percabangan dan Perulangan
**Mata Pelajaran:** Informatika
**Kelas/Semester:** XI / Ganjil
**Materi Pokok:** Bab 2 - Struktur Kontrol: Percabangan (if/elif/else) dan Perulangan (for/while)
**Alokasi Waktu:** 5 JP

## A. Tujuan Pembelajaran
1. Menerapkan struktur percabangan if/elif/else dalam Python
2. Menggunakan perulangan for dan while untuk memproses data berulang
3. Membuat program grade nilai, tebak angka, dan deret bilangan
4. Mengidentifikasi kapan menggunakan percabangan dan perulangan

## B. Alat dan Bahan
1. Komputer/laptop dengan Python 3.x
2. Teks editor / IDE Python
3. Google Colab (alternatif)

## C. Langkah Kerja

### Langkah 1: Percabangan if/elif/else
Buat file `percabangan.py`:
```python
# Percabangan if/elif/else
nilai = int(input("Masukkan nilai ujian (0-100): "))

if nilai >= 90:
    print("Grade A - Sangat Baik")
elif nilai >= 80:
    print("Grade B - Baik")
elif nilai >= 70:
    print("Grade C - Cukup")
elif nilai >= 60:
    print("Grade D - Kurang")
else:
    print("Grade E - Tidak Lulus")

# Cek kelulusan
if nilai >= 70:
    print(f"Selamat! Nilai {nilai} dinyatakan LULUS")
else:
    print(f"Maaf! Nilai {nilai} dinyatakan TIDAK LULUS")
```

### Langkah 2: Program Grade Nilai (Lengkap)
Buat file `grade_nilai.py` dan lengkapi bagian yang kosong:
```python
# === PROGRAM GRADE NILAI ===
# Lengkapi bagian yang bertanda TODO

print("=== Grade Nilai ===")
nama = input("Nama siswa: ")
nilai = int(input("Nilai akhir: "))

# TODO: Tentukan grade dengan if/elif/else
# A: 90-100, B: 80-89, C: 70-79, D: 60-69, E: <60
if ___________________:
    grade = "A"
    predikat = "Sangat Baik"
elif _________________:
    grade = "B"
    predikat = "Baik"
elif _________________:
    grade = "C"
    predikat = "Cukup"
elif _________________:
    grade = "D"
    predikat = "Kurang"
else:
    grade = "E"
    predikat = "Tidak Lulus"

# TODO: Tentukan status lulus/tidak (lulus jika nilai >= 70)
if ___________________:
    status = "LULUS"
else:
    status = "TIDAK LULUS"

# Cetak hasil
print(f"Nama    : {nama}")
print(f"Nilai   : {nilai}")
print(f"Grade   : {grade} ({predikat})")
print(f"Status  : {status}")
```

### Langkah 3: Perulangan for
Buat file `perulangan_for.py`:
```python
# Perulangan for

# Mencetak 1-10
print("Deret 1-10:")
for i in range(1, 11):
    print(i, end=" ")
print()

# Mencetak bilangan genap
print("Bilangan genap 2-20:")
for i in range(2, 21, 2):
    print(i, end=" ")
print()

# Menjumlahkan deret
total = 0
for i in range(1, 101):
    total += i
print(f"Jumlah 1 + 2 + ... + 100 = {total}")

# Iterasi string
kata = "INFORMATIKA"
for huruf in kata:
    print(huruf, end="-")
print()
```

### Langkah 4: Perulangan while
Buat file `perulangan_while.py`:
```python
# Perulangan while

# Hitung mundur
print("Hitung mundur:")
counter = 5
while counter > 0:
    print(counter)
    counter -= 1
print("Go!")

# Input dengan validasi
password = ""
while password != "admin123":
    password = input("Masukkan password: ")
    if password != "admin123":
        print("Password salah, coba lagi!")
print("Password benar! Akses granted.")
```

### Langkah 5: Program Tebak Angka
Buat file `tebak_angka.py` dan lengkapi:
```python
# === PROGRAM TEBAK ANGKA ===
import random

angka_rahasia = random.randint(1, 20)
print("=== Tebak Angka (1-20) ===")
print("Tebak angka antara 1 sampai 20!")

tebakan = 0
percobaan = 0

# TODO: Buat perulangan while yang terus berjalan
# sampai tebakan benar
while tebakan != ________________:
    tebakan = int(input("Masukkan tebakanmu: "))
    percobaan += 1

    # TODO: Beri petunjuk apakah tebakan terlalu besar/kecil
    if tebakan ________________:
        print("Terlalu besar, coba lagi!")
    elif tebakan ________________:
        print("Terlalu kecil, coba lagi!")

# TODO: Cetak selamat dan jumlah percobaan
print(f"Selamat! Tebakanmu benar.")
print(f"Jumlah percobaan: {percobaan}")
```

### Langkah 6: Program Deret Bilangan
Buat file `deret_bilangan.py`:
```python
# === PROGRAM DERET BILANGAN ===
print("=== Deret Bilangan ===")
n = int(input("Masukkan jumlah suku (n): "))

print(f"\nDeret 1 hingga {n}:")
for i in range(1, n + 1):
    print(i, end=" ")
print()

# TODO: Cetak deret bilangan ganjil dari 1 hingga n
print(f"Bilangan ganjil 1-{n}:")
# tulis kode di sini

# TODO: Cetak deret bilangan genap dari 2 hingga n
print(f"Bilangan genap 2-{n}:")
# tulis kode di sini

# TODO: Hitung dan cetak total deret 1+2+...+n
total = 0
for i in range(1, n + 1):
    total += i
print(f"Jumlah deret 1 hingga {n} = {total}")

# TODO: Cetak deret kuadrat 1^2, 2^2, 3^2, ..., n^2
print(f"Deret kuadrat 1^2 hingga {n}^2:")
# tulis kode di sini
```

### Langkah 7: Gabungan Percabangan dan Perulangan
Buat file `menu_sekolah.py`:
```python
# Aplikasi Menu Sekolah
print("=== APLIKASI DATA SEKOLAH ===")

while True:
    print("\nMenu:")
    print("1. Cek Kelulusan")
    print("2. Deret Bilangan")
    print("3. Keluar")
    pilihan = int(input("Pilih menu (1-3): "))

    if pilihan == 1:
        print("\n--- Cek Kelulusan ---")
        nama = input("Nama: ")
        nilai = int(input("Nilai: "))
        if nilai >= 70:
            print(f"{nama} LULUS dengan nilai {nilai}")
        else:
            print(f"{nama} TIDAK LULUS dengan nilai {nilai}")

    elif pilihan == 2:
        print("\n--- Deret Bilangan ---")
        n = int(input("Masukkan batas: "))
        for i in range(1, n + 1):
            print(i, end=" ")
        print()

    elif pilihan == 3:
        print("Terima kasih!")
        break

    else:
        print("Pilihan tidak valid!")
```

## D. Tabel Hasil/Data Pengamatan

| No | Program | Input/Skenario | Output | Keterangan |
|----|---------|----------------|--------|------------|
| 1 | percabangan.py | nilai=85 | | |
| 2 | percabangan.py | nilai=55 | | |
| 3 | grade_nilai.py | nama="Siswa", nilai=92 | | |
| 4 | tebak_angka.py | tebak 3 kali benar | | |
| 5 | deret_bilangan.py | n=7 | | |
| 6 | menu_sekolah.py | pilih semua menu | | |

## E. Diskusi dan Analisis
1. Apa perbedaan antara `if-elif-else` dengan beberapa `if` terpisah? Kapan sebaiknya menggunakan masing-masing?
2. Jelaskan perbedaan perulangan `for` dan `while`. Berikan contoh kasus yang cocok untuk masing-masing.
3. Pada program tebak angka, apa fungsi `import random` dan `random.randint(1, 20)`?
4. Apa yang terjadi jika pengguna memasukkan angka di luar rentang (misal -5 atau 1000) pada program grade nilai? Bagaimana cara mengatasinya?
5. Buatlah flowchart sederhana dari program menu_sekolah.py.

## F. Kesimpulan
Tuliskan kesimpulan dari praktikum ini minimal 3 poin.

## G. Penilaian

| Aspek | Bobot | Skor (1-4) | Nilai |
|-------|-------|------------|-------|
| Kode percabangan benar | 15% | | |
| Kode perulangan benar | 15% | | |
| Program tebak angka lengkap | 20% | | |
| Program deret bilangan lengkap | 20% | | |
| Jawaban diskusi | 20% | | |
| Kesimpulan | 10% | | |
| **Total** | **100%** | | |
