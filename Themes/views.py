from django.shortcuts import render
from .models import Theme


def mavzu(request):
    data = Theme.objects.all()
    return render(request, 'mavzu-1.html', {'data': data})