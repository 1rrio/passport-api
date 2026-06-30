from rest_framework import serializers
from .models import (
    Pemohon,
    JenisPaspor,
    KantorImigrasi,
    PengajuanPaspor,
    PerpanjanganPaspor,
    Pembayaran,
)


class PemohonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pemohon
        fields = "__all__"


class JenisPasporSerializer(serializers.ModelSerializer):
    class Meta:
        model = JenisPaspor
        fields = "__all__"


class KantorImigrasiSerializer(serializers.ModelSerializer):
    class Meta:
        model = KantorImigrasi
        fields = "__all__"


class PengajuanPasporSerializer(serializers.ModelSerializer):
    class Meta:
        model = PengajuanPaspor
        fields = "__all__"


class PerpanjanganPasporSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerpanjanganPaspor
        fields = "__all__"


class PembayaranSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pembayaran
        fields = "__all__"