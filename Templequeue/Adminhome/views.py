from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

from .careers_form import careers_form
from .darshan_form import darsh_form
from .day_form import day_form
from .district_form import dist_form

from .expensetype_form import expense_form
from .incometype_form import income_form
from .location_form import loca_form
from .models import distric_model, priest_model, templeinfo_model, location_model, staff_model, \
    pooja_model, month_model, day_model, transtype_model, income_model, expense_model, poojaschedule_model, \
    specialday_model, careers_model, darshan_model, poojatype_model
from .month_form import month_form
from .poojaschedule_form import schedule_form
from .poojatype_form import pooja_form
from .poojatypecategory_form import poojatype_form
from .priest_form import prie_form
from .specialday_form import specialday_form
from .staff_form import staf_form
from .templeinfo_form import temple_form
from .transfertype_form import transf_form
from Registration.models import enquiry_model

from Registration.models import role_model

from Registration.enquiry_form import enquiry_form

from Devotee.models import application_model


# Create your views here.
def home (request):
    return HttpResponse("<a href='insert_district'>District</a>"
                        "<br><br><a href='insert_location'>Location</a>"
                        "<br><br><a href='insert_staff'> staff</a>"
                        "<br><br><a href='insert_templeinfo'>Temple info</a>"
                        "<br><br><a href='insert_priest'>Hindu Priest</a>"
                       
                        "<br><br><a href='insert_pooja'>Poojatype</a>"
                        "<br><br><a href='insert_day'>Day</a>"
                        "<br><br><a href='insert_transf'>transfermode</a>"
                        "<br><br><a href='insert_income'>income</a>"
                        "<br><br><a href='insert_month'>month</a>"
                        "<br><br><a href='insert_expense'>expense</a>"
                        "<br><br><a href='insert_schedule'>schedule</a>"
                        "<br><br><a href='insert_special'>special</a>"
                        "<br><br><a href='insert_careers'>Careers</a>"
                        "<br><br><a href='insert_darshan'>Darshana timming</a>"
                        "<br><br><a href='view_enquiry'> view enquiry</a>"
                        "<br><br><a href='view_application'> view Applications</a>"
                        "<br><br><a href='insert_poojatype'>Pooja Type </a>"


                        )

def insert_district(request):
    context={}
    frm= dist_form(request.POST or None)
    dist=request.POST.get('distname')
    if distric_model.objects.filter(distname=dist).exists():
        messages.info(request,'District Already Exists')
        return redirect('/Adhome/insert_district')
    else:

        if frm.is_valid():
            frm.save()
            return redirect('/Adhome/insert_district')

    context['f']=frm
    context['distric_list'] = distric_model.objects.all()
    return render(request,"adddist.html",context)
# display distric details
def show_district(request):
    context = {}
    context['distric_list'] = distric_model.objects
    return render(request, "adddist.html", context)
#update district
def update_district(request,did):
    context={}
    obj=get_object_or_404(distric_model,id=did)
    frm = dist_form(request.POST or None,instance=obj)
    if frm.is_valid():
        frm.save()
        return HttpResponseRedirect("/Adhome/insert_district")
    context['dis_data'] = frm
    return render(request, "updatedistrict.html", context)
#delete district
def delete_district(request,did):
    context={}
    obj = get_object_or_404(distric_model, id=did)
    obj.delete()
    return HttpResponseRedirect("/Adhome/insert_district")
def insert_location(request):
    context={}
    frm= loca_form(request.POST or None)
    loca = request.POST.get('locname')
    if location_model.objects.filter(locname=loca).exists():
        messages.info(request, 'Location Name Already Exists')
        return redirect('/Adhome/insert_location')
    else:
        if frm.is_valid():
            frm.save()
            return redirect('/Adhome/insert_location')
    context['f']=frm
    context['location_list'] = location_model.objects.all()
    return render(request,"addloc.html",context)
#display location details
def show_location(request):
    context = {}
    context['location_list'] = location_model.objects.all()
    return render(request, "addloc.html", context)
#update location
def update_location(request,lid):
    context={}
    obj=get_object_or_404(location_model,id=lid)
    frm = loca_form(request.POST or None,instance=obj)
    if frm.is_valid():
        frm.save()
        return HttpResponseRedirect("/Adhome/insert_location")
    context['loc_data'] = frm
    return render(request, "updateloca.html", context)
#delete district
def delete_location(request,lid):
    context={}
    obj = get_object_or_404(location_model, id=lid)
    obj.delete()
    return HttpResponseRedirect("/Adhome/insert_location")
def insert_staff(request):
    context={}
    frm= staf_form(request.POST or None,request.FILES or None)
    if request.POST:
        try:
            staffname = request.POST.get('sname')
            saddress = request.POST.get('address')
            semail = request.POST.get('email')
            smobile = request.POST.get('mobile')
            File1 = request.FILES['photo']
            sphoto=File1.name
            dob = request.POST.get('dob')
            sage = request.POST.get('age')
            gender = request.POST.get('gender')
            staffusername = request.POST.get('username')
            staffpassword = request.POST.get('password')
            staffconfirm_password = request.POST.get('confirm_password')
            if staffconfirm_password == staffpassword:
                if frm.is_valid():
                    loginid=User.objects.create_user(username=staffusername,password=staffpassword)
                    role = role_model.objects.create(login=loginid, roletype=3)
                    staffreg=staff_model.objects.create(sname=staffname,address=saddress,email=semail,mobile=smobile,photo=sphoto,dob=dob,age=sage,gender=gender,login=loginid)
                    return HttpResponseRedirect('/Adhome')
            else:
                messages.error(request,"password does not match")
        except Exception as ex:
            error_message="User Name Alredy Exists"

            messages.error(request,error_message)

    context['f']=frm
    context['staff_list'] = staff_model.objects.all()
    return render(request,"addstaff.html",context)

# display staff details
def show_staff(request):
    context = {}
    context['staff_list'] = staff_model.objects.all()
    return render(request, "addstaff.html", context)
#update district

#delete district
def delete_staff(request,sid):
    context={}
    obj = get_object_or_404(staff_model, id=sid)
    obj.delete()
    return HttpResponseRedirect("/Adhome/insert_staff")
def insert_templeinfo(request):
    context={}
    frm=temple_form(request.POST or None,request.FILES)
    temple = request.POST.get('tname')
    if templeinfo_model.objects.filter(tname=temple).exists():
        messages.info(request, 'Temple Name Already Exists')
        return redirect('/Adhome/insert_templeinfo')
    else:
        if frm.is_valid():
            frm.save()
            return redirect('/Adhome/insert_templeinfo')
    context['f'] = frm
    context['info_list'] = templeinfo_model.objects.all()

    return render(request,"addtemp.html",context)
#display temple info details
def show_templeinfo(request):
    context = {}
    context['info_list'] = templeinfo_model.objects.all()
    return render(request, "addtemp.html", context)
#update district
def update_templeinfo(request,tid):
    context={}
    obj=get_object_or_404(templeinfo_model,id=tid)
    frm = temple_form(request.POST or None,request.FILES or None ,instance=obj)
    if frm.is_valid():
        frm.save()
        return HttpResponseRedirect("/Adhome/insert_templeinfo")
    context['info_data'] = frm
    return render(request, "updatetemple.html", context)
#delete district
def delete_templeinfo(request,tid):
    context={}
    obj = get_object_or_404(templeinfo_model, id=tid)
    obj.delete()
    return HttpResponseRedirect("/Adhome/insert_templeinfo")

def insert_priest(request):
    context={}
    frm= prie_form(request.POST or None)
    priest= request.POST.get('Pname')
    phoneno= request.POST.get('Phone')
    if priest_model.objects.filter(Pname=priest,Phone=phoneno).exists():
        messages.info(request, 'Priest  Already Exists')
        return redirect('/Adhome/insert_priest')
    else:
        if frm.is_valid():
            frm.save()
            return redirect('/Adhome/insert_priest')

        context['f'] = frm
        context['priest_list'] = priest_model.objects.all()
        return render(request, "addprie.html", context)
#display priest details
def show_priest(request):
    context = {}
    context['priest_list'] = priest_model.objects.all()
    return render(request, "addprie.html", context)
#update district
def update_priest(request,pid):
    context={}
    obj=get_object_or_404(priest_model,id=pid)
    frm = prie_form(request.POST or None,instance=obj)
    if frm.is_valid():
        frm.save()
        return HttpResponseRedirect("/Adhome/insert_priest")
    context['priest_data'] = frm
    return render(request, "updatepriest.html", context)
#delete district
def delete_priest(request,pid):
    context={}
    obj = get_object_or_404(priest_model, id=pid)
    obj.delete()
    return HttpResponseRedirect("/Adhome/insert_priest")

def insert_pooja(request):
    context={}
    frm= pooja_form(request.POST or None,request.FILES)
    pooja=request.POST.get('poojatypeid')
    if pooja_model.objects.filter(poojatypeid=pooja).exists():
        messages.info(request, 'Pooja Type Id Already Exists')
        return redirect('/Adhome/insert_pooja')
    else:
        if frm.is_valid():
            frm.save()
            return redirect('/Adhome/insert_pooja')
    context['f']=frm
    context['pooja_list'] = pooja_model.objects.all()
    return render(request,"addpooja.html",context)
#display priest details
def show_pooja(request):
    context = {}
    context['pooja_list'] = pooja_model.objects.all()
    return render(request, "addpooja.html", context)
#update district
def update_pooja(request,pid):
    context={}
    obj=get_object_or_404(pooja_model,id=pid)
    frm = pooja_form(request.POST or None,instance=obj)
    if frm.is_valid():
        frm.save()
        return HttpResponseRedirect("/Adhome/insert_pooja")
    context['pooja_data'] = frm
    return render(request, "updatepooja.html", context)
#delete district
def delete_pooja(request,pid):
    context={}
    obj = get_object_or_404(pooja_model, id=pid)
    obj.delete()
    return HttpResponseRedirect("/Adhome/insert_pooja")
def insert_day(request):
    context={}
    frm = day_form(request.POST or None)
    day = request.POST.get('day')
    if day_model.objects.filter(day=day).exists():
        messages.info(request, 'This Day Already Exists')
        return redirect('/Adhome/insert_day')
    else:

        if frm.is_valid():
            frm.save()
            return redirect('/Adhome/insert_day')
    context['f']=frm
    context['day_list'] = day_model.objects.all()

    return render(request,"addday.html",context)
def show_day(request):
    context = {}
    context['day_list'] = day_model.objects.all()
    return render(request, "addday.html", context)
#update district
def update_day(request,did):
    context={}
    obj=get_object_or_404(day_model,id=did)
    frm = day_form(request.POST or None,instance=obj)
    if frm.is_valid():
        frm.save()
        return HttpResponseRedirect("/Adhome/insert_day")
    context['day_data'] = frm
    return render(request, "updateday.html", context)
#delete district
def delete_day(request,did):
    context={}
    obj = get_object_or_404(day_model, id=did)
    obj.delete()
    return HttpResponseRedirect("/Adhome/insert_day")
def insert_transf(request):
    context={}
    frm=transf_form(request.POST or None)
    trans = request.POST.get('transmode')
    if transtype_model.objects.filter(transmode=trans).exists():
        messages.info(request, 'This Transation Mode Already Exists')
        return redirect('/Adhome/insert_transf')
    else:

        if frm.is_valid():
            frm.save()
            return redirect('/Adhome/insert_transf')
    context['f']=frm
    context['trans_list'] = transtype_model.objects.all()
    return render(request,"addtrans.html",context)
def show_transf(request):
    context = {}
    context['trans_list'] = transtype_model.objects.all()
    return render(request, "addtrans.html", context)
#update district
def update_trans(request,tid):
    context={}
    obj=get_object_or_404(transtype_model,id=tid)
    frm = transf_form(request.POST or None,instance=obj)
    if frm.is_valid():
        frm.save()
        return HttpResponseRedirect("/Adhome/insert_transf")
    context['trans_data'] = frm
    return render(request, "updatetrans.html", context)
#delete district
def delete_trans(request,tid):
    context={}
    obj = get_object_or_404(transtype_model, id=tid)
    obj.delete()
    return HttpResponseRedirect("/Adhome/insert_transf")
def insert_income(request):
    context={}
    frm=income_form(request.POST or None)
    income = request.POST.get('inctype')
    if income_model.objects.filter(inctype=income).exists():
        messages.info(request, 'Income Already Exists')
        return redirect('/Adhome/insert_income')
    else:

        if frm.is_valid():
            frm.save()
            return redirect('/Adhome/insert_income')
    context['f']=frm
    context['income_list'] = income_model.objects.all()
    return render(request,"addincome.html",context)
def show_income(request):
    context = {}
    context['income_list'] = income_model.objects.all()
    return render(request, "addincome.html", context)
#update district
def update_income(request,iid):
    context={}
    obj=get_object_or_404(income_model,id=iid)
    frm = income_form(request.POST or None,instance=obj)
    if frm.is_valid():
        frm.save()
        return HttpResponseRedirect("/Adhome/insert_income")
    context['income_data'] = frm
    return render(request, "updateincome.html", context)
#delete district
def delete_income(request,iid):
    context={}
    obj = get_object_or_404(income_model, id=iid)
    obj.delete()
    return HttpResponseRedirect("/Adhome/insert_income")


def insert_month(request):
    context={}
    frm=month_form(request.POST or None)
    mont = request.POST.get('Month')
    if month_model.objects.filter(Month=mont).exists():
        messages.info(request, 'Month Already Exists')
        return redirect('/Adhome/insert_month')
    else:

        if frm.is_valid():
            frm.save()
            return redirect('/Adhome/insert_month')

    context['f'] = frm
    context['month_list'] = month_model.objects.all()
    return render(request,"addmonth.html",context)
def show_month(request):
    context = {}
    context['month_list'] = month_model.objects.all()
    return render(request, "addmonth.html", context)
#update district
def update_month(request,mid):
    context={}
    obj=get_object_or_404(month_model,id=mid)
    frm = month_form(request.POST or None,instance=obj)
    if frm.is_valid():
        frm.save()
        return HttpResponseRedirect("/Adhome/insert_month")
    context['month_data'] = frm
    return render(request, "updatemonth.html", context)
#delete district
def delete_month(request,mid):
    context={}
    obj = get_object_or_404(month_model, id=mid)
    obj.delete()
    return HttpResponseRedirect("/Adhome/insert_month")

def insert_expense(request):
    context={}
    frm=expense_form(request.POST or None)
    exp = request.POST.get('Exptype')
    if expense_model.objects.filter(Exptype=exp).exists():
        messages.info(request, 'This Expenses Already Exists')
        return redirect('/Adhome/insert_expense')
    else:

        if frm.is_valid():
            frm.save()
            return redirect('/Adhome/insert_expense')

    context['f'] = frm
    context['expense_list'] = expense_model.objects.all()

    return render(request,"addexpense.html",context)
#show expense details
def show_expense(request):
    context = {}
    context['expense_list'] = expense_model.objects.all()
    return render(request, "addexpense.html", context)
#update district
def update_expense(request,eid):
    context={}
    obj=get_object_or_404(expense_model,id=eid)
    frm = expense_form(request.POST or None,instance=obj)
    if frm.is_valid():
        frm.save()
        return HttpResponseRedirect("/Adhome/insert_expense")
    context['expense_data'] = frm
    return render(request, "updateexpense.html", context)
#delete district
def delete_expense(request,eid):
    context={}
    obj = get_object_or_404(expense_model, id=eid)
    obj.delete()
    return HttpResponseRedirect("/Adhome/insert_expense")
def insert_schedule(request):
    context={}
    frm=schedule_form(request.POST or None)
    pooja = request.POST.get('poojaid')
    day=request.POST.get('dayid')
    timings = request.POST.get('Timings')
    if poojaschedule_model.objects.filter(dayid=day,poojaid=pooja,Timings=timings).exists():
        messages.info(request, 'This Schdule Already Exists')
        return redirect('/Adhome/insert_schedule')
    else:

        if frm.is_valid():
            frm.save()
            return redirect('/Adhome/insert_schedule')
        context['f'] = frm
        context['schedule_list'] = poojaschedule_model.objects.all()
        return render(request, "addschedule.html", context)

    # show expense details
def show_schedule(request):
        context = {}
        context['schedule_list'] = poojaschedule_model.objects.all()
        return render(request, "addschedule.html", context)

    # update district
def update_schedule(request, sid):
        context = {}
        obj = get_object_or_404(poojaschedule_model, id=sid)
        frm = schedule_form(request.POST or None, instance=obj)
        schedule = request.POST.get('dayid')
        if poojaschedule_model.objects.filter(dayid=schedule).exists():
            messages.info(request, 'This Schdule Already Exists')
            return redirect('/Adhome/insert_schedule')
        else:

            if frm.is_valid():
                frm.save()
                return redirect('/Adhome/insert_schedule')
        context['schedule_data'] = frm
        return render(request, "updateschedule.html", context)

    # delete district
def delete_schedule(request, sid):
        context = {}
        obj = get_object_or_404(poojaschedule_model, id=sid)
        obj.delete()
        return HttpResponseRedirect("/Adhome/insert_schedule")

def insert_special(request):
    context={}
    frm=specialday_form(request.POST or None)
    special = request.POST.get('Title')
    if specialday_model.objects.filter(Title=special).exists():
        messages.info(request, 'This Title Already Exists')
        return redirect('/Adhome/insert_special')
    else:

        if frm.is_valid():
            frm.save()
            return redirect('/Adhome/insert_special')

    context['f'] = frm
    context['special_list'] = specialday_model.objects.all()
    return render(request,"addspecial.html",context)
#show expense details
def show_special(request):
    context = {}
    context['special_list'] = specialday_model.objects.all()
    return render(request, "addspecial.html", context)
#update special
def update_special(request,sid):
    context={}
    obj=get_object_or_404(specialday_model,id=sid)
    frm = specialday_form(request.POST or None,instance=obj)
    if frm.is_valid():
        frm.save()
        return HttpResponseRedirect("/Adhome/insert_special")
    context['special_data'] = frm
    return render(request, "updatespecial.html", context)
#delete special
def delete_special(request,sid):
    context={}
    obj = get_object_or_404(specialday_model, id=sid)
    obj.delete()
    return HttpResponseRedirect("/Adhome/insert_special")

def insert_careers(request):
    context={}
    frm=careers_form(request.POST or None)
    careers = request.POST.get('Refno')
    if careers_model.objects.filter(Refno=careers).exists():
        messages.info(request, 'This Reference Id Already Exists')
        return redirect('/Adhome/insert_careers')
    else:

        if frm.is_valid():
            frm.save()
            return redirect('/Adhome/insert_careers')

    context['f'] = frm
    context['careers_list'] = careers_model.objects.all()
    return render(request,"addcareers.html",context)
#show expense details
def show_careers(request):
    context = {}
    context['careers_list'] = careers_model.objects.all()
    return render(request, "addcareers.html", context)
#update special
def update_careers(request,cid):
    context={}
    obj=get_object_or_404(careers_model,id=cid)
    frm = careers_form(request.POST or None,instance=obj)
    if frm.is_valid():
        frm.save()
        return HttpResponseRedirect("/Adhome/insert_careers")
    context['careers_data'] = frm
    return render(request, "updatecareers.html", context)
#delete special
def delete_careers(request,cid):
    context={}
    obj = get_object_or_404(careers_model, id=cid)
    obj.delete()
    return HttpResponseRedirect("/Adhome/insert_careers")
def insert_darshan(request):
    context={}
    frm=darsh_form(request.POST or None)
    timings=request.POST.get('Timings')
    if darshan_model.objects.filter(Timings=timings).exists():
        messages.info(request, 'This darshan time Already Exists')
        return redirect('/Adhome/insert_darshan')
    else:

        if frm.is_valid():
            frm.save()
            return redirect('/Adhome/insert_darshan')

    context['f'] = frm
    context['darshan_list'] = darshan_model.objects.all()
    return render(request,"adddarshan.html",context)

def show_darshan(request):
    context = {}
    context['darshan_list'] = darshan_model.objects.all()
    return render(request, "adddarshan.html", context)
def update_darshan(request,did):
    context={}
    obj=get_object_or_404(darshan_model,id=did)
    frm = darsh_form(request.POST or None,instance=obj)
    if frm.is_valid():
        frm.save()
        return HttpResponseRedirect("/Adhome/insert_darshan")
    context['dars_data'] = frm
    return render(request, "updatedarshan.html", context)
#delete special
def delete_darshan(request,did):
    context={}
    obj = get_object_or_404(darshan_model, id=did)
    obj.delete()
    return HttpResponseRedirect("/Adhome/insert_darshan")
def view_enquiry(request):
    context = {}
    context['enq_list'] = enquiry_model.objects.filter(Status='new')
    return render(request, "viewenquiry.html", context)

def more_enquiry(request,enid):
    context={}
    context['enquiry_list']=enquiry_model.objects.filter(id=enid)
    return render(request, "Activate_enquiry.html", context)
def activate_enquiry(request,enid):
    context={}
    obj = get_object_or_404(enquiry_model, id=enid)
    new_status='read'
    obj.Status=new_status
    obj.save()
    return HttpResponseRedirect("/Adhome/view_enquiry")
#delete special
def delete_enquiry(request,eid):
    context={}
    obj = get_object_or_404(enquiry_model, id=eid)
    obj.delete()
    return HttpResponseRedirect("/Adhome/show_enquiry")

def view_application(request):
    context={}

    context["view_appli"]= application_model.objects.prefetch_related('Devotee_id', 'careerid')

    return render(request, "showapplication.html", context)


def insert_poojatype(request):
    context={}
    frm= poojatype_form(request.POST or None,request.FILES)
    pooja=request.POST.get('Pooja_type')
    if poojatype_model.objects.filter(Pooja_type=pooja).exists():
        messages.info(request,'Pooja Type is Already Exists')
        return redirect('/Adhome/insert_poojatype')
    else:

        if frm.is_valid():
            frm.save()
            return redirect('/Adhome/insert_poojatype')

    context['f']=frm
    context['poojatype_list'] = poojatype_model.objects.all()
    return render(request,"addpoojatype.html",context)
def show_poojatype(request):
    context = {}
    context['poojatype_list'] = poojatype_model.objects.all()
    return render(request, "addpoojatype.html", context)
def update_poojatype(request,pid):
    context={}
    obj=get_object_or_404(poojatype_model,id=pid)
    frm = poojatype_form(request.POST or None,instance=obj)
    if frm.is_valid():
        frm.save()
        return HttpResponseRedirect("/Adhome/insert_poojatype")
    context['poojatype_data'] = frm
    return render(request, "updatepoojatype.html", context)
#delete district
def delete_poojatype(request,pid):
    context={}
    obj = get_object_or_404(poojatype_model, id=pid)
    obj.delete()
    return HttpResponseRedirect("/Adhome/insert_poojatype")