# Administrasi Guru Informatika 2026/2027

**MGMP Informatika — SMA Negeri 6 Cimahi**

---

## 📚 Tentang Repositori

Repositori ini berisi seluruh dokumen administrasi pembelajaran Informatika untuk tiga jenjang:

| Kelas | Fase | JP/Minggu | Buku Pegangan |
|-------|------|-----------|---------------|
| **X** | E | 2 JP | Informatika untuk SMA/MA/SMK/MAK Kelas X (Edisi Revisi) — 9 Bab |
| **XI** | F | 5 JP | Informatika untuk SMA/MA Kelas XI (Edisi Revisi) — 6 Bab |
| **XII** | F | 5 JP | Informatika untuk SMA/MA Kelas XII (Budi Permana dkk.) — 6 Bab |

Total **197 file**, **~44.000 baris** dokumen siap pakai.

---

## 📁 Struktur Direktori

```
kerja_2026-2027/
├── administrasi_guru_kelas_X/          # Kelas X — Fase E
│   ├── 00_COVER.md
│   ├── 01_ANALISIS_ALOKASI_WAKTU.md
│   ├── 01b_RPE_Rincian_Pekan_Efektif.md
│   ├── 02_PROTA.md                     # Program Tahunan
│   ├── 03_PROSEM.md                    # Program Semester
│   ├── 04_ATP.md                       # Alur Tujuan Pembelajaran
│   ├── 05_KKTP.md                      # Kriteria Ketercapaian Tujuan Pembelajaran
│   ├── 06_PEMETAAN_KOMPETENSI_PENILAIAN.md
│   ├── 06b_BANK_SOAL.md
│   ├── 06c_PROGRAM_KOKURIKULER_8_DIMENSI.md
│   ├── 07_JURNAL_MENGAJAR.md
│   ├── 08_ANALISIS_CP_TP.md
│   ├── 09_DAFTAR_NILAI.md
│   ├── 10_PROGRAM_REMEDIAL_PENGAYAAN.md
│   ├── 11_INVENTARIS_LAB.md
│   ├── 12_JADWAL_LAB_BUKU_PRAKTIK.md
│   ├── generate_x.py                   # Generator dokumen admin
│   ├── Materi/
│   │   ├── Bab_1_Informatika_dan_Keterampilan_Generik.md
│   │   ├── ...
│   │   └── generate_materi_x.py
│   └── modul_ajar/
│       ├── Modul_Ajar_00_Pengenalan_Kontrak_Belajar.md
│       ├── Modul_Ajar_01_BK_Dekomposisi.md
│       ├── ... (33 modul ajar + PTS, PAT, Review)
│       └── Review_02_Review_Semester_2.md
│
├── administrasi_guru_kelas_XI/         # Kelas XI — Fase F
│   ├── (struktur sama seperti di atas)
│   ├── generate_xi.py
│   └── modul_ajar/
│       ├── Modul_Ajar_01_Bab1_Pengantar_8_Elemen.md
│       ├── ... (40 modul ajar + PTS, PAT, Review)
│       └── Review_02_Review_Semester_2.md
│
├── administrasi_guru_kelas_XII/        # Kelas XII — Fase F
│   ├── (struktur sama seperti di atas)
│   ├── generate_xii.py
│   └── modul_ajar/
│       ├── 1.01_Konsep_Literasi_Digital_dan_Etika_Bermedia_Digital.md
│       ├── ... (40 modul ajar + PTS, PAT, Review)
│       └── Modul_Ajar_6.08_Presentasi_Proyek_dan_Refleksi.md
│
└── README.md
```

---

## 📋 Dokumen per Kelas

### Root Dokumen (16 file per kelas)

| # | File | Deskripsi |
|---|------|-----------|
| 00 | `COVER` | Cover administrasi guru |
| 01 | `ANALISIS_ALOKASI_WAKTU` | Analisis alokasi waktu dan jam efektif |
| 01b | `RPE` | Rincian Pekan Efektif |
| 02 | `PROTA` | Program Tahunan |
| 03 | `PROSEM` | Program Semester (Ganjil & Genap) |
| 04 | `ATP` | Alur Tujuan Pembelajaran |
| 05 | `KKTP` | Kriteria Ketercapaian TP |
| 06 | `PEMETAAN` | Pemetaan Kompetensi & Penilaian |
| 06b | `BANK_SOAL` | Bank Soal |
| 06c | `KOKURIKULER` | Program Kokurikuler 8 Dimensi Profil Lulusan |
| 07 | `JURNAL` | Jurnal Mengajar |
| 08 | `ANALISIS_CP_TP` | Analisis CP & TP |
| 09 | `DAFTAR_NILAI` | Daftar Nilai Peserta Didik |
| 10 | `REMEDIAL` | Program Remedial & Pengayaan |
| 11 | `INVENTARIS_LAB` | Inventaris Laboratorium Komputer |
| 12 | `JADWAL_LAB` | Jadwal Lab & Buku Praktik |

### Modul Ajar

| Kelas | Jumlah Modul | Pembagian |
|-------|:-----------:|-----------|
| X | 33 | 00 (pengenalan) + 1-32 (Bab 1-9) |
| XI | 40 | 01-40 (Bab 1-6) |
| XII | 40 | 1.01-6.08 (Bab 1-6) |

Setiap kelas juga dilengkapi:
- **PTS Ganjil** — Penilaian Tengah Semester
- **PAT Genap** — Penilaian Akhir Tahun
- **Review Semester 1** — Review Bab ganjil
- **Review Semester 2** — Review Bab genap

---

## 🚀 Generator Script

Setiap kelas memiliki generator Python untuk membuat ulang dokumen root administrasi:

```bash
# Kelas X
cd administrasi_guru_kelas_X
python3 generate_x.py

# Kelas XI
cd administrasi_guru_kelas_XI
python3 generate_xi.py

# Kelas XII
cd administrasi_guru_kelas_XII
python3 generate_xii.py
```

Generator materi juga tersedia di masing-masing folder `Materi/`:

```bash
cd administrasi_guru_kelas_X/Materi
python3 generate_materi_x.py
```

> **Catatan:** Modul ajar bersifat statis (.md) dan tidak dihasilkan dari script — diedit langsung.

---

## 🎯 Fitur

- **8 Dimensi Profil Lulusan** — menggantikan P5 (Profil Pelajar Pancasila) sesuai kebijakan Deep Learning 2025/2026
- **Konten menarik** — dilengkapi analogi, diagram ASCII, contoh nyata, dan studi kasus
- **Rubrik 4 level** — deskripsi konkret untuk setiap level pencapaian
- **LKPD original** — soal dan tugas relevan, spesifik per topik
- **Diferensiasi** — aktivitas untuk peserta didik dengan kesulitan belajar dan yang perlu pengayaan
- **Refleksi** — lembar refleksi untuk peserta didik dan guru

---

## 🌐 Web (GitHub Pages)

Web statis responsif dengan tema portal pemerintah, bisa diakses di:

```
https://natedekaka.github.io/kerja_2026-2027/
```

Fitur: dark mode, search, animasi, back-to-top, mobile hamburger, progress bar, tim MGMP.

---

## 👤 Identitas MGMP

| | |
|---|---|
| Ketua MGMP | **Raden Hana Amalia, ST.** |
| Sekretaris | **Daniarsyah, S.Kom.** |
| Anggota | Lingga Oktaviani, S.Kom. |
| Anggota | Razzib Zabbal Noor, S.Kom. |
| Anggota | Edi Kusnadi, M.Pd. |
| Anggota | Muharima Rasyid Noor, S.St. |
| Sekolah | SMA Negeri 6 Cimahi |
| Tahun Pelajaran | 2026/2027 |

---

## 🛠 Teknologi

- Markdown (.md) — dokumen utama
- Python 3 — generator script + converter web
- Git + GitHub — version control
- GitHub Pages — hosting web statis

---

*Dokumen ini dikelola oleh MGMP Informatika SMA Negeri 6 Cimahi dan diperuntukkan bagi seluruh guru Informatika di lingkungan sekolah.*
