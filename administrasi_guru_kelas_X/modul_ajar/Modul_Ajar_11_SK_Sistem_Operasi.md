# MODUL AJAR INFORMATIKA KELAS X

## SK: SISTEM OPERASI

---

### A. INFORMASI UMUM

| Komponen | Deskripsi |
|---|---|
| Satuan Pendidikan | SMA Negeri 6 Cimahi |
| Mata Pelajaran | Informatika |
| Kelas / Fase | X (Sepuluh) / Fase E |
| Elemen | SK — Sistem Komputer |
| Tujuan Pembelajaran | TP.3.2: Menjelaskan peran sistem operasi (OS) dalam interaksi antara hardware, software, dan user |
| Alokasi Waktu | 2 JP (2 × 45 menit) |
| Pertemuan ke- | 11 (Kesebelas) |
| Kompetensi Awal | Peserta didik sudah mengenal sistem operasi (Windows, Android, iOS) dalam penggunaan sehari-hari tetapi belum memahami peran OS secara konseptual. Peserta didik telah mempelajari perangkat keras (Modul 10) sehingga siap memahami bagaimana OS menjadi jembatan antara hardware dan software. |
| Integrasi 8 Dimensi | Penalaran Kritis, Kemandirian, Keimanan & Ketakwaan, Kewargaan, Komunikasi, Kolaborasi, Kreativitas, Kesehatan |
| **Integrasi 7 KAIH** | Beribadah, Berolahraga |
| **Pendekatan Deep Learning** | Mindful → Mining → Joyful |
| Sarana & Proyektor, laptop guru (dual-boot Windows + Linux jika memungkinkan), komputer siswa (Windows dan/atau Linux), Task Manager, Device Manager, File Explorer, Terminal/Command Prompt, papan tulis, spidol, kertas plano, slide presentasi, koneksi internet |
| Target Peserta Didik | Reguler (dengan diferensiasi) |
| Model Pembelajaran | Diskusi + Studi Kasus |
| Metode | Diskusi interaktif, eksplorasi langsung, studi kasus kelompok, presentasi, kuis |
| Sumber Belajar | Buku Informatika Kelas X Bab 4, artikel perbandingan OS (Windows vs Linux vs macOS), dokumentasi Ubuntu, video "How Operating System Works", studi kasus migrasi OS di sekolah |

### B. TUJUAN PEMBELAJARAN
### B.1 PEMAHAMAN BERMAKNA (MEANINGFUL)
Memahami bagaimana komputer bekerja dari dalam membantu kita merawat perangkat, memilih spesifikasi yang tepat, dan memecahkan masalah teknis sehari-hari.


### B.2 PERTANYAAN PEMANTIK (MINDFUL)
1. Apa yang akan terjadi jika...?
2. Bagaimana konsep ini terhubung dengan kehidupan sehari-harimu?
3. Mengapa materi ini penting untuk dipelajari?

#### B.1 Tujuan
1. Menjelaskan peran sistem operasi sebagai penghubung antara hardware, software, dan pengguna.
2. Mengidentifikasi komponen-komponen utama sistem operasi (kernel, shell/interface, file system, device driver).
3. Membedakan karakteristik sistem operasi Windows, Linux, dan macOS.
4. Mengeksplorasi fungsi OS melalui alat bawaan (Task Manager, File Explorer, Terminal, Device Manager).
5. Menganalisis faktor-faktor yang perlu dipertimbangkan dalam memilih OS untuk kebutuhan tertentu.

#### B.2 Indikator Keberhasilan
- [ ] Peserta didik menjelaskan 4 peran utama sistem operasi dengan analogi yang tepat.
- [ ] Peserta didik menyebutkan 4 komponen OS dan fungsinya masing-masing.
- [ ] Peserta didik membuka Task Manager dan mengidentifikasi proses yang berjalan.
- [ ] Peserta didik menyajikan analisis perbandingan OS dalam studi kasus.

#### B.3 Kata Kunci
Sistem operasi, kernel, shell, GUI, CLI, file system, device driver, manajemen memori, manajemen proses, manajemen file, manajemen perangkat, Windows, Linux, macOS, Android, iOS, booting, multitasking

### C. KEGIATAN PEMBELAJARAN

| **Fase DL** | **Tahap** | **Waktu** | **Aktivitas Guru** | **Aktivitas Siswa** | **Media/Sumber** |
|---|---|---|---|---|---|
| **MINDFULL** | **Pemanasan** | 10 menit | Guru membuka dengan salam dan doa. Apersepsi: "Coba sebutkan OS yang kalian tahu!" — siswa menjawab (Windows, Android, iOS, macOS, Linux). "Apa bedanya? Kenapa ada banyak OS?" Guru menampilkan 4 logo OS dan meminta siswa menebak kelebihan masing-masing. Guru menyampaikan tujuan: memahami peran OS dalam sistem komputer. | Siswa menjawab salam, berdoa. Menyebutkan OS yang dikenal. Menebak kelebihan masing-masing OS. Termotivasi. | Slide logo OS, papan tulis |
| **MINING FULL** | **Eksplorasi** — Konsep Sistem Operasi** | 15 menit | Guru menjelaskan peran OS dengan analogi "Manajer Perusahaan": OS adalah manajer yang mengatur sumber daya (CPU, memori, storage) dan melayani "karyawan" (aplikasi). Guru menjelaskan 4 tugas utama OS: (1) Manajemen Proses — mengatur aplikasi yang berjalan, (2) Manajemen Memori — mengalokasikan RAM, (3) Manajemen File — mengatur penyimpanan, (4) Manajemen Perangkat — menghubungkan driver. Guru juga menjelaskan komponen OS: (1) Kernel — inti OS yang berinteraksi langsung dengan hardware, (2) Shell/Interface — GUI (Windows) dan CLI (Terminal), (3) File System — NTFS, FAT32, ext4, (4) Device Driver — jembatan OS ke hardware. | Siswa menyimak dan mencatat. Mengajukan pertanyaan. Menulis analogi "manajer perusahaan" di catatan. | Slide presentasi, papan tulis |
| **MINING FULL** | **Eksplorasi** — Praktik Eksplorasi OS** | 20 menit | Guru memandu eksplorasi OS di komputer: (1) Task Manager — Ctrl+Shift+Esc → lihat proses, CPU usage, RAM usage, disk usage. "Aplikasi mana yang paling boros memori?", (2) File Explorer — beda file system (This PC, C:, D:), lihat properties drive, (3) Device Manager — lihat semua device driver, cari yang ada tanda seru kuning, (4) Command Prompt/Terminal — perintah dasar: ipconfig, dir/ls, ping. Bagi yang pakai Windows dan Linux: bandingkan perbedaan tampilan dan perintah. | Siswa membuka Task Manager. Mengamati proses, CPU, RAM. Membuka File Explorer. Mencoba perintah di CMD/Terminal. Mencatat pengamatan. | Task Manager, File Explorer, Device Manager, CMD/Terminal |
| **MINING FULL** | **Eksplorasi** — Studi Kasus Kelompok** | 20 menit | Guru membagi kelas menjadi 5-6 kelompok. Studi kasus: "Sekolah ingin ganti OS lab komputer — pilihannya tetap Windows, pindah ke Linux, atau Chromebook?" Setiap kelompok mendapat 1 sudut pandang: (A) Tim Windows — argumentasi pro Windows (kompatibilitas, familiar, banyak software), (B) Tim Linux — argumentasi pro Linux (gratis, open source, ringan, keamanan), (C) Tim Chromebook — argumentasi pro Chromebook (murah, mudah, cloud-based), (D) Tim Netral — analisis biaya-manfaat dari sisi sekolah (biaya lisensi, pelatihan guru, maintenance), (E) Tim Rekomendasi Hybrid — kombinasi OS yang paling optimal (misal: Windows untuk admin + Linux untuk lab coding). | Siswa berdiskusi dalam kelompok. Mencari argumentasi pro sudut pandang mereka. Mencatat di kertas plano. Bersiap debat/diskusi. | Kertas plano, spidol, akses internet |
| **MINING FULL** | **Eksplorasi** — Presentasi & Diskusi** | 10 menit | Guru memoderasi presentasi singkat dari setiap sudut pandang (masing-masing 2 menit). Guru memberikan penguatan: "Tidak ada OS yang sempurna — setiap OS punya kelebihan dan kekurangan. Pemilihan tergantung kebutuhan, anggaran, dan kesiapan sumber daya manusia." Guru menambahkan fakta: banyak server dan superkomputer pakai Linux, banyak perusahaan dan gaming pakai Windows. | Masing-masing kelompok presentasi. Kelompok lain menanggapi. Menyimak penguatan guru. | Kertas plano hasil diskusi |
| **JOYFULL** | **Penutup Kreatif** | 15 menit | Guru memimpin refleksi: "Apa yang paling menarik dari sistem operasi?" Guru memberikan tugas: cari 3 perbedaan utama Windows vs Linux (dari segi lisensi, interface, keamanan, dan software). Guru menambahkan penguatan spiritual: "Sistem operasi mengatur sumber daya dengan tertib — begitulah kita sebagai manusia harus mengatur hidup dengan tertib dan bertanggung jawab." Doa dan salam. | Siswa menjawab refleksi. Mencatat tugas. Berdoa dan menjawab salam. | Buku catatan |

### D. ASESMEN

#### D.1 Asesmen Diagnostik
| No | Pertanyaan | Tujuan |
|---|---|---|
| 1 | OS apa yang terpasang di HP dan laptopmu? | Mengidentifikasi pengalaman OS |
| 2 | Apa yang terjadi saat komputer pertama kali dinyalakan? | Mengukur pemahaman booting |
| 3 | Kenapa aplikasi kadang lemot saat banyak tab terbuka? | Mengukur pemahaman manajemen memori |
| 4 | Apa beda Windows dan Linux menurut yang kamu tahu? | Mengukur pengetahuan perbandingan OS |

#### D.2 Asesmen Formatif
| Aspek | Indikator | Teknik | Instrumen |
|---|---|---|---|
| Konsep OS | Menjelaskan peran dan komponen OS | Tanya jawab | Pertanyaan lisan |
| Eksplorasi Praktik | Membuka Task Manager, identifikasi proses | Cek praktik | Lembar observasi |
| Studi Kasus | Argumentasi logis, data pendukung | Presentasi | Rubrik studi kasus |
| Partisipasi | Aktif diskusi dan eksplorasi | Observasi | Lembar partisipasi |

#### D.3 Asesmen Sumatif
**Bentuk:** Laporan Perbandingan OS
**Tugas:** Buat laporan perbandingan antara Windows dan Linux dalam bentuk tabel dengan aspek:
1. Lisensi dan biaya
2. Antarmuka (GUI)
3. Keamanan
4. Ketersediaan software
5. Kemudahan penggunaan
6. Kinerja pada hardware lama
7. Komunitas dan dukungan
8. Rekomendasi penggunaan

#### D.4 Rubrik Penilaian
| Kriteria | SB (4) | B (3) | C (2) | PB (1) |
|---|---|---|---|---|---|
| Peran OS | 4 peran + analogi tepat | 3 peran + analogi | 2 peran | <2 |
| Komponen OS | 4 komponen + fungsi detail | 4 komponen + fungsi | 3 komponen | <3 |
| Eksplorasi Praktik | Task Manager + Explorer + Device + CMD | 3 dari 4 | 2 dari 4 | <2 |
| Laporan Perbandingan | 8 aspek, data akurat | 6-7 aspek | 4-5 aspek | <4 |

#### D.5 Contoh Soal/Tugas
**Soal:** Andi memiliki laptop lama (2015) dengan RAM 4GB dan prosesor Intel Core i3. Laptop tersebut lemot saat menjalankan Windows 10. OS apa yang akan kamu rekomendasikan? Berikan 3 alasan!

**Jawaban Referensi:**
Rekomendasi: Linux (misal Ubuntu atau Linux Mint)
1. **Lebih ringan** — Linux membutuhkan RAM lebih sedikit (Ubuntu ~2GB, Windows 10 ~3-4GB).
2. **Gratis** — tidak perlu lisensi berbayar.
3. **Keamanan** — Linux lebih jarang terkena virus/malware.
4. Alternatif: Windows 10 LTSC (versi ringan) atau upgrade RAM ke 8GB.

### E. LEMBAR KERJA PESERTA DIDIK (LKPD)

**LKPD 11.1 — SISTEM OPERASIKU**

**Nama:** __________ **Kelas:** __________ **Tanggal:** __________

**Bagian A — Tantangan Mudah: Peran OS**
Jodohkan: Manajemen Proses (c), Manajemen Memori (b), Manajemen File (a), Manajemen Perangkat (d).

Jelaskan dengan analogi "Manajer Perusahaan" untuk keempat peran di atas!

**Bagian B — Tantangan Sedang: Eksplorasi OS**
Buka Task Manager (Ctrl+Shift+Esc). Catat: nama OS, CPU, RAM total/terpakai, jumlah proses, aplikasi tertinggi CPU & RAM, disk usage.

**Praktik Terminal/CMD:** Jalankan `ipconfig`, `ping google.com`, `dir`/`ls`, `systeminfo`/`neofetch`.

**Bagian C — Tantangan Sulit: Analisis Migrasi OS**
**Kasus:** SMA Negeri 6 Cimahi memiliki 30 komputer di laboratorium. Spesifikasi: Intel i3, RAM 4GB, HDD 500GB. Saat ini menggunakan Windows 10. Sekolah ingin menghemat biaya lisensi.

**Diskusikan dalam kelompok dan jawab:**

| Aspek | Windows | Linux | Chromebook |
|---|---|---|---|---|---|
| Biaya lisensi | | | |
| Kemudahan | | | |
| Software | | | |
| Maintenance | | | |
| Keamanan | | | |
| Kinerja HW lama | | | |

**Kesimpulan:** OS terbaik: _______. Alasan: 1) ___, 2) ___, 3) ___.

**Refleksi:** Apa yang terjadi jika komputer tidak memiliki OS?

### F. DIFERENSIASI PEMBELAJARAN

| Kesiapan Siswa | Tindakan |
|---|---|
| **Belum Siap** | Fokus eksplorasi Windows, panduan screenshot, tidak perlu Linux/CMD |
| **Siap** | Mengerjakan LKPD, mencoba CMD, partisipasi studi kasus |
| **Mahir** | Instal Linux di VirtualBox, perbandingan langsung, jelaskan kernel & system call |

### G. REFLEKSI GURU

| Aspek | Catatan |
|---|---|
| Analogi efektif? | |
| Antusiasme Task Manager? | |
| Studi kasus migrasi? | |
| Kesulitan utama? | |
| Strategi efektif? | |
| Rencana perbaikan? | |

### H. BAHAN BACAAN UNTUK GURU

1. **Tips:** Analogi "Manajer" — Kernel = CEO, Shell = resepsionis, File System = arsip, Driver = teknis.

2. **Error:** Windows = Office, BIOS = OS, Linux sulit, Android/iOS bukan OS.

3. **Mengenalkan Linux:** Live USB, bellard.org/jslinux, WSL, video Ubuntu.

4. **File System:** Windows (NTFS, FAT32), Linux (ext4, Btrfs), macOS (APFS).

5. **Fakta:** 96% server pakai Linux. Android kernel Linux. Superkomputer TOP500 pakai Linux.

---
Mengetahui,
Kepala Sekolah

_________________________

Guru Mata Pelajaran,

Daniarsyah, S.Kom.
NIP. 198004052022211004

---
