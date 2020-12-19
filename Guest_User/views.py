from django.shortcuts import render,redirect
from Guest_User.models import Response
from User.models import Templ_Contact,Templ_Technologies


# Create your views here.

def Guest_Home(request):
    tech= Templ_Technologies.objects.filter(Status='Active')
    if Templ_Contact.objects.count() > 0:
        contact = Templ_Contact.objects.first()
    else:
        contact=None
       
       
    return render(request,'index.html',{
            'contact':contact,
            'Technologies':tech
                        })
    


def Contact(request):
    if request.method == 'POST':
        Name = request.POST['name']
        EMail = request.POST['email']
        Mobile = request.POST['mobile']
        Service = request.POST['service']
        Need = request.POST['need']
        Language = request.POST.get('language')
        Description = request.POST['desc']

        Data = Response(Name=Name,EMail=EMail,Mobile=Mobile,Service=Service,Need=Need,Language=Language,
        Description=Description)
        Data.save()
        return redirect('Message')
    
    language = Templ_Technologies.objects.all()
    return render(request,'Contact.html',{ 'language':language })


def Message(request):
    return render(request,'Message.html')
 