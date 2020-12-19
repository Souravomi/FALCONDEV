from django.forms.models import model_to_dict
from django.http.response import JsonResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
from User.models import User_Login , Templ_Contact , Academic_Projects ,Business_Works,User_Updates,Templ_Technologies,Templ_Services,Templ_Contact,Updations
from Guest_User.models import Response
from datetime import datetime
from django.contrib import messages
from django.utils.timezone import now
from django.core.serializers import serialize
from django.contrib import auth
from django.contrib.auth.decorators import login_required

from django.contrib.auth import logout
from django.core.files.storage import FileSystemStorage


#-------Admin Home Page----------------------
@login_required(login_url='/Dashboard')
def Admin_Home(request):
    res = Response.objects.filter(Status='Submitted').order_by('id')
    academic = Academic_Projects.objects.filter(Status='Active').order_by('id')
    business = Business_Works.objects.filter(Status='Active').order_by('id')
    updations = Updations.objects.all()
    data = User_Login.objects.get(EMail=request.session['username'])
    return render(request,'Dashboard/Dashboard.html',{'data':data , 'res':res ,'academic':academic , 'business':business,'updations':updations})


def getByLanguage(request,lang):
    if lang =='All':
        data=  Academic_Projects.objects.all()
        data = serialize('json', data)
    else:
        data = Academic_Projects.objects.filter(Language=lang)
        data = serialize('json', data)
    return HttpResponse(data)
    
    

#-------Admin Login Page-----------------------

def Admin_Login(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        admin = auth.authenticate(username=username, password=password)
       
        # try:
        #     admin = User_Login.objects.get(EMail=username,Password=password)
        # request.session['username'] = username
        # except:
        #     admin = None
        
        if admin is not None:
            
            auth.login(request,admin)
            request.session['username'] = username
            #visit = User_Login.objects.filter(EMail=request.session['username'])
            # request.session['last_login'] = visit.last_login
            #User_Login.objects.filter(EMail=request.session['username']).update(last_login=now())
            return redirect('Admin_Home')

        else:
            messages.success(request,'Inconrrect Username/Password ! Contact Admin')
            return render(request,'Admin_Login.html')
    else:
        return render(request,'Admin_Login.html')


#-------Admin Profile Page-----------------------
@login_required(login_url='/Dashboard')
def Admin_Profile(request):
    if request.method == 'POST':
        if 'contctbtn' in request.POST:
            User_id = User_Login.objects.get(EMail=request.session['username'])
            Subject = request.POST['Sub']
            Issue = request.POST['Isu']
            Desc = request.POST['Desc']

            table = User_Updates(User_id=User_id,Subject=Subject,Issue=Issue,Desc=Desc)
            table.save()

            messages.success(request,'Response Submitted Successfully')
            return redirect('Admin_Profile')

        elif 'passbtn' in request.POST:
            username = request.session['username']
            current = request.POST['old']
            New = request.POST['psw']
            try:
                user = User_Login.objects.get(EMail=username,Password=current)
           
            except:
                user = None
        
            if user is not None :
                user.Password = New
                user.save(update_fields = ['Password'])
                return redirect('Admin_Profile')
            else:
                print('User not there')
                messages.success(request,'Your Current Password Is Incorrect! Try Again')
                data = User_Login.objects.get(EMail=request.session['username'])
                return render(request,'Dashboard/Profile.html',{'data':data})
    else:
        data = User_Login.objects.get(EMail=request.session['username'])
        return render(request,'Dashboard/Profile.html',{'data':data})


#-------Admin UI Page-----------------------

@login_required(login_url='/Dashboard')
def Admin_UI(request):
    if request.method == 'POST':
        if 'lanbtn' in request.POST:
            Language = request.POST['lan']
            Description = request.POST['desc']
            Image = request.FILES['img']
            Status = request.POST['status']
            Owner = request.session['username']

            Result = Templ_Technologies(Language=Language,Description=Description,Image=Image,
            Status=Status,Owner=Owner)
            Result.save()

            upd = Updations(Update = 'Language Added',Change=Language,Owner=request.session['username'])
            upd.save()
            
            messages.success(request,'Language Added Successfully!')
            return redirect('Admin_UI')

        elif 'mobbtn' in request.POST:
            Mob = request.POST['mob']
            TableCount = Templ_Contact.objects.count()
            if TableCount > 0:
                Table = Templ_Contact.objects.first()
                Table.Mobile = Mob
                Table.save()
                
            else:
                Templ_Contact(Mobile=Mob).save()
                

            upd = Updations(Update = 'Mobile Updated',Change=Mob,Owner=request.session['username'])
            upd.save()

            messages.success(request,'Mobile Updated Successfully!')
            return redirect('Admin_UI')

        elif 'embtn' in request.POST:
            EMail = request.POST['email']
            DataCount = Templ_Contact.objects.count()
            if DataCount > 0:
                Data= Templ_Contact.objects.first()
                Data.EMail=EMail
                Data.save()
            else:
                Templ_Contact(Mobile=Mob).save()
             
            

            upd = Updations(Update = 'E-mail Updated',Change=EMail,Owner=request.session['username'])
            upd.save()

            messages.success(request,'E-Mail Updated Successfully!')
            return redirect('Admin_UI')

    else:
        techn = Templ_Technologies.objects.all().order_by('id')
        service = Templ_Services.objects.all().order_by('id')
        data = User_Login.objects.get(EMail=request.session['username'])
        contact = Templ_Contact.objects.first()
        return render(request,'Dashboard/UI.html',{'data':data , 'techn':techn , 'service':service, 'contact':contact})





#-------Admin Updation Page-----------------------
@login_required(login_url='/Dashboard')
def Admin_Updations(request):
    data = User_Login.objects.get(EMail=request.session['username'])
    updates = Updations.objects.all()
    return render(request,'Dashboard/Updations.html',{'data':data , 'updates':updates})



#-------Admin Services Page-----------------------
@login_required(login_url='/Dashboard')
def Admin_Services(request):
    if request.method == 'POST':
        if 'academic' in request.POST:
            #print("Acdemic Button clicked")
            Name = request.POST['name']
            Type = request.POST['Type']
            Language = request.POST['Language']
            Owner = request.POST['Owner']
            Status = request.POST['Status']
            Description = request.POST['desc']
            Result = Academic_Projects(Name=Name,Type=Type,Language=Language,Owner=Owner,Status=Status,
            Description=Description)
            Result.save() #Saved

            upd = Updations(Update = 'Academic Project Added',Change=Name,Owner=request.session['username'])
            upd.save()
            messages.success(request,'Academic Project Added Successfully!')
            return redirect('Admin_Services')

        elif 'business' in request.POST:
            #Data from Business form
            #print("Business Button clicked")
            Name = request.POST['Busname']
            Type = request.POST['BusType']
            Language = request.POST['BusLanguage']
            Client_Name = request.POST['Clname']
            Client_Contact = request.POST['clmob']
            Client_Email = request.POST['clemail']
            URL = request.POST['url']
            Status = request.POST['BusStatus']
            Description = request.POST['BusDesc']
            Data = Business_Works(Name=Name,Type=Type,Language=Language,Client_Name=Client_Name,
            Client_Contact=Client_Contact,Client_Email=Client_Email,URL=URL,Status=Status,
            Description=Description)
            Data.save() #Saved
            
            upd = Updations(Update = 'Business Project Added',Change=Name,Owner=request.session['username'])
            upd.save()
            messages.success(request,'Business Project Added Successfully!')
            return redirect('Admin_Services')
    else:
        academic = Academic_Projects.objects.all().order_by('id')
        business = Business_Works.objects.all().order_by('id')
        languages = Templ_Technologies.objects.all().order_by('id')
        user = User_Login.objects.all()
        data = User_Login.objects.get(EMail=request.session['username'])
        return render(request,'Dashboard/Services.html',{'data':data , 'academic':academic , 'business':business ,'languages':languages, 'user':user})



#-------Admin Task Page-----------------------    
@login_required(login_url='/Dashboard')
def Admin_Task(request):
    if request.method == 'POST':
        if 'servicebtn' in request.POST:

            Service = request.POST['service']
            Description = request.POST['desc']
            Type = request.POST['type']
            Owner = request.session['username']
            Status = request.POST['status']
    
            Result = Templ_Services(Service=Service,Description=Description,Type=Type,Owner=Owner,
            Status=Status,)
            Result.save() #Saved

            upd = Updations(Update = 'New Service Added',Change=Service,Owner=request.session['username'])
            upd.save()
            messages.success(request,'Service Added Successfully!')
            return redirect('Admin_Task')


    else:
        userressrch = Response.objects.all()
        servsrch = Templ_Services.objects.all()
        lansearch = Templ_Technologies.objects.all()
        acasearch = Academic_Projects.objects.all()
        bussearch = Business_Works.objects.all()
        data = User_Login.objects.get(EMail=request.session['username'])
        return render(request,'Dashboard/Task.html',{'data':data,'userressrch':userressrch,'servsrch':servsrch,'lansearch':lansearch,'acasearch':acasearch,'bussearch':bussearch})

    

#-------Logout Page-----------------------

def Logout(request):
    logout(request)
    return render(request,'Dashboard/Logout.html')

