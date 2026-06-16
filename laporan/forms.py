from django import forms

from .models import LaporanHafalan


class LaporanHafalanForm(forms.ModelForm):
    class Meta:
        model = LaporanHafalan
        fields = ["santri", "periode_awal", "periode_akhir", "catatan_perkembangan"]
        widgets = {
            "periode_awal": forms.DateInput(attrs={"type": "date"}),
            "periode_akhir": forms.DateInput(attrs={"type": "date"}),
            "catatan_perkembangan": forms.Textarea(attrs={"rows": 4}),
        }

    def clean(self):
        cleaned_data = super().clean()
        periode_awal = cleaned_data.get("periode_awal")
        periode_akhir = cleaned_data.get("periode_akhir")
        if periode_awal and periode_akhir and periode_akhir < periode_awal:
            raise forms.ValidationError("Periode akhir tidak boleh lebih awal dari periode awal.")
        return cleaned_data
