from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
    return HttpResponse('Halaman Utama Perpustakaan')

def buku(request):
    judul = ["Belajar Django", "Belajar Pyton", "Belajar Bootstrap"]
    penulis = "Jokay Peday"

    konteks = {
        'title' : judul,
        'penulis' : penulis,
    }
    return render(request, 'buku.html', konteks)

def penerbit(request):
    return HttpResponse('Halaman Penerbit')