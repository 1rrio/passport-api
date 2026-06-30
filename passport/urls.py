from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    PemohonViewSet,
    JenisPasporViewSet,
    KantorImigrasiViewSet,
    PengajuanPasporViewSet,
    PerpanjanganPasporViewSet,
    PembayaranViewSet,
)

router = DefaultRouter()

router.register(r'pemohon', PemohonViewSet)
router.register(r'jenis-paspor', JenisPasporViewSet)
router.register(r'kantor-imigrasi', KantorImigrasiViewSet)
router.register(r'pengajuan', PengajuanPasporViewSet)
router.register(r'perpanjangan', PerpanjanganPasporViewSet)
router.register(r'pembayaran', PembayaranViewSet)

urlpatterns = [
    path('', include(router.urls)),
]