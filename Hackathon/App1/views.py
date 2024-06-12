from django.shortcuts import render

# Create your views here.
def IndexView(request):
    """Página de inicio"""
    return render(request, "index.html")