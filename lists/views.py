from django.shortcuts import render,redirect
from django.http import HttpResponse
from lists.models import Item
from lists.models import List
# Create your views here.
def new_list(request):
    list_user = List.objects.create()
    Item.objects.create(text=request.POST['item_text'],list =list_user)
    return redirect('/lists/the-new-page/')

def view_list(request):
    items = Item.objects.all()
    return render(request,'list.html',{'items':items})

def home_page(request):
    return render(request,'home.html')

