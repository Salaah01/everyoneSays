from django.shortcuts import render


def index(request):
    """Renders the index page."""
    return render(request, 'pages/index.html')
