#!/usr/bin/env python3
"""
Generator dokumen administrasi Guru Kelas XII — Informatika Fase F (5 JP/minggu)
Buku: Informatika untuk SMA/MA Kelas XII — Budi Permana, dkk.
Kemendikdasmen, Tahun Pelajaran 2026/2027

56 files:
  - 16 root documents
  - 40 modul ajar
"""

import os
import shutil

BASE = os.path.dirname(os.path.abspath(__file__))
MODUL_DIR = os.path.join(BASE, "modul_ajar")

GURU = "Daniarsyah, S.Kom."
NIP = "198004052022211004"
GOL = "IX"
SEKOLAH = "SMA Negeri 6 Cimahi"
MAPEL = "Informatika"
KELAS = "XII"
TP = "2026/2027"

# CP Fase F — Elemen & Capaian Pembelajaran (shared G-11 & G-12)
CP_ELEMEN = {
    "AL": "Algoritma dan Pemrograman",
    "DSI": "Dampak Sosial Informatika",
    "PLB": "Praktik Lintas Bidang",
    "TIK": "Teknologi Informasi dan Komunikasi (pemahaman konsep)",
    "SK": "Sistem Komputer",
    "JKI": "Jaringan Komputer dan Internet"
}

# CP Teks per elemen
CP_TEKS = {
    "AL": "Pada akhir fase F, peserta didik mampu menerapkan strategi algoritmik standar untuk mengembangkan program komputer yang terstruktur dalam bahasa pemrograman prosedural (C/C++) untuk Arduino, menggunakan pustaka standar, serta mampu menguji dan menyempurnakan program.",
    "DSI": "Pada akhir fase F, peserta didik mampu memahami, menganalisis, dan mengevaluasi dampak sosial informatika dalam berbagai bidang kehidupan, termasuk aspek hukum (UU ITE), etika digital, serta peran teknologi digital dalam pendidikan dan ekonomi.",
    "PLB": "Pada akhir fase F, peserta didik mampu merancang, mengimplementasikan, dan mempresentasikan solusi berbasis informatika untuk masalah nyata melalui kerja interdisipliner dengan memanfaatkan sistem komputer dan jaringan, secara kreatif, mandiri, dan kolaboratif.",
    "TIK": "Pada akhir fase F, peserta didik mampu memahami perkembangan teknologi informasi dan komunikasi terkini (IoT, Big Data, AI, Cloud Computing), literasi digital, serta dampaknya terhadap kehidupan bermasyarakat.",
    "SK": "Pada akhir fase F, peserta didik mampu memahami arsitektur dan komponen sistem komputer (SBC, mikrokontroler), menginstal dan mengkonfigurasi perangkat keras dan lunak, serta menggunakan simulator untuk mengembangkan sistem tertanam sederhana.",
    "JKI": "Pada akhir fase F, peserta didik mampu memahami konsep, topologi, dan mekanisme kerja jaringan komputer dan internet, mengkonfigurasi komponen jaringan sederhana, serta menerapkan prinsip keamanan siber (cyber security) dalam pertukaran data."
}

# 8 Dimensi Profil Lulusan
DIMENSI = [
    ("Keimanan dan Ketakwaan", "Beriman, bertakwa kepada Tuhan Yang Maha Esa, dan berakhlak mulia"),
    ("Kewargaan", "Berkebinekaan global dan cinta tanah air"),
    ("Penalaran Kritis", "Bernalar kritis dalam memproses informasi"),
    ("Kreativitas", "Kreatif dan inovatif dalam menghasilkan gagasan dan karya"),
    ("Kolaborasi", "Kolaboratif dan bergotong royong"),
    ("Kemandirian", "Mandiri dan bertanggung jawab"),
    ("Kesehatan", "Pola hidup sehat jasmani dan rohani"),
    ("Komunikasi", "Komunikatif dan efektif dalam menyampaikan gagasan")
]


# =========== BAB INFO ===========
# 5 JP/pertemuan, 200 JP/tahun
BAB = {
    "1": {
        "judul": "Informatika Sekarang dan Masa Depan",
        "jp": 20, "tm": 4,
        "sub": [
            "Konsep Literasi Digital dan Etika Bermedia Digital",
            "Revolusi Industri 4.0 dan Teknologi Digital",
            "Internet of Things (IoT) dan Big Data",
            "Kecerdasan Buatan (AI) dan Cloud Computing"
        ],
        "smt": 1,
        "cp": ["TIK"],
        "deskripsi": "Membahas literasi digital, revolusi industri 4.0, IoT, Big Data, AI, dan Cloud Computing sebagai fondasi pemahaman teknologi informasi masa kini."
    },
    "2": {
        "judul": "Sistem Komputer",
        "jp": 35, "tm": 7,
        "sub": [
            "Konsep Single Board Computer (SBC) dan Single Board Controller (SBCtrl)",
            "Pengenalan Arduino dan Mikrokontroler",
            "Instalasi IDE Arduino dan Konfigurasi Awal",
            "Komponen Penunjang Arduino (Sensor, Aktuator, Breadboard)",
            "Simulator Arduino (Wokwi, Tinkercad)",
            "Praktik: Rangkaian LED, Button, dan Sensor Sederhana",
            "Proyek Mini: Sistem Monitoring Suhu Berbasis Arduino"
        ],
        "smt": 1,
        "cp": ["SK"],
        "deskripsi": "Mempelajari SBC, mikrokontroler, Arduino, instalasi IDE, komponen penunjang, dan simulator untuk mengembangkan sistem tertanam sederhana."
    },
    "3": {
        "judul": "Berpikir Komputasional dan Algoritma Pemrograman",
        "jp": 35, "tm": 7,
        "sub": [
            "Manfaat Berpikir Komputasional dalam Kehidupan Sehari-hari",
            "Dasar Pemrograman Bahasa C untuk Arduino",
            "Struktur Dasar Program C (Variabel, Tipe Data, Operator)",
            "Struktur Kontrol: Percabangan dan Perulangan",
            "Array dan Manipulasi Data",
            "Fungsi dan Library Arduino",
            "Proyek Pennrograman: Aplikasi Kontrol Otomatis"
        ],
        "smt": 1,
        "cp": ["AL"],
        "deskripsi": "Menerapkan berpikir komputasional dan pemrograman bahasa C untuk Arduino dengan struktur dasar, array, fungsi, dan library."
    },
    "4": {
        "judul": "Jaringan Komputer dan Internet",
        "jp": 25, "tm": 5,
        "sub": [
            "Konsep Jaringan Komputer dan Klasifikasinya",
            "Topologi Jaringan dan Aspek Teknis",
            "Komponen dan Perangkat Jaringan",
            "Mekanisme Pertukaran Data (TCP/IP, UDP, DNS)",
            "Cyber Security: Ancaman dan Mitigasi Keamanan Jaringan"
        ],
        "smt": 2,
        "cp": ["JKI"],
        "deskripsi": "Memahami jaringan komputer, topologi, komponen, mekanisme pertukaran data, dan prinsip keamanan siber."
    },
    "5": {
        "judul": "Dampak Sosial Informatika",
        "jp": 25, "tm": 5,
        "sub": [
            "Peran Teknologi Digital dalam Masyarakat",
            "Media Sosial: Peluang dan Tantangan",
            "Teknologi Digital dalam Bidang Pendidikan",
            "Teknologi Digital dalam Bidang Ekonomi (E-commerce, Fintech)",
            "Undang-Undang Informasi dan Transaksi Elektronik (UU ITE)"
        ],
        "smt": 2,
        "cp": ["DSI"],
        "deskripsi": "Menganalisis dan mengevaluasi dampak sosial informatika, peran teknologi digital, media sosial, dan aspek hukum UU ITE."
    },
    "6": {
        "judul": "Praktik Lintas Bidang",
        "jp": 40, "tm": 8,
        "sub": [
            "Pengantar Proyek Lintas Bidang dan Identifikasi Masalah",
            "Perencanaan Proyek: Tujuan, Ruang Lingkup, dan Metodologi",
            "Desain Solusi dan Alokasi Sumber Daya",
            "Implementasi: Pengembangan Prototipe (IoT / Arduino / Aplikasi)",
            "Pengujian dan Perbaikan Prototipe",
            "Penyusunan Laporan dan Dokumentasi Proyek",
            "Persiapan Presentasi dan Publikasi Hasil",
            "Presentasi Proyek dan Refleksi"
        ],
        "smt": 2,
        "cp": ["PLB"],
        "deskripsi": "Proyek interdisipliner mengintegrasikan seluruh capaian pembelajaran informatika untuk menyelesaikan masalah nyata."
    }
}


def dimensi_tabel():
    lines = ["### Profil Lulusan 8 Dimensi (Deep Learning)\n"]
    lines.append("| Dimensi | Deskripsi Singkat |")
    lines.append("|---------|-------------------|")
    for d, desk in DIMENSI:
        lines.append(f"| {d} | {desk} |")
    return "\n".join(lines) + "\n"


def cover():
    return f"""# COVER ADMINISTRASI GURU

**SEKOLAH**       : {SEKOLAH}
**MATA PELAJARAN** : {MAPEL}
**KELAS**         : {KELAS}
**TAHUN PELAJARAN**: {TP}
**GURU**          : {GURU}
**NIP**           : {NIP}
**GOLONGAN**      : {GOL}

---

**Dokumen Administrasi Guru {MAPEL} Kelas {KELAS} Semester 1 & 2**
**Fase F — Capaian Pembelajaran Fase F (Kelas XI–XII)**
**Alokasi Waktu: 5 JP/minggu × 40 minggu = 200 JP/tahun**

**Buku Referensi:**
- Permana, Budi dkk. (2025). *Informatika untuk SMA/MA Kelas XII*. Jakarta: Kemendikdasristek.
- Buku digital: https://buku.kemendikdasmen.go.id/katalog/informatika-untuk-smama-kelas-xii

---

**Daftar Isi:**
1. Analisis Alokasi Waktu & RPE (Rincian Pekan Efektif)
2. PROTA (Program Tahunan)
3. PROSEM (Program Semester)
4. ATP (Alur Tujuan Pembelajaran)
5. KKTP (Kriteria Ketercapaian Tujuan Pembelajaran)
6. Pemetaan Kompetensi dan Penilaian
7. Bank Soal
8. Program Kokurikuler (8 Dimensi Profil Lulusan)
9. Jurnal Mengajar
10. Analisis CP → TP
11. Daftar Nilai
12. Program Remedial & Pengayaan
13. Inventaris Lab Komputer
14. Jadwal Lab & Buku Praktik
15. Modul Ajar (40 pertemuan)

---

{dimensi_tabel()}
"""


def analisis_alokasi_waktu():
    return f"""# ANALISIS ALOKASI WAKTU DAN RPE
**{MAPEL} — Kelas {KELAS} — {TP}**
**Fase F — 5 JP/minggu**

## A. Perhitungan Minggu Efektif

### Semester 1 (Ganjil)
| No | Bulan | Total Minggu | Minggu Tidak Efektif | Minggu Efektif | Keterangan |
|----|-------|-------------|---------------------|----------------|------------|
| 1 | Juli | 4 | 1 | 3 | Libur Idul Adha, MPLS, Libur Tahun Baru Islam |
| 2 | Agustus | 5 | 0 | 5 | |
| 3 | September | 4 | 0 | 4 | |
| 4 | Oktober | 4 | 1 | 3 | PTS Ganjil |
| 5 | November | 5 | 0 | 5 | |
| 6 | Desember | 4 | 3 | 1 | PAS, Libur Semester |
| | **Jumlah** | **26** | **5** | **21** | |

**Total Minggu Efektif S1: 21 minggu**
**Total JP Efektif S1: 21 × 5 = 105 JP**

### Semester 2 (Genap)
| No | Bulan | Total Minggu | Minggu Tidak Efektif | Minggu Efektif | Keterangan |
|----|-------|-------------|---------------------|----------------|------------|
| 1 | Januari | 5 | 0 | 5 | |
| 2 | Februari | 4 | 0 | 4 | |
| 3 | Maret | 4 | 0 | 4 | |
| 4 | April | 4 | 0 | 4 | |
| 5 | Mei | 4 | 1 | 3 | PAT |
| 6 | Juni | 4 | 4 | 0 | Libur Kenaikan Kelas |
| | **Jumlah** | **25** | **5** | **20** | |

**Total Minggu Efektif S2: 20 minggu**
**Total JP Efektif S2: 20 × 5 = 100 JP**

### Total Tahunan
- Minggu Efektif: 21 + 20 = **41 minggu** (digunakan 40 minggu)
- JP Efektif: 105 + 100 = **205 JP** (dialokasikan 200 JP)
- Cadangan: 5 JP (untuk fleksibilitas dan review tambahan)

## B. RPE — Rincian Pekan Efektif

### Semester 1 (Ganjil)
| Pekan Ke- | Bulan | Kegiatan | JP | Keterangan |
|-----------|-------|----------|----|------------|
| 1 | Juli | Bab 1: Pertemuan 1 | 5 | Literasi Digital |
| 2 | Juli | Bab 1: Pertemuan 2 | 5 | Revolusi Industri 4.0 |
| 3 | Juli | Bab 1: Pertemuan 3 | 5 | IoT & Big Data |
| 4 | Agt | Bab 1: Pertemuan 4 | 5 | AI & Cloud Computing |
| 5 | Agt | Bab 2: Pertemuan 1 | 5 | SBC & SBCtrl |
| 6 | Agt | Bab 2: Pertemuan 2 | 5 | Arduino & Mikrokontroler |
| 7 | Agt | Bab 2: Pertemuan 3 | 5 | Instalasi IDE Arduino |
| 8 | Sep | Bab 2: Pertemuan 4 | 5 | Komponen Penunjang |
| 9 | Sep | Bab 2: Pertemuan 5 | 5 | Simulator Arduino |
| 10 | Sep | Bab 2: Pertemuan 6 | 5 | Praktik Rangkaian Dasar |
| 11 | Sep | Bab 2: Pertemuan 7 | 5 | Proyek Mini Sistem Monitoring |
| 12 | Okt | **Review + PTS** | 5 | Ulangan Tengah Semester |
| 13 | Okt | Bab 3: Pertemuan 1 | 5 | Manfaat Berpikir Komputasional |
| 14 | Okt | Bab 3: Pertemuan 2 | 5 | Dasar Pemrograman C Arduino |
| 15 | Okt | Bab 3: Pertemuan 3 | 5 | Struktur Dasar Program C |
| 16 | Nov | Bab 3: Pertemuan 4 | 5 | Struktur Kontrol |
| 17 | Nov | Bab 3: Pertemuan 5 | 5 | Array dan Manipulasi Data |
| 18 | Nov | Bab 3: Pertemuan 6 | 5 | Fungsi dan Library Arduino |
| 19 | Nov | Bab 3: Pertemuan 7 | 5 | Proyek Pemrograman |
| 20 | Des | **Review** | 5 | Review akhir semester |
| 21 | Des | **PAS** | 5 | Penilaian Akhir Semester |
| | | **Total S1** | **105** | |

### Semester 2 (Genap)
| Pekan Ke- | Bulan | Kegiatan | JP | Keterangan |
|-----------|-------|----------|----|------------|
| 1 | Jan | Bab 4: Pertemuan 1 | 5 | Konsep & Klasifikasi Jaringan |
| 2 | Jan | Bab 4: Pertemuan 2 | 5 | Topologi Jaringan |
| 3 | Jan | Bab 4: Pertemuan 3 | 5 | Komponen Jaringan |
| 4 | Jan | Bab 4: Pertemuan 4 | 5 | Mekanisme Pertukaran Data |
| 5 | Jan | Bab 4: Pertemuan 5 | 5 | Cyber Security |
| 6 | Feb | Bab 5: Pertemuan 1 | 5 | Peran Teknologi Digital |
| 7 | Feb | Bab 5: Pertemuan 2 | 5 | Media Sosial |
| 8 | Feb | Bab 5: Pertemuan 3 | 5 | Teknologi Digital & Pendidikan |
| 9 | Feb | Bab 5: Pertemuan 4 | 5 | Teknologi Digital & Ekonomi |
| 10 | Mar | Bab 5: Pertemuan 5 | 5 | UU ITE |
| 11 | Mar | Bab 6: Pertemuan 1 | 5 | Pengantar & Identifikasi Masalah |
| 12 | Mar | Bab 6: Pertemuan 2 | 5 | Perencanaan Proyek |
| 13 | Mar | Bab 6: Pertemuan 3 | 5 | Desain Solusi |
| 14 | Apr | Bab 6: Pertemuan 4 | 5 | Implementasi Prototipe |
| 15 | Apr | Bab 6: Pertemuan 5 | 5 | Implementasi Prototipe (lanj.) |
| 16 | Apr | Bab 6: Pertemuan 6 | 5 | Pengujian & Perbaikan |
| 17 | Apr | Bab 6: Pertemuan 7 | 5 | Laporan & Dokumentasi |
| 18 | Mei | Bab 6: Pertemuan 8 | 5 | Presentasi & Refleksi |
| 19 | Mei | **Review** | 5 | Review akhir semester |
| 20 | Mei | **PAT** | 5 | Penilaian Akhir Tahun |
| | | **Total S2** | **100** | |

**Total JP Tahunan: 105 + 100 = 205 JP (digunakan ~200 JP)**
"""


def prota():
    return f"""# PROGRAM TAHUNAN (PROTA)
**{MAPEL} — Kelas {KELAS} — {TP}**
**Fase F — 5 JP/minggu — 200 JP/tahun**

| Semester | Bab | Materi | JP | Jumlah JP |
|----------|-----|--------|----|-----------|
| 1 (Ganjil) | 1 | Informatika Sekarang dan Masa Depan | 20 | |
| | 2 | Sistem Komputer | 35 | |
| | 3 | Berpikir Komputasional dan Algoritma Pemrograman | 35 | |
| | | Review + PTS | 10 | 100 |
| 2 (Genap) | 4 | Jaringan Komputer dan Internet | 25 | |
| | 5 | Dampak Sosial Informatika | 25 | |
| | 6 | Praktik Lintas Bidang | 40 | |
| | | Review + PAT | 10 | 100 |
| | | **Total** | | **200** |

**Distribusi per Elemen CP:**
| Elemen CP | Bab Terkait | JP |
|-----------|-------------|-----|
| Teknologi Informasi dan Komunikasi (TIK) | Bab 1 | 20 |
| Sistem Komputer (SK) | Bab 2 | 35 |
| Algoritma dan Pemrograman (AL) | Bab 3 | 35 |
| Jaringan Komputer dan Internet (JKI) | Bab 4 | 25 |
| Dampak Sosial Informatika (DSI) | Bab 5 | 25 |
| Praktik Lintas Bidang (PLB) | Bab 6 | 40 |
| Review + PTS/PAT | | 20 |
| **Total** | | **200** |

**Guru Pengampu:** {GURU}
**NIP:** {NIP}
"""


def prosem():
    lines = [f"# PROGRAM SEMESTER (PROSEM)\n**{MAPEL} — Kelas {KELAS} — {TP}**\n**Fase F — 5 JP/minggu**\n"]

    for smt in [1, 2]:
        label = "Ganjil" if smt == 1 else "Genap"
        lines.append(f"\n## Semester {label}\n")
        lines.append("| No | Bab | Judul Materi | JP | JP Kumulatif |")
        lines.append("|----|-----|--------------|----|--------------|")
        no = 0
        kumulatif = 0
        for k in sorted(BAB.keys()):
            b = BAB[k]
            if b["smt"] == smt:
                for i, sub in enumerate(b["sub"]):
                    no += 1
                    kumulatif += 5
                    label_bab = f"{k}.{i+1}"
                    lines.append(f"| {no} | {label_bab} | {sub} | 5 | {kumulatif} |")
        if smt == 1:
            no += 1; lines.append(f"| {no} | - | Review + PTS | 10 | {kumulatif + 10} |")
        else:
            no += 1; lines.append(f"| {no} | - | Review + PAT | 10 | {kumulatif + 10} |")
    return "\n".join(lines) + "\n"


def atp():
    lines = [f"# ALUR TUJUAN PEMBELAJARAN (ATP)\n**{MAPEL} — Kelas {KELAS} — {TP}**\n**Fase F**\n"]

    tp_counter = 0
    for k in sorted(BAB.keys()):
        b = BAB[k]
        cp_labels = ", ".join(f"{cp}: {CP_ELEMEN[cp]}" for cp in b["cp"])
        lines.append(f"\n### Bab {k}: {b['judul']}\n")
        lines.append(f"**Capaian Pembelajaran Terkait:** {cp_labels}")
        lines.append(f"**Alokasi Waktu:** {b['jp']} JP\n")
        lines.append("| No TP | Tujuan Pembelajaran | JP | Elemen |")
        lines.append("|-------|-------------------|----|--------|")
        for i, sub in enumerate(b["sub"]):
            tp_counter += 1
            tp_id = f"{k}.{i+1}"
            lines.append(f"| {tp_id} | {sub} | 5 | {b['cp'][0]} |")
        lines.append("")
    return "\n".join(lines) + "\n"


def kktp():
    lines = [f"# KRITERIA KETERCAPAIAN TUJUAN PEMBELAJARAN (KKTP)\n**{MAPEL} — Kelas {KELAS} — {TP}**\n"]

    lines.append("**Interval Nilai:**")
    lines.append("| Predikat | Rentang Nilai | Keterangan |")
    lines.append("|----------|---------------|------------|")
    lines.append("| Sangat Baik (A) | 90–100 | Melampaui ekspektasi |")
    lines.append("| Baik (B) | 78–89 | Memenuhi ekspektasi |")
    lines.append("| Cukup (C) | 65–77 | Belum sepenuhnya memenuhi |")
    lines.append("| Kurang (D) | <65 | Perlu remedial |")

    lines.append("\n## KKTP per Tujuan Pembelajaran\n")
    lines.append("| No TP | Tujuan Pembelajaran | Indikator Ketercapaian | KKTP |")
    lines.append("|-------|-------------------|------------------------|------|")
    tp_counter = 0
    for k in sorted(BAB.keys()):
        b = BAB[k]
        for i, sub in enumerate(b["sub"]):
            tp_counter += 1
            tp_id = f"{k}.{i+1}"
            indikator = f"Peserta didik mampu menjelaskan dan menerapkan konsep {sub.lower()}"
            lines.append(f"| {tp_id} | {sub} | {indikator} | ≥78 |")
    return "\n".join(lines) + "\n"


def pemetaan():
    lines = [f"# PEMETAAN KOMPETENSI DAN PENILAIAN\n**{MAPEL} — Kelas {KELAS} — {TP}**\n"]

    lines.append("| Bab | Judul | JP | Teknik Penilaian | Bentuk Instrumen |")
    lines.append("|-----|-------|----|-----------------|-------------------|")
    for k in sorted(BAB.keys()):
        b = BAB[k]
        teknik = "Tes Tulis, Observasi, Produk"
        if k in ["2", "3", "6"]:
            teknik = "Tes Tulis, Praktik, Produk, Observasi"
        elif k == "4":
            teknik = "Tes Tulis, Praktik, Observasi"
        elif k == "5":
            teknik = "Tes Tulis, Diskusi, Produk (Essay)"
        instrumen = "Soal PG/Uraian, Rubrik Praktik, Rubrik Proyek"
        if k == "6":
            instrumen = "Rubrik Proyek, Rubrik Presentasi, Laporan"
        lines.append(f"| {k} | {b['judul']} | {b['jp']} | {teknik} | {instrumen} |")

    lines.append("\n\n### Rincian Teknik Penilaian\n")
    lines.append("**1. Penilaian Sikap (Observasi)**")
    lines.append("- Observasi harian melalui jurnal sikap (8 dimensi Profil Lulusan)")
    lines.append("- Format: catatan anekdotal\n")
    lines.append("**2. Penilaian Pengetahuan (Tes Tulis)**")
    lines.append("- Pilihan Ganda, Isian Singkat, Uraian")
    lines.append("- Dilaksanakan setiap akhir bab (formatif) dan PTS/PAT (sumatif)\n")
    lines.append("**3. Penilaian Keterampilan (Praktik/Produk/Proyek)**")
    lines.append("- Praktik Arduino (Bab 2-3)")
    lines.append("- Proyek Internet/Jaringan (Bab 4)")
    lines.append("- Proyek Lintas Bidang (Bab 6)")
    return "\n".join(lines) + "\n"


def bank_soal():
    return f"""# BANK SOAL
**{MAPEL} — Kelas {KELAS} — {TP}**
**Fase F — 200 JP/tahun**

## Daftar Soal per Bab

### Bab 1: Informatika Sekarang dan Masa Depan
1. Jelaskan apa yang dimaksud dengan literasi digital dan sebutkan 4 pilar utamanya!
2. Bagaimana revolusi industri 4.0 mengubah pola kerja manusia? Berikan 3 contoh!
3. Apa perbedaan antara IoT dan Big Data? Jelaskan hubungan keduanya!
4. Sebutkan dan jelaskan 3 contoh penerapan AI dalam kehidupan sehari-hari!
5. Apa keuntungan penggunaan Cloud Computing bagi perusahaan? Sebutkan minimal 3!
6. **Soal HOTS:** Bagaimana dampak perkembangan AI terhadap dunia pendidikan di Indonesia? Analisis peluang dan tantangannya!
7. **Soal HOTS:** Jika Anda diminta merancang solusi IoT untuk mengatasi kemacetan di kota besar, komponen apa saja yang dibutuhkan dan bagaimana cara kerjanya?

### Bab 2: Sistem Komputer
1. Jelaskan perbedaan antara Single Board Computer (SBC) dan Single Board Controller (SBCtrl)!
2. Sebutkan minimal 3 contoh SBC dan 3 contoh SBCtrl yang kamu ketahui!
3. Apa fungsi utama Arduino dalam sistem tertanam (embedded system)?
4. Jelaskan langkah-langkah instalasi IDE Arduino pada sistem operasi Linux!
5. Sebutkan 3 komponen penunjang Arduino beserta fungsinya!
6. **Soal HOTS:** Anda ingin membuat alat monitoring suhu ruangan menggunakan Arduino. Buatlah desain sederhana yang mencakup komponen yang dibutuhkan, rangkaian dasar, dan prinsip kerjanya!
7. **Soal HOTS:** Bandingkan kelebihan dan kekurangan penggunaan simulator (Wokwi/Tinkercad) vs perangkat fisik Arduino dalam pembelajaran sistem tertanam!

### Bab 3: Berpikir Komputasional dan Algoritma Pemrograman
1. Sebutkan 4 pilar berpikir komputasional dan berikan contoh penerapannya!
2. Apa yang dimaksud dengan variabel dan tipe data dalam bahasa C?
3. Jelaskan perbedaan antara perulangan for dan while dalam bahasa C!
4. Bagaimana cara mendeklarasikan array satu dimensi dalam bahasa C?
5. Apa fungsi library dalam pemrograman Arduino? Sebutkan 2 contoh!
6. **Soal HOTS:** Buatlah program C untuk Arduino yang membaca nilai sensor suhu (LM35) dan menyalakan LED hijau jika suhu < 30°C, LED kuning jika 30-35°C, dan LED merah jika > 35°C!
7. **Soal HOTS:** Sebuah program Arduino perlu mengontrol 3 LED yang menyala bergantian setiap 500ms. Buatlah algoritma dan programnya menggunakan array!

### Bab 4: Jaringan Komputer dan Internet
1. Jelaskan perbedaan antara jaringan LAN, MAN, dan WAN!
2. Sebutkan dan gambarkan 3 jenis topologi jaringan!
3. Apa fungsi router, switch, dan modem dalam jaringan komputer?
4. Jelaskan perbedaan protokol TCP dan UDP dalam pertukaran data!
5. Sebutkan 3 jenis ancaman keamanan siber dan cara mitigasinya!
6. **Soal HOTS:** Sebuah sekolah ingin membangun jaringan komputer yang menghubungkan 3 gedung. Desainlah topologi yang paling efisien dengan mempertimbangkan biaya, kecepatan, dan keamanan!
7. **Soal HOTS:** Bagaimana mekanisme serangan DDoS dapat melumpuhkan sebuah server? Jelaskan langkah-langkah mitigasi yang dapat dilakukan!

### Bab 5: Dampak Sosial Informatika
1. Bagaimana peran teknologi digital dalam meningkatkan kualitas pendidikan di Indonesia?
2. Apa dampak positif dan negatif media sosial bagi remaja?
3. Jelaskan bagaimana e-commerce dan fintech mengubah pola ekonomi masyarakat!
4. Sebutkan 5 hal yang diatur dalam UU ITE terkait penyebaran informasi digital!
5. **Soal HOTS:** Analisislah dampak maraknya hoaks di media sosial terhadap stabilitas sosial dan politik di Indonesia. Berikan solusi berbasis teknologi dan edukasi!
6. **Soal HOTS:** Bagaimana seharusnya keseimbangan antara kebebasan berekspresi di internet dan perlindungan data pribadi diatur?

### Bab 6: Praktik Lintas Bidang
1. Jelaskan langkah-langkah dalam merancang proyek lintas bidang!
2. Bagaimana cara mengidentifikasi masalah yang dapat diselesaikan dengan solusi berbasis informatika?
3. **Soal Proyek:** Buatlah prototipe sistem monitoring kualitas udara berbasis Arduino yang terintegrasi dengan aplikasi berbasis web! Sertakan: rumusan masalah, desain, implementasi, dan rencana pengujian!
4. **Soal HOTS:** Evaluasilah proyek yang telah Anda buat. Identifikasi 3 kelemahan dan berikan saran perbaikan yang spesifik dan terukur!
"""


def kokurikuler():
    return f"""# PROGRAM KOKURIKULER — 8 DIMENSI PROFIL LULUSAN
**{MAPEL} — Kelas {KELAS} — {TP}**
**Model Deep Learning**

## Matriks Integrasi 8 Dimensi dalam Pembelajaran Informatika

| Dimensi | Deskripsi | Implementasi dalam Pembelajaran | Bab Terkait |
|---------|-----------|--------------------------------|-------------|
| Keimanan & Ketakwaan | Beriman, bertakwa, dan berakhlak mulia | Etika penggunaan teknologi, tanggung jawab moral dalam bermedia digital | 1, 5 |
| Kewargaan | Berkebinekaan global, cinta tanah air | Literasi digital kebangsaan, analisis UU ITE, kontribusi teknologi untuk Indonesia | 1, 5 |
| Penalaran Kritis | Bernalar kritis | Analisis algoritma, debugging program, evaluasi keamanan jaringan | 2, 3, 4 |
| Kreativitas | Kreatif dan inovatif | Merancang solusi IoT, programming kreatif, proyek lintas bidang | 2, 3, 6 |
| Kolaborasi | Bergotong royong | Kerja kelompok proyek, diskusi, presentasi bersama | 6 |
| Kemandirian | Mandiri dan bertanggung jawab | Praktik mandiri Arduino, eksplorasi simulator, tugas individu | 1, 2, 3 |
| Kesehatan | Pola hidup sehat | Ergonomi penggunaan komputer, manajemen waktu digital, screen time | 1, 5 |
| Komunikasi | Komunikatif dan efektif | Presentasi proyek, laporan tertulis, diskusi kelas | 6 |

## Kegiatan Kokurikuler

| Kegiatan | Bentuk | JP | Dimensi Terkait |
|----------|--------|----|-----------------|
| Diskusi Etika Digital & AI | Diskusi panel kelas | 2 JP | Keimanan, Kewargaan, Penalaran Kritis |
| Proyek IoT Sederhana | Praktik lab | 10 JP | Kreativitas, Kolaborasi, Kemandirian |
| Simulasi Keamanan Jaringan | Praktik lab | 5 JP | Penalaran Kritis, Kolaborasi |
| Debat Dampak Media Sosial | Debat kelas | 3 JP | Penalaran Kritis, Komunikasi, Kewargaan |
| Pameran Proyek Lintas Bidang | Presentasi publik | 5 JP | Kreativitas, Komunikasi, Kolaborasi |
"""


def jurnal():
    lines = [f"# JURNAL MENGAJAR\n**{MAPEL} — Kelas {KELAS} — {TP}**\n"]

    lines.append("Format:\n")
    lines.append("| Pertemuan | Tanggal | Bab | Materi | JP | Kehadiran | Ket. |")
    lines.append("|-----------|---------|-----|--------|----|-----------|------|")
    pert = 0
    for k in sorted(BAB.keys()):
        b = BAB[k]
        for i, sub in enumerate(b["sub"]):
            pert += 1
            bab_label = f"Bab {k}"
            lines.append(f"| {pert} | | {bab_label} | {sub} | 5 | | |")
    # Review + PTS/PAT
    pert += 1; lines.append(f"| {pert} | | - | Review Semester 1 | 5 | | |")
    pert += 1; lines.append(f"| {pert} | | - | PTS Ganjil | 5 | | |")
    pert += 1; lines.append(f"| {pert} | | - | Review Semester 2 | 5 | | |")
    pert += 1; lines.append(f"| {pert} | | - | PAT Genap | 5 | | |")
    return "\n".join(lines) + "\n"


def analisis_cp_tp():
    lines = [f"# ANALISIS CP → TP\n**{MAPEL} — Kelas {KELAS} — {TP}**\n**Fase F**\n"]

    for k in sorted(BAB.keys()):
        b = BAB[k]
        cp_labels = ", ".join(f"{cp}: {CP_ELEMEN[cp]}" for cp in b["cp"])
        cp_teks = "\n".join(f"{CP_TEKS[cp]}" for cp in b["cp"])
        lines.append(f"### Bab {k}: {b['judul']}\n")
        lines.append(f"**Elemen CP:** {cp_labels}\n")
        lines.append(f"**Capaian Pembelajaran:**\n{cp_teks}\n")
        lines.append("**Tujuan Pembelajaran:**")
        for i, sub in enumerate(b["sub"]):
            lines.append(f"- TP {k}.{i+1}: {sub}")
        lines.append("")
    return "\n".join(lines) + "\n"


def daftar_nilai():
    return f"""# DAFTAR NILAI
**{MAPEL} — Kelas {KELAS} — {TP}**

## Format Penilaian

| No | Nama Peserta Didik | Nilai Harian (Rata-rata) | PTS | PAS/PAT | Nilai Akhir | Predikat |
|----|-------------------|------------------------|-----|---------|-------------|----------|
| 1 | | | | | | |
| 2 | | | | | | |
| ... | | | | | | |

**Keterangan:**
- Nilai Harian = Rata-rata nilai formatif per bab (tes tulis + praktik/produk)
- PTS = Nilai Penilaian Tengah Semester
- PAS/PAT = Nilai Penilaian Akhir Semester/Akhir Tahun
- Nilai Akhir = (40% × Nilai Harian) + (30% × PTS) + (30% × PAS/PAT)

## Rubrik Konversi Nilai
| Predikat | Rentang |
|----------|---------|
| A (Sangat Baik) | 90–100 |
| B (Baik) | 78–89 |
| C (Cukup) | 65–77 |
| D (Kurang) | <65 |
"""


def remedial():
    return f"""# PROGRAM REMEDIAL DAN PENGAYAAN
**{MAPEL} — Kelas {KELAS} — {TP}**

## A. Program Remedial

### Kriteria Remedial
- Peserta didik dengan nilai < 78 (KKTP) wajib mengikuti remedial

### Bentuk Remedial
| Bentuk | Deskripsi | Waktu |
|--------|-----------|-------|
| Pembelajaran Ulang | Bimbingan khusus materi yang belum tuntas | Di luar JP |
| Bimbingan Perorangan | Tutorial individu/pasangan | Saat JP atau luar JP |
| Penugasan | Tugas terstruktur tambahan | Luar JP |
| Tutor Sebaya | Bantuan teman yang sudah tuntas | Saat JP |

### Jadwal Remedial
| Bab | Materi | Bentuk Remedial | Target |
|-----|--------|----------------|--------|
| 1 | Informatika Sekarang dan Masa Depan | Penugasan + Bimbingan | Semua mencapai KKTP |
| 2 | Sistem Komputer | Praktik ulang | Semua mencapai KKTP |
| 3 | Berpikir Komputasional & Algoritma | Bimbingan + Praktik | Semua mencapai KKTP |
| 4 | Jaringan Komputer dan Internet | Penugasan | Semua mencapai KKTP |
| 5 | Dampak Sosial Informatika | Bimbingan | Semua mencapai KKTP |
| 6 | Praktik Lintas Bidang | Perbaikan proyek | Semua mencapai KKTP |

## B. Program Pengayaan

### Kriteria Pengayaan
- Peserta didik dengan nilai > 89 mengikuti program pengayaan

### Bentuk Pengayaan
| Jenis | Kegiatan |
|-------|----------|
| Eksplorasi Mandiri | Mengeksplorasi topik lanjutan (AI/ML, cyber security tingkat lanjut) |
| Proyek Tambahan | Membuat proyek mandiri dengan tingkat kesulitan lebih tinggi |
| Tutor Sebaya | Membantu teman yang mengalami kesulitan |
| Kompetisi | Persiapan lomba/olimpiade informatika |

### Topik Pengayaan
1. Pengembangan aplikasi IoT lanjutan dengan cloud integration
2. Implementasi machine learning sederhana pada Arduino
3. Ethical hacking dan penetration testing dasar
4. Pembuatan aplikasi web/ mobile untuk monitoring IoT
"""


def inventaris_lab():
    return f"""# INVENTARIS LABORATORIUM KOMPUTER
**{MAPEL} — {SEKOLAH} — {TP}**

| No | Nama Barang | Jumlah | Kondisi | Keterangan |
|----|-------------|--------|---------|------------|
| 1 | Komputer/PC | | | |
| 2 | Laptop | | | |
| 3 | Monitor | | | |
| 4 | Keyboard | | | |
| 5 | Mouse | | | |
| 6 | Headphone | | | |
| 7 | Arduino Board (Uno/Mega) | | | |
| 8 | Sensor Kit Arduino | | | |
| 9 | Breadboard + Kabel Jumper | | | |
| 10 | LED + Resistor | | | |
| 11 | Router WiFi | | | |
| 12 | Switch/Hub | | | |
| 13 | Kabel LAN (UTP) | | | |
| 14 | Proyektor | | | |
| 15 | Speaker Aktif | | | |
| 16 | UPS/Stabilizer | | | |
| 17 | AC Ruangan | | | |
| 18 | Papan Tulis Whiteboard | | | |

**Catatan:** *) Diisi sesuai kondisi aktual laboratorium
"""


def jadwal_lab():
    return f"""# JADWAL LABORATORIUM DAN BUKU PRAKTIK
**{MAPEL} — {SEKOLAH} — {TP}**

## A. Jadwal Penggunaan Lab Komputer
| Hari | Jam Ke- | Kelas | Kegiatan | Guru |
|------|---------|-------|----------|------|
| | | | | |

*Diisi sesuai jadwal yang ditetapkan sekolah*

## B. Buku Praktik
| No | Tanggal | Kelas | Materi Praktik | Paraf Guru | Parah Siswa |
|----|---------|-------|----------------|------------|-------------|
| | | | | | |

## C. Panduan Praktik

### Praktik 1: Arduino — Rangkaian LED Sederhana (Bab 2)
- **Tujuan:** Membuat LED menyala menggunakan Arduino
- **Alat:** Arduino Uno, Breadboard, LED, Resistor 220Ω, Kabel Jumper
- **Software:** Arduino IDE / Wokwi Simulator

### Praktik 2: Arduino — Sensor Suhu (Bab 3)
- **Tujuan:** Membaca nilai sensor suhu LM35 dan menampilkan di Serial Monitor
- **Alat:** Arduino Uno, Sensor LM35, Breadboard, Kabel Jumper
- **Software:** Arduino IDE

### Praktik 3: Konfigurasi Jaringan Sederhana (Bab 4)
- **Tujuan:** Menghubungkan 2 komputer dalam satu jaringan lokal
- **Alat:** 2 PC/Laptop, Kabel LAN, Switch
- **Software:** Command Prompt / Terminal
"""


# =========== MODUL AJAR ===========

def generate_modul_ajar(bab_id, bab_data, pertemuan, total_pertemuan, sub_judul, semester):
    """Generate one modul ajar markdown file."""
    hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jum'at"]
    fase = "F"
    alokasi = "5 JP × 45 menit = 225 menit"

    cp_elemen_list = [f"{cp}: {CP_ELEMEN[cp]}" for cp in bab_data["cp"]]
    cp_teks_list = [f"- {CP_TEKS[cp]}" for cp in bab_data["cp"]]

    # TP list
    tp_list = "\n".join([f"- {bab_id}.{i+1}. Peserta didik mampu menjelaskan dan menerapkan {sub.lower()}"
                        for i, sub in enumerate(bab_data["sub"])])

    # Learning objectives for this pertemuan
    tp_ini = f"{bab_id}.{pertemuan}. Peserta didik mampu memahami dan menerapkan konsep {sub_judul.lower()}"

    # Prerequisites
    if pertemuan == 1:
        prasyarat = "Peserta didik telah memiliki pemahaman dasar tentang informatika dan teknologi informasi dari kelas sebelumnya."
    else:
        prasyarat = f"Peserta didik telah menguasai materi pertemuan sebelumnya pada Bab {bab_id}."

    # Activities based on the type of lesson
    is_praktik = any(kata in sub_judul.lower() for kata in ["praktik", "proyek", "simulator", "instalasi", "prototipe"])
    is_teori = not is_praktik and pertemuan <= total_pertemuan - 2
    is_proyek = "proyek" in sub_judul.lower()

    if is_proyek:
        kegiatan = f"""
**Pendahuluan (20 menit)**
1. Guru membuka pelajaran, doa, dan presensi
2. Apersepsi: mengaitkan proyek dengan permasalahan nyata di lingkungan sekitar
3. Motivasi: pentingnya solusi berbasis informatika untuk kehidupan sehari-hari
4. Guru menyampaikan TP dan skenario pembelajaran proyek

**Inti (175 menit) — Model PjBL (Project Based Learning)**
1. **Penentuan Pertanyaan Mendasar** (20 menit): Peserta didik mengidentifikasi masalah dan menentukan topik proyek
2. **Mendesain Perencanaan Proyek** (30 menit): Kelompok menyusun rencana kerja, jadwal, dan pembagian tugas
3. **Menyusun Jadwal** (15 menit): Membuat timeline penyelesaian proyek
4. **Memonitor Kemajuan Proyek** (60 menit): Peserta didik mengerjakan proyek, guru memfasilitasi dan memonitor
5. **Menguji Hasil** (30 menit): Pengujian awal prototipe dan dokumentasi
6. **Evaluasi Pengalaman** (20 menit): Refleksi proses dan kendala yang dihadapi

**Penutup (30 menit)**
1. Peserta didik mempresentasikan perkembangan proyek
2. Guru memberikan umpan balik dan penguatan
3. Menyepakati target penyelesaian proyek untuk pertemuan berikutnya
4. Refleksi pembelajaran hari ini
5. Doa dan penutup
"""
    elif is_praktik:
        kegiatan = f"""
**Pendahuluan (20 menit)**
1. Guru membuka pelajaran, doa, dan presensi
2. Apersepsi: mengingatkan kembali materi teori yang mendasari praktik
3. Demonstrasi singkat langkah-langkah praktik oleh guru
4. Guru menyampaikan tujuan praktik dan prosedur keselamatan kerja
5. Pembagian kelompok dan alat/bahan praktik

**Inti (175 menit) — Model PBL (Problem Based Learning) + Discovery Learning**
1. **Orientasi pada Masalah** (15 menit): Guru menyajikan skenario masalah yang relevan
2. **Mengorganisasi Belajar** (20 menit): Peserta didik membaca modul/buku petunjuk praktik
3. **Membimbing Penyelidikan** (60 menit): Peserta didik melakukan praktik secara berkelompok, guru memfasilitasi
4. **Mengembangkan dan Menyajikan Hasil** (40 menit): Setiap kelompok mencatat hasil dan menyiapkan presentasi singkat
5. **Menganalisis dan Mengevaluasi** (40 menit): Presentasi hasil, diskusi, dan umpan balik

**Penutup (30 menit)**
1. Guru memberikan penguatan dan koreksi terhadap hasil praktik
2. Menyimpulkan hasil praktik dan keterkaitan dengan konsep
3. Tugas: membuat laporan praktik
4. Refleksi pembelajaran hari ini
5. Doa dan penutup
"""
    else:
        kegiatan = f"""
**Pendahuluan (20 menit)**
1. Guru membuka pelajaran dengan salam, doa, dan presensi
2. Apersepsi: mengaitkan materi dengan pengalaman peserta didik atau materi sebelumnya
3. Pertanyaan pemantik untuk membangkitkan rasa ingin tahu
4. Guru menyampaikan tujuan pembelajaran dan skenario kegiatan

**Inti (175 menit) — Model Discovery Learning + Cooperative Learning**
1. **Stimulation** (20 menit): Peserta didik mengamati tayangan/gambar/artikel terkait materi
2. **Problem Statement** (25 menit): Guru memberikan pertanyaan-pertanyaan kunci
3. **Data Collection** (50 menit): Peserta didik mengumpulkan informasi dari buku dan sumber digital
4. **Data Processing** (40 menit): Diskusi kelompok untuk mengolah dan menganalisis informasi
5. **Verification** (20 menit): Verifikasi hasil diskusi dengan referensi dan bimbingan guru
6. **Generalization** (20 menit): Menarik kesimpulan bersama

**Penutup (30 menit)**
1. Guru bersama peserta didik menyimpulkan materi
2. Evaluasi formatif (kuis/pertanyaan lisan)
3. Tugas mandiri untuk pertemuan berikutnya
4. Refleksi pembelajaran
5. Doa dan penutup
"""

    # Assessment
    if is_proyek:
        assessment = """| Aspek | Teknik Penilaian | Instrumen |
|-------|-----------------|-----------|
| Sikap | Observasi | Rubrik sikap (8 dimensi) |
| Pengetahuan | Tes Tulis | Soal uraian terkait proyek |
| Keterampilan | Produk/Proyek | Rubrik proyek, rubrik presentasi |"""
    elif is_praktik:
        assessment = """| Aspek | Teknik Penilaian | Instrumen |
|-------|-----------------|-----------|
| Sikap | Observasi | Rubrik sikap (disiplin, kerjasama) |
| Pengetahuan | Tes Tulis | Soal uraian singkat |
| Keterampilan | Kinerja/Praktik | Rubrik praktik, ceklist |"""
    else:
        assessment = """| Aspek | Teknik Penilaian | Instrumen |
|-------|-----------------|-----------|
| Sikap | Observasi | Rubrik sikap (keaktifan, tanggung jawab) |
| Pengetahuan | Tes Tulis | Kuis, soal uraian |
| Keterampilan | - | - |"""

    # 8 Dimensi for this pertemuan
    if is_proyek:
        dimensi_fokus = "Kolaborasi, Kreativitas, Komunikasi, Penalaran Kritis, Kemandirian"
    elif is_praktik:
        dimensi_fokus = "Kemandirian, Penalaran Kritis, Kolaborasi, Kreativitas"
    else:
        dimensi_fokus = "Penalaran Kritis, Komunikasi, Keimanan & Ketakwaan, Kewargaan"

    # Glossarium based on bab
    if bab_id == "1":
        glos = "- **Literasi Digital**: kemampuan memahami dan menggunakan teknologi informasi dan komunikasi secara efektif, etis, dan kritis\n- **IoT**: Internet of Things, jaringan perangkat fisik yang terhubung ke internet\n- **Big Data**: kumpulan data berukuran sangat besar yang memerlukan teknologi khusus untuk mengolahnya\n- **AI**: Artificial Intelligence, kecerdasan buatan yang mensimulasikan kecerdasan manusia\n- **Cloud Computing**: model komputasi berbasis internet yang menyediakan sumber daya sesuai permintaan"
    elif bab_id == "2":
        glos = "- **SBC**: Single Board Computer, komputer lengkap dalam satu papan sirkuit (Raspberry Pi)\n- **SBCtrl**: Single Board Controller, mikrokontroler dalam satu papan (Arduino)\n- **Arduino**: platform prototyping elektronik open-source berbasis mikrokontroler\n- **IDE**: Integrated Development Environment, perangkat lunak untuk menulis dan mengunggah program\n- **Sensor**: perangkat yang mendeteksi perubahan lingkungan fisik\n- **Aktuator**: perangkat yang mengubah sinyal listrik menjadi gerakan fisik"
    elif bab_id == "3":
        glos = "- **Berpikir Komputasional**: metode pemecahan masalah dengan menerapkan konsep ilmu komputer\n- **Variabel**: tempat penyimpanan data dalam program\n- **Array**: struktur data yang menyimpan kumpulan elemen dengan tipe yang sama\n- **Fungsi**: blok kode yang menjalankan tugas tertentu dan dapat dipanggil berulang\n- **Library**: kumpulan fungsi siap pakai dalam pemrograman"
    elif bab_id == "4":
        glos = "- **LAN**: Local Area Network, jaringan komputer dalam area terbatas\n- **Topologi**: susunan fisik atau logis dari jaringan komputer\n- **TCP/IP**: protokol komunikasi data antar komputer di internet\n- **DNS**: Domain Name System, sistem penerjemah nama domain ke IP address\n- **Cyber Security**: praktik melindungi sistem, jaringan, dan data dari serangan digital"
    elif bab_id == "5":
        glos = "- **Teknologi Digital**: teknologi yang menggunakan sistem digital untuk memproses informasi\n- **Media Sosial**: platform digital untuk interaksi sosial dan berbagi konten\n- **E-commerce**: perdagangan elektronik melalui internet\n- **Fintech**: teknologi finansial yang menyediakan layanan keuangan digital\n- **UU ITE**: Undang-Undang Informasi dan Transaksi Elektronik"
    elif bab_id == "6":
        glos = "- **Proyek Lintas Bidang**: proyek yang mengintegrasikan berbagai disiplin ilmu\n- **Prototipe**: model awal dari suatu produk untuk pengujian konsep\n- **Integrasi**: penggabungan beberapa komponen sistem menjadi satu kesatuan\n- **Dokumentasi**: catatan tertulis yang menjelaskan proses dan hasil proyek"
    else:
        glos = "-"

    # Daftar Pustaka
    if bab_id == "1":
        dapus = """- Permana, Budi dkk. (2025). *Informatika untuk SMA/MA Kelas XII*. Jakarta: Kemendikdasristek.
- Kementerian Komunikasi dan Informatika RI. (2021). *Modul Literasi Digital*.
- Artikel jurnal dan sumber daring terkait IoT, Big Data, AI, dan Cloud Computing."""
    elif bab_id in ["2", "3"]:
        dapus = """- Permana, Budi dkk. (2025). *Informatika untuk SMA/MA Kelas XII*. Jakarta: Kemendikdasristek.
- Arduino.cc. (2025). *Arduino Documentation*. https://www.arduino.cc/en/Guide
- Wokwi. (2025). *Wokwi Online Simulator*. https://wokwi.com
- Barrett, S. (2020). *Arduino Microcontroller Processing for Everyone*. Morgan & Claypool."""
    elif bab_id == "4":
        dapus = """- Permana, Budi dkk. (2025). *Informatika untuk SMA/MA Kelas XII*. Jakarta: Kemendikdasristek.
- Kurose, J.F. & Ross, K.W. (2021). *Computer Networking: A Top-Down Approach*. Pearson.
- Stallings, W. (2020). *Network Security Essentials*. Pearson."""
    elif bab_id == "5":
        dapus = """- Permana, Budi dkk. (2025). *Informatika untuk SMA/MA Kelas XII*. Jakarta: Kemendikdasristek.
- Undang-Undang No. 11 Tahun 2008 tentang Informasi dan Transaksi Elektronik (UURI 2008) dan perubahannya.
- Artikel jurnal dan sumber daring terkait dampak sosial informatika."""
    elif bab_id == "6":
        dapus = """- Permana, Budi dkk. (2025). *Informatika untuk SMA/MA Kelas XII*. Jakarta: Kemendikdasristek.
- Referensi lain sesuai topik proyek yang dipilih peserta didik."""
    else:
        dapus = "- Permana, Budi dkk. (2025). *Informatika untuk SMA/MA Kelas XII*. Jakarta: Kemendikdasristek."

    return f"""---
modul: {bab_id}.{pertemuan:02d}
bab: {bab_id}
judul_bab: {bab_data['judul']}
pertemuan: {pertemuan}
total_pertemuan: {total_pertemuan}
sub_judul: {sub_judul}
jp: 5
semester: {semester}
---

# MODUL AJAR {MAPEL} — KELAS {KELAS}
## Pertemuan {pertemuan}: {sub_judul}

| Informasi | Detail |
|-----------|--------|
| **Sekolah** | {SEKOLAH} |
| **Mata Pelajaran** | {MAPEL} |
| **Kelas/Fase** | {KELAS} / {fase} |
| **Bab {bab_id}** | {bab_data['judul']} |
| **Materi** | {sub_judul} |
| **Alokasi Waktu** | {alokasi} |
| **Semester** | {'Ganjil' if semester == 1 else 'Genap'} |
| **Tahun Pelajaran** | {TP} |

---

## A. CAPAIAN PEMBELAJARAN (CP)

### Elemen CP:
{chr(10).join(f"- {cp_elemen}" for cp_elemen in cp_elemen_list)}

### Teks CP:
{chr(10).join(cp_teks_list)}

## B. TUJUAN PEMBELAJARAN (TP)

### TP pada Bab Ini:
{tp_list}

### TP Khusus Pertemuan Ini:
{tp_ini}

## C. INDIKATOR KETERCAPAIAN TUJUAN PEMBELAJARAN
- Peserta didik mampu menjelaskan konsep {sub_judul.lower()} dengan benar
- Peserta didik mampu mengidentifikasi komponen/pilar utama dari {sub_judul.lower()}
- Peserta didik mampu menerapkan konsep {sub_judul.lower()} dalam studi kasus

## D. PRASYARAT PENGETAHUAN
{prasyarat}

## E. PROFIL LULUSAN 8 DIMENSI (DEEP LEARNING)
**Dimensi yang Dikembangkan:** {dimensi_fokus}

| Dimensi | Aktivitas Pembelajaran |
|---------|----------------------|
| Penalaran Kritis | Menganalisis dan mengevaluasi informasi terkait materi |
| Komunikasi | Menyampaikan pendapat dan hasil diskusi |
| Kolaborasi | Kerja sama dalam diskusi/praktik kelompok |
| Kemandirian | Mengerjakan tugas dan eksplorasi mandiri |

## F. SARANA DAN PRASARANA
| Alat/Bahan | Spesifikasi | Keterangan |
|------------|-------------|------------|
| Komputer/Laptop | OS minimal Windows 10 / Linux / macOS | 1 per 2-3 siswa |
| Proyektor/LCD | - | Untuk presentasi guru |
| Koneksi Internet | Stabil | Untuk akses sumber belajar |
| Modul/Bahan Ajar | Buku cetak/digital | - |
| Papan Tulis | Whiteboard | Untuk coretan diskusi |
{'| Arduino Kit | Arduino Uno + komponen | Untuk praktik |' if bab_id in ['2','3'] else ''}
{'| Simulator (opsional) | Wokwi / Tinkercad | Alternatif praktik virtual |' if bab_id in ['2','3'] else ''}
{'| Perangkat Jaringan | Router/Switch, Kabel LAN | Untuk praktik jaringan |' if bab_id == '4' else ''}

## G. MODEL DAN METODE PEMBELAJARAN
| Aspek | Pendekatan |
|-------|-----------|
| Model Pembelajaran | {'Project Based Learning (PjBL)' if is_proyek else 'Problem Based Learning + Discovery Learning' if is_praktik else 'Discovery Learning + Cooperative Learning'} |
| Metode | {'Proyek, presentasi, diskusi, demonstrasi' if is_proyek else 'Praktik, diskusi, demonstrasi, tanya jawab' if is_praktik else 'Diskusi, tanya jawab, penugasan, presentasi'} |
| Pendekatan | Student-Centered Learning (Saintifik) |

## H. KEGIATAN PEMBELAJARAN
{kegiatan}

## I. PENILAIAN PEMBELAJARAN
### 1. Teknik Penilaian
{assessment}

### 2. Rubrik Penilaian Sikap
| Dimensi | Kriteria | Skor |
|---------|----------|------|
| Keimanan & Ketakwaan | Berdoa sebelum/sesudah belajar, bersikap jujur | 1-4 |
| Penalaran Kritis | Aktif bertanya, menganalisis dengan logis | 1-4 |
| Kolaborasi | Bekerja sama, menghargai pendapat teman | 1-4 |
| Komunikasi | Menyampaikan pendapat dengan jelas dan sopan | 1-4 |
| Kemandirian | Mengerjakan tugas tanpa bergantung orang lain | 1-4 |

### 3. Rubrik Penilaian Pengetahuan
| Skor | Kriteria |
|------|----------|
| 4 | Jawaban lengkap, tepat, dan disertai contoh/analisis |
| 3 | Jawaban benar tetapi kurang detail |
| 2 | Jawaban kurang tepat |
| 1 | Jawaban tidak tepat/tidak menjawab |

### 4. Rubrik Penilaian Keterampilan (jika ada)
| Aspek | Skor 4 (Sangat Baik) | Skor 3 (Baik) | Skor 2 (Cukup) | Skor 1 (Kurang) |
|-------|---------------------|---------------|----------------|-----------------|
| Persiapan | Alat lengkap, siap praktik | Alat lengkap | Alat kurang lengkap | Tidak siap |
| Proses | Langkah tepat, sistematis | Langkah tepat | Langkah kurang tepat | Tidak mengikuti prosedur |
| Hasil | Berhasil, rapi, sesuai tujuan | Berhasil, cukup rapi | Kurang berhasil | Tidak berhasil |
| Laporan | Lengkap, sistematis, analitis | Lengkap, sistematis | Kurang lengkap | Tidak membuat laporan |

## J. REMEDIAL DAN PENGAYAAN
### Remedial
- Pembelajaran ulang/ bimbingan perorangan bagi peserta didik yang belum mencapai KKTP (nilai < 78)
- Tugas tambahan terstruktur

### Pengayaan
- Eksplorasi mandiri topik lanjutan
- Proyek pengembangan tambahan bagi peserta didik yang telah mencapai nilai > 89

## K. GLOSARIUM
{glos}

## L. DAFTAR PUSTAKA
{dapus}

---

**Disusun oleh:**
{GURU}
NIP. {NIP}

**Mengetahui,**
Kepala {SEKOLAH}
"""


def generate_all():
    """Generate all documents."""
    # Create modul_ajar dir
    os.makedirs(MODUL_DIR, exist_ok=True)

    # 1. Root documents
    docs = {
        "00_COVER.md": cover(),
        "01_ANALISIS_ALOKASI_WAKTU.md": analisis_alokasi_waktu(),
        "01b_RPE_Rincian_Pekan_Efektif.md": "_(Lihat Analisis Alokasi Waktu — sudah mencakup RPE)_",
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

    print("=" * 60)
    print(f"GENERATOR ADMINISTRASI GURU KELAS {KELAS}")
    print(f"{SEKOLAH} — {TP}")
    print(f"{MAPEL} — Fase F — 5 JP/minggu — 200 JP/tahun")
    print("=" * 60)

    print("\n[1/3] Membuat 16 dokumen root...")
    count = 0
    for fname, content in docs.items():
        fp = os.path.join(BASE, fname)
        with open(fp, "w", encoding="utf-8") as f:
            f.write(content)
        count += 1
        print(f"  ✓ {fname}")
    print(f"  → {count} file root dibuat.")

    # 2. Modul Ajar (40 files)
    print("\n[2/3] Membuat 40 modul ajar...")
    ma_count = 0
    pert_global = 0
    for k in sorted(BAB.keys()):
        b = BAB[k]
        total_tm = b["tm"]
        for i, sub in enumerate(b["sub"]):
            pert_global += 1
            pert_local = i + 1
            content = generate_modul_ajar(k, b, pert_local, total_tm, sub, b["smt"])
            fname = f"{k}.{pert_local:02d}_{sub.replace(' ','_').replace(':','-')}.md"
            # Shorten filename
            short = sub.replace(' ', '_').replace(':','-').replace('/','-')
            short = short[:50]  # keep reasonable length
            fname = f"{k}.{pert_local:02d}_{short}.md"
            fp = os.path.join(MODUL_DIR, fname)
            with open(fp, "w", encoding="utf-8") as f:
                f.write(content)
            ma_count += 1
            if ma_count % 5 == 0:
                print(f"  ... {ma_count} modul ajar generated")
        print(f"  ✓ Bab {k}: {b['judul']} — {total_tm} modul ajar")

    print(f"  → {ma_count} modul ajar dibuat.")

    # 3. Summary
    print("\n[3/3] Ringkasan:")
    total_root = count
    total_ma = ma_count
    total_all = total_root + total_ma
    print(f"  Root documents: {total_root}")
    print(f"  Modul Ajar:     {total_ma}")
    print(f"  Total:          {total_all} files")

    # Count lines
    print("\n--- Statistik Baris ---")
    total_lines = 0
    for root, dirs, files in os.walk(BASE):
        if 'generate_xii.py' in root:
            continue
        for f in files:
            if f.endswith('.md'):
                fp = os.path.join(root, f)
                with open(fp, 'r') as fh:
                    lines = len(fh.readlines())
                total_lines += lines
    print(f"  Total baris: {total_lines}")
    print("=" * 60)
    print("SELESAI. Semua dokumen Grade XII siap digunakan.")
    print("=" * 60)


if __name__ == "__main__":
    generate_all()
