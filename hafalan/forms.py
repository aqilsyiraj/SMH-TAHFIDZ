from django import forms

from .models import SetoranHafalan


SURAH_CHOICES = [(s, s) for s in ['Al-Fatihah', 'Al-Baqarah', "Ali 'Imran", 'An-Nisa', "Al-Ma'idah", "Al-An'am", "Al-A'raf", 'Al-Anfal', 'At-Taubah', 'Yunus', 'Hud', 'Yusuf', "Ar-Ra'd", 'Ibrahim', 'Al-Hijr', 'An-Nahl', 'Al-Isra', 'Al-Kahf', 'Maryam', 'Ta-Ha', 'Al-Anbiya', 'Al-Hajj', "Al-Mu'minun", 'An-Nur', 'Al-Furqan', "Asy-Syu'ara", 'An-Naml', 'Al-Qasas', "Al-'Ankabut", 'Ar-Rum', 'Luqman', 'As-Sajdah', 'Al-Ahzab', 'Saba', 'Fatir', 'Yasin', 'As-Saffat', 'Sad', 'Az-Zumar', 'Ghafir', 'Fussilat', 'Asy-Syura', 'Az-Zukhruf', 'Ad-Dukhan', 'Al-Jasiyah', 'Al-Ahqaf', 'Muhammad', 'Al-Fath', 'Al-Hujurat', 'Qaf', 'Az-Zariyat', 'At-Tur', 'An-Najm', 'Al-Qamar', 'Ar-Rahman', "Al-Waqi'ah", 'Al-Hadid', 'Al-Mujadilah', 'Al-Hasyr', 'Al-Mumtahanah', 'As-Saff', "Al-Jumu'ah", 'Al-Munafiqun', 'At-Tagabun', 'At-Talaq', 'At-Tahrim', 'Al-Mulk', 'Al-Qalam', 'Al-Haqqah', "Al-Ma'arij", 'Nuh', 'Al-Jinn', 'Al-Muzzammil', 'Al-Muddassir', 'Al-Qiyamah', 'Al-Insan', 'Al-Mursalat', 'An-Naba', "An-Nazi'at", "'Abasa", 'At-Takwir', 'Al-Infitar', 'Al-Mutaffifin', 'Al-Insyiqaq', 'Al-Buruj', 'At-Tariq', "Al-A'la", 'Al-Gasyiyah', 'Al-Fajr', 'Al-Balad', 'Asy-Syams', 'Al-Lail', 'Ad-Duha', 'Asy-Syarh', 'At-Tin', "Al-'Alaq", 'Al-Qadr', 'Al-Bayyinah', 'Az-Zalzalah', "Al-'Adiyat", "Al-Qari'ah", 'At-Takasur', "Al-'Asr", 'Al-Humazah', 'Al-Fil', 'Quraisy', "Al-Ma'un", 'Al-Kausar', 'Al-Kafirun', 'An-Nasr', 'Al-Lahab', 'Al-Ikhlas', 'Al-Falaq', 'An-Nas']]

class SetoranHafalanForm(forms.ModelForm):
    class Meta:
        model = SetoranHafalan
        fields = [
            "santri",
            "tanggal",
            "jenis_setoran",
            "kategori_juz",
            "surah",
            "halaman_awal", 
            "halaman_akhir",
            "kualitas",
            "catatan",
        ]
        widgets = {
            "tanggal": forms.DateInput(attrs={"type": "date"}),
            "catatan": forms.Textarea(attrs={"rows": 3}),
            "surah": forms.Select(choices=SURAH_CHOICES),
        }

    def clean(self):
        cleaned_data = super().clean()
        halaman_awal = cleaned_data.get("halaman_awal") 
        halaman_akhir = cleaned_data.get("halaman_akhir") 
        if ( 
            halaman_awal and 
            halaman_akhir and 
            halaman_akhir < halaman_awal 
            ): 
            raise forms.ValidationError(
                 "Halaman akhir tidak boleh lebih kecil dari halaman awal." 
                 )
        return cleaned_data
