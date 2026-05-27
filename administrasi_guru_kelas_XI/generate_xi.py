#!/usr/bin/env python3
"""
Generator dokumen administrasi Guru Kelas XI — Informatika Fase F (5 JP/minggu)
Buku: Informatika untuk SMA/MA Kelas XI (Edisi Revisi)
Kemendikdasmen, Tahun Pelajaran 2026/2027

16 root documents:
  - Cover, Analisis Waktu, RPE, PROTA, PROSEM, ATP, KKTP
  - Pemetaan, Bank Soal, Kokurikuler, Jurnal, Analisis CP-TP
  - Daftar Nilai, Remedial, Inventaris Lab, Jadwal Lab
"""

import os

BASE = os.path.dirname(os.path.abspath(__file__))

GURU = "Daniarsyah, S.Kom."
NIP = "198004052022211004"
GOL = "IX"
SEKOLAH = "SMA Negeri 6 Cimahi"
MAPEL = "Informatika"
KELAS = "XI"
TP = "2026/2027"

# CP Fase F — 8 Elemen
CP_ELEMEN = {
    "BK": "Berpikir Komputasional",
    "TIK": "Teknologi Informasi dan Komunikasi",
    "SK": "Sistem Komputer",
    "JKI": "Jaringan Komputer dan Internet",
    "AD": "Analisis Data",
    "AP": "Algoritma dan Pemrograman",
    "DSI": "Dampak Sosial Informatika",
    "PLB": "Praktik Lintas Bidang",
}

# CP Teks per elemen (Fase F)
CP_TEKS = {
    "BK": "Peserta didik mampu menganalisis beberapa strategi algoritmik secara kritis untuk menghasilkan banyak alternatif solusi dari satu persoalan dengan memberikan justifikasi efisiensi, kelebihan, dan keterbatasan dari setiap alternatif solusi, kemudian memilih dan menerapkan solusi terbaik, paling efisien, dan optimal dengan merancang struktur data yang lebih kompleks dan abstrak.",
    "TIK": "Peserta didik mampu memahami penggunaan mesin pencari untuk riset; mengevaluasi kebenaran konten menggunakan verifikasi teks, gambar, dan video; membaca lateral; merancang kebutuhan sistem komputer; memahami konfigurasi keamanan lanjut; mengkreasi konten digital; memahami hukum & perundang-undangan digital; memahami pemanfaatan platform lokapasar, perbankan & dompet digital.",
    "SK": "Peserta didik mampu menghasilkan prototipe perangkat lunak yang berinteraksi dengan single board computer/controller atau kit elektronika untuk edukasi yang bisa diprogram, serta mengomunikasikan produk dan proses pengembangannya.",
    "JKI": "Peserta didik mampu memahami konsep lanjutan jaringan komputer dan internet meliputi topologi jaringan, OSI Layer, komponen jaringan, mekanisme pertukaran data, cyber security, tata kelola kontrol akses data, serta faktor-faktor dan konfigurasi keamanan jaringan.",
    "AD": "Peserta didik mampu memanfaatkan sumber data yang legal, terbuka, terpercaya guna mengolah data untuk pengambilan keputusan dan prediksi secara efektif, efisien, dan optimal tanpa atau dengan komputer.",
    "AP": "Peserta didik mampu mengembangkan program modular yang berukuran besar menggunakan bahasa pemrograman yang ditentukan; memahami, memelihara, dan menyempurnakan struktur program (aspek statik) dan eksekusi (aspek dinamik) suatu source code; memahami algoritma standar dan strategi efisiensinya; merancang dan mengimplementasikan struktur data abstrak yang kompleks seperti beberapa library standar termasuk library untuk AI dan library untuk pengolahan data bervolume besar; serta menerjemahkan program antar bahasa.",
    "DSI": "Peserta didik mampu mengkaji, menganalisis, dan memberikan berbagai argumentasi dan rasional secara kritis pada kasus-kasus sosial terkini terkait produk TIK dan sistem komputasi.",
    "PLB": "Peserta didik mampu bergotong royong dalam tim inklusif untuk mengerjakan projek pengembangan sistem komputasi dengan menganalisis dan mengidentifikasi persoalan, merancang, mengimplementasi, menguji, dan menyempurnakan sistem komputasi, serta mengomunikasikan produk dan proses pengembangannya.",
}

# 8 Dimensi Profil Lulusan
DIMENSI = [
    ("Keimanan & Ketakwaan", "Berakhlak mulia, etika digital, toleransi"),
    ("Kewargaan", "Cinta tanah air, kesadaran berbangsa, kontribusi sosial"),
    ("Penalaran Kritis", "Menganalisis, mengevaluasi, justifikasi"),
    ("Kreativitas", "Menghasilkan gagasan & karya orisinal"),
    ("Kolaborasi", "Kerja tim, kepemimpinan, inklusif"),
    ("Kemandirian", "Inisiatif, regulasi diri, tanggung jawab"),
    ("Kesehatan", "Kebugaran, manajemen waktu layar, ergonomi"),
    ("Komunikasi", "Presentasi, dokumentasi, argumen"),
]

# BAB info — 5 JP/pertemuan, 200 JP/tahun
BAB = {
    "1": {
        "judul": "Tentang Informatika",
        "jp": 15, "smt": 1,
        "cp": ["BK", "TIK", "DSI", "PLB"],
        "sub": [
            "Pengantar Informatika kelas XI; 8 elemen Informatika; kaitan antar elemen",
            "STEAM dalam Informatika; Profesi & karier bidang Informatika",
            "PLB: Aplikasi Informatika dalam berbagai bidang",
        ],
        "deskripsi": "Membahas 8 elemen Informatika, kaitannya dengan STEAM, profesi IT, dan praktik lintas bidang."
    },
    "2": {
        "judul": "Strategi Algoritmik dan Pemrograman",
        "jp": 55, "smt": 1,
        "cp": ["AP", "BK", "PLB"],
        "sub": [
            "Proses pemrograman: analisis masalah → perancangan → implementasi → pengujian",
            "Berpikir komputasional: Algoritma — efisiensi, efektivitas, optimalitas",
            "Rekursi: konsep, fungsi rekursif, contoh faktorial & deret",
            "Rekursi: implementasi dalam Python; perbandingan iteratif vs rekursif",
            "Greedy: konsep, karakteristik, contoh masalah (koin, jadwal)",
            "Greedy: implementasi — coin change, activity selection",
            "Dinamis: konsep pemrograman dinamis, overlapping subproblems",
            "Dinamis: implementasi — fibonacci, knapsack dasar",
            "Array & String: operasi lanjutan, sorting, searching",
            "Manipulasi String: pattern matching, palindrom, anagram",
            "PLB Kimia: simulasi reaksi kimia / PLB Fisika: simulasi gerak",
            "PLB Biologi: simulasi pertumbuhan populasi / analisis data genetika sederhana",
        ],
        "deskripsi": "Mempelajari strategi algoritmik: rekursi, greedy, pemrograman dinamis; struktur data array & string; dan PLB sains."
    },
    "3": {
        "judul": "Berpikir Kritis dan Dampak Sosial Informatika",
        "jp": 20, "smt": 1,
        "cp": ["DSI", "TIK"],
        "sub": [
            "Berpikir Kritis: literasi digital lanjutan, verifikasi teks, gambar, video",
            "Membaca Lateral: evaluasi informasi digital kompleks, riset dengan mesin pencari",
            "Dampak Sosial Informatika: analisis kasus terkini (hoaks, cyberbullying, privasi)",
            "Debat & Evaluasi: argumentasi kritis dampak TIK; literasi demokrasi digital",
        ],
        "deskripsi": "Menerapkan berpikir kritis, verifikasi informasi, dan menganalisis dampak sosial TIK."
    },
    "4": {
        "judul": "Jaringan Komputer dan Internet",
        "jp": 25, "smt": 2,
        "cp": ["JKI", "SK"],
        "sub": [
            "Pengantar jaringan komputer; sejarah, manfaat, jenis jaringan",
            "Topologi jaringan (star, bus, ring, mesh, hybrid); perangkat jaringan",
            "OSI Layer (7 layer) & TCP/IP; enkapsulasi data",
            "Mekanisme pertukaran data; IP address, routing, DNS",
            "Cyber Security: ancaman (malware, phishing, DDoS), kriptografi",
            "Tata kelola akses data; konfigurasi firewall, VPN, autentikasi",
            "Praktik: simulasi jaringan dengan Cisco Packet Tracer",
        ],
        "deskripsi": "Memahami jaringan komputer, OSI Layer, pertukaran data, cyber security, dan konfigurasi jaringan."
    },
    "5": {
        "judul": "Pengembangan Aplikasi Mobile dengan Library AI",
        "jp": 35, "smt": 2,
        "cp": ["AP", "SK", "PLB"],
        "sub": [
            "Pengantar aplikasi: web apps, desktop apps, mobile apps; perbandingan platform",
            "App Inventor: UI designer, komponen dasar, event handling",
            "App Inventor: navigasi antar screen, variabel, prosedur",
            "App Inventor: penyimpanan data lokal (TinyDB), integrasi sensor",
            "Library AI: pengenalan AI — machine learning, computer vision, NLP",
            "Image Classification: menggunakan library AI (ML Kit / TensorFlow Lite)",
            "Text/Speech Recognition: integrasi library AI dalam aplikasi mobile",
            "Proyek: Perencanaan aplikasi mobile berbasis AI (analisis, desain)",
            "Proyek: Implementasi aplikasi mobile berbasis AI",
            "Proyek: Presentasi & demonstrasi aplikasi mobile",
        ],
        "deskripsi": "Mengembangkan aplikasi mobile dengan App Inventor dan mengintegrasikan library AI."
    },
    "6": {
        "judul": "Proyek Analisis Data",
        "jp": 30, "smt": 2,
        "cp": ["AD", "PLB"],
        "sub": [
            "Big Data: pengertian, karakteristik (Volume, Velocity, Variety), sumber data",
            "Pengolahan Data: web scraping, data cleaning, transformasi data",
            "Visualisasi Data: dashboard, grafik infografis, interpretasi",
            "Proyek 'Hutanku': analisis data lingkungan, desain solusi komputasi",
            "Proyek 'Hutanku': implementasi & presentasi",
        ],
        "deskripsi": "Menganalisis data bervolume besar, visualisasi, dan proyek analisis data lingkungan 'Hutanku'."
    },
}


# =========== 16 ROOT DOCUMENTS ===========

def cover():
    """00_COVER.md"""
    return f"""# ADMINISTRASI GURU INFORMATIKA

## KELAS XI (FASE F) — TAHUN PELAJARAN 2026/2027

---

**MATA PELAJARAN** : Informatika  
**KELAS / FASE** : XI (Sebelas) / Fase F  
**JUMLAH JP** : 5 JP per minggu  
**TAHUN PELAJARAN** : 2026/2027  
**BUKU SUMBER** : Informatika untuk SMA/MA Kelas XI (Edisi Revisi) — Kemendikdasmen RI  
**LINK BUKU** : https://buku.kemendikdasmen.go.id/katalog/informatika-untuk-smama-kelas-xi-edisi-revisi

---

### IDENTITAS GURU

| | |
|---|---|
| Nama Guru | : Daniarsyah, S.Kom. |
| NIP / NUPTK | : 198004052022211004 |
| Pangkat / Gol. | : Guru Ahli Pertama / IX |
| Unit Kerja | : SMA Negeri 6 Cimahi |
| Alamat Sekolah | : Jalan Melong Raya No. 172 Cijerah — Cimahi Selatan |
| Provinsi | : Jawa Barat |

---

### DOKUMEN ADMINISTRASI

| No | Dokumen | Keterangan |
|---|---|---|
| 1 | Analisis Alokasi Waktu | 44 minggu efektif, 200 JP/tahun |
| 2 | RPE (Rincian Pekan Efektif) | Per semester × 22 minggu efektif |
| 3 | PROTA (Program Tahunan) | 8 elemen, 6 bab, 200 JP |
| 4 | PROSEM (Program Semester) | Rincian mingguan 5 JP |
| 5 | ATP (Alur Tujuan Pembelajaran) | 25 TP, 8 elemen Fase F |
| 6 | KKTP (Kriteria Ketercapaian TP) | Rubrik penilaian per TP |
| 7 | Pemetaan Kompetensi & Penilaian | Teknik & instrumen penilaian |
| 8 | Bank Soal | Diagnostik, formatif, PTS, PAS, PAT |
| 9 | Program Kokurikuler 8 Dimensi | Integrasi deep learning |
| 10 | Jurnal Mengajar | Jurnal harian 5 JP |
| 11 | Analisis CP → TP | Tracing CP ke TP |
| 12 | Daftar Nilai | Nilai per TP & per elemen |
| 13 | Program Remedial & Pengayaan | Remedial TP <65, pengayaan >85 |
| 14 | Inventaris Lab Komputer | Perlengkapan laboratorium |
| 15 | Jadwal Lab & Buku Praktik | Jadwal penggunaan lab + log |
| 16–48 | Modul Ajar (33 file) | RPP lengkap per pertemuan (5 JP) |

---

> **Profil Lulusan 8 Dimensi** (Kemendikdasmen, 2025) — P5 resmi diintegrasikan ke dalam pembelajaran mendalam (deep learning) sebagai program kokurikuler.

---

Mengetahui,  
Kepala Sekolah

_________________________

Guru Mata Pelajaran,

Daniarsyah, S.Kom.
NIP. 198004052022211004

_________________________
"""


def analisis_alokasi_waktu():
    """01_ANALISIS_ALOKASI_WAKTU.md"""
    return f"""# ANALISIS ALOKASI WAKTU

**Mata Pelajaran** : Informatika  
**Kelas / Fase** : XI (Sebelas) / Fase F  
**Tahun Pelajaran** : 2026/2027  
**Jumlah JP per Minggu** : 5 JP (1 JP = 45 menit)  

---

## A. PERHITUNGAN MINGGU EFEKTIF

### Semester 1 (Ganjil) — 2026

| No | Bulan | Jumlah Minggu | Minggu Efektif | Keterangan |
|---|---|---|---|---|
| 1 | Juli 2026 | 4 | 3 | MPLS (1 minggu) |
| 2 | Agustus 2026 | 5 | 5 | — |
| 3 | September 2026 | 4 | 4 | — |
| 4 | Oktober 2026 | 4 | 3 | PTS (1 minggu) |
| 5 | November 2026 | 4 | 4 | — |
| 6 | Desember 2026 | 4 | 3 | PAS (1 minggu + libur) |
| | **Jumlah** | **25** | **22** | |

### Semester 2 (Genap) — 2027

| No | Bulan | Jumlah Minggu | Minggu Efektif | Keterangan |
|---|---|---|---|---|
| 1 | Januari 2027 | 5 | 5 | — |
| 2 | Februari 2027 | 4 | 4 | — |
| 3 | Maret 2027 | 4 | 3 | PTS (1 minggu) |
| 4 | April 2027 | 4 | 4 | — |
| 5 | Mei 2027 | 4 | 4 | — |
| 6 | Juni 2027 | 5 | 2 | PAT + libur (3 minggu) |
| | **Jumlah** | **26** | **22** | |

---

## B. ALOKASI JP PER SEMESTER

| Komponen | Semester 1 | Semester 2 | Total |
|---|---|---|---|
| Minggu Efektif | 22 | 22 | 44 |
| JP per Minggu | 5 | 5 | 5 |
| **Total JP Pembelajaran** | **110** | **110** | **220** |
| PTS | (2 JP × 2) 4 | (2 JP × 2) 4 | 8 |
| PAS / PAT | 6 | 6 | 12 |
| **Total JP Efektif** | **100** | **100** | **200** |

---

## C. DISTRIBUSI JP PER BAB

### Semester 1 (Ganjil)

| Bab | Materi | Elemen | Alokasi JP |
|---|---|---|---|
| 1 | Tentang Informatika (8 elemen, STEAM, profesi IT) | BK, TIK, DSI | 15 |
| 2 | Strategi Algoritmik dan Pemrograman | AP, BK, PLB | 55 |
| 3 | Berpikir Kritis dan Dampak Sosial Informatika | DSI, TIK | 20 |
| | **Review & PTS** | — | 10 |
| | **Total Semester 1** | | **100** |

### Semester 2 (Genap)

| Bab | Materi | Elemen | Alokasi JP |
|---|---|---|---|
| 4 | Jaringan Komputer dan Internet | JKI, SK | 25 |
| 5 | Pengembangan Aplikasi Mobile dengan Library AI | AP, SK | 35 |
| 6 | Proyek Analisis Data "Hutanku Dulu, Kini, dan Akan Datang" | AD, PLB | 30 |
| | **Review & PAS/PAT** | — | 10 |
| | **Total Semester 2** | | **100** |

| **Total JP Efektif (1 Tahun)** | | | **200** |

---

Mengetahui,  
Kepala Sekolah

_________________________

Guru Mata Pelajaran,

Daniarsyah, S.Kom.
NIP. 198004052022211004

_________________________
"""


def rpe():
    """01b_RPE_Rincian_Pekan_Efektif.md"""
    return f"""# RINCIAN PEKAN EFEKTIF (RPE)

**Mata Pelajaran** : Informatika  
**Kelas / Fase** : XI (Sebelas) / Fase F  
**Tahun Pelajaran** : 2026/2027  
**Jumlah JP per Minggu** : 5 JP  

---

## SEMESTER 1 (GANJIL) — 2026/2027

| No | Bulan | Minggu ke- | JP | Kegiatan |
|---|---|---|---|---|
| 1 | Juli | 1 | 5 | MPLS — Pengenalan Lingkungan Sekolah |
| 2 | Juli | 2 | 5 | Bab 1: Tentang Informatika — Pengantar & 8 Elemen |
| 3 | Juli | 3 | 5 | Bab 1: STEAM & Profesi Bidang Informatika |
| 4 | Juli | 4 | 5 | Bab 1: Praktik Lintas Bidang — Aplikasi Informatika |
| 5 | Agustus | 1 | 5 | Bab 2: Proses Pemrograman & Analisis Masalah |
| 6 | Agustus | 2 | 5 | Bab 2: Perancangan Solusi & Algoritma |
| 7 | Agustus | 3 | 5 | Bab 2: Implementasi — Coding Dasar |
| 8 | Agustus | 4 | 5 | Bab 2: Pengujian & Debugging |
| 9 | Agustus | 5 | 5 | Bab 2: Rekursi — Konsep & Implementasi |
| 10 | September | 1 | 5 | Bab 2: Algoritma Greedy — Teori & Contoh |
| 11 | September | 2 | 5 | Bab 2: Greedy — Implementasi Program |
| 12 | September | 3 | 5 | Bab 2: Pemrograman Dinamis — Konsep |
| 13 | September | 4 | 5 | Bab 2: Pemrograman Dinamis — Implementasi |
| 14 | Oktober | 1 | 5 | Bab 2: Struktur Data — Array & String |
| 15 | Oktober | 2 | 5 | Bab 2: Manipulasi String Lanjutan |
| 16 | Oktober | 3 | 5 | **PTS — Ujian Tengah Semester** |
| 17 | Oktober | 4 | 5 | Bab 2: PLB — Penerapan dalam Kimia & Fisika |
| 18 | November | 1 | 5 | Bab 2: PLB — Penerapan dalam Biologi |
| 19 | November | 2 | 5 | Bab 3: Berpikir Kritis — Literasi Digital Lanjutan |
| 20 | November | 3 | 5 | Bab 3: Verifikasi Informasi & Membaca Lateral |
| 21 | November | 4 | 5 | Bab 3: Dampak Sosial Informatika — Kasus Terkini |
| 22 | Desember | 1 | 5 | Bab 3: Debat/Evaluasi Dampak TIK |
| 23 | Desember | 2 | 5 | Review Semester 1 |
| 24 | Desember | 3 | 5 | **PAS — Penilaian Akhir Semester** |
| 25 | Desember | 4 | — | **Libur Semester 1** |

## SEMESTER 2 (GENAP) — 2026/2027

| No | Bulan | Minggu ke- | JP | Kegiatan |
|---|---|---|---|---|
| 1 | Januari | 1 | 5 | Bab 4: Pengantar Jaringan Komputer — Konsep |
| 2 | Januari | 2 | 5 | Bab 4: Topologi Jaringan & Perangkat |
| 3 | Januari | 3 | 5 | Bab 4: OSI Layer & Model TCP/IP |
| 4 | Januari | 4 | 5 | Bab 4: Mekanisme Pertukaran Data |
| 5 | Januari | 5 | 5 | Bab 4: Cyber Security — Ancaman & Proteksi |
| 6 | Februari | 1 | 5 | Bab 4: Tata Kelola Akses Data & Konfigurasi Keamanan |
| 7 | Februari | 2 | 5 | Bab 5: Pengantar Aplikasi Mobile — Web vs Desktop vs Mobile |
| 8 | Februari | 3 | 5 | Bab 5: App Inventor — Dasar & UI Design |
| 9 | Februari | 4 | 5 | Bab 5: App Inventor — Event Handling & Navigasi |
| 10 | Maret | 1 | 5 | Bab 5: App Inventor — Penyimpanan Data Lokal |
| 11 | Maret | 2 | 5 | Bab 5: Library AI — Pengenalan & Integrasi |
| 12 | Maret | 3 | 5 | **PTS — Ujian Tengah Semester** |
| 13 | Maret | 4 | 5 | Bab 5: AI — Image Classification dengan Library |
| 14 | April | 1 | 5 | Bab 5: AI — Text/Speech Recognition |
| 15 | April | 2 | 5 | Bab 5: Proyek Aplikasi Mobile — Perencanaan |
| 16 | April | 3 | 5 | Bab 5: Proyek Aplikasi Mobile — Implementasi |
| 17 | April | 4 | 5 | Bab 5: Proyek Aplikasi Mobile — Presentasi |
| 18 | Mei | 1 | 5 | Bab 6: Analisis Data — Big Data & Sumber Data |
| 19 | Mei | 2 | 5 | Bab 6: Pengolahan Data Bervolume Besar |
| 20 | Mei | 3 | 5 | Bab 6: Visualisasi Data & Interpretasi |
| 21 | Mei | 4 | 5 | Bab 6: Proyek "Hutanku" — Analisis & Desain |
| 22 | Juni | 1 | 5 | Bab 6: Proyek "Hutanku" — Implementasi & Presentasi |
| 23 | Juni | 2 | 5 | Review Semester 2 |
| 24 | Juni | 3 | 5 | **PAT — Penilaian Akhir Tahun** |
| 25 | Juni | 4 | — | **Libur Semester 2** |

---

Mengetahui,  
Kepala Sekolah

_________________________

Guru Mata Pelajaran,

Daniarsyah, S.Kom.
NIP. 198004052022211004

_________________________
"""


def prota():
    """02_PROTA.md"""
    return f"""# PROGRAM TAHUNAN (PROTA)

**Mata Pelajaran** : Informatika  
**Kelas / Fase** : XI (Sebelas) / Fase F  
**Tahun Pelajaran** : 2026/2027  
**Jumlah JP per Minggu** : 5 JP (1 JP = 45 menit)  

---

## A. CAPAIAN PEMBELAJARAN (CP) FASE F

Pada akhir fase F, peserta didik mengintegrasikan elemen-elemen dan mampu mengkaji berbagai strategi algoritmik yang menghasilkan lebih dari satu solusi persoalan, menganalisis setiap solusi, serta menentukan solusi yang paling efisien dan optimal untuk dikembangkan menjadi program komputer; mengkritisi kasus-kasus terkini terkait Informatika di masyarakat; merancang dan mengimplementasi struktur data abstrak yang lebih kompleks menggunakan beberapa library standar termasuk library untuk kecerdasan buatan (AI) dan library untuk pengolahan data bervolume besar; mengembangkan, melakukan pemeliharaan, dan penyempurnaan kode sumber program; memahami jaringan komputer dari sisi teknis termasuk keamanan siber (cyber security); bergotong royong untuk merancang, mengimplementasi, menguji, dan menghasilkan prototipe perangkat lunak; serta mengomunikasikan produk dan proses pengembangannya.

## B. CP PER ELEMEN

| No | Elemen | Capaian Pembelajaran |
|---|---|---|
| 1 | **BK** (Berpikir Komputasional) | Menganalisis beberapa strategi algoritmik secara kritis untuk menghasilkan banyak alternatif solusi, memberikan justifikasi efisiensi, kelebihan, dan keterbatasan; memilih solusi terbaik dengan struktur data kompleks & abstrak. |
| 2 | **TIK** (Teknologi Informasi & Komunikasi) | Memahami pemanfaatan platform digital; mengevaluasi kebenaran konten; mengkreasi konten digital; memahami hukum & etika digital. |
| 3 | **SK** (Sistem Komputer) | Menghasilkan prototipe perangkat lunak yang berinteraksi dengan single board computer/controller/kit elektronika yang bisa diprogram. |
| 4 | **JKI** (Jaringan Komputer & Internet) | Memahami OSI Layer, topologi jaringan, mekanisme pertukaran data, cyber security, tata kelola akses data, konfigurasi keamanan. |
| 5 | **AD** (Analisis Data) | Memanfaatkan sumber data legal & terpercaya untuk pengolahan data bervolume besar guna pengambilan keputusan dan prediksi. |
| 6 | **AP** (Algoritma & Pemrograman) | Mengembangkan program modular; memahami, memelihara, dan menyempurnakan source code; merancang struktur data abstrak; menggunakan library standar termasuk AI dan big data; menerjemahkan program antar bahasa. |
| 7 | **DSI** (Dampak Sosial Informatika) | Mengkaji, menganalisis, dan memberikan argumentasi kritis pada kasus-kasus sosial terkini terkait produk TIK dan sistem komputasi. |
| 8 | **PLB** (Praktik Lintas Bidang) | Bergotong royong dalam tim inklusif untuk mengerjakan projek pengembangan sistem komputasi; mengomunikasikan produk & proses. |

## C. PEMETAAN MATERI & ALOKASI WAKTU

### Semester 1 (Ganjil) — 100 JP Efektif

| Bab | Materi Pokok | Elemen | JP | Minggu ke- |
|---|---|---|---|---|
| 1 | **Tentang Informatika** — 8 elemen, STEAM, profesi IT, PLB | BK, TIK, DSI | 15 | 2–4 |
| 2 | **Strategi Algoritmik & Pemrograman** — proses pemrograman, rekursi, greedy, dinamis, array, string, PLB | AP, BK, PLB | 55 | 5–14, 17–18 |
| 3 | **Berpikir Kritis & Dampak Sosial Informatika** — literasi digital, verifikasi, DSI | DSI, TIK | 20 | 19–22 |
| | Review & PTS | — | 10 | 16, 23 |
| | **Total Semester 1** | | **100** | |

### Semester 2 (Genap) — 100 JP Efektif

| Bab | Materi Pokok | Elemen | JP | Minggu ke- |
|---|---|---|---|---|
| 4 | **Jaringan Komputer & Internet** — OSI Layer, topologi, cyber security, akses data | JKI, SK | 25 | 1–7 |
| 5 | **Aplikasi Mobile dengan Library AI** — App Inventor, AI library, image/speech recognition | AP, SK | 35 | 8–18 |
| 6 | **Proyek Analisis Data** — big data, pengolahan, visualisasi, proyek "Hutanku" | AD, PLB | 30 | 19–23 |
| | Review & PAS/PAT | — | 10 | 24–25 |
| | **Total Semester 2** | | **100** | |

| **Total JP Efektif 1 Tahun** | | **200** | |

## D. RINCIAN JP PER ELEMEN

| Elemen | JP |
|---|---|
| Berpikir Komputasional (BK) | 25 |
| Teknologi Informasi & Komunikasi (TIK) | 15 |
| Sistem Komputer (SK) | 15 |
| Jaringan Komputer & Internet (JKI) | 20 |
| Analisis Data (AD) | 25 |
| Algoritma & Pemrograman (AP) | 55 |
| Dampak Sosial Informatika (DSI) | 15 |
| Praktik Lintas Bidang (PLB) | 20 |
| Review & Ujian | 10 |
| **Total** | **200** |

---

Mengetahui,  
Kepala Sekolah

_________________________

Guru Mata Pelajaran,

Daniarsyah, S.Kom.
NIP. 198004052022211004

_________________________
"""


def prosem():
    """03_PROSEM.md"""
    return f"""# PROGRAM SEMESTER (PROSEM)

**Mata Pelajaran** : Informatika  
**Kelas / Fase** : XI (Sebelas) / Fase F  
**Tahun Pelajaran** : 2026/2027  
**Jumlah JP per Minggu** : 5 JP (1 JP = 45 menit)  

---

## SEMESTER 1 (GANJIL) — Juli s.d. Desember 2026

| Minggu ke- | Bulan | Bab | Materi Pembelajaran | JP | Elemen |
|---|---|---|---|---|---|
| 1 | Juli | — | **MPLS** — Pengenalan Lingkungan Sekolah | — | — |
| 2 | Juli | 1 | Pengantar Informatika kelas XI; 8 elemen Informatika; kaitan antar elemen | 5 | BK, TIK |
| 3 | Juli | 1 | STEAM dalam Informatika; Profesi & karier bidang Informatika | 5 | BK, DSI |
| 4 | Juli | 1 | **Praktik Lintas Bidang (PLB)**: Aplikasi Informatika dalam berbagai bidang | 5 | PLB |
| 5 | Agustus | 2 | Proses pemrograman: analisis masalah → perancangan → implementasi → pengujian | 5 | AP |
| 6 | Agustus | 2 | Berpikir komputasional: Algoritma — efisiensi, efektivitas, optimalitas | 5 | BK, AP |
| 7 | Agustus | 2 | **Rekursi**: konsep, fungsi rekursif, contoh faktorial & deret | 5 | AP, BK |
| 8 | Agustus | 2 | **Rekursi**: implementasi dalam Python; perbandingan iteratif vs rekursif | 5 | AP |
| 9 | Agustus | 2 | **Greedy**: konsep, karakteristik, contoh masalah (koin, jadwal) | 5 | BK, AP |
| 10 | September | 2 | **Greedy**: implementasi — coin change, activity selection | 5 | AP |
| 11 | September | 2 | **Dinamis**: konsep pemrograman dinamis, overlapping subproblems | 5 | BK, AP |
| 12 | September | 2 | **Dinamis**: implementasi — fibonacci, knapsack dasar | 5 | AP |
| 13 | September | 2 | **Array & String**: operasi lanjutan, sorting, searching | 5 | AP |
| 14 | Oktober | 2 | **Manipulasi String**: pattern matching, palindrom, anagram | 5 | AP |
| 15 | Oktober | — | **Review** Bab 1–2 | 5 | — |
| 16 | Oktober | — | **PTS** — Penilaian Tengah Semester | 5 | — |
| 17 | Oktober | 2 | **PLB Kimia**: simulasi reaksi kimia dengan program / **PLB Fisika**: simulasi gerak | 5 | AP, PLB |
| 18 | November | 2 | **PLB Biologi**: simulasi pertumbuhan populasi / analisis data genetika sederhana | 5 | AP, PLB |
| 19 | November | 3 | **Berpikir Kritis**: literasi digital lanjutan, verifikasi teks, gambar, video | 5 | DSI, TIK |
| 20 | November | 3 | **Membaca Lateral**: evaluasi informasi digital kompleks, riset dengan mesin pencari | 5 | DSI, TIK |
| 21 | November | 3 | **Dampak Sosial Informatika**: analisis kasus terkini (hoaks, cyberbullying, privasi) | 5 | DSI |
| 22 | Desember | 3 | **Debat & Evaluasi**: argumentasi kritis dampak TIK; literasi demokrasi digital | 5 | DSI, TIK |
| 23 | Desember | — | **Review** Semester 1 (Bab 1–3) | 5 | — |
| 24 | Desember | — | **PAS** — Penilaian Akhir Semester | 5 | — |
| 25 | Desember | — | **Libur Semester 1** | — | — |

## SEMESTER 2 (GENAP) — Januari s.d. Juni 2027

| Minggu ke- | Bulan | Bab | Materi Pembelajaran | JP | Elemen |
|---|---|---|---|---|---|
| 1 | Januari | 4 | Pengantar jaringan komputer; sejarah, manfaat, jenis jaringan | 5 | JKI |
| 2 | Januari | 4 | Topologi jaringan (star, bus, ring, mesh, hybrid); perangkat jaringan | 5 | JKI, SK |
| 3 | Januari | 4 | OSI Layer (7 layer) & TCP/IP; enkapsulasi data | 5 | JKI |
| 4 | Januari | 4 | Mekanisme pertukaran data; IP address, routing, DNS | 5 | JKI |
| 5 | Januari | 4 | **Cyber Security**: ancaman (malware, phishing, DDoS), kriptografi | 5 | JKI |
| 6 | Februari | 4 | Tata kelola akses data; konfigurasi firewall, VPN, autentikasi | 5 | JKI, SK |
| 7 | Februari | 4 | **Praktik**: simulasi jaringan dengan Cisco Packet Tracer / konfigurasi dasar | 5 | JKI, SK |
| 8 | Februari | 5 | Pengantar aplikasi: web apps, desktop apps, mobile apps; perbandingan platform | 5 | AP |
| 9 | Februari | 5 | **App Inventor**: UI designer, komponen dasar, event handling | 5 | AP |
| 10 | Februari | 5 | **App Inventor**: navigasi antar screen, variabel, prosedur | 5 | AP |
| 11 | Maret | 5 | **App Inventor**: penyimpanan data lokal (TinyDB), integrasi sensor | 5 | AP |
| 12 | Maret | — | **PTS** — Penilaian Tengah Semester (Bab 4–5) | 5 | — |
| 13 | Maret | 5 | **Library AI**: pengenalan AI — machine learning, computer vision, NLP | 5 | AP, BK |
| 14 | April | 5 | **Image Classification**: menggunakan library AI (ML Kit / TensorFlow Lite) | 5 | AP |
| 15 | April | 5 | **Text/Speech Recognition**: integrasi library AI dalam aplikasi mobile | 5 | AP |
| 16 | April | 5 | **Proyek**: Perencanaan aplikasi mobile berbasis AI (analisis, desain) | 5 | AP, PLB |
| 17 | April | 5 | **Proyek**: Implementasi aplikasi mobile berbasis AI | 5 | AP, PLB |
| 18 | Mei | 5 | **Proyek**: Presentasi & demonstrasi aplikasi mobile | 5 | AP, PLB |
| 19 | Mei | 6 | **Big Data**: pengertian, karakteristik (Volume, Velocity, Variety), sumber data | 5 | AD |
| 20 | Mei | 6 | **Pengolahan Data**: web scraping, data cleaning, transformasi data | 5 | AD |
| 21 | Mei | 6 | **Visualisasi Data**: dashboard, grafik infografis, interpretasi | 5 | AD |
| 22 | Juni | 6 | **Proyek "Hutanku"**: analisis data lingkungan, desain solusi komputasi | 5 | AD, PLB |
| 23 | Juni | 6 | **Proyek "Hutanku"**: implementasi & presentasi | 5 | AD, PLB |
| 24 | Juni | — | **Review** Semester 2 (Bab 4–6) | 5 | — |
| 25 | Juni | — | **PAT** — Penilaian Akhir Tahun | 5 | — |
| 26 | Juni | — | **Libur Semester 2** | — | — |

---

Mengetahui,  
Kepala Sekolah

_________________________

Guru Mata Pelajaran,

Daniarsyah, S.Kom.
NIP. 198004052022211004

_________________________
"""


def atp():
    """04_ATP.md"""
    return f"""# ALUR TUJUAN PEMBELAJARAN (ATP)

**Mata Pelajaran** : Informatika  
**Kelas / Fase** : XI (Sebelas) / Fase F  
**Tahun Pelajaran** : 2026/2027  
**Jumlah JP per Minggu** : 5 JP  

---

## A. CAPAIAN PEMBELAJARAN FASE F

| Elemen | Capaian Pembelajaran |
|---|---|
| **BK** | Peserta didik mampu menganalisis beberapa strategi algoritmik secara kritis untuk menghasilkan banyak alternatif solusi dari satu persoalan dengan memberikan justifikasi efisiensi, kelebihan, dan keterbatasan dari setiap alternatif solusi, kemudian memilih dan menerapkan solusi terbaik, paling efisien, dan optimal dengan merancang struktur data yang lebih kompleks dan abstrak. |
| **TIK** | Peserta didik mampu memahami penggunaan mesin pencari untuk riset; mengevaluasi kebenaran konten menggunakan verifikasi teks, gambar, dan video; membaca lateral; merancang kebutuhan sistem komputer; memahami konfigurasi keamanan lanjut; mengkreasi konten digital; memahami hukum & perundang-undangan digital; memahami pemanfaatan platform lokapasar, perbankan & dompet digital. |
| **SK** | Peserta didik mampu menghasilkan prototipe perangkat lunak yang berinteraksi dengan single board computer/controller atau kit elektronika untuk edukasi yang bisa diprogram, serta mengomunikasikan produk dan proses pengembangannya. |
| **JKI** | Peserta didik mampu memahami konsep lanjutan jaringan komputer dan internet meliputi topologi jaringan, OSI Layer, komponen jaringan, mekanisme pertukaran data, cyber security, tata kelola kontrol akses data, serta faktor-faktor dan konfigurasi keamanan jaringan. |
| **AD** | Peserta didik mampu memanfaatkan sumber data yang legal, terbuka, terpercaya guna mengolah data untuk pengambilan keputusan dan prediksi secara efektif, efisien, dan optimal tanpa atau dengan komputer. |
| **AP** | Peserta didik mampu mengembangkan program modular yang berukuran besar menggunakan bahasa pemrograman yang ditentukan; memahami, memelihara, dan menyempurnakan struktur program (aspek statik) dan eksekusi (aspek dinamik) suatu source code; memahami algoritma standar dan strategi efisiensinya; merancang dan mengimplementasikan struktur data abstrak yang kompleks seperti beberapa library standar termasuk library untuk AI dan library untuk pengolahan data bervolume besar; serta menerjemahkan program antar bahasa. |
| **DSI** | Peserta didik mampu mengkaji, menganalisis, dan memberikan berbagai argumentasi dan rasional secara kritis pada kasus-kasus sosial terkini terkait produk TIK dan sistem komputasi. |
| **PLB** | Peserta didik mampu bergotong royong dalam tim inklusif untuk mengerjakan projek pengembangan sistem komputasi dengan menganalisis dan mengidentifikasi persoalan, merancang, mengimplementasi, menguji, dan menyempurnakan sistem komputasi, serta mengomunikasikan produk dan proses pengembangannya. |

---

## B. TUJUAN PEMBELAJARAN (TP) & ALUR

### Semester 1 — Bab 1: Tentang Informatika (15 JP)

| Kode TP | Elemen | CP | TP | Indikator Keberhasilan | Materi Pokok | Aktivitas | Dimensi Profil Lulusan | JP | Sumber |
|---|---|---|---|---|---|---|---|---|---|
| TP.1.1 | BK, TIK | F.1 | Menjelaskan pengertian, ruang lingkup, dan 8 elemen Informatika serta kaitannya dengan STEAM | Mengidentifikasi minimal 6 dari 8 elemen Informatika dengan contoh nyata | 8 elemen Informatika, STEAM | Diskusi interaktif & mind map elemen Informatika | Penalaran Kritis, Kewargaan | 5 | Buku Bab 1 |
| TP.1.2 | DSI | F.2 | Menganalisis profesi dan karier di bidang Informatika serta perannya dalam masyarakat digital | Menyebutkan 5+ profesi IT dan menjelaskan kualifikasinya | Profesi IT, karier digital, industri 4.0 | Riset profesi IT & presentasi kelompok | Kemandirian, Kewargaan | 5 | Buku Bab 1, Internet |
| TP.1.3 | PLB | F.8 | Menerapkan praktik lintas bidang dengan mengaitkan Informatika dan disiplin ilmu lain (Kimia, Fisika, Biologi) | Menghasilkan mind map/poster keterkaitan Informatika dengan 3+ bidang sains | Praktik lintas bidang, interdisiplin | Proyek kelompok: aplikasi Informatika di berbagai sains | Kolaborasi, Kreativitas | 5 | Buku Bab 1 |

### Semester 1 — Bab 2: Strategi Algoritmik & Pemrograman (55 JP)

| Kode TP | Elemen | CP | TP | Indikator Keberhasilan | Materi Pokok | Aktivitas | Dimensi Profil Lulusan | JP | Sumber |
|---|---|---|---|---|---|---|---|---|---|
| TP.2.1 | AP | F.6 | Menganalisis proses pemrograman: analisis masalah → perancangan → implementasi → pengujian & debugging | Menjelaskan 4 tahap proses pemrograman dengan contoh kasus | Proses pemrograman, analisis, desain, coding, testing | Studi kasus: alur pengembangan program | Penalaran Kritis | 5 | Buku Bab 2 |
| TP.2.2 | BK, AP | F.1, F.6 | Membedakan efisiensi, efektivitas, dan optimalitas algoritma serta memilih strategi terbaik | Membandingkan 2+ algoritma pada kasus yang sama berdasarkan kompleksitas | Efisiensi algoritma, kompleksitas waktu/ruang | Praktik: membandingkan algoritma sorting (bubble, merge, quick) | Penalaran Kritis | 5 | Buku Bab 2 |
| TP.2.3 | AP, BK | F.6 | Menerapkan rekursi untuk menyelesaikan persoalan dengan mendefinisikan base case dan recursive case | Menulis program rekursif (faktorial, deret, fibonacci) dengan benar | Rekursi, base case, rekurensi, stack rekursif | Coding: faktorial, fibonacci, deret menggunakan rekursi | Kreativitas, Kemandirian | 10 | Buku Bab 2, Komputer |
| TP.2.4 | AP, BK | F.1, F.6 | Menerapkan algoritma greedy untuk menyelesaikan masalah optimasi | Menyelesaikan masalah coin change / activity selection dengan greedy | Greedy: coin change, activity selection, knapsack fractional | Coding: coin change & activity selection dengan Python | Penalaran Kritis, Kreativitas | 10 | Buku Bab 2, Komputer |
| TP.2.5 | AP, BK | F.1, F.6 | Menerapkan pemrograman dinamis untuk persoalan dengan overlapping subproblems | Menyelesaikan fibonacci DP, knapsack 0/1 dasar | Pemrograman dinamis, memoization, tabulation | Coding: fibonacci (DP), knapsack 0/1 | Penalaran Kritis, Kreativitas | 10 | Buku Bab 2, Komputer |
| TP.2.6 | AP | F.6 | Menggunakan struktur data array dan string untuk manipulasi data lanjutan | Mengimplementasikan sorting, searching, pattern matching | Array multidimensi, string, pattern matching, sorting | Coding: manipulasi array & string, pattern search | Penalaran Kritis, Kemandirian | 5 | Buku Bab 2, Komputer |
| TP.2.7 | BK | F.1 | Membandingkan performa strategi algoritmik (rekursif vs iteratif, greedy vs DP) pada satu persoalan | Menulis laporan perbandingan efisiensi 2+ algoritma | Analisis perbandingan algoritma, justifikasi | Studi kasus & laporan perbandingan algoritma | Penalaran Kritis, Komunikasi | 5 | Buku Bab 2 |
| TP.2.8 | AP, PLB | F.6, F.8 | Mengembangkan program modular sebagai solusi persoalan nyata lintas bidang | Menghasilkan program Python (min. 100 baris) dengan struktur modular | Program modular, fungsi, PLB (Kimia/Fisika/Biologi) | Proyek: simulasi sains dengan program | Kolaborasi, Kreativitas, Kemandirian | 5 | Buku Bab 2, Komputer |

### Semester 1 — Bab 3: Berpikir Kritis & Dampak Sosial Informatika (20 JP)

| Kode TP | Elemen | CP | TP | Indikator Keberhasilan | Materi Pokok | Aktivitas | Dimensi Profil Lulusan | JP | Sumber |
|---|---|---|---|---|---|---|---|---|---|
| TP.3.1 | TIK | F.2 | Menerapkan teknik verifikasi informasi digital (teks, gambar, video) menggunakan mesin pencari dan alat verifikasi | Memverifikasi 3 informasi dengan metode yang tepat | Literasi digital, verifikasi, reverse image search | Praktik: verifikasi berita hoaks & deepfake | Penalaran Kritis | 5 | Buku Bab 3 |
| TP.3.2 | TIK | F.2 | Menggunakan metode membaca lateral untuk mengevaluasi keabsahan informasi digital yang kompleks | Menerapkan lateral reading pada 3 sumber informasi berbeda | Lateral reading, evaluasi sumber, riset digital | Praktik: lateral reading — membandingkan sumber | Penalaran Kritis, Kewargaan | 5 | Buku Bab 3 |
| TP.3.3 | DSI | F.7 | Menganalisis kasus-kasus dampak sosial TIK terkini (hoaks, cyberbullying, privasi, demokrasi digital) | Mengidentifikasi 5+ dampak sosial TIK dan memberikan solusi | Dampak sosial TIK, etika digital, UU ITE | Analisis kasus: hoaks politik, doxing, digital footprint | Keimanan & Ketakwaan, Kewargaan | 5 | Buku Bab 3, Berita |
| TP.3.4 | DSI | F.7 | Menyusun argumentasi kritis secara lisan dan tulisan tentang dampak TIK di masyarakat | Menulis esai 500+ kata dengan argumen pro-kontra didukung data | Argumen kritis, debat, literasi demokrasi digital | Debat kelas / esai analitis dampak TIK | Komunikasi, Kewargaan, Penalaran Kritis | 5 | Buku Bab 3 |

### Semester 2 — Bab 4: Jaringan Komputer & Internet (25 JP)

| Kode TP | Elemen | CP | TP | Indikator Keberhasilan | Materi Pokok | Aktivitas | Dimensi Profil Lulusan | JP | Sumber |
|---|---|---|---|---|---|---|---|---|---|
| TP.4.1 | JKI | F.4 | Menganalisis topologi jaringan, perangkat jaringan, serta jenis-jenis jaringan komputer | Menggambar topologi jaringan dan menjelaskan fungsi 7+ perangkat | Topologi (star, bus, ring, mesh, hybrid), perangkat (router, switch, dll) | Simulasi: desain topologi jaringan untuk lab sekolah | Penalaran Kritis | 5 | Buku Bab 4 |
| TP.4.2 | JKI | F.4 | Menjelaskan OSI Layer (7 layer) dan model TCP/IP serta mekanisme enkapsulasi data | Mendeskripsikan fungsi setiap layer OSI dengan analogi | OSI Layer, TCP/IP, enkapsulasi, paket data | Diagram enkapsulasi & simulasi pertukaran data | Penalaran Kritis | 5 | Buku Bab 4 |
| TP.4.3 | JKI, SK | F.4, F.3 | Menerapkan konfigurasi jaringan dasar (IP, routing, DNS) dan simulasi dengan Packet Tracer | Melakukan konfigurasi IP statis/dinamis & routing sederhana | IP address, subnetting, routing, DNS, DHCP | Praktik: Cisco Packet Tracer — konfigurasi jaringan | Kemandirian, Kolaborasi | 5 | Buku Bab 4, Komputer |
| TP.4.4 | JKI | F.4 | Menerapkan prinsip cyber security: identifikasi ancaman, kriptografi, enkripsi dasar | Mengenkripsi data sederhana dan menjelaskan 5+ jenis ancaman | Cyber security, malware, phishing, DDoS, kriptografi | Praktik: enkripsi Caesar, analisis kasus serangan siber | Keimanan & Ketakwaan, Penalaran Kritis | 5 | Buku Bab 4 |
| TP.4.5 | JKI, SK | F.4, F.3 | Menerapkan tata kelola akses data, firewall, VPN, dan autentikasi multi-faktor | Mengkonfigurasi firewall dasar dan menjelaskan 3+ metode autentikasi | Firewall, VPN, AAA, MFA, tata kelola akses | Simulasi: firewall rule, VPN setup, MFA demo | Kemandirian, Kewargaan | 5 | Buku Bab 4, Komputer |

### Semester 2 — Bab 5: Aplikasi Mobile dengan Library AI (35 JP)

| Kode TP | Elemen | CP | TP | Indikator Keberhasilan | Materi Pokok | Aktivitas | Dimensi Profil Lulusan | JP | Sumber |
|---|---|---|---|---|---|---|---|---|---|
| TP.5.1 | AP | F.6 | Membedakan jenis aplikasi (web, desktop, mobile) dan platform pengembangannya | Menjelaskan perbedaan & kelebihan masing-masing platform aplikasi | Web apps, desktop apps, mobile apps, cross-platform | Presentasi: perbandingan platform & studi kasus | Penalaran Kritis | 5 | Buku Bab 5 |
| TP.5.2 | AP | F.6 | Mengembangkan aplikasi mobile berbasis blok menggunakan App Inventor dengan fitur UI, navigasi, dan penyimpanan data | Membuat aplikasi mobile fungsional (min. 3 screen) dengan App Inventor | App Inventor: UI, komponen, event, navigasi, TinyDB | Praktik: aplikasi mobile sederhana (kalkulator/catatan) | Kreativitas, Kemandirian | 10 | Buku Bab 5, Komputer |
| TP.5.3 | AP | F.6 | Mengintegrasikan library kecerdasan buatan (AI) dalam aplikasi mobile | Menambahkan minimal 1 fitur AI ke dalam aplikasi App Inventor | AI library, ML Kit, TensorFlow Lite, API | Tutorial: integrasi image classifier ke App Inventor | Penalaran Kritis, Kreativitas | 5 | Buku Bab 5, Komputer |
| TP.5.4 | AP | F.6 | Menerapkan image classification dan/atau text/speech recognition menggunakan library AI | Mendemonstrasikan aplikasi dengan fitur AI recognition | Image classification, speech recognition, NLP | Praktik: aplikasi pengenal objek / suara | Kreativitas, Kemandirian | 5 | Buku Bab 5, Komputer |
| TP.5.5 | AP, PLB | F.6, F.8 | Menghasilkan prototipe aplikasi mobile berbasis AI sebagai solusi persoalan nyata | Menghasilkan aplikasi mobile + dokumentasi + presentasi | Proyek aplikasi AI: analisis, desain, coding, testing, demo | Proyek kelompok: aplikasi AI untuk masalah sekolah/lingkungan | Kolaborasi, Kreativitas, Komunikasi | 10 | Buku Bab 5, Komputer |

### Semester 2 — Bab 6: Proyek Analisis Data (30 JP)

| Kode TP | Elemen | CP | TP | Indikator Keberhasilan | Materi Pokok | Aktivitas | Dimensi Profil Lulusan | JP | Sumber |
|---|---|---|---|---|---|---|---|---|---|
| TP.6.1 | AD | F.5 | Menjelaskan konsep big data, karakteristiknya (3V/5V), serta sumber data legal dan terpercaya | Mengidentifikasi 3+ sumber data terbuka & karakteristik big data | Big Data, data terbuka, data legal, etika data | Studi kasus: big data di berbagai bidang | Penalaran Kritis, Keimanan & Ketakwaan | 5 | Buku Bab 6 |
| TP.6.2 | AD | F.5 | Menerapkan teknik pengolahan data: web scraping, data cleaning, transformasi, dan analisis data bervolume besar | Membersihkan & mentransformasi dataset (min. 500 baris) | Web scraping, data cleaning, transformasi, pandas | Praktik: scraping data, cleaning, analisis menggunakan Python | Kemandirian, Penalaran Kritis | 10 | Buku Bab 6, Komputer |
| TP.6.3 | AD | F.5 | Menyajikan visualisasi data (dashboard/grafik) dan menulis interpretasi untuk pengambilan keputusan | Membuat 3+ visualisasi data dan menarik kesimpulan | Visualisasi data, dashboard, storytelling data | Praktik: dashboard data lingkungan (Google Data Studio / Python) | Kreativitas, Komunikasi | 5 | Buku Bab 6, Komputer |
| TP.6.4 | AD, PLB | F.5, F.8 | Menyelesaikan proyek analisis data secara kolaboratif dengan tema "Hutanku Dulu, Kini, dan yang Akan Datang" | Menghasilkan laporan + visualisasi + rekomendasi | Proyek: analisis data lingkungan, prediksi, rekomendasi | Proyek kelompok: analisis data deforestasi/lingkungan | Kolaborasi, Kewargaan, Kreativitas | 10 | Buku Bab 6, Komputer |

---

## C. GLOSARIUM

| Singkatan | Kepanjangan |
|---|---|
| BK | Berpikir Komputasional |
| TIK | Teknologi Informasi dan Komunikasi |
| SK | Sistem Komputer |
| JKI | Jaringan Komputer dan Internet |
| AD | Analisis Data |
| AP | Algoritma dan Pemrograman |
| DSI | Dampak Sosial Informatika |
| PLB | Praktik Lintas Bidang |
| JP | Jam Pelajaran (45 menit) |
| STEAM | Science, Technology, Engineering, Arts, Mathematics |
| OSI | Open Systems Interconnection |
| AI | Artificial Intelligence |
| DP | Dynamic Programming |
| VPN | Virtual Private Network |
| MFA | Multi-Factor Authentication |
| DNS | Domain Name System |

---

Mengetahui,  
Kepala Sekolah

_________________________

Guru Mata Pelajaran,

Daniarsyah, S.Kom.
NIP. 198004052022211004

_________________________
"""


def kktp():
    """05_KKTP.md"""
    return f"""# KRITERIA KETERCAPAIAN TUJUAN PEMBELAJARAN (KKTP)

**Mata Pelajaran** : Informatika  
**Kelas / Fase** : XI (Sebelas) / Fase F  
**Tahun Pelajaran** : 2026/2027  

---

## A. KRITERIA KETERCAPAIAN

Kriteria ketercapaian TP menggunakan **rubrik deskriptif** dengan 4 tingkat:

| Tingkat | Predikat | Deskripsi |
|---|---|---|
| 4 | Sangat Baik | Peserta didik mampu menerapkan konsep secara mandiri, kreatif, dan mampu mentransfer ke konteks lain |
| 3 | Baik | Peserta didik mampu menerapkan konsep dengan benar dan mandiri dalam konteks yang diajarkan |
| 2 | Cukup | Peserta didik mampu menerapkan konsep dengan bantuan/arahan guru |
| 1 | Kurang | Peserta didik belum mampu menerapkan konsep meskipun dengan arahan |

**KKM (Kriteria Ketuntasan Minimal)** : **65** (skala 0–100)  
**Nilai Minimal Tuntas** : Tingkat 3 (Baik)

---

## B. KRITERIA PER TP

### Semester 1

| Kode TP | TP | Kriteria Cukup (2) | Kriteria Baik (3) | Kriteria Sangat Baik (4) |
|---|---|---|---|---|
| TP.1.1 | Menjelaskan pengertian, ruang lingkup, dan 8 elemen Informatika serta kaitannya dengan STEAM | Menyebutkan 4+ elemen Informatika | Mengidentifikasi 6+ elemen dengan contoh | Menjelaskan 8 elemen lengkap dengan contoh & kaitan STEAM |
| TP.1.2 | Menganalisis profesi dan karier di bidang Informatika | Menyebutkan 3 profesi IT | Menyebutkan 5 profesi + deskripsi | Menganalisis peran & kualifikasi 5+ profesi secara kritis |
| TP.1.3 | Menerapkan praktik lintas bidang Informatika | Membuat mind map 2 bidang | Membuat mind map 3 bidang | Mind map 5+ bidang dengan analisis mendalam |
| TP.2.1 | Menganalisis proses pemrograman | Menjelaskan 2 tahap | Menjelaskan 4 tahap | Menerapkan 4 tahap pada kasus nyata |
| TP.2.2 | Membedakan efisiensi, efektivitas, optimalitas algoritma | Menjelaskan efisiensi | Membandingkan 2 algoritma | Membandingkan 3+ algoritma dengan justifikasi |
| TP.2.3 | Menerapkan rekursi | Menulis fungsi rekursif sederhana | Menulis fungsi rekursif dengan base case | Memecahkan masalah kompleks dengan rekursi & menganalisis stack |
| TP.2.4 | Menerapkan algoritma greedy | Menjelaskan konsep greedy | Menyelesaikan 1 kasus greedy | Menyelesaikan 2+ kasus & menganalisis kelemahan |
| TP.2.5 | Menerapkan pemrograman dinamis | Menjelaskan konsep DP | Mengimplementasikan fibonacci DP | Menyelesaikan knapsack 0/1 & menganalisis kompleksitas |
| TP.2.6 | Menggunakan array & string | Operasi array dasar | Sorting, searching array | Pattern matching & manipulasi string kompleks |
| TP.2.7 | Membandingkan strategi algoritmik | Menjelaskan perbedaan | Membandingkan 2 strategi | Laporan komparatif 3 strategi dengan analisis |
| TP.2.8 | Mengembangkan program modular | Membuat 2 fungsi | Program modular 5+ fungsi | Program 100+ baris, modular, dokumentasi lengkap |
| TP.3.1 | Menerapkan verifikasi informasi digital | Mengetahui alat verifikasi | Memverifikasi 1 informasi | Memverifikasi 3+ informasi dengan metode tepat |
| TP.3.2 | Menggunakan lateral reading | Menjelaskan konsep | Menerapkan pada 1 sumber | Menerapkan pada 3+ sumber & membandingkan |
| TP.3.3 | Menganalisis dampak sosial TIK | Menyebutkan 3 dampak | Mengidentifikasi 5 dampak + solusi | Analisis kasus mendalam dengan rekomendasi |
| TP.3.4 | Menyusun argumentasi kritis dampak TIK | Menulis esai 200 kata | Menulis esai 300+ kata | Esai 500+ kata pro-kontra didukung data |

### Semester 2

| Kode TP | TP | Kriteria Cukup (2) | Kriteria Baik (3) | Kriteria Sangat Baik (4) |
|---|---|---|---|---|
| TP.4.1 | Menganalisis topologi & perangkat jaringan | Menyebutkan 3 topologi | Menggambar 4+ topologi | Mendesain topologi untuk kebutuhan nyata |
| TP.4.2 | Menjelaskan OSI Layer & TCP/IP | Menyebutkan 7 layer | Menjelaskan 4+ layer dengan analogi | Menjelaskan semua layer + enkapsulasi + contoh protokol |
| TP.4.3 | Menerapkan konfigurasi jaringan | Konfigurasi IP statis | IP + routing sederhana | Konfigurasi lengkap + troubleshooting |
| TP.4.4 | Menerapkan cyber security | Menjelaskan 3 ancaman | Enkripsi sederhana + 5 ancaman | Analisis kasus & rekomendasi keamanan |
| TP.4.5 | Menerapkan tata kelola akses data | Menjelaskan firewall | Firewall + VPN dasar | MFA + firewall + VPN + audit log |
| TP.5.1 | Membedakan jenis aplikasi | Menyebutkan 2 platform | Menjelaskan 3 platform | Analisis perbandingan dengan studi kasus |
| TP.5.2 | Mengembangkan aplikasi App Inventor | UI 1 screen | 2 screen + navigasi | 3+ screen + penyimpanan data |
| TP.5.3 | Mengintegrasikan library AI | Menjelaskan AI library | Menambahkan 1 fitur AI | Integrasi AI fungsional dalam aplikasi |
| TP.5.4 | Menerapkan AI recognition | Mengetahui cara kerja | Mendemonstrasikan 1 fitur | Mendemonstrasikan 2+ fitur AI |
| TP.5.5 | Proyek aplikasi mobile AI | Prototipe dasar | Aplikasi fungsional | Aplikasi + dokumentasi + presentasi |
| TP.6.1 | Menjelaskan big data | Menjelaskan 3V | Mengidentifikasi 5V + 3 sumber data | Analisis data terbuka dengan konteks nyata |
| TP.6.2 | Menerapkan pengolahan data | Data cleaning sederhana | Scraping + cleaning | Scraping + cleaning + analisis (500+ baris) |
| TP.6.3 | Visualisasi & interpretasi data | 1 visualisasi | 3 visualisasi + interpretasi | Dashboard interaktif + kesimpulan bisnis |
| TP.6.4 | Proyek analisis data "Hutanku" | Laporan dasar | Laporan + visualisasi | Laporan + visualisasi + rekomendasi berbasis data |

---

## C. TEKNIK PENILAIAN

| Jenis Asesmen | Teknik | Bobot |
|---|---|---|
| Diagnostik | Tes awal (kognitif & non-kognitif) | — |
| Formatif | Observasi, kuis, LKPD, coding challenge | 30% |
| Sumatif (PTS) | Tes tertulis + praktik coding | 20% |
| Sumatif (PAS/PAT) | Tes tertulis + proyek | 30% |
| Proyek | Portofolio & presentasi | 20% |

---

Mengetahui,  
Kepala Sekolah

_________________________

Guru Mata Pelajaran,

Daniarsyah, S.Kom.
NIP. 198004052022211004

_________________________
"""


def pemetaan():
    """06_PEMETAAN_KOMPETENSI_PENILAIAN.md"""
    return f"""# PEMETAAN KOMPETENSI & PENILAIAN

**Mata Pelajaran** : Informatika  
**Kelas / Fase** : XI (Sebelas) / Fase F  
**Tahun Pelajaran** : 2026/2027  

---

## A. PEMETAAN KOMPETENSI PER ELEMEN

| Elemen | Kompetensi | Lingkup Materi |
|---|---|---|
| **BK** | Menganalisis strategi algoritmik (rekursi, greedy, DP); membandingkan solusi alternatif; justifikasi efisiensi | Bab 1: 8 elemen, Bab 2: strategi algoritmik |
| **TIK** | Verifikasi informasi digital; lateral reading; kreasi konten; hukum digital | Bab 1: definisi TIK, Bab 3: literasi digital |
| **SK** | Prototipe perangkat lunak; interaksi dengan controller/kit elektronika | Bab 4: konfigurasi jaringan, Bab 5: embedded AI |
| **JKI** | OSI Layer; topologi; cyber security; tata kelola akses data | Bab 4: jaringan & keamanan |
| **AD** | Big data; pengolahan data bervolume besar; visualisasi; prediksi | Bab 6: analisis data |
| **AP** | Rekursi, greedy, DP; program modular; library AI; dokumentasi; struktur data kompleks | Bab 2: algoritma, Bab 5: mobile AI |
| **DSI** | Kasus terkini; argumentasi kritis; etika digital; dampak TIK | Bab 3: dampak sosial, Bab 1: profesi |
| **PLB** | Projek sistem komputasi; kolaborasi; komunikasi produk | Bab 1: PLB, Bab 2: PLB sains, Bab 5–6: proyek |

---

## B. TEKNIK & INSTRUMEN PENILAIAN

| No | Jenis Penilaian | Teknik | Instrumen | Waktu |
|---|---|---|---|---|
| 1 | **Diagnostik** | Tes awal | Soal pilihan ganda + esai singkat | Awal semester |
| 2 | **Formatif** | Observasi | Lembar observasi aktivitas | Setiap pertemuan |
| 3 | **Formatif** | Kuis | Soal singkat (lisan/tulisan) | Akhir bab |
| 4 | **Formatif** | Praktik | Rubrik coding challenge | Per pertemuan coding |
| 5 | **Formatif** | Penugasan | LKPD | Per TP |
| 6 | **Formatif** | Projek | Rubrik proyek | Bab 2, 5, 6 |
| 7 | **Sumatif (PTS)** | Tes tulis + praktik | Soal PG + esai + coding | Tengah semester |
| 8 | **Sumatif (PAS)** | Tes tulis + proyek | Soal PG + esai + portofolio | Akhir semester 1 |
| 9 | **Sumatif (PAT)** | Tes tulis + proyek | Soal PG + esai + presentasi | Akhir semester 2 |
| 10 | **Portofolio** | Kumpulan karya | Dokumentasi proyek & tugas | Sepanjang tahun |

---

## C. BOBOT PENILAIAN

| Komponen | Semester 1 | Semester 2 |
|---|---|---|
| Formatif (Kuis, Praktik, Tugas) | 40% | 40% |
| Projek | 20% | 20% |
| PTS | 15% | 15% |
| PAS / PAT | 25% | 25% |
| **Total** | **100%** | **100%** |

---

## D. KISI-KISI SOAL

| Elemen | Bentuk Soal | Jumlah Soal | Level Kognitif |
|---|---|---|---|
| BK | PG + Esai | 8 | C3–C5 |
| TIK | PG + Esai | 5 | C3–C4 |
| SK | PG + Esai | 5 | C3–C4 |
| JKI | PG + Esai | 8 | C3–C5 |
| AD | PG + Esai | 8 | C3–C5 |
| AP | PG + Esai + Coding | 12 | C3–C6 |
| DSI | Esai | 5 | C4–C5 |
| PLB | Projek | 1 | C6 |

---

## E. RUBRIK PENILAIAN 8 DIMENSI PROFIL LULUSAN

| Dimensi | Kriteria | SB (4) | B (3) | C (2) | PB (1) |
|---|---|---|---|---|---|
| **Kolaborasi** | Kolaborasi dalam kerja kelompok | Aktif berkontribusi & memfasilitasi | Berkontribusi aktif | Terlibat pasif | Tidak terlibat |
| **Kemandirian** | Inisiatif & tanggung jawab belajar | Mandiri penuh & inisiatif | Mandiri dengan sedikit arahan | Perlu diarahkan | Sangat tergantung |
| **Penalaran Kritis** | Kualitas analisis & argumen | Analisis mendalam, argumen logis | Analisis baik, cukup logis | Analisis dangkal | Tidak menganalisis |
| **Kreativitas** | Orisinalitas karya/solusi | Karya orisinal & inovatif | Karya orisinal | Karya modifikasi | Karya meniru |
| **Keimanan & Ketakwaan** | Etika digital & tanggung jawab | Sangat etis & bertanggung jawab | Etis & bertanggung jawab | Cukup etis | Perlu bimbingan |
| **Kewargaan** | Kesadaran berbangsa & berkontribusi | Aktif berkontribusi untuk komunitas | Peduli lingkungan | Cukup peduli | Kurang peduli |
| **Kesehatan** | Kebugaran & manajemen diri | Menjaga postur, mengatur waktu layar | Cukup menjaga | Kurang menjaga | Tidak menjaga |
| **Komunikasi** | Penyampaian gagasan | Sangat jelas, terstruktur, meyakinkan | Jelas & terstruktur | Cukup jelas | Tidak jelas |

---

Mengetahui,  
Kepala Sekolah

_________________________

Guru Mata Pelajaran,

Daniarsyah, S.Kom.
NIP. 198004052022211004

_________________________
"""


def bank_soal():
    """06b_BANK_SOAL.md"""
    return f"""# BANK SOAL INFORMATIKA KELAS XI

## FASE F — TAHUN PELAJARAN 2026/2027

---

### A. ASESMEN DIAGNOSTIK (Awal Semester 1)

**Petunjuk:** Soal berikut untuk mengetahui kemampuan awal peserta didik.

| No | Soal | Elemen | Jawaban |
|---|---|---|---|
| 1 | Apa yang dimaksud dengan algoritma? | BK | Urutan langkah logis untuk menyelesaikan masalah |
| 2 | Sebutkan 3 perangkat lunak aplikasi yang kamu ketahui! | TIK | MS Word, Chrome, Excel (kebebasan) |
| 3 | Apa fungsi processor pada komputer? | SK | Memproses data/instruksi |
| 4 | Apa kepanjangan dari HTTP? | JKI | Hypertext Transfer Protocol |
| 5 | Apa perbedaan data dan informasi? | AD | Data = mentah, Informasi = data telah diolah |
| 6 | Bahasa pemrograman apa yang sudah kamu pelajari? | AP | Python, Java, dll. |
| 7 | Apa dampak positif media sosial? | DSI | Memperluas jaringan, informasi cepat |
| 8 | Apa itu kolaborasi? | PLB | Kerja sama dalam tim |

### B. SOAL FORMATIF

#### B.1 Bab 1 — Tentang Informatika (BK, TIK, DSI)

1. Sebutkan dan jelaskan minimal 6 dari 8 elemen Informatika! **(C2)**
2. Bagaimana kaitan antara Informatika dengan STEAM? Berikan contoh! **(C3)**
3. Analisislah 3 profesi di bidang Informatika dan jelaskan kualifikasi yang dibutuhkan! **(C4)**
4. Jelaskan bagaimana Informatika dapat diterapkan dalam bidang Kimia! **(C3)**
5. Menurutmu, apa tantangan terbesar dalam mengintegrasikan Informatika dengan disiplin ilmu lain? **(C4)**

#### B.2 Bab 2 — Strategi Algoritmik & Pemrograman (AP, BK)

1. Jelaskan 4 tahap proses pemrograman! **(C2)**
2. Apa perbedaan efisiensi waktu dan efisiensi memori dalam algoritma? **(C3)**
3. Buatlah fungsi rekursif untuk menghitung faktorial dari n! **(C3)**
4. Jelaskan konsep base case dan recursive case dalam rekursi! **(C2)**
5. Apa karakteristik masalah yang cocok diselesaikan dengan algoritma greedy? **(C3)**
6. Selesaikan masalah coin change dengan greedy: tentukan jumlah minimal koin untuk 42 rupiah jika tersedia koin 25, 10, 5, 1! **(C3)**
7. Jelaskan perbedaan pemrograman dinamis dengan rekursi biasa! **(C4)**
8. Implementasikan fibonacci ke-n menggunakan DP (memoization)! **(C3)**
9. Buatlah program Python untuk mengecek apakah sebuah kata adalah palindrom! **(C3)**
10. Bandingkan kompleksitas algoritma sorting bubble sort dan merge sort! **(C4)**

#### B.3 Bab 3 — Berpikir Kritis & DSI (TIK, DSI)

1. Apa yang dimaksud dengan verifikasi informasi digital? Sebutkan 3 alat yang bisa digunakan! **(C2)**
2. Jelaskan teknik membaca lateral (lateral reading) untuk mengevaluasi sumber informasi! **(C3)**
3. Analisislah sebuah kasus hoaks yang pernah beredar — bagaimana cara memverifikasinya? **(C4)**
4. Bagaimana dampak media sosial terhadap demokrasi digital di Indonesia? **(C4)**
5. Apa yang dimaksud dengan digital footprint dan mengapa penting untuk dikelola? **(C3)**

#### B.4 Bab 4 — Jaringan Komputer & Internet (JKI, SK)

1. Gambarkan dan jelaskan 4 topologi jaringan! **(C2)**
2. Jelaskan fungsi masing-masing 7 layer OSI! **(C3)**
3. Apa perbedaan TCP dan UDP? Berikan contoh penggunaan masing-masing! **(C3)**
4. Apa itu enkripsi? Jelaskan perbedaan enkripsi simetris dan asimetris! **(C3)**
5. Sebutkan 5 jenis ancaman cyber security dan cara pencegahannya! **(C3)**
6. Bagaimana cara kerja firewall dalam melindungi jaringan? **(C3)**
7. Apa perbedaan VPN dan proxy? Kapan sebaiknya menggunakan VPN? **(C4)**

#### B.5 Bab 5 — Aplikasi Mobile & AI (AP)

1. Jelaskan perbedaan web apps, desktop apps, dan mobile apps! **(C2)**
2. Sebutkan 3 komponen utama dalam App Inventor! **(C2)**
3. Bagaimana cara menyimpan data lokal pada aplikasi App Inventor? **(C3)**
4. Apa yang dimaksud dengan machine learning? Berikan 3 contoh penerapannya! **(C2)**
5. Jelaskan cara kerja image classification menggunakan library AI! **(C3)**
6. Bagaimana speech recognition dapat diintegrasikan ke dalam aplikasi mobile? **(C3)**
7. Rancanglah aplikasi mobile berbasis AI untuk menyelesaikan masalah di sekolahmu! **(C6)**

#### B.6 Bab 6 — Proyek Analisis Data (AD, PLB)

1. Apa yang dimaksud dengan big data? Jelaskan karakteristik 5V! **(C2)**
2. Sebutkan 3 sumber data terbuka yang legal di Indonesia! **(C2)**
3. Jelaskan tahapan data cleaning dan mengapa penting dilakukan! **(C3)**
4. Buatlah visualisasi data (diagram batang) dari data berikut: [data diberikan] **(C3)**
5. Bagaimana data dapat digunakan untuk pengambilan keputusan? Berikan contoh! **(C4)**
6. Rancanglah proyek analisis data sederhana dengan tema lingkungan! **(C6)**

### C. SOAL PTS (Semester 1)

**A. Pilihan Ganda (20 soal)**

1. Berikut ini yang BUKAN termasuk elemen Informatika adalah...
   a. Berpikir Komputasional
   b. Analisis Data
   c. **Kalkulus**
   d. Jaringan Komputer dan Internet

2. Proses pemrograman yang benar adalah...
   a. Implementasi → Analisis → Desain → Pengujian
   b. **Analisis → Desain → Implementasi → Pengujian**
   c. Desain → Analisis → Pengujian → Implementasi
   d. Pengujian → Analisis → Desain → Implementasi

3. Fungsi rekursif memiliki dua komponen utama yaitu...
   a. **Base case dan recursive case**
   b. Input dan output
   c. Variabel dan konstanta
   d. Looping dan branching

4. Algoritma greedy selalu mengambil keputusan...
   a. **Terbaik pada saat itu (local optimum)**
   b. Terbaik untuk masa depan (global optimum)
   c. Acak
   d. Berdasarkan data masa lalu

5. Pemrograman dinamis cocok untuk masalah yang memiliki sifat...
   a. **Overlapping subproblems dan optimal substructure**
   b. Hanya satu solusi
   c. Tidak memerlukan optimasi
   d. Linear dan sederhana

6-20. (Soal lanjutan mencakup semua materi Bab 1–3)

**B. Esai (5 soal)**
1. Bandingkan algoritma rekursif dan iteratif untuk menghitung deret Fibonacci! Mana yang lebih efisien? Jelaskan!
2. Analisislah sebuah berita hoaks yang kamu temui — bagaimana cara memverifikasinya dengan metode lateral reading?
3. Jelaskan penerapan Informatika dalam bidang Fisika! Berikan contoh program yang bisa dibuat!
4. Bagaimana dampak cyberbullying terhadap kesehatan mental remaja? Berikan solusi pencegahannya!
5. Buatlah program Python untuk menentukan jumlah minimal koin menggunakan greedy algorithm!

### D. SOAL PAS (Semester 1)

**A. Pilihan Ganda (25 soal)**
Mencakup seluruh materi Bab 1–3.

**B. Esai (5 soal)**
1. Implementasikan fungsi rekursif untuk menyelesaikan Menara Hanoi dengan n piringan!
2. Selesaikan masalah knapsack 0/1 dengan bobot [2,3,4,5] dan nilai [3,4,5,6] kapasitas 8 menggunakan DP!
3. Tulis esai argumentatif tentang "Dampak Media Sosial terhadap Demokrasi di Indonesia" (min. 300 kata)!
4. Buatlah program modular Python untuk mensimulasikan pertumbuhan populasi dengan rumus logistik!
5. Evaluasilah sebuah sumber informasi digital menggunakan metode lateral reading — sertakan langkah-langkahnya!

### E. SOAL PTS (Semester 2)

**A. Pilihan Ganda (20 soal)**
1. Layer ke-3 pada OSI layer adalah...
   a. **Network Layer**
   b. Transport Layer
   c. Data Link Layer
   d. Session Layer

2. Protokol yang digunakan untuk mengirim email adalah...
   a. HTTP
   b. **SMTP**
   c. FTP
   d. DNS

3. Berikut ini yang termasuk serangan cyber adalah...
   a. **Phishing**
   b. Backup
   c. Encryption
   d. Authentication

4. App Inventor menggunakan bahasa pemrograman berbasis...
   a. **Blok/visual**
   b. Teks (Python)
   c. Teks (Java)
   d. Markdown

5. Komponen untuk menyimpan data lokal di App Inventor adalah...
   a. Firebase
   b. **TinyDB**
   c. SQLite
   d. CloudDB

6-20. (Soal lanjutan)

**B. Esai (5 soal)**
1. Jelaskan perbedaan enkapsulasi data pada OSI layer vs TCP/IP!
2. Buatlah aplikasi App Inventor sederhana untuk kalkulator BMI!
3. Bagaimana cara kerja image classification? Jelaskan dari input gambar hingga output label!
4. Konfigurasikan jaringan sederhana (2 PC, 1 switch, 1 router) di Packet Tracer!
5. Analisislah sebuah kasus kebocoran data di Indonesia — apa penyebab dan solusinya?

### F. SOAL PAT (Semester 2)

**A. Pilihan Ganda (25 soal)**
Mencakup seluruh materi Bab 4–6.

**B. Esai (5 soal)**
1. Rancang dan jelaskan arsitektur keamanan jaringan untuk sebuah sekolah menengah!
2. Buatlah aplikasi mobile dengan App Inventor yang mengintegrasikan image classifier untuk mengenali jenis sampah!
3. Lakukan analisis data dari dataset yang diberikan (data lingkungan) — cleaning, transformasi, visualisasi, dan interpretasi!
4. Bandingkan kelebihan dan kekurangan: rekursif vs greedy vs DP dalam menyelesaikan masalah optimasi!
5. Refleksikan proyek "Hutanku Dulu, Kini, dan yang Akan Datang" — apa temuan, tantangan, dan rekomendasi kalian?

### G. KARTU SOAL

| Kartu | Elemen | Indikator | Level | Bentuk |
|---|---|---|---|---|
| KS-01 | BK | Menganalisis strategi algoritmik | C4 | Esai |
| KS-02 | AP | Mengimplementasikan rekursi | C3 | Coding |
| KS-03 | AP | Mengimplementasikan greedy | C3 | Coding |
| KS-04 | AP | Mengimplementasikan DP | C3 | Coding |
| KS-05 | JKI | Menganalisis topologi jaringan | C3–C4 | PG + Esai |
| KS-06 | JKI | Menerapkan cyber security | C3 | Esai |
| KS-07 | AD | Menerapkan pengolahan data | C3 | Praktik |
| KS-08 | AD | Menyajikan visualisasi data | C3 | Praktik |
| KS-09 | DSI | Menganalisis dampak TIK | C4 | Esai |
| KS-10 | TIK | Menerapkan verifikasi informasi | C3 | Praktik |
| KS-11 | SK | Menghasilkan prototipe | C6 | Projek |
| KS-12 | PLB | Mengomunikasikan produk | C6 | Presentasi |

---

**Kunci Jawaban Soal Pilihan Ganda (tersedia terpisah)**

---

Mengetahui,  
Kepala Sekolah

_________________________

Guru Mata Pelajaran,

Daniarsyah, S.Kom.
NIP. 198004052022211004

_________________________
"""


def kokurikuler():
    """06c_PROGRAM_KOKURIKULER_8_DIMENSI.md"""
    return f"""# PROGRAM KOKURIKULER — INTEGRASI 8 DIMENSI PROFIL LULUSAN

## DALAM PEMBELAJARAN INFORMATIKA KELAS XI (FASE F)

---

### A. LATAR BELAKANG

Berdasarkan kebijakan Kemendikdasmen tahun 2025, **P5 (Projek Penguatan Profil Pelajar Pancasila) resmi dihapus** dan digantikan dengan konsep **Profil Lulusan 8 Dimensi**. Perubahan ini berlaku mulai tahun ajaran 2025/2026, sehingga untuk TP 2026/2027 telah sepenuhnya menggunakan kerangka baru.

**Perubahan utama:**
- P5 dulunya merupakan kegiatan projek kokurikuler yang berdiri sendiri
- Kini **8 Dimensi Profil Lulusan** terintegrasi penuh ke dalam **deep learning** di setiap mata pelajaran
- Tidak ada alokasi jam khusus projek — seluruh jam digunakan untuk pembelajaran bermakna
- Pendekatan deep learning: **mindful, meaningful, joyful** melalui pikir, hati, rasa, dan raga

---

### B. 8 DIMENSI PROFIL LULUSAN & INTEGRASINYA DI INFORMATIKA KELAS XI

| No | Dimensi | Deskripsi | Integrasi dalam Informatika Kelas XI |
|---|---|---|---|
| 1 | **Keimanan & Ketakwaan** | Berakhlak mulia, etika digital, toleransi | JKI (cyber security, etika hacking), DSI (etika AI, UU ITE), AD (etika data) |
| 2 | **Kewargaan** | Cinta tanah air, kesadaran berbangsa, kontribusi sosial | DSI (demokrasi digital), Bab 6 (data lingkungan Indonesia), PLB (proyek untuk komunitas) |
| 3 | **Penalaran Kritis** | Menganalisis, mengevaluasi, justifikasi | BK (perbandingan algoritma), AP (debugging), AD (interpretasi data) |
| 4 | **Kreativitas** | Menghasilkan gagasan & karya orisinal | AP (coding kreatif), Bab 5 (aplikasi mobile AI), Bab 6 (dashboard data) |
| 5 | **Kolaborasi** | Kerja tim, kepemimpinan, inklusif | PLB (proyek tim), AP (pair programming), Bab 6 (proyek kelompok) |
| 6 | **Kemandirian** | Inisiatif, regulasi diri, tanggung jawab | AP (coding mandiri), BK (problem solving), proyek individu |
| 7 | **Kesehatan** | Kebugaran, manajemen waktu layar, ergonomi | JKI (postur, screen time), TIK (ergonomi kerja komputer) |
| 8 | **Komunikasi** | Presentasi, dokumentasi, argumen | PLB (presentasi proyek), DSI (debat), AP (dokumentasi kode) |

---

### C. STRATEGI INTEGRASI DEEP LEARNING

Setiap modul ajar mengintegrasikan **3 pilar deep learning**:

| Pilar | Arti | Contoh di Informatika Kelas XI |
|---|---|---|
| **Mindful** | Siswa memahami tujuan pembelajaran | "Mengapa belajar rekursi penting untuk pemrograman?" |
| **Meaningful** | Materi terkait kehidupan nyata | Kasus kebocoran data, hoaks, aplikasi AI di smartphone |
| **Joyful** | Proses belajar positif | Coding challenge, lomba debugging, gamifikasi |

### D. MATRIKS INTEGRASI PER BAB

| Bab | Dimensi Dominan | Aktivitas Kokurikuler |
|---|---|---|
| 1 | Penalaran Kritis, Kewargaan | Diskusi profesi IT di Indonesia |
| 2 | Penalaran Kritis, Kreativitas, Kemandirian | Coding challenge, lomba algoritma |
| 3 | Penalaran Kritis, Kewargaan, Komunikasi | Debat dampak TIK, verifikasi berita |
| 4 | Penalaran Kritis, Keimanan, Kemandirian | Simulasi keamanan jaringan, etika siber |
| 5 | Kreativitas, Kolaborasi, Kemandirian | Hackathon aplikasi mobile AI |
| 6 | Kolaborasi, Kewargaan, Komunikasi | Proyek data lingkungan kampung/hutan |

---

### E. ASESMEN 8 DIMENSI

| Nama Siswa | Keimanan | Kewargaan | Penalaran | Kreativitas | Kolaborasi | Kemandirian | Kesehatan | Komunikasi | Catatan |
|---|---|---|---|---|---|---|---|---|---|
| | /4 | /4 | /4 | /4 | /4 | /4 | /4 | /4 | |

**Skala:** 4 = Sangat Berkembang | 3 = Berkembang | 2 = Mulai Berkembang | 1 = Belum Terlihat

### F. LEMBAR REFLEKSI SISWA

| Pertanyaan | Jawaban |
|---|---|
| **Mindful:** Apa yang aku pelajari hari ini? | |
| **Meaningful:** Bagaimana ini terhubung dengan kehidupan nyata? | |
| **Joyful:** Hal paling menyenangkan dari pembelajaran hari ini? | |
| **Dimensi:** Dimensi mana yang paling berkembang pada diriku? | |

---

> **Catatan:** Tidak diperlukan modul projek terpisah — seluruh dimensi dikembangkan melalui aktivitas yang sudah dirancang di modul ajar.

---

Mengetahui,  
Kepala Sekolah

_________________________

Guru Mata Pelajaran,

Daniarsyah, S.Kom.
NIP. 198004052022211004

_________________________
"""


def jurnal():
    """07_JURNAL_MENGAJAR.md"""
    return f"""# JURNAL MENGAJAR INFORMATIKA KELAS XI

**Tahun Pelajaran** : 2026/2027  
**Kelas** : XI (Fase F)  

---

## SEMESTER 1 (GANJIL)

| Pertemuan ke- | Tanggal | Bab | Materi | JP | Kegiatan | Penilaian | Keterangan |
|---|---|---|---|---|---|---|---|
| 1 | | | — MPLS | 5 | Pengenalan sekolah | — | |
| 2 | | 1 | 8 elemen Informatika & STEAM | 5 | Diskusi & mind map | Formatif (observasi) | |
| 3 | | 1 | Profesi IT & karier digital | 5 | Riset & presentasi | Formatif (presentasi) | |
| 4 | | 1 | PLB — Aplikasi Informatika | 5 | Proyek kelompok | Formatif (proyek) | |
| 5 | | 2 | Proses pemrograman | 5 | Studi kasus | Formatif (LKPD) | |
| 6 | | 2 | Efisiensi algoritma | 5 | Praktik sorting | Formatif (praktik) | |
| 7 | | 2 | Rekursi — konsep | 5 | Coding rekursif | Formatif (coding) | |
| 8 | | 2 | Rekursi — implementasi | 5 | Coding lanjutan | Formatif (coding) | |
| 9 | | 2 | Greedy — konsep | 5 | Diskusi & contoh | Formatif (kuis) | |
| 10 | | 2 | Greedy — implementasi | 5 | Coding greedy | Formatif (coding) | |
| 11 | | 2 | Dinamis — konsep | 5 | Diskusi DP | Formatif (LKPD) | |
| 12 | | 2 | Dinamis — implementasi | 5 | Coding DP | Formatif (coding) | |
| 13 | | 2 | Array & string | 5 | Coding struktur data | Formatif (praktik) | |
| 14 | | 2 | Manipulasi string | 5 | Pattern matching | Formatif (coding) | |
| 15 | | — | Review Bab 1–2 | 5 | Latihan soal | Formatif (tes) | |
| 16 | | — | **PTS** | 5 | Tes tulis + praktik | Sumatif | |
| 17 | | 2 | PLB Kimia/Fisika | 5 | Coding simulasi sains | Formatif (proyek) | |
| 18 | | 2 | PLB Biologi | 5 | Coding analisis data | Formatif (proyek) | |
| 19 | | 3 | Literasi digital lanjutan | 5 | Verifikasi berita | Formatif (praktik) | |
| 20 | | 3 | Lateral reading | 5 | Evaluasi sumber | Formatif (LKPD) | |
| 21 | | 3 | Dampak sosial TIK | 5 | Analisis kasus | Formatif (diskusi) | |
| 22 | | 3 | Debat dampak TIK | 5 | Debat/esai | Formatif (presentasi) | |
| 23 | | — | Review Semester 1 | 5 | Latihan soal | Formatif | |
| 24 | | — | **PAS** | 5 | Tes tulis + portofolio | Sumatif | |
| 25 | | — | Libur | — | — | — | |

## SEMESTER 2 (GENAP)

| Pertemuan ke- | Tanggal | Bab | Materi | JP | Kegiatan | Penilaian | Keterangan |
|---|---|---|---|---|---|---|---|
| 1 | | 4 | Pengantar jaringan komputer | 5 | Diskusi & video | Formatif (observasi) | |
| 2 | | 4 | Topologi & perangkat jaringan | 5 | Simulasi topologi | Formatif (LKPD) | |
| 3 | | 4 | OSI Layer & TCP/IP | 5 | Diagram enkapsulasi | Formatif (kuis) | |
| 4 | | 4 | Pertukaran data & routing | 5 | Simulasi routing | Formatif (praktik) | |
| 5 | | 4 | Cyber security | 5 | Enkripsi & kasus | Formatif (praktik) | |
| 6 | | 4 | Tata kelola akses & konfigurasi | 5 | Simulasi firewall/VPN | Formatif (praktik) | |
| 7 | | 4 | Praktik Packet Tracer | 5 | Konfigurasi jaringan | Formatif (proyek) | |
| 8 | | 5 | Pengantar aplikasi mobile | 5 | Riset platform | Formatif (presentasi) | |
| 9 | | 5 | App Inventor — UI & event | 5 | Coding App Inventor | Formatif (coding) | |
| 10 | | 5 | App Inventor — navigasi | 5 | Coding multi-screen | Formatif (coding) | |
| 11 | | 5 | App Inventor — data lokal | 5 | TinyDB | Formatif (coding) | |
| 12 | | — | **PTS** | 5 | Tes tulis + praktik | Sumatif | |
| 13 | | 5 | Library AI — pengenalan | 5 | Tutorial AI | Formatif (LKPD) | |
| 14 | | 5 | Image classification | 5 | Coding AI | Formatif (coding) | |
| 15 | | 5 | Text/speech recognition | 5 | Coding AI | Formatif (coding) | |
| 16 | | 5 | Proyek — perencanaan | 5 | Desain aplikasi AI | Formatif (proyek) | |
| 17 | | 5 | Proyek — implementasi | 5 | Coding proyek | Formatif (proyek) | |
| 18 | | 5 | Proyek — presentasi | 5 | Demo aplikasi | Formatif (presentasi) | |
| 19 | | 6 | Big data | 5 | Diskusi & studi kasus | Formatif (kuis) | |
| 20 | | 6 | Pengolahan data | 5 | Python scraping/cleaning | Formatif (coding) | |
| 21 | | 6 | Visualisasi data | 5 | Dashboard | Formatif (praktik) | |
| 22 | | 6 | Proyek "Hutanku" — desain | 5 | Perencanaan proyek | Formatif (proyek) | |
| 23 | | 6 | Proyek "Hutanku" — final | 5 | Implementasi & presentasi | Formatif (presentasi) | |
| 24 | | — | Review Semester 2 | 5 | Latihan soal | Formatif | |
| 25 | | — | **PAT** | 5 | Tes tulis + portofolio | Sumatif | |

---

Mengetahui,  
Kepala Sekolah

_________________________

Guru Mata Pelajaran,

Daniarsyah, S.Kom.
NIP. 198004052022211004

_________________________
"""


def analisis_cp_tp():
    """08_ANALISIS_CP_TP.md"""
    return f"""# ANALISIS CP → TP

**Mata Pelajaran** : Informatika  
**Kelas / Fase** : XI (Sebelas) / Fase F  
**Tahun Pelajaran** : 2026/2027  

---

| Elemen | CP | TP | Indikator | JP |
|---|---|---|---|---|
| **BK** | Menganalisis beberapa strategi algoritmik secara kritis untuk menghasilkan banyak alternatif solusi dari satu persoalan dengan memberikan justifikasi efisiensi, kelebihan, dan keterbatasan dari setiap alternatif solusi, kemudian memilih dan menerapkan solusi terbaik, paling efisien, dan optimal dengan merancang struktur data yang lebih kompleks dan abstrak. | TP.1.1: Menjelaskan 8 elemen Informatika & STEAM | Mengidentifikasi 6+ elemen | 5 |
| | | TP.2.2: Membedakan efisiensi, efektivitas, optimalitas algoritma | Membandingkan 2+ algoritma | 5 |
| | | TP.2.7: Membandingkan performa strategi algoritmik | Laporan perbandingan 2+ strategi | 5 |
| **TIK** | Memahami penggunaan mesin pencari untuk riset; mengevaluasi kebenaran konten; membaca lateral; mengkreasi konten digital; memahami hukum digital. | TP.3.1: Menerapkan verifikasi informasi digital | Memverifikasi 3 informasi | 5 |
| | | TP.3.2: Menggunakan lateral reading | Menerapkan pada 3+ sumber | 5 |
| **SK** | Menghasilkan prototipe perangkat lunak yang berinteraksi dengan single board computer/controller atau kit elektronika untuk edukasi yang bisa diprogram, serta mengomunikasikan produk dan proses pengembangannya. | TP.4.3: Menerapkan konfigurasi jaringan | Konfigurasi IP + routing | 5 |
| | | TP.4.5: Menerapkan tata kelola akses data | Firewall + VPN + MFA | 5 |
| **JKI** | Memahami konsep lanjutan jaringan komputer dan internet: OSI Layer, topologi, komponen, mekanisme pertukaran data, cyber security, tata kelola kontrol akses data, konfigurasi keamanan. | TP.4.1: Menganalisis topologi & perangkat jaringan | Mendesain topologi untuk kebutuhan nyata | 5 |
| | | TP.4.2: Menjelaskan OSI Layer & TCP/IP | Menjelaskan 7 layer + enkapsulasi | 5 |
| | | TP.4.4: Menerapkan cyber security | Analisis kasus + enkripsi | 5 |
| **AD** | Memanfaatkan sumber data yang legal, terbuka, terpercaya guna mengolah data untuk pengambilan keputusan dan prediksi secara efektif, efisien, dan optimal. | TP.6.1: Menjelaskan big data | Identifikasi 5V + 3 sumber data | 5 |
| | | TP.6.2: Menerapkan pengolahan data | Scraping + cleaning + analisis | 10 |
| | | TP.6.3: Visualisasi & interpretasi data | Dashboard + kesimpulan | 5 |
| **AP** | Mengembangkan program modular; memahami, memelihara, dan menyempurnakan source code; merancang struktur data abstrak; menggunakan library standar termasuk AI dan big data; menerjemahkan program antar bahasa. | TP.2.1: Menganalisis proses pemrograman | Menjelaskan 4 tahap | 5 |
| | | TP.2.3: Menerapkan rekursi | Fungsi rekursif + base case | 10 |
| | | TP.2.4: Menerapkan greedy | Menyelesaikan 2+ kasus greedy | 10 |
| | | TP.2.5: Menerapkan DP | Fibonacci DP + knapsack | 10 |
| | | TP.2.6: Manipulasi array & string | Sorting, searching, pattern | 5 |
| | | TP.5.2: Mengembangkan aplikasi App Inventor | Aplikasi 3+ screen | 10 |
| | | TP.5.3: Integrasi library AI | 1 fitur AI dalam aplikasi | 5 |
| | | TP.5.4: AI recognition | Demo 2+ fitur AI | 5 |
| **DSI** | Mengkaji, menganalisis, dan memberikan argumentasi kritis pada kasus-kasus sosial terkini terkait produk TIK dan sistem komputasi. | TP.1.2: Menganalisis profesi IT | Analisis 5+ profesi | 5 |
| | | TP.3.3: Menganalisis dampak sosial TIK | 5 dampak + solusi | 5 |
| | | TP.3.4: Argumentasi kritis dampak TIK | Esai 500+ kata pro-kontra | 5 |
| **PLB** | Bergotong royong dalam tim inklusif untuk mengerjakan projek pengembangan sistem komputasi; mengomunikasikan produk & proses. | TP.1.3: Praktik lintas bidang | Mind map 3+ bidang | 5 |
| | | TP.2.8: Program modular lintas bidang | Program 100+ baris modular | 5 |
| | | TP.5.5: Proyek aplikasi mobile AI | Aplikasi + dokumentasi + demo | 10 |
| | | TP.6.4: Proyek analisis data "Hutanku" | Laporan + visualisasi + rekomendasi | 10 |
| | **Review & Ujian** | | | 10 |
| | **Total** | **25 TP** | | **200** |

---

Mengetahui,  
Kepala Sekolah

_________________________

Guru Mata Pelajaran,

Daniarsyah, S.Kom.
NIP. 198004052022211004

_________________________
"""


def daftar_nilai():
    """09_DAFTAR_NILAI.md"""
    return f"""# DAFTAR NILAI INFORMATIKA KELAS XI

**Tahun Pelajaran** : 2026/2027  
**Semester** : 1 (Ganjil) / 2 (Genap)  

---

## A. DAFTAR NILAI PER TP

| No | Nama Siswa | TP.1.1 | TP.1.2 | TP.1.3 | TP.2.1 | ... | TP.6.4 | Rata-rata |
|---|---|---|---|---|---|---|---|---|
| 1 | | | | | | | | |
| 2 | | | | | | | | |
| 3 | | | | | | | | |
| 4 | | | | | | | | |
| 5 | | | | | | | | |
| 6 | | | | | | | | |
| 7 | | | | | | | | |
| 8 | | | | | | | | |
| 9 | | | | | | | | |
| 10 | | | | | | | | |
| 11 | | | | | | | | |
| 12 | | | | | | | | |
| 13 | | | | | | | | |
| 14 | | | | | | | | |
| 15 | | | | | | | | |
| 16 | | | | | | | | |
| 17 | | | | | | | | |
| 18 | | | | | | | | |
| 19 | | | | | | | | |
| 20 | | | | | | | | |
| 21 | | | | | | | | |
| 22 | | | | | | | | |
| 23 | | | | | | | | |
| 24 | | | | | | | | |
| 25 | | | | | | | | |
| 26 | | | | | | | | |
| 27 | | | | | | | | |
| 28 | | | | | | | | |
| 29 | | | | | | | | |
| 30 | | | | | | | | |
| 31 | | | | | | | | |
| 32 | | | | | | | | |
| 33 | | | | | | | | |
| 34 | | | | | | | | |
| 35 | | | | | | | | |
| 36 | | | | | | | | |

## B. REKAP NILAI PER ELEMEN

| No | Nama Siswa | BK | TIK | SK | JKI | AD | AP | DSI | PLB | Rata-rata |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | | | | | | | | | | |
| 2 | | | | | | | | | | |
| 3 | | | | | | | | | | |
| dst | | | | | | | | | | |

## C. NILAI AKHIR SEMESTER

| No | Nama Siswa | Formatif (40%) | Projek (20%) | PTS (15%) | PAS/PAT (25%) | Nilai Akhir | Predikat |
|---|---|---|---|---|---|---|---|
| 1 | | | | | | | |
| 2 | | | | | | | |
| 3 | | | | | | | |
| dst | | | | | | | |

**Predikat:**  
- 92–100: Sangat Baik (A)  
- 83–91: Baik (B)  
- 75–82: Cukup (C)  
- <75: Perlu Bimbingan (D)  

---

Mengetahui,  
Kepala Sekolah

_________________________

Guru Mata Pelajaran,

Daniarsyah, S.Kom.
NIP. 198004052022211004

_________________________
"""


def remedial():
    """10_PROGRAM_REMEDIAL_PENGAYAAN.md"""
    return f"""# PROGRAM REMEDIAL & PENGAYAAN

**Mata Pelajaran** : Informatika  
**Kelas / Fase** : XI (Sebelas) / Fase F  
**Tahun Pelajaran** : 2026/2027  

---

## A. KRITERIA

| Program | Kriteria | Tindak Lanjut |
|---|---|---|
| Remedial | Nilai TP < 65 (belum tuntas) | Pembelajaran ulang + bimbingan + tes ulang |
| Pengayaan | Nilai TP ≥ 85 (sangat baik) | Pengayaan materi + proyek mandiri |

---

## B. PROGRAM REMEDIAL

| No | TP | Nama Siswa | Nilai | Bentuk Remedial | Jadwal | Nilai Akhir |
|---|---|---|---|---|---|---|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |
| 4 | | | | | | |
| 5 | | | | | | |
| 6 | | | | | | |
| 7 | | | | | | |
| 8 | | | | | | |
| 9 | | | | | | |
| 10 | | | | | | |

**Bentuk Remedial:**
1. **Pembelajaran Ulang** — Guru mengulang materi dengan metode berbeda
2. **Bimbingan Khusus** — Belajar terbimbing (tutor sebaya / guru)
3. **Tugas Tambahan** — Soal latihan terstruktur
4. **Tes Ulang** — Soal setara dengan tingkat kesulitan yang sama

---

## C. PROGRAM PENGAYAAN

| No | TP | Nama Siswa | Nilai | Bentuk Pengayaan | Target |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |
| 6 | | | | | |
| 7 | | | | | |
| 8 | | | | | |
| 9 | | | | | |
| 10 | | | | | |

**Bentuk Pengayaan:**
1. **Proyek Mandiri** — Pengembangan program/aplikasi lebih lanjut
2. **Studi Kasus Kompleks** — Masalah algoritma tingkat lanjut
3. **Mentor Sebaya** — Membantu teman yang remedial
4. **Kompetisi** — Ikut serta dalam lomba coding/IT

---

Mengetahui,  
Kepala Sekolah

_________________________

Guru Mata Pelajaran,

Daniarsyah, S.Kom.
NIP. 198004052022211004

_________________________
"""


def inventaris_lab():
    """11_INVENTARIS_LAB.md"""
    return f"""# INVENTARIS LABORATORIUM KOMPUTER

**SMA Negeri 6 Cimahi**  
**Tahun Pelajaran** : 2026/2027  

---

## A. DATA RUANG LAB

| Item | Keterangan |
|---|---|
| Nama Ruang | Laboratorium Komputer |
| Luas Ruang | |
| Kapasitas | |
| Penanggung Jawab | Daniarsyah, S.Kom. |

## B. INVENTARIS PERANGKAT KERAS

| No | Nama Barang | Merek/Tipe | Jumlah | Kondisi | Keterangan |
|---|---|---|---|---|---|
| 1 | Komputer PC (CPU + Monitor) | | | | |
| 2 | Laptop | | | | |
| 3 | Proyektor/LCD | | | | |
| 4 | Printer | | | | |
| 5 | Scanner | | | | |
| 6 | Speaker aktif | | | | |
| 7 | Mouse | | | | |
| 8 | Keyboard | | | | |
| 9 | Headphone | | | | |
| 10 | Kabel LAN | | | | |
| 11 | Switch/Hub | | | | |
| 12 | Router | | | | |
| 13 | Access Point | | | | |
| 14 | UPS | | | | |
| 15 | Stabilizer | | | | |
| 16 | Hardisk Eksternal | | | | |
| 17 | Flashdisk | | | | |
| 18 | Webcam | | | | |

## C. INVENTARIS PERANGKAT LUNAK

| No | Nama Software | Lisensi | Jumlah Lisensi | Keterangan |
|---|---|---|---|---|
| 1 | Windows OS | | | |
| 2 | Microsoft Office | | | |
| 3 | Python | Open Source | | |
| 4 | Google Chrome | Free | | |
| 5 | App Inventor (web) | Free | | |
| 6 | Cisco Packet Tracer | | | |
| 7 | Visual Studio Code | Open Source | | |
| 8 | Google Colab | Free | | |
| 9 | Canva | Free | | |
| 10 | Adobe /alternatif | | | |

## D. PERALATAN PENDUKUNG

| No | Nama Barang | Jumlah | Kondisi | Keterangan |
|---|---|---|---|---|
| 1 | Papan Tulis Whiteboard | | | |
| 2 | Meja Komputer | | | |
| 3 | Kursi Komputer | | | |
| 4 | Lemari Penyimpanan | | | |
| 5 | Kabel Roll / Terminal | | | |
| 6 | AC / Kipas | | | |
| 7 | Stop Kontak | | | |
| 8 | Tool Kit | | | |

---

Mengetahui,  
Kepala Sekolah

_________________________

Guru Mata Pelajaran / Kepala Lab,

Daniarsyah, S.Kom.
NIP. 198004052022211004

_________________________
"""


def jadwal_lab():
    """12_JADWAL_LAB_BUKU_PRAKTIK.md"""
    return f"""# JADWAL LABORATORIUM & BUKU PRAKTIK

**SMA Negeri 6 Cimahi**  
**Tahun Pelajaran** : 2026/2027  

---

## A. JADWAL PENGGUNAAN LAB KOMPUTER

| Hari | Jam ke- | Waktu | Kelas | Guru | Mata Pelajaran |
|---|---|---|---|---|---|
| Senin | 1–2 | 07.00–08.30 | | | |
| Senin | 3–4 | 08.30–10.00 | | | |
| Senin | 5–6 | 10.30–12.00 | | | |
| Selasa | 1–2 | 07.00–08.30 | | | |
| Selasa | 3–4 | 08.30–10.00 | | | |
| Selasa | 5–6 | 10.30–12.00 | | | |
| Rabu | 1–2 | 07.00–08.30 | XI | Daniarsyah, S.Kom. | Informatika |
| Rabu | 3–4 | 08.30–10.00 | XI | Daniarsyah, S.Kom. | Informatika |
| Rabu | 5–6 | 10.30–12.00 | XI | Daniarsyah, S.Kom. | Informatika |
| Kamis | 1–2 | 07.00–08.30 | | | |
| Kamis | 3–4 | 08.30–10.00 | | | |
| Kamis | 5–6 | 10.30–12.00 | | | |
| Jumat | 1–2 | 07.00–08.30 | | | |
| Jumat | 3–4 | 08.30–10.00 | | | |
| Sabtu | 1–2 | 07.00–09.00 | | | |

> **Catatan:** 5 JP Informatika kelas XI dijadwalkan pada hari Rabu (3 × 45 menit) + hari lainnya (2 × 45 menit) — dapat disesuaikan dengan jadwal sekolah.

## B. JADWAL PRAKTIK PER BAB

| Bab | Judul | Kebutuhan Lab | Software | JP |
|---|---|---|---|---|
| 1 | Tentang Informatika | — | — | 15 |
| 2 | Strategi Algoritmik & Pemrograman | Komputer/lab | Python IDLE / Google Colab | 55 |
| 3 | Berpikir Kritis & DSI | Komputer/lab (riset) | Browser, Google | 20 |
| 4 | Jaringan Komputer & Internet | Komputer/lab | Cisco Packet Tracer | 25 |
| 5 | Aplikasi Mobile + AI | Komputer/lab + HP | App Inventor (browser) | 35 |
| 6 | Proyek Analisis Data | Komputer/lab | Python, Google Colab, Sheets | 30 |

## C. BUKU PRAKTIK / LOG BOOK

| Tanggal | Kelas | Materi Praktik | JP | Perangkat Digunakan | Jumlah Siswa | Kendala | Paraf Guru |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |

---

Mengetahui,  
Kepala Sekolah

_________________________

Guru Mata Pelajaran / Kepala Lab,

Daniarsyah, S.Kom.
NIP. 198004052022211004

_________________________
"""


def generate_all():
    """Generate all 16 root documents."""
    print("=" * 60)
    print(f"GENERATOR ADMINISTRASI GURU KELAS {KELAS}")
    print(f"{SEKOLAH} \u2014 {TP}")
    print(f"{MAPEL} \u2014 Fase F \u2014 5 JP/minggu \u2014 200 JP/tahun")
    print("=" * 60)

    docs = {
        "00_COVER.md": cover(),
        "01_ANALISIS_ALOKASI_WAKTU.md": analisis_alokasi_waktu(),
        "01b_RPE_Rincian_Pekan_Efektif.md": rpe(),
        "02_PROTA.md": prota(),
        "03_PROSEM.md": prosem(),
        "04_ATP.md": atp(),
        "05_KKTP.md": kktp(),
        "06_PEMETAAN_KOMPETENSI_PENILAIAN.md": pemetaan(),
        "06b_BANK_SOAL.md": bank_soal(),
        "06c_PROGRAM_KOKURIKULER_8_DIMENSI.md": kokurikuler(),
        "07_JURNAL_MENGAJAR.md": jurnal(),
        "08_ANALISIS_CP_TP.md": analisis_cp_tp(),
        "09_DAFTAR_NILAI.md": daftar_nilai(),
        "10_PROGRAM_REMEDIAL_PENGAYAAN.md": remedial(),
        "11_INVENTARIS_LAB.md": inventaris_lab(),
        "12_JADWAL_LAB_BUKU_PRAKTIK.md": jadwal_lab(),
    }

    print("\n[1/1] Membuat 16 dokumen root...")
    count = 0
    for fname, content in docs.items():
        fp = os.path.join(BASE, fname)
        with open(fp, "w", encoding="utf-8") as f:
            f.write(content)
        count += 1
        print(f"  \u2713 {fname}")
    print(f"  \u2192 {count} file root dibuat.")
    print("=" * 60)
    print("SELESAI. Semua dokumen Kelas XI siap digunakan.")
    print("=" * 60)

if __name__ == "__main__":
    generate_all()
