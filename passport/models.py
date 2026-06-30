from django.db import models


class Pemohon(models.Model):
    JENIS_KELAMIN = (
        ('L', 'Laki-laki'),
        ('P', 'Perempuan'),
    )

    nik = models.CharField(max_length=16, unique=True)
    nama_lengkap = models.CharField(max_length=150)
    tempat_lahir = models.CharField(max_length=100)
    tanggal_lahir = models.DateField()
    jenis_kelamin = models.CharField(max_length=1, choices=JENIS_KELAMIN)
    alamat = models.TextField()
    no_hp = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    pekerjaan = models.CharField(max_length=100)
    kewarganegaraan = models.CharField(max_length=50, default="Indonesia")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['nama_lengkap']

    def __str__(self):
        return self.nama_lengkap


class JenisPaspor(models.Model):
    kode = models.CharField(max_length=10, unique=True)
    nama = models.CharField(max_length=100)
    masa_berlaku_tahun = models.PositiveIntegerField()
    biaya = models.DecimalField(max_digits=12, decimal_places=2)
    deskripsi = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['nama']

    def __str__(self):
        return self.nama


class KantorImigrasi(models.Model):
    kode = models.CharField(max_length=10, unique=True)
    nama = models.CharField(max_length=150)
    kota = models.CharField(max_length=100)
    alamat = models.TextField()
    telepon = models.CharField(max_length=20)
    email = models.EmailField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['nama']

    def __str__(self):
        return self.nama


class PengajuanPaspor(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Diproses', 'Diproses'),
        ('Disetujui', 'Disetujui'),
        ('Ditolak', 'Ditolak'),
        ('Selesai', 'Selesai'),
    )

    nomor_pengajuan = models.CharField(max_length=20, unique=True)
    pemohon = models.ForeignKey(
        Pemohon,
        on_delete=models.CASCADE,
        related_name='pengajuan'
    )
    jenis_paspor = models.ForeignKey(
        JenisPaspor,
        on_delete=models.PROTECT,
        related_name='pengajuan'
    )
    kantor_imigrasi = models.ForeignKey(
        KantorImigrasi,
        on_delete=models.PROTECT,
        related_name='pengajuan'
    )
    tanggal_pengajuan = models.DateField()
    tujuan_pengajuan = models.CharField(max_length=150)
    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default='Pending'
    )
    jadwal_wawancara = models.DateField(null=True, blank=True)
    catatan = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-tanggal_pengajuan']

    def __str__(self):
        return self.nomor_pengajuan


class PerpanjanganPaspor(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Diproses', 'Diproses'),
        ('Disetujui', 'Disetujui'),
        ('Ditolak', 'Ditolak'),
        ('Selesai', 'Selesai'),
    )

    nomor_perpanjangan = models.CharField(max_length=20, unique=True)
    pemohon = models.ForeignKey(
        Pemohon,
        on_delete=models.CASCADE,
        related_name='perpanjangan'
    )
    kantor_imigrasi = models.ForeignKey(
        KantorImigrasi,
        on_delete=models.PROTECT,
        related_name='perpanjangan'
    )
    nomor_paspor_lama = models.CharField(max_length=20)
    tanggal_kadaluarsa = models.DateField()
    tanggal_pengajuan = models.DateField()
    alasan = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default='Pending'
    )
    jadwal_pengambilan = models.DateField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-tanggal_pengajuan']

    def __str__(self):
        return self.nomor_perpanjangan


class Pembayaran(models.Model):
    STATUS = (
        ('Belum Bayar', 'Belum Bayar'),
        ('Menunggu Verifikasi', 'Menunggu Verifikasi'),
        ('Lunas', 'Lunas'),
    )

    METODE = (
        ('Transfer Bank', 'Transfer Bank'),
        ('QRIS', 'QRIS'),
        ('Kartu Kredit', 'Kartu Kredit'),
    )

    pengajuan = models.ForeignKey(
        PengajuanPaspor,
        on_delete=models.CASCADE,
        related_name='pembayaran'
    )
    kode_pembayaran = models.CharField(max_length=20, unique=True)
    metode = models.CharField(max_length=30, choices=METODE)
    jumlah = models.DecimalField(max_digits=12, decimal_places=2)
    tanggal_bayar = models.DateField()
    status = models.CharField(
        max_length=30,
        choices=STATUS,
        default='Belum Bayar'
    )
    bukti_pembayaran = models.ImageField(
        upload_to='bukti_pembayaran/',
        blank=True,
        null=True
    )
    keterangan = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-tanggal_bayar']

    def __str__(self):
        return self.kode_pembayaran