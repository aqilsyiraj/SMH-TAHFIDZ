from decimal import Decimal

from hafalan.models import SetoranHafalan
from .models import LaporanHafalan
from collections import defaultdict


def build_laporan_hafalan(santri, periode_awal, periode_akhir, catatan_perkembangan=""):
    setoran = SetoranHafalan.objects.filter(
        santri=santri,
        tanggal__range=(periode_awal, periode_akhir),
    ).order_by("-tanggal", "-created_at")

    total_setoran = setoran.count()
    jumlah_hari = max((periode_akhir - periode_awal).days + 1, 1)
    rata_rata_setoran_harian = total_setoran / jumlah_hari
    hafalan_terakhir = setoran.first()

    laporan = LaporanHafalan.objects.create(
        santri=santri,
        periode_awal=periode_awal,
        periode_akhir=periode_akhir,
        total_setoran=total_setoran,
        rata_rata_setoran_harian=Decimal(str(round(rata_rata_setoran_harian, 2))),
        hafalan_terakhir=( hafalan_terakhir.rentang_halaman if hafalan_terakhir else "-" ),
        kategori_juz_terakhir=hafalan_terakhir.get_kategori_juz_display() if hafalan_terakhir else "-",
        catatan_perkembangan=catatan_perkembangan,
    )
    return laporan

def build_progress_chart(
    santri,
    periode_awal=None,
    periode_akhir=None
):

    setoran = SetoranHafalan.objects.filter(
        santri=santri
    ).order_by("tanggal")

    if periode_awal and periode_akhir:

        setoran = setoran.filter(
            tanggal__range=(
                periode_awal,
                periode_akhir
            )
        )

    grouped = defaultdict(list)

    for item in setoran:

        grouped[item.tanggal].append(item)

    points = []

    for tanggal, items in grouped.items():

        jumlah_setoran = min(len(items), 5)

        last_item = items[-1]

        points.append({

            "tanggal": tanggal,

            "label": jumlah_setoran,

            "value": jumlah_setoran,

            "surah": last_item.surah,

            "halaman":
                f"{last_item.halaman_awal}-"
                f"{last_item.halaman_akhir}",

            "kualitas":
                last_item.get_kualitas_display(),
        })

    points.sort(key=lambda x: x["tanggal"])

    if len(points) < 2:

        status = "Data belum cukup"

    elif points[-1]["value"] > points[0]["value"]:

        status = "Setoran meningkat"

    elif points[-1]["value"] < points[0]["value"]:

        status = "Setoran menurun"

    else:

        status = "Setoran stabil"

    return points, status

def render_pesan_laporan(laporan):
    catatan = laporan.catatan_perkembangan or "Belum ada catatan tambahan."
    return (
        f"Assalamu'alaikum Bapak/Ibu {laporan.santri.nama_orang_tua}.\n\n"
        f"Berikut laporan hafalan ananda {laporan.santri.nama}:\n"
        f"Periode: {laporan.periode_awal} s.d. {laporan.periode_akhir}\n"
        f"Total setoran: {laporan.total_setoran}\n"
        f"Hafalan terakhir: {laporan.hafalan_terakhir}\n"
        f"Kategori juz: {laporan.kategori_juz_terakhir}\n"
        f"Rata-rata setoran harian: {laporan.rata_rata_setoran_harian}\n"
        f"Catatan: {catatan}\n\n"
        "Semoga ananda semakin istiqamah dalam menghafal Al-Qur'an.\n\n"
        "- Daerah Tahfidzul Qur'an Wilayah Zaid Bin Tsabit"
    )
