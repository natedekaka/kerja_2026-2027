#!/usr/bin/env python3
"""Generator Materi Ajar Informatika Kelas X — SMA Negeri 6 Cimahi."""
import os, textwrap

BASE = "/home/daniarsyah/Documents/kerja_2026-2027/administrasi_guru_kelas_X/Materi"
os.makedirs(BASE, exist_ok=True)

BAB = [
    {"id":"1","judul":"Informatika dan Keterampilan Generik","emoji":"💡","smt":1,
     "sub":[("A","Mengenal Informatika"),("B","Keterampilan Generik Abad 21"),("C","Profesi dan Karier di Bidang Informatika")]},
    {"id":"2","judul":"Berpikir Komputasional","emoji":"🧠","smt":1,
     "sub":[("A","Dasar Berpikir Komputasional"),("B","Dekomposisi dan Pengenalan Pola"),("C","Abstraksi dan Algoritma")]},
    {"id":"3","judul":"Teknologi Informasi dan Komunikasi","emoji":"💻","smt":1,
     "sub":[("A","Sejarah dan Perkembangan TIK"),("B","Perangkat TIK: Hardware, Software, Jaringan"),("C","Pemanfaatan TIK dalam Kehidupan")]},
    {"id":"4","judul":"Sistem Komputer","emoji":"⚙️","smt":1,
     "sub":[("A","Hardware: Komponen Fisik Komputer"),("B","Software: Perangkat Lunak Sistem dan Aplikasi"),("C","Sistem Operasi: Jembatan Pengguna dan Hardware")]},
    {"id":"5","judul":"Jaringan Komputer dan Internet","emoji":"🌐","smt":2,
     "sub":[("A","Dasar-Dasar Jaringan Komputer"),("B","Internet dan Cara Kerjanya"),("C","Keamanan Dasar di Dunia Maya")]},
    {"id":"6","judul":"Analisis Data","emoji":"📊","smt":2,
     "sub":[("A","Pengertian Data dan Informasi"),("B","Pengolahan Data dengan Spreadsheet"),("C","Visualisasi Data")]},
    {"id":"7","judul":"Algoritma dan Pemrograman","emoji":"🤖","smt":2,
     "sub":[("A","Logika dan Algoritma Dasar"),("B","Flowchart: Memvisualisasikan Algoritma"),("C","Pengenalan Scratch sebagai Alat Pemrograman"),("D","Proyek: Program Sederhana dengan Scratch")]},
    {"id":"8","judul":"Dampak Sosial Informatika","emoji":"🌍","smt":2,
     "sub":[("A","Dampak Positif TIK bagi Masyarakat"),("B","Dampak Negatif dan Risiko TIK"),("C","Etika Digital dan UU ITE")]},
    {"id":"9","judul":"Praktika Lintas Bidang","emoji":"🔧","smt":2,
     "sub":[("A","Kolaborasi dan Kerja Tim"),("B","Perencanaan Proyek TIK Sederhana"),("C","Presentasi dan Refleksi Proyek")]},
]


SOAL_PG = {
    "1": [
        ("Informatika adalah ilmu yang mempelajari...", ["a. cara merakit komputer", "b. pengolahan data menjadi informasi menggunakan teknologi komputer", "c. cara membuat website", "d. pemrograman saja", "e. jaringan internet"], "b"),
        ("Berikut ini yang BUKAN termasuk keterampilan generik Abad 21 adalah...", ["a. Berpikir kritis", "b. Kreativitas", "c. Menghafal tanpa memahami", "d. Kolaborasi", "e. Komunikasi"], "c"),
        ("Profesi yang bertanggung jawab mengembangkan aplikasi disebut...", ["a. Data Scientist", "b. Network Engineer", "c. Software Engineer", "d. UI/UX Designer", "e. Cyber Security Analyst"], "c"),
        ("Kemampuan memecah masalah menjadi bagian-bagian kecil disebut...", ["a. Abstraksi", "b. Algoritma", "c. Dekomposisi", "d. Pengenalan Pola", "e. Komputasi"], "c"),
        ("Teknologi yang memungkinkan benda sehari-hari terhubung ke internet disebut...", ["a. Cloud Computing", "b. Big Data", "c. IoT", "d. AI", "e. Blockchain"], "c"),
    ],
    "2": [
        ("Berpikir Komputasional adalah cara berpikir untuk...", ["a. menjadi programmer handal", "b. memecahkan masalah dengan logika dan konsep ilmu komputer", "c. menghafal kode pemrograman", "d. merakit komputer", "e. membuat game"], "b"),
        ("Memecah masalah besar menjadi bagian kecil disebut...", ["a. Abstraksi", "b. Algoritma", "c. Dekomposisi", "d. Pola", "e. Komputasi"], "c"),
        ("Mencari kesamaan dari masalah yang pernah dihadapi sebelumnya disebut...", ["a. Dekomposisi", "b. Pengenalan Pola", "c. Abstraksi", "d. Algoritma", "e. Evaluasi"], "b"),
        ("Memfilter informasi dan fokus pada yang penting disebut...", ["a. Dekomposisi", "b. Pengenalan Pola", "c. Abstraksi", "d. Algoritma", "e. Sorting"], "c"),
        ("Langkah-langkah sistematis untuk menyelesaikan masalah disebut...", ["a. Program", "b. Algoritma", "c. Abstraksi", "d. Data", "e. Komputer"], "b"),
    ],
    "3": [
        ("Alat komunikasi pertama yang menggunakan sinyal listrik untuk jarak jauh adalah...", ["a. Telepon", "b. Radio", "c. Telegraf", "d. Internet", "e. SMS"], "c"),
        ("World Wide Web (WWW) ditemukan oleh...", ["a. Bill Gates", "b. Tim Berners-Lee", "c. Mark Zuckerberg", "d. Steve Jobs", "e. Elon Musk"], "b"),
        ("Perangkat yang berfungsi memasukkan data ke komputer disebut...", ["a. Output device", "b. Storage device", "c. Input device", "d. Processing device", "e. Network device"], "c"),
        ("Berikut ini yang termasuk contoh software sistem operasi adalah...", ["a. Microsoft Word", "b. Google Chrome", "c. Windows 11", "d. Canva", "e. CapCut"], "c"),
        ("Contoh pemanfaatan TIK di bidang kesehatan adalah...", ["a. Gojek", "b. Shopee", "c. Halodoc", "d. Ruangguru", "e. TikTok"], "c"),
    ],
    "4": [
        ("Komponen komputer yang disebut sebagai 'otak' komputer adalah...", ["a. RAM", "b. Hard Disk", "c. CPU", "d. Motherboard", "e. PSU"], "c"),
        ("RAM adalah memori yang bersifat...", ["a. Permanen", "b. Sementara dan hilang saat komputer mati", "c. Tidak bisa dihapus", "d. Hanya untuk menyimpan file", "e. Sama seperti hard disk"], "b"),
        ("Perangkat lunak yang bertindak sebagai jembatan antara pengguna dan hardware adalah...", ["a. Aplikasi", "b. Browser", "c. Sistem Operasi", "d. Driver", "e. Utility"], "c"),
        ("Berikut ini yang termasuk perangkat output adalah...", ["a. Keyboard", "b. Mouse", "c. Monitor", "d. Scanner", "e. Mikrofon"], "c"),
        ("Linux adalah contoh dari...", ["a. Aplikasi perkantoran", "b. Browser", "c. Sistem Operasi", "d. Bahasa pemrograman", "e. Game"], "c"),
    ],
    "5": [
        ("Jaringan komputer yang mencakup area satu kota disebut...", ["a. PAN", "b. LAN", "c. MAN", "d. WAN", "e. CAN"], "c"),
        ("Perangkat yang mengarahkan data ke tujuan yang benar di internet adalah...", ["a. Switch", "b. Hub", "c. Router", "d. Modem", "e. Repeater"], "c"),
        ("Kepanjangan dari DNS adalah...", ["a. Domain Name System", "b. Digital Network Service", "c. Data Network Security", "d. Domain Network Server", "e. Digital Name System"], "a"),
        ("Tindakan penipuan dengan mengirim link palsu untuk mencuri data pribadi disebut...", ["a. Hacking", "b. Cracking", "c. Phishing", "d. Spamming", "e. Doxing"], "c"),
        ("Password yang PALING kuat di bawah ini adalah...", ["a. 123456", "b. password", "c. K1@$X_2026!", "d. admin", "e. kelas10"], "c"),
    ],
    "6": [
        ("Data yang sudah diolah sehingga memiliki makna disebut...", ["a. Fakta", "b. Informasi", "c. Angka", "d. File", "e. Database"], "b"),
        ("Fungsi di spreadsheet untuk menjumlahkan data adalah...", ["a. AVERAGE", "b. MAX", "c. SUM", "d. COUNT", "e. MIN"], "c"),
        ("Grafik yang paling cocok untuk melihat tren penjualan dari waktu ke waktu adalah...", ["a. Batang", "b. Garis", "c. Lingkaran", "d. Scatter", "e. Histogram"], "b"),
        ("Nilai tertinggi dari sekumpulan data bisa diketahui dengan fungsi...", ["a. MIN", "b. COUNT", "c. MAX", "d. SUM", "e. AVERAGE"], "c"),
        ("Fungsi IF di spreadsheet digunakan untuk...", ["a. Menjumlahkan data", "b. Menghitung rata-rata", "c. Membuat percabangan kondisi", "d. Mencari nilai tertinggi", "e. Menghitung jumlah data"], "c"),
    ],
    "7": [
        ("Logika AND akan menghasilkan nilai benar (true) jika...", ["a. Salah satu benar", "b. Keduanya benar", "c. Keduanya salah", "d. Minimal satu benar", "e. Tidak ada yang benar"], "b"),
        ("Flowchart adalah...", ["a. Bahasa pemrograman", "b. Diagram yang menggambarkan alur algoritma", "c. Software untuk coding", "d. Jenis komputer", "e. Alat input"], "b"),
        ("Simbol flowchart berbentuk belah ketupat digunakan untuk...", ["a. Start/End", "b. Proses", "c. Decision/kondisi", "d. Input/Output", "e. Konektor"], "c"),
        ("Scratch adalah bahasa pemrograman...", ["a. Teks tingkat tinggi", "b. Visual berbasis blok", "c. Mesin tingkat rendah", "d. Database", "e. Markup"], "b"),
        ("Blok berwarna kuning di Scratch termasuk kategori...", ["a. Motion", "b. Control", "c. Events", "d. Looks", "e. Sound"], "c"),
    ],
    "8": [
        ("Berikut adalah dampak positif TIK di bidang pendidikan...", ["a. Meningkatkan pengangguran", "b. Akses belajar dari mana saja", "c. Menyebarkan hoaks", "d. Membuat orang malas", "e. Menurunkan kreativitas"], "b"),
        ("Perundungan yang terjadi di dunia digital disebut...", ["a. Bullying", "b. Cyberbullying", "c. Phishing", "d. Stalking", "e. Doxing"], "b"),
        ("UU yang mengatur aktivitas digital di Indonesia adalah...", ["a. UU HAM", "b. UU ITE", "c. UU Pendidikan", "d. UU Ketenagakerjaan", "e. UU Lalu Lintas"], "b"),
        ("Ancaman hukuman untuk menyebarkan berita bohong (hoaks) menurut UU ITE adalah...", ["a. 2 tahun", "b. 4 tahun", "c. 6 tahun", "d. 8 tahun", "e. 10 tahun"], "c"),
        ("Hormon yang membuat kita merasa senang saat mendapat notifikasi disebut...", ["a. Serotonin", "b. Dopamin", "c. Adrenalin", "d. Endorfin", "e. Oksitosin"], "b"),
    ],
    "9": [
        ("Bekerja sama dengan orang lain untuk mencapai tujuan bersama disebut...", ["a. Kompetisi", "b. Kolaborasi", "c. Komunikasi", "d. Kreativitas", "e. Kritik"], "b"),
        ("Alat yang bisa digunakan untuk menulis dokumen bersama secara real-time adalah...", ["a. Microsoft Word", "b. Google Docs", "c. Notepad", "d. Canva", "e. Paint"], "b"),
        ("Dalam tujuan SMART, huruf S berarti...", ["a. Simple", "b. Specific", "c. Strong", "d. Strategic", "e. Smart"], "b"),
        ("Rubrik penilaian presentasi yang baik mencakup aspek berikut, KECUALI...", ["a. Konten", "b. Komunikasi", "c. Warna baju", "d. Visual", "e. Demo"], "c"),
        ("Langkah pertama dalam perencanaan proyek TIK adalah...", ["a. Membuat jadwal", "b. Menentukan ide dan masalah", "c. Membagi peran tim", "d. Membeli alat", "e. Uji coba"], "b"),
    ],
}

SOAL_URAIAN = {
    "1": [
        "Jelaskan apa yang dimaksud dengan Informatika dan berikan 3 contoh penerapannya dalam kehidupan sehari-hari!",
        "Sebutkan dan jelaskan 3 keterampilan generik Abad 21 yang paling penting menurutmu!",
        "Pilihlah satu profesi di bidang Informatika. Jelaskan tugas utamanya, skill yang dibutuhkan, dan mengapa profesi tersebut penting!",
        "Bagaimana informatika dapat membantu menyelesaikan masalah di lingkungan sekolahmu? Berikan contoh konkret!",
    ],
    "2": [
        "Jelaskan apa yang dimaksud dengan Berpikir Komputasional dan sebutkan 4 pilarnya!",
        "Berikan 2 contoh dekomposisi dalam kegiatan sehari-hari seorang pelajar!",
        "Apa perbedaan antara Abstraksi dan Algoritma? Berikan contoh masing-masing!",
        "Seorang temanmu kesulitan membagi waktu belajar untuk 5 mata pelajaran menghadapi ujian. Bantulah dia menggunakan konsep dekomposisi dan pengenalan pola!",
    ],
    "3": [
        "Jelaskan perkembangan TIK dari masa telegraf hingga era smartphone! Sebutkan 3 tonggak penting!",
        "Sebutkan dan jelaskan 3 komponen utama TIK (hardware, software, jaringan) beserta contoh masing-masing 2!",
        "Bagaimana TIK telah mengubah bidang transportasi dan perdagangan di Indonesia? Berikan contoh nyata!",
        "Menurutmu, apa dampak TIK yang paling terasa bagi pelajar di Indonesia saat ini? Jelaskan dengan contoh!",
    ],
    "4": [
        "Jelaskan fungsi masing-masing: CPU, RAM, Hard Disk/SSD, dan Motherboard dalam sistem komputer!",
        "Apa perbedaan antara software sistem dan software aplikasi? Berikan masing-masing 3 contoh!",
        "Jelaskan peran sistem operasi sebagai jembatan antara pengguna dan hardware!",
        "Apa yang dimaksud dengan GUI dan CLI? Sebutkan 2 kelebihan dan 2 kekurangan masing-masing!",
    ],
    "5": [
        "Jelaskan perbedaan antara jaringan PAN, LAN, MAN, dan WAN! Berikan contoh masing-masing!",
        "Jelaskan bagaimana cara kerja internet saat kamu mengetik www.google.com di browser hingga halaman muncul!",
        "Apa yang dimaksud dengan phishing? Jelaskan cara kerja dan 3 cara menghindarinya!",
        "Sebutkan 5 tips menjaga keamanan saat berselancar di internet yang wajib diketahui pelajar!",
    ],
    "6": [
        "Jelaskan perbedaan antara data dan informasi! Berikan 2 contoh di lingkungan sekolah!",
        "Sebutkan 4 fungsi dasar spreadsheet (SUM, AVERAGE, MAX, IF) beserta cara penulisan dan kegunaannya!",
        "Kapan sebaiknya menggunakan grafik batang, grafik garis, dan diagram lingkaran? Berikan contoh situasi!",
        "Seorang ketua OSIS ingin menyajikan data pemasukan dan pengeluaran selama satu tahun. Bantu dia menjelaskan jenis grafik apa yang cocok dan alasannya!",
    ],
    "7": [
        "Jelaskan apa yang dimaksud dengan algoritma dan sebutkan minimal 4 ciri algoritma yang baik!",
        "Buatlah flowchart sederhana untuk menentukan apakah seorang siswa lulus atau remedial (nilai >= 75 lulus)!",
        "Jelaskan perbedaan dan kegunaan blok Motion, Looks, Control, dan Events di Scratch!",
        "Buatlah algoritma dalam 8-10 langkah untuk 'Memesan tiket bioskop melalui aplikasi online'!",
    ],
    "8": [
        "Sebutkan 4 dampak positif TIK di Indonesia beserta contoh nyata masing-masing!",
        "Jelaskan apa yang dimaksud dengan 'dopamine loop' pada media sosial dan bagaimana cara menghindarinya!",
        "Sebutkan minimal 4 pasal penting dalam UU ITE beserta ancaman hukumannya!",
        "Apa yang harus kamu lakukan jika melihat temanmu mengalami cyberbullying di media sosial? Jelaskan langkah-langkahnya!",
    ],
    "9": [
        "Mengapa kolaborasi penting dalam proyek TIK? Sebutkan 3 alasan dan contoh peran dalam tim!",
        "Sebutkan dan jelaskan langkah-langkah perencanaan proyek TIK dari awal hingga akhir!",
        "Buatlah tujuan SMART untuk proyek 'Membuat konten edukasi tentang bahaya hoaks di media sosial'!",
        "Apa saja yang harus ada dalam presentasi proyek yang baik? Sebutkan struktur 5 bagian beserta durasi idealnya!",
    ],
}

GLOSARIUM = {
    "1": [
        ("Informatika", "Ilmu yang mempelajari pengolahan data menjadi informasi menggunakan teknologi komputer."),
        ("Keterampilan Generik", "Kemampuan dasar yang diperlukan di Abad 21, seperti 4C: Critical Thinking, Creativity, Collaboration, Communication."),
        ("Software Engineer", "Profesi yang merancang, mengembangkan, dan memelihara perangkat lunak."),
        ("Data Scientist", "Profesi yang menganalisis data untuk menghasilkan wawasan berharga bagi pengambilan keputusan."),
        ("Dekomposisi", "Memecah masalah besar menjadi bagian-bagian kecil yang lebih mudah dikelola."),
        ("IoT (Internet of Things)", "Teknologi yang memungkinkan benda sehari-hari terhubung ke internet dan saling bertukar data."),
        ("AI (Artificial Intelligence)", "Kecerdasan buatan — kemampuan mesin untuk meniru kecerdasan manusia."),
        ("Cloud Computing", "Teknologi yang memungkinkan penggunaan sumber daya komputasi melalui internet."),
    ],
    "2": [
        ("Berpikir Komputasional", "Cara berpikir untuk memecahkan masalah dengan menerapkan logika dan konsep ilmu komputer."),
        ("Dekomposisi", "Memecah masalah besar menjadi bagian-bagian kecil yang lebih mudah diselesaikan."),
        ("Pengenalan Pola", "Mencari kesamaan atau pola berulang dari masalah yang pernah dihadapi sebelumnya."),
        ("Abstraksi", "Memfilter informasi — fokus pada yang penting dan relevan, abaikan yang tidak perlu."),
        ("Algoritma", "Langkah-langkah sistematis untuk menyelesaikan masalah."),
        ("Logika Boolean", "Nilai benar/salah (true/false) yang menjadi dasar pengambilan keputusan dalam pemrograman."),
        ("Computational Thinking", "Istilah lain untuk Berpikir Komputasional."),
    ],
    "3": [
        ("TIK (Teknologi Informasi dan Komunikasi)", "Segala teknologi yang digunakan untuk mengolah, menyimpan, dan menyampaikan informasi."),
        ("Hardware", "Perangkat keras komputer yang bisa dilihat dan disentuh."),
        ("Software", "Perangkat lunak berupa program yang membuat hardware bisa bekerja."),
        ("Jaringan", "Sistem yang menghubungkan dua atau lebih perangkat untuk berbagi data."),
        ("WWW (World Wide Web)", "Sistem informasi global yang memungkinkan akses dokumen melalui internet."),
        ("Internet", "Jaringan global yang menghubungkan miliaran perangkat di seluruh dunia."),
        ("Sejarah TIK", "Perkembangan teknologi komunikasi dari telegraf, telepon, komputer, hingga internet."),
    ],
    "4": [
        ("CPU (Central Processing Unit)", "Otak komputer yang menjalankan semua perintah dan proses."),
        ("RAM (Random Access Memory)", "Memori sementara yang cepat tapi hilang saat komputer mati."),
        ("Storage (HDD/SSD)", "Penyimpanan permanen untuk data dan file."),
        ("Motherboard", "Papan sirkuit utama yang menghubungkan semua komponen komputer."),
        ("Sistem Operasi", "Software utama yang menjadi jembatan antara pengguna, aplikasi, dan hardware."),
        ("GUI (Graphical User Interface)", "Antarmuka pengguna berbasis grafis — ikon, menu, dan jendela."),
        ("CLI (Command Line Interface)", "Antarmuka pengguna berbasis teks — mengetik perintah."),
    ],
    "5": [
        ("Jaringan Komputer", "Dua atau lebih perangkat yang saling terhubung untuk berbagi data."),
        ("PAN (Personal Area Network)", "Jaringan pribadi dengan jangkauan sangat pendek (1-10 m)."),
        ("LAN (Local Area Network)", "Jaringan lokal dengan jangkauan satu gedung atau perumahan."),
        ("Router", "Perangkat yang mengarahkan data ke tujuan yang benar di internet."),
        ("DNS (Domain Name System)", "Sistem yang menerjemahkan nama domain menjadi IP Address."),
        ("Phishing", "Upaya penipuan dengan memancing korban memberikan data pribadi melalui link palsu."),
        ("Firewall", "Sistem keamanan yang menyaring lalu lintas data dan melindungi dari akses tidak sah."),
    ],
    "6": [
        ("Data", "Fakta mentah yang belum memiliki makna."),
        ("Informasi", "Data yang sudah diolah sehingga bermakna dan berguna untuk pengambilan keputusan."),
        ("Spreadsheet", "Aplikasi untuk mengolah data dalam tabel baris dan kolom (Excel, Google Sheets)."),
        ("Visualisasi Data", "Penyajian data dalam bentuk grafik atau diagram agar mudah dipahami."),
        ("Grafik Batang", "Grafik untuk membandingkan data antar kategori."),
        ("Grafik Garis", "Grafik untuk melihat tren perubahan data seiring waktu."),
        ("Diagram Lingkaran", "Grafik untuk menunjukkan proporsi atau persentase."),
        ("Fungsi IF", "Fungsi di spreadsheet untuk membuat percabangan kondisi (if-then-else)."),
    ],
    "7": [
        ("Algoritma", "Langkah-langkah sistematis dan logis untuk menyelesaikan masalah."),
        ("Flowchart", "Diagram yang menggambarkan alur algoritma menggunakan simbol-simbol standar."),
        ("Scratch", "Bahasa pemrograman visual berbasis blok yang dikembangkan oleh MIT."),
        ("Logika Boolean", "Sistem logika dengan dua nilai: benar (true) dan salah (false)."),
        ("Variabel", "Tempat penyimpanan data yang nilainya bisa berubah selama program berjalan."),
        ("Sprite", "Karakter atau objek dalam Scratch yang bisa diprogram."),
        ("Loop (Perulangan)", "Blok perintah yang menjalankan kode secara berulang (forever, repeat)."),
    ],
    "8": [
        ("Dampak Positif TIK", "Manfaat teknologi dalam pendidikan, kesehatan, ekonomi, dan komunikasi."),
        ("Dampak Negatif TIK", "Risiko seperti kecanduan, cyberbullying, hoaks, dan pelanggaran privasi."),
        ("Cyberbullying", "Perundungan yang terjadi di dunia digital melalui komentar, pesan, atau konten."),
        ("Hoaks", "Berita bohong atau informasi palsu yang sengaja disebarkan."),
        ("UU ITE", "Undang-Undang Informasi dan Transaksi Elektronik yang mengatur aktivitas digital."),
        ("Etika Digital", "Pedoman tentang apa yang boleh dan tidak boleh dilakukan di dunia digital."),
        ("Dopamine Loop", "Siklus kecanduan akibat pelepasan hormon dopamin saat mendapat notifikasi."),
    ],
    "9": [
        ("Kolaborasi", "Bekerja sama dengan orang lain untuk mencapai tujuan bersama."),
        ("SMART", "Kerangka kerja perencanaan tujuan: Specific, Measurable, Achievable, Relevant, Time-bound."),
        ("Presentasi", "Cara menyampaikan hasil proyek secara lisan dengan dukungan visual."),
        ("Refleksi", "Merenungkan apa yang sudah dipelajari, pengalaman, dan hal yang bisa ditingkatkan."),
        ("Timeline", "Jadwal atau garis waktu pengerjaan proyek dari awal hingga akhir."),
        ("Rubrik Penilaian", "Kriteria penilaian yang digunakan untuk mengevaluasi hasil kerja secara objektif."),
        ("Cross-functional Team", "Tim yang terdiri dari anggota dengan keahlian berbeda yang saling melengkapi."),
    ],
}

MEDIA = {
    "1": [
        ("YouTube", "Apa itu Informatika?", "https://youtu.be/...search?q=informatika+kemdikbud", "Video pengantar Informatika oleh KEMDIKBUD"),
        ("YouTube", "Kok Bisa? — Cara Kerja Komputer", "https://youtu.be/...search?q=kok+bisa+cara+kerja+komputer", "Animasi edukasi populer tentang komputer"),
        ("Website", "Karier IT di Indonesia", "https://glints.com/id/", "Informasi profesi dan gaji IT di Indonesia"),
        ("Website", "Dicoding — Belajar Coding", "https://www.dicoding.com/", "Platform belajar coding online Indonesia"),
        ("Website", "Apa itu 4C?", "https://www.kemdikbud.go.id/", "Penjelasan keterampilan Abad 21 dari Kemendikbud"),
    ],
    "2": [
        ("YouTube", "Belajar Berpikir Komputasional", "https://youtu.be/...search?q=berpikir+komputasional+kelas+10", "Video edukasi tentang 4 pilar Computational Thinking"),
        ("Simulasi", "Blockly Games", "https://blockly.games/", "Game belajar logika pemrograman visual"),
        ("YouTube", "Kok Bisa? — Berpikir Seperti Komputer", "https://youtu.be/...search?q=kok+bisa+berpikir+komputasional", "Penjelasan BK dengan animasi menarik"),
        ("Website", "Bebras Indonesia", "https://bebras.or.id/", "Tantangan berpikir komputasional untuk pelajar"),
        ("YouTube", "Apa itu Algoritma?", "https://youtu.be/...search?q=algoritma+untuk+anak+sma", "Penjelasan algoritma dengan analogi sehari-hari"),
    ],
    "3": [
        ("YouTube", "Sejarah Internet Indonesia", "https://youtu.be/...search?q=sejarah+internet+indonesia", "Video sejarah perkembangan internet di Indonesia"),
        ("YouTube", "Kok Bisa? — Internet Bisa Nyambung", "https://youtu.be/...search?q=kok+bisa+internet", "Animasi cara kerja internet dari Kok Bisa?"),
        ("Simulasi", "PhET Simulation — Internet", "https://phet.colorado.edu/in/simulations/", "Simulasi interaktif tentang jaringan dan sinyal"),
        ("Website", "Ruangguru — TIK Kelas 10", "https://www.ruangguru.com/", "Video belajar dan rangkuman TIK"),
        ("YouTube", "Sekolahmu — TIK untuk SMA", "https://youtu.be/...search?q=sekolahmu+TIK+SMA", "Pembelajaran TIK dari Sekolahmu channel"),
    ],
    "4": [
        ("YouTube", "Cara Kerja Komputer — Kok Bisa?", "https://youtu.be/...search?q=cara+kerja+komputer+kok+bisa", "Animasi tentang komponen dalam komputer"),
        ("YouTube", "Merakit PC untuk Pemula", "https://youtu.be/...search?q=merakit+PC+pemula+indonesia", "Tutorial merakit komputer oleh content creator IT Indonesia"),
        ("Simulasi", "PhET Simulation — CPU", "https://phet.colorado.edu/in/simulations/", "Simulasi tentang sirkuit dan logika dasar"),
        ("Website", "Zenius — Sistem Komputer", "https://www.zenius.net/", "Materi dan latihan soal sistem komputer"),
        ("YouTube", "Kelas IT — Sistem Operasi", "https://youtu.be/...search?q=kelas+IT+sistem+operasi", "Penjelasan fungsi dan jenis sistem operasi"),
    ],
    "5": [
        ("YouTube", "Cara Kerja Internet dalam 5 Menit", "https://youtu.be/...search?q=cara+kerja+internet+animasi", "Penjelasan internet dengan animasi"),
        ("YouTube", "Kok Bisa? — WiFi dan Jaringan", "https://youtu.be/...search?q=kok+bisa+wifi+jaringan", "Animasi edukasi tentang cara kerja jaringan nirkabel"),
        ("Simulasi", "Cisco Packet Tracer", "https://www.netacad.com/courses/packet-tracer", "Simulator jaringan untuk belajar topologi dan routing"),
        ("Website", "Daftar Phishing Terbaru", "https://www.kominfo.go.id/", "Portal Kominfo — info keamanan digital"),
        ("YouTube", "Tips Aman Internet — Kemendikbud", "https://youtu.be/...search?q=aman+di+internet+kemdikbud", "Tips keamanan digital dari Kemendikbud"),
    ],
    "6": [
        ("YouTube", "Apa itu Data vs Informasi?", "https://youtu.be/...search?q=data+dan+informasi+kelas+10", "Penjelasan perbedaan data dan informasi"),
        ("YouTube", "Belajar Google Sheets untuk Pemula", "https://youtu.be/...search?q=belajar+google+sheets+pemula", "Tutorial dasar Google Sheets dalam Bahasa Indonesia"),
        ("Simulasi", "PhET — Grafik dan Fungsi", "https://phet.colorado.edu/in/simulations/", "Simulasi untuk memahami visualisasi data dan grafik"),
        ("Website", "Google Sheets Training", "https://workspace.google.com/intl/id/training/", "Panduan resmi Google Sheets dari Google"),
        ("YouTube", "Cara Bikin Grafik di Excel", "https://youtu.be/...search?q=belajar+grafik+excel+indonesia", "Tutorial visualisasi data dengan Excel/Sheets"),
    ],
    "7": [
        ("YouTube", "Belajar Algoritma dan Flowchart", "https://youtu.be/...search?q=algoritma+dan+flowchart+indonesia", "Video belajar algoritma dasar dan flowchart"),
        ("YouTube", "Pemrograman Scratch untuk Pemula", "https://youtu.be/...search?q=tutorial+scratch+bahasa+indonesia", "Tutorial Scratch dari dasar oleh kreator Indonesia"),
        ("Simulasi", "Scratch MIT — Coba Online", "https://scratch.mit.edu/", "Platform pemrograman visual blok — gratis!"),
        ("Website", "Blockly Games", "https://blockly.games/", "Game coding visual untuk latihan logika"),
        ("YouTube", "Sekolahmu — Algoritma Pemrograman", "https://youtu.be/...search?q=sekolahmu+algoritma+pemrograman", "Materi algoritma dari Sekolahmu channel"),
    ],
    "8": [
        ("YouTube", "Kok Bisa? — Kecanduan Media Sosial", "https://youtu.be/...search?q=kok+bisa+kecanduan+medsos", "Animasi dopamine loop dan dampak media sosial"),
        ("YouTube", "UU ITE untuk Pelajar", "https://youtu.be/...search?q=UU+ITE+indonesia+edukasi", "Penjelasan pasal-pasal penting UU ITE"),
        ("Website", "Cek Fakta — Kominfo", "https://www.kominfo.go.id/", "Portal cek hoaks dan fakta dari Kominfo"),
        ("YouTube", "Sekolahmu — Etika Digital", "https://youtu.be/...search?q=sekolahmu+etika+digital", "Materi etika digital dan cyberbullying"),
        ("Website", "Stop Cyberbullying — Kemendikbud", "https://www.kemdikbud.go.id/", "Informasi pencegahan cyberbullying di sekolah"),
    ],
    "9": [
        ("YouTube", "Cara Presentasi yang Baik", "https://youtu.be/...search?q=cara+presentasi+yang+baik+pelajar", "Tips presentasi untuk pelajar SMA"),
        ("YouTube", "SMART Goals untuk Proyek", "https://youtu.be/...search?q=SMART+goals+tujuan+proyek", "Penjelasan tujuan SMART dalam perencanaan proyek"),
        ("Website", "Google Docs — Kolaborasi Online", "https://docs.google.com/", "Alat menulis dokumen bersama secara real-time"),
        ("Website", "Canva untuk Presentasi", "https://www.canva.com/", "Alat desain presentasi yang mudah digunakan"),
        ("YouTube", "Sekolahmu — Proyek TIK Kolaboratif", "https://youtu.be/...search?q=sekolahmu+proyek+TIK", "Tips mengerjakan proyek TIK bersama tim"),
    ],
}

CP_MAP = {
    "1": [
        ("Berpikir Komputasional", "Menerapkan berpikir komputasional dalam menyelesaikan persoalan sehari-hari."),
        ("Teknologi Informasi dan Komunikasi", "Mengenal teknologi informasi dan komunikasi serta penggunaannya."),
        ("Dampak Sosial Informatika", "Memahami dampak sosial dari perkembangan teknologi informasi."),
    ],
    "2": [
        ("Berpikir Komputasional", "Menerapkan dekomposisi, pengenalan pola, abstraksi, dan algoritma dalam pemecahan masalah secara terstruktur."),
    ],
    "3": [
        ("Teknologi Informasi dan Komunikasi", "Memahami sejarah, komponen, dan pemanfaatan TIK dalam berbagai bidang kehidupan."),
        ("Dampak Sosial Informatika", "Menganalisis dampak positif dan negatif TIK di masyarakat."),
    ],
    "4": [
        ("Sistem Komputer", "Memahami peran sistem operasi, komponen hardware, dan software dalam sistem komputer."),
        ("Teknologi Informasi dan Komunikasi", "Mengidentifikasi jenis-jenis perangkat lunak dan kegunaannya."),
    ],
    "5": [
        ("Jaringan Komputer dan Internet", "Memahami jenis-jenis jaringan, cara kerja internet, dan keamanan dasar di dunia maya."),
    ],
    "6": [
        ("Analisis Data", "Mengolah dan memvisualisasikan data menggunakan spreadsheet untuk mendukung pengambilan keputusan."),
    ],
    "7": [
        ("Algoritma dan Pemrograman", "Menyusun algoritma, membuat flowchart, dan mengimplementasikannya dalam bahasa pemrograman visual berbasis blok."),
        ("Berpikir Komputasional", "Menerapkan logika boolean dan struktur kontrol dalam pemrograman."),
    ],
    "8": [
        ("Dampak Sosial Informatika", "Menganalisis dampak positif dan negatif TIK serta menerapkan etika digital dan UU ITE dalam kehidupan sehari-hari."),
    ],
    "9": [
        ("Praktika Lintas Bidang", "Merencanakan, mengerjakan, dan mempresentasikan proyek TIK secara kolaboratif dengan menerapkan konsep SMART."),
        ("Dampak Sosial Informatika", "Merefleksikan dampak solusi TIK terhadap masyarakat dan lingkungan."),
    ],
}

PROYEK = {
    "1": {
        "judul": "Poster Digital: Profesi IT Masa Depan 🚀",
        "deskripsi": "Buat poster digital (Canva/PowerPoint) yang memperkenalkan 3 profesi di bidang Informatika. Setiap profesi harus mencakup: nama profesi, tugas utama, skill yang dibutuhkan, dan perkiraan gaji.",
        "alat": ["Canva / PowerPoint / Google Slides", "Akses internet untuk riset"],
        "langkah": [
            "Riset 3 profesi IT yang paling menarik menurut kamu",
            "Cari informasi tugas, skill, dan gaji dari sumber terpercaya (Glints, Dicoding, LinkedIn)",
            "Buat poster dengan layout yang rapi dan menarik secara visual",
            "Tambahkan elemen STEAM yang relevan dengan profesi tersebut",
            "Presentasikan poster di depan kelas (2 menit/orang)",
        ],
        "output": "Poster digital (.pdf/.jpg) + presentasi lisan 2 menit",
    },
    "2": {
        "judul": "Mind Map: BK dalam Kehidupan 🧠",
        "deskripsi": "Buat mind map (kertas atau Canva) yang menunjukkan bagaimana 4 pilar Berpikir Komputasional diterapkan dalam suatu aktivitas sehari-hari (misal: memasak, belanja, belajar ujian).",
        "alat": ["Kertas A3 / Canva", "Spidol warna / alat desain digital"],
        "langkah": [
            "Pilih satu aktivitas sehari-hari yang kamu kuasai",
            "Identifikasi dekomposisi: pecah aktivitas menjadi 4-5 langkah besar",
            "Cari pola berulang dalam aktivitas tersebut",
            "Tentukan informasi penting (abstraksi) dan buang yang tidak perlu",
            "Buat alur algoritma: langkah-langkah sistematis aktivitas tersebut",
            "Visualisasikan dalam mind map yang rapi dan menarik",
        ],
        "output": "Mind Map digital (.pdf/.jpg) atau fisik (difoto)",
    },
    "3": {
        "judul": "Infografis Sejarah TIK 📜",
        "deskripsi": "Buat infografis vertikal (Canva) yang menunjukkan timeline perkembangan Teknologi Informasi dan Komunikasi dari telegraf (1837) hingga era AI (2024). Sertakan 8-10 tonggak sejarah dengan ilustrasi dan deskripsi singkat.",
        "alat": ["Canva (cari template Infografis Timeline)", "Internet untuk riset gambar dan tahun"],
        "langkah": [
            "Riset 8-10 tonggak penting sejarah TIK (telegraf, telepon, komputer, internet, WWW, smartphone, AI, dll.)",
            "Urutkan berdasarkan tahun dari paling awal ke terbaru",
            "Buat infografis vertikal di Canva dengan template timeline",
            "Tambahkan ikon/ilustrasi untuk setiap tonggak sejarah",
            "Tulis deskripsi singkat (1-2 kalimat) per tonggak",
            "Cek kebenaran tahun dan fakta — jangan sampai salah sejarah!",
        ],
        "output": "Infografis vertikal (.pdf/.jpg) — ukuran A4 atau A3",
    },
    "4": {
        "judul": "Poster Anatomi Komputer 🖥️",
        "deskripsi": "Buat poster yang menampilkan komponen-komponen utama hardware komputer beserta fungsinya. Gambar atau ilustrasi komponen harus diberi label dan penjelasan singkat.",
        "alat": ["Canva / PowerPoint / Kertas gambar", "Referensi gambar komponen komputer"],
        "langkah": [
            "Identifikasi minimal 7 komponen hardware: CPU, RAM, HDD/SSD, Motherboard, PSU, GPU, dan satu komponen input/output",
            "Cari gambar referensi setiap komponen (bisa dari internet atau gambar tangan)",
            "Buat layout poster: susun komponen seperti diagram sistem komputer",
            "Beri label nama dan fungsi singkat pada setiap komponen",
            "Tambahkan panah alur data: Input → Proses → Output → Storage",
            "Buat semenarik mungkin dengan warna yang harmonis",
        ],
        "output": "Poster digital (.pdf/.jpg) atau poster fisik ukuran A3",
    },
    "5": {
        "judul": "Desain Jaringan Sekolah 🏫",
        "deskripsi": "Buat desain topologi jaringan yang ideal untuk lingkungan sekolah. Gambar menunjukkan bagaimana komputer di lab, laptop guru, server sekolah, dan koneksi internet terhubung.",
        "alat": ["Canva / draw.io / Cisco Packet Tracer / Kertas gambar", "Spidol warna / alat desain"],
        "langkah": [
            "Identifikasi perangkat yang perlu terhubung: lab komputer (20 PC), laptop guru (10), server sekolah, WiFi untuk siswa, printer jaringan",
            "Pilih topologi yang sesuai (Star direkomendasikan untuk sekolah)",
            "Gambar tata letak jaringan: router → switch → komputer/laptop/AP WiFi",
            "Beri label: alamat IP sederhana (192.168.1.x) dan nama perangkat",
            "Tambahkan legenda: router, switch, access point, kabel, server",
            "Jelaskan kelebihan topologi yang kamu pilih untuk sekolah",
        ],
        "output": "Diagram jaringan (.pdf/.jpg) + paragraf penjelasan topologi",
    },
    "6": {
        "judul": "Laporan Mini Survei 📊",
        "deskripsi": "Lakukan survei kecil kepada 10 teman tentang satu topik (misal: waktu belajar, aplikasi favorit, atau kebiasaan internet). Olah data di Google Sheets/Excel dan buat visualisasi grafik.",
        "alat": ["Google Sheets / Microsoft Excel", "Google Forms (opsional untuk survei)", "10 teman sebagai responden"],
        "langkah": [
            "Tentukan topik survei dan buat 3-4 pertanyaan sederhana",
            "Kumpulkan data dari 10 responden (teman sekelas)",
            "Masukkan data ke spreadsheet dengan rapi (baris = responden, kolom = pertanyaan)",
            "Hitung: jumlah, rata-rata, nilai tertinggi, nilai terendah menggunakan fungsi",
            "Buat minimal 2 grafik (batang dan lingkaran) dari data yang ada",
            "Tulis kesimpulan: temuan menarik apa yang kamu dapat dari survei ini?",
        ],
        "output": "File spreadsheet (.xlsx/.ods) + screenshot grafik + kesimpulan",
    },
    "7": {
        "judul": "Game Sederhana di Scratch 🎮",
        "deskripsi": "Buat game atau animasi interaktif menggunakan Scratch. Pilih salah satu: Game Tebak Angka, Kuis Interaktif, atau Animasi Cerita Pendek. Minimal menggunakan 3 kategori blok berbeda.",
        "alat": ["Scratch (https://scratch.mit.edu) — online atau offline", "Laptop/komputer dengan koneksi internet"],
        "langkah": [
            "Tentukan ide: Game Tebak Angka / Kuis Informatika / Animasi Cerita",
            "Buat flowchart sederhana alur program kamu",
            "Pilih sprite (karakter) dan backdrop (latar) yang sesuai",
            "Susun blok-blok program: events, control, motion/looks, variables",
            "Uji coba program — cari dan perbaiki bug (debugging)",
            "Tambahkan fitur tambahan: skor, timer, suara, atau level",
            "Simpan dan kumpulkan file .sb3 beserta dokumentasi",
        ],
        "output": "File Scratch (.sb3) + flowchart + dokumentasi singkat",
    },
    "8": {
        "judul": "Kampanye Digital: Bijak Bermedsos 📱",
        "deskripsi": "Buat satu konten kampanye digital (poster, flyer, atau infografis) yang mengajak teman-teman untuk bijak dalam bermedia sosial. Pilih satu tema: anti-cyberbullying, cek hoaks, atau jaga privasi.",
        "alat": ["Canva / PowerPoint", "Akses internet untuk referensi dan ilustrasi"],
        "langkah": [
            "Pilih satu tema kampanye: (a) Stop Cyberbullying, (b) Cek Hoaks Dulu, (c) Jaga Privasimu",
            "Riset fakta dan data pendukung tentang tema yang dipilih",
            "Tentukan target audiens (pelajar SMA) dan pesan utama",
            "Buat desain yang menarik perhatian — gunakan warna kontras, tipografi besar",
            "Tambahkan call-to-action (ajakan) yang jelas",
            "Siapkan 2-3 kalimat penjelasan untuk presentasi",
        ],
        "output": "Konten kampanye digital (.pdf/.jpg) + penjelasan lisan",
    },
    "9": {
        "judul": "Proposal Proyek TIK 📋",
        "deskripsi": "Buat proposal proyek TIK sederhana yang menawarkan solusi untuk satu masalah di lingkungan sekolah menggunakan teknologi. Format proposal mencakup: identitas, latar belakang, tujuan SMART, timeline, dan anggaran.",
        "alat": ["Google Docs / Microsoft Word", "Google Sheets untuk timeline dan anggaran"],
        "langkah": [
            "Identifikasi 1 masalah nyata di sekolah yang bisa dibantu teknologi (antrian, sampah, informasi jadwal, dll.)",
            "Rumuskan ide solusi TIK: aplikasi, website, poster digital, atau sistem informasi sederhana",
            "Tulis latar belakang: jelaskan masalah dan mengapa penting diselesaikan",
            "Buat tujuan SMART: Specific, Measurable, Achievable, Relevant, Time-bound",
            "Buat timeline pengerjaan (4-6 minggu) dan anggaran sederhana",
            "Identifikasi risiko dan rencana antisipasi",
        ],
        "output": "Dokumen proposal proyek (.pdf/.docx) — 2-3 halaman",
    },
}

RUBRIK = {
    "1": {
        "aspek": ["Pemahaman Konsep", "Ketepatan Informasi", "Kreativitas & Visual", "Penyajian/Presentasi"],
        "level1": ["Kurang memahami profesi IT dan tugasnya", "Informasi tidak akurat atau tidak lengkap", "Tidak ada elemen visual, hanya teks polos", "Tidak percaya diri, suara tidak jelas"],
        "level2": ["Cukup memahami, tapi penjelasan masih umum", "Informasi cukup akurat, ada 1-2 kesalahan", "Ada visual sederhana, layout cukup rapi", "Cukup jelas, kadang membaca teks"],
        "level3": ["Memahami dengan baik, mampu menjelaskan detail", "Informasi akurat, lengkap, dari sumber terpercaya", "Visual menarik, layout profesional, warna harmonis", "Percaya diri, kontak mata, penjelasan lancar"],
    },
    "2": {
        "aspek": ["Ketepatan Konsep BK", "Kelengkapan 4 Pilar", "Visual & Kerapian", "Contoh & Aplikasi"],
        "level1": ["Konsep BK tidak tepat atau salah", "Hanya mencakup 1-2 pilar", "Mind map berantakan, sulit dibaca", "Tidak ada contoh konkret"],
        "level2": ["Konsep BK cukup tepat", "Mencakup 3 dari 4 pilar", "Cukup rapi, ada struktur", "Contoh ada tapi kurang relevan"],
        "level3": ["Konsep BK tepat dan jelas", "Mencakup 4 pilar dengan baik", "Sangat rapi, menarik, mudah dipahami", "Contoh konkret dan relevan dengan kehidupan"],
    },
    "3": {
        "aspek": ["Ketepatan Sejarah", "Kelengkapan Informasi", "Visual & Timeline", "Kreativitas"],
        "level1": ["Banyak kesalahan tahun/fakta", "Kurang dari 6 tonggak sejarah", "Tidak ada urutan waktu yang jelas", "Hanya teks, tidak ada ilustrasi"],
        "level2": ["Sebagian besar tahun/fakta benar", "7-8 tonggak sejarah tercantum", "Urutan cukup jelas, desain sederhana", "Ada beberapa ilustrasi"],
        "level3": ["Semua tahun dan fakta akurat", "9-10 tonggak sejarah lengkap", "Timeline jelas, desain profesional", "Kreatif, ilustrasi menarik dan informatif"],
    },
    "4": {
        "aspek": ["Kelengkapan Komponen", "Ketepatan Fungsi", "Visual & Label", "Alur Sistem"],
        "level1": ["Kurang dari 4 komponen", "Fungsi tidak tepat atau salah", "Tidak ada label atau label salah", "Tidak menunjukkan alur data"],
        "level2": ["5-6 komponen tercantum", "Fungsi cukup tepat", "Ada label, cukup rapi", "Alur data ada tapi kurang jelas"],
        "level3": ["7+ komponen lengkap", "Fungsi tepat dan detail", "Label jelas, layout profesional", "Alur data Input→Proses→Output→Storage jelas"],
    },
    "5": {
        "aspek": ["Topologi & Kesesuaian", "Kelengkapan Perangkat", "Visual & Label", "Analisis & Justifikasi"],
        "level1": ["Topologi tidak sesuai untuk sekolah", "Perangkat tidak lengkap", "Tidak rapi, sulit dipahami", "Tidak ada penjelasan"],
        "level2": ["Topologi cukup sesuai", "Sebagian perangkat tercantum", "Cukup rapi, ada label", "Penjelasan ada tapi kurang mendalam"],
        "level3": ["Topologi sangat sesuai untuk sekolah", "Semua perangkat lengkap dengan IP", "Rapi, jelas, legenda lengkap", "Penjelasan kelebihan topologi mendalam"],
    },
    "6": {
        "aspek": ["Kualitas Data Survei", "Penggunaan Fungsi", "Visualisasi Grafik", "Analisis & Kesimpulan"],
        "level1": ["Data tidak lengkap atau < 5 responden", "Tidak menggunakan fungsi sama sekali", "Grafik tidak sesuai atau tidak ada", "Tidak ada kesimpulan"],
        "level2": ["Data cukup lengkap (5-7 responden)", "Menggunakan 2-3 fungsi dasar", "Grafik ada tapi kurang tepat jenisnya", "Kesimpulan ada tapi umum"],
        "level3": ["Data lengkap (10 responden), rapi", "Menggunakan SUM, AVERAGE, MAX, IF", "2 grafik sesuai jenis data, rapi", "Kesimpulan mendalam dan berbasis data"],
    },
    "7": {
        "aspek": ["Fungsionalitas Program", "Kompleksitas Blok", "Kreativitas & Desain", "Dokumentasi"],
        "level1": ["Program tidak berjalan", "Hanya 1-2 kategori blok", "Sprite default, tidak ada desain", "Tidak ada dokumentasi"],
        "level2": ["Program berjalan dengan bug", "3 kategori blok digunakan", "Ada modifikasi sprite/latar", "Dokumentasi minimal"],
        "level3": ["Program berjalan sempurna", "4+ kategori blok, ada variabel/logika", "Desain unik, menarik, sesuai tema", "Dokumentasi lengkap: flowchart + deskripsi"],
    },
    "8": {
        "aspek": ["Kesesuaian Tema", "Fakta & Data", "Desain & Daya Tarik", "Pesan & Ajakan"],
        "level1": ["Tema tidak jelas atau tidak sesuai", "Tidak ada fakta pendukung", "Desain membosankan, tidak menarik", "Pesan tidak sampai, tidak ada ajakan"],
        "level2": ["Tema sesuai tapi kurang fokus", "Ada fakta tapi tidak lengkap", "Desain cukup menarik", "Pesan cukup jelas, ajakan ada"],
        "level3": ["Tema jelas dan fokus", "Fakta akurat, bersumber, relevan", "Desain sangat menarik, warna kontras", "Pesan kuat, ajakan jelas dan menggerakkan"],
    },
    "9": {
        "aspek": ["Identifikasi Masalah", "Tujuan SMART", "Kelengkapan Proposal", "Ide Solusi"],
        "level1": ["Masalah tidak jelas atau tidak relevan", "Tujuan tidak SMART", "Proposal tidak lengkap", "Solusi tidak realistis"],
        "level2": ["Masalah cukup jelas", "Tujuan memenuhi 3-4 kriteria SMART", "Proposal cukup lengkap (3 komponen)", "Solusi cukup realistis"],
        "level3": ["Masalah spesifik dan relevan dengan sekolah", "Tujuan memenuhi 5 kriteria SMART", "Proposal lengkap: identitas, masalah, SMART, timeline, anggaran", "Solusi realistis, inovatif, dan aplikatif"],
    },
}

PENGAYAAN = {
    "1": [
        ("Eksplorasi Karier IT", "Kunjungi https://glints.com/id/ dan cari 3 profesi IT yang belum dibahas di kelas. Buat laporan 1 halaman tentang tugas, skill, gaji, dan prospek profesi tersebut."),
        ("Tantangan STEAM", "Pilih satu masalah di sekolahmu (sampah, antrian kantin, dll.) dan jelaskan bagaimana Informatika bisa membantu menyelesaikannya. Buat dalam format mind map atau infografis."),
    ],
    "2": [
        ("Tantangan Bebras", "Kerjakan soal-soal tantangan Bebras di https://bebras.or.id/ — pilih level SMA. Catat strategi penyelesaian dan 4 pilar BK mana yang kamu gunakan untuk setiap soal."),
        ("Algoritma di Sekitarku", "Ambil 3 aktivitas sehari-hari (misal: mencuci baju, charge HP, naik angkot). Tulis algoritma masing-masing dalam 5-7 langkah dan buat flowchart untuk salah satunya."),
    ],
    "3": [
        ("Wawancara TIK", "Wawancarai 1 orang dewasa (orang tua/guru/tetangga) tentang bagaimana TIK berubah selama hidup mereka. Tulis laporan 1 halaman: dulu vs sekarang, manfaat, dan tantangan."),
        ("Eksplorasi AI", "Coba gunakan ChatGPT (https://chatgpt.com) atau Gemini (https://gemini.google.com) untuk membantu mengerjakan tugas sekolah. Tulis refleksi: apa yang AI bisa lakukan dengan baik dan apa keterbatasannya?"),
    ],
    "4": [
        ("Riset Spesifikasi", "Cari 3 laptop/PC dengan rentang harga berbeda (5jt, 10jt, 15jt+). Bandingkan spesifikasi CPU, RAM, storage, dan GPU. Tulis rekomendasi untuk: pelajar, desainer grafis, dan gamer."),
        ("Eksplorasi OS", "Install Linux Ubuntu di VirtualBox atau coba live USB. Jelaskan perbedaan pengalaman menggunakan Linux vs Windows: tampilan, cara instal aplikasi, dan kecepatan."),
    ],
    "5": [
        ("Eksplorasi Keamanan", "Cek keamanan password kamu di https://haveibeenpwned.com/. Cari tahu apakah email atau akunmu pernah bocor. Tulis laporan: temuan dan langkah yang kamu ambil."),
        ("Simulasi Jaringan", "Coba Cisco Packet Tracer (gratis dari https://www.netacad.com/). Buat simulasi 2 PC terhubung ke switch, lalu ke router. Screenshot hasilnya dan jelaskan alur data."),
    ],
    "6": [
        ("Proyek Data Real", "Kumpulkan data nilai ujian 1 mata pelajaran dari 20 siswa (bisa minta ke guru). Hitung rata-rata, median, modus, nilai tertinggi, terendah. Buat 3 grafik berbeda dan tulis 3 temuan menarik."),
        ("Eksplorasi Big Data", "Cari artikel atau video tentang bagaimana Gojek/Shopee menggunakan data pengguna untuk meningkatkan layanan. Tulis ringkasan 1 paragraf dan jelaskan etika penggunaan data."),
    ],
    "7": [
        ("Scratch Tingkat Lanjut", "Buat game yang lebih kompleks di Scratch: game platformer (lompat rintangan) atau game shooting. Gunakan cloning, variabel global, dan message broadcasting."),
        ("Eksplorasi Python", "Coba buat program sederhana dengan Python di https://replit.com/ atau Google Colab. Program: kalkulator sederhana atau konversi suhu. Bandingkan dengan Scratch!"),
    ],
    "8": [
        ("Analisis Screen Time", "Catat waktu layar (screen time) HP-mu selama 3 hari. Analisis aplikasi mana yang paling banyak menghabiskan waktumu. Buat rencana pengurangan 20% screen time dan praktikkan."),
        ("Kampanye Nyata", "Buat konten kampanye sungguhan (bukan hanya tugas) dan posting di media sosialmu dengan hashtag #BijakBermedsos. Laporkan jumlah likes, komentar, dan dampak yang kamu rasakan."),
    ],
    "9": [
        ("Proyek Lintas Mapel", "Pilih satu masalah yang melibatkan minimal 2 mata pelajaran (misal: Fisika + Informatika untuk simulasi gerak). Buat proyek sederhana dan presentasikan di kelas."),
        ("Portofolio Digital", "Buat portofolio digital menggunakan Google Sites atau Canva Website yang menampilkan semua proyek Informatika yang pernah kamu buat semester ini. Sertakan refleksi untuk setiap proyek."),
    ],
}

RANGKUMAN = {
    "1": [
        "Informatika adalah ilmu yang mempelajari pengolahan data menjadi informasi menggunakan teknologi komputer, mencakup 5 bidang utama: BK, Pemrograman, Jaringan, Analisis Data, dan Dampak Sosial.",
        "Keterampilan generik Abad 21 (4C) meliputi Critical Thinking, Creativity, Collaboration, dan Communication — semuanya bisa diasah melalui belajar Informatika.",
        "Profesi di bidang Informatika sangat beragam: Software Engineer, Data Scientist, UI/UX Designer, Network Engineer, Cyber Security Analyst, dan masih banyak lagi dengan prospek yang cerah.",
    ],
    "2": [
        "Berpikir Komputasional adalah cara memecahkan masalah dengan menerapkan logika dan konsep ilmu komputer, terdiri dari 4 pilar: Dekomposisi, Pengenalan Pola, Abstraksi, dan Algoritma.",
        "Dekomposisi memecah masalah besar menjadi bagian kecil; Pengenalan Pola mencari kesamaan dari masalah sebelumnya; Abstraksi memfilter informasi penting; Algoritma menyusun langkah sistematis.",
        "BK bisa diterapkan di kehidupan sehari-hari seperti membereskan kamar, membuat video tugas, atau belajar ujian — bukan hanya untuk coding!",
        "Algoritma yang baik harus memiliki input, proses, output, langkah definitif, dan berhingga.",
    ],
    "3": [
        "TIK berkembang dari telegraf (1837), telepon, komputer, internet (1969), WWW (1991), hingga smartphone dan AI saat ini — setiap tahap membuat komunikasi semakin cepat.",
        "Tiga komponen utama TIK: Hardware (perangkat fisik), Software (program), dan Jaringan (koneksi antar perangkat).",
        "TIK telah mengubah berbagai bidang: pendidikan (Ruangguru), kesehatan (Halodoc), transportasi (Gojek), perdagangan (Shopee), dan perbankan (mobile banking).",
    ],
    "4": [
        "Hardware terdiri dari komponen input, proses (CPU), output, storage (HDD/SSD), dan network — semuanya bekerja sama membentuk sistem komputer.",
        "Software dibagi menjadi sistem operasi (Windows, Linux), aplikasi (Word, Chrome), dan utility (antivirus).",
        "Sistem Operasi adalah jembatan antara pengguna, aplikasi, dan hardware — fungsi utamanya mengelola CPU, memori, I/O, dan file.",
    ],
    "5": [
        "Jaringan komputer memungkinkan berbagi data dan sumber daya. Berdasarkan luas: PAN, LAN, MAN, dan WAN.",
        "Internet bekerja melalui DNS, router ISP, dan server global — data dipecah menjadi packet, dikirim, lalu dirakit kembali.",
        "Ancaman digital meliputi malware, phishing, cyberbullying, hoaks, dan hacking. Lindungi diri dengan password kuat, 2FA, dan jangan klik link sembarangan.",
    ],
    "6": [
        "Data adalah fakta mentah; Informasi adalah data yang sudah diolah sehingga bermakna dan berguna untuk pengambilan keputusan.",
        "Spreadsheet (Excel/Google Sheets) memudahkan pengolahan data dengan fungsi SUM, AVERAGE, MAX, MIN, COUNT, dan IF.",
        "Visualisasi data (grafik batang, garis, lingkaran) membuat pola dalam data lebih mudah dipahami daripada tabel angka.",
    ],
    "7": [
        "Algoritma adalah langkah-langkah sistematis untuk menyelesaikan masalah. Logika dasar meliputi AND, OR, dan NOT.",
        "Flowchart memvisualisasikan algoritma menggunakan simbol standar: terminator, proses, decision, dan input/output.",
        "Scratch adalah bahasa pemrograman visual berbasis blok dari MIT — cocok untuk pemula belajar konsep coding tanpa menulis teks.",
        "Proyek Scratch bisa berupa game kuis, game kejar-kejaran, atau animasi cerita — melatih kreativitas dan logika pemrograman.",
    ],
    "8": [
        "TIK membawa dampak positif di pendidikan, kesehatan, ekonomi, transportasi, komunikasi, dan hiburan — membuka kesempatan bagi siapa saja.",
        "Dampak negatif TIK meliputi kecanduan, cyberbullying, hoaks, pelanggaran privasi, dan penipuan online — harus diwaspadai.",
        "Etika digital dan UU ITE mengatur perilaku di dunia maya. Pelanggaran seperti pencemaran nama baik dan hoaks bisa diancam hukuman penjara.",
    ],
    "9": [
        "Kolaborasi dalam proyek TIK memungkinkan sinergi: banyak ide, pembagian tugas, saling support, dan review kesalahan.",
        "Perencanaan proyek yang baik menggunakan SMART (Specific, Measurable, Achievable, Relevant, Time-bound).",
        "Presentasi proyek harus mencakup: pembukaan, latar belakang, proses pengerjaan, demo, dan penutup — ditambah refleksi individu.",
    ],
}


def dedent(s):
    """Remove common leading whitespace from a multi-line string."""
    return textwrap.dedent(s).strip()


# ─── CONTENT GENERATORS ───────────────────────────────────────

def content_mengenal_informatika():
    return dedent("""
    ### 💡 Mengenal Informatika

    Informatika adalah ilmu yang mempelajari tentang **pengolahan data** menjadi **informasi** menggunakan **teknologi komputer**. Bidang ini mencakup cara berpikir logis, merancang sistem, dan memanfaatkan teknologi untuk menyelesaikan masalah.

    > 🧩 **Analogi:** Informatika itu seperti **dapur restoran**. Ada bahan mentah (data), ada resep (algoritma), ada koki (programmer), dan alat masak (komputer). Hasilnya adalah hidangan lezat (informasi/solusi). Kamu bisa menjadi koki (pembuat), pengunjung (pengguna), atau bahkan pemilik restoran (entrepreneur)!

    ### Ruang Lingkup Informatika

    | Bidang | Deskripsi | Contoh Karir |
    |--------|-----------|--------------|
    | **Berpikir Komputasional** | Cara memecah masalah & menyusun solusi logis | Analis sistem |
    | **Pemrograman** | Menulis kode untuk membuat aplikasi | Developer, programmer |
    | **Jaringan Komputer** | Menghubungkan komputer & internet | Network engineer |
    | **Analisis Data** | Mengolah data jadi wawasan berharga | Data analyst |
    | **Dampak Sosial** | Etika & pengaruh teknologi pada masyarakat | Konsultan digital |

    ### 🏫 Mengapa Informatika Penting?

    1. **Skill Abad 21** — Kemampuan digital adalah modal utama masa depan
    2. **Pemecahan Masalah** — Belajar berpikir sistematis dan kreatif
    3. **Peluang Karir** — Lapangan kerja TI terus bertumbuh pesat
    4. **Literasi Digital** — Jadi pengguna teknologi yang cerdas dan bijak

    ### 📌 Contoh Nyata

    Lisa, siswi SMA di Bandung, awalnya tidak tertarik dengan komputer. Setelah belajar informatika di kelas X, dia mulai suka membuat desain grafis dan belajar dasar coding. Sekarang dia aktif di ekstrakurikuler robotika dan bercita-cita menjadi **software engineer**. Semua dimulai dari satu langkah: mengenal informatika!

    ### 🔍 Cek Pemahaman
    1. Apa perbedaan utama antara data dan informasi?
    2. Sebutkan 3 dari 5 bidang utama dalam ruang lingkup Informatika!
    3. Mengapa Informatika penting dipelajari oleh semua siswa, bukan hanya yang ingin jadi programmer?

    ### 📋 Studi Kasus
    Lisa, siswi kelas X di Cimahi, awalnya mengira Informatika hanya tentang komputer dan coding. Setelah mengikuti pelajaran pertama, dia baru sadar bahwa Informatika mencakup banyak hal termasuk cara berpikir logis, menganalisis data, dan memahami dampak sosial teknologi.

    **Pertanyaan:**
    1. Menurutmu, apa kesalahpahaman paling umum tentang Informatika di kalangan siswa SMA?
    2. Bagaimana cara menjelaskan Informatika kepada temanmu yang menganggapnya sulit?

    > 🤔 **Refleksi:** Sebutkan 3 hal yang kamu bayangkan ketika mendengar kata "Informatika"? Bandingkan dengan teman sebangkumu!
    """)


def content_keterampilan_generik():
    return dedent("""
    ### 💪 Keterampilan Generik Abad 21

    Keterampilan generik adalah **kemampuan dasar** yang dibutuhkan di **segala bidang pekerjaan**, bukan cuma di dunia IT. Di abad 21, ada 4 keterampilan utama yang disebut **4C**.

    > 🧩 **Analogi:** Keterampilan generik itu seperti **obeng dan tang** — bukan alat khusus untuk satu pekerjaan, tapi bisa dipakai di banyak situasi. Kalau kamu punya obeng, kamu bisa memperbaiki mainan, memasang stop kontak, atau membuka laptop. Begitu juga 4C — berguna di mana saja!

    ### 4C: Keterampilan Abad 21

    ```
              ┌─────────────────────────────────────┐
              │      KETERAMPILAN ABAD 21 (4C)      │
              ├────────────┬────────────┬────────────┤
              │            │            │            │
            ┌─▼──┐      ┌─▼──┐      ┌─▼──┐      ┌─▼──┐
            │C1  │      │C2  │      │C3  │      │C4  │
            │Critical    │Creativity │Collaboration│Communication│
            │Thinking    │            │            │            │
            └─────┘      └─────┘      └─────┘      └─────┘
    ```

    | C | Keterampilan | Artinya | Contoh dalam Informatika |
    |---|-------------|---------|------------------------|
    | **C1** | **Critical Thinking** | Berpikir kritis & analitis | Mengecek hoaks, debugging program |
    | **C2** | **Creativity** | Kreativitas & inovasi | Mendesain tampilan aplikasi |
    | **C3** | **Collaboration** | Kolaborasi & kerja tim | Proyek kelompok membuat website |
    | **C4** | **Communication** | Komunikasi efektif | Presentasi hasil proyek |

    ### 🎯 Mengapa 4C Penting?

    Di era digital, kemampuan menghafal tidak lagi cukup — Google bisa melakukannya lebih baik. Yang dicari dunia kerja adalah **kemampuan berpikir, berkreasi, bekerja sama, dan berkomunikasi**.

    ### 📌 Contoh Nyata

    Saat mengerjakan tugas presentasi kelompok, kamu perlu:
    - **Critical Thinking** — Memilih informasi yang relevan
    - **Creativity** — Mendesain slide yang menarik di Canva
    - **Collaboration** — Membagi tugas dengan teman
    - **Communication** — Menyampaikan ide dengan jelas

    ### 🔍 Cek Pemahaman
    1. Sebutkan 4C keterampilan Abad 21 dan jelaskan masing-masing secara singkat!
    2. Mengapa kemampuan menghafal saja tidak cukup di era digital?
    3. Berikan contoh penerapan Collaboration dalam konteks tugas sekolah!

    ### 📋 Studi Kasus
    Sebuah kelompok tugas presentasi terdiri dari 5 orang. Andi ingin mengerjakan semuanya sendiri karena tidak percaya dengan anggota lain, Budi malas-malasan dan hanya menyuruh, Cici hanya mau mendesain saja, Dedi tidak berkontribusi apa-apa, dan Euis bingung harus mulai dari mana.

    **Pertanyaan:**
    1. Menurutmu, 4C mana yang kurang dalam kelompok ini?
    2. Jika kamu menjadi ketua kelompok, bagaimana cara kamu membagi tugas berdasarkan 4C?

    > 🤔 **Refleksi:** Dari 4C di atas, mana yang menurutmu paling kamu kuasai? Mana yang perlu ditingkatkan?
    """)


def content_profesi_karier():
    return dedent("""
    ### 🚀 Profesi dan Karier di Bidang Informatika

    Bidang informatika menawarkan **banyak pilihan karir** dengan prospek cerah dan gaji yang kompetitif. Semua perusahaan, dari startup hingga bank, butuh ahli IT!

    > 🧩 **Analogi:** Dunia kerja IT itu seperti **rumah sakit**. Ada dokter spesialis jantung, ada dokter gigi, ada perawat, ada apoteker — semuanya penting dan saling melengkapi. Sama seperti IT: ada programmer, desainer, network engineer, data analyst — semuanya dibutuhkan!

    ### Profesi Populer di Bidang IT

    | Profesi | Tugas Utama | Perangkat/Keterampilan |
    |---------|------------|----------------------|
    | **Software Engineer** | Membuat aplikasi/web | Python, JavaScript, Java |
    | **Frontend Developer** | Mendesain tampilan website | HTML, CSS, React |
    | **Backend Developer** | Mengelola server & database | SQL, Node.js, PHP |
    | **Data Analyst** | Menganalisis data perusahaan | Excel, SQL, Python |
    | **Network Engineer** | Mengatur jaringan & keamanan | Cisco, MikroTik |
    | **UI/UX Designer** | Mendesain pengalaman pengguna | Figma, Adobe XD |
    | **Cyber Security** | Melindungi sistem dari serangan | Ethical hacking tools |
    | **Game Developer** | Membuat game | Unity, C#, Blender |
    | **Cloud Engineer** | Mengelola infrastruktur cloud | AWS, Google Cloud |

    ### 🎓 Jalur Menuju Karir IT

    ```
       SMA (IPA/IPS) → Kuliah/Pendidikan TI
             │
             ├── S1 Informatika/Sistem Informasi/Ilmu Komputer
             ├── Bootcamp Coding (3-6 bulan)
             ├── Belajar Otodidak (YouTube, Coursera, Dicoding)
             └── Magang di Perusahaan IT
    ```

    ### 💡 Tahukah Kamu?

    Banyak tokoh IT sukses tanpa gelar sarjana:
    - **Mark Zuckerberg** (Facebook) — drop out Harvard
    - **Bill Gates** (Microsoft) — drop out Harvard
    - **Steve Jobs** (Apple) — drop out Reed College

    Tapi mereka punya satu kesamaan: **belajar coding sejak muda**.

    ### 📌 Contoh Nyata

    **Dicky**, lulusan SMK jurusan TKJ (Teknik Komputer dan Jaringan), bekerja sebagai **Network Operations Center (NOC) Engineer** di salah satu ISP besar di Bandung. Gaji pertamanya sudah UMR lebih. Dia memulai karir dari magang saat masih SMK. Bukti bahwa karir IT bisa dimulai sejak dini!

    ### 🔍 Cek Pemahaman
    1. Sebutkan 3 profesi di bidang Informatika beserta tugas utamanya!
    2. Apa perbedaan antara Frontend Developer dan Backend Developer?
    3. Apakah gelar sarjana adalah satu-satunya jalan menuju karir IT? Jelaskan!

    ### 📋 Studi Kasus
    Rina, lulusan SMA jurusan IPS, ingin bekerja di bidang IT tetapi bingung karena tidak punya latar belakang coding dari bangku sekolah. Teman-temannya berkata bahwa IT hanya untuk anak IPA.

    **Pertanyaan:**
    1. Benarkah IT hanya untuk anak IPA? Jelaskan pendapatmu!
    2. Carikan 3 alternatif jalur karir IT yang bisa ditempuh Rina tanpa harus kuliah S1 Informatika!

    > 🤔 **Refleksi:** Profesi IT mana yang paling menarik menurutmu? Cari tahu satu profesi lebih detail dan tuliskan di bukumu!
    """)


# ─── BAB 2 ─────────────────────────────────────────────────────

def content_dasar_bk():
    return dedent("""
    ### 🧠 Dasar Berpikir Komputasional

    Berpikir Komputasional (BK) adalah **cara berpikir untuk memecahkan masalah** dengan menerapkan konsep dan logika yang digunakan dalam ilmu komputer. Bukan berarti kita harus jadi komputer — tapi kita berpikir seperti seorang **computer scientist**.

    > 🧩 **Analogi:** Berpikir Komputasional itu seperti **resep masakan**. Saat kamu ingin memasak nasi goreng, kamu tidak langsung mencampur semua bahan secara asal. Kamu punya resep: langkah demi langkah, dari menyiapkan bahan hingga menyajikan. BK memberi kita **pola pikir** untuk memecahkan masalah apa pun secara terstruktur!

    ### 4 Pilar Berpikir Komputasional

    ```
              ┌──────────────────────────────────┐
              │   BERPIKIR KOMPUTASIONAL         │
              ├──────────┬──────────┬────────────┤
              │          │          │            │
            ┌─▼──┐    ┌─▼──┐    ┌─▼──┐      ┌─▼──┐
            │1.  │    │2.  │    │3.  │      │4.  │
            │Dekom-    │Pengenalan│Abstraksi  │Algoritma│
            │posisi    │Pola      │          │        │
            └─────┘    └─────┘    └─────┘    └─────┘
    ```

    ### Kenapa Perlu BK?

    1. **Universal** — Bisa diterapkan di semua bidang, bukan cuma IT
    2. **Efisien** — Membantu menemukan solusi paling efektif
    3. **Terstruktur** — Masalah besar jadi lebih mudah diselesaikan
    4. **Logis** — Melatih otak berpikir sistematis

    ### 📌 Contoh Nyata

    **Contoh: Membereskan Kamar**
    - **Dekomposisi:** Bedakan buku, pakaian, alat tulis
    - **Pola:** Buku diletakkan di rak, pakaian dilipat
    - **Abstraksi:** Fokus pada kategori saja, bukan merek barang
    - **Algoritma:** 1) Ambil buku → 2) Letakkan di rak → 3) Lipat pakaian → 4) Masukkan lemari

    ### 🔍 Cek Pemahaman
    1. Apa yang dimaksud dengan Berpikir Komputasional?
    2. Sebutkan 4 pilar utama dalam Berpikir Komputasional!
    3. Mengapa BK disebut sebagai keterampilan universal yang bisa diterapkan di semua bidang?

    ### 📋 Studi Kasus
    Seorang siswa bernama Dani sering lupa mengerjakan PR karena tidak punya jadwal belajar yang teratur. Setiap hari dia belajar asal-asalan tanpa prioritas, akibatnya banyak tugas menumpuk dan nilainya jelek.

    **Pertanyaan:**
    1. Bantu Dani menerapkan 4 pilar BK untuk menyelesaikan masalahnya!
    2. Buatkan jadwal belajar sederhana menggunakan prinsip dekomposisi!

    > 🤔 **Refleksi:** Coba ambil satu masalah sederhana di hidupmu (misal: bangun pagi, mengerjakan PR), lalu tuliskan solusinya menggunakan 4 pilar BK!
    """)


def content_dekomposisi_pola():
    return dedent("""
    ### 🔍 Dekomposisi dan Pengenalan Pola

    **Dekomposisi** adalah memecah masalah besar menjadi bagian-bagian kecil yang lebih mudah dikelola. **Pengenalan Pola** adalah mencari kesamaan atau pola berulang dari masalah-masalah yang pernah kita temui.

    > 🧩 **Analogi:** Dekomposisi itu seperti **memakan pizza**. Kamu tidak bisa langsung menelan satu pizza utuh! Kamu potong dulu jadi 8 bagian, lalu makan satu per satu. Begitu juga dengan masalah — pecah dulu jadi bagian kecil, selesaikan satu per satu.

    ### Dekomposisi dalam Praktik

    **Masalah:** Membuat video presentasi tugas sekolah

    ```
                    ┌── Cari referensi & bahan ──┐
                    │                            │
        ┌───────────┼── Tulis naskah ────────────┤
        │           │                            │
    MEMBUAT VIDEO ──┼── Rekam suara ─────────────┤
                    │                            │
                    ├── Editing video ───────────┤
                    │                            │
                    └── Upload & share ──────────┘
    ```

    ### Pengenalan Pola

    Pola adalah **kesamaan** atau **kemiripan** dari masalah yang pernah kita hadapi sebelumnya.

    | Masalah Baru | Masalah Sebelumnya | Pola yang Sama |
    |-------------|-------------------|----------------|
    | Menghitung rata-rata 10 nilai | Menghitung rata-rata 5 nilai | **Rumus:** jumlah / banyak data |
    | Login ke Gojek | Login ke Instagram | **Pola:** input user + password, klik login |
    | Chat di Discord | Chat di WhatsApp | **Pola:** tulis pesan, kirim |

    ### 📌 Contoh Nyata

    **Dekomposisi Belajar Ujian:**
    - Mata pelajaran → per bab → per sub-bab → per topik
    - Belajar 2 jam/hari: 30 menit Matematika, 30 menit Fisika, 30 menit Bahasa, 30 menit Informatika

    **Pengenalan Pola Mengerjakan Soal:**
    - Soal "Jika x = 5, hitung 2x + 3" → Pola: substitusi nilai
    - Soal serupa "Jika y = 10, hitung 3y - 2" → Pola yang sama!

    ### 🔍 Cek Pemahaman
    1. Jelaskan apa yang dimaksud dengan dekomposisi dan berikan 1 contoh!
    2. Apa yang dimaksud dengan pengenalan pola? Mengapa penting dalam pemecahan masalah?
    3. Sebutkan 3 pola yang kamu temukan dalam aktivitas menggunakan aplikasi Gojek!

    ### 📋 Studi Kasus
    Sebuah sekolah akan mengadakan acara pensi (pentas seni). Ada banyak hal yang harus dipersiapkan: panggung, sound system, bintang tamu, konsumsi, ticketing, dan dokumentasi.

    **Pertanyaan:**
    1. Gunakan konsep dekomposisi untuk memecah persiapan acara pensi menjadi bagian-bagian kecil!
    2. Pola apa yang bisa dikenali jika sekolah sudah pernah mengadakan acara serupa tahun lalu? Bagaimana pola itu membantu?

    > 🤔 **Refleksi:** Sebutkan 3 aktivitas sehari-hari yang bisa didekomposisi! Lalu cari pola dari aktivitas tersebut!
    """)


def content_abstraksi_algoritma():
    return dedent("""
    ### 🎯 Abstraksi dan Algoritma

    **Abstraksi** adalah memfilter informasi — fokus pada yang **penting dan relevan**, abaikan yang **tidak perlu**. **Algoritma** adalah **langkah-langkah sistematis** untuk menyelesaikan masalah.

    > 🧩 **Analogi:** Abstraksi itu seperti **melihat peta**. Peta tidak perlu menampilkan setiap pohon atau mobil — cukup jalan utama, gedung penting, dan nama tempat. Informasi yang tidak perlu dibuang. Sedangkan algoritma adalah **petunjuk arah** dari titik A ke titik B menggunakan peta itu.

    ### Abstraksi: Memilah yang Penting

    | Situasi | Detail Penting (Abstraksi) | Detail Tidak Penting |
    |---------|---------------------------|---------------------|
    | Membeli Gojek | Titik jemput, tujuan | Warna baju driver |
    | Memasak mie instan | Air, mie, bumbu, api | Merek panci |
    | Login akun | Username, password | Warna tombol login |
    | Memilih jurusan kuliah | Minat, prospek kerja | Warna seragam kampus |

    ### Algoritma: Langkah Sistematis

    **Ciri-ciri algoritma yang baik:**
    1. ✅ **Input** — Ada data yang dimasukkan
    2. ✅ **Proses** — Langkah yang jelas dan terbatas
    3. ✅ **Output** — Menghasilkan keluaran
    4. ✅ **Terdefinisi** — Setiap langkah jelas
    5. ✅ **Berakhir** — Tidak berjalan terus

    **Contoh Algoritma: Membuat Teh Manis**
    ```
    INPUT: air, teh celup, gula, gelas, dispenser
    PROSES:
      1. Ambil gelas
      2. Masukkan 1 kantong teh celup ke gelas
      3. Tuang air panas ke gelas (tunggu 3 menit)
      4. Angkat teh celup
      5. Masukkan 2 sendok gula
      6. Aduk rata
    OUTPUT: segelas teh manis
    ```

    ### 📌 Contoh Nyata

    **Abstraksi di Gojek:** Aplikasi Gojek hanya perlu tahu **titik jemput** dan **tujuan** kamu. Tidak perlu tahu apakah kamu pakai baju merah, apakah rambutmu panjang — itu tidak relevan.

    **Algoritma di TikTok:** Algoritma TikTok menentukan video apa yang muncul di FYP-mu berdasarkan: berapa lama kamu menonton, like, komentar, share. Ini adalah langkah-langkah logis yang dijalankan komputer!

    ### 🔍 Cek Pemahaman
    1. Apa yang dimaksud dengan abstraksi? Berikan contoh dalam penggunaan Gojek!
    2. Sebutkan 5 ciri algoritma yang baik!
    3. Mengapa abstraksi penting dalam pengembangan aplikasi?

    ### 📋 Studi Kasus
    Doni ingin membuat aplikasi sederhana untuk mencatat pengeluaran harian. la bingung harus mulai dari mana dan apa saja yang perlu dimasukkan ke dalam aplikasi. Temannya menyarankan untuk menggunakan abstraksi agar tidak terlalu rumit.

    **Pertanyaan:**
    1. Bantu Doni menentukan informasi apa saja yang PENTING (abstraksi) untuk aplikasi pencatatan pengeluaran!
    2. Buatlah algoritma dalam 6 langkah untuk "Mencatat pengeluaran harian menggunakan aplikasi"!

    > 🤔 **Refleksi:** Buatlah algoritma untuk "Membeli pulsa melalui mobile banking" dalam 5-7 langkah!
    """)


# ─── BAB 3 ─────────────────────────────────────────────────────

def content_sejarah_tik():
    return dedent("""
    ### 📜 Sejarah dan Perkembangan TIK

    Teknologi Informasi dan Komunikasi (TIK) adalah **segala teknologi yang digunakan untuk mengolah, menyimpan, dan menyampaikan informasi**.

    > 🧩 **Analogi:** Perkembangan TIK itu seperti **evolusi alat transportasi**. Dulu orang jalan kaki, lalu naik kuda, kemudian mobil, pesawat, dan sekarang bisa "bepergian" secara virtual melalui video call. Setiap fase membuat komunikasi semakin cepat dan mudah!

    ### Garis Waktu TIK

    ```
    3000 SM      1800       1900        1970       1990        2010       2024
      │           │           │           │           │           │          │
      v           v           v           v           v           v          v
    Abacus   Telegraf   Telepon   Komputer   Internet   Smartphone    AI &
                               Personal    Publik                 Cloud
    │         │         │         │         │         │          │
    │ Komunikasi via sinyal dan kabel
    │                                 │ Digital & online
    │                                          │
    │ Teknologi analog                     Teknologi digital
    ```

    ### Tonggak Sejarah TIK

    | Tahun | Peristiwa | Dampak |
    |-------|-----------|--------|
    | **~3000 SM** | Abacus (sempoa) ditemukan | Alat hitung pertama |
    | **1837** | Telegraf oleh Samuel Morse | Komunikasi jarak jauh via kabel |
    | **1876** | Telepon oleh Alexander Graham Bell | Komunikasi suara jarak jauh |
    | **1940-an** | Komputer elektronik pertama (ENIAC) | Komputer seukuran 1 ruangan |
    | **1969** | ARPANET (cikal bakal internet) | Awal mula internet |
    | **1970-an** | Mikroprosesor & PC | Komputer mulai masuk rumah |
    | **1991** | World Wide Web (WWW) oleh Tim Berners-Lee | Internet untuk semua orang |
    | **2007** | iPhone pertama | Era smartphone dimulai |
    | **2010+** | Cloud, AI, IoT, Big Data | Revolusi digital 4.0 |

    ### 📌 Contoh Nyata

    **Dari Telepon Kabel ke Smartphone:**
    Kakek-nenekmu mungkin ingat telepon rumah dengan kabel melingkar. Orangtuamu ingat Nokia 3310. Kamu punya smartphone yang 100.000x lebih kuat dari komputer NASA saat mendaratkan Apollo 11 ke bulan! Luar biasa, kan?

    ### 🔍 Cek Pemahaman
    1. Apa tonggak sejarah TIK yang terjadi pada tahun 1991?
    2. Sebutkan 3 perbedaan utama antara teknologi analog dan digital!
    3. Apa dampak penemuan mikroprosesor bagi perkembangan komputer?

    ### 📋 Studi Kasus
    Seorang kakek berusia 70 tahun bercerita bahwa dulu ia harus antre di kantor pos untuk menelepon saudaranya di luar kota. Sekarang cucunya bisa video call dengan teman di luar negeri gratis hanya dari HP.

    **Pertanyaan:**
    1. Sebutkan 3 teknologi yang membuat komunikasi berubah drastis dari zaman kakek hingga sekarang!
    2. Menurutmu, apa tantangan terbesar orang tua dalam beradaptasi dengan perkembangan TIK?

    > 🤔 **Refleksi:** Bayangkan hidup tanpa internet dan smartphone selama 1 minggu. Apa yang paling kamu rindukan?
    """)


def content_perangkat_tik():
    return dedent("""
    ### 💻 Perangkat TIK: Hardware, Software, dan Jaringan

    TIK terdiri dari tiga komponen utama yang harus saling bekerja sama agar berguna.

    > 🧩 **Analogi:** Sebuah sistem TIK itu seperti **tubuh manusia**:
    > - **Hardware** = Tulang dan otot (fisik)
    > - **Software** = Pikiran dan kesadaran (logika)
    > - **Jaringan** = Sistem saraf (koneksi)

    ### 1. Hardware (Perangkat Keras)

    | Jenis | Fungsi | Contoh |
    |-------|--------|--------|
    | **Input** | Memasukkan data | Keyboard, mouse, scanner, mikrofon |
    | **Proses** | Mengolah data | CPU, GPU, RAM |
    | **Output** | Menampilkan hasil | Monitor, speaker, printer |
    | **Storage** | Menyimpan data | Hard disk, SSD, flashdisk |
    | **Network** | Menghubungkan ke jaringan | NIC, router, modem |

    ```
         ┌──────────┐       ┌──────────┐       ┌──────────┐
         │  INPUT   │──────►│ PROCESSOR│──────►│  OUTPUT  │
         │ (Keyboard│       │  (CPU)   │       │ (Monitor)│
         │  Mouse)  │       └────┬─────┘       └──────────┘
         └──────────┘            │
                                 ▼
                          ┌──────────┐
                          │ STORAGE  │
                          │ (HDD/SSD)│
                          └──────────┘
    ```

    ### 2. Software (Perangkat Lunak)

    | Jenis Software | Fungsi | Contoh |
    |---------------|--------|--------|
    | **Sistem Operasi** | Mengelola hardware & software | Windows, macOS, Linux |
    | **Aplikasi** | Membantu tugas spesifik | Word, Excel, Chrome |
    | **Utilitas** | Memelihara sistem | Antivirus, disk cleaner |
    | **Bahasa Pemrograman** | Membuat software baru | Python, Java, Scratch |

    ### 3. Jaringan

    Menghubungkan perangkat sehingga bisa berbagi data.

    ### 📌 Contoh Nyata

    **Saat kamu main game online di HP:**
    - **Hardware:** HP-mu (CPU, RAM, layar, touchscreen)
    - **Software:** Game-nya (aplikasi), Android (OS)
    - **Jaringan:** Koneksi WiFi/data seluler ke server game

    ### 🔍 Cek Pemahaman
    1. Sebutkan 3 jenis hardware berdasarkan fungsinya beserta contoh masing-masing!
    2. Apa perbedaan antara software sistem operasi dan software aplikasi?
    3. Mengapa jaringan disebut sebagai komponen penting dalam TIK?

    ### 📋 Studi Kasus
    Di lab komputer sekolah, tiba-tiba semua komputer tidak bisa terhubung ke internet. Guru IT memeriksa dan menemukan bahwa kabel yang terhubung ke switch kendor.

    **Pertanyaan:**
    1. Komponen TIK mana yang bermasalah berdasarkan kasus di atas?
    2. Jika kamu diminta membantu, langkah apa yang akan kamu lakukan untuk mendiagnosis masalah jaringan?

    > 🤔 **Refleksi:** Sebutkan 2 contoh hardware input dan 2 contoh output yang ada di laboratorium komputer sekolahmu!
    """)


def content_pemanfaatan_tik():
    return dedent("""
    ### 🌍 Pemanfaatan TIK dalam Kehidupan

    TIK telah mengubah hampir semua aspek kehidupan kita. Mari lihat bagaimana TIK digunakan di berbagai bidang!

    > 🧩 **Analogi:** TIK itu seperti **listrik** di era modern. Dulu listrik mengubah segalanya — lampu ganti lilin, kulkas ganti es batu. Sekarang TIK (internet, smartphone, AI) mengubah cara kita hidup dengan cara yang sama fundamentalnya.

    ### Pemanfaatan TIK di Berbagai Bidang

    | Bidang | Sebelum TIK | Sesudah TIK | Contoh di Indonesia |
    |--------|-------------|-------------|-------------------|
    | **Pendidikan** | Belajar di kelas, buku cetak | Belajar online, e-book, video | Ruangguru, Google Classroom |
    | **Kesehatan** | Antre di puskesmas, rekam medis kertas | Telemedicine, rekam medis digital | Halodoc, Alodokter |
    | **Transportasi** | Angkot, taksi panggil manual | Ojek online, tracking real-time | Gojek, Grab |
    | **Perdagangan** | Belanja ke pasar/toko | E-commerce, kurir 1 hari | Shopee, Tokopedia |
    | **Perbankan** | Ke bank, buku tabungan | Mobile banking, QRIS | BCA mobile, GoPay |
    | **Hiburan** | TV, radio, majalah | Streaming, YouTube, TikTok | Netflix, Spotify |
    | **Pemerintahan** | Urus dokumen ke kantor | Layanan online | INAruang, e-KTP |

    ### Manfaat TIK bagi Pelajar

    1. 📚 **Akses ilmu tanpa batas** — YouTube, Wikipedia, Khan Academy
    2. ✍️ **Tugas lebih mudah** — Google Docs, Canva, presentasi digital
    3. 🤝 **Kolaborasi jarak jauh** — Google Meet, Zoom, Discord
    4. 🎮 **Belajar sambil bermain** — Quizizz, Kahoot, game edukasi
    5. 🎯 **Bakat tersalurkan** — Konten kreator, desainer, programmer muda

    ### 📌 Contoh Nyata

    **Revitalisasi** — Seorang petani di desa bisa mengetahui harga pasar terkini dari HP-nya. Penjual pisang goreng bisa menerima pembayaran QRIS. Siswa di pelosok bisa belajar dari guru terbaik lewat YouTube. **TIK meratakan kesempatan!**

    ### 🔍 Cek Pemahaman
    1. Sebutkan 3 bidang yang telah diubah oleh TIK beserta contohnya di Indonesia!
    2. Bagaimana TIK membantu petani di desa mendapatkan harga pasar yang adil?
    3. Sebutkan 3 manfaat TIK bagi pelajar yang paling kamu rasakan!

    ### 📋 Studi Kasus
    Bu Siti memiliki warung kelontong di depan sekolah. Sejak anaknya mengajarkan cara menggunakan QRIS dan GoFood Merchant, omzetnya naik 2 kali lipat. Namun Bu Siti juga khawatir dengan penipuan online.

    **Pertanyaan:**
    1. Teknologi apa saja yang dimanfaatkan Bu Siti untuk mengembangkan usahanya?
    2. Saran apa yang akan kamu berikan kepada Bu Siti agar aman bertransaksi digital?

    > 🤔 **Refleksi:** Sebutkan 3 aplikasi favoritmu. Bagaimana ketiganya memanfaatkan TIK untuk membantu hidupmu?
    """)


# ─── BAB 4 ─────────────────────────────────────────────────────

def content_hardware():
    return dedent("""
    ### ⚙️ Hardware: Komponen Fisik Komputer

    Hardware adalah semua bagian komputer yang **bisa dilihat dan disentuh**. Ibarat tubuh manusia, hardware adalah **anggota badan** — fisik yang bisa diraba.

    > 🧩 **Analogi:** Hardware itu seperti **dapur**. Ada kompor (CPU), wajan (motherboard), pisau (mouse/keyboard), talenan (RAM), lemari es (hard disk), dan piring (monitor). Semua alat fisik yang diperlukan untuk memasak.

    ### Komponen Utama Hardware

    ```
                     ┌──────────────────────┐
                     │      MONITOR         │
                     │   (Output Visual)    │
                     └──────────┬───────────┘
                                │
          ┌─────────────────────┼─────────────────────┐
          │                     │                     │
          ▼                     ▼                     ▼
    ┌──────────┐         ┌──────────┐         ┌──────────┐
    │ KEYBOARD ├────────►│   CPU    │◄────────│  MOUSE   │
    │ (Input)  │         │  (Otak)  │         │ (Input)  │
    └──────────┘         └────┬─────┘         └──────────┘
                              │
          ┌───────────────────┼────────────────────┐
          │                   │                    │
          ▼                   ▼                    ▼
    ┌──────────┐        ┌──────────┐        ┌──────────┐
    │   RAM    │        │  HDD/SSD │        │  SPEAKER │
    │ Memori   │        │ Storage  │        │ Output   │
    │ Sementara│        │ Permanen │        │ Audio    │
    └──────────┘        └──────────┘        └──────────┘
    ```

    ### Tabel Komponen dan Fungsinya

    | Komponen | Fungsi | Analogi |
    |----------|--------|---------|
    | **CPU** (Prosesor) | Otak komputer — menjalankan perintah | Manajer yang memberi instruksi |
    | **RAM** | Memori sementara, cepat tapi hilang saat mati | Meja kerja sementara |
    | **Hard Disk / SSD** | Penyimpanan permanen, lambat tapi awet | Lemari arsip |
    | **Motherboard** | Papan sirkuit utama penghubung semua komponen | Kerangka tubuh |
    | **Power Supply (PSU)** | Sumber listrik | Jantung yang pompa darah (listrik) |
    | **GPU / VGA Card** | Mengolah grafis / tampilan | Pelukis digital |

    ### CPU: Otak Komputer

    ```
    ┌─────────────────────────────────┐
    │     PROSESOR (CPU)              │
    │  ┌─────┐  ┌─────┐  ┌─────┐    │
    │  │ ALU │  │ CU  │  │ Cache│    │
    │  └─────┘  └─────┘  └─────┘    │
    │  • ALU = Arithmetic Logic Unit  │
    │  • CU = Control Unit            │
    │  • Cache = Memori super cepat   │
    └─────────────────────────────────┘
    ```

    ### 📌 Contoh Nyata

    Spek komputer lab sekolah biasanya: **Intel Core i3 / RAM 4 GB / SSD 256 GB**. Cukup untuk belajar Microsoft Office, browsing, dan coding dasar. Kalau mau gaming atau editing video berat, butuh spek lebih tinggi (i5/i7, RAM 16GB, GPU dedicated).

    ### 🔍 Cek Pemahaman
    1. Sebutkan 5 komponen utama hardware dan fungsinya masing-masing!
    2. Apa perbedaan antara RAM dan Hard Disk/SSD?
    3. Jelaskan fungsi ALU dan CU dalam prosesor!

    ### 📋 Studi Kasus
    Andi ingin membeli laptop untuk belajar dan desain grafis. Temannya menyarankan laptop dengan RAM 4 GB dan prosesor i3, tapi Andi juga lihat laptop lain dengan RAM 8 GB dan prosesor i5 harganya lebih mahal 2 juta.

    **Pertanyaan:**
    1. Komponen hardware mana yang paling penting untuk kebutuhan desain grafis?
    2. Berdasarkan spek yang berbeda, laptop mana yang sebaiknya dipilih Andi? Jelaskan alasannya!

    > 🤔 **Refleksi:** Coba lihat spek HP atau komputermu! Berapa GHz prosesornya? Berapa GB RAM-nya? Catat dan bandingkan dengan temanmu!
    """)


def content_software():
    return dedent("""
    ### 💿 Software: Perangkat Lunak Sistem dan Aplikasi

    Software adalah **program dan data** yang membuat hardware bisa bekerja. Software **tidak bisa disentuh** — dia adalah instruksi logis yang dijalankan komputer.

    > 🧩 **Analogi:** Hardware adalah **piano**, software adalah **lembaran musik**. Piano tanpa lembaran musik hanya benda mati. Lembaran musik tanpa piano tidak bisa dimainkan. Keduanya harus bersatu agar tercipta musik yang indah!

    ### Jenis-Jenis Software

    ```
                    ┌──────────────────────────────┐
                    │       SOFTWARE               │
                    ├────────────────────┬─────────┤
                    │                    │         │
              ┌─────▼──────┐      ┌─────▼──────┐  │
              │  SISTEM OS  │      │  APLIKASI  │  │
              │  (OS)       │      │            │  │
              │  Windows    │      │  Word      │  │
              │  Linux      │      │  Chrome    │  │
              │  macOS      │      │  Canva     │  │
              │  Android    │      │  Scratch   │  │
              └─────────────┘      └────────────┘  │
                    │                               │
              ┌─────▼──────┐                       │
              │  UTILITY   │                       │
              │  Antivirus │                       │
              │  Cleaner   │                       │
              └────────────┘                       │
                    └──────────────────────────────┘
    ```

    ### Perbandingan Software Sistem vs Aplikasi

    | Aspek | Software Sistem | Software Aplikasi |
    |-------|----------------|-------------------|
    | **Tujuan** | Mengelola hardware & software lain | Membantu tugas spesifik pengguna |
    | **Pengguna** | Sistem (otomatis) | Langsung oleh user |
    | **Contoh** | Windows 11, Android 14 | Word, Excel, Chrome, CapCut |
    | **Tanpa OS?** | OS diperlukan agar aplikasi jalan | Tidak bisa jalan tanpa OS |

    ### Software Aplikasi Populer

    | Kategori | Contoh | Fungsi |
    |----------|--------|--------|
    | **Office** | Microsoft Office, Google Docs | Menulis, spreadsheet, presentasi |
    | **Browser** | Chrome, Firefox, Edge | Berselancar di internet |
    | **Desain** | Canva, Figma, CorelDRAW | Membuat desain grafis |
    | **Editing** | CapCut, Kdenlive, Photoshop | Edit video, foto |
    | **Komunikasi** | WhatsApp, Discord, Zoom | Chat, video call |
    | **Pendidikan** | Google Classroom, Quizizz | Belajar dan tugas |

    ### 📌 Contoh Nyata

    **Saat kamu membuat laporan:**
    - **Sistem Operasi:** Windows 11 menyalakan laptop
    - **Aplikasi:** Microsoft Word untuk menulis
    - **Browser:** Chrome untuk mencari referensi
    - **Cloud:** Google Drive untuk menyimpan & share

    ### 🔍 Cek Pemahaman
    1. Jelaskan perbedaan software sistem dan software aplikasi!
    2. Sebutkan 3 contoh software aplikasi untuk desain grafis!
    3. Mengapa software aplikasi tidak bisa berjalan tanpa sistem operasi?

    ### 📋 Studi Kasus
    Seorang siswa menginstal 3 sistem operasi berbeda di satu laptop (Windows, Linux, dan macOS) untuk tugas sekolahnya. Dia bingung mengapa beberapa aplikasi Word dan Excel tidak bisa jalan di Linux.

    **Pertanyaan:**
    1. Mengapa aplikasi tertentu hanya bisa berjalan di sistem operasi tertentu?
    2. Menurutmu, sistem operasi apa yang paling cocok untuk seorang pelajar? Jelaskan alasannya!

    > 🤔 **Refleksi:** Sebutkan 5 aplikasi yang paling sering kamu pakai dalam sehari! Kategorikan sebagai sistem atau aplikasi!
    """)


def content_sistem_operasi():
    return dedent("""
    ### 🔗 Sistem Operasi: Jembatan Pengguna dan Hardware

    Sistem Operasi (OS) adalah **software paling penting** di komputer. Dia menjadi jembatan antara pengguna (kamu), aplikasi, dan hardware.

    > 🧩 **Analogi:** Sistem Operasi itu seperti **resepsionis** di hotel besar. Kamu (pengguna) datang dan minta sesuatu (buka file, buka browser). Resepsionis (OS) yang mengatur siapa yang melakukan apa — menyuruh petugas kebersihan, bellboy, atau teknisi (hardware) untuk bekerja. Kamu tidak perlu langsung ngomong ke petugasnya!

    ### Fungsi Utama Sistem Operasi

    ```
       ┌──────────────────────────────────────────┐
       │            PENGGUNA (USER)               │
       ├──────────────────────────────────────────┤
       │   APLIKASI: Word, Chrome, Game, Canva    │
       ├──────────────────────────────────────────┤
       │     SISTEM OPERASI (Windows/Linux)        │
       │   ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐  │
       │   │CPU   │ │Memory│ │I/O   │ │File  │  │
       │   │Mgmt  │ │Mgmt  │ │Mgmt  │ │Mgmt  │  │
       │   └──────┘ └──────┘ └──────┘ └──────┘  │
       ├──────────────────────────────────────────┤
       │           HARDWARE (CPU, RAM, dll)        │
       └──────────────────────────────────────────┘
    ```

    ### Sistem Operasi Populer

    | OS | Developer | Perangkat | UI | Kelebihan |
    |----|-----------|-----------|-----|-----------|
    | **Windows 11** | Microsoft | PC, Laptop | GUI | Banyak software, mudah dipakai |
    | **macOS** | Apple | MacBook, iMac | GUI | Desain premium, stabil |
    | **Linux (Ubuntu)** | Open-source | PC, Server | GUI/CLI | Gratis, ringan, aman |
    | **Android** | Google | Smartphone | Touch | Paling populer di HP |
    | **iOS** | Apple | iPhone, iPad | Touch | Keamanan, ekosistem Apple |

    ### CLI vs GUI

    ```
    ┌──────────────────┐    ┌──────────────────┐
    │      CLI         │    │      GUI         │
    │ (Command Line)   │    │ (Graphical)      │
    │                  │    │                  │
    │ $ ls -la         │    │  ╔══╗  ┌──┐     │
    │ $ cd Documents   │    │  ║  ║  │  │     │
    │ $ mkdir Tugas    │    │  ╚══╝  └──┘     │
    │ $ python run.py  │    │  Klik, drag,     │
    │                  │    │  visual          │
    │ Cepat, hemat     │    │ Mudah, ramah     │
    │ resource         │    │ pengguna         │
    └──────────────────┘    └──────────────────┘
    ```

    ### 📌 Contoh Nyata

    **Boot process:** Saat kamu tekan tombol power laptop:
    1. PSU memberi listrik ke motherboard
    2. BIOS/UEFI melakukan pengecekan hardware (POST)
    3. BIOS mencari bootloader di SSD/HDD
    4. Bootloader memuat Windows/Linux ke RAM
    5. Kamu lihat layar login — **selesai booting!**

    ### 🔍 Cek Pemahaman
    1. Sebutkan 4 fungsi utama sistem operasi!
    2. Apa perbedaan antara CLI dan GUI? Sebutkan kelebihan masing-masing!
    3. Sebutkan 3 sistem operasi populer beserta perangkat yang menggunakannya!

    ### 📋 Studi Kasus
    Laptop seorang siswa tiba-tiba muncul layar biru (Blue Screen of Death) saat sedang mengerjakan tugas. Semua file yang belum disimpan hilang.

    **Pertanyaan:**
    1. Jelaskan apa yang mungkin terjadi pada sistem operasi berdasarkan gejala di atas!
    2. Apa yang seharusnya dilakukan siswa tersebut untuk mencegah kejadian serupa di masa depan?

    > 🤔 **Refleksi:** OS apa yang kamu pakai di HP dan laptop? Sebutkan 3 kelebihan dan 3 kekurangan yang kamu rasakan!
    """)


# ─── BAB 5 ─────────────────────────────────────────────────────

def content_dasar_jaringan():
    return dedent("""
    ### 🌐 Dasar-Dasar Jaringan Komputer

    Jaringan komputer adalah **dua atau lebih komputer yang saling terhubung** untuk berbagi data dan sumber daya.

    > 🧩 **Analogi:** Jaringan komputer itu seperti **sistem pos**. Setiap komputer adalah sebuah rumah. Alamat rumah adalah IP Address. Tukang pos yang mengantarkan surat adalah data packet. Dan jalan yang menghubungkan rumah-rumah adalah kabel atau sinyal WiFi. **Internet adalah sistem pos seluruh dunia!**

    ### Manfaat Jaringan

    1. 📂 **Berbagi file** — Kirim data tanpa flashdisk
    2. 🖨️ **Berbagi printer** — Satu printer untuk banyak komputer
    3. 🌍 **Akses internet** — Terhubung ke seluruh dunia
    4. 💬 **Komunikasi** — Email, chat, video call
    5. ☁️ **Penyimpanan cloud** — Data bisa diakses di mana saja

    ### Jenis Jaringan Berdasarkan Luas

    | Jenis | Luas | Contoh | Ilustrasi |
    |-------|------|--------|-----------|
    | **PAN** (Personal) | 1-10 m | Bluetooth HP ke speaker | Satu kamar |
    | **LAN** (Local) | 10-1000 m | Lab komputer sekolah | Satu perumahan |
    | **MAN** (Metropolitan) | 10-50 km | WiFi seluruh kota | Satu kecamatan |
    | **WAN** (Wide) | >100 km | Internet global | Seluruh dunia |

    ### Topologi Jaringan

    ```
    Topologi Bus:                Topologi Star:
        ┌──┐  ┌──┐  ┌──┐          ┌──┐
        │PC│  │PC│  │PC│          │PC│
        └┬─┘  └┬─┘  └┬─┘          └┬─┘
         └─────┴──────┘            │
    ══════════════════════     ┌────┴────┐
                              │ SWITCH  │
    Topologi Ring:             ├─────────┤
      ┌──┐                    │ ─── ─── │
    ┌─│PC│                    │ PC  PC  │
    │ └──┘                    └─────────┘
    │  │
    └──┴──┐
       ┌──┐
       │PC│
       └──┘
    ```

    ### 📌 Contoh Nyata

    Di lab komputer sekolahmu, biasanya menggunakan **topologi Star**: setiap komputer terhubung ke satu **switch**, dan switch terhubung ke **router** yang menyediakan internet. Jika satu komputer mati, yang lain tidak terpengaruh.

    ### 🔍 Cek Pemahaman
    1. Sebutkan 4 jenis jaringan berdasarkan luas area beserta cakupannya!
    2. Apa perbedaan antara topologi Bus, Star, dan Ring?
    3. Sebutkan 3 manfaat jaringan komputer di lingkungan sekolah!

    ### 📋 Studi Kasus
    Di lab komputer sekolah terdapat 20 komputer yang semuanya mati saat satu komputer dimatikan. Ternyata masalahnya ada di kabel utama yang putus.

    **Pertanyaan:**
    1. Topologi jaringan apa yang paling mungkin digunakan berdasarkan gejala tersebut?
    2. Topologi apa yang lebih baik untuk lab komputer? Mengapa?

    > 🤔 **Refleksi:** Coba lihat sekeliling ruang kelas/lab komputer. Bagaimana kira-kira topologi jaringannya?
    """)


def content_internet():
    return dedent("""
    ### 🌍 Internet dan Cara Kerjanya

    Internet adalah **jaringan global** yang menghubungkan miliaran perangkat di seluruh dunia. Internet memungkinkan kita **mengakses informasi**, **berkomunikasi**, dan **bertransaksi** tanpa batas geografis.

    > 🧩 **Analogi:** Internet itu seperti **jalan tol global**. Setiap situs web adalah **kota**. Google adalah **papan petunjuk** yang memberitahu lokasi kota. Data yang bepergian adalah **mobil-mobil** yang melaju di jalan tol. Protokol TCP/IP adalah **aturan lalu lintas** yang memastikan semua mobil sampai dengan selamat.

    ### Bagaimana Internet Bekerja?

    ```
      Kamu ketik: www.google.com
           │
           ▼
      [DNS Server]  ── "Google? IP-nya 142.250.64.78"
           │
           ▼
      [Router ISP]  ── Menemukan rute tercepat
           │
           ▼
      [Router Global] ── Melompat dari router ke router
           │
           ▼
      [Server Google] ── "Halaman HTML siap dikirim!"
           │
           ▼
      Browser menampilkan Google.com ✅
    ```

    ### Komponen Internet

    | Komponen | Fungsi | Analogi |
    |----------|--------|---------|
    | **Server** | Komputer yang menyimpan website/data | Toko penyedia barang |
    | **Client** | Perangkat kita (HP/laptop) | Pembeli |
    | **ISP** | Penyedia layanan internet | Jalan tol & gerbang |
    | **Router** | Mengarahkan data ke tujuan | Simpang jalan & rambu |
    | **DNS** | Menerjemahkan nama jadi IP | Buku telepon raksasa |
    | **Domain** | Alamat website (google.com) | Nama toko |
    | **IP Address** | Alamat unik perangkat | Koordinat GPS |

    ### TCP/IP: Aturan Lalu Lintas Internet

    ```
       ┌──────────┐     ┌──────────┐     ┌──────────┐
       │   DATA   │────►│ DI-PECAH │────►│ DIBERI   │
       │ (File)   │     │ (Packet) │     │ ALAMAT   │
       └──────────┘     └──────────┘     └────┬─────┘
                                               │
                                               ▼
       ┌──────────┐     ┌──────────┐     ┌──────────┐
       │ DITAMPILKAN│◄───│ DI-RAKIT │◄────│ DIKIRIM  │
       │ (Hasil)   │     │ (Packet) │     │ (Route)  │
       └──────────┘     └──────────┘     └──────────┘
    ```

    ### 📌 Contoh Nyata

    Saat kamu nonton YouTube, **data video tidak dikirim utuh**. Video dipecah menjadi ribuan packet kecil, masing-masing mencari rute tercepat ke HP-mu. Kadang ada packet yang datang terlambat atau hilang — itulah yang menyebabkan video **buffering**! YouTube akan meminta ulang packet yang hilang.

    ### 🔍 Cek Pemahaman
    1. Jelaskan peran DNS, Router, dan ISP dalam proses mengakses website!
    2. Apa yang dimaksud dengan TCP/IP dan bagaimana cara kerjanya?
    3. Apa yang menyebabkan video buffering saat menonton YouTube?

    ### 📋 Studi Kasus
    Budi sedang mengerjakan ujian online di rumah menggunakan Zoom. Tiba-tiba koneksi internetnya sangat lambat. la melihat ada 5 perangkat yang terhubung ke WiFi rumah: HP ayah, HP ibu, laptop kakak, TV pintar, dan PlayStation.

    **Pertanyaan:**
    1. Faktor apa saja yang menyebabkan koneksi Budi lambat?
    2. Apa saranmu agar koneksi Budi stabil saat ujian?

    > 🤔 **Refleksi:** Pernah mengalami internet lambat saat Zoom atau main game? Kira-kira apa penyebabnya? Diskusikan dengan teman!
    """)


def content_keamanan_dunia_maya():
    return dedent("""
    ### 🔒 Keamanan Dasar di Dunia Maya

    Dunia maya (cyberspace) tidak selalu aman. Sama seperti di dunia nyata ada penjahat, di internet juga ada **ancaman digital** yang perlu kamu waspadai.

    > 🧩 **Analogi:** Keamanan internet itu seperti **mengunci rumah**. Kamu tidak akan meninggalkan rumah dalam keadaan pintu terbuka lebar, kan? Di internet, password adalah kuncinya, antivirus adalah satpamnya, dan dirimu sendiri adalah pemilik rumah yang harus waspada!

    ### Ancaman Digital yang Umum

    | Ancaman | Penjelasan | Analogi |
    |---------|-----------|---------|
    | **Malware** | Virus, trojan, ransomware yang merusak sistem | Pencuri yang masuk rumah |
    | **Phishing** | Pancingan untuk mencuri data pribadi | Orang mengaku bank, padahal penipu |
    | **Cyberbullying** | Perundungan di dunia digital | Perundungan di sekolah — tapi online |
    | **Hoaks** | Berita bohong | Gosip yang sengaja dibuat |
    | **Doxing** | Menyebarkan data pribadi orang | Memajang KTP orang di publik |
    | **Hacking** | Membobol akun orang | Mendobrak pintu rumah orang |

    ### Tips Aman di Internet 🛡️

    ```
      🔑  Password KUAT & BERBEDA untuk tiap akun!
          ❌ password123, nama, tanggal lahir
          ✅ G4nT3ng!2026_KlsX (min 8 karakter, campur huruf besar/kecil/angka/simbol)

      🔐  Aktifkan 2FA (Otentikasi 2 Faktor)
          Password + kode via SMS/Google Authenticator

      ❓  Jangan Klik Link Sembarangan!
          Cek URL sebelum klik — "g00gle.com" ≠ "google.com"

      📱  Jaga Data Pribadi
          Jangan sembarangan posting: alamat rumah, nomor HP, KTP

      🛑  STOP — THINK — CONNECT
          Berhenti, pikir dulu, baru terhubung!
    ```

    ### Cara Membuat Password Kuat

    | ❌ Lemah | ⚠️ Sedang | ✅ Kuat |
    |----------|-----------|---------|
    | `123456` | `kelas10` | `K1@$X_2026!` |
    | `password` | `sekolahku` | `B4ndung#Smkn6` |
    | `admin` | `jokowi` | `L!ndungi_AkunMu` |

    ### 📌 Contoh Nyata

    **Kasus:** Seorang siswa mendapat email yang mengatakan "Akun Google-mu akan dihapus! Klik link ini untuk menyelamatkan akun." Link-nya mirip google.com tapi sebenarnya **g00gle.com** (angka 0). Dia panik dan mengklik, lalu mengisi email dan password — **AKUN-NYA DICURI!**

    Ini adalah **phishing**. Selalu cek URL dengan saksama dan jangan panik!

    ### 🔍 Cek Pemahaman
    1. Sebutkan 3 jenis ancaman digital beserta penjelasan singkatnya!
    2. Apa itu phishing? Berikan contoh cara kerjanya!
    3. Sebutkan 3 karakteristik password yang kuat!

    ### 📋 Studi Kasus
    Sinta menerima pesan di WhatsApp dari nomor tidak dikenal yang mengaku sebagai operator sekolah. Pesan itu berisi link untuk mengisi data penerima bantuan siswa miskin dan meminta nomor rekening serta password akun sekolah.

    **Pertanyaan:**
    1. Termasuk ancaman apakah pesan yang diterima Sinta? Jelaskan!
    2. Apa yang harus dilakukan Sinta? Tuliskan langkah-langkahnya!

    > 🤔 **Refleksi:** Apakah kamu pakai password yang sama untuk semua akun? Kalau iya, apa risikonya? Diskusikan dengan temanmu!
    """)


# ─── BAB 6 ─────────────────────────────────────────────────────

def content_data_informasi():
    return dedent("""
    ### 📊 Pengertian Data dan Informasi

    **Data** adalah fakta mentah yang belum memiliki makna. **Informasi** adalah data yang sudah diolah sehingga bermakna dan berguna.

    > 🧩 **Analogi:** Data itu seperti **biji kopi** — masih mentah, belum bisa dinikmati. Informasi adalah **secangkir kopi hangat** — sudah diolah, siap dinikmati, dan memberi manfaat. Proses dari biji ke cangkir disebut **pengolahan data**.

    ### Perbedaan Data dan Informasi

    | Aspek | Data | Informasi |
    |-------|------|-----------|
    | **Bentuk** | Mentah, belum diolah | Sudah diolah, bermakna |
    | **Nilai** | Belum berguna langsung | Berguna untuk pengambilan keputusan |
    | **Contoh** | "35°C", "Rp50.000", "Senin" | "Suhu hari ini panas — 35°C", "Uang jajan saya Rp50.000 untuk seminggu" |
    | **Hubungan** | Bahan baku | Hasil olahan |

    ### Contoh: Dari Data ke Informasi

    ```
                    DATA MENTAH
                    ┌──────────┐
                    │ 85, 90   │
                    │ 78, 88   │
                    │ 92, 76   │
                    │ 80        │ ← Nilai dari 7 siswa
                    └──────────┘
                         │
                         ▼ Pengolahan
                    ┌──────────────────┐
                    │ Rata-rata = 84.1  │
                    │ Tertinggi = 92   │
                    │ Terendah = 76    │
                    │ Lulus semua ✅   │
                    └──────────────────┘
                         │
                         ▼
                    ┌──────────────────┐
                    │ KELAS X-A:       │
                    │ Nilai Informatika│
                    │ ✅ Rata-rata BAIK│
                    │ ★ Nilai terbaik │
                    │   = 92 (Lisa)   │
                    └──────────────────┘
    ```

    ### Karakteristik Informasi yang Baik

    1. **Akurat** — Bebas dari kesalahan
    2. **Tepat Waktu** — Tersedia saat dibutuhkan
    3. **Relevan** — Sesuai dengan kebutuhan
    4. **Lengkap** — Tidak setengah-setengah
    5. **Jelas** — Mudah dipahami

    ### 📌 Contoh Nyata

    **Gojek:**
    1. Data: GPS tracking driver (koordinat setiap 5 detik)
    2. Informasi: "Driver kamu sudah dekat, estimasi 2 menit sampai"
    3. Keputusan: Kamu siap-siap ke titik jemput

    **Sekolah:**
    1. Data: Nilai ulangan seluruh siswa
    2. Informasi: "Rata-rata kelas 84.1 — bagus! Tapi masih ada 3 siswa perlu remedial"
    3. Keputusan: Guru memberikan program remedial

    ### 🔍 Cek Pemahaman
    1. Jelaskan perbedaan antara data dan informasi!
    2. Sebutkan 5 karakteristik informasi yang baik!
    3. Berikan contoh proses perubahan data menjadi informasi di lingkungan sekolah!

    ### 📋 Studi Kasus
    Seorang wali kelas memiliki data mentah nilai 30 siswa untuk 5 mata pelajaran. la ingin mengetahui siapa siswa yang paling berprestasi, rata-rata nilai kelas per mata pelajaran, dan berapa banyak siswa yang remedial.

    **Pertanyaan:**
    1. Termasuk data atau informasikah nilai mentah 30 siswa tersebut?
    2. Informasi apa saja yang bisa dihasilkan dari data tersebut untuk membantu wali kelas mengambil keputusan?

    > 🤔 **Refleksi:** Ambil 3 contoh data di sekitarmu (suhu ruangan, nilai, jadwal pelajaran), lalu ubah menjadi informasi yang bermakna!
    """)


def content_spreadsheet():
    return dedent("""
    ### 📈 Pengolahan Data dengan Spreadsheet

    Spreadsheet adalah aplikasi yang memungkinkan kita mengolah data dalam bentuk **tabel baris dan kolom**. Contoh: Microsoft Excel, Google Sheets, LibreOffice Calc.

    > 🧩 **Analogi:** Spreadsheet itu seperti **papan catur raksasa** dengan 1.048.576 baris dan 16.384 kolom. Setiap kotak (cell) bisa diisi angka, teks, atau rumus. Kalau kamu mengubah satu angka, semua hasil perhitungan akan otomatis menyesuaikan. Ajaib!

    ### Pengenalan Spreadsheet

    ```
       ┌───────┬──────┬──────┬──────┬──────┐
       │       │  A   │  B   │  C   │  D   │
       ├───────┼──────┼──────┼──────┼──────┤
       │   1   │ Nama │ Tugas│ UTS  │ UAS  │ ← Header
       ├───────┼──────┼──────┼──────┼──────┤
       │   2   │Andi  │  85  │  78  │  90  │
       ├───────┼──────┼──────┼──────┼──────┤
       │   3   │Budi  │  90  │  88  │  85  │
       ├───────┼──────┼──────┼──────┼──────┤
       │   4   │Cici  │  75  │  80  │  82  │
       ├───────┼──────┼──────┼──────┼──────┤
       │   5   │      │      │      │      │
       ├───────┼──────┼──────┼──────┼──────┤
       │   6   │Rata2 │ =AVERAGE│       │
       └───────┴──────┴──────┴──────┴──────┘
               ↑ Cell A1 (kolom A, baris 1)
    ```

    ### Fungsi Dasar Spreadsheet

    | Fungsi | Cara Penulisan | Kegunaan |
    |--------|---------------|----------|
    | **SUM** | `=SUM(A1:A10)` | Menjumlahkan semua angka |
    | **AVERAGE** | `=AVERAGE(B2:B10)` | Menghitung rata-rata |
    | **MAX** | `=MAX(C2:C10)` | Nilai tertinggi |
    | **MIN** | `=MIN(D2:D10)` | Nilai terendah |
    | **COUNT** | `=COUNT(A2:A10)` | Menghitung jumlah data (angka) |
    | **IF** | `=IF(B2>75,"LULUS","REMEDIAL")` | Percabangan/kondisi |

    ### Operator Dasar

    ```
    +  Penjumlahan    =A1+B1
    -  Pengurangan    =A1-B1
    *  Perkalian      =A1*B1
    /  Pembagian      =A1/B1
    ^  Pangkat        =A1^2    (A1 kuadrat)
    %  Persen         =A1*10%  (10% dari A1)
    ```

    ### Contoh Praktik: Daftar Nilai

    | A | B | C | D | E | F |
    |---|---|---|---|---|---|
    | **Nama** | **Tugas** | **UTS** | **UAS** | **Nilai Akhir** | **Keterangan** |
    | Andi | 85 | 78 | 90 | `=B2*0.2+C2*0.3+D2*0.5` | `=IF(E2>75,"LULUS","REMEDIAL")` |
    | Budi | 90 | 88 | 85 | `=B3*0.2+C3*0.3+D3*0.5` | `=IF(E3>75,"LULUS","REMEDIAL")` |

    **Rumus Nilai Akhir:** Tugas (20%) + UTS (30%) + UAS (50%)

    ### 📌 Contoh Nyata

    **Seorang bendahara OSIS** menggunakan Google Sheets untuk mencatat:
    - Pemasukan (iuran, sponsor)
    - Pengeluaran (kegiatan, konsumsi)
    - Saldo otomatis dengan `=SUM(pemasukan) - SUM(pengeluaran)`
    - Semua bisa diakses bersama secara real-time!

    ### 🔍 Cek Pemahaman
    1. Sebutkan 4 fungsi dasar spreadsheet dan kegunaannya!
    2. Apa yang dimaksud dengan cell, row, dan column di spreadsheet?
    3. Bagaimana cara menulis rumus di spreadsheet? Berikan contoh!

    ### 📋 Studi Kasus
    Sebagai bendahara kelas, kamu diminta membuat laporan keuangan bulanan. Ada pemasukan dari iuran siswa (50 orang × Rp5.000) dan pengeluaran untuk kebersihan kelas (Rp50.000) serta alat tulis (Rp75.000).

    **Pertanyaan:**
    1. Buatlah rancangan spreadsheet dengan kolom yang sesuai!
    2. Tuliskan rumus yang digunakan untuk menghitung total pemasukan, total pengeluaran, dan saldo akhir!

    > 🤔 **Refleksi:** Buat spreadsheet sederhana untuk mencatat pengeluaran uang jajanmu selama seminggu! Gunakan rumus SUM untuk total!
    """)


def content_visualisasi_data():
    return dedent("""
    ### 📉 Visualisasi Data

    Visualisasi data adalah **penyajian data dalam bentuk gambar** seperti grafik, diagram, atau peta. Tujuannya agar data lebih mudah dipahami dan pola dalam data bisa terlihat jelas.

    > 🧩 **Analogi:** Visualisasi data itu seperti **peta**. Bandingkan: teks "Jalan dari sekolah ke rumahku: belok kiri, lurus 500m, belok kanan, sampai" vs peta yang menunjukkan rute secara visual. Jelas lebih mudah dipahami dengan peta! Begitu juga dengan data — grafik membuat data "berbicara".

    ### Jenis-Jenis Grafik

    ```
    Grafik Batang:        Grafik Garis:        Diagram Lingkaran:
    Nilai per siswa       Tren penjualan       Anggaran OSIS
    ██                    ░░                    ┌─────┐
    ██ ██                ░░ ▒▒                 │  30%│
    ██ ██ ██            ░░   ▒▒                │     │
    ██ ██ ██ ██        ░░     ▒▒               │45%  │
    ██ ██ ██ ██ ██    ░░       ▒▒              │     │
    A  B  C  D  E     Jan-Feb-Mar-Apr          └─────┘
    ```

    ### Kapan Menggunakan Grafik Apa?

    | Jenis Grafik | Cocok untuk | Contoh |
    |-------------|-------------|--------|
    | **Batang** | Membandingkan data antar kategori | Nilai per siswa, penjualan per produk |
    | **Garis** | Melihat tren/perubahan seiring waktu | Suhu harian, kenaikan pengguna Gojek |
    | **Lingkaran** | Proporsi / bagian dari keseluruhan | Persentase anggaran, asal kota siswa |
    | **Scatter** | Hubungan antara 2 variabel | Korelasi jam belajar vs nilai |
    | **Histogram** | Distribusi frekuensi | Sebaran nilai ulangan |

    ### Cara Membuat Grafik di Google Sheets

    ```
    Langkah 1: Siapkan data di tabel
    ┌──────────┬───────┐
    │  Bulan   │ Suhu  │
    ├──────────┼───────┤
    │ Jan      │  28   │
    │ Feb      │  29   │
    │ Mar      │  30   │
    │ Apr      │  31   │
    └──────────┴───────┘

    Langkah 2: Blok data → Insert → Chart
    Langkah 3: Pilih "Line chart"
    ```

    ### Aturan Visualisasi yang Baik

    1. ✅ **Sederhana** — Jangan terlalu ramai
    2. ✅ **Label jelas** — Sumbu X, Y, legend, judul
    3. ✅ **Warna kontras** — Bisa dibedakan dengan mudah
    4. ✅ **Skala sesuai** — Jangan menyesatkan dengan skala yang dipotong
    5. ❌ **Jangan 3D tanpa perlu** — 3D sering bikin data sulit dibaca

    ### 📌 Contoh Nyata

    **Gojek memvisualisasikan:**
    - Jumlah pesanan per jam (grafik garis → jam sibuk jam 7 pagi & 12 siang)
    - Daerah dengan order terbanyak (peta panas → Jakarta, Bandung, Surabaya)
    - Persentase jenis layanan (lingkaran → GoRide 45%, GoCar 30%, GoFood 25%)

    Dengan visualisasi ini, Gojek bisa memutuskan: di mana harus menambah driver, jam berapa promo makanan, dan sebagainya.

    ### 🔍 Cek Pemahaman
    1. Sebutkan 4 jenis grafik dan kapan waktu yang tepat menggunakannya!
    2. Apa aturan visualisasi data yang baik?
    3. Mengapa grafik lebih efektif daripada tabel untuk menyampaikan informasi?

    ### 📋 Studi Kasus
    OSIS sekolah ingin menyajikan data penggunaan anggaran tahun ini kepada seluruh siswa dalam acara LDKS. Data mereka: konsumsi 40%, acara 30%, dokumentasi 10%, transportasi 15%, dan cadangan 5%.

    **Pertanyaan:**
    1. Jenis grafik apa yang paling tepat untuk menyajikan data tersebut? Mengapa?
    2. Buatlah visualisasi sederhana menggunakan ASCII art atau deskripsikan bagaimana tampilan grafiknya!

    > 🤔 **Refleksi:** Kumpulkan data tinggi badan 10 temanmu, lalu buat grafik batang menggunakan Google Sheets. Pola apa yang kamu lihat?
    """)


# ─── BAB 7 ─────────────────────────────────────────────────────

def content_logika_algoritma():
    return dedent("""
    ### 🤖 Logika dan Algoritma Dasar

    **Logika** adalah ilmu tentang **penalaran yang benar**. **Algoritma** adalah **langkah-langkah sistematis** untuk menyelesaikan masalah. Tanpa algoritma yang baik, program tidak akan berjalan dengan benar.

    > 🧩 **Analogi:** Algoritma itu seperti **resep mie instan**. Langkah-langkahnya jelas, urut, dan terbatas: (1) Buka bungkus, (2) Rebus air, (3) Masukkan mie, (4) Masukkan bumbu, (5) Sajikan. Kalau langkahnya diacak — misalnya bumbu dimasukkan sebelum air mendidih — hasilnya tidak maksimal. Sama seperti program!

    ### Logika Dasar: AND, OR, NOT

    Dalam pemrograman, kita sering menggunakan logika **boolean** (true/false):

    ```
    AND    = semua harus benar (✅ AND ✅ = ✅)
    OR     = salah satu benar (✅ OR ❌ = ✅)
    NOT    = kebalikan (NOT ✅ = ❌)
    ```

    | Nilai A | Nilai B | A AND B | A OR B | NOT A |
    |---------|---------|---------|--------|-------|
    | ✅ | ✅ | ✅ | ✅ | ❌ |
    | ✅ | ❌ | ❌ | ✅ | ❌ |
    | ❌ | ✅ | ❌ | ✅ | ✅ |
    | ❌ | ❌ | ❌ | ❌ | ✅ |

    **Contoh dalam kehidupan:**
    - "Kamu boleh main game **JIKA** PR sudah selesai **DAN** sudah maghrib"
    - "Kamu dapat nilai A **JIKA** UTS >= 80 **ATAU** UAS >= 85"
    - "Kamu **TIDAK** boleh keluar kelas tanpa izin"

    ### Ciri-Ciri Algoritma yang Baik

    | Ciri | Penjelasan | Contoh Buruk | Contoh Baik |
    |------|-----------|-------------|-------------|
    | **Input** | Ada data yang diproses | — | Masukkan 2 angka |
    | **Output** | Menghasilkan hasil | — | Tampilkan jumlah |
    | **Definitif** | Setiap langkah jelas | "Masak sampai matang" | "Rebus 5 menit" |
    | **Finite** | Berhenti | "Ulang terus" | "Ulang 10 kali" |
    | **Efektif** | Bisa dijalankan | "Terbang ke bulan" | "Hitung luas segitiga" |

    ### Contoh Algoritma Sederhana

    **Algoritma Membeli Gojek:**
    ```
    1. Buka aplikasi Gojek
    2. Pilih GoRide
    3. Masukkan lokasi jemput (otomatis) dan tujuan
    4. Pilih driver yang tersedia
    5. Tunggu driver datang
    6. Naik dan sampai tujuan
    7. Bayar (cash/GoPay)
    8. Selesai
    ```

    ### 📌 Contoh Nyata

    **Algoritma TikTok FYP:**
    1. Kamu menonton video kucing
    2. Sistem mencatat: durasi tonton = 30 detik (lama = suka)
    3. Sistem mencari pola: "pengguna yang suka kucing juga suka..."
    4. TikTok menampilkan lebih banyak video kucing
    5. Kamu jadi betah berjam-jam di TikTok!
    6. **Ini adalah algoritma!**

    ### 🔍 Cek Pemahaman
    1. Jelaskan perbedaan logika AND, OR, dan NOT! Berikan contoh masing-masing!
    2. Sebutkan 5 ciri algoritma yang baik!
    3. Apa perbedaan antara algoritma yang definitif dan yang tidak? Berikan contoh!

    ### 📋 Studi Kasus
    Sebuah aplikasi Gojek ingin menambahkan fitur baru: jika saldo GoPay cukup, pembayaran otomatis menggunakan GoPay. Jika tidak, tampilkan pilihan metode pembayaran lain.

    **Pertanyaan:**
    1. Tuliskan algoritma sederhana untuk fitur tersebut menggunakan logika IF-THEN-ELSE!
    2. Logika boolean apa yang digunakan dalam kasus "Saldo cukup DAN lokasi tujuan valid"?

    > 🤔 **Refleksi:** Tuliskan algoritma "Bangun pagi dan berangkat sekolah" dalam 8 langkah. Tukarkan dengan temanmu, apakah langkahnya sudah jelas?
    """)


def content_flowchart():
    return dedent("""
    ### 📐 Flowchart: Memvisualisasikan Algoritma

    Flowchart adalah **diagram yang menggambarkan alur algoritma** menggunakan simbol-simbol standar. Flowchart membuat algoritma lebih mudah dipahami daripada teks.

    > 🧩 **Analogi:** Flowchart itu seperti **peta jalan**. Bayangkan algoritma "Pergi ke rumah teman" ditulis dalam teks: belok kiri, lurus, belok kanan... Lebih mudah dipahami pakai peta, kan? Flowchart adalah "peta" untuk program!

    ### Simbol Flowchart

    ```
        ┌──────────┐      ┌──────────────┐      ┌──────────┐
        │  START/  │      │   PROSES     │      │  INPUT/  │
        │  END     │      │  (Kegiatan)  │      │  OUTPUT  │
        └──────────┘      └──────────────┘      └──────────┘
        (Terminator)      (Process)            (Input/Output)

        ┌──────────┐      ┌──────┐       ┌──────────────────┐
        │ KONDISI  │      │      │       │                  │
        │ Ya / Tidak├──────► ◄───────       ► PREPARATION    │
        └──────────┘      └──────┘       │ (Inisialisasi)   │
        (Decision)         (Connector)    └──────────────────┘
    ```

    ### Contoh Flowchart: Menentukan Kelulusan

    ```
                    ┌──────────┐
                    │  START   │
                    └────┬─────┘
                         ▼
                    ┌──────────┐
                    │ Input    │
                    │ Nilai    │
                    └────┬─────┘
                         ▼
                    ┌──────────┐
                    │ Nilai    │
                 ┌──┤ >= 75?   ├──┐
                 │  └────┬─────┘  │
                 │       │ Ya    Tidak
                 ▼       ▼       ▼
            ┌────────┐      ┌──────────┐
            │ LULUS  │      │ REMEDIAL │
            └───┬────┘      └────┬─────┘
                │                │
                └────────┬───────┘
                         ▼
                    ┌──────────┐
                    │  END     │
                    └──────────┘
    ```

    ### Contoh Flowchart: Menghitung Luas Persegi

    ```
                    ┌──────────┐
                    │  START   │
                    └────┬─────┘
                         ▼
          ┌──────────────────────────┐
          │ Input sisi (s)           │
          └────────────┬─────────────┘
                       ▼
          ┌──────────────────────────┐
          │ Hitung luas = s × s      │
          └────────────┬─────────────┘
                       ▼
          ┌──────────────────────────┐
          │ Tampilkan luas           │
          └────────────┬─────────────┘
                       ▼
                    ┌──────────┐
                    │  END     │
                    └──────────┘
    ```

    ### 📌 Contoh Nyata

    **Flowchart Login Gojek:**
    1. START → Buka Aplikasi Gojek
    2. Input nomor HP
    3. Apakah nomor terdaftar?
       - Ya → Kirim OTP
       - Tidak → Tampilkan "Daftar dulu"
    4. Input OTP
    5. Apakah OTP benar?
       - Ya → Masuk ke halaman utama
       - Tidak → "OTP salah, coba lagi"
    6. END

    ### 🔍 Cek Pemahaman
    1. Sebutkan 4 simbol flowchart beserta fungsinya!
    2. Apa perbedaan antara simbol Process dan Decision dalam flowchart?
    3. Mengapa flowchart lebih mudah dipahami daripada algoritma dalam bentuk teks?

    ### 📋 Studi Kasus
    Seorang siswa diminta membuat flowchart untuk program "Cek Suhu Tubuh". Aturannya: jika suhu >= 38°C maka tampilkan "DEMAM", jika kurang tampilkan "SEHAT".

    **Pertanyaan:**
    1. Buatlah flowchart dalam bentuk teks (gunakan ASCII atau deskripsi langkah) untuk program tersebut!
    2. Bagaimana jika ditambahkan kondisi: jika suhu >= 38°C DAN ada batuk, tampilkan "SEGERA KE DOKTER"?

    > 🤔 **Refleksi:** Buatlah flowchart untuk algoritma "Membeli pulsa" atau "Membuat kopi" menggunakan simbol-simbol yang benar!
    """)


def content_scratch():
    return dedent("""
    ### 🧩 Pengenalan Scratch sebagai Alat Pemrograman

    **Scratch** adalah bahasa pemrograman **visual berbasis blok** yang dikembangkan oleh MIT Media Lab. Cocok untuk pemula karena tidak perlu menulis kode teks — cukup **seret dan susun blok-blok** seperti menyusun LEGO!

    > 🧩 **Analogi:** Scratch itu seperti **LEGO**: setiap blok adalah perintah (misal: "gerak 10 langkah", "putar 15 derajat", "katakan Halo"). Kamu tinggal menyusun blok-blok itu seperti menyusun balok LEGO — tanpa perlu lem (coding teks)! Hasilnya? Program yang bisa jalan!

    ### Tampilan Scratch

    ```
      ┌─────────────────────────────────────────────────────────┐
      │ Scratch 3.0                             [File] [Edit]  │
      ├──────────┬──────────────────────────┬──────────────────┤
      │          │                          │                  │
      │  BLOCKS  │      PROGRAM AREA        │     STAGE       │
      │  (Kode)  │   (Susun blok di sini)   │  (Hasil/layar)  │
      │          │                          │                  │
      │  Motion  │  when ▢ clicked          │  ┌──────────┐   │
      │  Looks   │  move 10 steps           │  │  Kucing  │   │
      │  Sound   │  say [Halo!] for 2 secs  │  │  🐱      │   │
      │  Events  │  wait 1 seconds          │  │          │   │
      │  Control │  forever                 │  └──────────┘   │
      │  Sensing │    next costume          │                  │
      │  ...     │                          │                  │
      ├──────────┴──────────────────────────┴──────────────────┤
      │ SPRITES  │  Backdrops  │  Sound                        │
      └────────────────────────────────────────────────────────┘
    ```

    ### Kategori Blok Scratch

    | Kategori | Warna | Fungsi | Contoh Blok |
    |----------|-------|--------|-------------|
    | **Motion** | 🔵 Biru | Menggerakkan sprite | `move 10 steps`, `turn 15 degrees` |
    | **Looks** | 🟣 Ungu | Mengubah tampilan | `say [Halo]`, `switch costume` |
    | **Sound** | 🟣 Pink | Memutar suara | `play sound`, `change volume` |
    | **Events** | 🟡 Kuning | Memicu kode | `when flag clicked`, `when key pressed` |
    | **Control** | 🟠 Oranye | Mengatur alur | `wait`, `forever`, `if then else` |
    | **Sensing** | 🔵 Biru Muda | Mendeteksi sesuatu | `touching mouse`, `ask and wait` |
    | **Operators** | 🟢 Hijau | Operasi matematika | `+`, `-`, `*`, `/`, `>` |
    | **Variables** | 🟠 Oranye | Membuat variabel | `set score to 0`, `change score` |

    ### Contoh Kode di Scratch

    ```blocks
    Ketika bendera hijau diklik
    ulang terus
        jika (senter menyentuh Kucing?) maka
            katakan Aduh! selama 2 detik
            mainkan suara Meow
        jika tidak
            jalan 10 langkah
            jika di pinggir, pantulkan
        akhir
    akhir
    ```

    ### 📌 Contoh Nyata

    Banyak game sederhana dibuat dengan Scratch oleh siswa SMP/SMA di seluruh dunia. Di Indonesia, Scratch sering digunakan untuk:
    - Membuat kuis interaktif
    - Animasi cerita pendek
    - Game sederhana (T-Rex run, Flappy Bird clone)
    - Simulasi fisika (gravitasi, gerak parabola)

    **Kunjungi** https://scratch.mit.edu untuk mencoba langsung secara online — **gratis!**

    ### 🔍 Cek Pemahaman
    1. Apa itu Scratch dan siapa yang mengembangkannya?
    2. Sebutkan 5 kategori blok di Scratch beserta warna dan fungsinya!
    3. Mengapa Scratch cocok untuk pemula belajar pemrograman?

    ### 📋 Studi Kasus
    Di kelas X, guru memberikan tugas membuat animasi sederhana dengan Scratch. Seorang siswa ingin membuat animasi kucing yang berjalan dan mengeong ketika disentuh oleh pointer mouse.

    **Pertanyaan:**
    1. Kategori blok apa saja yang diperlukan untuk membuat animasi tersebut?
    2. Tuliskan urutan blok yang kira-kira diperlukan (dalam bentuk deskripsi)!

    > 🤔 **Refleksi:** Apa perbedaan pemrograman blok (Scratch) dengan pemrograman teks (C++, Python)? Mana yang lebih mudah menurutmu?
    """)


def content_proyek_scratch():
    return dedent("""
    ### 🎮 Proyek: Program Sederhana dengan Scratch

    Saatnya **membuat program sungguhan**! Dengan Scratch, kamu bisa membuat game, animasi, atau cerita interaktif hanya dengan menyusun blok-blok.

    > 🧩 **Analogi:** Proyek ini seperti **membangun rumah dari LEGO**. Kamu sudah tahu fungsi setiap blok (motion, looks, control, dll). Sekarang saatnya merancang dan membangun sesuatu yang **nyata** — bukan sekadar latihan!

    ### 💡 Ide Proyek (Pilih Salah Satu)

    #### 1. 🎯 Game Kuis Interaktif
    ```
    Konsep: Pemain menjawab pertanyaan Informatika
    Fitur:
    ✅ Pertanyaan muncul acak
    ✅ Skor bertambah jika benar
    ✅ Timer 10 detik per soal
    ✅ Suara "benar" 🎉 dan "salah" 😢

    Blok yang digunakan: Events, Sensing, Variables, Control, Looks
    ```

    #### 2. 🐱 Game Kejar-Kejaran
    ```
    Konsep: Kucing mengejar tikus, dikendalikan mouse
    Fitur:
    ✅ Kucing mengikuti pointer mouse
    ✅ Tikus menghindar secara otomatis
    ✅ Skor bertambah jika kucing menyentuh tikus
    ✅ Level semakin cepat

    Blok yang digunakan: Motion, Control, Sensing, Variables
    ```

    #### 3. 🌟 Animasi Cerita "Liburan ke Bandung"
    ```
    Konsep: Animasi interaktif 2-3 menit
    Fitur:
    ✅ Karakter bicara dengan speech bubble
    ✅ Latar berubah (rumah → jalan → tujuan)
    ✅ Klik untuk lanjut ke scene berikutnya
    ✅ Efek suara dan musik

    Blok yang digunakan: Looks, Events, Control, Sound
    ```

    ### Langkah-Langkah Proyek

    ```
    ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐
    │  Tentukan │   │  Desain  │   │  Susun   │   │   Uji    │
    │  Ide     │──►│  Karakter│──►│  Blok    │──►│  & Debug │
    └──────────┘   └──────────┘   └──────────┘   └────┬─────┘
                                                       │
                                                ┌──────────┐
                                                │ Presentasi│
                                                │ & Kumpul  │
                                                └──────────┘
    ```

    ### Rubrik Penilaian

    | Aspek | Skor 4 | Skor 3 | Skor 2 | Skor 1 |
    |-------|--------|--------|--------|--------|
    | **Fungsionalitas** | Program berjalan sempurna | Berjalan dengan bug kecil | Berjalan sebagian | Tidak bisa jalan |
    | **Kreativitas** | Konsep unik & menarik | Cukup kreatif | Biasa saja | Tidak ada kreativitas |
    | **Kompleksitas** | Banyak blok & interaksi | Beberapa blok | Blok minimal | Sangat sederhana |
    | **Estetika** | Tampilan & suara menarik | Cukup rapi | Kurang rapi | Acak-acakan |

    ### 📌 Contoh Nyata

    **Proyek siswa SMA N 6 Cimahi tahun lalu:** Mereka membuat game "Petualangan Si Oncom" — sebuah game edukasi tentang sejarah Bandung. Karakter utama (Oncom, kucing lucu) harus mengumpulkan informasi sejarah sambil menghindari rintangan. Game ini dipresentasikan di acara class meeting!

    ```blocks
    Ketika bendera hijau diklik
    set skor ke 0
    tanyakan [Siapa nama kamu?] dan tunggu
    katakan (gabung [Selamat datang, ] (jawaban)) selama 2 detik
    forever
        if <touching [musuh v] ?> then
            change skor by (-1)
            say [Aduh!] for 1 seconds
        end
    end
    ```

    Selamat berkarya! 🚀

    ### 🔍 Cek Pemahaman
    1. Sebutkan 3 ide proyek yang bisa dibuat dengan Scratch!
    2. Apa saja 4 aspek penilaian dalam rubrik proyek Scratch?
    3. Jelaskan langkah-langkah pengerjaan proyek Scratch dari awal hingga akhir!

    ### 📋 Studi Kasus
    Sebuah kelompok memilih proyek "Game Kuis Informatika" dengan Scratch. Setelah seminggu, mereka baru membuat 3 soal, skor belum berfungsi, dan tampilan masih berantakan. Deadline tinggal 3 hari lagi.

    **Pertanyaan:**
    1. Apa yang salah dengan perencanaan proyek kelompok tersebut?
    2. Buatkan jadwal 3 hari yang efektif agar proyek mereka selesai tepat waktu!

    > 🤔 **Refleksi:** Setelah proyek selesai, tuliskan (1) Hal paling seru, (2) Kesulitan terbesar, (3) Satu hal yang akan kamu tingkatkan!
    """)


# ─── BAB 8 ─────────────────────────────────────────────────────

def content_dampak_positif():
    return dedent("""
    ### 🌍 Dampak Positif TIK bagi Masyarakat

    TIK telah membawa **banyak manfaat** bagi kehidupan manusia di berbagai bidang. Mari kita lihat sisi positif dari perkembangan teknologi!

    > 🧩 **Analogi:** Dampak positif TIK itu seperti **memiliki mobil**. Dulu kamu jalan kaki, sekarang:
    > - Kamu bisa ke mana saja dengan cepat (informasi)
    > - Kamu bisa bawa banyak barang (data)
    > - Kamu bisa antar jemput teman (berbagi)
    > - Tapi kamu juga perlu bensin (listrik), SIM (skill), dan bengkel (maintenance)!

    ### Dampak Positif di Berbagai Bidang

    | Bidang | Dampak Positif | Contoh di Indonesia |
    |--------|---------------|-------------------|
    | **Pendidikan** | Akses belajar dari mana saja, kapan saja | Ruangguru, Google Classroom, YouTube Edu |
    | **Kesehatan** | Konsultasi dokter tanpa antre | Halodoc, Alodokter telemedicine |
    | **Ekonomi** | Jual beli online, UMKM naik kelas | Shopee, Tokopedia, GoFood |
    | **Pemerintahan** | Layanan publik tanpa calo | INAruang, e-KTP, SIM online |
    | **Transportasi** | Mudah cari transportasi | Gojek, Grab, traveloka |
    | **Komunikasi** | Gratis, cepat, bisa video | WhatsApp, Zoom, Telegram |
    | **Hiburan** | Konten tak terbatas, kapan saja | YouTube, Netflix, TikTok |
    | **Sosial** | Terhubung dengan siapa saja | Instagram, Facebook, Twitter |

    ### TIK untuk Pendidikan di Indonesia

    ```
      ┌──────────────────────────────────────────────┐
      │  TIK UNTUK PENDIDIKAN                        │
      ├──────────────────────────────────────────────┤
      │                                              │
      │  📚 e-book & perpustakaan digital            │
      │  🎥 Video pembelajaran (YouTube Khan Academy)│
      │  📝 Tugas online (Google Classroom)          │
      │  🎮 Belajar lewat game (Quizizz, Kahoot)    │
      │  🤝 Diskusi online (Discord, WhatsApp Group) │
      │  🧑‍🏫 Kelas virtual (Zoom, Google Meet)       │
      │  📊 Analisis nilai (Spreadsheet)             │
      └──────────────────────────────────────────────┘
    ```

    ### 💡 TIK Membuka Kesempatan

    1. **Siapa pun bisa belajar** — YouTube, Khan Academy, MOOC
    2. **Siapa pun bisa berkarya** — Konten kreator, youtuber, penulis blog
    3. **Siapa pun bisa berbisnis** — Jualan via Shopee, Instagram, TikTok Shop
    4. **Siapa pun bisa terhubung** — Komunitas, forum, networking global

    ### 📌 Contoh Nyata

    **Pak Budi**, penjual tahu bulat di pinggir jalan, dulu hanya laku 50 pcs/hari. Setelah anaknya mengajari jualan di GoFood dan Instagram, sekarang bisa laku 200 pcs/hari! Dia juga menerima pembayaran QRIS. TIK membantu **UMKM naik kelas**.

    ### 🔍 Cek Pemahaman
    1. Sebutkan 4 dampak positif TIK di berbagai bidang beserta contoh di Indonesia!
    2. Bagaimana TIK membantu UMKM naik kelas?
    3. Jelaskan bagaimana TIK membuka kesempatan bagi siapa pun untuk belajar dan berkarya!

    ### 📋 Studi Kasus
    Seorang siswa di daerah terpencil ingin belajar programming tetapi tidak ada kursus IT di kotanya. la hanya punya HP Android dan kuota internet terbatas. la merasa putus asa karena keterbatasan akses.

    **Pertanyaan:**
    1. Bagaimana TIK bisa membantu siswa tersebut tetap belajar programming?
    2. Sebutkan minimal 3 sumber belajar online gratis yang bisa dia manfaatkan!

    > 🤔 **Refleksi:** Sebutkan 3 dampak positif TIK yang paling kamu rasakan dalam hidupmu sehari-hari!
    """)


def content_dampak_negatif():
    return dedent("""
    ### ⚠️ Dampak Negatif dan Risiko TIK

    Setiap teknologi punya **dua sisi**. Selain manfaat, TIK juga membawa risiko dan dampak negatif jika tidak digunakan dengan bijak.

    > 🧩 **Analogi:** TIK itu seperti **pisau**. Di tangan yang tepat, pisau membantu memasak. Di tangan yang salah, pisau bisa melukai. Yang membedakan bukan pisaunya, tapi **penggunanya**. Begitu juga TIK — manfaat atau mudarat tergantung pada kita!

    ### Dampak Negatif TIK

    | Dampak | Penjelasan | Contoh |
    |--------|-----------|--------|
    | **Kecanduan** | Terlalu sering pakai gadget/game/internet | Scroll TikTok 5 jam, begadang main game |
    | **Cyberbullying** | Perundungan di dunia digital | Body shaming di komentar IG, bully di grup WA |
    | **Hoaks** | Informasi palsu menyebar cepat | Berita "vaksin berbahaya" di WhatsApp |
    | **Pelanggaran Privasi** | Data pribadi bocor/disalahgunakan | Data bocor dari Facebook, e-commerce |
    | **Penipuan Online** | Modus penipuan lewat internet | Shopee palsu, undian berhadiah palsu |
    | **Kesenjangan Digital** | Yang punya akses vs tidak | Kota vs desa, kaya vs miskin |
    | **Dampak Fisik** | Gangguan kesehatan akibat gadget | Mata minus, sakit leher, obesitas |
    | **Isolasi Sosial** | Kurang interaksi tatap muka | Lebih nyaman chat daripada ketemu langsung |

    ### Kecanduan Media Sosial: Dopamine Loop

    ```
      Kamu dapat NOTIFIKASI
              │
              ▼
        Otak melepas DOPAMINE (hormon senang)
              │
              ▼
        Kamu membuka aplikasi
              │
              ▼
        Kamu lihat konten seru → 🧠 "Lagi dong!"
              │
              ▼
        Kamu SCROLL terus — 10 menit → 30 menit → 2 jam...
              │
              ▼
        ❌ Waktu habis, PR tidak selesai, begadang!
    ```

    ### Cara Menghindari Dampak Negatif

    ```
      ⏰  Atur waktu layar (Screen Time) — maks 3 jam/hari di luar belajar
      🔇  Matikan notifikasi aplikasi yang tidak penting
      ✅  Cek kebenaran berita sebelum share (cek sumber, cek hoaks di s.id/cekfakta)
      🔒  Jaga data pribadi — jangan posting KTP, alamat rumah
      🚫  Blokir akun yang toxic atau bully
      🤝  Prioritaskan interaksi langsung — ketemu teman, ngobrol offline
    ```

    ### 📌 Contoh Nyata

    **Kasus:** Seorang siswa SMA di Jakarta mengalami **cyberbullying** — videonya diedit dan dijadikan meme oleh teman sekelas, menyebar di grup WA, dan dia menjadi bahan ledekan. Akibatnya, dia jadi enggan ke sekolah, nilai turun, dan depresi.

    **Pelajaran:** Cyberbullying itu nyata dan berdampak serius. Jika kamu melihat cyberbullying, **bela korban** dan **laporkan ke guru**. Jika kamu yang mengalami, **bicara pada orang dewasa yang dipercaya**.

    ### 🔍 Cek Pemahaman
    1. Sebutkan 4 dampak negatif TIK beserta contohnya!
    2. Jelaskan apa yang dimaksud dengan "dopamine loop" di media sosial!
    3. Sebutkan 3 cara menghindari dampak negatif TIK!

    ### 📋 Studi Kasus
    Rizky menghabiskan 6 jam sehari untuk scroll TikTok. la sering begadang, PR tidak selesai, nilai turun, dan matanya minus. la sadar ini masalah tapi merasa susah berhenti.

    **Pertanyaan:**
    1. Dampak negatif TIK apa saja yang dialami Rizky?
    2. Buatkan rencana 5 langkah untuk membantu Rizky mengatur waktu layarnya!

    > 🤔 **Refleksi:** Pernahkah kamu atau temanmu mengalami dampak negatif TIK? Bagaimana cara kalian menghadapinya?
    """)


def content_etika_digital():
    return dedent("""
    ### ⚖️ Etika Digital dan UU ITE

    **Etika digital** adalah pedoman tentang **apa yang boleh dan tidak boleh** dilakukan di dunia digital. **UU ITE** adalah hukum yang mengatur aktivitas digital di Indonesia.

    > 🧩 **Analogi:** Di dunia nyata, kamu tidak akan masuk rumah orang tanpa izin, mencuri barang, atau berteriak kotor di masjid. Di dunia digital, aturannya sama: **ada etika dan ada hukum**. Etika adalah "sebaiknya", hukum adalah "harus". Melanggar etika bisa ditegur, melanggar hukum bisa dipidana.

    ### 10 Etika Digital yang Harus Kamu Tahu

    ```
      1.  ✍️  Gunakan bahasa yang sopan (tidak ada yang marah-marah di dunia nyata!)
      2.  🔍  Cek kebenaran info sebelum menyebar
      3.  ©️  Hargai hak cipta — sebutkan sumber
      4.  🙈  Jangan posting hal pribadi yang sensitif
      5.  🚫  Jangan bullying atau komentar jahat
      6.  🤝  Izinkan orang punya pendapat berbeda
      7.  📸  Minta izin sebelum tag/foto orang
      8.  ⏰  Jangan spam — kirim pesan berulang
      9.  🛑  Jangan menyamar/mengaku-aku orang lain
      10. 🔐  Jaga password dan akunmu
    ```

    ### UU ITE: Aturan yang Wajib Dipatuhi

    **Dasar Hukum:**
    - **UU No. 11/2008** → UU ITE pertama
    - **UU No. 19/2016** → Revisi pertama
    - **UU No. 1/2024** → Revisi terbaru

    ### Pasal-Pasal Penting UU ITE

    | Pasal | Bunyi Singkat | Ancaman Hukuman |
    |-------|---------------|----------------|
    | **Pasal 27 ayat 1** | Menyebarkan konten asusila/porno | 6 tahun penjara |
    | **Pasal 27 ayat 3** | Pencemaran nama baik (menghina orang) | 4 tahun penjara |
    | **Pasal 28 ayat 1** | Menyebarkan hoaks/berita bohong | 6 tahun penjara |
    | **Pasal 28 ayat 2** | Ujaran kebencian (SARA) | 6 tahun penjara |
    | **Pasal 29** | Ancaman kekerasan | 6 tahun penjara |
    | **Pasal 30** | Akses ilegal (hacking) | 7 tahun penjara |
    | **Pasal 32** | Memindahkan/mengubah data orang tanpa izin | 9 tahun penjara |
    | **Pasal 45A** | Penghinaan terhadap pemerintah | 6 tahun penjara |

    ### Yang HARUS Kamu Hindari di Medsos

    ❌ Menghina teman, guru, atau orang lain
    ❌ Menyebar foto/video orang tanpa izin
    ❌ Membagikan hoaks atau info yang belum tentu benar
    ❌ Membuat akun palsu untuk menipu
    ❌ Menyebar konten SARA

    ### 📌 Contoh Nyata

    **Kasus nyata di Indonesia:** Seorang mahasiswa dihukum 4 tahun penjara karena menghina Gubernur di media sosial (Pasal 27 ayat 3 UU ITE). Seorang ibu rumah tangga ditahan karena menyebar hoaks vaksin di grup WhatsApp (Pasal 28 ayat 1).

    **Pesan:** **Berpikir sebelum posting!** Apa yang kamu tulis di internet bisa menjadi **barang bukti hukum**. Jangan sampai candaan atau kekesalan sesaat berujung masalah besar.

    ### 🔍 Cek Pemahaman
    1. Sebutkan 5 dari 10 etika digital yang harus kamu tahu!
    2. Apa itu UU ITE dan pasal apa yang mengatur tentang pencemaran nama baik?
    3. Sebutkan 3 hal yang harus kamu hindari di media sosial!

    ### 📋 Studi Kasus
    Seorang siswa membuat status WhatsApp yang berisi foto temannya tanpa izin dan menulis caption yang menghina fisiknya. Status itu kemudian di-screenshot dan menyebar ke grup lain. Korban merasa malu dan tidak mau masuk sekolah.

    **Pertanyaan:**
    1. Etika digital apa yang dilanggar dalam kasus tersebut?
    2. Jika dilihat dari UU ITE, pasal apa yang bisa dikenakan? Jelaskan ancaman hukumannya!

    > 🤔 **Refleksi:** Sebutkan 2 hal yang sering kamu lihat di media sosial yang melanggar etika digital. Menurutmu, apa yang seharusnya dilakukan?
    """)


# ─── BAB 9 ─────────────────────────────────────────────────────

def content_kolaborasi():
    return dedent("""
    ### 🤝 Kolaborasi dan Kerja Tim

    **Kolaborasi** adalah bekerja sama dengan orang lain untuk mencapai tujuan bersama. Dalam dunia TIK, hampir **tidak ada proyek yang dikerjakan sendirian** — semuanya butuh tim!

    > 🧩 **Analogi:** Kolaborasi itu seperti **orkestra**. Ada pemain biola, piano, drum, gitar — masing-masing punya peran berbeda. Kalau semua main sendiri-sendiri, hasilnya berisik. Tapi dengan konduktor yang mengatur, mereka menciptakan **musik yang indah**. Dalam proyek TIK, kalian adalah orkestra itu!

    ### Mengapa Kolaborasi Penting?

    ```
       ┌───────────────────────────────────────────────────┐
       │        1 + 1 = 3 (Sinergi!)                      │
       │                                                   │
       │   Sendirian: 🧑       Bersama: 👩‍💻👨‍🎨👨‍🔧       │
       │   • Ide terbatas       • Banyak ide & sudut      │
       │   • Lambat              • Cepat (bagi tugas)      │
       │   • Gampang nyerah      • Saling support          │
       │   • Error tidak terlihat• Ada yang review         │
       └───────────────────────────────────────────────────┘
    ```

    ### Peran dalam Tim Proyek TIK

    | Peran | Tanggung Jawab | Skill yang Dilatih |
    |-------|---------------|-------------------|
    | **Ketua Tim** | Koordinasi, pembagian tugas, jadwal | Leadership, komunikasi |
    | **Analis** | Menganalisis masalah, kebutuhan pengguna | Critical thinking |
    | **Desainer** | Mendesain tampilan, alur program | Kreativitas, Figma/Canva |
    | **Programmer** | Menyusun kode/blok program | Coding, problem solving |
    | **Dokumenter** | Mencatat, laporan, video dokumentasi | Menulis, komunikasi |
    | **Presenter** | Menyampaikan hasil proyek | Public speaking |

    ### Alat Kolaborasi Digital yang Bisa Kamu Gunakan

    | Alat | Fungsi | Cocok untuk |
    |------|--------|-------------|
    | **Google Docs** | Menulis dokumen bersama real-time | Laporan, proposal |
    | **Google Slides / Canva** | Presentasi kolaboratif | Presentasi proyek |
    | **Google Sheets** | Spreadsheet bersama | Data, anggaran, jadwal |
    | **WhatsApp / Discord** | Komunikasi tim | Diskusi, notifikasi |
    | **GitHub** | Coding bersama (versi lanjutan) | Proyek pemrograman |
    | **Google Drive** | Penyimpanan file bersama | Arsip proyek |

    ### Aturan Kolaborasi yang Efektif

    ```
      ✅  Setiap anggota punya peran jelas
      ✅  Komunikasi terbuka dan sopan
      ✅  Tepat waktu dengan tugas yang diberikan
      ✅  Berani bertanya kalau bingung
      ✅  Berani memberi saran dengan sopan
      ❌  Jangan dominant sendiri
      ❌  Jangan diam pasif — "iya-iya" aja
      ❌  Jangan menunda-nunda tugas
    ```

    ### 📌 Contoh Nyata

    **Sukses karena tim:** Gojek tidak sukses karena satu orang. Ada tim **teknologi** (bikin app), tim **operasional** (atur driver), tim **marketing** (promosi), tim **legal** (urus izin). Semua harus bekerja sama. Di perusahaan IT, istilahnya **cross-functional team**.

    ### 🔍 Cek Pemahaman
    1. Mengapa kolaborasi penting dalam proyek TIK?
    2. Sebutkan 5 peran dalam tim proyek TIK beserta tanggung jawabnya!
    3. Sebutkan 3 alat kolaborasi digital dan fungsinya!

    ### 📋 Studi Kasus
    Sebuah kelompok proyek TIK terdiri dari 4 orang. Dalam pengerjaannya, hanya 2 orang yang aktif, 1 orang pasif, dan 1 orang sering tidak hadir. Akibatnya proyek hampir tidak selesai tepat waktu.

    **Pertanyaan:**
    1. Sebutkan masalah kolaborasi apa yang terjadi dalam kelompok tersebut!
    2. Berdasarkan aturan kolaborasi efektif, apa yang sebaiknya dilakukan ketua tim?

    > 🤔 **Refleksi:** Pengalaman kolaborasi apa yang paling berkesan buatmu? Apa yang membuat tim itu berhasil atau gagal?
    """)


def content_perencanaan_proyek():
    return dedent("""
    ### 📋 Perencanaan Proyek TIK Sederhana

    Perencanaan adalah kunci keberhasilan proyek. **Proyek yang baik direncanakan, bukan kebetulan!**

    > 🧩 **Analogi:** Perencanaan proyek itu seperti **membangun rumah**. Arsitek tidak langsung bangun — dia buat denah dulu, hitung bahan, anggaran, waktu. Kalau tidak ada rencana, rumah bisa roboh atau budget habis di tengah jalan!

    ### Langkah Perencanaan Proyek

    ```
      ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐
      │ 1. IDE   │   │ 2. TIM   │   │ 3. RENCANA│   │ 4. ALAT  │
      │          │   │          │   │           │   │          │
      │Tentukan  │──►│Bagi peran│──►│Buat jadwal│──►│Siapkan   │
      │topik &   │   │tentukan  │   │tujuan &   │   │alat &    │
      │masalah   │   │anggota   │   │anggaran   │   │bahan     │
      └──────────┘   └──────────┘   └──────────┘   └──────────┘
    ```

    ### Template Perencanaan Proyek

    **1. Identitas Proyek**
    | Item | Isian |
    |------|-------|
    | Nama Proyek | |
    | Anggota Tim | 1. ..., 2. ..., 3. ... |
    | Kelas | |
    | Tanggal Mulai | |
    | Tanggal Selesai | |

    **2. Masalah & Solusi**
    | Pertanyaan | Jawaban |
    |-----------|---------|
    | Masalah apa yang ingin diselesaikan? | |
    | Siapa yang merasakan masalah ini? | |
    | Mengapa ini penting? | |
    | Solusi apa yang ditawarkan? | |
    | Teknologi apa yang digunakan? | Scratch, Canva, dll |

    **3. Tujuan SMART**
    | Kriteria | Contoh |
    |----------|--------|
    | **S**pecific | Membuat game kuis Informatika dengan Scratch |
    | **M**easurable | 10 soal interaktif dengan skor |
    | **A**chievable | Dengan Scratch, dalam 2 minggu |
    | **R**elevant | Untuk belajar Informatika kelas X |
    | **T**ime-bound | Selesai 2 Desember 2026 |

    **4. Timeline / Jadwal**
    | Minggu | Kegiatan | Output |
    |--------|----------|--------|
    | 1 | Brainstorming ide & pembagian tim | Proposal ide |
    | 2 | Desain & perencanaan | Storyboard/flowchart |
    | 3-4 | Implementasi (coding Scratch) | Prototipe |
    | 5 | Uji coba & perbaikan | Program siap |
    | 6 | Dokumentasi & presentasi | Laporan & slide |

    **5. Alat & Bahan**
    | Kebutuhan | Detail |
    |-----------|--------|
    | **Software** | Scratch (online/offline), Canva |
    | **Hardware** | Laptop/komputer, koneksi internet |
    | **Lainnya** | Buku catatan, pulpen, flashdisk |

    ### 📌 Contoh Nyata

    **Proyek "Aplikasi PPDB Online"** — Sebenarnya ini proyek besar pemerintah. Tapi kalau disederhanakan untuk proyek kelas, kalian bisa:
    - Membuat **prototipe** (tampilan) PPDB di Canva
    - Membuat **animasi simulasi** pendaftaran di Scratch
    - Membuat **poster sosialisasi** digital

    ### 🔍 Cek Pemahaman
    1. Sebutkan 4 langkah perencanaan proyek TIK!
    2. Apa yang dimaksud dengan tujuan SMART? Sebutkan kepanjangannya!
    3. Mengapa perencanaan penting dalam sebuah proyek?

    ### 📋 Studi Kasus
    OSIS sekolah ingin membuat website sederhana untuk informasi kegiatan sekolah. Mereka memiliki waktu 1 bulan, dana Rp500.000, dan tim 5 orang yang semuanya masih pemula di bidang IT.

    **Pertanyaan:**
    1. Bantu OSIS membuat perencanaan proyek menggunakan template yang sudah dipelajari (identitas, masalah, tujuan SMART, timeline, alat)!
    2. Menurutmu, apakah target 1 bulan realistis untuk tim pemula? Jelaskan!

    > 🤔 **Refleksi:** Coba buat perencanaan proyek sederhana untuk "Membuat konten edukasi tentang anti-hoaks untuk media sosial"!
    """)


def content_presentasi_refleksi():
    return dedent("""
    ### 🎤 Presentasi dan Refleksi Proyek

    **Presentasi** adalah cara menyampaikan hasil proyek kepada orang lain. **Refleksi** adalah merenungkan apa yang sudah dipelajari. Keduanya sama pentingnya dengan pengerjaan proyek itu sendiri!

    > 🧩 **Analogi:** Presentasi dan refleksi itu seperti **pameran seni**. Kamu bukan cuma memajang lukisan — kamu juga menceritakan inspirasi, proses, dan pelajaran di baliknya. Penonton tidak hanya melihat karya, tapi juga **perjalananmu**.

    ### Struktur Presentasi

    ```
      ⏱️ Total: 10 menit per kelompok

      1. PEMBUKAAN (1 menit)
         - Salam, perkenalan anggota
         - Judul proyek

      2. LATAR BELAKANG (2 menit)
         - Masalah yang diangkat
         - Mengapa masalah ini penting

      3. PROSES PENGERJAAN (3 menit)
         - Perencanaan → implementasi → uji coba
         - Peran masing-masing anggota
         - Kendala dan solusi

      4. DEMO (3 menit)
         - Tunjukkan hasil karya!
         - Jalankan program/animasi

      5. PENUTUP (1 menit)
         - Kesimpulan
         - Refleksi tim
         - Saran untuk pengembangan
    ```

    ### Tips Presentasi yang Baik

    ```
      🎯  Kuasai materi — kamu yang membuatnya, pasti bisa!
      👁️  Kontak mata dengan audiens, jangan baca terus
      🗣️  Bicara jelas, tidak terlalu cepat
      🖼️  Slide sederhana — jangan penuh teks
      🎬  Demo harus sudah siap — jangan sambil loading!
      ❓  Siapkan jawaban untuk pertanyaan yang mungkin muncul
      😊  Santai dan percaya diri!
    ```

    ### Rubrik Penilaian Presentasi

    | Aspek | Sangat Baik (4) | Baik (3) | Cukup (2) | Kurang (1) |
    |-------|-----------------|----------|-----------|------------|
    | **Konten** | Lengkap, akurat, terstruktur | Lengkap | Kurang lengkap | Tidak jelas |
    | **Demo** | Berjalan sempurna | Sedikit kendala | Sebagian berjalan | Tidak jalan |
    | **Komunikasi** | Jelas, percaya diri | Jelas | Kurang jelas | Tidak siap |
    | **Visual** | Menarik & informatif | Cukup menarik | Kurang menarik | Tidak ada |

    ### Pertanyaan Refleksi untuk Tim

    Setelah presentasi, jawab pertanyaan berikut secara individu:

    ```
      1.  Apa kontribusiku dalam proyek ini?
      2.  Hal baru apa yang aku pelajari?
      3.  Apa bagian tersulit dan bagaimana aku mengatasinya?
      4.  Jika bisa mengulang, apa yang akan aku lakukan berbeda?
      5.  Apa yang paling membanggakan dari proyek ini?
      6.  Bagaimana proyek ini menghubungkan materi informatika dengan kehidupan nyata?
      7.  Skill 4C mana yang paling terasah? (Critical, Creative, Collaborative, Communicative)
    ```

    ### Format Laporan Proyek

    | Bab | Isi |
    |-----|-----|
    | **Halaman Judul** | Nama proyek, logo, anggota, kelas |
    | **Bab 1: Pendahuluan** | Latar belakang, rumusan masalah, tujuan |
    | **Bab 2: Perencanaan** | Alat & bahan, jadwal, pembagian peran |
    | **Bab 3: Implementasi** | Screenshot/kode/dokumentasi proses |
    | **Bab 4: Hasil & Pembahasan** | Demo, kendala, solusi |
    | **Bab 5: Penutup** | Kesimpulan, saran, refleksi |
    | **Lampiran** | Dokumentasi lengkap, link program |

    ### 📌 Contoh Nyata

    **Presentasi di kelas:** Kelompok A membuat "Game Edukasi Tebak Nama Pahlawan" dengan Scratch. Saat demo, ada bug — skor tidak bertambah. Anggota tim langsung menjelaskan: "Kami menemukan bug ini saat uji coba dan belum sempat diperbaiki. Seharusnya di blok 'if touching' ditambah variabel skor."

    ❓ **Guru bertanya:** "Apa yang kalian pelajari dari bug ini?"
    ✅ **Jawaban:** "Kami belajar pentingnya pengujian menyeluruh — jangan hanya uji satu skenario!"

    **Itulah refleksi!** 🎉

    ### 🔍 Cek Pemahaman
    1. Sebutkan 5 struktur presentasi proyek yang baik beserta durasinya!
    2. Sebutkan 4 aspek yang dinilai dalam rubrik penilaian presentasi!
    3. Mengapa refleksi sama pentingnya dengan pengerjaan proyek itu sendiri?

    ### 📋 Studi Kasus
    Kelompok B mempresentasikan proyek game Scratch mereka. Saat demo, game tiba-tiba error dan tidak mau jalan. Anggota kelompok panik dan hanya diam, sementara slide presentasi mereka penuh teks dan sulit dibaca.

    **Pertanyaan:**
    1. Berdasarkan tips presentasi yang baik, apa yang seharusnya dilakukan kelompok B saat demo error?
    2. Jika kamu menjadi anggota kelompok B, apa yang akan kamu tingkatkan untuk presentasi selanjutnya?

    > 🤔 **Refleksi:** Setelah menyelesaikan semua bab, apa perubahan terbesar dalam cara pandangmu terhadap Informatika? Tuliskan di jurnal belajarmu!
    """)


# ─── CONTENT MAP ──────────────────────────────────────────────

CONTENT_MAP = {
    "mengenal_informatika": content_mengenal_informatika,
    "keterampilan_generik": content_keterampilan_generik,
    "profesi_karier": content_profesi_karier,
    "dasar_bk": content_dasar_bk,
    "dekomposisi_pola": content_dekomposisi_pola,
    "abstraksi_algoritma": content_abstraksi_algoritma,
    "sejarah_tik": content_sejarah_tik,
    "perangkat_tik": content_perangkat_tik,
    "pemanfaatan_tik": content_pemanfaatan_tik,
    "hardware": content_hardware,
    "software": content_software,
    "sistem_operasi": content_sistem_operasi,
    "dasar_jaringan": content_dasar_jaringan,
    "internet": content_internet,
    "keamanan_dunia_maya": content_keamanan_dunia_maya,
    "data_informasi": content_data_informasi,
    "spreadsheet": content_spreadsheet,
    "visualisasi_data": content_visualisasi_data,
    "logika_algoritma": content_logika_algoritma,
    "flowchart": content_flowchart,
    "scratch": content_scratch,
    "proyek_scratch": content_proyek_scratch,
    "dampak_positif": content_dampak_positif,
    "dampak_negatif": content_dampak_negatif,
    "etika_digital": content_etika_digital,
    "kolaborasi": content_kolaborasi,
    "perencanaan_proyek": content_perencanaan_proyek,
    "presentasi_refleksi": content_presentasi_refleksi,
}

# ─── SUB CHAPTER KEYWORDS ─────────────────────────────────────

SUB_KEYS = {
    "1_A": "mengenal_informatika", "1_B": "keterampilan_generik", "1_C": "profesi_karier",
    "2_A": "dasar_bk", "2_B": "dekomposisi_pola", "2_C": "abstraksi_algoritma",
    "3_A": "sejarah_tik", "3_B": "perangkat_tik", "3_C": "pemanfaatan_tik",
    "4_A": "hardware", "4_B": "software", "4_C": "sistem_operasi",
    "5_A": "dasar_jaringan", "5_B": "internet", "5_C": "keamanan_dunia_maya",
    "6_A": "data_informasi", "6_B": "spreadsheet", "6_C": "visualisasi_data",
    "7_A": "logika_algoritma", "7_B": "flowchart", "7_C": "scratch", "7_D": "proyek_scratch",
    "8_A": "dampak_positif", "8_B": "dampak_negatif", "8_C": "etika_digital",
    "9_A": "kolaborasi", "9_B": "perencanaan_proyek", "9_C": "presentasi_refleksi",
}


# ─── GENERATE ──────────────────────────────────────────────────

def generate_all():
    print("=" * 60)
    print("GENERATOR MATERI AJAR KELAS X")
    print("9 Bab — Informatika SMA Negeri 6 Cimahi")
    print("=" * 60)

    total_lines = 0

    for bab in BAB:
        k = bab["id"]
        judul = bab["judul"]
        emoji = bab["emoji"]
        smt = bab["smt"]
        sub = bab["sub"]
        idx = int(k) - 1

        lines = []
        lines.append(f"# {emoji} Bab {k}: {judul}")
        lines.append("")
        lines.append(f"> **Semester {'Ganjil' if smt == 1 else 'Genap'}** | **Fase E** | **Kelas X** | **{len(sub)*5} JP**")
        lines.append("")
        lines.append("---")
        lines.append("")

        # Pemetaan CP
        lines.append("## 📊 Pemetaan Capaian Pembelajaran\n")
        lines.append("| Elemen CP | Deskripsi CP |")
        lines.append("|-----------|-------------|")
        for elemen, desc in CP_MAP.get(k, []):
            lines.append(f"| {elemen} | {desc} |")
        lines.append("")
        lines.append("---")
        lines.append("")

        # Tujuan
        lines.append("## 🎯 Tujuan Pembelajaran\n")
        for h, jdl in sub:
            lines.append(f"- **{h}.** {jdl}")
        lines.append("")

        # Peta Konsep
        lines.append("## 🗺️ Peta Konsep\n")
        lines.append("```")
        lines.append(f"               {emoji} {judul.upper()}")
        lines.append(f"                     |")
        for i, (h, jdl) in enumerate(sub):
            prefix = "                     ├──" if i < len(sub)-1 else "                     └──"
            lines.append(f"{prefix} {h}. {jdl}")
        lines.append("```\n")

        # Content for each sub
        for h, jdl in sub:
            key = SUB_KEYS.get(f"{k}_{h}", "")
            content_fn = CONTENT_MAP.get(key, None)
            lines.append(f"## {h}. {jdl}\n")
            if content_fn:
                lines.append(content_fn())
            else:
                lines.append(f"*[Materi {jdl} sedang dikembangkan]*\n")
            lines.append("")
            lines.append("> 🤔 **Mari Renungkan:** Apa hal paling menarik yang kamu pelajari dari bagian ini?\n")
            lines.append("---\n")

        # Proyek Mini
        proyek = PROYEK.get(k)
        if proyek:
            lines.append("---")
            lines.append(f"## 🏗️ Proyek Mini: {proyek['judul']}\n")
            lines.append(f"{proyek['deskripsi']}\n")
            lines.append("**Alat dan Bahan:**")
            for alat in proyek['alat']:
                lines.append(f"- {alat}")
            lines.append("")
            lines.append("**Langkah-langkah:**")
            for i, langkah in enumerate(proyek['langkah'], 1):
                lines.append(f"{i}. {langkah}")
            lines.append("")
            lines.append(f"> **Output:** {proyek['output']}")
            lines.append("")
            lines.append("---")
            lines.append("")

        # Rangkuman
        lines.append("## 📝 Rangkuman\n")
        for point in RANGKUMAN.get(k, []):
            lines.append(f"- {point}")
        lines.append("")

        # Latihan
        lines.append("---\n")
        lines.append("## ✍️ Latihan Soal\n")
        lines.append("### A. Pilihan Ganda\n")
        for i, (q, opts, ans) in enumerate(SOAL_PG.get(k, []), 1):
            lines.append(f"{i}. {q}")
            for opt in opts:
                lines.append(f"   {opt}")
            lines.append(f"   **Kunci Jawaban: {ans.upper()}**")
            lines.append("")
        lines.append("### B. Uraian\n")
        for i, q in enumerate(SOAL_URAIAN.get(k, []), 1):
            lines.append(f"{i}. {q}")
            lines.append("")

        # Rubrik
        rubrik = RUBRIK.get(k)
        if rubrik:
            lines.append("---")
            lines.append("## 📋 Rubrik Penilaian Proyek\n")
            lines.append("| Aspek | Kurang | Cukup | Baik |")
            lines.append("|-------|--------|-------|------|")
            for i in range(len(rubrik['aspek'])):
                lines.append(f"| {rubrik['aspek'][i]} | {rubrik['level1'][i]} | {rubrik['level2'][i]} | {rubrik['level3'][i]} |")
            lines.append("")
            lines.append("---")
            lines.append("")

        # Pengayaan
        pengayaan = PENGAYAAN.get(k, [])
        if pengayaan:
            lines.append("## 🚀 Tugas Pengayaan\n")
            for tugas_judul, desc in pengayaan:
                lines.append(f"### {tugas_judul}")
                lines.append(f"{desc}\n")
            lines.append("---")
            lines.append("")

        lines.append("## 📖 Glosarium\n")
        for term, defn in GLOSARIUM.get(k, []):
            lines.append(f"- **{term}**: {defn}")
        lines.append("")

        lines.append("---")
        lines.append("## 📺 Sumber & Media Pembelajaran\n")
        lines.append("| Platform | Sumber | Tautan | Keterangan |")
        lines.append("|----------|--------|--------|------------|")
        for platform, nama, link, ket in MEDIA.get(k, []):
            lines.append(f"| {platform} | {nama} | `{link}` | {ket} |")
        lines.append("")

        out = "\n".join(lines)

        fname = f"Bab_{k}_{judul.replace(' ','_')}.md"
        fp = os.path.join(BASE, fname)
        with open(fp, "w", encoding="utf-8") as f:
            f.write(out)

        n_lines = out.count("\n") + 1
        total_lines += n_lines
        print(f"  ✓ Bab {k}: {emoji} {judul} ({n_lines} baris)")

    print(f"\n  → {len(BAB)} file Materi Ajar dibuat.")
    print(f"  → Total: ~{total_lines} baris")
    print("=" * 60)


if __name__ == "__main__":
    generate_all()
