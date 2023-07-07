from django.shortcuts import render
from . import ml 
import numpy as np
import pandas as pd

# Create your views here.
def home(request):
    if request.method == 'POST':
        country = request.POST.get('country')
        education = request.POST.get('education')
        empLevel = request.POST.get('empLevel')
        exp = request.POST.get('exp')

        x = np.array([[country, education, exp, empLevel]])

        test_df = pd.DataFrame(x, columns=['Country', 'EdLevel', 'YearsCodePro', 'Employment'])

    return render(request, 'index.html')

