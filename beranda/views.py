from datetime import timedelta

from django.db.models import Count
from django.shortcuts import render
from django.utils import timezone

from hafalan.models import SetoranHafalan
from laporan.models import LaporanHafalan
from santri.models import Santri
from whatsapp_gateway.models import WhatsAppLog
from django.contrib.auth.decorators import login_required 

@login_required
def index(request):
    today = timezone.localdate()
    start_date = today - timedelta(days=6)
    jumlah_santri = Santri.objects.filter(aktif=True).count()
    pembagi_santri = max(jumlah_santri, 1)

    setoran_per_tanggal = {
        row["tanggal"]: row["total"]
        for row in SetoranHafalan.objects.filter(tanggal__range=(start_date, today))
        .values("tanggal")
        .annotate(total=Count("id"))
    }

    grafik_rata_rata_setoran = []
    for day_offset in range(30):
        tanggal = start_date + timedelta(days=day_offset)
        total = setoran_per_tanggal.get(tanggal, 0)
        rata_rata = total / pembagi_santri
        grafik_rata_rata_setoran.append(
            {
                "label": tanggal.strftime("%d/%m"),
                "total": total,
                "rata_rata": round(rata_rata, 2),
                "height": max(min(rata_rata * 100, 100), 6) if total else 4,
            }
        )

    context = {
        "jumlah_santri": jumlah_santri,
        "jumlah_setoran": SetoranHafalan.objects.count(),
        "jumlah_laporan": LaporanHafalan.objects.count(),
        "jumlah_pesan": WhatsAppLog.objects.count(),
        "setoran_terbaru": SetoranHafalan.objects.select_related("santri")[:8],
        "laporan_terbaru": LaporanHafalan.objects.select_related("santri")[:5],
        "grafik_rata_rata_setoran": grafik_rata_rata_setoran,
    }
    return render(request, "beranda/index.html", context)

# Create your views here.
