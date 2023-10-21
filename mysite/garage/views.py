from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from home.models import HomePage, IndexPage

def index_page(request):
    index_page = IndexPage.objects.live().first()
    return render(request, 'garage/index_page.html', {'index_page': index_page})

@user_passes_test(lambda u: u.is_superuser)
def home_page(request):
    home_page = HomePage.objects.live().first()
    return render(request, 'garage/home_page.html', {'home_page': home_page})

