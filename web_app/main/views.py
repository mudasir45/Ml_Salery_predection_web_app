from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

'Bachelor’s degree', 'Master’s degree', 'Less than Bachelors',
       'Post grad']