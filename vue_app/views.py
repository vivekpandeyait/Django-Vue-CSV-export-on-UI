from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import render
import pandas as pd
import json


def test_vue(request):
    return render(request, 'vue_app/test.html')


def Table(request):
    df = pd.read_csv(
        "C:/Users/OM SAI RAM/Desktop/mysite/mysite/vue_app/vivek.CSV")

    # parsing the DataFrame in json format.
    json_records = df.reset_index().to_json(orient='records')
    data = []
    data = json.loads(json_records)
    context = {'d': data}

    return render(request, 'vue_app/test.html', context)


def to(request):
   
    df = pd.read_csv(
        "C:/Users/OM SAI RAM/Desktop/mysite/mysite/vue_app/vivek.CSV")
    value = request.POST.get('data')

    df1 = df[df['OPEN'] == 1435.0]
    json_records = df1.reset_index().to_json(orient='records')
    data = []
    data = json.loads(json_records)
    context = {'n': data}
    print(value)

    return render(request, 'vue_app/filter.html', context)


def thanks(request):
    df = pd.read_csv(
        "C:/Users/OM SAI RAM/Desktop/mysite/mysite/vue_app/vivek.CSV")
    value = request.POST.get('data')

    df1 = df[df['OPEN'] == 1435.0]
    json_records = df1.reset_index().to_json(orient='records')
    data = []
    data = json.loads(json_records)
    context = {'n': data}
    print(value)
    df1.to_csv(r'C:/Users/OM SAI RAM/Desktop/mysite/mysite/vue_app/filterdata csv/filter.csv', index=False)
    return render(request, 'vue_app/thanks.html', context)