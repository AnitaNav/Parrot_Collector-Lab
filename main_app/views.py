from django.shortcuts import render

parrots = [
    {'name': 'Mojo', 'species': 'Blue Macaw', 'description': 'grumpy guy', 'age': 12},
    {'name': 'Einstein', 'species': 'Grey', 'description': 'smart fellow', 'age': 15},
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def parrots_index(request):
    return render(request, 'parrots/index.html', {
        'parrots': parrots
    })