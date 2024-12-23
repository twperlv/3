from django.shortcuts import render

def hello(request):
    return render(request, "ti_rtu_lv.html")
