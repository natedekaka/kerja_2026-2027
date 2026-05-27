# MODUL AJAR INFORMATIKA KELAS X

## PLB: Implementasi & Pengujian Proyek — Pengerjaan, Iterasi, dan Pelaporan Artefak Komputasional

---

### A. INFORMASI UMUM

| Komponen | Deskripsi |
|---|---|
| Satuan Pendidikan | SMA Negeri 6 Cimahi |
| Mata Pelajaran | Informatika |
| Kelas / Fase | X (Sepuluh) / Fase E |
| Elemen | PLB — Praktika Lintas Bidang |
| Tujuan Pembelajaran | TP.9.2: Mengimplementasikan & menguji artefak komputasional |
| Alokasi Waktu | 2 JP (2 × 45 menit) + pengerjaan mandiri (opsional) |
| Pertemuan ke- | 31 (dari 36 pertemuan) |
| Kompetensi Awal | Peserta didik telah menyusun proposal proyek pada pertemuan sebelumnya (TP.9.1). Masing-masing kelompok telah memiliki rencana kerja, pembagian peran, dan daftar alat/bahan yang dibutuhkan. Peserta didik menguasai dasar pemrograman visual/blok dan penggunaan tools pengembang. |
| Integrasi 8 Dimensi Profil Lulusan | **Beriman & Bertakwa** (kejujuran dalam melaporkan bug/kegagalan), **Kemandirian** (inisiatif menyelesaikan tugas), **Kolaborasi** (kerja tim dalam implementasi), **Kreativitas** (solusi teknis saat遇到 kendala), **Penalaran Kritis** (debugging dan analisis error), **Komunikasi** (laporan kemajuan lisan), **Kewargaan** (produk bermanfaat untuk umum), **Gotong Royong** (saling membantu antarkelompok) |
| Sarana & Prasarana | Komputer/laptop (1 per siswa atau berpasangan), proyektor, koneksi internet, akun GitHub/Google Drive, aplikasi pengembangan (Visual Studio Code, Scratch, Thunkable, Canva, atau tools sesuai proyek masing-masing), lembar issue log, sticky notes untuk catatan bug |
| Target Peserta Didik | Reguler (dengan diferensiasi untuk akselerasi dan pendampingan) |
| Model Pembelajaran | Project Based Learning (PjBL) — Sintaks: mengelola dan memonitor kemajuan, menguji hasil, mengevaluasi pengalaman |
| Metode | Kerja mandiri terbimbing, peer review, debugging bersama, presentasi kemajuan (daily stand-up), issue tracking |
| Sumber Belajar | Buku Informatika Kelas X Bab 9, dokumentasi tools yang digunakan (W3Schools, Scratch Wiki, Thunkable Docs), video tutorial implementasi proyek, contoh kode program dari repositori publik, lembar kerja issue log |

### B. TUJUAN PEMBELAJARAN

#### B.1 Tujuan Pembelajaran
1. Mengimplementasikan artefak komputasional sesuai dengan rencana proposal yang telah disusun pada pertemuan sebelumnya.
2. Melakukan pengujian internal (internal testing) terhadap artefak yang dikembangkan dan mencatat temuan pada issue log.
3. Melakukan perbaikan (iterasi) berdasarkan hasil pengujian untuk meningkatkan kualitas artefak.
4. Mendokumentasikan proses pengembangan, kendala, dan solusi dalam laporan kemajuan proyek.
5. Menyusun laporan proyek akhir yang mencakup hasil implementasi, pengujian, dan rencana pengembangan selanjutnya.

#### B.2 Indikator Keberhasilan
1. Menyelesaikan minimal 80% fitur yang direncanakan dalam proposal (artefak komputasional berfungsi).
2. Mengisi issue log dengan minimal 3 temuan (bug/ kekurangan) selama pengujian internal.
3. Memperbaiki minimal 2 dari 3 temuan bug/kekurangan yang tercatat.
4. Menyusun laporan kemajuan proyek yang mencakup dokumentasi proses, tangkapan layar, dan kendala yang dihadapi.

#### B.3 Kata Kunci
Implementasi, pengujian, debugging, issue log, iterasi, artefak komputasional, laporan proyek, presentasi, dokumentasi teknis

### C. KEGIATAN PEMBELAJARAN

| Tahap | Waktu | Aktivitas Guru | Aktivitas Siswa | Media/Sumber |
|---|---|---|---|---|
| **Pendahuluan** | 10 menit | 1) Membuka pelajaran dengan salam, doa, dan absensi. 2) Meninjau ulang proposal yang telah dikumpulkan — memastikan setiap kelompok siap implementasi. 3) Menjelaskan agenda pertemuan: "Hari ini kita eksekusi! Dari rencana jadi kenyataan. Kalian akan mengerjakan, menguji, dan memperbaiki proyek kalian." 4) Membagikan lembar issue log dan menjelaskan cara penggunaannya. 5) Menyampaikan target minimal pertemuan ini: 80% fitur utama selesai dan sudah diuji. | 1) Menjawab salam dan berdoa. 2) Mengecek kembali proposal dan memastikan semua alat/bahan sudah siap. 3) Mendengarkan agenda dan mencatat target harian. 4) Menerima lembar issue log dan membaca contoh pengisiannya. 5) Berkoordinasi dengan anggota kelompok mengenai pembagian tugas hari ini. | Proyektor, slide agenda, lembar issue log, proposal kelompok |
| **Inti — Tahap 1: Sesi Kerja Intensif** | 40 menit | 1) Berkeliling ke setiap kelompok untuk memonitor kemajuan. 2) Membantu kelompok yang mengalami kendala teknis (misal: error coding, masalah instalasi tools). 3) Mengajukan pertanyaan-pertanyaan probing: "Kenapa kamu memilih pendekatan ini?", "Apa yang terjadi jika inputnya salah?", "Bagaimana cara menyimpan data?" 4) Mencatat kemajuan setiap kelompok di lembar observasi guru. 5) Memberikan tantangan tambahan kepada kelompok yang sudah maju: "Coba tambahkan fitur sorting/pencarian!" | 1) Memulai pengerjaan sesuai pembagian tugas pada proposal. Teknisi mulai menulis kode/membangun antarmuka. 2) Desainer menyiapkan aset visual (gambar, ikon, layout). 3) Sekretaris mendokumentasikan proses dalam bentuk catatan atau foto. 4) Ketua memastikan semua anggota bekerja dan mengoordinasikan jika ada hambatan. 5) Mengacungkan tangan jika mengalami kendala teknis yang tidak bisa diselesaikan sendiri. | Laptop, VSCode/Scratch/Thunkable, aset proyek, koneksi internet, dokumentasi tools |
| **Inti — Tahap 2: Cek Kemajuan (Mid-Session Stand-up)** | 10 menit | 1) Meminta semua kelompok berhenti sejenak. 2) Memanggil setiap kelompok secara bergiliran untuk laporan kemajuan 1 menit. 3) Menanyakan: "Apa yang sudah dikerjakan?", "Apa kendala terbesar?", "Apa solusi yang sudah dicoba?" 4) Memberikan masukan singkat dan solusi untuk kendala yang disebutkan. 5) Memotivasi kelompok yang tertinggal. | 1) Berhenti mengerjakan proyek dan berkumpul dengan kelompok. 2) Perwakilan kelompok (ketua atau sekretaris) menyampaikan laporan kemajuan: (a) fitur yang sudah jadi, (b) kendala, (c) rencana setelah ini. 3) Mendengarkan masukan dari guru. 4) Mencatat solusi yang disarankan guru. 5) Menyemangati anggota kelompok yang lain. | Laporan lisan, catatan kemajuan guru |
| **Inti — Tahap 3: Pengujian Internal** | 15 menit | 1) Membagikan lembar issue log dan menjelaskan cara mengisi: nomor, deskripsi bug, tingkat keparahan (ringan/sedang/berat), status (open/fixed). 2) Memandu proses pengujian: "Sekarang, setiap anggota kelompok bergantian mencoba produk. Cari sebanyak mungkin bug! Catat semuanya di issue log." 3) Mengingatkan: "Tidak apa-apa menemukan banyak bug. Itu artinya kita jujur dan ingin produknya lebih baik." 4) Memastikan setiap anggota mendapat giliran mencoba. | 1) Menerima lembar issue log. 2) Anggota yang bukan teknisi (desainer, sekretaris, dokumentator) menjadi penguji utama. 3) Mencoba semua fitur yang sudah jadi: klik setiap tombol, isi setiap form, coba input yang salah. 4) Mencatat temuan di issue log: "Bug #1: tombol simpan tidak merespons saat input kosong — Severity: sedang — Status: open". 5) Mengumpulkan issue log ke teknisi untuk diperbaiki. | Lembar issue log, produk proyek (aplikasi/web), alat tulis |
| **Inti — Tahap 4: Iterasi Perbaikan** | 10 menit | 1) Meminta teknisi segera memperbaiki bug yang ditemukan berdasarkan prioritas (berat dulu, baru sedang/ringan). 2) Berkeliling membantu debugging: "Coba periksa kondisi if-nya", "Apakah variabelnya sudah terdefinisi?", "Coba tambahkan console.log untuk tracing." 3) Memvalidasi perbaikan: setelah teknisi mengklaim bug fixed, guru memeriksa ulang. 4) Memberi apresiasi saat kelompok berhasil memperbaiki bug (tepuk tangan atau stiker bintang). | 1) Teknisi menerima issue log dari tim penguji. 2) Memprioritaskan bug: severity BERAT diperbaiki dulu. 3) Memperbaiki kode/desain sesuai temuan. 4) Setelah diperbaiki, mengubah status issue menjadi "fixed". 5) Menunjukkan hasil perbaikan ke guru untuk validasi. 6) Anggota lain menyiapkan dokumentasi (screenshot before-after) untuk laporan. | Laptop, issue log, kode program, alat tulis |
| **Penutup** | 15 menit | 1) Meminta setiap kelompok mengisi lembar refleksi: "Apa kendala terbesar hari ini?" dan "Apa pencapaian terbesar?" 2) Mengumpulkan issue log dan lembar refleksi. 3) Mengingatkan tenggat final proyek (presentasi pada pertemuan ke-32). 4) Memberikan tugas: (a) lanjutkan pengerjaan di rumah jika belum selesai, (b) siapkan slide presentasi, (c) dokumentasikan produk dalam bentuk video singkat (max 2 menit). 5) Motivasi: "Produk hebat lahir dari proses yang tidak sempurna. Teruslah memperbaiki!" | 1) Mengisi lembar refleksi individu. 2) Mengumpulkan issue log dan refleksi ke meja guru. 3) Mencatat tenggat dan tugas mandiri. 4) Berdiskusi dengan kelompok untuk rencana pertemuan berikutnya. 5) Membersihkan meja dan merapikan peralatan. | Lembar refleksi, issue log, catatan tugas |
| **Catatan Pembelajaran Tambahan** | — | Jika waktu tidak cukup, sesi kerja intensif dapat dilanjutkan di luar jam pelajaran (tugas mandiri kelompok). Guru menyediakan sesi konsultasi via Google Classroom atau WhatsApp grup. Issue log dapat dilanjutkan secara digital menggunakan Google Sheets atau Trello. | — | Google Classroom, Google Sheets, Trello |

### D. ASESMEN

#### D.1 Asesmen Diagnostik
1. **Cek kesiapan**: setiap kelompok menunjukkan (a) proposal final, (b) daftar alat/bahan, (c) pembagian tugas sebelum memulai implementasi.
2. **Kuis teknis singkat** (lisan saat berkeliling): "Apa fungsi dari variable dalam kode?", "Bagaimana cara menampilkan output di tools yang kalian gunakan?"

#### D.2 Asesmen Formatif
1. **Observasi kerja kelompok**: mencatat partisipasi aktif setiap anggota (skala 1-4).
2. **Issue log**: kelengkapan dan ketepatan pencatatan bug/temuan.
3. **Cek kemajuan (stand-up)**: kemampuan menyampaikan kemajuan dan kendala secara jelas.
4. **Lembar refleksi**: kualitas refleksi individu tentang proses dan pembelajaran.

#### D.3 Asesmen Sumatif
**Produk**: Artefak komputasional yang berfungsi + laporan proyek akhir, dinilai dengan rubrik di bawah ini.

#### D.4 Rubrik Penilaian Implementasi & Pengujian Proyek

| No. | Kriteria | SB (4) — Sangat Baik | B (3) — Baik | C (2) — Cukup | PB (1) — Perlu Bimbingan |
|---|---|---|---|---|---|
| 1 | **Kesesuaian Implementasi** | ≥80% fitur sesuai proposal dan berfungsi penuh | 60-79% fitur sesuai proposal dan berfungsi | 40-59% fitur berfungsi, ada penyimpangan dari proposal | <40% fitur berfungsi atau tidak sesuai proposal |
| 2 | **Kualitas Pengujian** | Issue log lengkap (≥3 bug), severity jelas, semua bug terverifikasi | Issue log lengkap, severity jelas | Issue log terisi tapi kurang detail | Tidak ada issue log atau tidak diisi |
| 3 | **Perbaikan (Iterasi)** | Semua bug berat dan sedang diperbaiki (≥2 bug fixed) | Bug berat diperbaiki (≥1 bug fixed) | Ada upaya perbaikan tapi belum tuntas | Tidak ada perbaikan |
| 4 | **Dokumentasi & Laporan** | Laporan lengkap: proses, screenshot, kendala, solusi, link produk | Laporan lengkap tanpa screenshot | Laporan kurang lengkap | Tidak ada laporan |
| 5 | **Kolaborasi Tim** | Semua anggota berkontribusi aktif, pembagian tugas jelas | Sebagian besar anggota aktif | Hanya 1-2 anggota yang bekerja | Hanya 1 anggota yang bekerja |

**Nilai Akhir = (Total Skor / 20) × 100**

#### D.5 Contoh Laporan Proyek
Laporan diketik dengan format: (1) Halaman Judul & Identitas Kelompok, (2) Pendahuluan (latar belakang & tujuan), (3) Proses Implementasi (dokumentasi langkah-langkah pengerjaan), (4) Hasil Pengujian (issue log dan perbaikannya), (5) Dokumentasi Produk (screenshot dan/atau link video), (6) Kendala & Solusi, (7) Rencana Pengembangan Selanjutnya. Panjang minimal 4 halaman. Dikumpulkan dalam bentuk PDF via Google Classroom.

### E. LEMBAR KERJA PESERTA DIDIK (LKPD)

**LKPD 9.2: Implementasi & Pengujian Proyek Lintas Bidang**

**Nama Kelompok:** _____________ **Nama Proyek:** _____________ **Tanggal:** _____________

**Anggota — Peran & Tugas Hari Ini:**
1. _____________ (______) — Tugas: _______________________________________________
2. _____________ (______) — Tugas: _______________________________________________
3. _____________ (______) — Tugas: _______________________________________________
4. _____________ (______) — Tugas: _______________________________________________

**Tugas 1: Ceklis Kesiapan Implementasi**
Sebelum mulai, pastikan semua tersedia:
☐ Proposal proyek final sudah dicetak/dibuka
☐ Laptop/komputer menyala dan terhubung internet
☐ Tools pengembangan sudah terinstal (VSCode/Scratch/Thunkable/dll.)
☐ Aset desain sudah siap (gambar, ikon, font, warna)
☐ Akun Google Drive/GitHub sudah siap untuk backup
☐ Pembagian tugas hari ini sudah jelas

**Tugas 2: Log Pengerjaan (Sesi Intensif)**
| Waktu Mulai | Aktivitas | PIC | Keterangan |
|---|---|---|---|
| ___:___ | | | |
| ___:___ | | | |
| ___:___ | | | |
| ___:___ | | | |

**Tugas 3: Laporan Cek Kemajuan (Mid-Session)**
- Fitur yang sudah selesai: _____________________________________________________
- Kendala terbesar: ___________________________________________________________
- Rencana setelah ini: _________________________________________________________

**Tugas 4: Issue Log — Pengujian Internal**
| No. | Deskripsi Bug/Kekurangan | Fitur Terkait | Severity (Ringan/Sedang/Berat) | Status (Open/Fixed) | Validasi Guru |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |

**Tugas 5: Refleksi Individu**
Nama: _____________
1. Satu hal baru yang saya pelajari hari ini:
___________________________________________________________________________
2. Kontribusi saya untuk kelompok hari ini:
___________________________________________________________________________
3. Kendala yang saya hadapi:
___________________________________________________________________________
4. Hal yang akan saya lakukan lebih baik pada pertemuan berikut:
___________________________________________________________________________

### F. DIFERENSIASI PEMBELAJARAN

| Level | Karakteristik Peserta Didik | Strategi Diferensiasi |
|---|---|---|
| **Level 1 (Akselerasi)** | Kelompok yang menyelesaikan implementasi lebih cepat dari target dan ingin tantangan lebih | Ditugaskan untuk: (1) menambahkan fitur lanjutan (autentikasi pengguna, animasi, database, sorting/pencarian), (2) melakukan pengujian ke kelompok lain (cross-testing), (3) menyusun dokumentasi teknis dalam bahasa Inggris, (4) mendeploy proyek ke hosting gratis (GitHub Pages/Netlify). |
| **Level 2 (Reguler)** | Kelompok dengan kemampuan rata-rata, mengerjakan sesuai rencana proposal | Mengikuti alur standar: implementasi sesuai proposal, pengujian internal, perbaikan bug. Disediakan cheat sheet teknis dan contoh kode dari repositori guru. |
| **Level 3 (Pendampingan)** | Kelompok yang mengalami kesulitan teknis signifikan atau tertinggal | (1) Disediakan template kode/desain yang bisa langsung dimodifikasi, (2) Guru mendampingi secara intensif dengan pendekatan step-by-step, (3) Fitur dikurangi menjadi fitur esensial saja (minimal 2 fitur), (4) Boleh menggunakan tools yang lebih sederhana (Scratch daripada coding teks), (5) Anggota kelompok yang lebih mampu dipasangkan sebagai peer tutor. |

### G. REFLEKSI GURU

1. **Apakah target 80% fitur selesai tercapai?** ____ dari ____ kelompok mencapai target.
2. **Kendala teknis apa yang paling sering muncul?** ☐ Error kode ☐ Tools tidak kompatibel ☐ Aset tidak siap ☐ Jaringan internet ☐ Lainnya: _______________
3. **Apakah issue log digunakan dengan baik oleh semua kelompok?** ☐ Ya, semua ☐ Sebagian ☐ Tidak
4. **Kelompok mana yang membutuhkan sesi tambahan?** ________________________________
5. **Apakah alokasi waktu untuk pengujian (15 menit) cukup?** ☐ Ya ☐ Tidak, perlu ________ menit
6. **Strategi apa yang efektif hari ini?** ______________________________________________
7. **Hal apa yang perlu diperbaiki untuk implementasi proyek tahun depan?** _______________
8. **Catatan khusus tentang dinamika kelompok:** _____________________________________

### H. BAHAN BACAAN UNTUK GURU

1. **Buku Guru Informatika Kelas X** — Bab 9: Praktika Lintas Bidang, Kemendikbudristek.
2. **"The Art of Debugging"** — Panduan debugging untuk pemula dari GeeksforGeeks (https://www.geeksforgeeks.org/debugging-techniques/).
3. **"Issue Tracking for Beginners"** — Artikel tentang pentingnya issue log dalam pengembangan perangkat lunak (Atlassian Agile Coach).
4. **Panduan Pengujian Sederhana** — Materi dari ISTQB (International Software Testing Qualifications Board) level dasar yang sudah diadaptasi untuk pembelajaran SMA.
5. **Video tutorial implementasi proyek:** (a) "Coding a Website in 30 Minutes" — freeCodeCamp, (b) "Scratch Project Tutorial" — Scratch Team, (c) "Thunkable App Development" — Thunkable Docs.
6. **Contoh dokumentasi proyek siswa:** repositori publik dari siswa SMA yang mengikuti lomba INFORMATIKA atau LKS.
7. **"Peer Review dalam Project Based Learning"** — Jurnal Pendidikan Vokasi, 2023: strategi melakukan review antarkelompok.
8. **Checklist presentasi proyek** — format penilaian untuk pertemuan berikutnya (presentasi final).

---

Mengetahui,
Kepala Sekolah

_________________________

Guru Mata Pelajaran,

Daniarsyah, S.Kom.
NIP. 198004052022211004
