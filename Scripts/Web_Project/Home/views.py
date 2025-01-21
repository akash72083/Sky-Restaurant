from django.shortcuts import render,HttpResponse
from Home.models import BOOK_TABLE, AboutUs, Items, Feedback, ItemList

# Create your views here.
def home(request):
    items = Items.objects.all()
    list = ItemList.objects.all()
    review = Feedback.objects.all()
    return render(request,'home.html', {'items': items,'list': list, 'review':review})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def book_table(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        number = request.POST.get('number')
        email = request.POST.get('email')
        person = request.POST.get('person')
        date = request.POST.get('date')
        if name!='' and len(number)==10 and email!=''and person!=''and date!='':
            data = BOOK_TABLE(Name=name,Number=number,Email=email,Person=person,Date=date)
            data.save()
    return render(request,'book_table.html')

def order(request):
    return render(request,'order.html')

def feedback(request):
    if request.method == 'POST':
        user_name = request.POST.get('name')
        description = request.POST.get('description')
        rating = request.POST.get('rating')
        image = request.FILES.get('image')
        if user_name!='' and description!='' and rating!='' and image!='':
            feed = Feedback(User_name=user_name,Description=description,Rating=rating,Image=image)
            feed.save()
    return render(request,'feedback.html')


