from django.shortcuts import render
from lost.forms import formlost,formfound
from lost.models import Lost, Found
def lost(request):
    form=formlost()

    if request.method=="POST":
        form=formlost(request.POST)

        if form.is_valid():
            form.save(commit=True)
    
    return render(request,"lost.html",{'form':form})



def lostitems(request):
    lostitem= Lost.objects.all();

    return render(request, 'lostitem.html',{'lostitem': lostitem})



def landing(request):

    return render(request, 'landing.html')



def found(request):
    ff= formfound()
    if request.method=="POST":
        ff=formfound(request.POST)

        if ff.is_valid():
            ff.save(commit=True)
    

    return render(request, 'found.html', {'ff':ff})



def founditems(request):
    founditem= Found.objects.all()
    return render(request, 'founditems.html',{'j':founditem})
