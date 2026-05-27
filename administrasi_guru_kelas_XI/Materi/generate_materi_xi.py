#!/usr/bin/env python3
"""Generator Materi Ajar menarik — Informatika Kelas XI (6 Bab, Edisi Revisi)."""
import os, textwrap

BASE = "/home/daniarsyah/Documents/kerja_2026-2027/administrasi_guru_kelas_XI/Materi"
os.makedirs(BASE, exist_ok=True)

BAB = [
    {"id":"1","judul":"Tentang Informatika","emoji":"📖","smt":1,
     "sub":[("A","8 Elemen Informatika & STEAM"),("B","Profesi dan Karier di Bidang Informatika"),("C","Praktik Lintas Bidang dalam Informatika")]},
    {"id":"2","judul":"Strategi Algoritmik dan Pemrograman","emoji":"⚙️","smt":1,
     "sub":[("A","Proses Pemrograman & Efisiensi Algoritma"),("B","Rekursi: Fungsi yang Memanggil Dirinya Sendiri"),("C","Algoritma Greedy: Pilihan Terbaik Saat Ini"),("D","Pemrograman Dinamis: Optimasi dengan Subproblem"),("E","Array, String, dan Manipulasi Data"),("F","Perbandingan Strategi Algoritmik")]},
    {"id":"3","judul":"Berpikir Kritis dan Dampak Sosial Informatika","emoji":"🔍","smt":1,
     "sub":[("A","Literasi Digital & Verifikasi Informasi"),("B","Membaca Lateral: Evaluasi Sumber Digital"),("C","Dampak Sosial TIK di Masyarakat"),("D","Debat & Argumen Kritis Dampak TIK")]},
    {"id":"4","judul":"Jaringan Komputer dan Internet","emoji":"🌐","smt":2,
     "sub":[("A","Pengantar Jaringan & Topologi"),("B","OSI Layer & Mekanisme Pertukaran Data"),("C","Cyber Security: Ancaman & Mitigasi"),("D","Tata Kelola Akses Data"),("E","Praktik Packet Tracer")]},
    {"id":"5","judul":"Pengembangan Aplikasi Mobile dengan Library AI","emoji":"📱","smt":2,
     "sub":[("A","Pengantar Aplikasi Mobile"),("B","Membangun UI dengan App Inventor"),("C","Navigasi & Penyimpanan Data"),("D","Integrasi Library AI ke Aplikasi"),("E","Image Classification & Speech Recognition"),("F","Proyek Aplikasi AI: Perencanaan"),("G","Proyek Aplikasi AI: Implementasi & Presentasi")]},
    {"id":"6","judul":"Proyek Analisis Data","emoji":"📊","smt":2,
     "sub":[("A","Big Data: Era Data Raksasa"),("B","Pengolahan Data dengan Tools Digital"),("C","Visualisasi Data yang Menarik"),("D","Proyek Analisis Data: Desain"),("E","Proyek Analisis Data: Implementasi")]},
]

# ─── SOAL PILIHAN GANDA ─────────────────────────────────────────
SOAL_PG = {
    "1": [
        ("Berikut ini yang **bukan** merupakan elemen Informatika adalah...",
         ["a. Berpikir Komputasional (BK)", "b. Teknologi Informasi dan Komunikasi (TIK)",
          "c. Sistem Komputer (SK)", "d. Jaringan Komputer dan Internet (JKI)",
          "e. Animasi dan Desain Grafis (ADG)"], "e"),
        ("STEAM merupakan singkatan dari...",
         ["a. Science, Technology, Engineering, Arts, Mathematics",
          "b. Science, Theory, Engineering, Arts, Mathematics",
          "c. System, Technology, Engineering, Arts, Management",
          "d. Science, Technology, Education, Arts, Mathematics",
          "e. Social, Technology, Engineering, Arts, Mathematics"], "a"),
        ("Contoh penerapan informatika di bidang seni (Arts) adalah...",
         ["a. Simulasi gerak planet dengan Python", "b. Metode agile dalam rekayasa perangkat lunak",
          "c. Desain UI/UX dan animasi dengan Figma dan Blender", "d. Analisis data percobaan fisika",
          "e. Sorting dan graph theory"], "c"),
        ("Profesi IT yang bertugas melindungi sistem dari serangan digital disebut...",
         ["a. Software Engineer", "b. Data Scientist", "c. Network Engineer",
          "d. Cyber Security Analyst", "e. DevOps Engineer"], "d"),
        ("Dalam 8 elemen Informatika, elemen yang membahas dampak sosial teknologi informasi adalah...",
         ["a. Analisis Data (AD)", "b. Algoritma dan Pemrograman (AP)",
          "c. Dampak Sosial Informatika (DSI)", "d. Praktik Lintas Bidang (PLB)",
          "e. Berpikir Komputasional (BK)"], "c"),
    ],
    "2": [
        ("Kompleksitas algoritma O(n\u00b2) berarti waktu eksekusi berbanding lurus dengan...",
         ["a. Konstanta, tidak tergantung data", "b. Jumlah data (n)",
          "c. Kuadrat jumlah data (n\u00b2)", "d. Logaritma jumlah data (log n)",
          "e. Eksponensial jumlah data (2\u207f)"], "c"),
        ("Dalam fungsi rekursif, kondisi yang menghentikan pemanggilan diri sendiri disebut...",
         ["a. Recursive case", "b. Base case", "c. Loop condition", "d. Stack frame",
          "e. Infinite recursion"], "b"),
        ("Algoritma greedy selalu mengambil pilihan...",
         ["a. Terbaik secara keseluruhan (global optimal)", "b. Terbaik pada saat itu (lokal optimal)",
          "c. Pilihan acak", "d. Pilihan yang paling rumit", "e. Pilihan yang paling sederhana"], "b"),
        ("Teknik menyimpan hasil sub-masalah untuk digunakan kembali disebut...",
         ["a. Rekursi", "b. Iterasi", "c. Memoisasi (Memoization)", "d. Branching", "e. Sorting"], "c"),
        ("Dalam array Python, indeks elemen pertama adalah...",
         ["a. -1", "b. 0", "c. 1", "d. 2", "e. Tergantung panjang array"], "b"),
    ],
    "3": [
        ("Teknik membaca secara 'menyamping' dengan membuka tab baru untuk mengecek kredibilitas sumber disebut...",
         ["a. Vertical reading", "b. Deep reading", "c. Lateral reading", "d. Speed reading",
          "e. Skimming"], "c"),
        ("Berikut ini adalah tools verifikasi informasi, **kecuali**...",
         ["a. Google Image Search", "b. TinEye", "c. TurnBackHoax", "d. Instagram",
          "e. cekfakta.com"], "d"),
        ("Dampak negatif TIK di bidang sosial adalah...",
         ["a. Akses pendidikan global", "b. Telemedicine", "c. Cyberbullying di media sosial",
          "d. Marketplace dan cashless", "e. E-government"], "c"),
        ("Dalam struktur argumen kritis, 'Warrant' berarti...",
         ["a. Pernyataan yang diyakini", "b. Fakta/angka yang mendukung",
          "c. Logika yang menghubungkan data dengan klaim", "d. Batasan kebenaran argumen",
          "e. Jawaban untuk argumen lawan"], "c"),
        ("Hoaks menyebar lebih cepat dari berita benar karena...",
         ["a. Hoaks selalu lebih panjang", "b. Hoaks lebih menarik secara emosional dan mudah dipercaya",
          "c. Hoaks hanya beredar di WhatsApp", "d. Pemerintah menyebarkan hoaks",
          "e. Media sosial hanya menampilkan hoaks"], "b"),
    ],
    "4": [
        ("Topologi jaringan yang paling umum digunakan pada jaringan sekolah saat ini adalah...",
         ["a. Bus", "b. Ring", "c. Star", "d. Mesh", "e. Tree"], "c"),
        ("Layer OSI yang bertanggung jawab untuk routing dan pengalamatan IP adalah...",
         ["a. Physical Layer", "b. Data Link Layer", "c. Network Layer", "d. Transport Layer",
          "e. Application Layer"], "c"),
        ("Serangan cyber berupa pemancingan data pribadi melalui email palsu disebut...",
         ["a. Malware", "b. Phishing", "c. DDoS", "d. SQL Injection", "e. Social Engineering"], "b"),
        ("Prinsip keamanan yang menyatakan 'beri akses seminimal mungkin' disebut...",
         ["a. Need to Know", "b. Separation of Duties", "c. Audit Trail", "d. Least Privilege",
          "e. Zero Trust"], "d"),
        ("Perintah Cisco untuk menguji koneksi ke IP tujuan adalah...",
         ["a. ipconfig", "b. tracert", "c. ping", "d. show ip route", "e. netstat"], "c"),
    ],
    "5": [
        ("MIT App Inventor adalah platform untuk membuat aplikasi...",
         ["a. iOS native", "b. Android native dengan drag-and-drop", "c. Web app dengan JavaScript",
          "d. Desktop app dengan Python", "e. Hybrid app dengan React Native"], "b"),
        ("Komponen App Inventor yang berfungsi menyimpan data lokal secara key-value adalah...",
         ["a. Notifier", "b. TextBox", "c. TinyDB", "d. ListView", "e. Balloon"], "c"),
        ("Library AI pada App Inventor yang berfungsi mengenali objek di gambar adalah...",
         ["a. TextToSpeech", "b. TranslateExtension", "c. SoundExtension", "d. LookExtension",
          "e. PersonalImageClassifier"], "d"),
        ("CNN dalam konteks AI adalah singkatan dari...",
         ["a. Central Neural Network", "b. Convolutional Neural Network", "c. Computer Network Node",
          "d. Complex Numerical Notation", "e. Continuous Natural Network"], "b"),
        ("Extension App Inventor memiliki ekstensi file...",
         ["a. .apk", "b. .aix", "c. .app", "d. .aia", "e. .exe"], "b"),
    ],
    "6": [
        ("Berikut ini yang **bukan** termasuk 5V Big Data adalah...",
         ["a. Volume", "b. Velocity", "c. Variety", "d. Visibility", "e. Value"], "d"),
        ("Library Python yang paling umum digunakan untuk pengolahan data adalah...",
         ["a. NumPy", "b. Pandas", "c. Matplotlib", "d. Scikit-learn", "e. Requests"], "b"),
        ("Tahap pertama dalam siklus pengolahan data adalah...",
         ["a. Visualisasi", "b. Analisis", "c. Koleksi data", "d. Pembersihan data", "e. Pelaporan"], "c"),
        ("Visualisasi bar chart paling cocok digunakan untuk...",
         ["a. Menunjukkan tren dari waktu ke waktu", "b. Membandingkan nilai antar kategori",
          "c. Menunjukkan proporsi dari total", "d. Menunjukkan konsentrasi data geografis",
          "e. Menampilkan data detail dalam tabel"], "b"),
        ("Sumber Big Data yang menghasilkan 500 jam konten per menit adalah...",
         ["a. Media sosial (Twitter)", "b. Transaksi e-commerce", "c. Video (YouTube/CCTV)",
          "d. Sensor IoT", "e. Kesehatan (rekam medis)"], "c"),
    ],
}

# ─── SOAL URAIAN ────────────────────────────────────────────────
SOAL_URAIAN = {
    "1": [
        "Jelaskan apa yang dimaksud dengan 8 elemen Informatika dan berikan contoh penerapan dari masing-masing elemen dalam kehidupan sehari-hari!",
        "Bagaimana hubungan antara Informatika dan STEAM? Berikan contoh konkret penerapan STEAM dalam sebuah proyek Informatika!",
        "Sebutkan dan jelaskan minimal 3 profesi di bidang Informatika beserta tugas utamanya! Mengapa profesi-profesi ini penting di era digital?",
        "Berikan contoh bagaimana Informatika dapat diterapkan di bidang ekonomi dan kedokteran! Jelaskan manfaatnya masing-masing!",
    ],
    "2": [
        "Jelaskan perbedaan antara Rekursi dan Iterasi! Kapan sebaiknya menggunakan Rekursi dan kapan menggunakan Iterasi? Berikan contoh masing-masing!",
        "Apa yang dimaksud dengan algoritma Greedy? Jelaskan dengan contoh kasus Activity Selection atau Coin Change!",
        "Bagaimana Dynamic Programming (DP) dapat mengoptimalkan kinerja program? Jelaskan konsep Memoization dengan contoh kasus Fibonacci!",
        "Bandingkan kelebihan dan kekurangan dari Algoritma Greedy, Dynamic Programming, Rekursi, dan Iterasi! Kapan waktu yang tepat menggunakan masing-masing?",
    ],
    "3": [
        "Apa yang dimaksud dengan Literasi Digital? Jelaskan langkah-langkah verifikasi informasi untuk memeriksa kebenaran berita viral di media sosial!",
        "Jelaskan apa itu Lateral Reading dan bagaimana cara melakukannya! Berikan contoh situasi di mana Lateral Reading sangat diperlukan!",
        "Tuliskan 3 dampak positif dan 3 dampak negatif TIK di masyarakat! Berikan contoh nyata untuk masing-masing dampak!",
        "Buatlah sebuah argumen kritis lengkap (Klaim, Data, Warrant, Qualifier, Rebuttal) tentang topik: 'Media sosial lebih banyak dampak negatifnya bagi remaja'!",
    ],
    "4": [
        "Jelaskan perbedaan antara LAN, MAN, dan WAN! Berikan contoh masing-masing dalam konteks kehidupan sehari-hari!",
        "Gambarkan dan jelaskan fungsi dari 7 layer OSI Model! Gunakan mnemonik untuk memudahkan mengingat urutan layer!",
        "Apa saja jenis ancaman cyber security yang perlu diwaspadai? Jelaskan cara mitigasi untuk melindungi data pribadi dari serangan tersebut!",
        "Jelaskan prinsip Least Privilege dan Need to Know dalam tata kelola akses data! Berikan contoh penerapannya di lingkungan sekolah!",
    ],
    "5": [
        "Jelaskan perbedaan antara aplikasi mobile native (iOS/Android) dengan aplikasi hybrid/cross-platform! Apa kelebihan dan kekurangan masing-masing?",
        "Bagaimana cara membangun aplikasi sederhana dengan MIT App Inventor? Jelaskan langkah-langkah dari Designer hingga Blocks!",
        "Apa yang dimaksud dengan Library AI? Jelaskan 3 library AI yang tersedia di App Inventor dan fungsinya masing-masing!",
        "Jelaskan cara kerja Image Classification dan Speech Recognition! Bagaimana kedua teknologi ini dapat diterapkan dalam aplikasi mobile?",
    ],
    "6": [
        "Jelaskan konsep Big Data dan 5V-nya! Berikan contoh sumber Big Data yang ada di Indonesia!",
        "Jelaskan siklus pengolahan data dari koleksi hingga visualisasi! Tools apa saja yang bisa digunakan pada setiap tahap?",
        "Apa pentingnya visualisasi data? Sebutkan dan jelaskan 3 jenis visualisasi data serta kapan waktu yang tepat menggunakannya!",
        "Buatlah rencana proyek analisis data sederhana tentang topik kebiasaan belajar siswa di sekolahmu! Sertakan: pertanyaan penelitian, data yang dikumpulkan, tools, dan output yang dihasilkan!",
    ],
}

# ─── RANGKUMAN ──────────────────────────────────────────────────
RANGKUMAN = {
    "1": [
        "Informatika memiliki **8 elemen**: BK, TIK, SK, JKI, AD, AP, DSI, dan PLB \u2014 semuanya saling melengkapi membentuk bidang ilmu ini.",
        "**STEAM** (Science, Technology, Engineering, Arts, Mathematics) adalah pendekatan yang menghubungkan Informatika dengan berbagai bidang keilmuan.",
        "Terdapat banyak **profesi IT** seperti Software Engineer, Data Scientist, UI/UX Designer, Network Engineer, Cyber Security Analyst, dan AI Engineer dengan prospek karier yang cerah.",
        "Informatika bisa diterapkan di **semua bidang** \u2014 dari sains, seni, ekonomi, hingga kedokteran \u2014 menjadikannya ilmu yang lintas bidang.",
        "Elemen **Praktik Lintas Bidang (PLB)** menekankan bahwa Informatika bukan hanya coding, tapi juga kemampuan memecahkan masalah di berbagai konteks.",
    ],
    "2": [
        "Proses pemrograman terdiri dari 4 tahap: **Analisis \u2192 Desain \u2192 Implementasi \u2192 Pengujian**. Efisiensi algoritma diukur dengan **Big O Notation**.",
        "**Rekursi** adalah fungsi yang memanggil dirinya sendiri, terdiri dari base case dan recursive case. Cocok untuk masalah bertingkat seperti pohon dan fractal.",
        "**Algoritma Greedy** mengambil pilihan terbaik saat ini (lokal optimal) dengan harapan menghasilkan solusi global optimal \u2014 contoh: Coin Change dan Activity Selection.",
        "**Dynamic Programming** menyimpan hasil sub-masalah (Memoization) untuk menghindari perhitungan ulang \u2014 sangat efektif untuk masalah dengan overlapping subproblems.",
        "**Array** adalah struktur data untuk menyimpan kumpulan nilai terindeks, dimulai dari indeks 0. String juga bisa diperlakukan seperti array karakter.",
    ],
    "3": [
        "**Literasi Digital** adalah kemampuan menggunakan teknologi digital secara bijak, termasuk memverifikasi informasi menggunakan teknik **cek sumber, cek fakta, reverse image, dan lateral reading**.",
        "**Lateral Reading** adalah teknik membaca \u2018menyamping\u2019 \u2014 membuka tab baru untuk mengecek kredibilitas sumber sebelum mempercayai informasi.",
        "**TIK** membawa dampak positif (pendidikan global, telemedicine, e-commerce) dan negatif (hoaks, cyberbullying, kecanduan, pelanggaran privasi, kesenjangan digital).",
        "**Argumen Kritis** terdiri dari: Klaim, Data, Warrant, Qualifier, dan Rebuttal. Dalam debat, serang argumen bukan orangnya, gunakan data bukan emosi.",
        "Tools verifikasi informasi seperti **TurnBackHoax, Mafindo, cekfakta.com, dan Google Image Search** membantu kita membedakan hoaks dan fakta.",
    ],
    "4": [
        "Jaringan komputer dibagi menjadi **LAN** (lokal), **MAN** (kota), dan **WAN** (luas). Topologi yang paling umum adalah **Star** karena jika satu kabel putus yang lain tidak terganggu.",
        "**OSI Model** memiliki 7 layer: Physical, Data Link, Network, Transport, Session, Presentation, Application. Setiap layer membungkus data dengan header-nya (enkapsulasi).",
        "**Cyber Security** melindungi sistem dari ancaman seperti Malware, Phishing, DDoS, Man-in-the-Middle, SQL Injection, dan Social Engineering dengan mitigasi seperti 2FA dan password manager.",
        "**Tata kelola akses data** menggunakan model RBAC (Role-Based Access Control) dengan prinsip Least Privilege \u2014 beri akses seminimal mungkin sesuai peran.",
        "**Cisco Packet Tracer** adalah simulator jaringan yang memungkinkan praktik konfigurasi tanpa alat fisik. Perintah dasar: ping, ipconfig, tracert.",
    ],
    "5": [
        "Aplikasi mobile terdiri dari 3 jenis: **Native iOS** (Swift), **Native Android** (Kotlin/Java), dan **Hybrid/Cross-platform** (Flutter, React Native).",
        "**MIT App Inventor** adalah platform drag-and-drop untuk membuat aplikasi Android dengan dua bagian utama: **Designer** (tampilan) dan **Blocks** (logika).",
        "**Library AI** seperti LookExtension, SoundExtension, dan TextToSpeech memungkinkan aplikasi memiliki \u2018panca indera digital\u2019 \u2014 melihat, mendengar, dan berbicara.",
        "**Image Classification** menggunakan CNN untuk mengenali objek di gambar, sedangkan **Speech Recognition** mengubah suara menjadi teks.",
        "Proyek akhir bab ini adalah membuat **aplikasi mobile berbasis AI** untuk menyelesaikan masalah nyata \u2014 mulai dari perencanaan, implementasi di App Inventor, hingga presentasi.",
    ],
    "6": [
        "**Big Data** memiliki 5V: Volume, Velocity, Variety, Veracity, Value. Contoh di Indonesia: Gojek, BPJS Kesehatan, dan e-commerce memproses data raksasa setiap hari.",
        "Siklus pengolahan data: **Koleksi \u2192 Pembersihan (Cleaning) \u2192 Analisis \u2192 Visualisasi & Pelaporan**. Tools: Excel, Google Sheets, Python (Pandas), Tableau.",
        "**Visualisasi data** membantu menyampaikan informasi dengan cepat. Jenis utama: Bar Chart (perbandingan), Line Chart (tren), dan Pie Chart (proporsi).",
        "Proyek analisis data dimulai dengan **perencanaan** (topik, pertanyaan, metode), dilanjutkan implementasi (koleksi data, cleaning, analisis, visualisasi), dan diakhiri **presentasi**.",
        "Visualisasi yang baik harus sederhana, akurat, kontekstual, dengan warna bijak maksimal 5 warna. Hindari 3D chart dan pie chart lebih dari 5 kategori.",
    ],
}

# ─── GLOSARIUM ─────────────────────────────────────────────────
GLOSARIUM = {
    "1": [
        ("8 Elemen Informatika", "Delapan bidang yang membentuk ilmu Informatika: BK, TIK, SK, JKI, AD, AP, DSI, dan PLB."),
        ("STEAM", "Pendekatan interdisipliner: Science, Technology, Engineering, Arts, Mathematics."),
        ("Software Engineer", "Profesi pengembang perangkat lunak yang merancang, coding, dan menguji aplikasi."),
        ("Data Scientist", "Profesi yang menganalisis data besar untuk menghasilkan insight bisnis."),
        ("Cyber Security Analyst", "Profesi yang melindungi sistem dan data dari serangan siber."),
        ("Praktik Lintas Bidang", "Penerapan informatika di berbagai bidang seperti kedokteran, seni, ekonomi, dan sains."),
    ],
    "2": [
        ("Big O Notation", "Notasi yang mengukur efisiensi algoritma berdasarkan pertumbuhan waktu eksekusi terhadap ukuran input."),
        ("Rekursi", "Fungsi yang memanggil dirinya sendiri, terdiri dari base case dan recursive case."),
        ("Algoritma Greedy", "Strategi algoritmik yang mengambil pilihan terbaik pada saat ini (lokal optimal)."),
        ("Dynamic Programming", "Teknik optimasi dengan menyimpan hasil sub-masalah (memoization) untuk menghindari perhitungan ulang."),
        ("Array", "Struktur data yang menyimpan kumpulan nilai dengan tipe data sama, diakses menggunakan indeks."),
        ("Base Case", "Kondisi berhenti dalam fungsi rekursif untuk mencegah infinite loop."),
        ("Memoization", "Teknik menyimpan hasil perhitungan sub-masalah agar tidak dihitung ulang."),
    ],
    "3": [
        ("Literasi Digital", "Kemampuan menggunakan teknologi digital secara bijak, termasuk memverifikasi informasi dan berpikir kritis."),
        ("Lateral Reading", "Teknik verifikasi informasi dengan membuka tab baru untuk mengecek kredibilitas sumber dari berbagai sudut pandang."),
        ("Vertical Reading", "Membaca informasi hanya dari satu sumber tanpa verifikasi silang ke sumber lain."),
        ("Hoaks", "Informasi palsu yang sengaja disebarkan untuk menyesatkan publik, sering kali memicu emosi."),
        ("Cyberbullying", "Perundungan yang terjadi di dunia digital melalui media sosial, pesan, atau platform online."),
        ("Kesenjangan Digital", "Ketimpangan akses dan kemampuan menggunakan teknologi digital antara kelompok masyarakat."),
        ("Argumen Kritis (Toulmin)", "Struktur argumen yang terdiri dari Klaim, Data, Warrant, Qualifier, dan Rebuttal."),
    ],
    "4": [
        ("LAN", "Local Area Network — jaringan komputer dalam area terbatas seperti satu ruangan atau gedung."),
        ("MAN", "Metropolitan Area Network — jaringan komputer yang mencakup satu kota."),
        ("WAN", "Wide Area Network — jaringan komputer yang mencakup area luas antar kota atau negara."),
        ("OSI Model", "Model referensi 7 layer yang menjelaskan proses pertukaran data dalam jaringan komputer."),
        ("Enkapsulasi", "Proses pembungkusan data dengan header di setiap layer OSI sebelum dikirim melalui jaringan."),
        ("Phishing", "Serangan cyber berupa pemancingan data pribadi melalui email atau pesan palsu."),
        ("Malware", "Perangkat lunak berbahaya yang dirancang untuk merusak sistem atau mencuri data."),
        ("Least Privilege", "Prinsip keamanan yang memberikan akses seminimal mungkin kepada pengguna."),
        ("RBAC", "Role-Based Access Control — model kontrol akses berdasarkan peran pengguna dalam organisasi."),
        ("Cisco Packet Tracer", "Software simulasi jaringan untuk merancang dan mengkonfigurasi jaringan tanpa alat fisik."),
    ],
    "5": [
        ("Native App", "Aplikasi yang dibuat khusus untuk satu platform (iOS/Android) menggunakan bahasa spesifik platform."),
        ("Hybrid App", "Aplikasi multi-platform yang dibuat dengan satu basis kode untuk berbagai sistem operasi."),
        ("MIT App Inventor", "Platform drag-and-drop untuk membuat aplikasi Android tanpa coding rumit."),
        ("TinyDB", "Database lokal pada App Inventor yang menyimpan data dalam format key-value."),
        ("Library AI", "Kumpulan fungsi siap pakai untuk menambahkan kecerdasan buatan ke dalam aplikasi."),
        ("CNN", "Convolutional Neural Network — arsitektur jaringan saraf tiruan untuk pengenalan gambar."),
        ("Image Classification", "Teknologi AI yang mengenali dan mengklasifikasikan objek dalam gambar."),
        ("Speech Recognition", "Teknologi yang mengubah suara manusia menjadi teks."),
    ],
    "6": [
        ("Big Data", "Kumpulan data berukuran sangat besar yang tidak dapat diolah dengan metode tradisional."),
        ("5V Big Data", "Karakteristik Big Data: Volume, Velocity, Variety, Veracity, dan Value."),
        ("Data Cleaning", "Proses membersihkan data dari kesalahan, duplikasi, atau nilai kosong sebelum dianalisis."),
        ("Visualisasi Data", "Penyajian data dalam bentuk grafik, diagram, atau peta agar mudah dipahami."),
        ("Pandas", "Library Python untuk manipulasi dan analisis data yang menyediakan struktur DataFrame."),
        ("Bar Chart", "Grafik batang untuk membandingkan nilai antar kategori."),
        ("Line Chart", "Grafik garis untuk menunjukkan tren data dari waktu ke waktu."),
        ("Pie Chart", "Grafik lingkaran untuk menunjukkan proporsi atau bagian dari keseluruhan."),
    ],
}

# ─── MEDIA PEMBELAJARAN ─────────────────────────────────────────
MEDIA = {
    "1": [
        ("YouTube", "Apa itu 8 Elemen Informatika?", "youtu.be/search?q=8+elemen+informatika", "Penjelasan elemen Informatika oleh KEMDIKBUD"),
        ("YouTube", "STEAM Education Explained", "youtu.be/search?q=STEAM+pendidikan", "Video penjelasan STEAM dalam pendidikan"),
        ("Website", "Dicoding — Belajar Coding", "https://www.dicoding.com/", "Platform belajar coding Indonesia"),
        ("Website", "Glints — Karier IT", "https://glints.com/id/", "Informasi lowongan dan profesi IT"),
    ],
    "2": [
        ("YouTube", "Big O Notation dalam 5 Menit", "youtu.be/search?q=Big+O+Notation+indonesia", "Penjelasan efisiensi algoritma"),
        ("Simulasi", "Visualgo — Visualisasi Algoritma", "https://visualgo.net/", "Simulasi visual berbagai algoritma"),
        ("YouTube", "Apa itu Rekursi?", "youtu.be/search?q=rekursi+algoritma", "Penjelasan rekursi dengan animasi"),
        ("YouTube", "Dynamic Programming untuk Pemula", "youtu.be/search?q=dynamic+programming+pemula", "Konsep DP dengan contoh sederhana"),
        ("Website", "HackerRank", "https://www.hackerrank.com/", "Platform latihan soal algoritma dan coding"),
    ],
    "3": [
        ("YouTube", "Literasi Digital untuk Pemula", "youtu.be/search?q=literasi+digital+indonesia", "Video pengenalan literasi digital"),
        ("Website", "TurnBackHoax — Fact Check", "https://turnbackhoax.id/", "Platform verifikasi hoaks Indonesia"),
        ("Website", "Mafindo", "https://www.mafindo.or.id/", "Masyarakat Anti Fitnah Indonesia"),
        ("Website", "cekfakta.com", "https://cekfakta.com/", "Kolaborasi fact-checker Indonesia"),
        ("YouTube", "Cara Lateral Reading", "youtu.be/search?q=lateral+reading+indonesia", "Teknik membaca lateral untuk verifikasi"),
    ],
    "4": [
        ("YouTube", "Apa itu Jaringan Komputer?", "youtu.be/search?q=apa+itu+jaringan+komputer", "Penjelasan dasar jaringan komputer"),
        ("Simulasi", "Cisco Packet Tracer — Tutorial", "youtu.be/search?q=packet+tracer+tutorial+indonesia", "Panduan praktik Packet Tracer"),
        ("YouTube", "OSI Layer Dijelaskan", "youtu.be/search?q=OSI+layer+indonesia", "Penjelasan 7 layer OSI dengan analogi"),
        ("Website", "Cyber Security untuk Remaja", "youtu.be/search?q=cyber+security+dasar", "Tips keamanan digital untuk pelajar"),
        ("Website", "Cisco Networking Academy", "https://www.netacad.com/", "Kursus jaringan gratis dari Cisco"),
    ],
    "5": [
        ("Website", "MIT App Inventor", "https://appinventor.mit.edu/", "Platform resmi MIT App Inventor"),
        ("YouTube", "Tutorial App Inventor Pemula", "youtu.be/search?q=tutorial+app+inventor+indonesia", "Panduan membuat aplikasi dengan App Inventor"),
        ("YouTube", "Apa itu AI? Pengenalan AI", "youtu.be/search?q=apa+itu+AI+indonesia", "Konsep dasar kecerdasan buatan"),
        ("YouTube", "Image Classification dengan AI", "youtu.be/search?q=image+classification+AI", "Cara kerja klasifikasi gambar dengan CNN"),
        ("Website", "AI Extension App Inventor", "https://appinventor.mit.edu/extensions", "Koleksi extension AI untuk App Inventor"),
    ],
    "6": [
        ("YouTube", "Apa itu Big Data?", "youtu.be/search?q=apa+itu+big+data+indonesia", "Penjelasan Big Data dan 5V"),
        ("Website", "Google Data Studio", "https://datastudio.google.com/", "Tools visualisasi data gratis dari Google"),
        ("Website", "Tableau Public", "https://public.tableau.com/", "Platform visualisasi data interaktif"),
        ("YouTube", "Tutorial Python Pandas", "youtu.be/search?q=tutorial+pandas+python+indonesia", "Belajar analisis data dengan Pandas"),
        ("Website", "Google Trends", "https://trends.google.com/", "Tools analisis tren pencarian Google"),
    ],
}

# ─── PEMETAAN CAPAIAN PEMBELAJARAN ────────────────────────────
CP_MAP = {
    "1": [
        ("Berpikir Komputasional (BK)", "Menerapkan strategi algoritmik standar dan berpikir komputasional dalam menyelesaikan persoalan sehari-hari"),
        ("Teknologi Informasi dan Komunikasi (TIK)", "Memahami peran TIK dalam berbagai bidang dan menggunakannya secara bertanggung jawab"),
        ("Dampak Sosial Informatika (DSI)", "Menganalisis dampak sosial dari perkembangan teknologi informasi di masyarakat"),
    ],
    "2": [
        ("Algoritma dan Pemrograman (AP)", "Menerapkan strategi algoritmik (rekursi, greedy, pemrograman dinamis) dan membandingkan efisiensinya dalam pemrograman"),
    ],
    "3": [
        ("Dampak Sosial Informatika (DSI)", "Mengevaluasi informasi digital secara kritis dan menganalisis dampak sosial TIK di masyarakat"),
    ],
    "4": [
        ("Jaringan Komputer dan Internet (JKI)", "Memahami arsitektur jaringan, model OSI, dan menerapkan prinsip keamanan siber dalam tata kelola akses data"),
    ],
    "5": [
        ("Algoritma dan Pemrograman (AP)", "Mengembangkan aplikasi mobile dengan mengintegrasikan library AI untuk menyelesaikan masalah nyata"),
    ],
    "6": [
        ("Analisis Data (AD)", "Menerapkan siklus pengolahan data mulai dari koleksi, pembersihan, analisis, hingga visualisasi"),
    ],
}

# ─── PROYEK MINI ───────────────────────────────────────────────
PROYEK = {
    "1": {
        "judul": "🧠 Mind Map STEAM + Karier",
        "deskripsi": "Buatlah mind map digital yang menghubungkan 8 elemen Informatika dengan bidang STEAM dan profesi IT terkait. Proyek ini membantu kamu melihat gambaran utuh Informatika sebagai ilmu lintas bidang.",
        "alat": ["Canva / MindMeister / XMind / kertas A3+spidol warna", "Buku catatan untuk riset", "Smartphone/laptop untuk mencari referensi"],
        "langkah": [
            "Riset 8 elemen Informatika (BK, TIK, SK, JKI, AD, AP, DSI, PLB) dan catat definisi singkat masing-masing.",
            "Cari minimal 1 contoh penerapan setiap elemen dalam kehidupan nyata.",
            "Hubungkan setiap elemen dengan bidang STEAM yang relevan dan sebutkan profesi IT terkait.",
            "Buat mind map dengan Canva/XMind — pusat: 'Informatika', cabang utama: 8 elemen, sub-cabang: STEAM & profesi.",
            "Tambahkan ikon/ilustrasi dan warna berbeda untuk setiap cabang.",
            "Presentasikan mind map ke kelas dalam 3-5 menit — jelaskan hubungan yang kamu temukan.",
        ],
        "output": "Mind map digital (PDF/JPG) + presentasi lisan 3-5 menit",
    },
    "2": {
        "judul": "⚡ Kuis Interaktif Algoritma",
        "deskripsi": "Buat program Python sederhana yang membandingkan 2 strategi algoritmik (misal: Linear Search vs Binary Search, atau rekursi biasa vs DP Fibonacci). Program harus menampilkan waktu eksekusi dan perbandingan efisiensi.",
        "alat": ["Python 3 (IDLE / VS Code / Google Colab)", "Modul time untuk mengukur kecepatan", "Buku catatan untuk analisis"],
        "langkah": [
            "Pilih 2 algoritma yang akan dibandingkan (contoh: rekursi Fibonacci vs DP Fibonacci, atau Linear Search vs Binary Search).",
            "Implementasikan kedua algoritma dalam fungsi Python yang terpisah.",
            "Gunakan modul `time` untuk mengukur waktu eksekusi masing-masing algoritma dengan berbagai ukuran input.",
            "Buat tabel sederhana yang menampilkan perbandingan waktu eksekusi untuk n = 10, 100, 1000, 10000.",
            "Tambahkan komentar pada kode untuk menjelaskan cara kerja setiap algoritma.",
            "Demo program ke kelas dan jelaskan mengapa algoritma yang lebih efisien lebih unggul.",
        ],
        "output": "File Python (.py) + tabel perbandingan eksekusi + demo lisan",
    },
    "3": {
        "judul": "🔎 Laporan Verifikasi Berita",
        "deskripsi": "Pilih 1 berita viral dari media sosial, lalu verifikasi menggunakan teknik lateral reading dan tools fact-checking. Buat laporan lengkap yang menyimpulkan apakah berita tersebut hoaks atau fakta.",
        "alat": ["Smartphone/laptop dengan akses internet", "Browser (Chrome/Firefox) dengan tab", "Tools: Google Image Search, TinEye, TurnBackHoax, cekfakta.com", "Dokumen (Google Docs / Canva)"],
        "langkah": [
            "Pilih 1 berita viral dari media sosial (WhatsApp, Instagram, TikTok, Twitter) — screenshot berita tersebut.",
            "Identifikasi sumber asli berita: siapa penulis, media apa, kapan diterbitkan.",
            "Lakukan lateral reading: buka tab baru, cari informasi dari 3 sumber berbeda tentang topik yang sama.",
            "Gunakan reverse image search (Google Images / TinEye) untuk mengecek keaslian foto/gambar.",
            "Cek di platform fact-checking (TurnBackHoax, cekfakta.com, Mafindo) apakah berita sudah pernah diverifikasi.",
            "Buat laporan: screenshot berita, langkah verifikasi, kesimpulan (hoaks/fakta), dan saran.",
        ],
        "output": "Laporan verifikasi (PDF/Google Docs) — 1-2 halaman + screenshot",
    },
    "4": {
        "judul": "🌐 Desain + Simulasi Jaringan",
        "deskripsi": "Rancang jaringan komputer untuk 2 laboratorium sekolah menggunakan Cisco Packet Tracer. Konfigurasi IP, routing dasar, dan uji konektivitas antar perangkat dalam jaringan.",
        "alat": ["Cisco Packet Tracer (install di lab atau download)", "Laptop/komputer", "Buku catatan untuk sketsa desain"],
        "langkah": [
            "Buat sketsa desain jaringan di kertas: 2 lab (@10 PC), 1 server, 2 switch, 1 router, koneksi internet.",
            "Buka Cisco Packet Tracer dan tambahkan semua perangkat sesuai sketsa.",
            "Sambungkan perangkat dengan kabel Copper Straight-Through yang sesuai.",
            "Konfigurasi IP address: Lab A (192.168.1.0/24), Lab B (192.168.2.0/24), Router sebagai gateway.",
            "Konfigurasi routing statis di router agar kedua lab bisa saling terhubung.",
            "Uji koneksi dengan perintah `ping` antar PC di lab yang berbeda — dokumentasikan hasilnya.",
        ],
        "output": "File Packet Tracer (.pkt) + laporan konfigurasi + screenshot hasil ping",
    },
    "5": {
        "judul": "🤖 Prototipe Aplikasi AI",
        "deskripsi": "Buat aplikasi Android sederhana di MIT App Inventor yang mengintegrasikan 1 fitur AI (LookExtension untuk klasifikasi gambar, SoundExtension untuk pengenal suara, atau TextToSpeech). Aplikasi harus menyelesaikan masalah nyata.",
        "alat": ["MIT App Inventor (ai2.appinventor.mit.edu)", "Akun Gmail (untuk login)", "Smartphone Android (untuk uji coba)", "AI Extension (.aix): LookExtension / SoundExtension / TextToSpeech"],
        "langkah": [
            "Tentukan masalah nyata yang akan diselesaikan (misal: aplikasi pengenal tanaman obat, atau voice note untuk tunanetra).",
            "Buka MIT App Inventor, buat project baru, dan impor extension AI yang dibutuhkan (.aix).",
            "Desain UI: buat screen utama dengan Button, Label, Kamera, dan komponen lain yang diperlukan.",
            "Buat blok logika: tombol aktifkan AI → tangkap gambar/rekam suara → panggil extension → tampilkan hasil.",
            "Uji coba aplikasi di smartphone Android — catat bug dan perbaiki.",
            "Build APK, presentasikan aplikasi ke kelas — tunjukkan fitur AI bekerja secara real-time.",
        ],
        "output": "File project (.aia) + file APK + presentasi demo 5-7 menit",
    },
    "6": {
        "judul": "📈 Dashboard Data Sederhana",
        "deskripsi": "Analisis dataset kecil (minimal 30 baris) menggunakan Google Sheets atau Python Pandas, lalu buat dashboard visualisasi interaktif. Tema bebas: kebiasaan belajar, pengeluaran harian, atau data lingkungan sekolah.",
        "alat": ["Google Sheets / Microsoft Excel", "(Opsional) Google Colab dengan Python Pandas + Matplotlib", "Google Data Studio / Canva untuk dashboard", "Data survei (Google Forms)"],
        "langkah": [
            "Tentukan topik dan buat pertanyaan penelitian yang ingin dijawab (minimal 2 pertanyaan).",
            "Kumpulkan data menggunakan Google Forms (sebarkan ke teman sekelas) — minimal 30 responden.",
            "Export data ke Google Sheets atau CSV. Lakukan pembersihan data: hapus baris kosong, perbaiki format.",
            "Analisis data: hitung rata-rata, median, nilai maks/min, dan korelasi antar variabel.",
            "Buat visualisasi: 1 bar chart, 1 pie chart, dan 1 line chart atau scatter plot.",
            "Buat dashboard di Google Data Studio/Canva yang merangkum semua temuan dalam 1 halaman.",
        ],
        "output": "File data (CSV) + dashboard visualisasi (PDF/screenshot) + presentasi 5 menit",
    },
}

# ─── RUBRIK PENILAIAN ───────────────────────────────────────────
RUBRIK = {
    "1": {
        "aspek": ["Kelengkapan Elemen", "Pemahaman Konsep", "Visual & Tata Letak", "Presentasi"],
        "level1": ["Kurang dari 5 elemen dibahas", "Konsep keliru atau tidak tepat", "Berantakan, tidak rapi", "Tidak jelas, membaca teks terus"],
        "level2": ["5-7 elemen dibahas dengan baik", "Konsep cukup tepat, kurang detail", "Cukup rapi, ada struktur", "Cukup jelas, kadang membaca catatan"],
        "level3": ["Semua 8 elemen dibahas lengkap", "Konsep tepat, detail, dengan contoh nyata", "Rapi, menarik, warna harmonis, ikon sesuai", "Lancar, percaya diri, interaktif dengan audiens"],
    },
    "2": {
        "aspek": ["Kebenaran Program", "Perbandingan Algoritma", "Dokumentasi Kode", "Presentasi & Demo"],
        "level1": ["Program error atau tidak jalan", "Tidak ada perbandingan yang jelas", "Tanpa komentar, sulit dibaca", "Demo gagal, tidak bisa menjelaskan"],
        "level2": ["Program jalan dengan sedikit bug", "Ada perbandingan tapi kurang detail", "Ada komentar di beberapa bagian", "Demo berjalan, penjelasan cukup jelas"],
        "level3": ["Program jalan sempurna, tidak ada error", "Perbandingan lengkap dengan tabel dan analisis", "Kode rapi, komentar jelas, struktur baik", "Demo lancar, menjelaskan konsep dengan baik"],
    },
    "3": {
        "aspek": ["Ketepatan Verifikasi", "Kelengkapan Analisis", "Penggunaan Tools", "Kualitas Laporan"],
        "level1": ["Hanya 1-2 langkah verifikasi dilakukan", "Analisis dangkal, tanpa kesimpulan jelas", "Tidak menggunakan tools verifikasi", "Laporan tidak terstruktur, banyak typo"],
        "level2": ["3-4 langkah verifikasi dilakukan", "Analisis cukup, kesimpulan ada", "Menggunakan 2-3 tools verifikasi", "Laporan terstruktur, cukup rapi"],
        "level3": ["Semua 5 langkah verifikasi dilakukan", "Analisis mendalam, kesimpulan jelas dan beralasan", "Menggunakan 4+ tools secara optimal", "Laporan profesional, rapi, siap publikasi"],
    },
    "4": {
        "aspek": ["Desain Topologi", "Konfigurasi IP", "Fungsionalitas Jaringan", "Dokumentasi"],
        "level1": ["Topologi tidak sesuai, perangkat kurang", "IP tidak sesuai, tidak ada pemetaan", "Tidak ada koneksi antar perangkat", "Tidak ada dokumentasi"],
        "level2": ["Topologi sesuai, perangkat lengkap", "IP benar untuk satu lab", "Koneksi berhasil dalam satu lab", "Dokumentasi ada tapi kurang detail"],
        "level3": ["Topologi optimal, efisien, dan rapi", "IP benar untuk kedua lab, routing berfungsi", "Semua perangkat terhubung, ping berhasil antar lab", "Dokumentasi lengkap dengan screenshot"],
    },
    "5": {
        "aspek": ["Fungsionalitas Aplikasi", "Fitur AI", "UI/UX Design", "Presentasi Demo"],
        "level1": ["Aplikasi crash atau tidak jalan", "Fitur AI tidak berfungsi", "Tampilan berantakan, sulit digunakan", "Tidak bisa demo, tidak siap"],
        "level2": ["Aplikasi berjalan dengan bug minor", "Fitur AI berfungsi tapi kurang akurat", "Tampilan cukup rapi, mudah digunakan", "Demo berjalan, penjelasan cukup"],
        "level3": ["Aplikasi berjalan sempurna, stabil", "Fitur AI akurat dan responsif", "Tampilan profesional, intuitif, estetis", "Demo lancar, menjelaskan dengan percaya diri"],
    },
    "6": {
        "aspek": ["Kualitas Data", "Analisis & Insight", "Visualisasi", "Dokumentasi & Presentasi"],
        "level1": ["Data < 20 baris, tidak dibersihkan", "Tidak ada analisis, hanya tabel mentah", "Visualisasi asal, tidak sesuai jenis data", "Laporan tidak lengkap, presentasi tidak jelas"],
        "level2": ["Data 20-30 baris, dibersihkan cukup", "Analisis deskriptif dasar (mean, max, min)", "Visualisasi tepat untuk 2 jenis data", "Laporan lengkap, presentasi cukup jelas"],
        "level3": ["Data > 30 baris, bersih, siap analisis", "Analisis mendalam termasuk korelasi", "3+ visualisasi tepat, menarik, informatif", "Laporan profesional, presentasi meyakinkan"],
    },
}

# ─── TUGAS PENGAYAAN ────────────────────────────────────────────
PENGAYAAN = {
    "1": [
        ("🌟 Eksplorasi Karier IT di Dicoding", "Kunjungi [Dicoding](https://www.dicoding.com/) dan pilih 1 learning path yang paling menarik bagimu (misal: Android, Front-End, Machine Learning). Buat ringkasan 1 halaman tentang: apa yang dipelajari di path tersebut, berapa jam estimasi belajar, dan prospek karier setelah menyelesaikannya."),
        ("🎨 Poster 8 Elemen Informatika", "Buat poster informatif (A3) yang menjelaskan 8 elemen Informatika dengan desain kreatif. Setiap elemen harus disertai: nama, ikon, definisi singkat, dan contoh penerapan. Gunakan Canva atau desain manual. Poster akan dipajang di kelas."),
    ],
    "2": [
        ("⚡ Tantangan Coding di HackerRank", "Selesaikan minimal 5 soal algoritma di [HackerRank](https://www.hackerrank.com/) pada kategori *Problem Solving* (mulai dari level Easy). Screenshot hasil submission yang accepted dan catat pendekatan yang kamu gunakan untuk setiap soal. Bandingkan kompleksitas algoritma yang kamu tulis dengan solusi optimal."),
        ("🔄 Visualisasi Algoritma di Visualgo", "Kunjungi [Visualgo.net](https://visualgo.net/) dan pelajari visualisasi dari 3 algoritma: Binary Search, Greedy (Activity Selection), dan Dynamic Programming (Knapsack). Tuliskan penjelasan bagaimana masing-masing algoritma bekerja berdasarkan animasi yang kamu lihat."),
    ],
    "3": [
        ("📰 Cek Fakta dengan Mafindo", "Kunjungi [TurnBackHoax.id](https://turnbackhoax.id/) atau [cekfakta.com](https://cekfakta.com/) dan pilih 1 artikel hasil fact-checking. Analisis: topik berita, sumber berita asli, metode verifikasi yang digunakan, dan kesimpulan. Tulis refleksi: apa yang kamu pelajari dari kasus tersebut?"),
        ("🗣️ Debat Mini Kelas", "Bentuk kelompok pro-kontra (4-5 orang per tim) dan lakukan debat selama 10 menit tentang topik: *'Penggunaan AI di sekolah lebih banyak manfaatnya daripada risikonya'*. Gunakan struktur Toulmin (Klaim, Data, Warrant, Qualifier, Rebuttal). Nilai berdasarkan kekuatan argumen, bukan kemenangan."),
    ],
    "4": [
        ("🌐 Kursus Jaringan di Cisco NetAcad", "Daftar dan mulai modul *Introduction to Networks* di [Cisco Networking Academy](https://www.netacad.com/) (gratis). Selesaikan modul 1-3 dan catat: 3 konsep baru yang kamu pelajari, 1 hal yang paling menarik, dan 1 pertanyaan yang masih mengganjal."),
        ("🔐 Tantangan Cyber Security", "Pelajari dasar-dasar cyber security melalui [Cisco CyberOps Associate](https://www.netacad.com/) atau artikel di [NCSC Indonesia](https://www.bssn.go.id/). Buat poster infografis tip keamanan digital untuk remaja — minimal 5 tips dengan ilustrasi menarik."),
    ],
    "5": [
        ("📱 Eksplorasi Extension AI App Inventor", "Jelajahi halaman [MIT App Inventor Extensions](https://appinventor.mit.edu/extensions) dan cari 3 extension AI yang belum dibahas di kelas. Untuk setiap extension, tulis: nama, fungsi, cara kerja, dan 1 ide aplikasi yang bisa dibuat menggunakan extension tersebut."),
        ("🤖 Tutorial AI untuk Pemula", "Tonton video YouTube *'Cara Kerja Neural Network'* dan *'Apa itu CNN?'* (cari dengan bahasa Indonesia). Buat mind map konsep AI yang mencakup: Neural Network, CNN, Training Data, Confidence Score, dan contoh penerapan di kehidupan sehari-hari."),
    ],
    "6": [
        ("📊 Dashboard Data Publik", "Kunjungi [data.go.id](https://data.go.id/) (Portal Data Terbuka Indonesia) dan unduh 1 dataset yang menarik bagimu. Gunakan Google Sheets atau Python untuk membuat: 1 bar chart, 1 line chart, dan 1 dashboard sederhana. Tulis 3 insight yang kamu temukan dari data tersebut."),
        ("🏆 Tantangan Analisis Data", "Selesaikan tutorial *'Pandas for Data Analysis'* di [Kaggle](https://www.kaggle.com/learn) atau [Dicoding](https://www.dicoding.com/). Kerjakan latihan yang disediakan dan screenshot hasilnya. Catat: fungsi/library baru apa yang kamu pelajari di luar materi kelas?"),
    ],
}

def dedent(s):
    return textwrap.dedent(s).strip()

# ─── BAB 1: Tentang Informatika ───────────────────────────────

def c1_a():
    return dedent("""
    ### 📖 8 Elemen Informatika & STEAM
    Informatika bukan cuma tentang coding! Ada **8 elemen** yang saling terkait membentuk bidang ilmu ini.

    > 🧩 **Analogi:** Informatika itu seperti **tim sepak bola**. Setiap pemain punya posisi dan peran berbeda, tapi semuanya bekerja sama untuk satu tujuan. Begitu juga 8 elemen Informatika — mereka berbeda tapi saling melengkapi.

    ### 8 Elemen Informatika
    ```
      ┌──────────────────────────────────────────────────────┐
      │                  8 ELEMEN INFORMATIKA                │
      ├──────────┬──────────┬──────────┬─────────────────────┤
      │    BK    │   TIK    │    SK    │    JKI              │
      │ Berpikir │ Teknologi│  Sistem  │ Jaringan Komputer   │
      │ Komputasi│ Informasi│ Komputer │ dan Internet        │
      │   onal   │ & Komuni │          │                     │
      │          │   kasi   │          │                     │
      ├──────────┼──────────┼──────────┼─────────────────────┤
      │    AD    │   AP     │   DSI    │    PLB              │
      │ Analisis │ Algoritma│ Dampak   │ Praktik Lintas      │
      │   Data   │ dan      │ Sosial   │ Bidang              │
      │          │ Pemrogram│ Informati│                     │
      │          │   an     │   ka     │                     │
      └──────────┴──────────┴──────────┴─────────────────────┘
    ```

    ### Hubungan dengan STEAM
    **STEAM** = **S**cience, **T**echnology, **E**ngineering, **A**rts, **M**athematics.
    Informatika adalah jembatan yang menghubungkan semua bidang STEAM!

    | Bidang STEAM | Kaitan dengan Informatika | Contoh |
    |--------------|--------------------------|--------|
    | **Science** | Simulasi ilmiah, bioinformatika | Simulasi gerak planet dengan Python |
    | **Technology** | Inti dari Informatika itu sendiri | Coding, jaringan, AI |
    | **Engineering** | Rekayasa perangkat lunak | Metode agile, prototyping |
    | **Arts** | Desain UI/UX, animasi, game | Figma, Blender, Unity |
    | **Mathematics** | Logika, algoritma, struktur data | Sorting, graph theory |

    > 🔑 **Pesan Penting:** Memahami 8 elemen membantu kamu melihat gambaran besar Informatika — bukan coder, tapi **pemecah masalah**!

    ### 🔍 Cek Pemahaman
    1. Sebutkan 4 dari 8 elemen Informatika! Jelaskan fungsi masing-masing secara singkat.
    2. Bagaimana elemen Berpikir Komputasional (BK) berbeda dari elemen Teknologi Informasi dan Komunikasi (TIK)?
    3. Jelaskan hubungan antara Informatika dan STEAM! Berikan satu contoh konkret.

    ### 📋 Studi Kasus
    Sekolah kamu ingin membuat **taman pintar (smart garden)** di halaman belakang. Proyek ini membutuhkan berbagai keahlian: ada yang merancang sensor penyiraman otomatis, ada yang membuat aplikasi monitoring, ada yang mendesain tampilan dashboard, dan ada yang menganalisis data pertumbuhan tanaman. Tim yang terdiri dari 5 siswa, masing-masing mengambil peran berbeda.

    **Analisis:**
    1. Elemen Informatika apa saja yang terlibat dalam proyek smart garden ini? Identifikasi minimal 4 elemen.
    2. Bagaimana pendekatan STEAM bisa membantu proyek ini menjadi lebih baik?
    """)

def c1_b():
    return dedent("""
    ### 💼 Profesi dan Karier di Bidang Informatika
    Lulusan Informatika bisa kerja di mana saja! Hampir semua perusahaan butuh ahli IT.

    > 🧩 **Analogi:** Profesi IT itu seperti **rumah sakit**. Ada dokter bedah (software engineer), dokter umum (IT support), spesialis jantung (AI engineer), perawat (network admin), apoteker (data analyst) — semuanya penting dan punya spesialisasi masing-masing.

    ### Profesi IT Populer
    | Profesi | Gaji Rata-rata (Entry) | Tugas Utama |
    |---------|----------------------|-------------|
    | **Software Engineer** | Rp8-15 juta/bln | Membangun aplikasi/web |
    | **Data Scientist** | Rp10-20 juta/bln | Menganalisis data untuk insight bisnis |
    | **UI/UX Designer** | Rp7-12 juta/bln | Mendesain tampilan aplikasi yang user-friendly |
    | **Network Engineer** | Rp6-10 juta/bln | Mengelola infrastruktur jaringan |
    | **Cyber Security Analyst** | Rp10-18 juta/bln | Melindungi sistem dari serangan |
    | **AI/Machine Learning Engineer** | Rp12-25 juta/bln | Mengembangkan model AI |
    | **DevOps Engineer** | Rp12-20 juta/bln | Mengelola deployment & infrastruktur |

    ### 🚀 Tips Mempersiapkan Diri
    1. **Bangun portofolio** — proyek nyata lebih berharga dari nilai rapor
    2. **Ikuti course online** — Coursera, Dicoding, Progate
    3. **Bergabung komunitas** — Discord IT, grup Telegram programming
    4. **Latihan soal coding** — HackerRank, LeetCode, Codewars

    > ✍️ **Aktivitas:** Cari satu profesi IT yang menarik bagimu. Tulis: tugas hariannya, skills yang dibutuhkan, dan perkiraan gajinya!

    ### 🔍 Cek Pemahaman
    1. Sebutkan 3 profesi IT dan jelaskan tugas utama masing-masing!
    2. Mengapa portofolio proyek nyata lebih berharga daripada nilai rapor dalam industri IT?
    3. Skill apa saja yang dibutuhkan untuk menjadi seorang Data Scientist?

    ### 📋 Studi Kasus
    Rina adalah siswa kelas XI yang sangat suka bermain game dan sering membantu teman-temannya memperbaiki komputer yang bermasalah. Orang tuanya ingin Rina menjadi dokter, tapi Rina bercita-cita bekerja di bidang IT. Ia bingung menentukan profesi IT apa yang cocok dengan minatnya.

    **Analisis:**
    1. Profesi IT apa yang paling cocok untuk Rina berdasarkan minatnya? Jelaskan alasanmu!
    2. Buatlah rencana 3 langkah yang bisa Rina lakukan selama SMA untuk mempersiapkan karier IT-nya!
    """)

def c1_c():
    return dedent("""
    ### 🔗 Praktik Lintas Bidang dalam Informatika
    Informatika bisa diterapkan di **semua bidang** — sains, seni, sosial, olahraga, apapun!

    > 🧩 **Analogi:** Informatika itu seperti **listrik**. Listrik bisa nyalain lampu di rumah, di rumah sakit, di pabrik, di stadion. Begitu juga Informatika — bisa dipakai di bidang apa saja!

    ### Contoh Lintas Bidang
    | Bidang | Penerapan Informatika |
    |--------|----------------------|
    | **Kimia** | Simulasi reaksi kimia, pemodelan molekul 3D |
    | **Fisika** | Simulasi gerak, analisis data percobaan |
    | **Biologi** | Analisis DNA, klasifikasi spesies dengan AI |
    | **Ekonomi** | Prediksi pasar saham, analisis keuangan |
    | **Seni** | Musik digital, generative art, animasi |
    | **Kedokteran** | Diagnosa penyakit dengan AI, robot bedah |

    ### 📝 Aktivitas: Mind Map Lintas Bidang
    Buatlah mind map yang menunjukkan bagaimana Informatika bisa diterapkan di **3 bidang** yang kamu minati!

    ```
              ┌── Kimia: Simulasi Molekul ──┐
              │                              │
              │         INFORMATIKA          │
              │                              │
      Biologi ─┤  (coding, data, AI, IoT)    ├── Ekonomi
      Analisis │                              │     Prediksi
      DNA      └──────────────────────────────┘     Saham
    ```

    ### 🔍 Cek Pemahaman
    1. Sebutkan 3 bidang selain Teknologi yang bisa menerapkan Informatika! Berikan contohnya!
    2. Mengapa Informatika disebut sebagai "ilmu lintas bidang"?
    3. Bagaimana Informatika membantu bidang kedokteran? Berikan 2 contoh!

    ### 📋 Studi Kasus
    Sebuah kelompok siswa kelas XI mendapat tugas membuat proyek sosial. Mereka ingin membantu warung kecil milik Pak Budi yang masih mencatat keuangan secara manual di buku. Pelanggan sering mengeluh karena pesanan sering tertukar dan stok barang tidak terkontrol.

    **Analisis:**
    1. Bagaimana Informatika bisa membantu menyelesaikan masalah Pak Budi? Jelaskan minimal 2 penerapan!
    2. Elemen Informatika apa saja yang terlibat dalam solusi yang kamu usulkan?
    """)


# ─── BAB 2: Strategi Algoritmik & Pemrograman ─────────────────

def c2_a():
    return dedent("""
    ### ⚙️ Proses Pemrograman & Efisiensi Algoritma

    ### 4 Tahap Pemrograman
    ```
      ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐
      │ ANALISIS │   │ DESAIN   │   │ IMPLEMEN-│   │ PENGUJIAN│
      │ Masalah  │──►│ Algoritma│──►│ TASI     │──►│ & DEBUG  │
      │          │   │          │   │ (Coding) │   │          │
      └──────────┘   └──────────┘   └──────────┘   └────┬─────┘
                                                         │
                                                    (loop back)
    ```

    > 🧩 **Analogi:** Ini seperti **resep masakan**. Kamu analisis mau masak apa (analisis), tentukan bahan dan langkahnya (desain), masak (coding), lalu cicipi — kalau asin tambah gula (debug).

    ### Efisiensi Algoritma
    Algoritma yang baik harus **efisien** — cepat dan tidak boros memori.

    | Algoritma | Waktu untuk 1000 data | Waktu untuk 1 juta data |
    |-----------|---------------------|------------------------|
    | **Linear Search** | 0,001 detik | 1 detik |
    | **Binary Search** | 0,00001 detik | 0,00001 detik |
    | **Bubble Sort** | 0,001 detik | 1000 detik (~17 menit!) |
    | **Merge Sort** | 0,0001 detik | 0,1 detik |

    > 🔑 **Big O Notation** adalah cara mengukur efisiensi. O(1) = konstan (paling cepat), O(n) = linear, O(n²) = kuadratik (lambat untuk data besar).

    ### ✍️ Latihan
    Mana yang lebih efisien untuk mencari nomor telepon di buku telepon dengan 10.000 nama?
    - **Linear Search**: Cek satu per satu dari halaman pertama
    - **Binary Search**: Buka halaman tengah, lalu cari di kiri/kanan

    ### 🔍 Cek Pemahaman
    1. Sebutkan 4 tahap dalam proses pemrograman! Mengapa tahap analisis penting dilakukan pertama?
    2. Apa perbedaan antara O(1), O(n), dan O(n\u00b2)? Berikan contoh algoritma untuk masing-masing!
    3. Untuk data 1 juta item, mengapa Binary Search (O(log n)) jauh lebih cepat dari Linear Search (O(n))?

    ### 📋 Studi Kasus
    Perpustakaan SMA Nusantara memiliki 10.000 buku. Selama ini, siswa mencari buku dengan cara melihat satu per satu rak. Seorang siswa bernama Dimas mengusulkan program pencarian buku digital agar lebih efisien.

    **Analisis:**
    1. Algoritma pencarian mana yang paling tepat untuk program yang diusulkan Dimas? Jelaskan alasannya!
    2. Jika data buku bertambah menjadi 100.000, apakah pilihan algoritmamu masih tetap sama? Mengapa?
    """)

def c2_b():
    return dedent("""
    ### 🔄 Rekursi: Fungsi yang Memanggil Dirinya Sendiri
    Rekursi adalah teknik di mana sebuah **fungsi memanggil dirinya sendiri** untuk menyelesaikan masalah.

    > 🧩 **Analogi:** Rekursi itu seperti **cermin yang berhadapan dengan cermin lain** — kamu melihat pantulan yang terus berulang. Atau seperti **boneka Matryoshka Rusia** — di dalam boneka besar ada boneka lebih kecil, dan seterusnya.

    ### Struktur Rekursi
    ```python
    def faktorial(n):
        # BASE CASE: kondisi berhenti
        if n <= 1:
            return 1
        # RECURSIVE CASE: panggil diri sendiri
        return n * faktorial(n - 1)
    
    print(faktorial(5))  # Output: 120
    ```

    ### Cara Kerja
    ```
    faktorial(5) = 5 × faktorial(4)
                 = 5 × 4 × faktorial(3)
                 = 5 × 4 × 3 × faktorial(2)
                 = 5 × 4 × 3 × 2 × faktorial(1)
                 = 5 × 4 × 3 × 2 × 1
                 = 120
    ```

    ### Rekursi vs Iterasi
    | Aspek | Rekursi | Iterasi (for/while) |
    |-------|---------|---------------------|
    | **Kode** | Lebih pendek, elegan | Lebih panjang |
    | **Mudah dibaca** | Untuk masalah tertentu (pohon, fractal) | Untuk masalah umum |
    | **Memori** | Lebih boros (stack) | Lebih hemat |
    | **Kecepatan** | Agak lambat | Cepat |

    ### Contoh: Fibonacci
    ```python
    def fibonacci(n):
        if n <= 1:
            return n
        return fibonacci(n-1) + fibonacci(n-2)
    
    print(fibonacci(10))  # Output: 55
    ```

    > 💡 **Tips:** Selalu pastikan ada **base case** (kondisi berhenti) — kalau tidak, program akan error "stack overflow"!

    ### 🔍 Cek Pemahaman
    1. Apa perbedaan antara base case dan recursive case dalam fungsi rekursif?
    2. Mengapa rekursi Fibonacci tanpa DP sangat lambat untuk n = 50?
    3. Kapan sebaiknya menggunakan rekursi dibandingkan iterasi? Berikan contoh masalah!

    ### 📋 Studi Kasus
    Dalam pelajaran seni, Dimas mendapat tugas membuat gambar **pohon fractal** menggunakan prinsip rekursif. Setiap cabang pohon bercabang menjadi 2 cabang yang lebih kecil, dan seterusnya. Dimas ingin pohonnya memiliki kedalaman 5 tingkat (5 kali percabangan).

    **Analisis:**
    1. Gambarkan bagaimana pola rekursif bekerja pada pohon fractal tersebut! Berapa total cabang yang terbentuk?
    2. Apa yang terjadi jika Dimas lupa memberikan base case (kedalaman 0) pada programnya?
    """)

def c2_c():
    return dedent("""
    ### 🎯 Algoritma Greedy: Pilihan Terbaik Saat Ini
    Greedy = **rakus** = algoritma yang selalu mengambil pilihan **terbaik pada saat itu juga** (lokal optimal) dengan harapan menghasilkan solusi terbaik secara keseluruhan (global optimal).

    > 🧩 **Analogi:** Greedy itu seperti **jalan-jalan ke pasar malam**. Kamu punya uang Rp50.000 dan harus memilih makanan terbaik. Kamu beli yang paling kamu suka duluan — tanpa mikirin nanti bisa kehabisan uang atau tidak. **Pokoknya sekarang yang paling enak dulu!**

    ### Contoh: Coin Change
    **Masalah:** Kembalian Rp4.700 dengan koin minimal. Koin yang tersedia: Rp1.000, Rp500, Rp200, Rp100.

    ```
    Strategi Greedy: Ambil koin terbesar yang bisa diambil.
    
    Rp4.700 → ambil Rp1.000 (sisa Rp3.700)
            → ambil Rp1.000 (sisa Rp2.700)
            → ambil Rp1.000 (sisa Rp1.700)
            → ambil Rp1.000 (sisa Rp700)
            → ambil Rp500  (sisa Rp200)
            → ambil Rp200  (sisa Rp0)
    
    Total: 6 koin (4×1000 + 1×500 + 1×200) ✅
    ```

    ### Contoh: Activity Selection
    **Masalah:** Dalam satu ruangan, jadwalkan kegiatan sebanyak mungkin yang tidak bertabrakan.

    ```
    Kegiatan:                        Pilih yang selesai paling awal!
    ─── 1. ────── 08:00-09:00 ✓           ────
    ───── 2. ─── 08:30-09:30              ───
    ─── 3. ─── 09:00-10:00 ✓                    ────
    ───── 4. ─ 10:30-10:45 ✓                          ──
    ```

    > 💡 **Kunci Greedy:** Pilih yang **selesai paling awal** = bisa muat lebih banyak kegiatan!

    ### Kapan Greedy Tepat?
    ✅ Kalau pilihan lokal terbukti menghasilkan solusi global optimal
    ❌ Tidak semua masalah bisa diselesaikan dengan Greedy

    ```python
    # Contoh: Coin Change dengan Greedy di Python
    koin = [1000, 500, 200, 100]
    sisa = 4700
    hasil = []
    for k in koin:
        while sisa >= k:
            hasil.append(k)
            sisa -= k
    print(hasil)  # [1000, 1000, 1000, 1000, 500, 200]
    ```

    ### 🔍 Cek Pemahaman
    1. Jelaskan prinsip utama algoritma Greedy dengan kata-katamu sendiri!
    2. Dalam kasus Activity Selection, mengapa memilih kegiatan yang selesai paling awal adalah strategi Greedy yang tepat?
    3. Kapan algoritma Greedy **tidak** tepat digunakan? Berikan contoh!

    ### 📋 Studi Kasus
    Saat bazar sekolah, Dita memiliki uang Rp25.000 untuk membeli makanan. Berikut harga makanan yang tersedia: Siomay Rp5.000, Batagor Rp7.000, Risol Rp3.000, Cireng Rp4.000, dan Es Buah Rp6.000. Dita ingin mendapatkan **sebanyak mungkin jenis makanan** dengan uang yang ada.

    **Analisis:**
    1. Jika Dita menggunakan strategi Greedy, makanan apa yang pertama kali dibelinya? Apakah strategi Greedy menghasilkan solusi optimal untuk kasus ini?
    2. Coba gunakan strategi berbeda dan bandingkan hasilnya dengan strategi Greedy!
    """)

def c2_d():
    return dedent("""
    ### 📊 Pemrograman Dinamis: Optimasi dengan Subproblem
    **Dynamic Programming (DP)** adalah teknik menyelesaikan masalah dengan **memecahnya menjadi sub-masalah kecil**, menyimpan hasilnya, dan menggunakan kembali hasil tersebut.

    > 🧩 **Analogi:** DP itu seperti **belajar naik sepeda**. Kamu tidak perlu belajar dari nol setiap kali naik sepeda — otakmu sudah menyimpan \"cara naik sepeda\" (memoisasi) dan tinggal menggunakannya lagi.

    ### DP vs Rekursi Biasa
    ```
    FIBONACCI dengan REKURSI biasa:       FIBONACCI dengan DP (Memoization):
    
    fib(5)                                  fib(5)
    ├── fib(4)                              ├── fib(4) → simpan di cache
    │   ├── fib(3)                          │   ├── fib(3) → simpan
    │   │   ├── fib(2)                      │   │   ├── fib(2) → simpan
    │   │   │   ├── fib(1) ✅               │   │   │   ├── fib(1) ✅
    │   │   │   └── fib(0) ✅               │   │   │   └── fib(0) ✅
    │   │   └── fib(1) ✅                   │   │   └── (pakai cache fib(1))
    │   └── fib(2) → HITUNG LAGI! ❌        │   └── (pakai cache fib(2))
    └── fib(3) → HITUNG LAGI! ❌            └── (pakai cache fib(3))
    ```

    ### Implementasi DP
    ```python
    # Tanpa DP — lambat untuk n besar
    def fib_rekursif(n):
        if n <= 1: return n
        return fib_rekursif(n-1) + fib_rekursif(n-2)  # O(2^n)
    
    # Dengan DP (Memoization) — cepat!
    cache = {}
    def fib_dp(n):
        if n <= 1: return n
        if n not in cache:
            cache[n] = fib_dp(n-1) + fib_dp(n-2)
        return cache[n]  # O(n)
    
    print(fib_dp(50))  # Output: 12586269025 (LANGSUNG!)
    ```

    | n | fib(n) | Rekursi biasa | DP (Memoization) |
    |---|--------|--------------|------------------|
    | 10 | 55 | 0,001 detik | 0,001 detik |
    | 30 | 832040 | 0,5 detik | 0,001 detik |
    | 50 | 12.586.269.025 | ~600 tahun! | 0,001 detik |

    > 🔑 **2 Kunci DP:** 1) **Overlapping Subproblems** — sub-masalah yang berulang, 2) **Optimal Substructure** — solusi optimal dari sub-masalah membentuk solusi optimal keseluruhan.

    ### 🔍 Cek Pemahaman
    1. Jelaskan perbedaan utama antara rekursi biasa dan Dynamic Programming!
    2. Apa yang dimaksud dengan Memoization? Bagaimana cara kerjanya?
    3. Mengapa fib(50) dengan rekursi biasa memakan waktu ~600 tahun, tapi dengan DP hanya 0,001 detik?

    ### 📋 Studi Kasus
    Seorang siswa bernama Adi ingin menabung untuk mengikuti study tour ke Yogyakarta seharga Rp1.500.000 dalam waktu 6 bulan (180 hari). Setiap hari ia bisa menabung Rp5.000, Rp10.000, atau Rp20.000. Ia ingin tahu berapa banyak cara yang bisa dilakukan untuk mencapai target tersebut.

    **Analisis:**
    1. Mengapa masalah ini cocok diselesaikan dengan DP daripada rekursi biasa?
    2. Konsep DP apa (Overlapping Subproblems / Optimal Substructure) yang muncul dalam masalah tabungan Adi? Jelaskan!
    """)

def c2_e():
    return dedent("""
    ### 📦 Array, String, dan Manipulasi Data

    ### Array — Kumpulan Data Terindeks
    ```python
    nilai = [85, 92, 78, 90, 88]  # Array 5 elemen
    # Indeks: 0   1   2   3   4
    print(nilai[0])    # 85
    print(nilai[-1])   # 88 (indeks negatif = dari belakang)
    print(len(nilai))  # 5 (panjang array)
    ```

    > 🧩 **Analogi:** Array seperti **loker di sekolah**. Setiap loker punya nomor (indeks) dan isi (data). Nomor dimulai dari 0!

    ### Operasi Dasar Array
    ```python
    angka = [3, 1, 4, 1, 5]
    angka.append(9)       # Tambah di akhir → [3,1,4,1,5,9]
    angka.sort()          # Urutkan → [1,1,3,4,5,9]
    angka.reverse()       # Balik → [9,5,4,3,1,1]
    angka.pop()           # Ambil & hapus terakhir → 1
    print(angka.index(4)) # Cari posisi angka 4 → 2
    ```

    ### String — Teks juga Kumpulan Data!
    ```python
    teks = "Informatika"
    print(teks[0])        # 'I'
    print(teks[:4])       # 'Info' (dari 0 sampai 3)
    print(teks[-3:])      # 'ika' (3 karakter terakhir)
    print(teks.upper())   # 'INFORMATIKA'
    print(teks.count('a')) # 2 (huruf 'a' muncul 2x)
    ```

    ### Pattern Matching Sederhana
    ```python
    teks = "Hari ini belajar Python di kelas XI"
    cari = "Python"
    if cari in teks:
        print(f"'{cari}' ditemukan!")
    
    # Cari posisi
    posisi = teks.find("kelas")
    print(f"Dimulai dari indeks: {posisi}")  # Output: 23
    ```

    > ✍️ **Latihan:** Buat program yang menerima 7 nama teman sekelas, simpan dalam array, urutkan secara alfabet, lalu tampilkan!

    ### 🔍 Cek Pemahaman
    1. Apa perbedaan indeks positif dan negatif dalam array Python? Berikan contoh!
    2. Jelaskan fungsi `append()`, `sort()`, dan `pop()` pada array!
    3. Bagaimana cara mencari kata tertentu di dalam sebuah string menggunakan Python?

    ### 📋 Studi Kasus
    Ketua kelas XI IPA 1 ingin membuat aplikasi **presensi kehadiran** sederhana. Setiap hari, guru mencatat siapa saja yang hadir. Selama seminggu, data kehadiran dikumpulkan dalam sebuah array. Dari 35 siswa, ternyata rata-rata 3 siswa tidak hadir setiap hari.

    **Analisis:**
    1. Buat array Python sederhana yang menyimpan data kehadiran 5 siswa selama 1 minggu! Bagaimana cara menentukan siswa dengan kehadiran terbanyak?
    2. Jika data kehadiran disimpan sebagai string panjang, bagaimana cara menghitung jumlah siswa yang hadir setiap hari?
    """)

def c2_f():
    return dedent("""
    ### ⚖️ Perbandingan Strategi Algoritmik

    Setiap strategi punya **kelebihan dan kekurangan**. Mari bandingkan!

    ### Tabel Perbandingan
    | Aspek | Rekursif | Iteratif | Greedy | Dynamic Programming |
    |-------|----------|----------|--------|-------------------|
    | **Prinsip** | Panggil diri sendiri | Ulang dengan loop | Pilih terbaik lokal | Simpan sub-masalah |
    | **Mudah?** | Untuk masalah tertentu | Umum | Konsep sederhana | Konsep sulit |
    | **Efisiensi** | Lambat (tanpa DP) | Cepat | Cepat | Cepat |
    | **Memori** | Boros stack | Hemat | Hemat | Cukup besar |
    | **Cocok untuk** | Tree, fractal | Masalah umum | Optimasi sederhana | Optimasi kompleks |

    ### Kapan Pakai Yang Mana?
    ```
    ┌──────────────────────────────────────────────────┐
    │              PERTANYAAN KUNCI                    │
    ├──────────────────────────────────────────────────┤
    │                                                   │
    │  Apakah subproblem berulang?                      │
    │     ├── Ya → Apakah solusi lokal = global?        │
    │     │         ├── Ya → GREEDY ✅                  │
    │     │         └── Tidak → DP ✅                   │
    │     └── Tidak → Apakah masalah bisa dipecah?      │
    │               ├── Ya → REKURSI ✅                 │
    │               └── Tidak → ITERASI ✅              │
    └──────────────────────────────────────────────────┘
    ```

    ### Contoh: Menghitung Uang Kembalian
    | Strategi | Cara | Hasil |
    |----------|------|-------|
    | **Greedy** | Ambil koin terbesar dulu | 6 koin (4×1000+500+200) ✅ |
    | **DP** | Cari kombinasi minimal | 6 koin (sama, karena koin standar) |
    | **Rekursi** | Coba semua kemungkinan | 6 koin, tapi lambat |
    | **Iterasi** | Loop dari koin terbesar | 6 koin, sederhana |

    > 💡 **Insight:** Tidak ada strategi \"paling baik\" untuk semua masalah — **pilih yang paling sesuai** dengan karakteristik masalah!

    ### 🔍 Cek Pemahaman
    1. Sebutkan 4 strategi algoritmik yang dibahas! Jelaskan prinsip dasar masing-masing!
    2. Kapan waktu yang tepat menggunakan algoritma Greedy? Kapan waktu yang tepat menggunakan DP?
    3. Buatlah diagram alir (flowchart) sederhana untuk memilih strategi algoritmik!

    ### 📋 Studi Kasus
    SMA Bangsa mengadakan lomba **Hackathon** antarkelas. Setiap tim mendapat masalah yang berbeda: Tim A mendapat masalah mencari jalur terpendek pengiriman makanan, Tim B mendapat masalah menyusun jadwal pelajaran tanpa tabrakan, dan Tim C mendapat masalah mencari kata dalam kamus raksasa.

    **Analisis:**
    1. Strategi algoritmik apa yang paling cocok untuk masing-masing tim? Jelaskan alasannya!
    2. Jika Tim A mencoba menggunakan rekursi sederhana untuk masalah pengiriman makanan, apa yang akan terjadi?
    """)


# ─── BAB 3: Berpikir Kritis & DSI ─────────────────────────────

def c3_a():
    return dedent("""
    ### 🔍 Literasi Digital & Verifikasi Informasi
    Di era banjir informasi, kemampuan **memverifikasi** berita adalah **skill hidup** yang paling penting.

    > 🧩 **Analogi:** Literasi digital itu seperti **kekebalan tubuh**. Setiap hari tubuhmu diserang virus dan bakteri (hoaks, misinformasi). Sistem imunmu harus kuat untuk melawannya. Literasi digital adalah **sistem imun untuk pikiranmu**.

    ### Teknik Verifikasi Informasi
    ```
    1. CEK SUMBER — Siapa yang menulis? Apakah kredibel?
    2. CEK FAKTA — Apakah berita ini sudah diverifikasi pihak lain?
    3. REVERSE IMAGE — Cari sumber asli foto/gambar
    4. LATERAL READING — Buka tab lain, cari info dari sumber berbeda
    5. CEK TANGGAL — Apakah ini berita lama yang diedarkan lagi?
    ```

    ### Tools Verifikasi
    | Tools | Fungsi | Link |
    |-------|--------|------|
    | **Google Image Search** | Cari sumber asli gambar | images.google.com |
    | **TinEye** | Reverse image search | tineye.com |
    | **TurnBackHoax** | Fact-checking Indonesia | turnbackhoax.id |
    | **Mafindo** | Masyarakat Anti Fitnah | mafindo.or.id |
    | **cekfakta.com** | Kolaborasi fact-checker | cekfakta.com |

    ### ✍️ Aktivitas: Verifikasi Berita
    1. Ambil 1 berita viral dari media sosial
    2. Cek sumbernya — siapa penulis, medianya apa
    3. Gunakan reverse image search untuk foto-fotonya
    4. Cari versi berbeda dari berita yang sama
    5. Kesimpulan: Hoaks atau Fakta?

    ### 🔍 Cek Pemahaman
    1. Apa yang dimaksud dengan literasi digital? Mengapa penting di era sekarang?
    2. Sebutkan 5 langkah verifikasi informasi yang bisa dilakukan sebelum menyebarkan berita!
    3. Mengapa hoaks bisa menyebar 6x lebih cepat dari berita benar?

    ### 📋 Studi Kasus
    Sebuah pesan berantai di WhatsApp grup kelas berbunyi: "INFO PENTING! Pemerintah memberikan bantuan Rp2.500.000 untuk setiap siswa SMA. Daftar segera di link bit.ly/bansos-siswa sebelum 1 Juni 2025! Share ke 10 grup lain agar tidak ketinggalan!" Banyak teman sekelas yang langsung mendaftar dan menyebarkan pesan tersebut.

    **Analisis:**
    1. Langkah verifikasi apa yang harus dilakukan sebelum mempercayai informasi tersebut?
    2. Apa risiko yang mungkin terjadi jika teman-temanmu tetap mengklik link tersebut?
    """)

def c3_b():
    return dedent("""
    ### 📖 Membaca Lateral: Evaluasi Sumber Digital
    **Lateral Reading** adalah teknik membaca yang **tidak percaya pada satu sumber saja**. Kamu membaca secara \"menyamping\" — membuka tab baru untuk mengecek kredibilitas sumber.

    > 🧩 **Analogi:** Lateral reading itu seperti **detektif**. Kalau ada seorang saksi memberi kesaksian, detektif tidak langsung percaya. Dia cek latar belakang saksi, cari saksi lain, bandingkan cerita. Sama dengan lateral reading — jangan percaya satu sumber!

    ### Cara Lateral Reading
    ```python
    # BUKAN LATERAL READING ❌
    Baca artikel → Percaya → Share
    
    # LATERAL READING ✅
    Baca artikel → Buka tab baru
        → Cari siapa penulisnya (kredibel?)
        → Cari medianya (punya sejarah hoaks?)
        → Cari sumber lain yang membahas topik sama
        → Bandingkan semua informasi → Baru simpulkan!
    ```

    ### Praktik Lateral Reading
    | Langkah | Pertanyaan | Di mana Cek? |
    |---------|-----------|-------------|
    | 1 | Siapa penulis artikel ini? | Cari nama penulis + "linkedin" |
    | 2 | Siapa pemilik media ini? | Cari "[nama media] about" |
    | 3 | Apa kata media lain? | Cari topik + sumber berita lain |
    | 4 | Apakah ada data/fakta pendukung? | Cek link referensi dalam artikel |
    | 5 | Kapan artikel diterbitkan? | Cek tanggal publikasi |

    > 🔑 **Ingat:** Informasi yang baik tidak takut diverifikasi. Semakin banyak sumber yang kamu cek, semakin yakin kamu dengan kebenarannya!

    ### 🔍 Cek Pemahaman
    1. Jelaskan perbedaan antara membaca vertikal (vertical reading) dan membaca lateral (lateral reading)!
    2. Sebutkan 5 langkah dalam melakukan lateral reading!
    3. Mengapa lateral reading dianggap lebih efektif daripada hanya membaca satu sumber?

    ### 📋 Studi Kasus
    Sebuah video viral di TikTok menunjukkan seorang artis terkenal meninggal dunia karena kecelakaan. Video tersebut sudah ditonton 5 juta kali dan ribuan komentar berduka. Namun, kamu curiga karena tidak ada berita dari media mainstream. Seorang teman memintamu untuk ikut menyebarkan kabar duka tersebut.

    **Analisis:**
    1. Terapkan teknik lateral reading untuk kasus ini! Sumber apa saja yang perlu kamu cek?
    2. Setelah mengecek, ternyata video itu hoaks dan artis tersebut masih hidup. Bagaimana seharusnya kamu menanggapi teman yang sudah ikut menyebarkan?
    """)

def c3_c():
    return dedent("""
    ### 🌍 Dampak Sosial TIK di Masyarakat
    Teknologi Informasi dan Komunikasi (TIK) telah mengubah masyarakat secara fundamental — ada dampak positif dan negatif.

    > 🧩 **Analogi:** TIK itu seperti **api**. Api bisa masak makanan (positif), tapi juga bisa membakar rumah (negatif). Tergantung siapa yang menggunakan dan bagaimana.

    ### Dampak Positif
    | Bidang | Dampak Positif TIK |
    |--------|-------------------|
    | **Pendidikan** | Akses ilmu dari seluruh dunia (YouTube, Coursera) |
    | **Kesehatan** | Telemedicine, rekam medis digital |
    | **Ekonomi** | Marketplace, cashless, financial inclusion |
    | **Demokrasi** | Partisipasi publik, e-government |
    | **Sosial** | Terhubung dengan teman, keluarga jarak jauh |

    ### Dampak Negatif
    | Dampak | Penjelasan | Contoh Nyata |
    |--------|-----------|-------------|
    | **Hoaks** | Berita palsu menyebar 6x lebih cepat dari berita benar | Isu vaksin, politik |
    | **Cyberbullying** | Perundungan di dunia digital | Kasus bunuh diri akibat bully di medsos |
    | **Kecanduan** | Dopamine loop dari notifikasi | Nomophobia (takut tanpa HP) |
    | **Privasi** | Data pribadi dikumpulkan & dijual | Skandal Cambridge Analytica |
    | **Kesenjangan Digital** | Yang tidak punya akses makin tertinggal | Daerah 3T sulit internet |

    > 💬 **Diskusi:** Apakah menurutmu dampak positif TIK lebih besar daripada dampak negatifnya? Mengapa?

    ### 🔍 Cek Pemahaman
    1. Sebutkan 3 dampak positif dan 3 dampak negatif TIK di masyarakat!
    2. Apa yang dimaksud dengan "kesenjangan digital"? Mengapa hal ini perlu diatasi?
    3. Mengapa kecanduan gadget bisa disebut sebagai "dopamine loop"? Jelaskan!

    ### 📋 Studi Kasus
    Seorang teman sekelasmu, Aulia, menghabiskan 6-8 jam sehari bermain game online dan media sosial. Nilainya turun drastis, sering tidak mengerjakan PR, dan mulai menarik diri dari pertemanan offline. Orang tuanya sudah menyita HP, tapi Aulia malah marah dan kabur dari rumah.

    **Analisis:**
    1. Dampak negatif TIK apa yang dialami Aulia? Identifikasi minimal 2 dampak!
    2. Sebagai teman, apa yang bisa kamu lakukan untuk membantu Aulia? Rancang rencana aksi minimal 3 langkah!
    """)

def c3_d():
    return dedent("""
    ### 🗣️ Debat & Argumen Kritis Dampak TIK
    Mampu berdebat secara **kritis dan santun** tentang dampak TIK adalah salah satu kompetensi penting abad 21.

    > 🧩 **Analogi:** Debat itu seperti **pertandingan catur**. Bukan soal siapa yang paling keras suaranya, tapi siapa yang punya **argumentasi paling kuat** dengan **data dan logika** yang solid.

    ### Struktur Argumen Kritis
    ```
    ┌──────────────────────────────────────────────┐
    │              ARGUMEN KRITIS                  │
    ├──────────────────────────────────────────────┤
    │  1. KLAIM  — Pernyataan yang kamu yakini     │
    │  2. DATA   — Fakta/angka yang mendukung      │
    │  3. WARRANT— Logika yang menghubungkan       │
    │              data dengan klaim               │
    │  4. QUALIFIER— Batasan/sejauh mana ini benar │
    │  5. REBUTTAL— Jawaban untuk argumen lawan    │
    └──────────────────────────────────────────────┘
    ```

    ### Contoh Argumen
    **Topik Debat:** \"Apakah media sosial lebih banyak dampak positifnya?\"

    ```
    KLAIM: Media sosial lebih banyak dampak negatif bagi remaja.
    
    DATA: Survei menunjukkan 60% remaja merasa cemas setelah 
          menggunakan Instagram. Kasus bullying online naik 40%.
    
    WARRANT: Penggunaan medsos yang berlebihan terbukti 
             memicu kecemasan sosial dan perbandingan tidak sehat.
    
    QUALIFIER: Namun, untuk remaja yang menggunakan medsos 
               secara positif (belajar, bisnis), dampaknya baik.
    
    REBUTTAL: Lawan bilang medsos baik untuk koneksi sosial. 
              Tapi penelitian menunjukkan makin sering online, 
              makin merasa sendiri (social media paradox).
    ```

    ### Topik Debat untuk Kelas
    1. **Pro-Kontra:** AI akan menggantikan guru di masa depan
    2. **Pro-Kontra:** Pemerintah berhak memblokir media sosial
    3. **Pro-Kontra:** Belajar coding wajib untuk semua siswa SMA

    > 💡 **Aturan Debat:** 1) Dengar lawan bicara. 2) Serang argumen, bukan orangnya. 3) Gunakan data, bukan emosi. 4) Akui kalau argumen lawan kuat.

    ### 🔍 Cek Pemahaman
    1. Sebutkan 5 komponen struktur argumen kritis menurut Toulmin! Jelaskan masing-masing!
    2. Mengapa dalam debat kita harus "menyerang argumen, bukan orangnya"?
    3. Buatlah satu argumen kritis sederhana tentang topik "Penggunaan HP di sekolah harus dilarang"!

    ### 📋 Studi Kasus
    Kelas XI akan mengadakan **debat** dengan topik: "Penggunaan media sosial untuk pembelajaran di sekolah". Siswa dibagi menjadi tim pro dan kontra. Tim pro berargumen bahwa media sosial memudahkan akses materi dan diskusi. Tim kontra berargumen bahwa media sosial mengganggu konsentrasi belajar.

    **Analisis:**
    1. Buatlah argumen kritis lengkap (Klaim, Data, Warrant, Qualifier, Rebuttal) untuk **tim pro**!
    2. Buatlah argumen kritis lengkap untuk **tim kontra**! Argumen mana yang menurutmu lebih kuat? Mengapa?
    """)


# ─── BAB 4: Jaringan Komputer & Internet ──────────────────────

def c4_a():
    return dedent("""
    ### 🌐 Pengantar Jaringan & Topologi
    Jaringan komputer adalah **dua atau lebih komputer yang terhubung** untuk berbagi data dan sumber daya.

    > 🧩 **Analogi:** Jaringan komputer itu seperti **sistem jalan**. Ada jalan kampung (LAN), jalan provinsi (MAN), dan jalan tol antar pulau (WAN). Semakin lebar jalannya, semakin banyak data yang bisa lewat!

    ### Jenis Jaringan
    | Jenis | Luas | Contoh | Seperti... |
    |-------|------|--------|------------|
    | **LAN** | 1 ruangan - 1 gedung | Lab komputer sekolah | Jalan di komplek perumahan |
    | **MAN** | 1 kota | Koneksi antar cabang bank | Jalan provinsi |
    | **WAN** | Antar kota/negara | Internet | Jalan tol lintas pulau |

    ### Topologi Jaringan
    ```
    STAR:        RING:         BUS:          MESH:
      ⭐           ⭕           🚌             🔀
      PC─Switch   PC─PC        PC PC PC       PC═PC
      │  │  │     │   │        │  │  │       ║║║║
      PC PC PC    PC─PC        ═══KABEL═══    PC═PC
    ✅ Paling    ✅ Satu arah  ✅ Hemat      ✅ Paling andal
    ❌ Butuh hub ❌ 1 mati= ❌ Kabel putus ❌ Boros kabel
                  semua mati   =semua mati
    ```

    ### Perangkat Jaringan
    | Perangkat | Fungsi | 
    |-----------|--------|
    | **Router** | Menghubungkan jaringan berbeda (LAN → Internet) |
    | **Switch** | Menghubungkan komputer dalam satu LAN |
    | **Access Point** | Memancarkan sinyal WiFi |
    | **Modem** | Mengubah sinyal ISP jadi data digital |

    > 💡 **Topologi Star** adalah yang paling umum karena jika satu kabel putus, komputer lain tidak terganggu.

    ### 🔍 Cek Pemahaman
    1. Jelaskan perbedaan antara LAN, MAN, dan WAN! Berikan contoh masing-masing!
    2. Gambarkan topologi Star dan Ring! Apa kelebihan dan kekurangan masing-masing?
    3. Apa fungsi Router, Switch, dan Access Point dalam sebuah jaringan?

    ### 📋 Studi Kasus
    SMA Harapan Bangsa sedang membangun **laboratorium komputer baru** dengan 30 PC. Semua PC harus terhubung ke internet dan bisa saling berbagi data. Kepala sekolah meminta usulan desain jaringan yang efisien dan mudah dikelola.

    **Analisis:**
    1. Topologi apa yang paling tepat untuk laboratorium tersebut? Jelaskan kelebihan dan kekurangannya!
    2. Perangkat jaringan apa saja yang dibutuhkan? Gambarkan skema jaringan sederhananya!
    """)

def c4_b():
    return dedent("""
    ### 📦 OSI Layer & Mekanisme Pertukaran Data

    ### OSI 7 Layer
    OSI (Open Systems Interconnection) adalah **model referensi** yang menjelaskan bagaimana data berpindah dari satu komputer ke komputer lain.

    > 🧩 **Analogi:** OSI Layer itu seperti **proses pengiriman paket**. Kamu beli kue online, kue dibungkus (Presentation), dikasih label alamat (Session), diantar kurir (Transport), lewat jalan tertentu (Network), dikirim bit per bit (Data Link), jadi sinyal listrik (Physical).

    ```
    ┌──────┬─────────────────────────────────────────────┐
    │Layer │ Fungsi                    │ Contoh Protocol │
    ├──────┼───────────────────────────┼─────────────────┤
    │ 7    │ APPLICATION — Antarmuka   │ HTTP, FTP, DNS  │
    │      │ user dengan jaringan      │                 │
    │ 6    │ PRESENTATION — Enkripsi,  │ SSL/TLS, JPEG   │
    │      │ kompresi, format data     │                 │
    │ 5    │ SESSION — Mengelola sesi  │ NetBIOS, RPC    │
    │      │ koneksi                   │                 │
    │ 4    │ TRANSPORT — Pengiriman    │ TCP, UDP        │
    │      │ data andal (TCP) / cepat  │                 │
    │ 3    │ NETWORK — Routing, alamat │ IP, ICMP        │
    │      │ IP                        │                 │
    │ 2    │ DATA LINK — Framing,      │ Ethernet, MAC   │
    │      │ deteksi error             │                 │
    │ 1    │ PHYSICAL — Sinyal listrik │ Kabel, WiFi     │
    │      │ / radio, bit              │                 │
    └──────┴───────────────────────────┴─────────────────┘
    ```

    ### Enkapsulasi Data
    Setiap layer **membungkus** data dari layer di atasnya dengan header-nya sendiri.

    ```
    [Data Asli] → Layer 7-6-5
    ↓
    [TCP header | Data] → Layer 4 (Transport)
    ↓
    [IP header | TCP header | Data] → Layer 3 (Network)
    ↓
    [MAC header | IP | TCP | Data | Trailer] → Layer 2 (Data Link)
    ↓
    [10101010010101010101010] → Layer 1 (Physical)
    ```

    > 🔑 **Mnemonic:** **A**ll **P**eople **S**eem **T**o **N**eed **D**ata **P**rocessing (Application → Physical)

    ### 🔍 Cek Pemahaman
    1. Sebutkan 7 layer OSI dari atas ke bawah beserta fungsi masing-masing!
    2. Apa yang dimaksud dengan enkapsulasi data dalam konteks OSI Layer?
    3. Pada layer berapa protokol HTTP dan TCP bekerja? Jelaskan perbedaan fungsi keduanya!

    ### 📋 Studi Kasus
    Ketika kamu mengirim foto selfie ke teman melalui **Instagram**, data foto tersebut melewati proses enkapsulasi berlapis sebelum sampai ke temanmu. Mulai dari data foto asli hingga menjadi sinyal listrik yang dikirim melalui kabel atau WiFi.

    **Analisis:**
    1. Jelaskan bagaimana data foto selfie tersebut dibungkus (enkapsulasi) di setiap layer OSI! Mulai dari Application hingga Physical layer!
    2. Jika koneksi internet temanmu lambat, layer apa yang paling mungkin terpengaruh? Mengapa?
    """)

def c4_c():
    return dedent("""
    ### 🔒 Cyber Security: Ancaman & Mitigasi
    Cyber Security adalah praktik melindungi sistem, jaringan, dan data dari serangan digital.

    > 🧩 **Analogi:** Cyber security itu seperti **sistem keamanan rumah**. Ada pagar (firewall), CCTV (monitoring), kunci ganda (MFA), satpam (antivirus), dan asuransi (backup). Semakin banyak lapisan, semakin aman!

    ### Jenis Ancaman
    | Ancaman | Deskripsi | Contoh |
    |---------|-----------|--------|
    | **Malware** | Software berbahaya | Virus, ransomware WannaCry |
    | **Phishing** | Pemancing data pribadi | Email palsu dari "bank" |
    | **DDoS** | Banjir traffic ke server | Website down total |
    | **Man-in-the-Middle** | Menyadap komunikasi | WiFi palsu di kafe |
    | **SQL Injection** | Inject kode ke database | Bocor data pengguna |
    | **Social Engineering** | Manipulasi psikologis | "Saya dari IT, minta password" |

    ### Mitigasi: Cara Melindungi Diri
    ```
    🔐  Gunakan password berbeda untuk setiap akun
    🔑  Aktifkan 2FA (Two Factor Authentication)
    🔄  Update software & antivirus secara rutin
    📁  Backup data penting ke cloud + hard drive
    🔗  Jangan klik link sembarangan
    📧  Verifikasi pengirim email
    🛡️  Gunakan VPN di WiFi publik
    ```

    ### Password Manager
    Gunakan **password manager** (Bitwarden, 1Password, Google Password Manager) untuk menyimpan semua password — kamu cukup ingat 1 password utama.

    > 🔑 **Aturan Password:** Minimal 12 karakter, kombinasi huruf besar-kecil-angka-simbol. Contoh: `S4y4!ncL4s$XI_2026`

    ### 🔍 Cek Pemahaman
    1. Sebutkan 3 jenis ancaman cyber dan jelaskan cara kerjanya!
    2. Apa itu phishing? Bagaimana cara mengenali email phishing?
    3. Sebutkan minimal 4 cara untuk melindungi data pribadi dari serangan cyber!

    ### 📋 Studi Kasus
    Rudi menerima SMS yang mengaku dari "Bank Central" yang menyatakan: "Akun Anda akan diblokir! Klik link berikut untuk verifikasi: bit.ly/bank-central-verif. Abaikan = akun diblokir 24 jam!" Rudi panik karena ia memang punya rekening di bank tersebut. Ia hampir mengklik link itu sebelum bertanya pada gurunya.

    **Analisis:**
    1. Jenis serangan cyber apa yang dialami Rudi? Jelaskan ciri-cirinya!
    2. Apa yang seharusnya dilakukan Rudi? Buat langkah-langkah yang benar!
    """)

def c4_d():
    return dedent("""
    ### 🛡️ Tata Kelola Akses Data
    Tata kelola akses data mengatur **siapa boleh mengakses apa** dalam sebuah sistem.

    > 🧩 **Analogi:** Akses data itu seperti **tingkatan di game**. Player biasa cuma bisa main di level 1-5. Admin bisa akses semua level. Game master bisa ubah aturan game. Setiap peran punya **wewenang berbeda**.

    ### Model Kontrol Akses
    ```
    ┌────────────────────────────────────────────────────┐
    │  MAC (Mandatory) — Label keamanan (Top Secret,     │
    │                    Confidential, Public)           │
    │  DAC (Discretionary) — Pemilik data atur akses    │
    │  RBAC (Role-Based) — Akses berdasar peran          │
    │                    (Siswa, Guru, Admin)            │
    │  ABAC (Attribute-Based) — Akses berdasar atribut   │
    │                    (Jam kerja, lokasi, device)     │
    └────────────────────────────────────────────────────┘
    ```

    ### Implementasi
    | Peran | Akses ke Data Nilai | Akses ke Data Pribadi | Akses ke Konfigurasi |
    |-------|--------------------|----------------------|---------------------|
    | **Siswa** | Lihat nilai sendiri | ✗ | ✗ |
    | **Guru** | Input & edit nilai | ✗ | ✗ |
    | **Wali Kelas** | Lihat semua nilai kelas | Lihat data pribadi | ✗ |
    | **Admin IT** | ✗ | ✗ | Kelola server & akun |
    | **Kepala Sekolah** | Lihat laporan | Lihat laporan | ✗ |

    ### Prinsip Keamanan
    - **Least Privilege:** Beri akses seminimal mungkin
    - **Need to Know:** Akses hanya pada yang perlu diketahui
    - **Separation of Duties:** Tugas penting dipegang > 1 orang
    - **Audit Trail:** Catat semua aktivitas akses

    ### 🔍 Cek Pemahaman
    1. Jelaskan perbedaan antara model akses RBAC dan MAC!
    2. Apa yang dimaksud dengan prinsip Least Privilege? Berikan contohnya!
    3. Mengapa prinsip Separation of Duties penting dalam keamanan data?

    ### 📋 Studi Kasus
    SMA Nusantara menggunakan **sistem informasi sekolah** yang memiliki data nilai, data pribadi siswa, data keuangan, dan konfigurasi server. Pengguna sistem meliputi: siswa, guru, wali kelas, admin TU, kepala sekolah, dan admin IT. Saat ini, semua pengguna bisa mengakses hampir semua data — dan baru-baru ini terjadi kebocoran data nilai.

    **Analisis:**
    1. Rancang tabel akses (siapa boleh mengakses apa) menggunakan model RBAC untuk sistem tersebut!
    2. Kebocoran data nilai terjadi karena seorang siswa bisa mengakses database. Prinsip apa yang dilanggar? Bagaimana seharusnya?
    """)

def c4_e():
    return dedent("""
    ### 🖥️ Praktik Packet Tracer
    **Cisco Packet Tracer** adalah software simulasi jaringan yang memungkinkan kamu merancang, mengkonfigurasi, dan menguji jaringan tanpa alat fisik.

    > 🧩 **Analogi:** Packet Tracer itu seperti **game simulasi kota (SimCity)** tapi untuk jaringan komputer. Kamu bisa bangun jaringan, sambungkan perangkat, atur konfigurasi — tanpa harus beli router beneran!

    ### Aktivitas: Konfigurasi Jaringan Dasar
    ```
    ┌──────────┐        ┌──────────┐        ┌──────────┐
    │   PC 0   │───────►│  Switch  │◄───────│   PC 1   │
    │ 192.168. │        │          │        │ 192.168. │
    │  1.1     │        └────┬─────┘        │  1.2     │
    └──────────┘             │              └──────────┘
                            │
                     ┌──────┴──────┐
                     │   Router    │───► Internet
                     │ 192.168.1.1 │
                     └─────────────┘
    ```

    ### Langkah-Langkah
    1. **Buka Packet Tracer** → Tambahkan 2 PC, 1 Switch, 1 Router
    2. **Sambungkan** dengan kabel Copper Straight-Through
    3. **Konfigurasi IP:**
       - PC0: 192.168.1.2/24, Gateway: 192.168.1.1
       - PC1: 192.168.1.3/24, Gateway: 192.168.1.1
       - Router: 192.168.1.1/24
    4. **Uji koneksi** → Buka Command Prompt di PC0 → `ping 192.168.1.3`

    ### Perintah Dasar
    | Perintah | Fungsi |
    |----------|--------|
    | `ping [IP]` | Tes koneksi ke IP tujuan |
    | `ipconfig` | Lihat konfigurasi IP sendiri |
    | `tracert [IP]` | Lacak jalur yang dilewati paket |
    | `show ip route` (Router) | Lihat tabel routing |

    > 💡 **Tips:** Kalau ping gagal, cek: kabel terhubung?, IP sudah benar? firewall mati?

    ### 🔍 Cek Pemahaman
    1. Apa fungsi Cisco Packet Tracer dalam pembelajaran jaringan?
    2. Sebutkan langkah-langkah untuk mengkonfigurasi 2 PC agar bisa saling ping!
    3. Apa artinya jika perintah `ping` berhasil? Apa yang terjadi jika gagal?

    ### 📋 Studi Kasus
    Sekolah kamu memiliki **2 gedung** yang berjarak 200 meter. Gedung A (lab komputer) dan Gedung B (perpustakaan). Kamu diminta merancang jaringan yang menghubungkan kedua gedung agar siswa di perpustakaan bisa mengakses internet dari server di lab komputer. Tersedia 2 router, 2 switch, dan kabel secukupnya.

    **Analisis:**
    1. Gambarkan desain jaringan di Packet Tracer untuk menghubungkan kedua gedung!
    2. Konfigurasi IP apa yang akan kamu berikan untuk PC di Gedung A dan Gedung B? Bagaimana cara memastikan koneksi berhasil?
    """)


# ─── BAB 5: Aplikasi Mobile & AI ──────────────────────────────

def c5_a():
    return dedent("""
    ### 📱 Pengantar Aplikasi Mobile
    Aplikasi mobile adalah program yang berjalan di perangkat bergerak (smartphone/tablet). Ada 3 jenis utama.

    > 🧩 **Analogi:** Aplikasi mobile itu seperti **toko**. Ada toko yang khusus untuk iPhone (native iOS), khusus Android (native Android), dan toko online yang bisa diakses dari HP mana pun (web app / hybrid).

    ### Jenis Aplikasi Mobile
    ```
    ┌──────────────────────────────────────────────────────┐
    │                  JENIS APLIKASI MOBILE               │
    ├──────────────┬──────────────┬────────────────────────┤
    │  Native iOS  │ Native       │ Hybrid / Cross-platform│
    │              │ Android      │                        │
    │  Bahasa:     │ Bahasa:      │ Bahasa:                │
    │  Swift       │ Kotlin/Java  │ Flutter, React Native  │
    │  Toko:       │ Toko:        │ Satu kode untuk semua  │
    │  App Store   │ Play Store   │ platform               │
    │              │              │                        │
    │  ✅ Performa │ ✅ Performa  │ ✅ Hemat waktu         │
    │  ❌ Mahal    │ ❌ Mahal     │ ❌ Performa kurang     │
    └──────────────┴──────────────┴────────────────────────┘
    ```

    ### App Inventor — Cara Mudah Buat Aplikasi!
    **MIT App Inventor** adalah platform **drag-and-drop** untuk membuat aplikasi Android tanpa coding rumit.

    ```python
    # Di App Inventor, kamu "coding" dengan memblok visual:
    # ┌─────────────────────────┐
    # │ when Button1.Click     │
    # │   do set Label1.Text   │
    # │      to "Halo Dunia!"  │
    # └─────────────────────────┘
    ```

    | Komponen | Fungsi | Seperti di Coding |
    |----------|--------|-------------------|
    | **Button** | Tombol yang bisa diklik | Event handler |
    | **Label** | Teks yang ditampilkan | Variable output |
    | **TextBox** | Input teks dari user | Input |
    | **Notifier** | Pesan pop-up | Alert/Toast |
    | **TinyDB** | Simpan data lokal | Database lokal |

    ### 🔍 Cek Pemahaman
    1. Sebutkan 3 jenis aplikasi mobile! Apa kelebihan dan kekurangan masing-masing?
    2. Apa itu MIT App Inventor? Mengapa platform ini cocok untuk pemula?
    3. Komponen App Inventor apa yang berfungsi seperti "variable output" dalam pemrograman teks?

    ### 📋 Studi Kasus
    OSIS SMA ingin membuat **aplikasi informasi sekolah** yang bisa diakses semua siswa. Aplikasi ini harus menampilkan jadwal pelajaran, pengumuman, dan daftar ekstrakurikuler. Ketua OSIS bertanya padamu apakah sebaiknya aplikasi dibuat native Android (Kotlin), iOS (Swift), atau menggunakan App Inventor.

    **Analisis:**
    1. Platform mana yang paling tepat untuk proyek ini? Pertimbangkan biaya, waktu, dan keahlian tim!
    2. Fitur apa saja yang bisa dibuat dengan App Inventor untuk aplikasi informasi sekolah ini?
    """)

def c5_b():
    return dedent("""
    ### 🎨 Membangun UI dengan App Inventor

    ### Designer — Tampilan Aplikasi
    Di App Inventor, ada 2 bagian utama: **Designer** (tampilan) dan **Blocks** (logika).

    ```
    ┌────────────────────────────────────────────────────┐
    │              APP INVENTOR DESIGNER                 │
    ├────────────────────────────────────────────────────┤
    │                                                    │
    │   ┌──────────────────────────────┐                 │
    │   │       JUDUL APLIKASI         │ ← Label        │
    │   ├──────────────────────────────┤                 │
    │   │                              │                 │
    │   │  [ Masukkan nama kamu ]      │ ← TextBox      │
    │   │                              │                 │
    │   │   ┌──────────────────────┐   │                 │
    │   │   │     SAYA HALO!       │   │ ← Button       │
    │   │   └──────────────────────┘   │                 │
    │   │                              │                 │
    │   │   ┌──────────────────────┐   │                 │
    │   │   │   Halo, Dani!        │   │ ← Label (hasil) │
    │   │   └──────────────────────┘   │                 │
    │   └──────────────────────────────┘                 │
    │                                                    │
    ├────────────────────────────────────────────────────┤
    │ Palette: Button, Label, TextBox, ListView, ...    │
    └────────────────────────────────────────────────────┘
    ```

    ### Komponen Dasar UI
    | Komponen | Letak di Palette | Fungsi |
    |----------|-----------------|--------|
    | **Button** | User Interface | Tombol interaktif |
    | **Label** | User Interface | Teks statis/dinamis |
    | **TextBox** | User Interface | Input teks |
    | **Image** | User Interface | Tampilkan gambar |
    | **ListView** | User Interface | Daftar pilihan |
    | **HorizontalArrangement** | Layout | Atur komponen horizontal |
    | **VerticalArrangement** | Layout | Atur komponen vertikal |
    | **Notifier** | User Interface | Pesan pop-up |

    ### 📝 Tugas: Buat Aplikasi "Perkenalan"
    **Fitur:** Input nama → Klik tombol → Muncul "Halo, [nama]!"

    > ✍️ **Langkah:** 1) Seret Label, TextBox, Button, Label (hasil). 2) Atur properti (teks, warna, ukuran). 3) Buat blok: when Button.Click → set LabelHasil.Text ke "Halo, " + TextBox.Text

    ### 🔍 Cek Pemahaman
    1. Sebutkan 5 komponen UI dasar di App Inventor dan fungsinya!
    2. Apa perbedaan antara HorizontalArrangement dan VerticalArrangement?
    3. Jelaskan cara membuat aplikasi "Halo, [nama]!" menggunakan App Inventor!

    ### 📋 Studi Kasus
    Kamu diminta membuat **aplikasi perpustakaan sekolah** sederhana. Aplikasi harus memiliki: judul "Perpustakaan SMA", kolom pencarian buku, tombol "Cari", dan area hasil pencarian. Temanmu sudah membuat desain di kertas, dan kamu perlu mewujudkannya di App Inventor.

    **Analisis:**
    1. Komponen UI apa saja yang diperlukan untuk membuat aplikasi tersebut? Gambarkan tata letaknya!
    2. Buatlah blok logika sederhana untuk tombol "Cari" — ketika diklik, tampilkan "Mencari..." di label hasil!
    """)

def c5_c():
    return dedent("""
    ### 🔄 Navigasi & Penyimpanan Data

    ### Navigasi Antar Screen
    Aplikasi biasanya punya lebih dari 1 layar. App Inventor mendukung **multi-screen**.

    ```
    Screen1 (Menu)          Screen2 (Detail)
    ┌──────────────────┐    ┌──────────────────┐
    │  📱 Aplikasi Ku  │    │  Detail Item     │
    │                  │    │                  │
    │  [☰ Lihat Data]──────►│  Nama: Andi      │
    │  [➕ Tambah]     │    │  Kelas: XI       │
    │  [ℹ️ Tentang]    │    │  [◀ Kembali]──────►│
    └──────────────────┘    └──────────────────┘
    ```

    ```blocks
    # Blok untuk pindah screen
    when ButtonLihat.Click
        do open another screen screenName "Screen2"
    ```

    ### Menyimpan Data dengan TinyDB
    **TinyDB** adalah database lokal yang menyimpan data **key-value** (seperti kamus/dictionary di Python).

    ```python
    # Konsep TinyDB seperti dictionary Python:
    data = {"nama": "Andi", "kelas": "XI"}
    
    # Di App Inventor:
    # ┌──────────────────────────────────────┐
    # │ call TinyDB1.StoreValue              │
    # │   tag     "nama"                     │ ── Simpan
    # │   valueToStore "Andi"                │
    # └──────────────────────────────────────┘
    # ┌──────────────────────────────────────┐
    # │ call TinyDB1.GetValue                │
    # │   tag     "nama"                     │ ── Ambil
    # │   valueIfTagNotThere ""              │
    # └──────────────────────────────────────┘
    ```

    | Screen | Fungsi | Data yang Disimpan | 
    |--------|--------|-------------------|
    | **Screen1** | Form input | Nama, kelas ke TinyDB |
    | **Screen2** | Tampilkan data | Baca dari TinyDB |

    > ✍️ **Latihan:** Buat aplikasi catatan harian dengan TextBox untuk input dan TinyDB untuk menyimpan!

    ### 🔍 Cek Pemahaman
    1. Bagaimana cara pindah dari Screen1 ke Screen2 di App Inventor?
    2. Apa perbedaan TinyDB dengan variabel biasa? Kapan sebaiknya menggunakan TinyDB?
    3. Jelaskan konsep penyimpanan key-value pada TinyDB menggunakan analogi kamus!

    ### 📋 Studi Kasus
    Seorang siswa bernama Fajar ingin membuat **aplikasi catatan harian (diary)**. Aplikasi memiliki 2 screen: Screen1 untuk menulis catatan dengan TextBox dan tombol "Simpan", Screen2 untuk menampilkan daftar semua catatan yang sudah disimpan. Fajar bingung bagaimana menyimpan catatan agar tidak hilang saat aplikasi ditutup.

    **Analisis:**
    1. Komponen App Inventor apa yang sebaiknya Fajar gunakan untuk menyimpan catatan? Mengapa?
    2. Buatlah alur logika (pseudocode/blocks) untuk proses: tulis catatan → simpan → tampilkan di Screen2!
    """)

def c5_d():
    return dedent("""
    ### 🤖 Integrasi Library AI ke Aplikasi
    **Library AI** adalah kumpulan fungsi siap pakai untuk menambahkan **kecerdasan buatan** ke aplikasi.

    > 🧩 **Analogi:** Library AI itu seperti **indera buatan** untuk aplikasimu. Mau aplikasi bisa melihat? Tambahkan library computer vision. Mau bisa mendengar? Tambahkan library speech recognition. Mau bisa bicara? Tambahkan text-to-speech. **Aplikasi jadi punya "panca indera" digital!**

    ### Library AI di App Inventor
    App Inventor punya **extension** (tambahan) untuk AI:

    | Library AI | Kemampuan | Seperti Indera |
    |-----------|-----------|---------------|
    | **LookExtension** | Mengenali objek di gambar | Mata 👁️ |
    | **SoundExtension** | Mengenali suara | Telinga 👂 |
    | **TranslateExtension** | Menerjemahkan teks | Otak bahasa 🧠 |
    | **TextToSpeech** | Membacakan teks | Mulut 🗣️ |
    | **PersonalImageClassifier** | Belajar mengenali gambar sendiri | Belajar 🎓 |

    ### Cara Menambahkan Extension
    ```
    1. Di App Inventor, buka menu Palette
    2. Scroll ke bawah → Extension
    3. Klik "Import extension"
    4. Upload file .aix (extension file)
    5. Extension siap digunakan!
    ```

    ### Contoh: Integrasi AI Look
    ```blocks
    # Saat tombol ditekan, kamera aktif dan AI mengenali objek
    when ButtonFoto.Click
        do call LookExtension1.Detect
                imageData Camera1.Picture
    
    when LookExtension1.Detected
        # Hasil deteksi muncul di Label,
        # misal: "Saya melihat: mobil (95%)"
    ```

    > 🔑 **Konsep Penting:** AI bukan magic — dia **belajar dari data**. Makin banyak data training, makin akurat hasilnya!

    ### 🔍 Cek Pemahaman
    1. Apa yang dimaksud dengan Library AI? Berikan 3 contoh library AI di App Inventor!
    2. Bagaimana cara menambahkan extension di App Inventor?
    3. Mengapa AI membutuhkan data training yang banyak untuk bisa akurat?

    ### 📋 Studi Kasus
    Dalam pelajaran Biologi, kelas XI mendapat tugas **mengidentifikasi tanaman obat** di sekitar sekolah. Ada 20 jenis tanaman yang harus dikenali. Seorang siswa bernama Dewi ingin membuat aplikasi yang bisa mengenali tanaman obat hanya dengan memotretnya menggunakan HP.

    **Analisis:**
    1. Library AI apa yang paling tepat untuk aplikasi Dewi? Jelaskan cara kerjanya!
    2. Jika aplikasi sering salah mengenali tanaman, apa yang perlu dilakukan? Jelaskan alasannya!
    """)

def c5_e():
    return dedent("""
    ### 🖼️ Image Classification & Speech Recognition
    Dua kemampuan AI yang paling populer: **mengenali gambar** dan **mengenali suara**.

    ### Image Classification — AI Melihat
    **Cara Kerja:**
    ```
    [Input Gambar] → [AI Model] → [Hasil Klasifikasi]
         ↓              ↓                ↓
    Foto kucing    CNN (Convolutional    "Kucing"
    dari kamera    Neural Network)        (confidence: 95%)
    ```

    ### Aktivitas: Klasifikasi Gambar
    1. Ambil foto 3 benda berbeda (buku, botol, pensil)
    2. Gunakan LookExtension untuk mendeteksi
    3. Catat: apakah AI benar? Seberapa yakin?

    | Benda | Hasil Deteksi | Confidence | Benar/Salah |
    |-------|--------------|------------|-------------|
    | Buku tulis | "Book" | 92% | ✅ |
    | Botol minum | "Water bottle" | 87% | ✅ |
    | Pensil | "Pencil" | 76% | ✅ |

    ### Speech Recognition — AI Mendengar
    **Cara Kerja:**
    ```
    [Suara] → [Speech-to-Text] → [Teks]
    "Halo, apa kabar?"           "Halo apa kabar"
    ```

    ### Aktivitas: Aplikasi Voice Note
    Buat aplikasi yang bisa:
    1. Merekam suara (klik tombol → bicara)
    2. Mengubah suara menjadi teks
    3. Menyimpan teks ke TinyDB

    ```blocks
    when ButtonRekam.Click
        do call SoundExtension1.Recognize
    
    when SoundExtension1.AfterRecognize
        do set LabelHasil.Text to result
           call TinyDB1.StoreValue tag "catatan" value result
    ```

    > 💡 **Tahukah Kamu?** Siri, Google Assistant, dan Alexa menggunakan teknologi yang sama — Speech Recognition + NLP!

    ### 🔍 Cek Pemahaman
    1. Jelaskan cara kerja Image Classification menggunakan CNN!
    2. Bagaimana Speech Recognition mengubah suara menjadi teks?
    3. Apa yang dimaksud dengan "confidence score" dalam hasil deteksi AI? Mengapa penting?

    ### 📋 Studi Kasus
    Di sekolah kamu ada seorang siswa tunanetra bernama Bagas yang kesulitan mencatat pelajaran. Kamu ingin membuat **aplikasi voice note** yang bisa merekam penjelasan guru, mengubahnya menjadi teks, dan menyimpannya. Ini akan sangat membantu Bagas dan teman-teman lain.

    **Analisis:**
    1. Fitur AI apa saja yang diperlukan untuk aplikasi voice note tersebut? Jelaskan alurnya!
    2. Jika guru menjelaskan dalam 3 bahasa (Indonesia, Inggris, Jawa), tantangan apa yang mungkin muncul? Bagaimana solusinya?
    """)

def c5_f():
    return dedent("""
    ### 📋 Proyek Aplikasi AI: Perencanaan

    ### Tugas Akhir Bab 5
    Buatlah **aplikasi mobile berbasis AI** untuk menyelesaikan masalah nyata di sekitar sekolah/rumah!

    ### Ide Proyek
    | Proyek | Fitur AI | Masalah yang Diselesaikan |
    |--------|----------|--------------------------|
    | **Pengenal Tanaman Obat** | Image Classification | Tanaman obat sulit dikenali |
    | **Penerjemah Bahasa Daerah** | Text Translation | Melestarikan bahasa daerah |
    | **Pengingat Tugas Sekolah** | Text-to-Speech + TinyDB | Suka lupa tugas |
    | **Detektor Sampah Organik** | Image Classification | Sulit memilah sampah |
    | **Aplikasi Belajar Bahasa Inggris** | Speech Recognition | Latihan pronunciation |

    ### Rencana Proyek (Template)
    | Aspek | Isian |
    |-------|-------|
    | **Nama Aplikasi** | ... |
    | **Anggota Tim** | ... |
    | **Masalah** | ... |
    | **Fitur Utama** | 1. ... 2. ... 3. ... |
    | **AI Library yang Digunakan** | ... |
    | **Desain UI** | (sketsa/layout) |
    | **Pembagian Tugas** | ... |
    | **Target Selesai** | ... |

    > 💡 **Tips Memilih Proyek:** Pilih masalah yang kamu ALAMI sendiri — kamu akan lebih termotivasi menyelesaikannya!

    ### 🔍 Cek Pemahaman
    1. Sebutkan 3 ide proyek aplikasi AI yang bisa dibuat dengan App Inventor!
    2. Apa saja komponen yang harus ada dalam rencana proyek aplikasi?
    3. Mengapa penting memilih masalah yang kamu alami sendiri sebagai topik proyek?

    ### 📋 Studi Kasus
    Kelompokmu (5 orang) mendapat tugas proyek aplikasi AI. Setiap anggota memiliki ide berbeda: Andi ingin membuat aplikasi pengenal sampah organik, Budi ingin membuat penerjemah bahasa Sunda, Citra ingin membuat pengingat tugas sekolah, Dewi ingin membuat detektor kemacetan, dan Eko ingin membuat aplikasi belajar Bahasa Inggris.

    **Analisis:**
    1. Bantulah kelompokmu memilih SATU ide proyek yang paling layak! Pertimbangkan: waktu (2 minggu), keahlian, data yang tersedia, dan dampak!
    2. Buatlah rencana proyek lengkap untuk ide yang terpilih (nama, fitur, AI library, pembagian tugas)!
    """)

def c5_g():
    return dedent("""
    ### 🚀 Proyek Aplikasi AI: Implementasi & Presentasi

    ### Tahap Implementasi
    ```python
    # Pseudocode alur implementasi:
    
    # 1. SETUP
    - Buka App Inventor
    - Buat project baru
    - Import extension AI yang dibutuhkan
    
    # 2. DESIGNER
    - Buat Screen1 (input/utama)
    - Buat Screen2 (hasil)
    - Tambahkan komponen: Button, Label, Camera, dll
    
    # 3. BLOCKS (logika)
    - when Button.Click → aktifkan fitur AI
    - when AI.Detected → tampilkan hasil
    - Simpan data ke TinyDB
    
    # 4. TESTING
    - Uji coba di emulator/smartphone
    - Catat bug dan perbaiki
    
    # 5. FINAL
    - Build APK
    - Siapkan slide presentasi
    ```

    ### Rubrik Penilaian Proyek
    | Aspek | Bobot | Kriteria |
    |-------|-------|----------|
    | **Fungsionalitas** | 30% | Aplikasi berjalan tanpa error |
    | **Fitur AI** | 25% | AI berfungsi dengan baik |
    | **UI/UX** | 15% | Tampilan rapi, mudah digunakan |
    | **Dokumentasi** | 15% | Laporan lengkap |
    | **Presentasi** | 15% | Demo lancar, menjelaskan dengan baik |

    ### Tips Presentasi
    1. **Mulai dengan masalah** — kenapa aplikasi ini penting?
    2. **Demo langsung** — tunjukkan aplikasi bekerja (bukan slide!)
    3. **Ceritakan kendala** — jujur tentang kesulitan dan bagaimana mengatasinya
    4. **Refleksikan pembelajaran** — apa yang paling berkesan dari proyek ini?

    > 🎯 **Ingat:** Proyek ini bukan cuma soal nilai. Ini **portofolio pertamamu** sebagai developer! Simbaik baik-baik untuk bekal masa depan.

    ### 🔍 Cek Pemahaman
    1. Sebutkan 5 tahap implementasi proyek aplikasi AI!
    2. Apa saja aspek yang dinilai dalam rubrik penilaian proyek? Mana yang bobotnya paling besar?
    3. Mengapa penting untuk memulai presentasi dengan "masalah" bukan dengan "fitur aplikasi"?

    ### 📋 Studi Kasus
    Hari presentasi proyek tiba. Kelompok Rina membuat aplikasi "EcoScan" — pendeteksi jenis sampah menggunakan Image Classification. Saat demo di depan kelas, aplikasi tiba-tiba crash saat memotret sampah plastik. Rina panik dan tidak tahu harus berbuat apa.

    **Analisis:**
    1. Apa yang sebaiknya Rina lakukan saat demo mengalami error? Berikan strategi menghadapi situasi tersebut!
    2. Setelah presentasi, bagaimana cara Rina memperbaiki aplikasinya? Langkah debugging apa yang harus dilakukan?
    """)


# ─── BAB 6: Proyek Analisis Data ───────────────────────────────

def c6_a():
    return dedent("""
    ### 📊 Big Data: Era Data Raksasa
    **Big Data** adalah kumpulan data berukuran sangat besar yang tidak bisa diolah dengan cara tradisional.

    > 🧩 **Analogi:** Big Data itu seperti **samudra**. Kalau mau ambil segelas air, cukup pakai gelas. Tapi kalau mau memindahkan seluruh samudra, butuh teknologi khusus. Big Data adalah "teknologi khusus" untuk mengelola data raksasa!

    ### 5V Big Data
    ```
    1. VOLUME  — Ukuran besar (terabyte - petabyte)
    2. VELOCITY — Kecepatan data masuk (real-time)
    3. VARIETY  — Ragam jenis data (teks, gambar, video, sensor)
    4. VERACITY — Ketidakpastian/kualitas data
    5. VALUE   — Nilai/manfaat data setelah diolah
    ```

    ### Sumber Big Data
    | Sumber | Contoh Data | Volume per Hari |
    |--------|-------------|----------------|
    | **Media Sosial** | Postingan, like, komentar | 500 juta tweet |
    | **Sensor IoT** | Suhu, kelembaban, gerakan | Miliaran data point |
    | **Transaksi** | Belanja online, transfer bank | Jutaan transaksi |
    | **Video** | YouTube, CCTV, streaming | 500 jam video/menit |
    | **Kesehatan** | Rekam medis, genome | Terabyte per rumah sakit |

    ### Big Data di Indonesia
    - **Gojek** — memproses jutaan transaksi per hari
    - **BPJS Kesehatan** — data 200+ juta peserta
    - **Dana** — jutaan transaksi digital per hari
    - **E-commerce** — jutaan produk, review, transaksi

    > 💬 **Diskusi:** Data apa saja yang kamu hasilkan setiap hari? Berapa kira-kira ukurannya?

    ### 🔍 Cek Pemahaman
    1. Sebutkan dan jelaskan 5V dari Big Data!
    2. Berikan 3 contoh sumber Big Data beserta volume data yang dihasilkan setiap hari!
    3. Mengapa Big Data di Indonesia seperti Gojek dan BPJS disebut sebagai contoh Big Data?

    ### 📋 Studi Kasus
    Kantin sekolah SMA Merdeka melayani sekitar 500 siswa setiap hari. Setiap transaksi mencatat: nama siswa, makanan yang dibeli, harga, dan waktu pembelian. Selama 1 bulan, terkumpul ribuan data transaksi. Kepala sekolah ingin mengetahui menu apa yang paling laris, jam berapa kantin paling ramai, dan berapa rata-rata pengeluaran siswa per hari.

    **Analisis:**
    1. Apakah data kantin tersebut sudah bisa disebut Big Data? Jelaskan menggunakan konsep 5V!
    2. Data apa saja yang perlu dikumpulkan agar analisisnya lebih akurat?
    """)

def c6_b():
    return dedent("""
    ### 🔧 Pengolahan Data dengan Tools Digital
    Data mentah tidak berguna tanpa **pengolahan**. Tools digital membantu mengubah data menjadi informasi.

    > 🧩 **Analogi:** Data mentah itu seperti **bahan makanan di dapur**. Mentah, belum bisa dimakan. Tapi setelah diolah — dipotong, dimasak, dibumbui — jadilah hidangan lezat. **Pengolahan data = memasak!**

    ### Tools Pengolahan Data
    | Tools | Tingkat Kesulitan | Fungsi Utama |
    |-------|------------------|-------------|
    | **Microsoft Excel** | 🟢 Mudah | Spreadsheet, formula, pivot table |
    | **Google Sheets** | 🟢 Mudah | Spreadsheet online, kolaborasi real-time |
    | **Python (Pandas)** | 🔴 Sulit | Analisis data tingkat lanjut |
    | **Tableau Public** | 🟡 Sedang | Visualisasi data interaktif |
    | **Google Data Studio** | 🟡 Sedang | Dashboard data |

    ### Siklus Pengolahan Data
    ```
    ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐
    │  KOLEKSI │   │  BERSIH- │   │  ANALISIS│   │  VISUA-  │
    │  Data    │──►│  KAN     │──►│  Data    │──►│  LISASI  │
    │          │   │  (Cleaning)│  │          │   │  & Lapor │
    └──────────┘   └──────────┘   └──────────┘   └──────────┘
    ```

    ### Studi Kasus: Analisis Data Nilai Kelas
    ```python
    import pandas as pd
    
    data = {
        "nama": ["Andi", "Budi", "Citra", "Dewi"],
        "nilai": [85, 72, 90, 78]
    }
    df = pd.DataFrame(data)
    
    print(f"Rata-rata: {df['nilai'].mean()}")    # 81.25
    print(f"Tertinggi: {df['nilai'].max()}")      # 90
    print(f"Terendah: {df['nilai'].min()}")        # 72
    print(f"Lulus (>=78): {df[df['nilai'] >= 78]}")
    ```

    > ✍️ **Latihan:** Kumpulkan data tinggi badan 10 teman sekelasmu. Gunakan Excel/Google Sheets untuk: rata-rata, tertinggi, terendah!

    ### 🔍 Cek Pemahaman
    1. Sebutkan 4 tahap dalam siklus pengolahan data!
    2. Apa perbedaan antara data mentah dan informasi? Berikan contoh!
    3. Tools apa yang paling tepat digunakan untuk analisis data sederhana? Untuk analisis tingkat lanjut?

    ### 📋 Studi Kasus
    Setelah ujian tengah semester, wali kelas XI IPA 2 ingin menganalisis hasil ujian 35 siswa. Data yang tersedia adalah nama siswa dan nilai untuk 5 mata pelajaran. Wali kelas ingin tahu: rata-rata nilai per mapel, siswa dengan nilai tertinggi dan terendah, serta berapa siswa yang tidak lulus (nilai < 70) di setiap mapel.

    **Analisis:**
    1. Tools apa yang paling tepat digunakan wali kelas? Jelaskan langkah-langkah analisisnya!
    2. Buat contoh data sederhana (5 siswa, 3 mapel) dan hitung rata-rata, nilai tertinggi, dan nilai terendah menggunakan Python (Pandas)!
    """)

def c6_c():
    return dedent("""
    ### 📈 Visualisasi Data yang Menarik
    **Visualisasi data** adalah penyajian data dalam bentuk **grafik, diagram, atau peta** agar mudah dipahami.

    > 🧩 **Analogi:** Visualisasi data itu seperti **poster dibandingkan novel**. Novel 300 halaman butuh waktu berhari-hari untuk dibaca. Poster yang bagus bisa menyampaikan pesan dalam 3 detik. **Visualisasi data adalah poster untuk datamu!**

    ### Jenis Visualisasi
    ```
    📊 BAR CHART — Bandingkan kategori (nilai per mapel)
        ██ 85
        ██████ 90
        ██ 78
    
    📈 LINE CHART — Tren dari waktu ke waktu (nilai per semester)
        ─╱╲──╱╲──╱╲──
        80─85─78─90
    
    🥧 PIE CHART — Proporsi/bagian dari total (%
    suara)
        ⬤

    🗺️ HEATMAP — Konsentrasi data (daerah rawan)
        🟥🟧🟨🟩
    
    📋 TABLE — Data detail
        Nama │ Nilai
        ─────┼──────
        Andi │ 85
    ```

    ### Aturan Visualisasi yang Baik
    ✅ **Sederhana** — jangan terlalu banyak informasi
    ✅ **Akurat** — skala sumbu jangan dimanipulasi
    ✅ **Kontekstual** — beri judul dan label yang jelas
    ✅ **Warna bijak** — jangan gunakan > 5 warna
    ❌ **3D chart** — sering menyesatkan persepsi
    ❌ **Pie chart > 5 kategori** — susah dibaca

    ### ✍️ Aktivitas
    1. Kumpulkan data: jumlah siswa per jurusan di sekolahmu
    2. Buat bar chart dan pie chart di Excel/Google Sheets
    3. Bandingkan: mana yang lebih mudah dipahami?
    4. Presentasikan ke kelas!

    ### 🔍 Cek Pemahaman
    1. Sebutkan 3 jenis visualisasi data dan kapan waktu yang tepat menggunakan masing-masing!
    2. Apa aturan visualisasi data yang baik? Sebutkan minimal 3!
    3. Mengapa pie chart tidak disarankan untuk lebih dari 5 kategori?

    ### 📋 Studi Kasus
    OSIS sekolah ingin membuat **laporan tahunan** dalam bentuk infografis yang menarik. Data yang dimiliki: jumlah siswa per jurusan (IPA 120, IPS 90, Bahasa 45), tren nilai rata-rata sekolah 3 tahun terakhir (83, 85, 87), dan alokasi dana OSIS (kegiatan 60%, perlengkapan 25%, cadangan 15%). Ketua OSIS meminta bantuanmu memilih visualisasi yang tepat.

    **Analisis:**
    1. Jenis visualisasi apa yang paling tepat untuk masing-masing data tersebut? Jelaskan alasannya!
    2. Buat sketsa infografis sederhana untuk laporan tahunan OSIS tersebut!
    """)

def c6_d():
    return dedent("""
    ### 🎯 Proyek Analisis Data: Desain

    ### Tugas Akhir Bab 6 — Proyek Analisis Data
    Lakukan analisis data nyata dari lingkungan sekitarmu!

    ### Pilih Topik
    | Topik | Data yang Dikumpulkan | Sumber Data |
    |-------|----------------------|-------------|
    | **Polusi Udara** | PM2.5, suhu, kelembaban | Sensor IoT / BMKG |
    | **Nilai Ujian** | Nilai per mapel, tren | Data sekolah |
    | **Kebiasaan Belajar** | Jam belajar, nilai | Survei teman sekelas |
    | **Pengeluaran** | Uang saku, pengeluaran | Survei siswa |
    | **Trafik Sekolah** | Jumlah siswa per jam | Observasi/pintu gerbang |

    ### Template Perencanaan
    ```
    ┌──────────────────────────────────────────────────┐
    │           PROYEK ANALISIS DATA                   │
    ├──────────────────────────────────────────────────┤
    │                                                    │
    │  JUDUL: [judul proyek]                             │
    │                                                    │
    │  PERTANYAAN: [apa yang ingin diketahui?]           │
    │  • Apakah ada hubungan jam belajar & nilai?        │
    │  • Bagaimana tren nilai dari semester 1 ke 2?      │
    │                                                    │
    │  DATA: [data apa yang dikumpulkan?]                │
    │  • 50 siswa kelas XI                               │
    │  • Variabel: jam belajar, nilai ujian              │
    │                                                    │
    │  METODE: [tools & teknik]                          │
    │  • Google Forms (koleksi data)                     │
    │  • Python/Excel (analisis)                         │
    │  • Canva/Data Studio (visualisasi)                 │
    │                                                    │
    │  OUTPUT: [apa yang akan dihasilkan?]               │
    │  • Laporan analisis (PDF)                          │
    │  • Poster infografis                               │
    │  • Presentasi 10 slide                             │
    └──────────────────────────────────────────────────┘
    ```

    > 💡 **Pilih data yang MUDAH dikumpulkan** — lebih baik proyek sederhana selesai daripada proyek ambisius tapi tidak selesai!

    ### 🔍 Cek Pemahaman
    1. Sebutkan 5 topik proyek analisis data yang bisa dilakukan di lingkungan sekolah!
    2. Apa saja komponen yang harus ada dalam template perencanaan proyek analisis data?
    3. Mengapa penting untuk menentukan pertanyaan penelitian sebelum mengumpulkan data?

    ### 📋 Studi Kasus
    Kelompokmu tertarik meneliti **tingkat polusi udara** di sekitar sekolah. Namun, alat sensor PM2.5 harganya mahal. Kalian punya waktu 2 minggu dan anggaran Rp0. Sumber data yang tersedia: data BMKG online, observasi visual (kepadatan kendaraan), dan wawancara warga sekitar.

    **Analisis:**
    1. Sesuaikan rencana proyek dengan kendala yang ada! Data apa yang bisa dikumpulkan dengan sumber yang tersedia?
    2. Buat rancangan proyek singkat: pertanyaan penelitian, data yang dikumpulkan, tools analisis, dan output!
    """)

def c6_e():
    return dedent("""
    ### 🏁 Proyek Analisis Data: Implementasi

    ### Tahap Implementasi
    ```python
    # 1. KOLEKSI DATA
    # Buat Google Forms, sebarkan ke responden
    # Export ke CSV / Google Sheets
    
    # 2. BERSIHKAN DATA (Cleaning)
    import pandas as pd
    df = pd.read_csv("data_survei.csv")
    df = df.dropna()  # Hapus baris kosong
    df = df[df['jam_belajar'] > 0]  # Filter data valid
    
    # 3. ANALISIS
    rata_jam = df['jam_belajar'].mean()
    rata_nilai = df['nilai'].mean()
    korelasi = df['jam_belajar'].corr(df['nilai'])
    print(f"Korelasi jam belajar & nilai: {korelasi}")
    
    # 4. VISUALISASI
    import matplotlib.pyplot as plt
    plt.scatter(df['jam_belajar'], df['nilai'])
    plt.xlabel('Jam Belajar/hari')
    plt.ylabel('Nilai Ujian')
    plt.title('Hubungan Jam Belajar & Nilai')
    plt.savefig('grafik.png')
    ```

    ### Format Laporan
    | Bab | Isi |
    |-----|-----|
    | **1. Pendahuluan** | Latar belakang, pertanyaan penelitian |
    | **2. Metode** | Cara pengumpulan data, tools |
    | **3. Hasil** | Tabel, grafik, temuan utama |
    | **4. Analisis** | Interpretasi data, insight |
    | **5. Kesimpulan** | Jawaban pertanyaan, saran |

    ### Tips Presentasi
    1. **Cerita dulu, data kemudian** — mulai dengan narasi
    2. **Satu slide = satu pesan** — jangan terlalu penuh
    3. **Visual > Teks** — pakai grafik, bukan tabel besar
    4. **Panggil insight** — "Ternyata... yang mengejutkan adalah..."

    ### 🔍 Cek Pemahaman
    1. Sebutkan 5 tahap implementasi proyek analisis data!
    2. Apa perbedaan antara analisis dan interpretasi data?
    3. Sebutkan 4 tips presentasi data yang efektif!

    ### 📋 Studi Kasus
    Setelah berminggu-minggu mengerjakan proyek analisis data tentang **kebiasaan belajar**, kelompokmu menemukan temuan menarik: ternyata siswa yang belajar antara 2-3 jam per hari mendapat nilai lebih tinggi daripada yang belajar lebih dari 5 jam. Temuan ini kontroversial karena bertentangan dengan anggapan umum "makin lama belajar, makin pintar".

    **Analisis:**
    1. Bagaimana sebaiknya kelompokmu mempresentasikan temuan ini agar tidak disalahpahami? Strategi apa yang harus digunakan?
    2. Faktor lain apa yang mungkin mempengaruhi hasil ini (confounding variables)? Sebutkan minimal 3!

    ---
    > 🎉 **Selamat!** Kamu telah menyelesaikan perjalanan Informatika kelas XI! Dari coding, AI, hingga analisis data — kamu punya bekal untuk menjadi **pemecah masalah di era digital**. Tetap belajar dan berkarya! 🚀
    """)


# ─── CONTENT MAP ──────────────────────────────────────────────

C = {
    "1_A": c1_a, "1_B": c1_b, "1_C": c1_c,
    "2_A": c2_a, "2_B": c2_b, "2_C": c2_c, "2_D": c2_d, "2_E": c2_e, "2_F": c2_f,
    "3_A": c3_a, "3_B": c3_b, "3_C": c3_c, "3_D": c3_d,
    "4_A": c4_a, "4_B": c4_b, "4_C": c4_c, "4_D": c4_d, "4_E": c4_e,
    "5_A": c5_a, "5_B": c5_b, "5_C": c5_c, "5_D": c5_d, "5_E": c5_e, "5_F": c5_f, "5_G": c5_g,
    "6_A": c6_a, "6_B": c6_b, "6_C": c6_c, "6_D": c6_d, "6_E": c6_e,
}

# ─── GENERATE ─────────────────────────────────────────────────

def generate_all():
    print("=" * 60)
    print("GENERATOR MATERI AJAR KELAS XI")
    print("6 Bab — format menarik, analogi, diagram, contoh nyata")
    print("=" * 60)
    total_lines = 0

    for bab in BAB:
        k = bab["id"]; judul = bab["judul"]; emoji = bab["emoji"]; sub = bab["sub"]; smt = bab["smt"]
        lines = []
        lines.append(f"# {emoji} Bab {k}: {judul}\n")
        lines.append(f"> **Semester {'Ganjil' if smt == 1 else 'Genap'}** | **Fase F** | **Kelas XI** | **{len(sub)*5} JP**\n")
        lines.append("---\n")
        lines.append("## 📊 Pemetaan Capaian Pembelajaran\n")
        lines.append("| Elemen CP | Deskripsi CP |")
        lines.append("|-----------|-------------|")
        for elemen, desc in CP_MAP.get(k, []):
            lines.append(f"| {elemen} | {desc} |")
        lines.append("")
        lines.append("---\n")
        lines.append("## 🎯 Tujuan Pembelajaran\n")
        for h, jdl in sub:
            lines.append(f"- **{h}.** {jdl}")
        lines.append("")
        lines.append("## 🗺️ Peta Konsep\n")
        lines.append("```")
        lines.append(f"               {emoji} {judul.upper()}")
        lines.append(f"                     |")
        for i, (h, jdl) in enumerate(sub):
            prefix = "                     ├──" if i < len(sub)-1 else "                     └──"
            lines.append(f"{prefix} {h}. {jdl}")
        lines.append("```\n")

        for h, jdl in sub:
            key = f"{k}_{h}"
            fn = C.get(key)
            lines.append(f"## {h}. {jdl}\n")
            if fn:
                lines.append(fn())
            else:
                lines.append(f"*[Materi {jdl} sedang dikembangkan]*\n")
            lines.append("")
            lines.append("> 🤔 **Mari Renungkan:** Apa hal paling menarik yang kamu pelajari dari bagian ini?\n")
            lines.append("---\n")

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

        lines.append("## 📝 Rangkuman\n")
        for point in RANGKUMAN.get(k, []):
            lines.append(f"- {point}")
        lines.append("")
        lines.append("---\n## ✍️ Latihan Soal\n")
        lines.append("### Pilihan Ganda\n")
        for i, (q, opts, ans) in enumerate(SOAL_PG.get(k, []), 1):
            lines.append(f"{i}. {q}")
            for opt in opts:
                lines.append(f"   {opt}")
            lines.append(f"   **Kunci Jawaban: {ans.upper()}**")
            lines.append("")
        lines.append("### Uraian\n")
        for i, soal in enumerate(SOAL_URAIAN.get(k, []), 1):
            lines.append(f"{i}. {soal}\n")

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
        lines.append("## 🚀 Tugas Pengayaan\n")
        for p_judul, p_desc in PENGAYAAN.get(k, []):
            lines.append(f"### {p_judul}")
            lines.append(f"{p_desc}\n")

        # Glosarium
        lines.append("---")
        lines.append("## 📖 Glosarium\n")
        for term, defn in GLOSARIUM.get(k, []):
            lines.append(f"- **{term}**: {defn}")
        lines.append("")

        # Media Pembelajaran
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
        n = out.count("\n") + 1
        total_lines += n
        print(f"  ✓ Bab {k}: {emoji} {judul} ({n} baris)")

    print(f"\n  → {len(BAB)} file Materi Ajar Kelas XI dibuat.")
    print(f"  → Total: ~{total_lines} baris")
    print("=" * 60)

if __name__ == "__main__":
    generate_all()
