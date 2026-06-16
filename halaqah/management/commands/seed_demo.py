from datetime import date

from django.core.management.base import BaseCommand

from hafalan.models import SetoranHafalan
from santri.models import Santri


class Command(BaseCommand):
    help = "Mengisi data contoh untuk demo aplikasi tahfidz."

    def handle(self, *args, **options):
        santri, _ = Santri.objects.get_or_create(
            nis="ZBT001",
            defaults={
                "nama": "Muhammad Fikri",
                "jenis_kelamin": "L",
                "tanggal_lahir": date(2012, 5, 10),
                "ustadz_pembina": "Ustadz Ahmad",
                "nama_orang_tua": "Bapak Hidayat",
                "nomor_wa_orang_tua": "6281234567890",
                "alamat": "Wilayah Zaid Bin Tsabit",
            },
        )

        SetoranHafalan.objects.get_or_create(
            santri=santri,
            tanggal=date.today(),
            jenis_setoran="ziyadah",
            surah="An-Naba",
            ayat_awal=1,
            ayat_akhir=10,
            defaults={
                "kategori_juz": "juz_1_5",
                "kualitas": "baik",
                "catatan": "Lancar, perlu penguatan tajwid pada beberapa ayat.",
            },
        )

        self.stdout.write(self.style.SUCCESS("Data demo berhasil dibuat."))
