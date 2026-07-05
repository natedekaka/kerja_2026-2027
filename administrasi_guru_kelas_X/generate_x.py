#!/usr/bin/env python3
"""
Generator dokumen administrasi Guru Kelas X — Informatika Fase E (2 JP/minggu)
Buku: Informatika untuk SMA/MA/SMK/MAK Kelas X (Edisi Revisi) — Kemendikdasmen
Tahun Pelajaran 2026/2027

16 root documents (tanpa modul ajar):
  1. 00_COVER.md
  2. 01_ANALISIS_ALOKASI_WAKTU.md
  3. 01b_RPE_Rincian_Pekan_Efektif.md
  4. 02_PROTA.md
  5. 03_PROSEM.md
  6. 04_ATP.md
  7. 05_KKTP.md
  8. 06_PEMETAAN_KOMPETENSI_PENILAIAN.md
  9. 06b_BANK_SOAL.md
 10. 06c_PROGRAM_KOKURIKULER_8_DIMENSI.md
 11. 07_JURNAL_MENGAJAR.md
 12. 08_ANALISIS_CP_TP.md
 13. 09_DAFTAR_NILAI.md
 14. 10_PROGRAM_REMEDIAL_PENGAYAAN.md
 15. 11_INVENTARIS_LAB.md
 16. 12_JADWAL_LAB_BUKU_PRAKTIK.md
"""

import os

BASE = os.path.dirname(os.path.abspath(__file__))

GURU = "Daniarsyah, S.Kom."
NIP = "198004052022211004"
GOL = "IX"
SEKOLAH = "SMA Negeri 6 Cimahi"
MAPEL = "Informatika"
KELAS = "X"
FASE = "E"
TP = "2026/2027"

CP_ELEMEN = {
    "BK": "Berpikir Komputasional",
    "TIK": "Teknologi Informasi dan Komunikasi",
    "SK": "Sistem Komputer",
    "JKI": "Jaringan Komputer dan Internet",
    "AD": "Analisis Data",
    "AP": "Algoritma dan Pemrograman",
    "DSI": "Dampak Sosial Informatika",
    "PLB": "Praktik Lintas Bidang"
}

CP_TEKS = {
    "BK": "Pada akhir fase E, peserta didik mampu memahami validitas sumber data, menggunakan mesin pencari dengan variabel lebih banyak, mengetahui ekosistem periksa fakta, menggunakan cara membaca lateral untuk mengevaluasi informasi digital, serta menerapkan strategi algoritmik standar untuk menghasilkan beberapa solusi persoalan dengan data diskrit bervolume tidak kecil pada kehidupan sehari-hari maupun implementasinya dalam program komputer.",
    "TIK": "Pada akhir fase E, peserta didik mampu memanfaatkan berbagai aplikasi secara bersamaan dan optimal untuk berkomunikasi, mencari sumber data yang akan diolah menjadi informasi, serta mahir menggunakan fitur lanjut aplikasi perkantoran beserta otomasinya untuk mengintegrasikan dan menyajikan konten aplikasi.",
    "SK": "Pada akhir fase E, peserta didik mampu memahami peran sistem operasi dan mekanisme internal yang terjadi pada interaksi antara perangkat keras, perangkat lunak, dan pengguna.",
    "JKI": "Pada akhir fase E, peserta didik mampu menerapkan konektivitas jaringan lokal, komunikasi data via ponsel, konektivitas internet melalui jaringan kabel dan nirkabel, serta enkripsi untuk memproteksi data pada saat penyambungan perangkat ke jaringan.",
    "AD": "Pada akhir fase E, peserta didik mampu memahami aspek privasi dan keamanan data, mengumpulkan data secara otomatis dari berbagai sumber data, memodelkan data berbagai bidang, serta menerapkan siklus pengolahan data (pengumpulan, pengolahan, visualisasi, analisis, interpretasi, publikasi) dengan menggunakan perkakas TIK yang sesuai.",
    "AP": "Pada akhir fase E, peserta didik mampu menerapkan praktik baik konsep pemrograman prosedural dalam salah satu bahasa pemrograman prosedural (Python) dan mampu mengembangkan program yang terstruktur dalam notasi algoritma atau notasi lain berdasarkan strategi algoritmik yang tepat.",
    "DSI": "Pada akhir fase E, peserta didik mampu memahami sejarah perkembangan komputer dan tokoh-tokohnya, memahami hak kekayaan intelektual, lisensi, aspek teknis, hukum, ekonomi, lingkungan, dan sosial dari produk TIK.",
    "PLB": "Pada akhir fase E, peserta didik mampu bergotong royong untuk menyelesaikan suatu persoalan kompleks dengan mengembangkan artefak komputasional, serta mengomunikasikan rancangan produk, produk, dan prosesnya secara lisan dan tertulis."
}

DIMENSI = [
    ("Keimanan dan Ketakwaan kepada Tuhan YME", "Berakhlak mulia, menjalankan ajaran agama, toleransi"),
    ("Kewargaan (Citizenship)", "Cinta tanah air, kesadaran berbangsa, hak & kewajiban sebagai warga negara"),
    ("Penalaran Kritis", "Menganalisis, mengevaluasi, menarik kesimpulan berbasis data"),
    ("Kreativitas", "Menghasilkan gagasan & karya orisinal, berpikir divergen"),
    ("Kolaborasi", "Bekerja sama dalam tim, menghargai perbedaan, kepemimpinan"),
    ("Kemandirian", "Inisiatif, regulasi diri, tanggung jawab, percaya diri"),
    ("Kesehatan", "Kebugaran jasmani, kesehatan mental, gaya hidup aktif"),
    ("Komunikasi", "Menyampaikan gagasan secara lisan & tulisan, literasi digital, presentasi")
]

# === DATA ELEMEN & TP ===
ELEMEN_DATA = [
    {
        "id": "0", "singkatan": "", "nama": "Pengenalan & Kontrak Belajar", "jp": 2, "smt": 1,
        "cp_elemen": "", "cp_teks": "Menyepakati tujuan & aturan pembelajaran Informatika",
        "tp_list": [
            {"kode": "0.1", "judul": "Menjelaskan tujuan, ruang lingkup, dan sistem penilaian Informatika kelas 10", "indikator": "Menyebutkan 8 elemen Informatika & sistem penilaian dengan benar", "materi": "Ruang lingkup Informatika Fase E", "kegiatan": "Diskusi interaktif & kontrak belajar", "dimensi": "Kemandirian, Penalaran Kritis", "sumber": "Buku Bab 1, Silabus", "kktp_indikator": ["Menjelaskan 8 elemen Informatika", "Memahami sistem penilaian", "Mengetahui ruang lingkup pembelajaran"]},
            {"kode": "0.2", "judul": "Menyepakati kontrak belajar, norma digital, dan penggunaan perangkat selama KBM", "indikator": "Menandatangani kontrak belajar & aturan penggunaan perangkat", "materi": "Aturan KBM, etika digital dasar", "kegiatan": "Simulasi tata tertib & penandatangan kontrak", "dimensi": "Keimanan & Ketakwaan, Kolaborasi", "sumber": "\u2014", "kktp_indikator": ["Menyepakati kontrak belajar", "Memahami norma digital", "Mematuhi aturan penggunaan perangkat"]}
        ]
    },
    {
        "id": "1", "singkatan": "BK", "nama": "Berpikir Komputasional", "jp": 8, "smt": 1,
        "cp_elemen": "BK", "cp_teks": CP_TEKS["BK"],
        "tp_list": [
            {"kode": "1.1", "judul": "Mendekomposisi masalah kompleks menjadi sub-masalah yang lebih kecil dan terkelola", "indikator": "Memecah minimal 1 masalah kompleks menjadi 3+ sub-masalah secara logis", "materi": "Dekomposisi (decomposition)", "kegiatan": "Studi kasus: memecah masalah sehari-hari (Studi Kasus)", "dimensi": "Penalaran Kritis, Kemandirian", "sumber": "Buku Bab 2, LKPD", "kktp_indikator": ["Mengidentifikasi masalah utama", "Memecah menjadi sub-masalah", "Menjelaskan hubungan antar sub-masalah"]},
            {"kode": "1.2", "judul": "Mengidentifikasi pola/kesamaan dari sekumpulan data atau situasi masalah", "indikator": "Menemukan minimal 2 pola dari data yang diberikan", "materi": "Pengenalan Pola (pattern recognition)", "kegiatan": "Eksplorasi data: menemukan pola dari deret angka/gambar", "dimensi": "Penalaran Kritis, Kreativitas", "sumber": "Buku Bab 2, LKPD", "kktp_indikator": ["Mengamati data dengan teliti", "Menemukan kesamaan/pola", "Menjelaskan pola yang ditemukan"]},
            {"kode": "1.3", "judul": "Melakukan abstraksi dengan memilah informasi esensial dan non-esensial", "indikator": "Menentukan informasi penting & membuang informasi tidak relevan dari suatu kasus", "materi": "Abstraksi (abstraction)", "kegiatan": "Latihan: memilah info penting dari deskripsi masalah kompleks", "dimensi": "Penalaran Kritis", "sumber": "Buku Bab 2, LKPD", "kktp_indikator": ["Mengidentifikasi info penting", "Membuang info tidak relevan", "Menyederhanakan masalah"]},
            {"kode": "1.4", "judul": "Menyusun algoritma solusi menggunakan pseudocode atau flowchart untuk suatu persoalan", "indikator": "Membuat algoritma dalam bentuk flowchart/pseudocode untuk 1 kasus", "materi": "Perancangan Algoritma (algorithm design)", "kegiatan": "Praktik menyusun algoritma solusi (unplugged)", "dimensi": "Kreativitas, Kemandirian", "sumber": "Buku Bab 2, LKPD", "kktp_indikator": ["Menulis pseudocode logis", "Menggambar flowchart sesuai notasi", "Algoritma menghasilkan output benar"]}
        ]
    },
    {
        "id": "2", "singkatan": "TIK", "nama": "Teknologi Informasi & Komunikasi", "jp": 8, "smt": 1,
        "cp_elemen": "TIK", "cp_teks": CP_TEKS["TIK"],
        "tp_list": [
            {"kode": "2.1", "judul": "Menggunakan fitur lanjut pengolah kata (mail merge, daftar isi, referensi) untuk dokumentasi", "indikator": "Menghasilkan dokumen dengan mail merge, daftar isi otomatis, dan daftar pustaka", "materi": "Mail merge, daftar isi, footnote, daftar pustaka (MS Word / Google Docs)", "kegiatan": "Praktik membuat dokumen formal (makalah) dengan fitur lanjut", "dimensi": "Kemandirian, Kreativitas", "sumber": "Buku Bab 3, Komputer", "kktp_indikator": ["Mail merge berfungsi", "Daftar isi otomatis", "Format dokumen rapi"]},
            {"kode": "2.2", "judul": "Mengolah data menggunakan formula, fungsi, dan grafik pada spreadsheet", "indikator": "Mengolah data menggunakan minimal 5 fungsi (SUM, AVERAGE, VLOOKUP, IF, COUNTIF) dan menyajikan grafik", "materi": "Formula & fungsi spreadsheet, grafik, pivot table (MS Excel / Google Sheets)", "kegiatan": "Praktik mengolah data nilai & membuat dashboard", "dimensi": "Penalaran Kritis, Kreativitas", "sumber": "Buku Bab 3, Komputer", "kktp_indikator": ["Menggunakan formula", "Membuat grafik sesuai data", "Menginterpretasi hasil"]},
            {"kode": "2.3", "judul": "Membuat presentasi interaktif dengan fitur animasi, hyperlink, dan kolaborasi daring", "indikator": "Membuat presentasi dengan slide master, animasi kustom, hyperlink, dan kolaborasi real-time", "materi": "Slide master, animasi, hyperlink, kolaborasi (MS PowerPoint / Google Slides)", "kegiatan": "Praktik presentasi interaktif produk informasi", "dimensi": "Kreativitas, Kolaborasi", "sumber": "Buku Bab 3, Komputer", "kktp_indikator": ["Slide master digunakan", "Animasi/hyperlink berfungsi", "Kolaborasi real-time"]},
            {"kode": "2.4", "judul": "Mengintegrasikan data antar aplikasi perkantoran (mail merge dari spreadsheet, chart di presentasi)", "indikator": "Mengintegrasikan 2+ aplikasi untuk menyelesaikan satu tugas terpadu", "materi": "Otomasi & integrasi aplikasi perkantoran", "kegiatan": "Proyek mini: membuat laporan terintegrasi (data \u2192 grafik \u2192 presentasi)", "dimensi": "Kreativitas, Kemandirian", "sumber": "Buku Bab 3, Komputer", "kktp_indikator": ["Data terhubung antar aplikasi", "Output terintegrasi", "Efisien & rapi"]}
        ]
    },
    {
        "id": "3", "singkatan": "SK", "nama": "Sistem Komputer", "jp": 6, "smt": 1,
        "cp_elemen": "SK", "cp_teks": CP_TEKS["SK"],
        "tp_list": [
            {"kode": "3.1", "judul": "Mengidentifikasi komponen perangkat keras komputer dan menjelaskan fungsinya", "indikator": "Menyebutkan minimal 8 komponen HW dan fungsinya dengan benar", "materi": "Perangkat keras: CPU, RAM, storage, GPU, motherboard, dll", "kegiatan": "Eksplorasi perangkat komputer: identifikasi komponen internal PC", "dimensi": "Kemandirian, Penalaran Kritis", "sumber": "Buku Bab 4, Komputer", "kktp_indikator": ["Menyebutkan nama komponen", "Menjelaskan fungsi", "Mengidentifikasi pada PC nyata"]},
            {"kode": "3.2", "judul": "Menjelaskan peran sistem operasi dalam mengelola sumber daya dan interaksi HW-SW-user", "indikator": "Membedakan fungsi kernel, driver, file system, dan shell/interface", "materi": "Sistem operasi: kernel, driver, file system, OS modern (Windows, Linux, macOS)", "kegiatan": "Studi kasus perbandingan OS & simulasi manajemen file", "dimensi": "Penalaran Kritis", "sumber": "Buku Bab 4", "kktp_indikator": ["Menjelaskan kernel", "Menjelaskan driver", "Menjelaskan file system"]},
            {"kode": "3.3", "judul": "Menganalisis mekanisme internal sistem komputer mulai dari booting hingga eksekusi aplikasi", "indikator": "Menjelaskan alur booting, loading driver, dan eksekusi program", "materi": "Booting, BIOS/UEFI, loading OS, manajemen memori", "kegiatan": "Simulasi alur booting & diagram interaksi HW-SW-user", "dimensi": "Penalaran Kritis", "sumber": "Buku Bab 4", "kktp_indikator": ["Diagram alur booting", "Menjelaskan peran BIOS/UEFI", "Menjelaskan loading OS"]}
        ]
    },
    {
        "id": "4", "singkatan": "JKI", "nama": "Jaringan Komputer & Internet", "jp": 6, "smt": 1,
        "cp_elemen": "JKI", "cp_teks": CP_TEKS["JKI"],
        "tp_list": [
            {"kode": "4.1", "judul": "Menjelaskan jenis jaringan, topologi, dan perangkat jaringan beserta fungsinya", "indikator": "Menggambar topologi jaringan dan menyebutkan fungsi 5+ perangkat jaringan", "materi": "LAN, WAN, topologi (star, bus, ring, mesh), perangkat (router, switch, modem, AP)", "kegiatan": "Simulasi topologi jaringan & identifikasi perangkat di lab", "dimensi": "Penalaran Kritis", "sumber": "Buku Bab 5", "kktp_indikator": ["Menggambar topologi", "Menyebutkan perangkat", "Menjelaskan fungsi perangkat"]},
            {"kode": "4.2", "judul": "Menerapkan konfigurasi konektivitas internet (IP address, DNS, WiFi)", "indikator": "Melakukan konfigurasi IP statis/dinamis dan koneksi WiFi", "materi": "IP address, DNS, DHCP, WiFi, koneksi kabel/nirkabel", "kegiatan": "Praktik konfigurasi jaringan: setting IP, koneksi WiFi, troubleshooting", "dimensi": "Kemandirian, Kolaborasi", "sumber": "Buku Bab 5", "kktp_indikator": ["Setting IP address", "Koneksi ke jaringan", "Troubleshooting dasar"]},
            {"kode": "4.3", "judul": "Menerapkan enkripsi sederhana dan proteksi data saat tersambung ke jaringan", "indikator": "Mengenkripsi data sederhana (Caesar cipher) & mengaktifkan proteksi (firewall, VPN dasar)", "materi": "Enkripsi (Caesar cipher), firewall, VPN, HTTPS, keamanan WiFi", "kegiatan": "Praktik enkripsi sederhana & simulasi proteksi jaringan", "dimensi": "Keimanan & Ketakwaan, Penalaran Kritis", "sumber": "Buku Bab 5", "kktp_indikator": ["Melakukan enkripsi Caesar cipher", "Menjelaskan firewall/VPN", "Menerapkan proteksi data"]}
        ]
    },
    {
        "id": "6", "singkatan": "AD", "nama": "Analisis Data", "jp": 8, "smt": 2,
        "cp_elemen": "AD", "cp_teks": CP_TEKS["AD"],
        "tp_list": [
            {"kode": "6.1", "judul": "Membedakan konsep data, informasi, dan pengetahuan serta tahapan siklus pengolahan data", "indikator": "Menjelaskan perbedaan data-informasi-pengetahuan dengan contoh nyata", "materi": "Data, informasi, pengetahuan; siklus pengolahan data", "kegiatan": "Diskusi & studi kasus: dari data mentah \u2192 informasi \u2192 keputusan", "dimensi": "Penalaran Kritis", "sumber": "Buku Bab 6", "kktp_indikator": ["Definisi data", "Definisi informasi", "Definisi pengetahuan"]},
            {"kode": "6.2", "judul": "Menganalisis aspek privasi dan keamanan data pribadi di era digital", "indikator": "Mengidentifikasi 5+ risiko kebocoran data & cara pencegahannya", "materi": "Privasi data, keamanan data, regulasi (UU PDP), phishing", "kegiatan": "Studi kasus kebocoran data & simulasi phishing", "dimensi": "Keimanan & Ketakwaan, Penalaran Kritis", "sumber": "Buku Bab 6", "kktp_indikator": ["Risiko kebocoran data", "Regulasi perlindungan data", "Cara pencegahan"]},
            {"kode": "6.3", "judul": "Menerapkan siklus pengolahan data dari pengumpulan hingga interpretasi menggunakan perkakas TIK", "indikator": "Mengumpulkan data dari 2+ sumber, membersihkan, & mengolah di spreadsheet", "materi": "Pengumpulan data (form, web scraping dasar), pembersihan, transformasi data", "kegiatan": "Praktik: mengumpulkan data (Google Forms), membersihkan, & mengolah", "dimensi": "Kemandirian, Kreativitas", "sumber": "Buku Bab 6, Komputer", "kktp_indikator": ["Mengumpulkan dari \u22652 sumber", "Membersihkan data", "Mengolah di spreadsheet"]},
            {"kode": "6.4", "judul": "Menyajikan visualisasi data dan menarik interpretasi/kesimpulan", "indikator": "Membuat 3+ jenis grafik/dashboard dan menulis interpretasi data", "materi": "Visualisasi data (chart, dashboard), analisis, interpretasi", "kegiatan": "Praktik membuat dashboard data (Google Data Studio/Sheets)", "dimensi": "Kreativitas, Penalaran Kritis", "sumber": "Buku Bab 6, Komputer", "kktp_indikator": ["Variasi grafik", "Dashboard informatif", "Interpretasi tepat"]}
        ]
    },
    {
        "id": "7", "singkatan": "AP", "nama": "Algoritma & Pemrograman", "jp": 14, "smt": 2,
        "cp_elemen": "AP", "cp_teks": CP_TEKS["AP"],
        "tp_list": [
            {"kode": "7.1", "judul": "Menulis notasi algoritma (pseudocode & flowchart) untuk solusi persoalan sehari-hari", "indikator": "Membuat pseudocode & flowchart untuk 2 kasus berbeda (sekuensial & percabangan)", "materi": "Pseudocode, flowchart, algoritma sekuensial", "kegiatan": "Unplugged: merancang algoritma tanpa komputer", "dimensi": "Penalaran Kritis, Kreativitas", "sumber": "Buku Bab 7", "kktp_indikator": ["Pseudocode benar", "Flowchart sesuai notasi", "Output sesuai"]},
            {"kode": "7.2", "judul": "Menggunakan variabel, tipe data, dan I/O dalam bahasa Python", "indikator": "Menulis program Python dengan input, proses, output yang benar", "materi": "Python: variabel, tipe data (int, float, str, bool), input(), print()", "kegiatan": "Praktik coding Python: program konversi suhu/sederhana", "dimensi": "Kemandirian, Kreativitas", "sumber": "Buku Bab 7, Komputer, Python", "kktp_indikator": ["Variabel tepat", "Tipe data sesuai", "Input/output benar"]},
            {"kode": "7.3", "judul": "Menerapkan struktur sekuensial & percabangan (if/elif/else, nested if) dalam program", "indikator": "Membuat program dengan minimal 2 kondisi percabangan yang benar", "materi": "Percabangan: if, if-else, elif, nested if", "kegiatan": "Praktik: program penentu kelulusan, kategori usia", "dimensi": "Kreativitas, Penalaran Kritis", "sumber": "Buku Bab 7, Komputer", "kktp_indikator": ["Syntax if benar", "Logika kondisi tepat", "Output sesuai input"]},
            {"kode": "7.4", "judul": "Menerapkan perulangan (for, while) untuk pemrosesan data berulang", "indikator": "Membuat program dengan perulangan for dan while (minimal 2 kasus)", "materi": "Perulangan: for, while, range, nested loop", "kegiatan": "Praktik: program deret bilangan, tabel perkalian", "dimensi": "Kreativitas, Penalaran Kritis", "sumber": "Buku Bab 7, Komputer", "kktp_indikator": ["For loop benar", "While loop benar", "Loop berhenti tepat"]},
            {"kode": "7.5", "judul": "Membuat fungsi untuk program modular", "indikator": "Membuat minimal 2 fungsi dengan parameter & return value", "materi": "Fungsi: definisi, parameter, return value, scope variabel", "kegiatan": "Praktik: program modular dengan fungsi", "dimensi": "Kreativitas, Kemandirian", "sumber": "Buku Bab 7, Komputer", "kktp_indikator": ["Definisi fungsi benar", "Parameter & return", "Fungsi dipanggil"]},
            {"kode": "7.6", "judul": "Melakukan debugging dan menangani error pada program Python", "indikator": "Menemukan & memperbaiki 3+ jenis error (syntax, runtime, logic)", "materi": "Debugging: tracing, breakpoint, try-except, error handling", "kegiatan": "Praktik debugging: mencari & memperbaiki error dalam kode", "dimensi": "Kemandirian, Penalaran Kritis", "sumber": "Buku Bab 7, Komputer", "kktp_indikator": ["Identifikasi error", "Memperbaiki syntax error", "Memperbaiki logic error"]},
            {"kode": "7.7", "judul": "Mengembangkan program Python terstruktur sebagai solusi atas persoalan nyata", "indikator": "Menghasilkan program Python utuh (min. 50 baris) yang menyelesaikan 1 masalah spesifik", "materi": "Proyek pemrograman: analisis \u2192 desain \u2192 coding \u2192 testing", "kegiatan": "Proyek individual: program pengelolaan data/konversi/kalkulator", "dimensi": "Kreativitas, Kemandirian, Penalaran Kritis", "sumber": "Buku Bab 7, Komputer", "kktp_indikator": ["Program berjalan", "Terstruktur", "Menyelesaikan masalah"]}
        ]
    },
    {
        "id": "8", "singkatan": "DSI", "nama": "Dampak Sosial Informatika", "jp": 6, "smt": 2,
        "cp_elemen": "DSI", "cp_teks": CP_TEKS["DSI"],
        "tp_list": [
            {"kode": "8.1", "judul": "Menjelaskan sejarah perkembangan komputer dan kontribusi tokoh-tokoh penting", "indikator": "Membuat timeline sejarah komputer dengan 10+ tonggak penting", "materi": "Sejarah komputer: generasi 1\u20135, tokoh (Turing, von Neumann, Jobs, dll)", "kegiatan": "Presentasi kelompok: timeline sejarah komputer & tokoh", "dimensi": "Kewargaan, Kemandirian", "sumber": "Buku Bab 8", "kktp_indikator": ["Urutan kronologis", "Tokoh penting", "Peristiwa signifikan"]},
            {"kode": "8.2", "judul": "Membedakan jenis lisensi perangkat lunak dan memahami HAKI", "indikator": "Mengklasifikasikan 5+ lisensi software (open source vs proprietary) dan menjelaskan HAKI", "materi": "HAKI, lisensi (GPL, MIT, Apache, proprietary), creative commons, open source", "kegiatan": "Studi kasus: perbandingan lisensi & simulasi pencatatan HAKI", "dimensi": "Keimanan & Ketakwaan, Penalaran Kritis", "sumber": "Buku Bab 8", "kktp_indikator": ["Membedakan open source/proprietary", "Menjelaskan HAKI", "Contoh lisensi"]},
            {"kode": "8.3", "judul": "Menganalisis dampak positif & negatif TIK di berbagai bidang (ekonomi, sosial, lingkungan)", "indikator": "Menulis esai analisis dampak TIK dengan argumen pro-kontra minimal 3 bidang", "materi": "Dampak TIK: ekonomi (e-commerce), sosial (medsos), lingkungan (e-waste), profesi IT", "kegiatan": "Debat/diskusi: dampak TIK & proyek literasi digital", "dimensi": "Penalaran Kritis, Kewargaan", "sumber": "Buku Bab 8", "kktp_indikator": ["Analisis \u22653 bidang", "Argumen seimbang", "Kesimpulan logis"]}
        ]
    },
    {
        "id": "9", "singkatan": "PLB", "nama": "Praktik Lintas Bidang", "jp": 6, "smt": 2,
        "cp_elemen": "PLB", "cp_teks": CP_TEKS["PLB"],
        "tp_list": [
            {"kode": "9.1", "judul": "Mengidentifikasi persoalan nyata di lingkungan sekitar & merencanakan solusi komputasional", "indikator": "Menyusun proposal proyek (latar belakang, tujuan, rencana implementasi)", "materi": "Identifikasi masalah, perencanaan proyek, pembagian peran tim", "kegiatan": "Diskusi kelompok: identifikasi masalah sekolah/lingkungan & proposal", "dimensi": "Kolaborasi, Kemandirian", "sumber": "Buku Bab 9", "kktp_indikator": ["Latar belakang jelas", "Tujuan spesifik", "Rencana realistis"]},
            {"kode": "9.2", "judul": "Mengimplementasikan & menguji artefak komputasional sebagai solusi persoalan", "indikator": "Menghasilkan prototipe/solusi (program, website, poster interaktif, dll.) dan mengujinya", "materi": "Implementasi, pengujian, debugging, iterasi perbaikan", "kegiatan": "Kerja kelompok: membangun solusi sesuai rencana", "dimensi": "Kolaborasi, Kreativitas", "sumber": "Buku Bab 9, Komputer, Tools", "kktp_indikator": ["Produk berfungsi", "Pengujian dilakukan", "Iterasi perbaikan"]},
            {"kode": "9.3", "judul": "Mempresentasikan produk, proses pengembangan, dan manfaatnya bagi masyarakat", "indikator": "Menyajikan presentasi final (produk + dokumentasi proses) dan menerima umpan balik", "materi": "Presentasi, demonstrasi produk, refleksi, dokumentasi proyek", "kegiatan": "Presentasi final & pameran karya Informatika", "dimensi": "Kolaborasi, Kreativitas, Kemandirian", "sumber": "Buku Bab 9", "kktp_indikator": ["Presentasi jelas", "Demonstrasi produk", "Refleksi tim"]}
        ]
    }
]


# =========== FUNGSI GENERATOR ===========

def dimensi_tabel_singkat():
    lines = ["### Profil Lulusan 8 Dimensi (Integrasi Deep Learning)\n"]
    lines.append("| No | Dimensi Kompetensi | Deskripsi |")
    lines.append("|---|---|---|")
    for i, (d, desk) in enumerate(DIMENSI, 1):
        lines.append(f"| {i} | **{d}** | {desk} |")
    return "\n".join(lines) + "\n"


# =========== 1. COVER ===========
def cover():
    return f"""# ADMINISTRASI GURU INFORMATIKA

## KELAS X (FASE E) — TAHUN PELAJARAN 2026/2027

---

**MATA PELAJARAN** : Informatika  
**KELAS / FASE** : X (Sepuluh) / Fase E  
**JUMLAH JP** : 2 JP per minggu  
**TAHUN PELAJARAN** : 2026/2027  
**BUKU SUMBER** : Informatika untuk SMA/MA/SMK/MAK Kelas X (Edisi Revisi) — Kemendikdasmen RI

---

### IDENTITAS GURU

| | |
|---|---|
| Nama Guru | : {GURU} |
| NIP / NUPTK | : {NIP} |
| Pangkat / Gol. | : Guru Ahli Pertama / {GOL} |
| Unit Kerja | : {SEKOLAH} |
| Alamat Sekolah | : Jalan Melong Raya No. 172 Cijerah — Cimahi Selatan |
| Provinsi | : Jawa Barat |

---

### DOKUMEN ADMINISTRASI

| No | Dokumen | Keterangan |
|---|---|---|
| 1 | Analisis Alokasi Waktu | Perhitungan JP efektif per tahun |
| 2 | Program Tahunan (PROTA) | Pembagian elemen per semester |
| 3 | Program Semester (PROMES) | Rincian per bulan/minggu |
| 4 | ATP (Alur Tujuan Pembelajaran) | Silabus Kurikulum Merdeka |
| 5 | KKTP (Kriteria Ketercapaian TP) | Interval nilai & predikat |
| 6 | Pemetaan Kompetensi & Penilaian | Teknik & instrumen asesmen |
| 7 | Jurnal Mengajar Guru | Catatan harian pembelajaran |
| 8 | Analisis CP - TP | Keterkaitan CP ke tujuan pembelajaran |
| 9 | Daftar Nilai | Rekap nilai pengetahuan & keterampilan |
| 10 | Modul Ajar | Rencana pembelajaran per pertemuan |
| 11 | Program Remedial & Pengayaan | Tindak lanjut hasil belajar |

---

### CAPAIAN PEMBELAJARAN INFORMATIKA FASE E

| Elemen | Deskripsi CP |
|---|---|
| **BK** — Berpikir Komputasional | Memahami validitas sumber data, mesin pencari variabel, ekosistem periksa fakta, membaca lateral; menerapkan strategi algoritmik standar untuk solusi persoalan data diskrit bervolume tidak kecil |
| **TIK** — Teknologi Informasi & Komunikasi | Memanfaatkan aplikasi secara bersamaan & optimal; mahir fitur lanjut aplikasi perkantoran (pengolah kata, angka, presentasi) beserta otomasinya |
| **SK** — Sistem Komputer | Memahami peran sistem operasi, mekanisme internal interaksi HW/SW/user |
| **JKI** — Jaringan Komputer & Internet | Menerapkan konektivitas jaringan lokal, internet kabel/nirkabel, enkripsi proteksi data |
| **AD** — Analisis Data | Memahami privasi & keamanan data, mengumpulkan data otomatis, siklus pengolahan data, visualisasi, interpretasi |
| **AP** — Algoritma & Pemrograman | Menerapkan pemrograman prosedural tekstual terstruktur (Python) berdasarkan strategi algoritmik |
| **DSI** — Dampak Sosial Informatika | Memahami sejarah komputer, HAKI, lisensi, aspek hukum/ekonomi/lingkungan/sosial produk TIK |
| **PLB** — Praktik Lintas Bidang | Proyek tematik: identifikasi masalah → desain → implementasi → uji → presentasi artefak komputasional |

---

{dimensi_tabel_singkat()}

---

> Dokumen ini disusun untuk Tahun Pelajaran 2026/2027  
> Berdasarkan Capaian Pembelajaran Kurikulum Merdeka,  
> **Profil Lulusan 8 Dimensi** (Permendikdasmen No. 13/2025),  
> **Gerakan 7 Kebiasaan Anak Indonesia Hebat** (SEB 3 Menteri No. 1/2025),  
> serta **Pendekatan Pembelajaran Mendalam (Deep Learning)** — Mindful, Meaningful, Joyful —  
> yang diintegrasikan ke dalam setiap modul ajar dan kegiatan kokurikuler.
"""


# =========== 2. ANALISIS ALOKASI WAKTU ===========
def analisis_alokasi_waktu():
    return f"""# ANALISIS ALOKASI WAKTU

**Mata Pelajaran** : Informatika  
**Kelas / Fase** : X (Sepuluh) / Fase E  
**Tahun Pelajaran** : 2026/2027  
**Jumlah JP per Minggu** : 2 JP (1 JP = 45 menit)

---

## A. STRUKTUR KURIKULUM

| Komponen | Keterangan |
|---|---|
| Mata Pelajaran | Informatika (Kelompok MIPA) |
| Fase | E (Kelas X) |
| Alokasi Waktu | 2 JP per minggu |
| Durasi 1 JP | 45 menit |
| Total JP per Tahun | 76 JP (38 minggu × 2 JP) |

---

## B. PERHITUNGAN MINGGU EFEKTIF

### Semester 1 (Ganjil) — TP 2026/2027

| No | Bulan | Jml Minggu | Minggu Efektif | Keterangan |
|---|---|---|---|---|
| 1 | Juli 2026 | 4 | 3 | Minggu ke-1: MPLS/Pengenalan |
| 2 | Agustus 2026 | 4 | 4 | Belajar Efektif |
| 3 | September 2026 | 4 | 4 | Belajar Efektif |
| 4 | Oktober 2026 | 4 | 4 | Belajar Efektif |
| 5 | November 2026 | 4 | 3 | Minggu ke-4: PTS |
| 6 | Desember 2026 | 4 | 2 | Minggu ke-1: PAS, minggu ke-2: Libur |
| | **Jumlah** | **24** | **20** | |

### Semester 2 (Genap) — TP 2026/2027

| No | Bulan | Jml Minggu | Minggu Efektif | Keterangan |
|---|---|---|---|---|
| 1 | Januari 2027 | 4 | 4 | Belajar Efektif |
| 2 | Februari 2027 | 4 | 4 | Belajar Efektif |
| 3 | Maret 2027 | 4 | 4 | Belajar Efektif |
| 4 | April 2027 | 4 | 3 | Minggu ke-4: PTS |
| 5 | Mei 2027 | 4 | 3 | Belajar Efektif |
| 6 | Juni 2027 | 4 | 2 | Minggu ke-1: PAT, minggu ke-2: Libur |
| | **Jumlah** | **24** | **20** |

---

## C. REKAPITULASI MINGGU EFEKTIF

| Uraian | Semester 1 | Semester 2 | Total |
|---|---|---|---|
| Total Minggu | 24 | 24 | 48 |
| Minggu Tidak Efektif | 4 | 4 | 8 |
| **Minggu Efektif** | **20** | **20** | **40** |

---

## D. ALOKASI JP PER SEMESTER

| Uraian | Semester 1 | Semester 2 | Total |
|---|---|---|---|
| Minggu Efektif | 20 | 20 | 40 |
| JP per Minggu | 2 | 2 | 2 |
| **Total JP Efektif** | **40** | **40** | **80** |
| **JP untuk Pembelajaran** | **36** | **36** | **72** |
| **JP untuk PTS** | **2** | **2** | **4** |
| **JP untuk PAS/PAT** | **2** | **2** | **4** |

> **Catatan:** Berdasarkan kalender pendidikan, total JP efektif 80 JP/tahun.  
> **JP Pembelajaran per semester:** 36 JP (setara 18 minggu × 2 JP)
> **Cadangan/fleksibilitas** diambil dari JP pembelajaran jika ada hari libur tambahan.

---

## E. DISTRIBUSI JP PEMBELAJARAN

### Semester 1 (Ganjil)

| No | Elemen | Alokasi JP | Target Minggu |
|---|---|---|---|
| 1 | Pengenalan & Kontrak Belajar | 2 JP | 1 minggu |
| 2 | **BK** — Berpikir Komputasional | 8 JP | 4 minggu |
| 3 | **TIK** — Teknologi Informasi & Komunikasi | 8 JP | 4 minggu |
| 4 | **SK** — Sistem Komputer | 6 JP | 3 minggu |
| 5 | **JKI** — Jaringan Komputer & Internet | 6 JP | 3 minggu |
| 6 | Review & Pengayaan | 4 JP | 2 minggu |
| 7 | Cadangan (hari libur tak terduga) | 2 JP | 1 minggu |
| | **Total JP Pembelajaran** | **36 JP** | **18 minggu** |
| 8 | PTS (Penilaian Tengah Semester) | 2 JP | 1 minggu |
| 9 | PAS (Penilaian Akhir Semester) | 2 JP | 1 minggu |
| | **Total Semester 1** | **40 JP** | **20 minggu** |

### Semester 2 (Genap)

| No | Elemen | Alokasi JP | Target Minggu |
|---|---|---|---|
| 1 | **AD** — Analisis Data | 8 JP | 4 minggu |
| 2 | **AP** — Algoritma & Pemrograman | 14 JP | 7 minggu |
| 3 | **DSI** — Dampak Sosial Informatika | 6 JP | 3 minggu |
| 4 | **PLB** — Praktik Lintas Bidang | 6 JP | 3 minggu |
| 5 | Cadangan (hari libur tak terduga) | 2 JP | 1 minggu |
| | **Total JP Pembelajaran** | **36 JP** | **18 minggu** |
| 6 | PTS (Penilaian Tengah Semester) | 2 JP | 1 minggu |
| 7 | PAT (Penilaian Akhir Tahun) | 2 JP | 1 minggu |
| | **Total Semester 2** | **40 JP** | **20 minggu** |

---

## F. RINCIAN JP PEMBELAJARAN PER ELEMEN (TAHUNAN)

| No | Elemen | JP | Persentase |
|---|---|---|---|
| 1 | BK — Berpikir Komputasional | 8 | 11,1% |
| 2 | TIK — Teknologi Informasi & Komunikasi | 8 | 11,1% |
| 3 | SK — Sistem Komputer | 6 | 8,3% |
| 4 | JKI — Jaringan Komputer & Internet | 6 | 8,3% |
| 5 | AD — Analisis Data | 8 | 11,1% |
| 6 | AP — Algoritma & Pemrograman | 14 | 19,5% |
| 7 | DSI — Dampak Sosial Informatika | 6 | 8,3% |
| 8 | PLB — Praktik Lintas Bidang | 6 | 8,3% |
| 9 | Review, Cadangan & Pengayaan | 10 | 13,9% |
| | **Total** | **72** | **100%** |

---

Mengetahui,  
Kepala Sekolah

_________________________

Guru Mata Pelajaran,

{GURU}
NIP. {NIP}

_________________________
"""


# =========== 3. RPE ===========
def rpe():
    return f"""# RINCIAN PEKAN EFEKTIF (RPE)

**Satuan Pendidikan** : _________________________
**Mata Pelajaran** : Informatika
**Kelas / Fase** : X (Sepuluh) / Fase E
**Tahun Pelajaran** : 2026/2027
**Jumlah JP** : 2 JP per minggu

---

## SEMESTER 1 (GANJIL) — Juli s.d. Desember 2026

| Minggu ke- | Bulan | Tanggal | JP | Elemen | Materi / Kegiatan | Keterangan |
|---|---|---|---|---|---|---|
| **JULI 2026** |||||||
| 1 | Juli | 13–18 | — | — | MPLS & Libur Awal Masuk | **Tidak Efektif** |
| 2 | Juli | 20–25 | 2 | Pengenalan | Orientasi, kontrak belajar, asesmen diagnostik | Efektif |
| 3 | Juli | 27–1 | 2 | BK | Dekomposisi (TP.1.1) | Efektif |
| **AGUSTUS 2026** |||||||
| 4 | Agt | 3–8 | 2 | BK | Pengenalan Pola (TP.1.2) | Efektif |
| 5 | Agt | 10–15 | 2 | BK | Abstraksi (TP.1.3) | Efektif |
| 6 | Agt | 17–22 | 2 | BK | Perancangan Algoritma (TP.1.4) | Efektif |
| 7 | Agt | 24–29 | 2 | TIK | Pengolah kata lanjut (TP.2.1) | Efektif |
| **SEPTEMBER 2026** |||||||
| 8 | Sep | 31–5 | 2 | TIK | Spreadsheet (TP.2.2) | Efektif |
| 9 | Sep | 7–12 | 2 | TIK | Presentasi interaktif (TP.2.3) | Efektif |
| 10 | Sep | 14–19 | 2 | TIK | Integrasi aplikasi (TP.2.4) | Efektif |
| 11 | Sep | 21–26 | 2 | SK | Perangkat keras komputer (TP.3.1) | Efektif |
| **OKTOBER 2026** |||||||
| 12 | Okt | 28–3 | 2 | SK | Sistem operasi (TP.3.2) | Efektif |
| 13 | Okt | 5–10 | 2 | SK | Mekanisme internal (TP.3.3) | Efektif |
| 14 | Okt | 12–17 | 2 | JKI | Jaringan & topologi (TP.4.1) | Efektif |
| 15 | Okt | 19–24 | 2 | JKI | Konektivitas internet (TP.4.2) | Efektif |
| 16 | Okt | 26–31 | 2 | JKI | Enkripsi & keamanan (TP.4.3) | Efektif |
| **NOVEMBER 2026** |||||||
| 17 | Nov | 2–7 | 2 | Review | Review semester 1 | Efektif |
| 18 | Nov | 9–14 | 2 | Review | Proyek mini lintas elemen | Efektif |
| 19 | Nov | 16–21 | 2 | **PTS** | Penilaian Tengah Semester | **PTS** |
| 20 | Nov | 23–28 | 2 | Cadangan | Hari libur / cadangan | Efektif |
| **DESEMBER 2026** |||||||
| 21 | Des | 30–5 | 2 | **PAS** | Penilaian Akhir Semester | **PAS** |
| 22 | Des | 7–12 | — | — | Libur Semester 1 | **Tidak Efektif** |
| 23 | Des | 14–19 | — | — | Libur Semester 1 | **Tidak Efektif** |
| 24 | Des | 21–26 | — | — | Libur Semester 1 | **Tidak Efektif** |

**Rekap:** Efektif = 18 minggu + 2 minggu ujian = 20 minggu (40 JP)

---

## SEMESTER 2 (GENAP) — Januari s.d. Juni 2027

| Minggu ke- | Bulan | Tanggal | JP | Elemen | Materi / Kegiatan | Keterangan |
|---|---|---|---|---|---|---|
| **JANUARI 2027** |||||||
| 1 | Jan | 4–9 | 2 | AD | Pengantar analisis data (TP.6.1) | Efektif |
| 2 | Jan | 11–16 | 2 | AD | Privasi & keamanan data (TP.6.2) | Efektif |
| 3 | Jan | 18–23 | 2 | AD | Siklus pengolahan data (TP.6.3) | Efektif |
| 4 | Jan | 25–30 | 2 | AD | Visualisasi data (TP.6.4) | Efektif |
| **FEBRUARI 2027** |||||||
| 5 | Feb | 1–6 | 2 | AP | Notasi algoritma (TP.7.1) | Efektif |
| 6 | Feb | 8–13 | 2 | AP | Python dasar (TP.7.2) | Efektif |
| 7 | Feb | 15–20 | 2 | AP | Percabangan (TP.7.3) | Efektif |
| 8 | Feb | 22–27 | 2 | AP | Perulangan (TP.7.4) | Efektif |
| **MARET 2027** |||||||
| 9 | Mar | 1–6 | 2 | AP | Fungsi (TP.7.5) | Efektif |
| 10 | Mar | 8–13 | 2 | AP | Debugging (TP.7.6) | Efektif |
| 11 | Mar | 15–20 | 2 | AP | Proyek pemrograman (TP.7.7) | Efektif |
| 12 | Mar | 22–27 | 2 | DSI | Sejarah komputer (TP.8.1) | Efektif |
| **APRIL 2027** |||||||
| 13 | Apr | 29–3 | 2 | DSI | Lisensi & HAKI (TP.8.2) | Efektif |
| 14 | Apr | 5–10 | 2 | DSI | Dampak TIK (TP.8.3) | Efektif |
| 15 | Apr | 12–17 | 2 | PLB | Perencanaan proyek (TP.9.1) | Efektif |
| 16 | Apr | 19–24 | 2 | **PTS** | Penilaian Tengah Semester | **PTS** |
| **MEI 2027** |||||||
| 17 | Mei | 26–1 | — | — | Libur Awal Mei | **Tidak Efektif** |
| 18 | Mei | 3–8 | 2 | PLB | Implementasi proyek (TP.9.2) | Efektif |
| 19 | Mei | 10–15 | 2 | PLB | Presentasi final (TP.9.3) | Efektif |
| 20 | Mei | 17–22 | 2 | Review | Review akhir tahun | Efektif |
| 21 | Mei | 24–29 | 2 | Cadangan | Hari libur / cadangan | Efektif |
| **JUNI 2027** |||||||
| 22 | Jun | 31–5 | 2 | **PAT** | Penilaian Akhir Tahun | **PAT** |
| 23 | Jun | 7–12 | — | — | Libur Semester 2 | **Tidak Efektif** |
| 24 | Jun | 14–19 | — | — | Libur Semester 2 | **Tidak Efektif** |
| 25 | Jun | 21–26 | — | — | Libur Semester 2 | **Tidak Efektif** |

**Rekap:** Efektif = 18 minggu + 2 minggu ujian = 20 minggu (40 JP)

---

## REKAP TAHUNAN

| Semester | Minggu Efektif | JP Efektif | JP PTS | JP PAS/PAT | Total JP |
|---|---|---|---|---|---|
| Ganjil | 20 | 36 | 2 | 2 | 40 |
| Genap | 20 | 36 | 2 | 2 | 40 |
| **Total** | **40** | **72** | **4** | **4** | **80** |

---

Mengetahui,  
Kepala Sekolah

_________________________

Guru Mata Pelajaran,

{GURU}
NIP. {NIP}

_________________________
"""


# =========== 4. PROTA ===========
def prota():
    return f"""# PROGRAM TAHUNAN (PROTA)

**Satuan Pendidikan** : _________________________  
**Mata Pelajaran** : Informatika  
**Kelas / Fase** : X (Sepuluh) / Fase E  
**Tahun Pelajaran** : 2026/2027  
**Jumlah JP per Minggu** : 2 JP  

---

## A. CAPAIAN PEMBELAJARAN FASE E

Pada akhir fase E, peserta didik mampu:
1. Memahami peran sistem operasi dan mekanisme internal interaksi HW/SW/user
2. Menerapkan keamanan dalam penyambungan perangkat ke jaringan lokal dan internet
3. Mengumpulkan dan mengintegrasikan data dari berbagai sumber secara manual/otomatis
4. Memahami fitur lanjut, otomasi, serta integrasi aplikasi perkantoran
5. Menerapkan strategi algoritmik standar untuk program terstruktur dalam bahasa pemrograman prosedural tekstual
6. Bergotong royong menyelesaikan persoalan kompleks dengan mengembangkan artefak komputasional
7. Mengomunikasikan rancangan produk, produk, dan prosesnya secara lisan dan tertulis
8. Memahami sejarah perkembangan komputer, HAKI, lisensi, aspek teknis, hukum, ekonomi, lingkungan, dan sosial dari produk TIK
9. Mengenal berbagai bidang studi dan profesi terkait Informatika

---

## B. DISTRIBUSI ELEMEN PER SEMESTER

### Semester 1 (Ganjil) — 40 JP Efektif

| No | Elemen | Alokasi JP | Keterangan |
|---|---|---|---|
| 1 | Pengenalan, Kontrak Belajar & Asesmen Diagnostik | 2 JP | Menyepakati aturan, pretest awal |
| 2 | **BK** — Berpikir Komputasional | 8 JP | Dekomposisi, pengenalan pola, abstraksi, algoritma |
| 3 | **TIK** — Teknologi Informasi & Komunikasi | 8 JP | Fitur lanjut MS Office/Google Workspace, otomasi |
| 4 | **SK** — Sistem Komputer | 6 JP | Sistem operasi, HW/SW, mekanisme internal |
| 5 | **JKI** — Jaringan Komputer & Internet | 6 JP | Jaringan lokal, internet, enkripsi dasar |
| 6 | Review & Kegiatan Proyek Mini | 4 JP | Penguatan materi semester 1 |
| 7 | Cadangan | 2 JP | Hari libur tak terduga |
| 8 | PTS (Penilaian Tengah Semester) | 2 JP | Asesmen sumatif tengah semester |
| 9 | PAS (Penilaian Akhir Semester) | 2 JP | Asesmen sumatif akhir semester |
| | **Total Semester 1** | **40 JP** | |

### Semester 2 (Genap) — 40 JP Efektif

| No | Elemen | Alokasi JP | Keterangan |
|---|---|---|---|
| 1 | **AD** — Analisis Data | 8 JP | Privasi data, siklus pengolahan data, visualisasi |
| 2 | **AP** — Algoritma & Pemrograman | 14 JP | Python: sekuensial, percabangan, perulangan, fungsi |
| 3 | **DSI** — Dampak Sosial Informatika | 6 JP | Sejarah komputer, HAKI, etika digital |
| 4 | **PLB** — Praktik Lintas Bidang | 6 JP | Proyek tematik antar-elemen |
| 5 | Cadangan | 2 JP | Hari libur tak terduga |
| 6 | PTS (Penilaian Tengah Semester) | 2 JP | Asesmen sumatif tengah semester |
| 7 | PAT (Penilaian Akhir Tahun) | 2 JP | Asesmen sumatif akhir tahun |
| | **Total Semester 2** | **40 JP** | |

---

## C. JUMLAH JP TAHUNAN

| Semester | JP Pembelajaran | JP PTS | JP PAS/PAT | Total |
|---|---|---|---|---|
| Semester 1 (Ganjil) | 36 | 2 | 2 | **40** |
| Semester 2 (Genap) | 36 | 2 | 2 | **40** |
| **Total Tahunan** | **72** | **4** | **4** | **80** |

---

## D. SARANA & SUMBER BELAJAR

| Jenis | Rincian |
|---|---|
| Buku Pokok | Informatika untuk SMA/MA/SMK/MAK Kelas X (Edisi Revisi) — Kemendikdasmen |
| Buku Referensi | Buku Ajar Informatika Kelas X (Erlangga, Henry Pandia) |
| Perangkat Keras | Komputer/laptop, proyektor, jaringan internet, smartphone |
| Perangkat Lunak | Windows/Linux, MS Office/Google Workspace, Python IDLE, Replit, Google Colab, Canva, Quizizz |
| Platform | Google Classroom, Rumah Belajar, blog guru |

---

## E. 8 DIMENSI PROFIL LULUSAN YANG DIINTEGRASIKAN

| No | Dimensi | Deskripsi | Terintegrasi pada |
|---|---|---|---|
| 1 | **Keimanan & Ketakwaan** | Akhlak digital, etika bermedia sosial, kejujuran akademik | DSI, TIK, AD |
| 2 | **Kewargaan** | Cinta tanah air, kesadaran berbangsa, kontribusi sosial | DSI, PLB |
| 3 | **Penalaran Kritis** | Analisis informasi, evaluasi sumber, berpikir logis | BK, AD, AP |
| 4 | **Kreativitas** | Menghasilkan solusi & karya orisinal, inovasi | AP, PLB, TIK |
| 5 | **Kolaborasi** | Kerja sama tim, kepemimpinan, pembagian peran | PLB, AP (pair programming), JKI |
| 6 | **Kemandirian** | Regulasi diri, inisiatif belajar, manajemen proyek | BK, AP, Review |
| 7 | **Kesehatan** | Kebugaran digital, manajemen waktu layar, postur ergonomis | JKI, DSI |
| 8 | **Komunikasi** | Presentasi, dokumentasi, literasi digital, argumentasi | PLB, TIK, AP |

---

Mengetahui,  
Kepala Sekolah

_________________________

Guru Mata Pelajaran,

{GURU}
NIP. {NIP}

_________________________
"""


# =========== 5. PROSEM ===========
def prosem():
    lines = ["# PROGRAM SEMESTER (PROMES/PROSEM)\n"]
    lines.append("**Satuan Pendidikan** : _________________________  ")
    lines.append("**Mata Pelajaran** : Informatika  ")
    lines.append("**Kelas / Fase** : X (Sepuluh) / Fase E  ")
    lines.append("**Tahun Pelajaran** : 2026/2027  ")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Semester 1
    lines.append("## SEMESTER 1 (GANJIL)\n")
    lines.append("### A. Perhitungan Minggu Efektif\n")
    lines.append("| No | Bulan | Jml Minggu | Minggu Efektif | Keterangan |")
    lines.append("|---|---|---|---|---|")
    s1_bulan = [("Juli 2026", 4, 3, "MPLS & awal masuk"), ("Agustus 2026", 4, 4, "Efektif"), ("September 2026", 4, 4, "Efektif"), ("Oktober 2026", 4, 4, "Efektif"), ("November 2026", 4, 3, "PTS minggu terakhir"), ("Desember 2026", 4, 2, "PAS & libur")]
    total_jml_s1 = 0; total_efektif_s1 = 0
    for i, (bln, jml, efektif, ket) in enumerate(s1_bulan, 1):
        lines.append(f"| {i} | {bln} | {jml} | {efektif} | {ket} |")
        total_jml_s1 += jml; total_efektif_s1 += efektif
    lines.append(f"| | **Jumlah** | **{total_jml_s1}** | **{total_efektif_s1}** | |")

    lines.append("\n### B. Jadwal Pembelajaran Semester 1\n")
    lines.append("| Pertemuan | Minggu Ke- | JP | Elemen | Materi Pokok | Tujuan Pembelajaran (TP) | Sumber |")
    lines.append("|---|---|---|---|---|---|---|")
    s1_jadwal = [
        (1, 1, 2, "Pengenalan", "Orientasi pembelajaran Informatika, kontrak belajar, asesmen diagnostik", "TP.0.1: Menjelaskan tujuan & ruang lingkup Informatika kelas 10\n| | | | | | TP.0.2: Menyepakati aturan KBM, norma digital, penggunaan perangkat", "Buku Bab 1"),
        (2, 2, 2, "**BK**", "Dekomposisi: memecah masalah kompleks menjadi bagian kecil", "TP.1.1: Mendekomposisi masalah sehari-hari menjadi sub-masalah", "Buku Bab 2"),
        (3, 3, 2, "**BK**", "Pengenalan Pola (Pattern Recognition)", "TP.1.2: Mengidentifikasi pola dari sekumpulan data/masalah", ""),
        (4, 4, 2, "**BK**", "Abstraksi: memilah informasi esensial & non-esensial", "TP.1.3: Melakukan abstraksi terhadap masalah untuk fokus pada informasi penting", ""),
        (5, 5, 2, "**BK**", "Perancangan Algoritma & penyelesaian masalah", "TP.1.4: Menyusun algoritma solusi dengan pseudocode/flowchart", ""),
        (6, 6, 2, "**TIK**", "Aplikasi perkantoran: fitur lanjut pengolah kata (mail merge, referensi, template)", "TP.2.1: Menggunakan fitur lanjut pengolah kata untuk dokumentasi", "Buku Bab 3"),
        (7, 7, 2, "**TIK**", "Aplikasi pengolah angka: formula, fungsi, grafik, pivot table", "TP.2.2: Mengolah data menggunakan formula dan fungsi pada spreadsheet", ""),
        (8, 8, 2, "**TIK**", "Aplikasi presentasi: desain, animasi, hyperlink, kolaborasi", "TP.2.3: Membuat presentasi interaktif dengan fitur lanjut", ""),
        (9, 9, 2, "**TIK**", "Otomasi aplikasi perkantoran: integrasi antar-aplikasi", "TP.2.4: Mengintegrasikan data antar aplikasi perkantoran", ""),
        (10, 10, 2, "**SK**", "Perangkat keras komputer: komponen, fungsi, cara kerja", "TP.3.1: Mengidentifikasi komponen HW dan fungsinya", "Buku Bab 4"),
        (11, 11, 2, "**SK**", "Perangkat lunak: sistem operasi, aplikasi, mekanisme internal", "TP.3.2: Menjelaskan peran OS dalam interaksi HW-SW-user", ""),
        (12, 12, 2, "**SK**", "Interaksi HW-SW-user: booting, driver, sistem file", "TP.3.3: Menganalisis mekanisme internal sistem komputer", ""),
        (13, 13, 2, "**JKI**", "Jaringan komputer: LAN, topologi, perangkat jaringan", "TP.4.1: Menjelaskan jenis & topologi jaringan komputer", "Buku Bab 5"),
        (14, 14, 2, "**JKI**", "Internet: protokol, IP address, DNS, konektivitas", "TP.4.2: Menerapkan konfigurasi konektivitas internet", ""),
        (15, 15, 2, "**JKI**", "Keamanan jaringan: enkripsi dasar, proteksi data, firewall", "TP.4.3: Menerapkan enkripsi sederhana & proteksi data saat online", ""),
        (16, 16, 2, "**Review**", "Review & pengayaan materi semester 1", "TP.5.1: Mereview seluruh materi semester 1", ""),
        (17, 17, 2, "**Review**", "Proyek mini lintas elemen (BK+TIK+SK+JKI)", "TP.5.2: Menyajikan solusi berbasis Informatika untuk kasus nyata", ""),
        (18, 18, 2, "Cadangan", "Hari libur/cadangan", "\u2014", ""),
        (19, 19, 2, "**PTS**", "Penilaian Tengah Semester", "\u2014", ""),
        (20, 20, 2, "**PAS**", "Penilaian Akhir Semester", "\u2014", ""),
    ]
    for pert, minggu, jp, elemen, materi, tp, sumber in s1_jadwal:
        lines.append(f"| {pert} | {minggu} | {jp} | {elemen} | {materi} | {tp} | {sumber} |")

    lines.append(""); lines.append("---"); lines.append("")

    # Semester 2
    lines.append("## SEMESTER 2 (GENAP)\n")
    lines.append("### A. Perhitungan Minggu Efektif\n")
    lines.append("| No | Bulan | Jml Minggu | Minggu Efektif | Keterangan |")
    lines.append("|---|---|---|---|---|")
    s2_bulan = [("Januari 2027", 4, 4, "Awal semester"), ("Februari 2027", 4, 4, "Efektif"), ("Maret 2027", 4, 4, "Efektif"), ("April 2027", 4, 3, "PTS minggu terakhir"), ("Mei 2027", 4, 3, "Efektif"), ("Juni 2027", 4, 2, "PAT & libur")]
    total_jml_s2 = 0; total_efektif_s2 = 0
    for i, (bln, jml, efektif, ket) in enumerate(s2_bulan, 1):
        lines.append(f"| {i} | {bln} | {jml} | {efektif} | {ket} |")
        total_jml_s2 += jml; total_efektif_s2 += efektif
    lines.append(f"| | **Jumlah** | **{total_jml_s2}** | **{total_efektif_s2}** | |")

    lines.append("\n### B. Jadwal Pembelajaran Semester 2\n")
    lines.append("| Pertemuan | Minggu Ke- | JP | Elemen | Materi Pokok | Tujuan Pembelajaran (TP) | Sumber |")
    lines.append("|---|---|---|---|---|---|---|")
    s2_jadwal = [
        (1, 1, 2, "**AD**", "Pengantar Analisis Data: data, informasi, pengetahuan", "TP.6.1: Membedakan data, informasi, dan pengetahuan", "Buku Bab 6"),
        (2, 2, 2, "**AD**", "Privasi & keamanan data: aspek hukum, etika pengelolaan data", "TP.6.2: Menganalisis aspek privasi & keamanan data pribadi", ""),
        (3, 3, 2, "**AD**", "Siklus pengolahan data: pengumpulan, pembersihan, transformasi", "TP.6.3: Menerapkan siklus pengolahan data dari berbagai sumber", ""),
        (4, 4, 2, "**AD**", "Visualisasi & interpretasi data: grafik, dashboard, insight", "TP.6.4: Menyajikan visualisasi data dan menarik kesimpulan", ""),
        (5, 5, 2, "**AP**", "Pengantar Algoritma & Pemrograman: notasi algoritma", "TP.7.1: Menulis pseudocode & flowchart untuk solusi masalah", "Buku Bab 7"),
        (6, 6, 2, "**AP**", "Pengenalan Python: variabel, tipe data, input/output", "TP.7.2: Menggunakan variabel, tipe data, I/O dalam Python", ""),
        (7, 7, 2, "**AP**", "Struktur sekuensial & percabangan (if/else, nested if)", "TP.7.3: Menerapkan struktur sekuensial dan percabangan dalam program", ""),
        (8, 8, 2, "**AP**", "Struktur perulangan (for, while, nested loop)", "TP.7.4: Menerapkan perulangan untuk pemrosesan data berulang", ""),
        (9, 9, 2, "**AP**", "Fungsi & modularisasi program", "TP.7.5: Membuat fungsi untuk program modular", ""),
        (10, 10, 2, "**AP**", "Praktik debugging: tracing, breakpoint, error handling", "TP.7.6: Melakukan debugging dan menangani error pada program", ""),
        (11, 11, 2, "**AP**", "Proyek pemrograman individual: program terstruktur", "TP.7.7: Mengembangkan program Python terstruktur sebagai solusi masalah", ""),
        (12, 12, 2, "**DSI**", "Sejarah perkembangan komputer & tokoh-tokohnya", "TP.8.1: Menjelaskan sejarah komputer & kontribusi tokoh penting", "Buku Bab 8"),
        (13, 13, 2, "**DSI**", "HAKI, lisensi perangkat lunak, dan etika digital", "TP.8.2: Membedakan jenis lisensi software dan HAKI", ""),
        (14, 14, 2, "**DSI**", "Dampak TIK: aspek ekonomi, sosial, lingkungan, profesi IT", "TP.8.3: Menganalisis dampak positif & negatif TIK di berbagai bidang", ""),
        (15, 15, 2, "**PLB**", "Identifikasi masalah & perencanaan proyek", "TP.9.1: Mengidentifikasi persoalan nyata & merencanakan solusi komputasional", "Buku Bab 9"),
        (16, 16, 2, "**PLB**", "Implementasi & pengujian proyek", "TP.9.2: Mengimplementasikan & menguji artefak komputasional", ""),
        (17, 17, 2, "**PLB**", "Presentasi & refleksi proyek", "TP.9.3: Mempresentasikan produk & proses pengembangan", ""),
        (18, 18, 2, "Cadangan", "Hari libur/cadangan", "\u2014", ""),
        (19, 19, 2, "**PTS**", "Penilaian Tengah Semester", "\u2014", ""),
        (20, 20, 2, "**PAT**", "Penilaian Akhir Tahun", "\u2014", ""),
    ]
    for pert, minggu, jp, elemen, materi, tp, sumber in s2_jadwal:
        lines.append(f"| {pert} | {minggu} | {jp} | {elemen} | {materi} | {tp} | {sumber} |")

    lines.append(""); lines.append("---"); lines.append("")

    # Rekap JP
    lines.append("## C. REKAPITULASI JP PER ELEMEN (TAHUNAN)\n")
    lines.append("| Elemen | JP | Persentase |")
    lines.append("|---|---|---|")
    for e, j, p in [("Pengenalan & Kontrak Belajar", "2 JP", "2,5%"), ("BK \u2014 Berpikir Komputasional", "8 JP", "10%"), ("TIK \u2014 Teknologi Informasi & Komunikasi", "8 JP", "10%"), ("SK \u2014 Sistem Komputer", "6 JP", "7,5%"), ("JKI \u2014 Jaringan Komputer & Internet", "6 JP", "7,5%"), ("Review & Pengayaan", "4 JP", "5%"), ("AD \u2014 Analisis Data", "8 JP", "10%"), ("AP \u2014 Algoritma & Pemrograman", "14 JP", "17,5%"), ("DSI \u2014 Dampak Sosial Informatika", "6 JP", "7,5%"), ("PLB \u2014 Praktik Lintas Bidang", "6 JP", "7,5%"), ("Cadangan", "4 JP", "5%"), ("PTS + PAS/PAT", "8 JP", "10%"), ("**Total**", "**80 JP**", "**100%**")]:
        lines.append(f"| {e} | {j} | {p} |")

    lines.append(""); lines.append("---"); lines.append("")
    lines.append("Mengetahui,  "); lines.append("Kepala Sekolah"); lines.append(""); lines.append("_________________________"); lines.append(""); lines.append("Guru Mata Pelajaran,"); lines.append(""); lines.append(f"{GURU}"); lines.append(f"NIP. {NIP}"); lines.append(""); lines.append("_________________________")
    return "\n".join(lines) + "\n"


# =========== 6. ATP ===========
def atp():
    lines = [f"# ALUR TUJUAN PEMBELAJARAN (ATP)\n"]
    lines.append("**Satuan Pendidikan** : _________________________")
    lines.append("**Mata Pelajaran** : Informatika")
    lines.append("**Kelas / Fase** : X (Sepuluh) / Fase E")
    lines.append("**Tahun Pelajaran** : 2026/2027")
    lines.append("**Jumlah JP** : 2 JP per minggu")
    lines.append(""); lines.append("---"); lines.append("")
    lines.append("## FORMAT 10 KOLOM\n")

    for elem in ELEMEN_DATA:
        e_sing = elem["singkatan"]; e_nama = elem["nama"]; e_jp = elem["jp"]
        cp_label = f"Elemen: {e_sing} \u2014 " if e_sing else ""
        lines.append(f"### {cp_label}{e_nama} ({e_jp} JP)\n")
        lines.append("| No TP | Elemen CP | Capaian Pembelajaran | Tujuan Pembelajaran | Indikator Keberhasilan | Materi Pokok | Kegiatan Pembelajaran | Dimensi Profil Lulusan | Alokasi Waktu | Sumber Belajar |")
        lines.append("|---|---|---|---|---|---|---|---|---|---|")
        for tp in elem["tp_list"]:
            kode = tp["kode"]
            cp_cell = elem["cp_teks"] if e_sing else "\u2014"
            cp_elemen_cell = e_sing if e_sing else "\u2014"
            alokasi = "2 JP" if kode != "0.1" and kode != "0.2" else "1 JP"
            if kode == "0.2": alokasi = "1 JP"
            lines.append(f"| TP.{kode} | {cp_elemen_cell} | {cp_cell} | {tp['judul']} | {tp['indikator']} | {tp['materi']} | {tp['kegiatan']} | {tp['dimensi']} | {alokasi} | {tp['sumber']} |")
        lines.append("")

    lines.append("---"); lines.append(""); lines.append("## GLOSARIUM\n")
    lines.append("| Istilah | Arti |"); lines.append("|---|---|")
    for ist, arti in [("BK", "Berpikir Komputasional"), ("TIK", "Teknologi Informasi & Komunikasi"), ("SK", "Sistem Komputer"), ("JKI", "Jaringan Komputer & Internet"), ("AD", "Analisis Data"), ("AP", "Algoritma & Pemrograman"), ("DSI", "Dampak Sosial Informatika"), ("PLB", "Praktik Lintas Bidang"), ("TP", "Tujuan Pembelajaran"), ("CP", "Capaian Pembelajaran"), ("JP", "Jam Pelajaran (45 menit)")]:
        lines.append(f"| {ist} | {arti} |")
    lines.append(""); lines.append("---"); lines.append("")
    lines.append("Mengetahui,  "); lines.append("Kepala Sekolah"); lines.append(""); lines.append("_________________________"); lines.append(""); lines.append("Guru Mata Pelajaran,"); lines.append(""); lines.append(f"{GURU}"); lines.append(f"NIP. {NIP}"); lines.append(""); lines.append("_________________________")
    return "\n".join(lines) + "\n"


# =========== 7. KKTP ===========
def kktp():
    lines = [f"# KRITERIA KETERCAPAIAN TUJUAN PEMBELAJARAN (KKTP)\n"]
    lines.append("**Satuan Pendidikan** : _________________________")
    lines.append("**Mata Pelajaran** : Informatika")
    lines.append("**Kelas / Fase** : X (Sepuluh) / Fase E")
    lines.append("**Tahun Pelajaran** : 2026/2027")
    lines.append(""); lines.append("---"); lines.append("")
    lines.append("## A. PENGERTIAN\n")
    lines.append("KKTP (Kriteria Ketercapaian Tujuan Pembelajaran) adalah rubrik yang digunakan untuk menentukan apakah peserta didik telah mencapai tujuan pembelajaran yang ditetapkan. KKTP bersifat fleksibel dan dapat disesuaikan dengan karakteristik mata pelajaran dan peserta didik.")
    lines.append(""); lines.append("---"); lines.append("")
    lines.append("## B. TEKNIK PENENTUAN KKTP\n")
    lines.append("Pendekatan yang digunakan: **Interval Nilai** dengan deskripsi kualitatif.\n")
    lines.append("| Interval Nilai | Predikat | Deskripsi |")
    lines.append("|---|---|---|")
    lines.append("| 90 \u2013 100 | **Sangat Baik (SB)** | Peserta didik menguasai TP secara mendalam, mampu menerapkan dalam konteks baru, dan menunjukkan kreativitas |")
    lines.append("| 75 \u2013 89 | **Baik (B)** | Peserta didik menguasai seluruh indikator TP dengan mandiri |")
    lines.append("| 60 \u2013 74 | **Cukup (C)** | Peserta didik menguasai sebagian besar indikator TP, masih perlu bimbingan pada beberapa aspek |")
    lines.append("| < 60 | **Perlu Bimbingan (PB)** | Peserta didik belum mencapai indikator TP secara memadai, perlu intervensi remedial |")
    lines.append(""); lines.append("---"); lines.append("")
    lines.append("## C. KKTP PER ELEMEN\n")

    for elem in ELEMEN_DATA:
        e_sing = elem["singkatan"]; e_nama = elem["nama"]
        label = f"### Elemen {e_sing} \u2014 {e_nama}\n" if e_sing else f"### {e_nama}\n"
        lines.append(label)
        lines.append("| Kode TP | Tujuan Pembelajaran | KKTP (\u226575) | Indikator Ketercapaian |")
        lines.append("|---|---|---|---|")
        for tp in elem["tp_list"]:
            ceklist = " \u25a1 ".join([""] + tp["kktp_indikator"])
            lines.append(f"| TP.{tp['kode']} | {tp['judul']} | {tp['indikator']} |{ceklist} |")
        lines.append("")

    lines.append("---"); lines.append("")
    lines.append("## D. KKTP KOMPOSIT PER ELEMEN\n")
    lines.append("| Elemen | Rata-rata KKTP | Predikat Kualitatif |"); lines.append("|---|---|---|")
    for elem in ELEMEN_DATA:
        label = f"{elem['singkatan']} \u2014 {elem['nama']}" if elem['singkatan'] else elem['nama']
        lines.append(f"| {label} | | |")
    lines.append(""); lines.append("---"); lines.append("")
    lines.append("## E. KONVERSI NILAI KE RAPOR KURIKULUM MERDEKA\n")
    lines.append("| Interval Nilai | Predikat | Deskripsi |"); lines.append("|---|---|---|")
    lines.append("| 90 \u2013 100 | SB (Sangat Baik) | Peserta didik sangat kompeten |")
    lines.append("| 75 \u2013 89 | B (Baik) | Peserta didik kompeten |")
    lines.append("| 60 \u2013 74 | C (Cukup) | Peserta didik cukup kompeten |")
    lines.append("| < 60 | PB (Perlu Bimbingan) | Peserta didik belum kompeten |")
    lines.append(""); lines.append("---"); lines.append("")
    lines.append("## F. TINDAK LANJUT HASIL KKTP\n")
    lines.append("| Predikat | Tindak Lanjut |"); lines.append("|---|---|")
    lines.append("| Sangat Baik | Pengayaan: eksplorasi mandiri, proyek tingkat lanjut, tutor sebaya |")
    lines.append("| Baik | Lanjut ke TP berikutnya |")
    lines.append("| Cukup | Bimbingan terfokus pada indikator yang belum tercapai |")
    lines.append("| Perlu Bimbingan | Remedial: pembelajaran ulang dengan metode berbeda, peer tutoring, tugas tambahan |")
    lines.append(""); lines.append("---"); lines.append("")
    lines.append("Mengetahui,  "); lines.append("Kepala Sekolah"); lines.append(""); lines.append("_________________________"); lines.append(""); lines.append("Guru Mata Pelajaran,"); lines.append(""); lines.append(f"{GURU}"); lines.append(f"NIP. {NIP}"); lines.append(""); lines.append("_________________________")
    return "\n".join(lines) + "\n"


# =========== 8. PEMETAAN ===========
def pemetaan():
    return f"""# PEMETAAN KOMPETENSI & TEKNIK PENILAIAN

**Satuan Pendidikan** : _________________________
**Mata Pelajaran** : Informatika
**Kelas / Fase** : X (Sepuluh) / Fase E
**Tahun Pelajaran** : 2026/2027

---

## A. JENIS ASESMEN

| Jenis Asesmen | Waktu | Fungsi |
|---|---|---|
| **Asesmen Diagnostik** | Awal pembelajaran (sebelum materi) | Mengetahui kemampuan awal & kebutuhan belajar siswa |
| **Asesmen Formatif** | Selama proses pembelajaran | Memantau perkembangan belajar, memberikan umpan balik |
| **Asesmen Sumatif** | Akhir lingkup materi/semester | Mengukur pencapaian hasil belajar di akhir periode |

---

## B. PEMETAAN PER ELEMEN

### SEMESTER 1 (Ganjil)

| Elemen | TP | Teknik Asesmen | Instrumen | Bobot | Waktu |
|---|---|---|---|---|---|
| **BK** \u2014 Berpikir Komputasional | TP.1.1 s.d TP.1.4 | | | | |
| | | Formatif: Observasi, Tes Tulis | LKPD, Soal uraian dekomposisi, Soal pola | 25% | Setiap pertemuan |
| | | Sumatif: Praktik, Projek | Rubrik solusi berpikir komputasional | 25% | Akhir elemen |
| **TIK** \u2014 Teknologi Informasi & Komunikasi | TP.2.1 s.d TP.2.4 | | | | |
| | | Formatif: Praktik | Ceklist hasil dokumen/spreadsheet/presentasi | 25% | Setiap pertemuan |
| | | Sumatif: Produk | Rubrik proyek integrasi aplikasi perkantoran | 25% | Akhir elemen |
| **SK** \u2014 Sistem Komputer | TP.3.1 s.d TP.3.3 | | | | |
| | | Formatif: Tes Tulis, Observasi | Soal pilihan ganda & uraian, LKPD identifikasi HW | 25% | Setiap pertemuan |
| | | Sumatif: Tes Tulis, Praktik | Soal uraian mekanisme sistem, simulasi booting | 25% | Akhir elemen |
| **JKI** \u2014 Jaringan Komputer & Internet | TP.4.1 s.d TP.4.3 | | | | |
| | | Formatif: Praktik, Observasi | Ceklist konfigurasi jaringan, LKPD enkripsi | 25% | Setiap pertemuan |
| | | Sumatif: Praktik | Rubrik simulasi jaringan & enkripsi | 25% | Akhir elemen |

### SEMESTER 2 (Genap)

| Elemen | TP | Teknik Asesmen | Instrumen | Bobot | Waktu |
|---|---|---|---|---|---|
| **AD** \u2014 Analisis Data | TP.6.1 s.d TP.6.4 | | | | |
| | | Formatif: Tes Tulis, Praktik | Soal analisis data, LKPD pengolahan data | 25% | Setiap pertemuan |
| | | Sumatif: Produk | Rubrik dashboard & laporan analisis data | 25% | Akhir elemen |
| **AP** \u2014 Algoritma & Pemrograman | TP.7.1 s.d TP.7.7 | | | | |
| | | Formatif: Praktik, Observasi | Rubrik coding Python, ceklist debugging | 25% | Setiap pertemuan |
| | | Sumatif: Produk, Projek | Rubrik program Python & dokumentasi | 25% | Akhir elemen |
| **DSI** \u2014 Dampak Sosial Informatika | TP.8.1 s.d TP.8.3 | | | | |
| | | Formatif: Tes Tulis, Diskusi | Soal uraian, rubrik partisipasi diskusi | 25% | Setiap pertemuan |
| | | Sumatif: Esai, Presentasi | Rubrik esai analisis dampak TIK | 25% | Akhir elemen |
| **PLB** \u2014 Praktik Lintas Bidang | TP.9.1 s.d TP.9.3 | | | | |
| | | Formatif: Observasi | Rubrik kerja sama tim, catatan kemajuan | 25% | Setiap pertemuan |
| | | Sumatif: Projek | Rubrik produk, dokumentasi, & presentasi | 25% | Akhir elemen |

---

## C. KISI-KISI PENILAIAN PER ELEMEN

### Elemen BK \u2014 Berpikir Komputasional

| Indikator Soal | Level Kognitif | Bentuk Soal | Jumlah Soal |
|---|---|---|---|
| Memecah masalah menjadi sub-masalah | C4 (Menganalisis) | Uraian | 2 |
| Mengidentifikasi pola dari data | C4 (Menganalisis) | Uraian/PG | 3 |
| Melakukan abstraksi | C4 (Menganalisis) | Uraian | 1 |
| Menyusun algoritma solusi | C6 (Mencipta) | Praktik/Flowchart | 1 |

### Elemen TIK \u2014 Teknologi Informasi & Komunikasi

| Indikator Soal | Level Kognitif | Bentuk Soal | Jumlah Soal |
|---|---|---|---|
| Menggunakan fitur lanjut pengolah kata | C3 (Mengaplikasi) | Praktik | 1 |
| Mengolah data dengan spreadsheet | C3 (Mengaplikasi) | Praktik | 1 |
| Membuat presentasi interaktif | C3 (Mengaplikasi) | Praktik | 1 |
| Mengintegrasikan aplikasi | C4 (Menganalisis) | Praktik/Produk | 1 |

### Elemen SK \u2014 Sistem Komputer

| Indikator Soal | Level Kognitif | Bentuk Soal | Jumlah Soal |
|---|---|---|---|
| Mengidentifikasi komponen HW | C2 (Memahami) | PG | 5 |
| Menjelaskan peran OS | C2 (Memahami) | Uraian | 2 |
| Menganalisis mekanisme internal | C4 (Menganalisis) | Uraian | 2 |

### Elemen JKI \u2014 Jaringan Komputer & Internet

| Indikator Soal | Level Kognitif | Bentuk Soal | Jumlah Soal |
|---|---|---|---|
| Menjelaskan topologi & perangkat | C2 (Memahami) | PG/Uraian | 3 |
| Konfigurasi konektivitas | C3 (Mengaplikasi) | Praktik | 1 |
| Menerapkan enkripsi & proteksi | C3 (Mengaplikasi) | Praktik | 1 |

### Elemen AD \u2014 Analisis Data

| Indikator Soal | Level Kognitif | Bentuk Soal | Jumlah Soal |
|---|---|---|---|
| Membedakan data, informasi, pengetahuan | C2 (Memahami) | PG | 3 |
| Menganalisis privasi & keamanan data | C4 (Menganalisis) | Uraian | 2 |
| Menerapkan siklus pengolahan data | C3 (Mengaplikasi) | Praktik | 1 |
| Visualisasi & interpretasi | C4 (Menganalisis) | Produk | 1 |

### Elemen AP \u2014 Algoritma & Pemrograman

| Indikator Soal | Level Kognitif | Bentuk Soal | Jumlah Soal |
|---|---|---|---|
| Menulis pseudocode/flowchart | C3 (Mengaplikasi) | Uraian | 2 |
| Program dengan variabel, I/O | C3 (Mengaplikasi) | Praktik | 1 |
| Program dengan percabangan | C3 (Mengaplikasi) | Praktik | 1 |
| Program dengan perulangan | C3 (Mengaplikasi) | Praktik | 1 |
| Membuat fungsi | C3 (Mengaplikasi) | Praktik | 1 |
| Debugging | C4 (Menganalisis) | Praktik | 1 |
| Proyek program | C6 (Mencipta) | Produk | 1 |

### Elemen DSI \u2014 Dampak Sosial Informatika

| Indikator Soal | Level Kognitif | Bentuk Soal | Jumlah Soal |
|---|---|---|---|
| Menjelaskan sejarah komputer | C1 (Mengingat) | PG | 3 |
| Membedakan lisensi software | C2 (Memahami) | PG/Uraian | 2 |
| Menganalisis dampak TIK | C4 (Menganalisis) | Esai | 1 |

### Elemen PLB \u2014 Praktik Lintas Bidang

| Indikator Soal | Level Kognitif | Bentuk Soal | Jumlah Soal |
|---|---|---|---|
| Menyusun proposal proyek | C6 (Mencipta) | Produk | 1 |
| Mengimplementasikan solusi | C6 (Mencipta) | Produk | 1 |
| Mempresentasikan hasil | C2 (Memahami) | Presentasi | 1 |

---

## D. PERSENTASE BOBOT PENILAIAN

| Komponen | Bobot | Keterangan |
|---|---|---|
| **Formatif** | 60% | Observasi, LKPD, praktik harian, kuis |
| **Sumatif Lingkup Materi** | 20% | Akhir setiap elemen/bab |
| **Sumatif Semester (PTS/PAT)** | 20% | PTS (10%) + PAS/PAT (10%) |
| **Total** | **100%** | |

---

## E. RUBRIK PENILAIAN 8 DIMENSI PROFIL LULUSAN

| Dimensi | Kriteria | SB (4) | B (3) | C (2) | PB (1) |
|---|---|---|---|---|---|
| **Kolaborasi** (sebelumnya: Gotong Royong) | Kolaborasi dalam kerja kelompok | Aktif berkontribusi & memfasilitasi | Berkontribusi aktif | Terlibat pasif | Tidak terlibat |
| **Kemandirian** (sebelumnya: Mandiri) | Inisiatif & tanggung jawab belajar | Mandiri penuh & inisiatif | Mandiri dengan sedikit arahan | Perlu diarahkan | Sangat tergantung |
| **Penalaran Kritis** (sebelumnya: Bernalar Kritis) | Kualitas analisis & argumen | Analisis mendalam, argumen logis | Analisis baik, cukup logis | Analisis dangkal | Tidak menganalisis |
| **Kreativitas** (sebelumnya: Kreatif) | Orisinalitas karya/solusi | Karya orisinal & inovatif | Karya orisinal | Karya modifikasi | Karya meniru |
| **Keimanan & Ketakwaan** (sebelumnya: Beriman) | Etika digital & tanggung jawab | Sangat etis & bertanggung jawab | Etis & bertanggung jawab | Cukup etis | Perlu bimbingan |
| **Kewargaan** | Kesadaran berbangsa & berkontribusi | Aktif berkontribusi untuk komunitas | Peduli lingkungan | Cukup peduli | Kurang peduli |
| **Kesehatan** | Kebugaran & manajemen diri | Menjaga postur, mengatur waktu layar | Cukup menjaga | Kurang menjaga | Tidak menjaga |
| **Komunikasi** | Penyampaian gagasan | Sangat jelas, terstruktur, meyakinkan | Jelas & terstruktur | Cukup jelas | Tidak jelas |

---

Mengetahui,  
Kepala Sekolah

_________________________

Guru Mata Pelajaran,

{GURU}
NIP. {NIP}

_________________________
"""


# =========== 9. BANK SOAL ===========
def bank_soal():
    return f"""# BANK SOAL INFORMATIKA KELAS X

**Satuan Pendidikan** : _________________________
**Mata Pelajaran** : Informatika
**Kelas / Fase** : X (Sepuluh) / Fase E
**Tahun Pelajaran** : 2026/2027

---

## A. ASESMEN DIAGNOSTIK (AWAL TAHUN)

### A.1 Soal Diagnostik \u2014 15 Menit

| No | Soal | Jawaban Singkat |
|---|---|---|
| 1 | Apa yang dimaksud dengan komputer? | |
| 2 | Sebutkan 3 perangkat keras komputer yang kamu ketahui! | |
| 3 | Apa fungsi dari sistem operasi? | |
| 4 | Apakah kamu pernah membuat program? Jika ya, bahasa apa? | |
| 5 | Apa itu internet? | |
| 6 | Sebutkan 1 aplikasi perkantoran yang kamu kuasai! | |
| 7 | Apa yang kamu ketahui tentang data? | |
| 8 | Apakah kamu punya media sosial? Bagaimana cara menjaga privasi di sana? | |
| 9 | Sebutkan 1 profesi di bidang IT yang kamu tahu! | |
| 10 | Dari skala 1\u201310, seberapa tertarik kamu dengan Informatika? | |

---

## B. SOAL FORMATIF PER ELEMEN

### B.1 Elemen BK \u2014 Berpikir Komputasional

#### Soal PG (Pilihan Ganda)

| No | Soal | A | B | C | D | E | Kunci |
|---|---|---|---|---|---|---|---|
| 1 | Memecah masalah kompleks menjadi bagian-bagian kecil disebut dengan... | Abstraksi | **Dekomposisi** | Pengenalan pola | Algoritma | Evaluasi | **B** |
| 2 | Dalam berpikir komputasional, menemukan kesamaan dari data disebut... | Dekomposisi | Abstraksi | **Pengenalan pola** | Algoritma | Refleksi | **C** |
| 3 | Contoh dekomposisi yang tepat adalah... | Membaca buku | **Memecah proyek besar menjadi tugas-tugas kecil** | Menulis kode | Menggambar diagram | Mendengarkan musik | **B** |
| 4 | Abstraksi dalam berpikir komputasional berarti... | Memperumit masalah | **Mengabaikan detail yang tidak relevan** | Menambah data | Membuang semua informasi | Mengulang pola | **B** |
| 5 | Manakah yang BUKAN merupakan fondasi berpikir komputasional? | Dekomposisi | Pengenalan pola | **Deduksi** | Abstraksi | Algoritma | **C** |

#### Soal Uraian

| No | Soal | Skor Maks |
|---|---|---|
| 1 | Jelaskan perbedaan dekomposisi dan abstraksi! Berikan contoh masing-masing! | 20 |
| 2 | Buatlah flowchart untuk masalah: "Menentukan apakah suatu bilangan genap atau ganjil" | 20 |
| 3 | Diberikan data: 2, 4, 6, 8, 10, 12, ..., _. Tentukan pola dan 2 angka berikutnya! | 15 |
| 4 | Seorang siswa ingin merencanakan acara ulang tahun. Bantu dia dengan melakukan dekomposisi masalah tersebut minimal 4 sub-masalah dan 12 detail kegiatan! | 25 |

#### Soal Praktik

| No | Soal | Alat |
|---|---|---|
| 1 | Buatlah diagram pohon dekomposisi untuk masalah "Membangun aplikasi mobile sederhana" | Kertas/karton/spidol |

---

### B.2 Elemen TIK \u2014 Teknologi Informasi & Komunikasi

#### Soal PG

| No | Soal | A | B | C | D | E | Kunci |
|---|---|---|---|---|---|---|---|
| 1 | Fungsi pada spreadsheet untuk menjumlahkan data adalah... | AVERAGE | COUNT | **SUM** | MAX | IF | **C** |
| 2 | Dalam Microsoft Word, fitur untuk membuat surat massal dengan data dari Excel disebut... | Referensi | **Mail Merge** | Table | Macro | Template | **B** |
| 3 | Shortcut untuk menyimpan file di sebagian besar aplikasi perkantoran adalah... | Ctrl+P | Ctrl+C | **Ctrl+S** | Ctrl+V | Ctrl+X | **C** |
| 4 | Fungsi IF pada spreadsheet digunakan untuk... | Menjumlah data | **Membuat keputusan logis** | Mencari data | Membuat grafik | Mengurutkan data | **B** |
| 5 | Untuk membuat daftar isi otomatis di Word, kita harus menggunakan... | Tabel | **Heading styles** | Page break | Footer | Comment | **B** |

#### Soal Uraian

| No | Soal | Skor Maks |
|---|---|---|
| 1 | Jelaskan langkah-langkah membuat mail merge di Microsoft Word! | 20 |
| 2 | Apa perbedaan fungsi VLOOKUP dan INDEX-MATCH? Kapan masing-masing digunakan? | 20 |
| 3 | Sebutkan 3 jenis grafik pada spreadsheet dan kapan tepat menggunakannya! | 15 |

#### Soal Praktik

| No | Soal | Alat |
|---|---|---|
| 1 | Buat dokumen undangan rapat dengan mail merge untuk 5 orang! | MS Word/Google Docs |
| 2 | Buat spreadsheet: data 10 siswa (nama, nilai UTS, nilai UAS, rata-rata, grade) lengkap dengan grafik! | MS Excel/Google Sheets |

---

### B.3 Elemen SK \u2014 Sistem Komputer

#### Soal PG

| No | Soal | A | B | C | D | E | Kunci |
|---|---|---|---|---|---|---|---|
| 1 | Bagian komputer yang berfungsi sebagai "otak" pemrosesan data adalah... | RAM | **CPU** | Harddisk | Motherboard | GPU | **B** |
| 2 | Fungsi dari RAM adalah... | Menyimpan data permanen | **Menyimpan data sementara** | Memproses grafik | Mengatur daya | Menghubungkan komponen | **B** |
| 3 | Contoh sistem operasi adalah... | Microsoft Word | **Linux** | Google Chrome | Python | Adobe Photoshop | **B** |
| 4 | Urutan booting yang benar adalah... | OS \u2192 BIOS \u2192 POST | POST \u2192 BIOS \u2192 OS | **BIOS \u2192 POST \u2192 OS** | OS \u2192 POST \u2192 BIOS | POST \u2192 OS \u2192 BIOS | **C** |
| 5 | Driver pada komputer berfungsi untuk... | Mempercepat internet | **Menghubungkan OS dengan HW** | Membersihkan file | Menambah memori | Mengatur password | **B** |

#### Soal Uraian

| No | Soal | Skor Maks |
|---|---|---|
| 1 | Gambarkan dan jelaskan arsitektur interaksi HW-SW-user dalam sistem komputer! | 20 |
| 2 | Jelaskan perbedaan antara HDD dan SSD dari segi cara kerja, kecepatan, dan ketahanan! | 15 |
| 3 | Apa yang terjadi saat tombol power komputer ditekan? Jelaskan alurnya! | 15 |

---

### B.4 Elemen JKI \u2014 Jaringan Komputer & Internet

#### Soal PG

| No | Soal | A | B | C | D | E | Kunci |
|---|---|---|---|---|---|---|---|
| 1 | Alat yang digunakan untuk menghubungkan dua jaringan berbeda adalah... | Switch | Hub | **Router** | Modem | Access Point | **C** |
| 2 | Kepanjangan dari DNS adalah... | **Domain Name System** | Data Network Service | Digital Network Server | Domain Network Service | Data Name System | **A** |
| 3 | Manakah yang merupakan jaringan nirkabel? | **WiFi** | Ethernet | Fiber optik | Coaxial | UTP | **A** |
| 4 | Enkripsi Caesar cipher adalah... | Enkripsi dengan kunci publik | **Enkripsi dengan menggeser huruf** | Enkripsi dengan matriks | Enkripsi modern | Enkripsi kuantum | **B** |
| 5 | Protokol yang mengamankan komunikasi web adalah... | HTTP | FTP | SMTP | **HTTPS** | TCP/IP | **D** |

#### Soal Uraian

| No | Soal | Skor Maks |
|---|---|---|
| 1 | Gambarkan topologi star dan jelaskan kelebihan serta kekurangannya! | 20 |
| 2 | Jelaskan cara kerja enkripsi Caesar cipher! Enkripsikan kata "INFORMATIKA" dengan shift 3! | 20 |
| 3 | Apa yang dimaksud dengan firewall? Sebutkan 3 fungsinya! | 15 |

---

### B.5 Elemen AD \u2014 Analisis Data

#### Soal PG

| No | Soal | A | B | C | D | E | Kunci |
|---|---|---|---|---|---|---|---|
| 1 | Urutan siklus pengolahan data yang benar adalah... | Visualisasi \u2192 Kumpul \u2192 Olah \u2192 Analisis | **Kumpul \u2192 Olah \u2192 Visualisasi \u2192 Analisis \u2192 Interpretasi** | Olah \u2192 Kumpul \u2192 Analisis \u2192 Visualisasi | Analisis \u2192 Kumpul \u2192 Olah \u2192 Visualisasi | Interpretasi \u2192 Olah \u2192 Visualisasi | **B** |
| 2 | Contoh data pribadi yang sensitif adalah... | Nama | Alamat | **NIK** | Hobi | Jenis kelamin | **C** |
| 3 | Grafik yang paling tepat untuk menampilkan proporsi/persentase adalah... | **Pie chart** | Bar chart | Line chart | Scatter plot | Area chart | **A** |
| 4 | UU Perlindungan Data Pribadi di Indonesia adalah... | UU ITE | **UU PDP** | UU Hak Cipta | UU Pers | UU Informasi | **B** |

#### Soal Uraian

| No | Soal | Skor Maks |
|---|---|---|
| 1 | Sebutkan 5 risiko kebocoran data pribadi dan cara pencegahannya! | 20 |
| 2 | Berikan contoh data, informasi, dan pengetahuan dari kasus "nilai ujian siswa"! | 15 |
| 3 | Jelaskan perbedaan antara data kuantitatif dan kualitatif! Berikan 3 contoh masing-masing! | 15 |

#### Soal Praktik

| No | Soal | Alat |
|---|---|---|
| 1 | Kumpulkan data favorit dari 10 teman (film/warna/makanan), olah, dan buat dashboard visualisasinya! | Google Sheets / Data Studio |

---

### B.6 Elemen AP \u2014 Algoritma & Pemrograman

#### Soal PG

| No | Soal | A | B | C | D | E | Kunci |
|---|---|---|---|---|---|---|---|
| 1 | Manakah yang BUKAN tipe data dalam Python? | int | float | str | **char** | bool | **D** |
| 2 | Fungsi untuk menampilkan output di Python adalah... | input() | **print()** | output() | display() | write() | **B** |
| 3 | Hasil dari `print(2 ** 3)` adalah... | 5 | 6 | **8** | 9 | 10 | **C** |
| 4 | Struktur percabangan dalam Python menggunakan kata kunci... | for | while | **if** | elif | else | **C** |
| 5 | Perulangan `for i in range(5):` akan mengulang sebanyak... | 4 kali | **5 kali** | 6 kali | 10 kali | Error | **B** |
| 6 | Fungsi untuk mengubah string menjadi integer adalah... | str() | float() | **int()** | bool() | list() | **C** |
| 7 | Manakah penulisan komentar yang benar di Python? | // ini komentar | **# ini komentar** | /* komentar */ | <!-- komentar --> | ' komentar | **B** |

#### Soal Uraian

| No | Soal | Skor Maks |
|---|---|---|
| 1 | Buat pseudocode untuk program yang meminta 2 angka lalu menampilkan hasil penjumlahan, pengurangan, perkalian, dan pembagian! | 20 |
| 2 | Jelaskan perbedaan antara while dan for loop! Kapan masing-masing lebih tepat digunakan? | 15 |

#### Soal Praktik

| No | Soal | Skor | Alat |
|---|---|---|---|
| 1 | Buat program yang meminta nama dan nilai siswa, lalu menentukan lulus (\u226575) atau tidak! | 20 | Python |
| 2 | Buat program deret Fibonacci hingga suku ke-n (input user)! | 25 | Python |
| 3 | Buat program kalkulator sederhana (+, \u2013, *, /) dengan menu pilihan! | 30 | Python |

---

### B.7 Elemen DSI \u2014 Dampak Sosial Informatika

#### Soal PG

| No | Soal | A | B | C | D | E | Kunci |
|---|---|---|---|---|---|---|---|
| 1 | Komputer generasi pertama menggunakan komponen... | Transistor | IC | **Tabung vakum** | Mikroprosesor | AI | **A** |
| 2 | Tokoh yang dikenal sebagai "bapak komputer" adalah... | Bill Gates | Steve Jobs | **Alan Turing** | Mark Zuckerberg | Charles Babbage | **C** |
| 3 | Lisensi open source yang mewajibkan kode turunan juga open source adalah... | MIT | Apache | **GPL** | BSD | Creative Commons | **C** |
| 4 | Dampak negatif media sosial yang sering terjadi adalah... | **Cyberbullying** | Kolaborasi global | Berbagi informasi | Belajar online | Networking | **A** |
| 5 | Contoh pelanggaran HAKI di bidang digital adalah... | **Pembajakan software** | Menggunakan open source | Membuat konten orisinal | Mencantumkan sumber | Berlisensi | **A** |

#### Soal Uraian

| No | Soal | Skor Maks |
|---|---|---|
| 1 | Buat esai minimal 3 paragraf tentang "Dampak Media Sosial terhadap Remaja" dari segi positif dan negatif! | 25 |
| 2 | Jelaskan perbedaan lisensi GPL, MIT, dan Creative Commons! Berikan contoh software masing-masing! | 20 |
| 3 | Bagaimana perkembangan komputer dari generasi 1 sampai 5? Buat timeline singkat! | 20 |

---

### B.8 Elemen PLB \u2014 Praktik Lintas Bidang

#### Soal Uraian / Projek

| No | Soal | Skor | Bentuk |
|---|---|---|---|
| 1 | Buat proposal proyek Informatika untuk menyelesaikan masalah di lingkungan sekolah! | 25 | Dokumen proposal |
| 2 | Implementasikan solusi dari proposal (program/website/poster interaktif/media edukasi) | 40 | Produk |
| 3 | Buat laporan dokumentasi & presentasikan di depan kelas! | 25 | Presentasi + Laporan |

---

## C. SOAL PTS SEMESTER 1

**Durasi:** 2 JP (90 menit) | **Bentuk:** PG (15 soal) + Uraian (3 soal) | **Skor Total:** 100

### C.1 Pilihan Ganda (PG) \u2014 60 Poin (4 poin/soal)

| No | Soal | Opsi | Kunci |
|---|---|---|---|
| 1 | Berpikir komputasional adalah cara berpikir untuk... | A) Menulis cepat B) **Menyelesaikan masalah secara sistematis** C) Membuat desain D) Berhitung cepat | **B** |
| 2 | Memecah masalah menjadi bagian kecil disebut... | A) Abstraksi B) **Dekomposisi** C) Pola D) Algoritma | **B** |
| 3 | Fungsi AVERAGE pada spreadsheet digunakan untuk... | A) Menjumlah B) **Mencari rata-rata** C) Menghitung D) Mencari nilai tertinggi | **B** |
| 4 | Sistem operasi adalah... | A) **Perangkat lunak yang mengelola HW dan SW** B) Aplikasi office C) Browser D) Game | **A** |
| 5 | Perangkat yang menghubungkan komputer ke internet disebut... | A) **Modem** B) Monitor C) Speaker D) Printer | **A** |
| 6 | Fungsi RAM adalah... | A) **Menyimpan data sementara** B) Menyimpan data permanen C) Memproses data D) Menampilkan gambar | **A** |
| 7 | Ctrl+S pada aplikasi perkantoran berfungsi untuk... | A) **Save** B) Print C) Copy D) Paste | **A** |
| 8 | Manakah yang termasuk perangkat output? | A) Mouse B) Keyboard C) **Monitor** D) Scanner | **C** |
| 9 | Topologi di mana semua komputer terhubung ke satu kabel utama adalah... | A) Star B) **Bus** C) Ring D) Mesh | **B** |
| 10 | VLOOKUP digunakan untuk... | A) **Mencari data secara vertikal** B) Menjumlah data C) Membuat grafik D) Filter data | **A** |
| 11 | Contoh enkripsi sederhana adalah... | A) **Caesar cipher** B) Firewall C) Antivirus D) Password | **A** |
| 12 | Slide master pada presentasi berfungsi untuk... | A) **Mengatur template slide secara global** B) Menambah animasi C) Membuat tabel D) Hyperlink | **A** |
| 13 | HTTP berbeda dengan HTTPS pada aspek... | A) **Keamanan enkripsi** B) Kecepatan C) Ukuran D) Kompatibilitas | **A** |
| 14 | Dalam dekomposisi, hal pertama yang dilakukan adalah... | A) **Identifikasi masalah utama** B) Selesaikan sub-masalah C) Buat laporan D) Evaluasi | **A** |
| 15 | Yang dimaksud dengan abstraksi adalah... | A) **Mengabaikan detail yang tidak perlu** B) Memecah masalah C) Mencari pola D) Membuat algoritma | **A** |

### C.2 Uraian \u2014 40 Poin

| No | Soal | Skor |
|---|---|---|
| 1 | Buat flowchart untuk menentukan bilangan prima atau bukan! | 15 |
| 2 | Jelaskan langkah-langkah membuat mail merge di aplikasi pengolah kata! | 10 |
| 3 | Sebutkan 3 mekanisme internal yang terjadi saat komputer dinyalakan (booting)! | 15 |

### C.3 Kunci Jawaban Uraian PTS

**No. 1 Flowchart Bilangan Prima:**
- Start \u2192 Input n \u2192 Jika n \u2264 1 \u2192 Output "Bukan Prima" \u2192 Selesai
- Loop i dari 2 sampai n/2 \u2192 Jika n % i == 0 \u2192 Output "Bukan Prima" \u2192 Selesai
- Jika tidak ada yang habis membagi \u2192 Output "Prima" \u2192 Selesai

**No. 2 Langkah Mail Merge:**
1. Siapkan data di Excel (daftar nama, alamat, dll)
2. Di Word: Mailings \u2192 Start Mail Merge \u2192 Letters
3. Pilih Recipients \u2192 Use Existing List \u2192 pilih file Excel
4. Insert merge field (nama, alamat, dll) di dokumen
5. Preview Results \u2192 Finish & Merge

**No. 3 Mekanisme Booting:**
1. Power on \u2192 power supply mengirim sinyal ke motherboard
2. BIOS/UEFI menjalankan POST (Power-On Self-Test): cek HW
3. BIOS mencari bootloader di storage (HDD/SSD)
4. Bootloader memuat sistem operasi ke RAM
5. OS mengambil alih kontrol \u2192 tampil desktop/shell

---

## D. SOAL PAS SEMESTER 1

**Durasi:** 2 JP (90 menit) | **Bentuk:** PG (20 soal) + Uraian (3 soal) | **Skor Total:** 100

### D.1 PG \u2014 60 Poin (3 poin/soal)

*(20 soal mencakup seluruh elemen semester 1: BK, TIK, SK, JKI)*

| No | Soal | Kunci |
|---|---|---|
| 1 | Berpikir komputasional membantu kita... | **Menyelesaikan masalah secara terstruktur** |
| 2 | Dekomposisi cocok digunakan ketika... | **Masalah terlalu kompleks untuk diselesaikan sekaligus** |
| 3 | Fungsi COUNT pada spreadsheet menghitung... | **Jumlah sel yang berisi angka** |
| 4 | Sistem operasi Windows termasuk jenis OS... | **Berbasis GUI (Graphical User Interface)** |
| 5 | IP address 192.168.1.1 termasuk kelas... | **C (jaringan lokal)** |
| 6\u201320 | *(Soal mencakup variasi seluruh materi semester 1)* | |

### D.2 Uraian \u2014 40 Poin

| No | Soal | Skor |
|---|---|---|
| 1 | Buat pseudocode program yang meminta 3 angka, lalu menampilkan angka terbesar! | 15 |
| 2 | Sebutkan 4 jenis perangkat jaringan dan fungsinya masing-masing! | 10 |
| 3 | Sebuah perusahaan ingin mengirim surat ke 100 pelanggan. Strategi TIK apa yang paling efisien? Jelaskan langkah-langkahnya! | 15 |

---

## E. SOAL PTS SEMESTER 2

*(Mencakup AD + AP pertemuan 1\u20133)*

| No | Bentuk | Soal | Skor |
|---|---|---|---|
| 1\u201310 | PG | AD (privasi data, siklus data) + AP (pseudocode, flowchart) | 40 |
| 1\u20133 | Uraian | Praktik pengolahan data & pseudocode | 40 |
| 1 | Praktik | Program Python konversi suhu | 20 |

---

## F. SOAL PAT SEMESTER 2 (KENAIKAN KELAS)

*(Mencakup AD, AP, DSI, PLB)*

| No | Bentuk | Lingkup | Skor |
|---|---|---|---|
| 1\u201315 | PG | AD + AP + DSI | 45 |
| 1\u20132 | Uraian | Esai dampak sosial + analisis program | 25 |
| 1 | Praktik | Program Python (pengelolaan data sederhana) | 30 |
| | **Total** | | **100** |

---

## G. FORMAT KARTU SOAL

> *(Untuk setiap soal yang diujikan dalam PTS/PAS/PAT)*

| Format Kartu Soal |
|---|
| **Satuan Pendidikan:** _________________ |
| **Mata Pelajaran:** Informatika |
| **Kelas/Fase:** X / Fase E |
| **No Soal:** ___ |
| **Bentuk:** PG / Uraian / Praktik |
| **Indikator Soal:** _________________ |
| **Level Kognitif:** C1 (Ingat) / C2 (Pahami) / C3 (Aplikasi) / C4 (Analisis) / C5 (Evaluasi) / C6 (Mencipta) |
| **Soal:** _________________ |
| **Kunci/Pedoman Penskoran:** _________________ |
| **Sumber:** Buku Informatika Kelas X / Referensi lain |

---

## H. REKAP BANK SOAL

| Elemen | PG | Uraian | Praktik | Total Butir |
|---|---|---|---|---|
| BK | 5 | 4 | 1 | 10 |
| TIK | 5 | 3 | 2 | 10 |
| SK | 5 | 3 | 0 | 8 |
| JKI | 5 | 3 | 0 | 8 |
| AD | 4 | 3 | 1 | 8 |
| AP | 7 | 2 | 3 | 12 |
| DSI | 5 | 3 | 0 | 8 |
| PLB | 0 | 1 | 3 | 4 |
| PTS Ganjil | 15 | 3 | 0 | 18 |
| PAS Ganjil | 20 | 3 | 0 | 23 |
| PTS Genap | 10 | 3 | 1 | 14 |
| PAT | 15 | 2 | 1 | 18 |
| **Total** | **96** | **33** | **12** | **141 butir** |

---

Mengetahui,  
Kepala Sekolah

_________________________

Guru Mata Pelajaran,

{GURU}
NIP. {NIP}

_________________________
"""


# =========== 10. KOKURIKULER ===========
def kokurikuler():
    return f"""# RENCANA KEGIATAN KOKURIKULER

**Satuan Pendidikan** : _________________________
**Mata Pelajaran** : Informatika
**Kelas / Fase** : X (Sepuluh) / Fase E
**Tahun Pelajaran** : 2026/2027

---

## A. PENGERTIAN

**Kegiatan Kokurikuler** adalah kegiatan yang dilaksanakan untuk pengembangan atau pendalaman kompetensi dasar
yang sudah dipelajari dalam kegiatan intrakurikuler dengan penugasan terstruktur dan/atau kegiatan terprogram
yang dilaksanakan di luar jam tatap muka namun masih dalam lingkup kurikulum.

---

## B. TUJUAN

1. Memperdalam dan memperluas pemahaman siswa terhadap materi Informatika
2. Mengembangkan keterampilan praktis melalui tugas proyek mandiri/kelompok
3. Membangun kemandirian dan tanggung jawab siswa dalam belajar
4. Meningkatkan kemampuan berpikir kritis, kreatif, dan kolaboratif

---

## C. PROGRAM KOKURIKULER PER SEMESTER

### SEMESTER 1 (Ganjil)

| No | Elemen | Jenis Kegiatan | Bentuk Luaran | Waktu | Penilaian |
|---|---|---|---|---|---|
| 1 | Pengenalan | Membaca & merangkum pengantar Informatika | Rangkuman tulisan tangan | Minggu 1\u20132 | Ceklist rangkuman |
| 2 | BK | Mengerjakan lembar kerja dekomposisi, pola, abstraksi | LKPD terisi lengkap | Minggu 3\u20136 | Skor LKPD |
| 3 | TIK | Proyek pembuatan dokumen terintegrasi | File dokumen + spreadsheet + presentasi | Minggu 7\u201310 | Rubrik proyek |
| 4 | SK | Poster komponen sistem komputer | Poster digital/fisik | Minggu 11\u201313 | Rubrik poster |
| 5 | JKI | Simulasi konfigurasi jaringan | Laporan simulasi + diagram | Minggu 14\u201315 | Rubrik laporan |

### SEMESTER 2 (Genap)

| No | Elemen | Jenis Kegiatan | Bentuk Luaran | Waktu | Penilaian |
|---|---|---|---|---|---|
| 1 | AD | Proyek analisis data sederhana | Laporan analisis + visualisasi data | Minggu 1\u20134 | Rubrik laporan |
| 2 | AP | Tugas pemrograman mandiri | Kode Python + dokumentasi | Minggu 5\u201311 | Rubrik coding |
| 3 | DSI | Esai dampak sosial informatika | Esai 3\u20135 paragraf | Minggu 12\u201314 | Rubrik esai |
| 4 | PLB | Proyek lintas bidang kelompok | Produk + laporan + presentasi | Minggu 15\u201318 | Rubrik proyek |

---

## D. JADWAL KEGIATAN KOKURIKULER

| Bulan ke- | Minggu ke- | Kegiatan | Keterangan |
|---|---|---|---|
| 1 | 1\u20132 | Rangkuman pengantar Informatika | Tugas mandiri |
| 2 | 3\u20136 | LKPD Berpikir Komputasional | Tugas di LKPD masing-masing |
| 3 | 7\u201310 | Proyek integrasi aplikasi perkantoran | Tugas kelompok (3\u20134 orang) |
| 4 | 11\u201313 | Poster sistem komputer | Tugas individu/kelompok |
| 5 | 14\u201315 | Laporan simulasi jaringan | Tugas kelompok |
| 6 | 1\u20134 | Proyek analisis data | Tugas individu |
| 7 | 5\u201311 | Tugas pemrograman Python | Tugas mandiri bertahap |
| 8 | 12\u201314 | Esai dampak sosial | Tugas individu |
| 9 | 15\u201318 | Proyek lintas bidang | Tugas kelompok + presentasi |

---

## E. PEDOMAN PENILAIAN KOKURIKULER

| Rentang Skor | Predikat | Deskripsi |
|---|---|---|
| 86\u2013100 | Sangat Baik (SB) | Luaran melebihi ekspektasi, orisinal, rapi |
| 71\u201385 | Baik (B) | Luaran sesuai kriteria, cukup rapi |
| 56\u201370 | Cukup (C) | Luaran kurang lengkap, perlu perbaikan |
| \u226455 | Perlu Bimbingan (PB) | Luaran tidak sesuai, perlu bimbingan intensif |

---

## F. REKAP NILAI KOKURIKULER

| No | Nama Siswa | Rangkuman | LKPD BK | Proyek TIK | Poster SK | Laporan JKI | Proyek AD | Python | Esai DSI | Proyek PLB | Rata-rata | Predikat |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | | | | | | | | | | | | |
| 2 | | | | | | | | | | | | |
| dst | | | | | | | | | | | | |

> Catatan: Nilai kokurikuler dicatat sebagai nilai tambahan dan diintegrasikan sebagai portofolio siswa.

---

## G. INTEGRASI 7 KEBIASAAN ANAK INDONESIA HEBAT (7 KAIH)

Berdasarkan SEB 3 Menteri No. 1 Tahun 2025 dan SE No. 14 Tahun 2025:

| # | Kebiasaan | Aktivitas Terintegrasi Informatika Kelas X | Waktu |
|---|-----------|--------------------------------------------|-------|
| 1 | **Bangun Pagi** | Kedisiplinan praktik lab, analisis data kehadiran | Harian |
| 2 | **Beribadah** | Doa sebelum/sesudah pembelajaran, etika digital | Setiap pertemuan |
| 3 | **Berolahraga** | Senam AIH, jeda ceria, ergonomi komputer | 2x/minggu |
| 4 | **Makan Sehat & Bergizi** | Tabel gizi & visualisasi data makanan (Bab 3 & 6) | Semester 2 |
| 5 | **Gemar Belajar** | Literasi digital 15 menit, eksplorasi Python mandiri | Setiap pertemuan |
| 6 | **Bermasyarakat** | Proyek PLB: solusi TIK untuk masalah sekolah | Semester 2 |
| 7 | **Tidur Cepat** | Edukasi screen time, proyek analisis data tidur | Semester 1 |

## H. LEMBAR REFLEKSI (Deep Learning + 7 KAIH)

| Pertanyaan | Jawaban |
|---|---|
| **Mindful:** Apa yang aku pelajari hari ini? | |
| **Meaningful:** Bagaimana ini berguna untuk kehidupanku? | |
| **Joyful:** Hal paling seru dari pembelajaran hari ini? | |
| **7 KAIH:** Kebiasaan baik apa yang aku lakukan hari ini? | |
| **Dimensi:** Dimensi Profil Lulusan mana yang terasah? | |

> **Catatan:** P5 tetap berjalan sebagai proyek tematik. 7 KAIH adalah pembiasaan harian. Deep Learning adalah pendekatan pembelajaran (Mindful, Meaningful, Joyful).

---

Mengetahui,  
Kepala Sekolah

_________________________

Guru Mata Pelajaran,

{GURU}
NIP. {NIP}

_________________________
"""


# =========== 11. JURNAL ===========
def jurnal():
    return f"""# JURNAL PEMBELAJARAN

**Satuan Pendidikan** : _________________________
**Mata Pelajaran** : Informatika
**Kelas / Fase** : X (Sepuluh) / Fase E
**Tahun Pelajaran** : 2026/2027

---

## A. FORMAT JURNAL HARIAN

| Pertemuan | Hari/Tanggal | JP | Materi | Metode | Kegiatan Inti | Refleksi | TTD Guru |
|---|---|---|---|---|---|---|---|
| 1 | | 2 | Pengenalan: CP, ATP, kontrak belajar | Diskusi, Ceramah | Kontrak belajar, pre-test diagnostik | | |
| 2 | | 2 | Konsep berpikir komputasional | Discovery Learning | Pengantar dekomposisi & studi kasus | | |
| 3 | | 2 | Dekomposisi | Diskusi, Latihan | Latihan dekomposisi masalah sehari-hari | | |
| 4 | | 2 | Pengenalan Pola | Problem Based Learning | Identifikasi pola dari data | | |
| 5 | | 2 | Abstraksi & Algoritma | Diskusi, Latihan | Menyusun langkah solusi & abstraksi | | |
| 6 | | 2 | Penerapan BK dalam kehidupan | Project Based Learning | Studi kasus & presentasi solusi | | |
| 7 | | 2 | Pengolah Kata (Word Processing) | Demonstrasi, Praktik | Fitur lanjut: mail merge, daftar isi | | |
| 8 | | 2 | Spreadsheet (Excel/Sheets) | Demonstrasi, Praktik | Formula, fungsi, grafik | | |
| 9 | | 2 | Presentasi (PowerPoint/Slides) | Demonstrasi, Praktik | Slide master, animasi, hyperlink | | |
| 10 | | 2 | Integrasi Aplikasi Perkantoran | Project Based Learning | Proyek integrasi dokumen | | |
| 11 | | 2 | Perangkat keras komputer | Discovery Learning | Identifikasi komponen HW | | |
| 12 | | 2 | Perangkat lunak & sistem operasi | Diskusi, Praktik | Instalasi OS virtual | | |
| 13 | | 2 | Mekanisme internal komputer | Diskusi, Animasi | Booting, arsitektur HW-SW-User | | |
| 14 | | 2 | Konsep jaringan komputer | Discovery Learning | Topologi, perangkat jaringan | | |
| 15 | | 2 | Internet & keamanan dasar | Diskusi, Praktik | Konfigurasi IP, enkripsi Caesar | | |
| 16 | | 2 | **PTS Semester 1** | Tes | Tes tulis | | |
| 17 | | 2 | Review Semester 1 & Refleksi | Diskusi | Pembahasan PTS, review materi | | |
| 18 | | 2 | **PAS Semester 1 + Pengayaan** | Tes | Tes akhir semester + pengayaan | | |
| 19 | | 2 | Konsep data & siklus pengolahan | Discovery Learning | Data, informasi, pengetahuan | | |
| 20 | | 2 | Privasi & keamanan data | Diskusi, Studi Kasus | UU PDP, perlindungan data pribadi | | |
| 21 | | 2 | Pengolahan data & visualisasi | Demonstrasi, Praktik | Pengolahan & visualisasi data | | |
| 22 | | 2 | Interpretasi data & dashboard | Project Based Learning | Membuat dashboard sederhana | | |
| 23 | | 2 | Pseudocode & flowchart | Discovery Learning | Menulis pseudocode & flowchart | | |
| 24 | | 2 | Pengenalan Python | Demonstrasi, Praktik | Variabel, tipe data, I/O | | |
| 25 | | 2 | Percabangan (if/elif/else) | Demonstrasi, Praktik | Program dengan percabangan | | |
| 26 | | 2 | Perulangan (for, while) | Demonstrasi, Praktik | Program dengan perulangan | | |
| 27 | | 2 | Fungsi & modularisasi | Demonstrasi, Praktik | Membuat fungsi sendiri | | |
| 28 | | 2 | Struktur data: list & dictionary | Demonstrasi, Praktik | Mengelola data dengan list & dict | | |
| 29 | | 2 | Debugging & error handling | Problem Based Learning | Try-except, membaca traceback | | |
| 30 | | 2 | Proyek pemrograman kelompok | Project Based Learning | Membuat program aplikasi sederhana | | |
| 31 | | 2 | **PTS Semester 2** | Tes | Tes tulis + praktik | | |
| 32 | | 2 | Sejarah & perkembangan komputer | Discovery Learning | Generasi komputer, tokoh penting | | |
| 33 | | 2 | Lisensi software & HAKI | Diskusi, Studi Kasus | Open source vs proprietary, HAKI | | |
| 34 | | 2 | Dampak TIK & etika digital | Diskusi, Esai | Dampak positif/negatif, etika digital | | |
| 35 | | 2 | Konsep proyek lintas bidang | Diskusi | Pemilihan topik, pembentukan kelompok | | |
| 36 | | 2 | Implementasi proyek lintas bidang | Project Based Learning | Pengembangan solusi & dokumentasi | | |
| 37 | | 2 | Finalisasi & presentasi proyek | Presentasi | Presentasi & evaluasi proyek | | |
| 38 | | 2 | **PAT / UKK** | Tes | Tes akhir tahun (teori + praktik) | | |
| 39 | | 2 | Pengayaan & remedial | Bimbingan | Perbaikan nilai & pengayaan | | |
| 40 | | 2 | Penutup tahun pelajaran | Diskusi | Refleksi tahunan, pengumuman hasil | | |

---

## B. LEGENDA METODE PEMBELAJARAN

| Kode | Metode |
|---|---|
| PBL | Problem Based Learning |
| PjBL | Project Based Learning |
| DL | Discovery Learning |
| D&D | Demonstrasi & Praktik |
| DS | Diskusi |

> Catatan: Jurnal ini diisi setiap selesai pertemuan. TTD guru sebagai bukti pelaksanaan pembelajaran.

---

Mengetahui,  
Kepala Sekolah

_________________________

Guru Mata Pelajaran,

{GURU}
NIP. {NIP}

_________________________
"""


# =========== 12. ANALISIS CP & TP ===========
def analisis_cp_tp():
    return f"""# ANALISIS CAPAIAN PEMBELAJARAN & TUJUAN PEMBELAJARAN

**Satuan Pendidikan** : _________________________
**Mata Pelajaran** : Informatika
**Kelas / Fase** : X (Sepuluh) / Fase E
**Tahun Pelajaran** : 2026/2027

---

## A. CAPAIAN PEMBELAJARAN (CP) FASE E

Pada akhir Fase E, peserta didik mampu menerapkan berpikir komputasional secara mandiri dalam menyelesaikan
persoalan dengan mengembangkan atau mengintegrasikan program berjumlah sedang yang modular, serta dapat
menggunakan dan memanfaatkan berbagai aplikasi perkantoran untuk berkreasi. Peserta didik mampu menjelaskan
cara kerja sistem komputer, jaringan komputer, dan internet, serta menerapkannya secara tepat untuk
memudahkan kehidupan. Peserta didik mampu mendeskripsikan, menganalisis, mengolah, dan menginterpretasi
data, serta mempresentasikan hasilnya. Peserta didik mampu menerapkan praktik baik dalam berlinteraksi
di ruang media digital dan menerapkannya sesuai konteks. Peserta didik mampu bergotong royong dalam
menyelesaikan persoalan yang diberikan dengan mengembangkan artefak komputasional secara terintegrasi
dan teruji dalam suatu proyek bidang yang diminati.

---

## B. ANALISIS CP PER ELEMEN

### Elemen 1: BK — Berpikir Komputasional (8 JP)

| Elemen CP | Sub-elemen | Kognitif | Keterampilan | Dimensi Profil Lulusan |
|---|---|---|---|---|
| Pada akhir Fase E, peserta didik mampu menerapkan berpikir komputasional secara mandiri dalam menyelesaikan persoalan dengan mengembangkan atau mengintegrasikan program berjumlah sedang yang modular | Dekomposisi | C4 (Menganalisis) | Memecah masalah | Penalaran Kritis |
| | Pengenalan Pola | C4 (Menganalisis) | Mengidentifikasi pola | Penalaran Kritis |
| | Abstraksi | C4 (Menganalisis) | Memilah informasi relevan | Penalaran Kritis |
| | Algoritma | C6 (Mencipta) | Menyusun langkah solusi | Kreativitas |

### Elemen 2: TIK — Teknologi Informasi & Komunikasi (8 JP)

| Elemen CP | Sub-elemen | Kognitif | Keterampilan | Dimensi Profil Lulusan |
|---|---|---|---|---|
| Peserta didik mampu menggunakan dan memanfaatkan berbagai aplikasi perkantoran untuk berkreasi | Pengolah Kata | C3 (Mengaplikasi) | Mengoperasikan fitur lanjut | Kreativitas |
| | Spreadsheet | C3 (Mengaplikasi) | Mengolah data & formula | Kreativitas |
| | Presentasi | C3 (Mengaplikasi) | Membuat presentasi interaktif | Komunikasi |
| | Integrasi Aplikasi | C4 (Menganalisis) | Mengintegrasikan dokumen | Kreativitas |

### Elemen 3: SK — Sistem Komputer (6 JP)

| Elemen CP | Sub-elemen | Kognitif | Keterampilan | Dimensi Profil Lulusan |
|---|---|---|---|---|
| Peserta didik mampu menjelaskan cara kerja sistem komputer | Perangkat Keras | C2 (Memahami) | Mengidentifikasi HW | Kemandirian |
| | Perangkat Lunak | C2 (Memahami) | Menjelaskan OS | Kemandirian |
| | Mekanisme Internal | C4 (Menganalisis) | Menganalisis booting | Penalaran Kritis |

### Elemen 4: JKI — Jaringan Komputer & Internet (6 JP)

| Elemen CP | Sub-elemen | Kognitif | Keterampilan | Dimensi Profil Lulusan |
|---|---|---|---|---|
| Peserta didik mampu menjelaskan cara kerja jaringan komputer dan internet, serta menerapkannya secara tepat | Konsep Jaringan | C2 (Memahami) | Topologi & perangkat | Penalaran Kritis |
| | Internet & Konektivitas | C3 (Mengaplikasi) | Konfigurasi IP, DNS | Kemandirian |
| | Keamanan Jaringan | C3 (Mengaplikasi) | Enkripsi dasar | Kewargaan |

### Elemen 5: AD — Analisis Data (8 JP)

| Elemen CP | Sub-elemen | Kognitif | Keterampilan | Dimensi Profil Lulusan |
|---|---|---|---|---|
| Peserta didik mampu mendeskripsikan, menganalisis, mengolah, dan menginterpretasi data, serta mempresentasikan hasilnya | Konsep Data | C2 (Memahami) | Data, informasi, pengetahuan | Penalaran Kritis |
| | Privasi & Keamanan Data | C4 (Menganalisis) | Menganalisis risiko | Kewargaan |
| | Pengolahan & Visualisasi | C4 (Menganalisis) | Mengolah & visualisasi data | Penalaran Kritis |
| | Dashboard & Interpretasi | C4 (Menganalisis) | Membaca & menyajikan data | Komunikasi |

### Elemen 6: AP — Algoritma & Pemrograman (14 JP)

| Elemen CP | Sub-elemen | Kognitif | Keterampilan | Dimensi Profil Lulusan |
|---|---|---|---|---|
| Peserta didik mampu menerapkan berpikir komputasional secara mandiri dalam menyelesaikan persoalan dengan mengembangkan atau mengintegrasikan program berjumlah sedang yang modular | Pseudocode & Flowchart | C3 (Mengaplikasi) | Merancang program | Kreativitas |
| | Dasar Python | C3 (Mengaplikasi) | Variabel, I/O | Kemandirian |
| | Percabangan | C3 (Mengaplikasi) | if/elif/else | Penalaran Kritis |
| | Perulangan | C3 (Mengaplikasi) | for, while | Kreativitas |
| | Fungsi | C3 (Mengaplikasi) | Modularisasi | Kreativitas |
| | Struktur Data | C3 (Mengaplikasi) | List, dictionary | Penalaran Kritis |
| | Debugging | C4 (Menganalisis) | Error handling | Penalaran Kritis |

### Elemen 7: DSI — Dampak Sosial Informatika (6 JP)

| Elemen CP | Sub-elemen | Kognitif | Keterampilan | Dimensi Profil Lulusan |
|---|---|---|---|---|
| Peserta didik mampu menerapkan praktik baik dalam berinteraksi di ruang media digital dan menerapkannya sesuai konteks | Sejarah Komputer | C1 (Mengingat) | Menjelaskan perkembangan | Kemandirian |
| | Lisensi & HAKI | C2 (Memahami) | Membedakan lisensi | Kewargaan |
| | Dampak TIK & Etika | C4 (Menganalisis) | Menganalisis dampak | Keimanan & Ketakwaan |

### Elemen 8: PLB — Praktik Lintas Bidang (6 JP)

| Elemen CP | Sub-elemen | Kognitif | Keterampilan | Dimensi Profil Lulusan |
|---|---|---|---|---|
| Peserta didik mampu bergotong royong dalam menyelesaikan persoalan yang diberikan dengan mengembangkan artefak komputasional secara terintegrasi dan teruji dalam suatu proyek bidang yang diminati | Proposal Proyek | C6 (Mencipta) | Menyusun rencana proyek | Kolaborasi |
| | Implementasi | C6 (Mencipta) | Mengembangkan produk | Kreativitas |
| | Dokumentasi & Presentasi | C6 (Mencipta) | Mendokumentasikan & presentasi | Komunikasi |

---

## C. KETERKAITAN CP DENGAN DIMENSI PROFIL LULUSAN

| Dimensi | Elemen CP yang Mendukung | Aktivitas |
|---|---|---|
| **Kolaborasi** | PLB (Praktik Lintas Bidang) | Proyek kelompok lintas bidang |
| **Kemandirian** | SK, JKI, AP | Praktik individu, instalasi, coding |
| **Penalaran Kritis** | BK, AD, JKI | Dekomposisi, analisis data, keamanan |
| **Kreativitas** | TIK, AP, PLB | Proyek perkantoran, coding, PLB |
| **Keimanan & Ketakwaan** | DSI | Etika digital, literasi media |
| **Kewargaan** | DSI, JKI | Lisensi HAKI, keamanan data |
| **Kesehatan** | Seluruh elemen | Manajemen waktu & postur saat praktik |
| **Komunikasi** | TIK, AD, PLB | Presentasi, dashboard, dokumentasi |

---

## D. PEMETAAN TP KE CP

| Elemen | CP | TP | Indikator | Bentuk Asesmen |
|---|---|---|---|---|
| BK | Menerapkan berpikir komputasional secara mandiri | TP.1.1 s.d TP.1.4 | Mendekomposisi, mengenali pola, abstraksi, algoritma | LKPD, rubrik proyek |
| TIK | Menggunakan aplikasi perkantoran untuk berkreasi | TP.2.1 s.d TP.2.4 | Mengoperasikan fitur lanjut office | Praktik, produk |
| SK | Menjelaskan cara kerja sistem komputer | TP.3.1 s.d TP.3.3 | Identifikasi HW, OS, mekanisme | Tes tulis, observasi |
| JKI | Menjelaskan jaringan & internet, menerapkan secara tepat | TP.4.1 s.d TP.4.3 | Topologi, konfigurasi, enkripsi | Praktik, laporan |
| AD | Mendeskripsikan, menganalisis, mengolah, interpretasi data | TP.6.1 s.d TP.6.4 | Siklus data, privasi, visualisasi | Produk, tes tulis |
| AP | Menerapkan BK dalam pemrograman modular | TP.7.1 s.d TP.7.7 | Pseudocode, Python, debugging | Praktik, proyek |
| DSI | Menerapkan praktik baik interaksi digital | TP.8.1 s.d TP.8.3 | Sejarah, lisensi, dampak TIK | Esai, tes tulis |
| PLB | Gotong royong mengembangkan artefak komputasional | TP.9.1 s.d TP.9.3 | Proposal, implementasi, presentasi | Rubrik proyek |

---

Mengetahui,  
Kepala Sekolah

_________________________

Guru Mata Pelajaran,

{GURU}
NIP. {NIP}

_________________________
"""


# =========== 13. DAFTAR NILAI ===========
def daftar_nilai():
    return f"""# DAFTAR NILAI INFORMATIKA KELAS X

**Satuan Pendidikan** : _________________________
**Mata Pelajaran** : Informatika
**Kelas / Fase** : X (Sepuluh) / Fase E
**Tahun Pelajaran** : 2026/2027

---

## A. KOMPONEN PENILAIAN

| No | Komponen | Bobot | Keterangan |
|---|---|---|---|
| 1 | **Formatif** (Observasi, LKPD, Praktik Harian, Kuis) | 60% | Dinilai setiap pertemuan |
| 2 | **Sumatif Lingkup Materi** (Akhir Elemen) | 20% | 1 kali per elemen |
| 3 | **Sumatif Semester (PTS)** | 10% | Tengah semester |
| 4 | **Sumatif Semester (PAS/PAT)** | 10% | Akhir semester |
| | **Total** | **100%** | |

---

## B. FORMAT NILAI FORMATIF PER ELEMEN

### Semester 1 (Ganjil)

#### Elemen BK — Berpikir Komputasional (TP.1.1 s.d TP.1.4)

| No | Nama Siswa | TP.1.1 Dekomposisi | TP.1.2 Pola | TP.1.3 Abstraksi | TP.1.4 Algoritma | Rata-rata BK |
|---|---|---|---|---|---|---|
| 1 | | | | | | |
| 2 | | | | | | |
| ... | | | | | | |

#### Elemen TIK — Teknologi Informasi & Komunikasi (TP.2.1 s.d TP.2.4)

| No | Nama Siswa | TP.2.1 Word | TP.2.2 Spreadsheet | TP.2.3 Presentasi | TP.2.4 Integrasi | Rata-rata TIK |
|---|---|---|---|---|---|---|
| 1 | | | | | | |
| 2 | | | | | | |
| ... | | | | | | |

#### Elemen SK — Sistem Komputer (TP.3.1 s.d TP.3.3)

| No | Nama Siswa | TP.3.1 HW | TP.3.2 SW/OS | TP.3.3 Mekanisme | Rata-rata SK |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |
| ... | | | | | |

#### Elemen JKI — Jaringan Komputer & Internet (TP.4.1 s.d TP.4.3)

| No | Nama Siswa | TP.4.1 Konsep | TP.4.2 Konfigurasi | TP.4.3 Keamanan | Rata-rata JKI |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |
| ... | | | | | |

### Semester 2 (Genap)

#### Elemen AD — Analisis Data (TP.6.1 s.d TP.6.4)

| No | Nama Siswa | TP.6.1 Data | TP.6.2 Privasi | TP.6.3 Olah/Visual | TP.6.4 Dashboard | Rata-rata AD |
|---|---|---|---|---|---|---|
| 1 | | | | | | |
| 2 | | | | | | |
| ... | | | | | | |

#### Elemen AP — Algoritma & Pemrograman (TP.7.1 s.d TP.7.7)

| No | Nama Siswa | TP.7.1 Flow | TP.7.2 Python | TP.7.3 If | TP.7.4 Loop | TP.7.5 Fungsi | TP.7.6 List | TP.7.7 Debug | Rata-rata AP |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | | | | | | | | | |
| 2 | | | | | | | | | |
| ... | | | | | | | | | |

#### Elemen DSI — Dampak Sosial Informatika (TP.8.1 s.d TP.8.3)

| No | Nama Siswa | TP.8.1 Sejarah | TP.8.2 Lisensi | TP.8.3 Dampak | Rata-rata DSI |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |
| ... | | | | | |

#### Elemen PLB — Praktik Lintas Bidang (TP.9.1 s.d TP.9.3)

| No | Nama Siswa | TP.9.1 Proposal | TP.9.2 Produk | TP.9.3 Presentasi | Rata-rata PLB |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |
| ... | | | | | |

---

## C. NILAI SUMATIF

### Nilai Sumatif Lingkup Materi

| No | Nama Siswa | BK | TIK | SK | JKI | AD | AP | DSI | PLB | Rata-rata |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | | | | | | | | | | |
| 2 | | | | | | | | | | |
| ... | | | | | | | | | | |

### Nilai Sumatif Semester

| No | Nama Siswa | PTS Ganjil | PAS Ganjil | PTS Genap | PAT Genap |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |
| ... | | | | | |

---

## D. NILAI AKHIR SEMESTER GANJIL

| No | Nama Siswa | Rata-rata Formatif (60%) | Sumatif Lingkup (20%) | PTS (10%) | PAS (10%) | Nilai Akhir | Predikat |
|---|---|---|---|---|---|---|---|
| 1 | | | | | | | |
| 2 | | | | | | | |
| ... | | | | | | | |

---

## E. NILAI AKHIR SEMESTER GENAP

| No | Nama Siswa | Rata-rata Formatif (60%) | Sumatif Lingkup (20%) | PTS (10%) | PAT (10%) | Nilai Akhir | Predikat |
|---|---|---|---|---|---|---|---|
| 1 | | | | | | | |
| 2 | | | | | | | |
| ... | | | | | | | |

---

## F. PREDIKAT

| Rentang Nilai | Predikat |
|---|---|
| 86 – 100 | Sangat Baik (SB) |
| 71 – 85 | Baik (B) |
| 56 – 70 | Cukup (C) |
| ≤ 55 | Perlu Bimbingan (PB) |

---

Mengetahui,  
Kepala Sekolah

_________________________

Guru Mata Pelajaran,

{GURU}
NIP. {NIP}

_________________________
"""


# =========== 14. REMEDIAL ===========
def remedial():
    return f"""# PROGRAM REMEDIAL & PENGAYAAN

**Satuan Pendidikan** : _________________________
**Mata Pelajaran** : Informatika
**Kelas / Fase** : X (Sepuluh) / Fase E
**Tahun Pelajaran** : 2026/2027

---

## A. KETENTUAN

1. **Remedial** diberikan kepada peserta didik yang belum mencapai Kriteria Ketercapaian Tujuan Pembelajaran (KKTP)
   atau nilai di bawah standar ketuntasan (≤70 dari rentang 0–100).
2. **Pengayaan** diberikan kepada peserta didik yang telah mencapai atau melampaui KKTP.
3. Remedial dilaksanakan maksimal 2 kali. Jika setelah 2 kali remedial belum tuntas, peserta didik mengikuti
   program pembelajaran ulang pada materi yang belum tuntas.

---

## B. JADWAL REMEDIAL & PENGAYAAN

| No | Elemen | Tanggal Remedial | Tanggal Pengayaan | Waktu | Tempat |
|---|---|---|---|---|---|
| 1 | BK (Berpikir Komputasional) | | | 2 JP | Lab Komputer / Kelas |
| 2 | TIK (Teknologi Informasi & Komunikasi) | | | 2 JP | Lab Komputer |
| 3 | SK (Sistem Komputer) | | | 2 JP | Kelas |
| 4 | JKI (Jaringan Komputer & Internet) | | | 2 JP | Lab Komputer |
| 5 | AD (Analisis Data) | | | 2 JP | Lab Komputer |
| 6 | AP (Algoritma & Pemrograman) | | | 2 JP | Lab Komputer |
| 7 | DSI (Dampak Sosial Informatika) | | | 2 JP | Kelas |
| 8 | PLB (Praktik Lintas Bidang) | | | 2 JP | Lab Komputer / Lapangan |

---

## C. FORMAT PROGRAM REMEDIAL

| No | Nama Siswa | Elemen | TP | Nilai Awal | Target KKTP (70) | Bentuk Remedial | Tanggal | Nilai Akhir | Keterangan |
|---|---|---|---|---|---|---|---|---|---|
| 1 | | | | | | | | | |
| 2 | | | | | | | | | |
| ... | | | | | | | | | |

### Bentuk-bentuk Remedial:

| Bentuk | Deskripsi |
|---|---|
| **Pembelajaran Ulang** | Mengulang materi dengan metode berbeda |
| **Bimbingan Perorangan** | Belajar satu lawan satu dengan guru/tutor sebaya |
| **Penugasan Khusus** | Tugas terstruktur tambahan |
| **Latihan Soal** | Soal-soal tambahan untuk memperkuat pemahaman |
| **Praktik Tambahan** | Praktik ulang di laboratorium |

---

## D. FORMAT PROGRAM PENGAYAAN

| No | Nama Siswa | Elemen | Bentuk Pengayaan | Tanggal | Deskripsi |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |
| ... | | | | | |

### Bentuk-bentuk Pengayaan:

| Bentuk | Deskripsi |
|---|---|
| **Proyek Mandiri** | Tugas proyek lebih kompleks |
| **Studi Kasus Lanjutan** | Menganalisis kasus lebih dalam |
| **Tutor Sebaya** | Membantu teman yang remedial |
| **Kompetisi/SOAL Tantangan** | Soal/kompetisi tingkat lebih tinggi |
| **Eksplorasi Mandiri** | Mengeksplorasi topik terkait secara mandiri |

---

## E. RENCANA REMEDIAL PER ELEMEN

### Elemen BK — Berpikir Komputasional

| TP | Indikator Belum Tuntas | Rencana Remedial |
|---|---|---|
| TP.1.1 | Belum mampu mendekomposisi masalah | Latihan dekomposisi dari masalah sederhana dengan panduan |
| TP.1.2 | Belum mampu mengidentifikasi pola | Studi pola dari kumpulan data bergambar |
| TP.1.3 | Belum mampu melakukan abstraksi | Latihan memilah informasi relevan/tidak relevan |
| TP.1.4 | Belum mampu menyusun algoritma | Latihan langkah demi langkah dengan panduan flowchart |

### Elemen TIK — Teknologi Informasi & Komunikasi

| TP | Indikator Belum Tuntas | Rencana Remedial |
|---|---|---|
| TP.2.1 | Belum menguasai fitur lanjut pengolah kata | Tutorial terpandu mail merge & daftar isi |
| TP.2.2 | Belum menguasai spreadsheet | Latihan formula dasar & fungsi SUM/AVERAGE/IF |
| TP.2.3 | Belum mampu membuat presentasi interaktif | Template presentasi dengan panduan slide master |
| TP.2.4 | Belum mampu integrasi aplikasi | Proyek mini integrasi dokumen sederhana |

### Elemen SK — Sistem Komputer

| TP | Indikator Belum Tuntas | Rencana Remedial |
|---|---|---|
| TP.3.1 | Belum hafal komponen HW | Games identifikasi komponen + kuis gambar |
| TP.3.2 | Belum paham jenis OS & fungsinya | Video tutorial sistem operasi + diskusi |
| TP.3.3 | Belum paham mekanisme internal | Animasi booting + simulasi virtual |

### Elemen JKI — Jaringan Komputer & Internet

| TP | Indikator Belum Tuntas | Rencana Remedial |
|---|---|---|
| TP.4.1 | Belum paham topologi & perangkat | Diagram interaktif + role play topologi |
| TP.4.2 | Belum bisa konfigurasi konektivitas | Simulasi Cisco Packet Tracer terbimbing |
| TP.4.3 | Belum paham enkripsi dasar | Praktik Caesar cipher dengan alat bantu |

### Elemen AD — Analisis Data

| TP | Indikator Belum Tuntas | Rencana Remedial |
|---|---|---|
| TP.6.1 | Belum paham data vs informasi vs pengetahuan | Studi kasus konkret dengan contoh nyata |
| TP.6.2 | Belum paham privasi data | Diskusi kasus kebocoran data + simulasi |
| TP.6.3 | Belum bisa mengolah & visualisasi data | Tutorial terpandu membuat grafik di spreadsheet |
| TP.6.4 | Belum bisa interpretasi & dashboard | Template dashboard + panduan interpretasi |

### Elemen AP — Algoritma & Pemrograman

| TP | Indikator Belum Tuntas | Rencana Remedial |
|---|---|---|
| TP.7.1 | Belum bisa pseudocode/flowchart | Lembar kerja langkah demi langkah |
| TP.7.2 | Belum paham variabel & I/O Python | Latihan interaktif di Python Tutor |
| TP.7.3 | Belum paham percabangan | Studi kasus if/elif/else dengan contoh sehari-hari |
| TP.7.4 | Belum paham perulangan | Latihan for/while dengan pola visual |
| TP.7.5 | Belum bisa membuat fungsi | Praktek membuat fungsi dari kode yang sudah ada |
| TP.7.6 | Belum paham list & dictionary | Latihan manipulasi data dengan list/dict |
| TP.7.7 | Belum bisa debugging | Belajar membaca traceback error |

### Elemen DSI — Dampak Sosial Informatika

| TP | Indikator Belum Tuntas | Rencana Remedial |
|---|---|---|
| TP.8.1 | Belum hafal sejarah & tokoh | Timeline visual + kuis tokoh |
| TP.8.2 | Belum paham lisensi software | Tabel perbandingan lisensi + contoh |
| TP.8.3 | Belum mampu analisis dampak | Studi kasus dampak TIK + panduan esai |

### Elemen PLB — Praktik Lintas Bidang

| TP | Indikator Belum Tuntas | Rencana Remedial |
|---|---|---|
| TP.9.1 | Belum bisa menyusun proposal | Template proposal + bimbingan per kelompok |
| TP.9.2 | Belum bisa implementasi solusi | Tutorial tambahan tools terkait proyek |
| TP.9.3 | Belum bisa presentasi | Latihan presentasi dengan umpan balik |

---

## F. REKAP HASIL REMEDIAL

| No | Elemen | Jumlah Siswa Belum Tuntas | Jumlah Sudah Tuntas Setelah Remedial 1 | Jumlah Sudah Tuntas Setelah Remedial 2 | Keterangan |
|---|---|---|---|---|---|
| 1 | BK | | | | |
| 2 | TIK | | | | |
| 3 | SK | | | | |
| 4 | JKI | | | | |
| 5 | AD | | | | |
| 6 | AP | | | | |
| 7 | DSI | | | | |
| 8 | PLB | | | | |

---

Mengetahui,  
Kepala Sekolah

_________________________

Guru Mata Pelajaran,

{GURU}
NIP. {NIP}

_________________________
"""


# =========== 15. INVENTARIS LAB ===========
def inventaris_lab():
    return f"""# INVENTARIS LABORATORIUM KOMPUTER

**Sekolah** : _________________________
**Tahun Pelajaran** : 2026/2027
**Penanggung Jawab Lab** : _________________________

---

## A. DATA RUANG LAB

| Item | Keterangan |
|---|---|
| Nama Ruang | Laboratorium Komputer |
| Luas Ruang | ______ m² |
| Kapasitas Maksimal | ______ siswa |
| Sumber Listrik | ______ KVA |
| Koneksi Internet | ISP: ______ / Bandwidth: ______ Mbps |
| AC/Non-AC | |
| Tahun Operasional | |

---

## B. INVENTARIS PERANGKAT KERAS (HARDWARE)

| No | Nama Barang | Spesifikasi | Tahun Peroleh | Kondisi | Jumlah Baik | Jumlah Rusak | Keterangan |
|---|---|---|---|---|---|---|---|
| **Komputer Server** | | | | | | | |
| 1 | PC Server | Prosesor: ___ RAM: ___ HDD: ___ | | Baik / Rusak | | | |
| **Komputer Client** | | | | | | | |
| 1 | PC Client 1 | Prosesor: ___ RAM: ___ HDD: ___ Monitor: ___ | | Baik / Rusak | | | |
| 2 | PC Client 2 | ... | | | | | |
| 3 | PC Client ... | ... | | | | | |
| **Laptop** | | | | | | | |
| 1 | Laptop 1 | Prosesor: ___ RAM: ___ Storage: ___ | | Baik / Rusak | | | |
| **Perangkat Jaringan** | | | | | | | |
| 1 | Router | Merek: ___ Tipe: ___ | | Baik / Rusak | | | |
| 2 | Switch | Merek: ___ Port: ___ | | Baik / Rusak | | | |
| 3 | Access Point | Merek: ___ Tipe: ___ | | Baik / Rusak | | | |
| 4 | Kabel UTP | Panjang: ___ m | | | | | |
| **Perangkat Pendukung** | | | | | | | |
| 1 | Proyektor | Merek: ___ Lumens: ___ | | Baik / Rusak | | | |
| 2 | Printer | Merek: ___ Tipe: ___ | | Baik / Rusak | | | |
| 3 | Scanner | Merek: ___ | | Baik / Rusak | | | |
| 4 | Speaker Aktif | Merek: ___ Daya: ___ | | Baik / Rusak | | | |
| 5 | UPS | Merek: ___ Kapasitas: ___ | | Baik / Rusak | | | |
| 6 | Stabilizer | Merek: ___ Kapasitas: ___ | | Baik / Rusak | | | |
| 7 | Kabel Power | | | | | | |
| 8 | Kabel VGA/HDMI | | | | | | |
| **Meubelair** | | | | | | | |
| 1 | Meja Komputer | Ukuran: ___ | | Baik / Rusak | | | |
| 2 | Kursi | Tipe: ___ | | Baik / Rusak | | | |
| 3 | Lemari Penyimpanan | Ukuran: ___ | | Baik / Rusak | | | |
| 4 | Papan Tulis | Ukuran: ___ | | Baik / Rusak | | | |
| 5 | Whiteboard | Ukuran: ___ | | Baik / Rusak | | | |

---

## C. INVENTARIS PERANGKAT LUNAK (SOFTWARE)

| No | Nama Software | Jenis | Lisensi | Jumlah Lisensi | Masa Berlaku | Keterangan |
|---|---|---|---|---|---|---|
| 1 | Windows 11 Pro | OS | Original/Gratis | | | |
| 2 | Microsoft Office 2021 | Perkantoran | Original/Gratis | | | |
| 3 | Python 3.x | Pemrograman | Open Source (Gratis) | Tak terbatas | | |
| 4 | Google Chrome | Browser | Gratis | Tak terbatas | | |
| 5 | Mozilla Firefox | Browser | Gratis | Tak terbatas | | |
| 6 | Visual Studio Code | Editor | Open Source (Gratis) | Tak terbatas | | |
| 7 | Canva (edu) | Desain | Gratis Edu | | | |
| 8 | Replit (edu) | Coding | Gratis Edu | | | |
| 9 | CorelDraw | Desain | Original | | | |
| 10 | Adobe Photoshop | Desain | Original | | | |
| 11 | Antivirus | Keamanan | Original/Gratis | | | |
| 12 | Aplikasi Tambahan lain | | | | | |

---

## D. REKAPITULASI INVENTARIS

| Kategori | Jumlah Total | Baik | Rusak Ringan | Rusak Berat | Keterangan |
|---|---|---|---|---|---|
| PC Server | | | | | |
| PC Client | | | | | |
| Laptop | | | | | |
| Router | | | | | |
| Switch | | | | | |
| Access Point | | | | | |
| Proyektor | | | | | |
| Printer | | | | | |
| UPS | | | | | |
| Meja Komputer | | | | | |
| Kursi | | | | | |

---

## E. CATATAN PEMELIHARAAN (MAINTENANCE LOG)

| Tanggal | Barang | Jenis Perawatan | Keterangan | Biaya | Petugas |
|---|---|---|---|---|---|
| | | Bersihkan / Perbaiki / Upgrade / Instal Ulang | | | |
| | | | | | |
| | | | | | |

---

## F. BUKU PEMINJAMAN LAB

### F.1 Peminjaman oleh Guru

| No | Tanggal | Nama Guru | Mata Pelajaran | Kelas | Jam ke- | Kebutuhan | Tanda Tangan |
|---|---|---|---|---|---|---|---|
| 1 | | | | | | | |
| 2 | | | | | | | |

### F.2 Peminjaman oleh Siswa (di luar jam pelajaran)

| No | Tanggal | Nama Siswa | Kelas | Keperluan | Jam Pinjam | Jam Kembali | Tanda Tangan |
|---|---|---|---|---|---|---|---|
| 1 | | | | | | | |
| 2 | | | | | | | |

---

## G. LAPORAN KERUSAKAN

| No | Tanggal Lapor | Barang Rusak | Deskripsi Kerusakan | Pelapor | Status | Tanggal Selesai |
|---|---|---|---|---|---|---|
| 1 | | | | | Belum / Proses / Selesai | |
| 2 | | | | | | |

---

Mengetahui,  
Kepala Sekolah

_________________________

Guru Mata Pelajaran / Kepala Lab,

{GURU}
NIP. {NIP}

_________________________
"""


# =========== 16. JADWAL LAB & BUKU PRAKTIK ===========
def jadwal_lab():
    return f"""# JADWAL LAB & BUKU ALAT BAHAN PRAKTIK

**Sekolah** : _________________________
**Tahun Pelajaran** : 2026/2027
**Lab** : Laboratorium Komputer

---

## A. JADWAL PENGGUNAAN LAB KOMPUTER

### Semester 1 (Ganjil)

| Hari | Jam ke- | Waktu | Kelas | Mata Pelajaran | Guru | Aplikasi yang Digunakan |
|---|---|---|---|---|---|---|
| **Senin** | 1\u20132 | 07.00\u201308.30 | | | | |
| | 3\u20134 | 08.30\u201310.00 | | | | |
| | 5\u20136 | 10.30\u201312.00 | | | | |
| | 7\u20138 | 12.30\u201314.00 | | INFORMATIKA X | ______ | ______ |
| **Selasa** | 1\u20132 | 07.00\u201308.30 | | | | |
| | 3\u20134 | 08.30\u201310.00 | | | | |
| | 5\u20136 | 10.30\u201312.00 | | INFORMATIKA X | ______ | ______ |
| | 7\u20138 | 12.30\u201314.00 | | | | |
| **Rabu** | ... | | | | | |
| **Kamis** | ... | | | INFORMATIKA X | ______ | ______ |
| **Jumat** | ... | | | | | |
| **Sabtu** | \u2014 | \u2014 | \u2014 | \u2014 | \u2014 | \u2014 |

### Semester 2 (Genap)

| Hari | Jam ke- | Waktu | Kelas | Mata Pelajaran | Guru | Aplikasi yang Digunakan |
|---|---|---|---|---|---|---|
| *(sama formatnya, sesuaikan jadwal)* | | | | | | |

---

## B. ATURAN PENGGUNAAN LAB

1. Guru wajib mengisi **Buku Peminjaman Lab** sebelum menggunakan
2. Siswa dilarang membawa makanan/minuman ke dalam lab
3. Siswa wajib menggunakan sepatu (dilarang sandal)
4. Siswa dilarang mengubah pengaturan sistem (setting, instalasi, uninstall)
5. Setelah selesai, matikan komputer dengan prosedur yang benar
6. Guru wajib memastikan semua perangkat mati dan ruangan bersih sebelum meninggalkan lab
7. Kerusakan akibat kelalaian menjadi tanggung jawab pengguna
8. Jika ada kerusakan, segera laporkan ke petugas lab

---

## C. BUKU ALAT & BAHAN PRAKTIK

### C.1 Format Pencatatan

| Tanggal | Kelas | Elemen | Praktik | Alat yang Digunakan | Bahan Habis Pakai | Jumlah Siswa | Keterangan | Paraf Guru |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |

### C.2 Perkiraan Kebutuhan Alat & Bahan per Elemen

| Elemen | Praktik | Alat | Bahan Habis Pakai | Peralatan Khusus |
|---|---|---|---|---|
| **BK** | Diagram pohon dekomposisi | \u2014 | Kertas karton, spidol, sticky notes | \u2014 |
| | Flowchart & pseudocode | \u2014 | Kertas, pulpen | \u2014 |
| **TIK** | Mail merge | Komputer/lab, proyektor | \u2014 | \u2014 |
| | Spreadsheet | Komputer/lab, proyektor | \u2014 | Software: MS Excel/Google Sheets |
| | Presentasi interaktif | Komputer/lab, proyektor | \u2014 | Software: MS PowerPoint/Google Slides |
| **SK** | Identifikasi HW | Komputer (bongkar pasang) | Thermal paste (jika bongkar) | Obeng, alat buka casing |
| | Simulasi booting | Komputer/lab | \u2014 | \u2014 |
| **JKI** | Konfigurasi IP | Komputer/lab | Kabel UTP, connector RJ-45 | Crimping tools, LAN tester |
| | Enkripsi Caesar | Komputer/HP | \u2014 | \u2014 |
| **AD** | Pengolahan data | Komputer/lab | \u2014 | Software: Google Sheets |
| | Visualisasi dashboard | Komputer/lab | \u2014 | Software: Google Data Studio |
| **AP** | Coding Python | Komputer/lab | \u2014 | Python IDLE / Replit / Google Colab |
| | Debugging | Komputer/lab | \u2014 | Python IDLE |
| **DSI** | Timeline sejarah | \u2014 | Kertas karton, spidol | \u2014 |
| | Debat/diskusi | \u2014 | \u2014 | \u2014 |
| **PLB** | Pembuatan proyek | Komputer/lab | Kertas, spidol, karton | Sesuai kebutuhan proyek |
| **PLB** | Presentasi & pameran proyek Informatika | Komputer/lab, HP siswa | Bahan craft, kertas | Sesuai kebutuhan |

### C.3 Rekapitulasi Penggunaan Alat per Semester

| No | Nama Alat | Total Penggunaan | Kondisi Akhir | Perlu Perbaikan/ Penggantian? |
|---|---|---|---|---|
| 1 | Komputer Lab | | | |
| 2 | Proyektor | | | |
| 3 | Router/Switch | | | |
| 4 | Printer | | | |
| 5 | Alat Crimping | | | |
| 6 | Obeng Kit | | | |

### C.4 Laporan Kebutuhan Bahan Praktik Semester Depan

| No | Bahan | Jumlah Dibutuhkan | Estimasi Biaya | Keterangan |
|---|---|---|---|---|
| 1 | Kertas HVS | ______ rim | Rp ______ | |
| 2 | Spidol Whiteboard | ______ buah | Rp ______ | |
| 3 | Kertas Karton | ______ lembar | Rp ______ | |
| 4 | Sticky Notes | ______ pack | Rp ______ | |
| 5 | Kabel UTP | ______ meter | Rp ______ | |
| 6 | Connector RJ-45 | ______ buah | Rp ______ | |
| 7 | Thermal paste | ______ tube | Rp ______ | |
| 8 | Tinta Printer | ______ buah | Rp ______ | |

---

## D. ATURAN PRAKTIKUM INFORMATIKA

### D.1 Prosedur Sebelum Praktik
1. Berdoa sebelum memulai
2. Cek kondisi perangkat yang akan digunakan
3. Login dengan akun masing-masing
4. Baca LKPD/modul praktik dengan teliti

### D.2 Prosedur Selama Praktik
1. Ikuti langkah kerja sesuai LKPD
2. Catat hasil dan temuan selama praktik
3. Jika ada masalah/error, tanya ke guru sebelum meminta bantuan teman
4. Tidak boleh bermain game/membuka media sosial selama praktik

### D.3 Prosedur Setelah Praktik
1. Simpan file di folder yang ditentukan / upload ke Google Classroom
2. Logout dari akun
3. Matikan komputer dengan prosedur yang benar
4. Rapikan meja dan kursi
5. Kembalikan alat/bahan ke tempat semula

---

## E. DAFTAR TERTIB LAB

| No | Aturan | Sanksi Pelanggaran |
|---|---|---|
| 1 | Membawa makanan/minuman | Teguran lisan |
| 2 | Mengubah setting sistem | Membersihkan/menginstal ulang |
| 3 | Membuka situs terlarang | Peringatan + laporan wali kelas |
| 4 | Bermain game saat KBM | Teguran + tugas tambahan |
| 5 | Merusak perangkat dengan sengaja | Mengganti/ganti rugi |
| 6 | Tidak mematikan komputer | Peringatan |
| 7 | Meninggalkan lab kotor | Membersihkan lab |

---

Mengetahui,  
Kepala Sekolah

_________________________

Guru Mata Pelajaran / Kepala Lab,

{GURU}
NIP. {NIP}

_________________________
"""


# =========== MAIN ===========
def main():
    import os
    base = BASE
    files = {
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
    os.makedirs(base, exist_ok=True)
    for filename, content in files.items():
        path = os.path.join(base, filename)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Generated: {filename}")


if __name__ == "__main__":
    main()
