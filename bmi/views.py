from django.shortcuts import render

# Create your views here.
def calculateBMI(weight, height):
    return weight / (height ** 2)

def index(request):
    context = {'bmi': calculateBMI(65,1.5)}
    return render(request, 'bmi/bmi_cal.html' , context)