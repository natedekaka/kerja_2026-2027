# MODUL AJAR INFORMATIKA KELAS X

## SK: MEKANISME INTERNAL SISTEM KOMPUTER (TP.3.3)

---

### A. INFORMASI UMUM

| Komponen | Deskripsi |
|---|---|
| Satuan Pendidikan | SMA Negeri 6 Cimahi |
| Mata Pelajaran | Informatika |
| Kelas / Fase | X (Sepuluh) / Fase E |
| Elemen | SK — Sistem Komputer |
| Tujuan Pembelajaran | TP.3.3: Menganalisis mekanisme internal sistem komputer |
| Alokasi Waktu | 2 JP (2 × 45 menit) |
| Pertemuan ke- | 12 |
| Kompetensi Awal | Peserta didik telah memahami komponen hardware komputer (CPU, RAM, motherboard, storage) pada pertemuan sebelumnya serta mampu mengidentifikasi fungsi masing-masing komponen. |
| Integrasi 8 Dimensi | Beriman & Bertakwa (mensyukuri ciptaan Tuhan berupa keteraturan sistem), Penalaran Kritis (menganalisis alur logis booting dan eksekusi), Kreativitas (membuat komik strip), Kemandirian (eksplorasi mandiri diagram alur) |
| **Integrasi 7 KAIH** | Beribadah, Berolahraga |
| **Pendekatan Deep Learning** | Mindful → Mining → Joyful |
| Sarana & Prasarana | Komputer/laptop, proyektor, video animasi booting & cara kerja CPU, kertas plano & spidol untuk diagram alur, aplikasi menggambar digital (Canva/Paint) |
| Target Peserta Didik | Reguler (dengan diferensiasi 3 tingkat kesiapan) |
| Model Pembelajaran | Simulasi + Diskusi Interaktif |
| Metode | Role-play simulasi komponen, tayangan video animasi, diskusi kelompok, penugasan proyek mini kreatif |
| Sumber Belajar | Buku Informatika Kemendikbud Bab 4, video YouTube "How a Computer Boots Up", "How CPU Works" (Crash Course Computer Science), artikel BIOS dan UEFI |

### B. TUJUAN PEMBELAJARAN
### B.1 PEMAHAMAN BERMAKNA (MEANINGFUL)
Memahami bagaimana komputer bekerja dari dalam membantu kita merawat perangkat, memilih spesifikasi yang tepat, dan memecahkan masalah teknis sehari-hari.


### B.2 PERTANYAAN PEMANTIK (MINDFUL)
1. Apa yang akan terjadi jika...?
2. Bagaimana konsep ini terhubung dengan kehidupan sehari-harimu?
3. Mengapa materi ini penting untuk dipelajari?

#### B.1 Tujuan Pembelajaran

1. Menganalisis alur booting sistem komputer dari tombol power ditekan hingga sistem operasi siap digunakan.
2. Menjelaskan peran BIOS/UEFI, POST, bootloader, dan sistem operasi dalam proses booting.
3. Memeragakan mekanisme eksekusi program dari input pengguna hingga output ditampilkan melalui simulasi role-play.
4. Menghubungkan fungsi setiap komponen (PSU, motherboard, CPU, RAM, storage) dalam alur kerja sistem komputer.
5. Mendokumentasikan pemahaman mekanisme internal dalam bentuk diagram alur dan komik strip kreatif.

#### B.2 Indikator Keberhasilan

| Indikator | Kriteria |
|---|---|
| Mampu menggambar diagram alur booting minimal 7 langkah dengan urutan yang benar | Minimal urutan 5 dari 7 langkah benar |
| Mampu menjelaskan peran BIOS/UEFI dalam proses booting dengan bahasa sendiri | Penjelasan mencakup fungsi POST dan bootloader |
| Mampu memeragakan alur eksekusi program dari input ke output | 4 tahap (input → CPU → RAM → output) tergambarkan |
| Mampu membuat komik strip "Perjalanan Data" minimal 6 panel | Alur data dari keyboard ke monitor logis dan berurutan |

#### B.3 Kata Kunci

Booting, BIOS, UEFI, POST, bootloader, Power Supply Unit (PSU), CPU, RAM, sistem operasi, alur eksekusi program, interrupt, clock cycle, kernel

### C. KEGIATAN PEMBELAJARAN

| **Fase DL** | **Tahap** | **Waktu** | **Aktivitas Guru** | **Aktivitas Siswa** | **Media/Sumber** |
|---|---|---|---|---|---|
| **MINDFULL** | **Pemanasan** | 10 menit | 1) Membuka dengan salam dan doa. 2) Mengecek kehadiran. 3) Orientasi: "Apa yang terjadi dari detik kita tekan tombol power sampai desktop muncul?" — memancing tebakan siswa. 4) Apersepsi: mengingatkan komponen hardware yang sudah dipelajari. 5) Menyampaikan TP dan indikator. 6) Asesmen diagnostik: memberikan 3 pertanyaan lisan tentang booting | 1) Menjawab salam dan berdoa. 2) Menyimak dan memberikan tebakan tentang proses booting. 3) Mengingat kembali komponen hardware. 4) Mencatat TP. 5) Menjawab pertanyaan diagnostik | Papan tulis, proyektor, slide pertanyaan |
| **MINING FULL** | **Eksplorasi** — Eksplorasi Konsep** | 20 menit | 1) Menjelaskan alur booting: Power ON → PSU → Motherboard → BIOS/UEFI → POST → Bootloader → Load OS ke RAM → OS ambil alih. 2) Menayangkan video animasi proses booting. 3) Menjelaskan perbedaan BIOS dan UEFI. 4) Menjelaskan mekanisme eksekusi program: user klik → OS kirim ke CPU → CPU ambil dari RAM → proses → kirim output | 1) Menyimak penjelasan dan mencatat alur booting. 2) Mengamati video animasi. 3) Bertanya jika ada yang kurang jelas. 4) Membuat catatan alur eksekusi program | Proyektor, video animasi booting, slide materi |
| **MINING FULL** | **Eksplorasi** — Simulasi Role-Play** | 20 menit | 1) Membagi 5 siswa menjadi komponen: Power Supply, BIOS, RAM, HDD, CPU. 2) Memberi properti kertas nama. 3) Memandu simulasi: guru menjadi "user" yang menekan tombol power → setiap komponen bergerak sesuai perannya secara berurutan. 4) Mengulang simulasi 2-3 kali dengan variasi (misal: error POST). 5) Meminta siswa lain mengamati dan mencatat urutan | 1) 5 siswa maju sebagai komponen. 2) Mengenakan properti. 3) Bergerak sesuai peran saat tombol power ditekan. 4) Siswa lain mengamati dan mencatat urutan simulasi | Properti kertas nama komponen, kartu petunjuk peran |
| **MINING FULL** | **Eksplorasi** — Praktik Mandiri** | 20 menit | 1) Membimbing siswa menggambar diagram alur booting dari ingatan di kertas plano. 2) Berkeliling memberikan bantuan pada kelompok yang kesulitan. 3) Memberikan tantangan tambahan: tambahkan langkah jika terjadi error (misal: RAM rusak) | 1) Menggambar diagram alur booting di kertas plano. 2) Menambahkan keterangan fungsi setiap langkah. 3) Mempresentasikan diagram di hadapan kelompok lain | Kertas plano, spidol warna, penggaris |
| **JOYFULL** | **Penutup Kreatif** | 15 menit | 1) Meminta 2-3 siswa mempresentasikan diagram alurnya. 2) Memberikan penguatan dan klarifikasi miskonsepsi. 3) Refleksi: "Apa bagian paling menarik dari proses booting?" 4) Menjelaskan tugas: buat komik strip 6 panel "Perjalanan Data dari Keyboard ke Monitor". 5) Doa penutup | 1) Mempresentasikan diagram alur. 2) Mendapatkan klarifikasi. 3) Mengisi refleksi. 4) Mencatat tugas komik strip. 5) Berdoa | Lembar refleksi, buku tugas |

### D. ASESMEN

#### D.1 Asesmen Diagnostik

Tiga pertanyaan lisan di awal pembelajaran:
1. Menurut kalian, apa yang pertama kali terjadi saat komputer dinyalakan?
2. Apa perbedaan antara data yang ada di hard disk dengan data di RAM?
3. Kenapa komputer tidak bisa langsung menyala seperti televisi?

#### D.2 Asesmen Formatif

Observasi selama simulasi role-play dan diskusi kelompok. Guru mencatat partisipasi dan pemahaman siswa menggunakan jurnal harian.

#### D.3 Asesmen Sumatif

1. Diagram alur booting (produk individu/kelompok)
2. Komik strip 6 panel "Perjalanan Data dari Keyboard ke Monitor" (tugas rumah)

#### D.4 Rubrik Penilaian

| Aspek | SB = 4 (Sangat Baik) | B = 3 (Baik) | C = 2 (Cukup) | PB = 1 (Perlu Bimbingan) |
|---|---|---|---|---|---|
| Diagram Alur Booting | 7 langkah lengkap, urutan benar, ada keterangan fungsi tiap langkah | 5-6 langkah, urutan benar, keterangan minimal | 3-4 langkah, urutan sebagian salah, tanpa keterangan | < 3 langkah atau urutan salah total |
| Simulasi Role-Play | Aktif berperan, menjelaskan peran komponen dengan benar, membantu teman | Berperan dengan benar, mampu menjawab 2 pertanyaan | Berperan namun ragu menjawab pertanyaan | Pasif atau tidak berpartisipasi |
| Komik Strip | 6 panel, alur logis, kreatif, ada teks penjelas, rapi | 4-5 panel, alur logis, ada teks | 3 panel, alur kurang logis | < 3 panel atau tidak dikumpulkan |

#### D.5 Contoh Soal/Tugas

Essay: "Jelaskan apa yang terjadi ketika BIOS menemukan bahwa RAM tidak terdeteksi saat POST. Bagaimana komputer merespons dan apa yang harus dilakukan pengguna?"
Pilihan Ganda: "Apa fungsi utama dari bootloader?" A) Menyalakan komputer B) Memuat sistem operasi ke RAM C) Membersihkan hard disk D) Mengecek suhu CPU

### E. LEMBAR KERJA PESERTA DIDIK (LKPD)

**LKPD 12.1 — Diagram Alur Booting**

Nama: _____________ Kelas: _____________ Tanggal: _____________

**Petunjuk:** Gambarlah diagram alur (flowchart) proses booting komputer dari tombol power ditekan hingga sistem operasi siap digunakan. Gunakan simbol flowchart standar (oval = mulai/selesai, persegi = proses, belah ketupat = keputusan).

**Tantangan Bertingkat:**
- Level Dasar (C): Gambar alur booting normal (7 langkah)
- Level Menengah (B): Gambar alur normal + tambahkan simbol keputusan untuk POST (passed/failed)
- Level Mahir (A): Gambar alur normal + POST + tambahkan alur alternatif jika booting gagal (troubleshooting)

**Tabel Pengamatan Simulasi:**

| No | Komponen | Peran dalam Booting | Urutan ke- |
|---|---|---|---|
| 1 | Power Supply | _________________ | ____ |
| 2 | BIOS/UEFI | _________________ | ____ |
| 3 | RAM | _________________ | ____ |
| 4 | HDD/SSD | _________________ | ____ |
| 5 | CPU | _________________ | ____ |

**Pertanyaan Refleksi:**
1. Apa yang terjadi jika salah satu komponen di atas rusak?
2. Kenapa booting kadang lama? Faktor apa yang memengaruhinya?

### F. DIFERENSIASI PEMBELAJARAN

1. **Level Dasar (C):** Siswa mendapat diagram alur yang sudah diacak — tugasnya mengurutkan dengan benar. Diberikan juga daftar kosakata (word bank) sebagai bantuan.
2. **Level Menengah (B):** Siswa menggambar diagram alur dari ingatan tanpa bantuan. Mendapat lembar kerja standar.
3. **Level Mahir (A):** Siswa menggambar diagram alur dan menambahkan skenario error handling (misal: boot loop, blue screen, RAM error). Juga diminta membandingkan BIOS vs UEFI dalam bentuk tabel.

### G. REFLEKSI GURU

1. Apakah simulasi role-play efektif membantu siswa memahami alur booting? Bagian mana yang perlu diperbaiki?
2. Apakah durasi waktu untuk setiap tahap sudah proporsional?
3. Siswa mana yang masih kesulitan memahami konsep? Intervensi apa yang diperlukan?
4. Apakah video animasi yang ditayangkan sudah sesuai dengan tingkat pemahaman siswa?
5. Bagaimana kualitas komik strip yang dihasilkan siswa? Apakah petunjuk tugas perlu diperjelas?

### H. BAHAN BACAAN UNTUK GURU

1. **BIOS vs UEFI:** BIOS (Basic Input Output System) adalah firmware tradisional yang telah digunakan sejak 1980-an. UEFI (Unified Extensible Firmware Interface) adalah pengganti modern dengan antarmuka grafis, dukungan mouse, booting lebih cepat, dan keamanan Secure Boot. UEFI mendukung disk GPT sementara BIOS terbatas pada MBR.
2. **Proses POST (Power-On Self-Test):** Serangkaian tes diagnostik yang dilakukan BIOS saat startup. BIOS memeriksa CPU, RAM, storage, dan perangkat lain. Jika ditemukan error, BIOS menghasilkan kode beep tertentu. Misalnya: 1 beep pendek = normal, 3 beep panjang = error RAM, beep terus-menerus = error PSU.
3. **Interrupt dan Clock Cycle:** CPU bekerja berdasarkan clock cycle (jutaan siklus per detik — GHz). Setiap instruksi membutuhkan beberapa clock cycle. Interrupt adalah sinyal yang memberitahu CPU untuk menghentikan sementara pekerjaan saat ini dan menangani kejadian tertentu (misal: tombol keyboard ditekan).
4. **Caching dan Pipeline:** CPU modern memiliki cache L1, L2, L3 untuk mempercepat akses data. Pipeline memungkinkan CPU memproses beberapa instruksi sekaligus dalam tahapan berbeda (fetch-decode-execute).

---

Mengetahui,
Kepala Sekolah

_________________________

Guru Mata Pelajaran,

Daniarsyah, S.Kom.
NIP. 198004052022211004

_________________________
