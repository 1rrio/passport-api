| Urutan | Endpoint                     | Fungsi                                                                                 |
| ------ | ---------------------------- | -------------------------------------------------------------------------------------- |
| 1      | `POST /api/jenis-paspor/`    | Menambahkan data jenis paspor.                                                         |
| 2      | `POST /api/kantor-imigrasi/` | Menambahkan data kantor imigrasi.                                                      |
| 3      | `POST /api/pemohon/`         | Menambahkan data pemohon.                                                              |
| 4      | `POST /api/pengajuan/`       | Membuat pengajuan paspor dengan memilih ID pemohon, jenis paspor, dan kantor imigrasi. |
| 5      | `POST /api/perpanjangan/`    | Menambahkan data perpanjangan paspor berdasarkan data pemohon dan kantor imigrasi.     |
| 6      | `POST /api/pembayaran/`      | Menambahkan data pembayaran berdasarkan ID pengajuan paspor.                           |

+-------------------+
|   JenisPaspor     |
+-------------------+
| id (PK)           |
| kode              |
| nama              |
| masa_berlaku      |
| biaya             |
| deskripsi         |
+-------------------+
          |
          | 1
          |
          | N
+-------------------+        +----------------------+
| PengajuanPaspor   |------->|   KantorImigrasi     |
+-------------------+        +----------------------+
| id (PK)           |        | id (PK)              |
| nomor_pengajuan   |        | kode                 |
| pemohon (FK)      |        | nama                 |
| jenis_paspor (FK) |        | kota                 |
| kantor_imigrasiFK |        | alamat               |
| tanggal_pengajuan |        | telepon              |
| tujuan            |        | email                |
| status            |        +----------------------+
| jadwal            |
| catatan           |
+-------------------+
        ^
        |
        |
        |
+-------------------+
|    Pemohon        |
+-------------------+
| id (PK)           |
| nik               |
| nama_lengkap      |
| tempat_lahir      |
| tanggal_lahir     |
| jenis_kelamin     |
| alamat            |
| no_hp             |
| email             |
| pekerjaan         |
| kewarganegaraan   |
+-------------------+

        |
        |1
        |
        |N
+----------------------+
| PerpanjanganPaspor   |
+----------------------+
| id (PK)              |
| nomor_perpanjangan   |
| pemohon (FK)         |
| kantor_imigrasi(FK)  |
| nomor_paspor_lama    |
| tanggal_kadaluarsa   |
| tanggal_pengajuan    |
| alasan               |
| status               |
| jadwal_pengambilan   |
+----------------------+

PengajuanPaspor
        |
        |1
        |
        |N
+-------------------+
|   Pembayaran      |
+-------------------+
| id (PK)           |
| pengajuan (FK)    |
| kode_pembayaran   |
| metode            |
| jumlah            |
| tanggal_bayar     |
| status            |
| bukti             |
| keterangan        |
+-------------------+
