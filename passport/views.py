from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import (
    Pemohon,
    JenisPaspor,
    KantorImigrasi,
    PengajuanPaspor,
    PerpanjanganPaspor,
    Pembayaran,
)

from .serializers import (
    PemohonSerializer,
    JenisPasporSerializer,
    KantorImigrasiSerializer,
    PengajuanPasporSerializer,
    PerpanjanganPasporSerializer,
    PembayaranSerializer,
)


class PemohonViewSet(viewsets.ModelViewSet):
    queryset = Pemohon.objects.all()
    serializer_class = PemohonSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["nik", "nama_lengkap", "email"]
    ordering_fields = "__all__"


class JenisPasporViewSet(viewsets.ModelViewSet):
    queryset = JenisPaspor.objects.all()
    serializer_class = JenisPasporSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["kode", "nama"]
    ordering_fields = "__all__"


class KantorImigrasiViewSet(viewsets.ModelViewSet):
    queryset = KantorImigrasi.objects.all()
    serializer_class = KantorImigrasiSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["kode", "nama", "kota"]
    ordering_fields = "__all__"


class PengajuanPasporViewSet(viewsets.ModelViewSet):
    queryset = PengajuanPaspor.objects.all()
    serializer_class = PengajuanPasporSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["nomor_pengajuan", "tujuan_pengajuan"]
    ordering_fields = "__all__"


class PerpanjanganPasporViewSet(viewsets.ModelViewSet):
    queryset = PerpanjanganPaspor.objects.all()
    serializer_class = PerpanjanganPasporSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["nomor_perpanjangan", "nomor_paspor_lama"]
    ordering_fields = "__all__"


class PembayaranViewSet(viewsets.ModelViewSet):
    queryset = Pembayaran.objects.all()
    serializer_class = PembayaranSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["kode_pembayaran"]
    ordering_fields = "__all__"