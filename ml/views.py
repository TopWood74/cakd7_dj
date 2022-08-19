from django.shortcuts import render
import joblib
import pandas as pd
import pickle

col_list = {'fare_cat' : [1,2,3,4], 'age_cat': [0,1,2,3,4], 'family': [0,1,2,3,4,5,6,7,8,9,10], 'sex_female': [0,1], 'sex_male': [0,1], 'embarked_C': [0,1], 'embarked_Q': [0,1], 'embarked_S': [0,1]}

# Create your views here.
def inputdata(request):
    context = { 'lis' : col_list}

    return render(request, 'ml/inputdata.html', context)

def result(request):
    cls = joblib.load('ml/tcl_model.pkl')

    col_li = list(col_list)
    df = pd.DataFrame(columns=col_li)

    lis = []
    if request.POST:
        for i in col_li:
            lis.append(request.POST[i])   

        df.loc[0,:] = lis
        ans = cls.predict(df)
        if ans == 0:
            ans = "Dead"
        else:
            ans = "Survived"

        context = { 'lis' : lis, 'ans': ans }
    else:
        context = {}

    return render(request, "ml/result.html", context)