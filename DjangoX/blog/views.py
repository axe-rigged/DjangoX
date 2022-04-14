from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'blog/index.html')

#def 404_handeler(): <-- tarvetta
#def gamedemo(): <-- sitten kun unitylla pieni peli demo testiin
