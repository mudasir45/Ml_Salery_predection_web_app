from django.shortcuts import render
import model.ml

# Create your views here.
def home(request):
    if request.method == 'POST':
        country = request.POST.get('country')
        education = request.POST.get('education')
        empLevel = request.POST.get('empLevel')
        exp = request.POST.get('exp')

        

    return render(request, 'index.html')

