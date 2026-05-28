# LKPD - Analisis Data dengan Python
**Mata Pelajaran:** Informatika
**Kelas/Semester:** XI / Genap
**Materi Pokok:** Bab 6 - Analisis Data (Import CSV, Sorting, Visualisasi dengan Matplotlib)
**Alokasi Waktu:** 5 JP

## A. Tujuan Pembelajaran
1. Mengimpor data dari file CSV ke dalam program Python
2. Melakukan pengurutan (sorting) data berdasarkan kriteria tertentu
3. Membuat visualisasi data menggunakan library Matplotlib
4. Menyajikan data dalam bentuk grafik yang informatif

## B. Alat dan Bahan
1. Komputer/laptop dengan koneksi internet
2. Google Colab (colab.research.google.com) atau Python 3.x dengan library pandas dan matplotlib
3. File dataset CSV (akan dibuat sendiri)

## C. Langkah Kerja

### Langkah 1: Persiapan Google Colab
1. Buka https://colab.research.google.com
2. Klik **File > New notebook**
3. Ganti nama notebook menjadi `Analisis_Data_XI.ipynb`
4. Jalankan cell pertama untuk cek library:
```python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

print("Library berhasil diimport!")
print(f"Pandas version: {pd.__version__}")
print(f"Matplotlib version: {plt.matplotlib.__version__}")
```

### Langkah 2: Membuat Dataset CSV
Buat file `nilai_siswa.csv` dengan data berikut. Bisa dibuat langsung di Colab:

```python
# Buat dataset nilai siswa
data = {
    "Nama": ["Andi", "Budi", "Citra", "Dewi", "Eko",
             "Fajar", "Gita", "Hadi", "Indah", "Joko",
             "Kiki", "Lala", "Mega", "Nina", "Oka"],
    "Kelas": ["XI-A", "XI-A", "XI-A", "XI-B", "XI-B",
              "XI-B", "XI-A", "XI-A", "XI-B", "XI-B",
              "XI-A", "XI-B", "XI-A", "XI-B", "XI-A"],
    "Tugas": [85, 78, 92, 88, 65,
              72, 95, 80, 74, 90,
              88, 76, 91, 83, 79],
    "UTS": [82, 75, 90, 85, 60,
            70, 93, 78, 72, 88,
            85, 74, 89, 80, 76],
    "UAS": [88, 80, 95, 86, 68,
            75, 96, 82, 76, 92,
            90, 78, 93, 85, 80]
}

df = pd.DataFrame(data)

# Simpan ke CSV
df.to_csv("nilai_siswa.csv", index=False)
print("Dataset berhasil dibuat!")
print(df.head())
```

### Langkah 3: Import dan Eksplorasi Data
```python
# Import data dari CSV
df = pd.read_csv("nilai_siswa.csv")

# Lihat 5 data pertama
print("5 Data Pertama:")
print(df.head())

# Info dataset
print("\nInfo Dataset:")
print(df.info())

# Statistik deskriptif
print("\nStatistik Deskriptif:")
print(df.describe())

# Cek jumlah siswa per kelas
print("\nJumlah Siswa per Kelas:")
print(df["Kelas"].value_counts())
```

### Langkah 4: Menambahkan Kolom Nilai Akhir
```python
# Hitung nilai akhir: 20% Tugas + 30% UTS + 50% UAS
df["Nilai_Akhir"] = (0.2 * df["Tugas"] +
                     0.3 * df["UTS"] +
                     0.5 * df["UAS"])

# Bulatkan 1 desimal
df["Nilai_Akhir"] = df["Nilai_Akhir"].round(1)

# Tambahkan kolom status
df["Status"] = df["Nilai_Akhir"].apply(
    lambda x: "Lulus" if x >= 70 else "Tidak Lulus"
)

print("\nData dengan Nilai Akhir:")
print(df[["Nama", "Kelas", "Nilai_Akhir", "Status"]].head(10))
```

### Langkah 5: Sorting Data
```python
# Urutkan berdasarkan Nilai Akhir (tertinggi ke terendah)
print("10 Siswa dengan Nilai Akhir Terbaik:")
df_sorted = df.sort_values("Nilai_Akhir", ascending=False)
print(df_sorted[["Nama", "Kelas", "Nilai_Akhir"]].head(10))

print("\n10 Siswa dengan Nilai Akhir Terendah:")
print(df_sorted[["Nama", "Kelas", "Nilai_Akhir"]].tail(10))

# Urutkan berdasarkan Nama (A-Z)
print("\nSiswa urut abjad:")
df_abjad = df.sort_values("Nama")
print(df_abjad[["Nama", "Kelas", "Nilai_Akhir"]])
```

### Langkah 6: Visualisasi dengan Matplotlib - Diagram Batang
```python
# Diagram batang nilai akhir seluruh siswa
plt.figure(figsize=(12, 6))
plt.bar(df["Nama"], df["Nilai_Akhir"], color="skyblue")
plt.axhline(y=70, color="red", linestyle="--", label="Batas Lulus (70)")
plt.xlabel("Nama Siswa", fontsize=12)
plt.ylabel("Nilai Akhir", fontsize=12)
plt.title("Nilai Akhir Siswa Kelas XI", fontsize=14, fontweight="bold")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()
```

### Langkah 7: Visualisasi - Diagram Lingkaran (Pie Chart)
```python
# Diagram lingkaran perbandingan kelas
kelas_count = df["Kelas"].value_counts()

plt.figure(figsize=(8, 8))
plt.pie(kelas_count.values, labels=kelas_count.index,
        autopct="%1.1f%%", colors=["gold", "lightcoral"],
        startangle=90, shadow=True)
plt.title("Perbandingan Jumlah Siswa per Kelas", fontsize=14, fontweight="bold")
plt.axis("equal")
plt.show()
```

### Langkah 8: Visualisasi - Diagram Garis (Perbandingan Nilai)
```python
# Perbandingan nilai Tugas, UTS, UAS per siswa
plt.figure(figsize=(14, 7))
x = range(len(df))
plt.plot(x, df["Tugas"], marker="o", label="Tugas", color="blue")
plt.plot(x, df["UTS"], marker="s", label="UTS", color="green")
plt.plot(x, df["UAS"], marker="^", label="UAS", color="orange")
plt.plot(x, df["Nilai_Akhir"], marker="d", label="Nilai Akhir", color="red", linewidth=2)

plt.xlabel("Siswa (Index)", fontsize=12)
plt.ylabel("Nilai", fontsize=12)
plt.title("Perbandingan Nilai Tugas, UTS, UAS, dan Nilai Akhir", fontsize=14)
plt.xticks(x, df["Nama"], rotation=45)
plt.legend()
plt.grid(True, linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()
```

### Langkah 9: Analisis Tambahan - Rata-rata per Kelas
```python
# Rata-rata nilai per kelas
rata_kelas = df.groupby("Kelas")[["Tugas", "UTS", "UAS", "Nilai_Akhir"]].mean().round(1)
print("Rata-rata Nilai per Kelas:")
print(rata_kelas)

# Diagram batang perbandingan rata-rata kelas
rata_kelas.plot(kind="bar", figsize=(10, 6))
plt.title("Perbandingan Rata-rata Nilai per Kelas", fontsize=14, fontweight="bold")
plt.xlabel("Kelas", fontsize=12)
plt.ylabel("Rata-rata Nilai", fontsize=12)
plt.xticks(rotation=0)
plt.legend(title="Komponen")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()
```

### Langkah 10: Tugas Mandiri
```python
# TODO 1: Hitung jumlah siswa yang lulus dan tidak lulus
# Tampilkan dalam diagram lingkaran

# TODO 2: Buat diagram batang horizontal (barh) untuk 5 nilai akhir terbaik

# TODO 3: Filter siswa dengan nilai akhir >= 80 (sangat baik), cetak daftarnya

# TODO 4: Buat scatter plot antara UTS dan UAS untuk melihat korelasi
```

## D. Tabel Hasil/Data Pengamatan

| No | Langkah | Deskripsi | Hasil/Cuplikan Output |
|----|---------|-----------|-----------------------|
| 1 | Import data | df.head() | |
| 2 | Statistik | df.describe() | |
| 3 | Sorting | 3 besar nilai akhir | |
| 4 | Diagram batang | Grafik nilai akhir | |
| 5 | Diagram lingkaran | Pie chart per kelas | |
| 6 | Diagram garis | Perbandingan nilai | |
| 7 | Rata-rata kelas | Groupby mean | |

## E. Diskusi dan Analisis
1. Jelaskan fungsi method `pd.read_csv()` dan `df.info()`. Informasi apa saja yang bisa didapat dari `df.describe()`?
2. Bagaimana cara kerja pengurutan (`sort_values`) secara descending dan ascending? Berikan contoh penggunaannya.
3. Pada diagram batang nilai akhir, apa arti garis horizontal merah di y=70? Mengapa garis tersebut penting?
4. Bandingkan diagram batang dan diagram lingkaran. Kapan sebaiknya menggunakan masing-masing jenis diagram?
5. Interpretasikan diagram perbandingan nilai Tugas, UTS, UAS. Apakah ada pola tertentu? Siswa mana yang paling konsisten?

## F. Kesimpulan
Tuliskan kesimpulan dari praktikum ini minimal 3 poin.

## G. Penilaian

| Aspek | Bobot | Skor (1-4) | Nilai |
|-------|-------|------------|-------|
| Import data dan eksplorasi | 15% | | |
| Menambahkan kolom dan sorting | 15% | | |
| Visualisasi diagram batang | 15% | | |
| Visualisasi diagram lingkaran | 15% | | |
| Visualisasi diagram garis | 15% | | |
| Tugas mandiri | 15% | | |
| Jawaban diskusi | 10% | | |
| **Total** | **100%** | | |
