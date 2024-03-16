from django.shortcuts import render
from .models import Pupil

def pupil(request):
    data = Pupil.objects.all()
    return render(request, 'student.html', {'data': data})
