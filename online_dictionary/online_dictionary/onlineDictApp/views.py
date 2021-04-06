from django.shortcuts import render
from .models import onlineDictionary
from .forms import DictionaryForm
# Create your views here.
def home(request):
    if request.method == 'POST':
        form = DictionaryForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = onlineDictionary.objects.all()
            return render(request,'index.html',{'all_items':all_items})

    else:
        all_items = onlineDictionary.objects.all()
        return render(request,'index.html',{'all_items':all_items})



def posts(request,pk_test):
    letter = onlineDictionary.objects.get(id=pk_test)
    return render(request,'index.html',{'letter':letter})

