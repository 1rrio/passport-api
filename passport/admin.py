from django.contrib import admin
from .models import (
    Pemohon,
    JenisPaspor,
    KantorImigrasi,
    PengajuanPaspor,
    PerpanjanganPaspor,
    Pembayaran,
)


@admin.register(Pemohon)
class PemohonAdmin(admin.ModelAdmin):
    list_display = (
        "nik",
        "nama_lengkap",
        "jenis_kelamin",
        "no_hp",
        "email",
        "kewarganegaraan",
    )
    search_fields = ("nik", "nama_lengkap", "email")
    list_filter = ("jenis_kelamin", "kewarganegaraan")


@admin.register(JenisPaspor)
class JenisPasporAdmin(admin.ModelAdmin):
    list_display = (
        "kode",
        "nama",
        "masa_berlaku_tahun",
        "biaya",
    )
    search_fields = ("kode", "nama")


@admin.register(KantorImigrasi)
class KantorImigrasiAdmin(admin.ModelAdmin):
    list_display = (
        "kode",
        "nama",
        "kota",
        "telepon",
    )
    search_fields = ("kode", "nama", "kota")
    list_filter = ("kota",)


@admin.register(PengajuanPaspor)
class PengajuanPasporAdmin(admin.ModelAdmin):
    list_display = (
        "nomor_pengajuan",
        "pemohon",
        "jenis_paspor",
        "status",
        "tanggal_pengajuan",
    )
    search_fields = (
        "nomor_pengajuan",
        "pemohon__nama_lengkap",
    )
    list_filter = (
        "status",
        "jenis_paspor",
        "kantor_imigrasi",
    )


@admin.register(PerpanjanganPaspor)
class PerpanjanganPasporAdmin(admin.ModelAdmin):
    list_display = (
        "nomor_perpanjangan",
        "pemohon",
        "status",
        "tanggal_pengajuan",
    )
    search_fields = (
        "nomor_perpanjangan",
        "pemohon__nama_lengkap",
    )
    list_filter = (
        "status",
        "kantor_imigrasi",
    )


@admin.register(Pembayaran)
class PembayaranAdmin(admin.ModelAdmin):
    list_display = (
        "kode_pembayaran",
        "pengajuan",
        "jumlah",
        "status",
        "tanggal_bayar",
    )
    search_fields = ("kode_pembayaran",)
    list_filter = ("status", "metode")