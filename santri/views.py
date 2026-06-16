from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import SantriForm
from .models import Santri
from django.contrib.auth.decorators import login_required 
from accounts.decorators import admin_required

@login_required
@admin_required
def student_list(request):
    query = request.GET.get("q", "")
    santri = Santri.objects.all()
    if query:
        santri = santri.filter(nama__icontains=query)
    return render(request, "santri/student_list.html", {"santri": santri, "query": query})

@login_required
@admin_required
def student_create(request):
    if request.method == "POST":
        form = SantriForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Data santri berhasil ditambahkan.")
            return redirect("santri:list")
    else:
        form = SantriForm()
    return render(request, "santri/student_form.html", {"form": form})
@login_required
@admin_required
def student_update(request, pk):

    santri = Santri.objects.get(pk=pk)

    if request.method == "POST":
        form = SantriForm(request.POST, instance=santri)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Data santri berhasil diperbarui."
            )

            return redirect("santri:list")

    else:
        form = SantriForm(instance=santri)

    return render(
        request,
        "santri/student_form.html",
        {
            "form": form,
            "edit_mode": True
        }
    )
@login_required
@admin_required
def student_delete(request, pk):

    santri = Santri.objects.get(pk=pk)

    if request.method == "POST":

        santri.delete()

        messages.success(
            request,
            "Data santri berhasil dihapus."
        )

        return redirect("santri:list")

    return render(
        request,
        "santri/student_confirm_delete.html",
        {
            "santri": santri
        }
    )