from django.shortcuts import render,redirect

# Create your views here.
def calculateBMI(weight, height):
    return weight / (height ** 2)

def index(request,id):
    if request.method == "POST":
        height = request.POST.get('height')
        weight = request.POST.get('weight')
        context = {'bmi': calculateBMI(float(height), float(weight))}
        for i,j in context.items():
            bmi_cal = j
        print(bmi_cal,'kkk')
        return redirect('/bmi/index/'+str(bmi_cal))
    return render(request, 'bmi/bmi_cal.html',locals())

def success(request,id):
    print(id)
    return render(request,'bmi/bmi_success.html',locals())

