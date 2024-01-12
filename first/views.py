from django.shortcuts import render
import logging

# Настройка логгирования
logger = logging.getLogger(__name__)


def home_view(request):
    return render(request, 'home.html')

def about_view(request):
    return render(request, 'about.html')
