import os
import sys
import django
import random

from datetime import date, timedelta

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

sys.path.append(BASE_DIR)

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'config.settings'
)

django.setup()

from santri.models import Santri
from hafalan.models import SetoranHafalan


# ====================================
# DATA MASTER
# ====================================

SURAH_LIST = [
    "Al-Fatihah",
    "Al-Baqarah",
    "Ali 'Imran",
    "An-Nisa",
    "Al-Ma'idah",
    "Al-An'am",
    "Al-A'raf",
    "Al-Anfal",
    "At-Taubah",
    "Yunus",
    "Hud",
    "Yusuf",
    "Ar-Ra'd",
    "Ibrahim",
    "Al-Hijr",
]

USTADZ = [
    "Ustadz Hanan",
    "Ustadz Fikri",
    "Ustadzah Aisyah",
]

SANTRI_DATA = [

    # JUZ 1-5
    ("Ahmad Fauzi", "juz_1_5"),
    ("Muhammad Rizki", "juz_1_5"),

    # JUZ 1-10
    ("Abdul Rohman", "juz_1_10"),
    ("Aisyah Putri", "juz_1_10"),

    # JUZ 1-15
    ("Siti Zahra", "juz_1_15"),
    ("Nur Hidayah", "juz_1_15"),

    # JUZ 1-20
    ("Fajar Ramadhan", "juz_1_20"),
    ("Ilham Maulana", "juz_1_20"),

    # JUZ 1-25
    ("Nabila Putri", "juz_1_25"),
    ("Hasan Basri", "juz_1_25"),

    # JUZ 1-30
    ("Lutfi Ramadhan", "juz_1_30"),
    ("Syifa Aulia", "juz_1_30"),
]


# ====================================
# HAPUS DATA LAMA
# ====================================

SetoranHafalan.objects.all().delete()
Santri.objects.all().delete()


# ====================================
# BATAS HALAMAN TIAP KATEGORI
# ====================================

BATAS_HALAMAN = {
    "juz_1_5": 100,
    "juz_1_10": 200,
    "juz_1_15": 300,
    "juz_1_20": 400,
    "juz_1_25": 500,
    "juz_1_30": 604,
}


# ====================================
# BUAT SANTRI + SETORAN
# ====================================

for i, (nama, kategori_juz) in enumerate(SANTRI_DATA):

    santri = Santri.objects.create(

        nis=f"2026{i+1:03}",

        nama=nama,

        jenis_kelamin=random.choice([
            "L",
            "P"
        ]),

        tanggal_lahir=date(
            2008,
            random.randint(1, 12),
            random.randint(1, 28)
        ),

        ustadz_pembina=random.choice(USTADZ),

        nama_orang_tua=f"Orang Tua {nama}",

        nomor_wa_orang_tua=f"62812345{i+1000}",

        alamat="Probolinggo",

        aktif=True,
    )

    batas_halaman = BATAS_HALAMAN[kategori_juz]

    halaman_progress = 1

    for x in range(25):

        tambahan = random.randint(1, 5)

        halaman_awal = halaman_progress

        halaman_akhir = min(
            halaman_awal + tambahan,
            batas_halaman
        )

        halaman_progress = halaman_akhir

        kualitas = random.choices(
            [
                "sangat_baik",
                "baik",
                "cukup",
                "perlu_bimbingan"
            ],
            weights=[45, 35, 15, 5]
        )[0]

        SetoranHafalan.objects.create(

            santri=santri,

            tanggal=date.today() - timedelta(
                days=random.randint(1, 120)
            ),

            jenis_setoran=random.choices(
                [
                    "ziyadah",
                    "murajaah"
                ],
                weights=[75, 25]
            )[0],

            kategori_juz=kategori_juz,

            surah=random.choice(SURAH_LIST),

            halaman_awal=halaman_awal,

            halaman_akhir=halaman_akhir,

            kualitas=kualitas,

            catatan=random.choice([
                "Hafalan sangat lancar",
                "Murajaah berjalan baik",
                "Perlu peningkatan makhraj",
                "Perlu pengulangan halaman",
                "Setoran sangat baik",
            ]),
        )

print("Dummy data berhasil dibuat!")