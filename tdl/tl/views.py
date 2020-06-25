from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import tlItem

# Create your views here.
def tlView(request):
    all_tl_items=tlItem.objects.all()
    return render(request,'tl.html',
    {'all_items':all_tl_items})


def addtl(request):
    new_item = tlItem(content = request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/tl/')