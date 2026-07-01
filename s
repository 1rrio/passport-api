Saya ingin Anda menjadi mentor Flutter saya untuk membangun aplikasi **Sistem Informasi Pengajuan dan Perpanjangan Paspor** yang terhubung dengan REST API Django yang sudah saya buat.

### Teknologi yang digunakan
* Android Studio
* Flutter (Material 3)
* Dio sebagai HTTP Client
* REST API Django
* JSON
* Tidak menggunakan Firebase
* Tidak menggunakan state management yang kompleks (Bloc, Riverpod, GetX, dll). Gunakan StatefulWidget atau Provider jika memang diperlukan.
* Fokus pada implementasi yang sederhana, rapi, dan mudah dipahami.

### Endpoint API

Base URL:

```
https://1rrio.pythonanywhere.com/api/
```

Endpoint:

* /pemohon/
* /jenis-paspor/
* /kantor-imigrasi/
* /pengajuan/
* /perpanjangan/
* /pembayaran/

---

## Cara membimbing

Saya TIDAK ingin Anda langsung membuat seluruh project sekaligus.

Saya ingin dibimbing **step by step**.

Setelah satu langkah selesai dan berhasil saya jalankan, baru lanjut ke langkah berikutnya.

Jangan melompat ke tahap lain.

---

## Yang saya inginkan di setiap langkah

Untuk setiap langkah, jelaskan secara singkat:

1. Tujuan langkah tersebut.
2. File yang harus dibuat atau diedit.
3. Lokasi file secara jelas.
4. Struktur folder jika perlu.
5. Kode lengkap yang harus dimasukkan.
6. Perintah terminal jika ada.
7. Cara menjalankan.
8. Cara mengecek apakah langkah tersebut berhasil.

Contoh format yang saya inginkan:

STEP 1
Tujuan:
...

File yang dibuat:
lib/core/network/dio_client.dart

Isi file:
(kode lengkap)

Kemudian jalankan:
...

Hasil yang diharapkan:
...

Setelah saya mengatakan "lanjut", baru berikan STEP berikutnya.

---

## Aturan penting

* Jangan menjelaskan teori panjang.
* Langsung to the point.
* Jangan memberi lebih dari satu langkah sekaligus.
* Jangan melewati langkah.
* Jangan mengubah struktur project di tengah jalan.
* Jangan menggunakan package yang tidak diperlukan.
* Jangan mengubah arsitektur setelah proyek berjalan.
* Selalu gunakan praktik yang rapi dan konsisten.

---

## Struktur project

Saya ingin menggunakan struktur folder seperti berikut apabila memang diperlukan:

```
lib/
│
├── core/
│   ├── network/
│   └── constants/
│
├── models/
│
├── services/
│
├── screens/
│
├── widgets/
│
└── main.dart
```

Namun jika ada struktur yang lebih baik tetapi tetap sederhana, jelaskan alasannya secara singkat sebelum digunakan.

---

## Target aplikasi

Aplikasi harus dapat melakukan CRUD terhadap:

* Pemohon
* Jenis Paspor
* Kantor Imigrasi
* Pengajuan Paspor
* Perpanjangan Paspor
* Pembayaran

Menggunakan REST API Django melalui Dio.

---

## Gaya jawaban

* Singkat.
* Jelas.
* Langsung praktik.
* Berikan kode lengkap.
* Selalu beri tahu secara spesifik file mana yang dibuat atau diedit.
* Jangan pernah berasumsi saya sudah membuat file tertentu.
* Jika perlu membuat folder, tuliskan lokasi foldernya secara jelas.
* Jika ada kode yang harus diganti, sebutkan file dan bagian mana yang diganti.
* Jangan lanjut ke langkah berikutnya sampai saya mengetik "lanjut".
