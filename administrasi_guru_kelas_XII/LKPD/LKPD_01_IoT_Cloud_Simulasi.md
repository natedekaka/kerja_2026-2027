# LKPD - Simulasi IoT dan Cloud Platform
**Mata Pelajaran:** Informatika
**Kelas/Semester:** XII / Ganjil
**Materi Pokok:** Bab 1 – Internet of Things (IoT) & Cloud Platform
**Alokasi Waktu:** 5 JP

## A. Tujuan Pembelajaran
1. Peserta didik mampu menjelaskan arsitektur IoT (device, gateway, cloud, aplikasi).
2. Peserta didik mampu menggunakan simulator IoT (Wokwi) untuk merancang sistem sederhana.
3. Peserta didik mampu menghubungkan sensor virtual ke platform cloud (ThingSpeak / Blynk).
4. Peserta didik mampu membaca data dari cloud dashboard.

## B. Alat dan Bahan
- PC/Laptop dengan koneksi internet
- Browser web (Chrome/Firefox/Edge)
- Akun Wokwi (https://wokwi.com) — gratis
- Akun ThingSpeak (https://thingspeak.com) — gratis
- Akun Blynk (https://blynk.io) — opsional

## C. Langkah Kerja

### Bagian 1: Eksplorasi Arsitektur IoT (15 menit)

1. Buka browser dan kunjungi https://wokwi.com
2. Pilih menu **Examples > Arduino Uno**
3. Amati komponen-komponen berikut:
   - **Device Layer**: Mikrokontroler (Arduino Uno), sensor, aktuator
   - **Gateway/Network**: WiFi (pada ESP32/ESP8266)
   - **Cloud/Platform**: ThingSpeak / Blynk
   - **Application Layer**: Dashboard monitoring
4. Gambarlah diagram arsitektur IoT di buku catatan dengan format:

```
+------------------+       +-----------+       +-------------+       +--------------+
|  Device Layer    |       | Gateway   |       | Cloud       |       | Application  |
| (Sensor + MCU)   | ----> | (WiFi)    | ----> | Platform    | ----> | (Dashboard)  |
| Arduino/ESP32    |       | ESP8266   |       | ThingSpeak  |       | Web/Mobile   |
+------------------+       +-----------+       +-------------+       +--------------+
```

### Bagian 2: Simulasi Rangkaian IoT dengan Wokwi (60 menit)

1. Buka https://wokwi.com/projects/new/arduino-uno
2. Hapus kode default, salin kode berikut:

```c
void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  int sensorValue = analogRead(A0);
  float voltage = sensorValue * (5.0 / 1023.0);

  Serial.print("Sensor Value: ");
  Serial.print(sensorValue);
  Serial.print(" | Voltage: ");
  Serial.println(voltage);

  digitalWrite(LED_BUILTIN, HIGH);
  delay(500);
  digitalWrite(LED_BUILTIN, LOW);
  delay(500);
}
```

3. Klik **Start Simulation** dan amati Serial Monitor.
4. Tambahkan komponen **Potentiometer** dari panel komponen:
   - Hubungkan pin tengah potentiometer ke A0
   - Hubungkan pin kiri ke GND, pin kanan ke 5V
5. Putar slider potentiometer dan amati perubahan nilai di Serial Monitor.
6. Catat 5 sampel data ke tabel pengamatan.

### Bagian 3: Koneksi ke Cloud ThingSpeak (60 menit)

1. Buka https://thingspeak.com dan login/daftar akun.
2. Klik **New Channel**, isi:
   - Name: `LKPD IoT - [Nama]`
   - Field 1: `Sensor Voltage`
   - Field 2: `Sensor Value`
   - Simpan dan catat **Write API Key**.
3. Buka project Wokwi baru → pilih **ESP32 Dev Module** (bukan Arduino Uno).
4. Salin kode berikut dan ganti `YOUR_API_KEY` dengan kunci ThingSpeak:

```c
#include <WiFi.h>
#include <HTTPClient.h>

const char* ssid = "Wokwi-GUEST";
const char* password = "";
const char* server = "http://api.thingspeak.com/update";
const char* apiKey = "YOUR_API_KEY";

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nWiFi Connected!");
}

void loop() {
  int sensorValue = analogRead(34);
  float voltage = sensorValue * (3.3 / 4095.0);

  HTTPClient http;
  String url = String(server) + "?api_key=" + apiKey
               + "&field1=" + String(voltage, 2)
               + "&field2=" + String(sensorValue);

  http.begin(url);
  int httpCode = http.GET();

  if (httpCode == 200) {
    Serial.println("Data sent to ThingSpeak!");
  } else {
    Serial.print("Failed, code: ");
    Serial.println(httpCode);
  }

  http.end();
  delay(15000);
}
```

5. Jalankan simulasi. Jika berhasil, data akan muncul di ThingSpeak Channel.
6. Buka tab **Private View** di ThingSpeak untuk melihat grafik.

### Bagian 4: Eksplorasi Dashboard Cloud (45 menit)

1. Di ThingSpeak, klik **Add Visualizations > Chart**.
2. Buat 2 widget:
   - Widget 1: Line Chart untuk Field 1 (Voltage)
   - Widget 2: Gauge untuk Field 2 (Sensor Value)
3. Klik **Save** dan presentasikan dashboard ke guru.

## D. Tabel Hasil/Data Pengamatan

| No | Sensor Value (ADC) | Voltage (V) | Keterangan |
|----|-------------------|-------------|------------|
| 1  |                   |             |            |
| 2  |                   |             |            |
| 3  |                   |             |            |
| 4  |                   |             |            |
| 5  |                   |             |            |

## E. Diskusi dan Analisis

1. Jelaskan perbedaan peran device layer, gateway, dan cloud platform dalam arsitektur IoT!
2. Apa pengaruh perubahan nilai potensiometer terhadap data yang dikirim ke ThingSpeak?
3. Jika koneksi WiFi terputus, apa yang terjadi pada data sensor? Bagaimana cara mengatasinya?
4. Bandingkan penggunaan Wokwi (simulator) dengan perangkat asli. Sebutkan kelebihan dan kekurangan masing-masing!
5. Bagaimana cara ThingSpeak menyimpan dan menampilkan data secara real-time?

## F. Kesimpulan

Buatlah kesimpulan minimal 3 paragraf yang mencakup:
- Prinsip kerja arsitektur IoT
- Pengalaman menggunakan simulator Wokwi
- Pengalaman menghubungkan perangkat ke cloud platform

## G. Penilaian

| Aspek | Bobot | Skor (1-4) | Nilai |
|-------|-------|------------|-------|
| Ketepatan diagram arsitektur IoT | 20% | | |
| Kode program (struktur, komentar) | 25% | | |
| Hasil simulasi dan data pengamatan | 20% | | |
| Dashboard cloud | 15% | | |
| Analisis dan kesimpulan | 20% | | |
| **Total** | **100%** | | |
