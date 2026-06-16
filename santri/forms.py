from django import forms

from .models import Santri


class SantriForm(forms.ModelForm):
    class Meta:
        model = Santri
        fields = [
            "nama",
            "nis",
            "jenis_kelamin",
            "tanggal_lahir",
            "ustadz_pembina",
            "nama_orang_tua",
            "nomor_wa_orang_tua",
            "alamat",
            "aktif",
        ]
        widgets = {
            "tanggal_lahir": forms.DateInput(format='%d/%m/%Y',attrs={"type": "date"}),
            "alamat": forms.Textarea(attrs={"rows": 3}),
        }
