from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "input.html")
def calc(request):
    w=request.POST['weight']
    h=request.POST['height']
    a=request.POST['age']
    g=request.POST['gender']
    goal=request.POST["goal"]
    if w.isdigit() and  h.isdigit() and  a.isdigit():
        if g=="m" or "M":
            bmr=88.362+(13.397*float(w)) + (4.799*float(h))-(5.677*float(a))
            if goal.lower()=="gain":
                bmr=bmr+1000
            elif goal.lower()=="lose":
                bmr=bmr-1000
            else:
                bmr=bmr
            
            
        else:
            bmr= 447.593+(9.247*float(w))+(3.098*float(h))-(4.330*float(a))
            if goal.lower()=="gain":
                bmr=bmr+1000
            elif goal.lower()=="lose":
                bmr=bmr-1000
            else:
                bmr=bmr
        return render(request, "result.html", {"res": bmr})
    else:
        bmr = "Oops!Only digits are allowed"
        return render(request, "result.html", {"res": bmr})
        
    
        
    
