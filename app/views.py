import random
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import Url_short 
import validators
from app import disutils
 
   
   
# Create your views here. 
def homeView(request):
    if request.method == 'POST':
        url = request.POST.get('url')  
        s = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()'
        shortCode = ("".join(random.sample(s,6)))  
        data = Url_short(url=url, short_url=shortCode) 
        valid = disutils.is_string_an_url(url)
        print('----',valid)
        
       
        print('--------',valid)
        shortCode = "http://127.0.0.1:8000/app/"+ shortCode
        context = {
            'data'  : shortCode,
        }
        print(context)
        if valid == True:
            data.save()
            return render(request, 'output.html', context )
        else:
           return HttpResponse('Check Your URL')
         
        #return HttpResponse(f'for {url} your short url is {shortCode}')
        
    return render(request, 'home.html')

def redirect_url(request,short_url):
    print('+++++++++++',short_url)
    obj = Url_short.objects.get(short_url = short_url)
    print("*****" + obj.url +"*****")
    link = obj.url
    print('#############################################  '+ link)
    return redirect(obj.url,permanent=True)

def outputView(request):
    return render(request, 'output.html')