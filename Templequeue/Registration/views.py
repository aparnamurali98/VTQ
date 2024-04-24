from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from .devoteereg_form import devo_form
from .enquiry_form import enquiry_form
from .models import devotee_model, role_model, enquiry_model
from Adminhome.models import location_model

from Adminhome.models import staff_model


# Create your views here.
def home (request):
    return HttpResponse("<a href='insert_devotee'>Sign Up</a>"
                        "<br><br><a href='insert_enquiry'>Enquriy management</a>"
                        "<br><br><a href='login'>Login</a>")
def insert_devotee(request):
    context={}
    frm= devo_form(request.POST or None,request.FILES or None)
    if request.POST:
        try:
            devname=request.POST.get('dname')
            addre=request.POST.get('address')
            devage=request.POST.get('age')
            devgender=request.POST.get('gender')
            File1 = request.FILES['photo']
            devphoto=File1.name
            devstar = request.POST.get('star')
            devemail = request.POST.get('email')
            devmobile = request.POST.get('mobile')
            devusername  = request.POST.get('username')
            devupassword = request.POST.get('password')
            devuconfirm_password = request.POST.get('confirm_password')
            if devuconfirm_password==devupassword:

                if frm.is_valid():

                    devloc = frm.cleaned_data['loc']
                    locid = location_model.objects.get(locname=devloc)
                    loginid=User.objects.create_user(username=devusername,password=devupassword)
                    role=role_model.objects.create(login=loginid,roletype=2)
                    devoteereg=devotee_model.objects.create(dname=devname,address=addre,age=devage,gender=devgender,photo=devphoto,star=devstar,email=devemail,mobile=devmobile,loc=locid,login=loginid)
                    return HttpResponseRedirect('/login')
            else:
                messages.error(request,"password does not match")
        except Exception as ex:
            # error_message="User Name Alredy Exists"
            error_message = ex

            messages.error(request,error_message)


    context['f']=frm
    return render(request,"adddevo.html",context)
def insert_enquiry(request):
    context={}
    frm=enquiry_form(request.POST or None)
    enquiry = request.POST.get('Name')
    if enquiry_model.objects.filter(Name=enquiry).exists():
        messages.info(request, 'This Enquiry Already Exists')
        return redirect('/login/insert_enquiry')
    else:

        if frm.is_valid():
            frm.save()
            return redirect('/login/insert_enquiry')

    context['f'] = frm
    return render(request,"addenquiry.html",context)

def login(request):
    if request.POST:
        context={}
        Uname=request.POST.get('username')
        paswrd=request.POST.get('password')
        user=authenticate(username=Uname,password=paswrd)
        if user is not None:
            user_id=user.id
            sp=user.is_superuser
            if sp is True:
                return HttpResponseRedirect('/Adhome')
            roll_obj=role_model.objects.filter(login=user_id)
            for role_obj in roll_obj:
                type=role_obj.roletype
                print(type)

                if type=='2':

                    devote_object=devotee_model.objects.filter(login=user_id)
                    for obj in devote_object:
                        request.session["devote_id"]=obj.id
                        request.session["devote_name"]=obj.dname
                        print(obj.id)
                        print(obj.dname)
                        return HttpResponseRedirect('/Devotee')
                elif type=='3':
                    staff_object = staff_model.objects.filter(login=user_id)
                    for obj in staff_object:
                        request.session["staff_id"] = obj.id
                        request.session["staff_name"] = obj.sname
                        print(obj.id)
                        print(obj.sname)
                        return HttpResponseRedirect('/staff_home')
                    else:
                        return HttpResponse(
                            "<script>alert('Invalid Credential !!!');window.location='/login';</script>")

        else:
            return HttpResponse("<script>alert('Invalid Credential !!!');window.location='/login';</script>")
    return render(request, "login.html")


