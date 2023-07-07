from django.shortcuts import render
from .ml import load_model
import numpy as np
import pandas as pd



# Create your views here.
def home(request):
    if request.method == 'POST':
        country = request.POST.get('country')
        education = request.POST.get('education')
        empLevel = request.POST.get('empLevel')
        exp = request.POST.get('exp')

        data = load_model()

        regressor = data["model"]
        le_education = data["le_education"]
        le_country = data["le_country"]
        le_emp = data["le_emp"]
        x = np.array([[country, education, exp, empLevel]])

        df = pd.DataFrame(x, columns=['Country', 'EdLevel', 'YearsCodePro', 'Employment'])
        df['EdLevel'] = le_education.transform(df['EdLevel'])
        df['Country'] = le_country.transform(df['Country'])
        df['Employment'] = le_emp.transform(df['Employment'])
        df = df.astype(float)
        
        salary = regressor.predict(df)
        salary = f"${salary[0]:.2f}"
        context = {
            'salary':salary,
        }
        return render(request, 'index.html', context)

    return render(request, 'index.html')

