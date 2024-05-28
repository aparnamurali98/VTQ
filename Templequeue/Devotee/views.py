from time import timezone

import django.utils.timezone
from django.db.models import Sum
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect

from Adminhome.models import staff_model

from Adminhome.models import templeinfo_model

from Adminhome.models import poojaschedule_model

from Adminhome.models import specialday_model

from Adminhome.models import income_model

from Adminhome.models import careers_model

from Adminhome.models import darshan_model
from django.urls import reverse

from .application_form import application_form
from .models import application_model, poojabook_model, bookingpooja_model, payment_model
from .payment_form import payment_form
from .poojabook_form import poojabook_form
from .searchtemple_form import location_form
from Registration.models import devotee_model

from Adminhome.models import pooja_model

from staff.income_form import incomes_form
from staff.models import incomes_model


# Create your views here.
def home (request):
    return HttpResponse("<a href='show_staff'>view staff</a>"
                       "<br><br><a href='show_templeinfo'> view templeinfo</a>"
                        "<br><br><a href='show_schedule'> view schedule</a>"
                        "<br><br><a href='show_special'> view special</a>"
                        "<br><br><a href='show_income'> viewincome</a>"
                        "<br><br><a href='show_careers'> view careers</a>"
                        "<br><br><a href='show_darshan'> view darshan timing</a>"
                
                        "<br><br><a href='search_temple'>Search tempe</a>"
                        "<br><br><a href='show_pooja'>show_pooja </a>"
                        "<br><br><a href='index'>index </a>"


                        )


def show_staff(request):
    context = {}
    context['staff_list'] = staff_model.objects.all()
    return render(request, "viewstaff.html", context)

def show_templeinfo(request):
    context = {}
    context['info_list'] = templeinfo_model.objects.all()
    return render(request, "vietemp.html", context)

def show_schedule(request):
     context = {}
     context['schedule_list'] = poojaschedule_model.objects.all()
     return render(request, "viewchedule.html", context)
def show_special(request):
    context = {}
    context['special_list'] = specialday_model.objects.all()
    return render(request, "viewspecial.html", context)
def show_income(request):
    context = {}
    context['income_list'] = income_model.objects.all()
    return render(request, "viewincome.html", context)
def show_careers(request):
    context = {}
    context['careers_list'] = careers_model.objects.all()
    return render(request, "viewcareers.html", context)

def show_darshan(request):
    context = {}
    context['darshan_list'] = darshan_model.objects.all()
    return render(request, "viewdarshan.html", context)
def search_temple(request):
    context = {}
    frm = location_form(request.POST or None)
    context['f'] = frm
    return render(request, "serachtemple.html", context)
def search_temple1(request):
    locid = request.GET.get('selected_value')
    data = templeinfo_model.objects.filter(loc=locid)
    data_list = [{'tname': item.tname, 'taddress': item.address, 'tdiscription': item.discription, 'tcotname': item.cotname, 'tPhoto': item.Photo.url} for item in data]
    return JsonResponse({'data': data_list})
def insert_Application(request,cid):
    context={}
    did = request.session["devote_id"]
    devote_object = devotee_model.objects.get(id=did)
    print(did)
    careerid=careers_model.objects.get(id=cid)
    frm=application_form(request.POST or None,request.FILES or None )
    if request.POST:
        if frm.is_valid():
            Resume = request.FILES.get('Resume')
            # Resume = File1.name
            appli=application_model.objects.create(careerid=careerid,Devotee_id=devote_object,Resume=Resume)
            return HttpResponseRedirect("/Devotee/show_careers")
    context['f'] = frm
    return render(request,"apply_career.html",context)



def show_pooja(request):
    context = {}
    context['pooja_list'] = pooja_model.objects.all()
    return render(request, "viewpooja.html", context)
# def insert_poojabook(request,pid):
#     context={}
#     did = request.session["devote_id"]
#     devote_object = devotee_model.objects.get(id=did)
#     print(did)
#
#     frm=poojabook_form(request.POST or None)
#     if request.POST:
#         if frm.is_valid():
#             Name=request.POST.get('Name')
#             star = request.POST.get('star')
#
#             pooja=poojabook_model.objects.create(Devotee_id=devote_object,Name=Name,star=star)
#             return HttpResponseRedirect("/Devotee/insert_poojabook")
#     context['f'] = frm
#     return render(request,"poojabook.html",context)

def Addtocart(request,pid):
    context = {}
    did = request.session["devote_id"]
    devote_object = devotee_model.objects.get(pk=did)
    pooja_object = pooja_model.objects.get(id=pid)
    pooja = poojabook_model.objects.create(Devotee=devote_object,pooja=pooja_object)
    poojabook_list = poojabook_model.objects.select_related('pooja').filter(Devotee=devote_object ,Status='cart')
    context['poojabook_list']=poojabook_list
    subtotal=poojabook_list.aggregate(subtotal=Sum('pooja__amount'))['subtotal']or 0
    context['subtotal']=subtotal
    return render(request, "viewcart.html", context)

def add_addtocart(request):
    context={}
    did = request.session["devote_id"]
    devote_object = devotee_model.objects.get(pk=did)
    pooja = request.POST.get('poojaid')
    obj = get_object_or_404(poojabook_model, id=pooja,Devotee=devote_object,Status='cart')
    print(obj)

    if request.POST:
        print('name1')
        Dname =request.POST.get('Dname')
        print(Dname)
        star=request.POST.get('star')
        obj.Name=Dname
        obj.star=star
        print('star',star)

        obj.save()
        return HttpResponseRedirect('/Devotee/show_pooja')


def delete_addtocart(request,poojaid):
    context={}
    obj = get_object_or_404(poojabook_model, id=poojaid)
    obj.delete()

    return HttpResponseRedirect("/Devotee/Addtocart")
def Confirm_order(request):
    context = {}
    did = request.session["devote_id"]
    devote_object = devotee_model.objects.get(id=did)
    print(did)
    if request.POST:
        Bookingdate = request.POST.get('bdate')
        total_amount = request.POST.get('amount')
        print(total_amount)
        pooja = bookingpooja_model.objects.create(Devotee=devote_object, Want_date=Bookingdate, Total_amount=total_amount)
        obj = poojabook_model.objects.filter( Status='cart',Devotee=devote_object)
        for poojaobject in obj:
            new_status = 'confirm'
            poojaobject.Status = new_status
            poojaobject.save()
            print('pooja',pooja)
            print('poojaid',pooja.id)
            # return redirect('payment', bookingid=pooja)
            pid = pooja.id
            print(pid)
            url = reverse('payment', kwargs={'pid': pid, 'subtotal': total_amount})
            return redirect(url)
        return HttpResponseRedirect("/Devotee/Addtocart")


# def payment(request,pid):
#     context = {}
#     frm = payment_form(request.POST or None)
#     if request.POST:
#         card_type = request.POST.get('card_type')
#         card_holder_name = request.POST.get('card_holder_name')
#         card_number = request.POST.get('card_number')
#         card_exp_date = request.POST.get('card_exp_date')
#         cvv_number = request.POST.get('cvv_number')
#         total_amount = request.POST.get('total_amount')
#         pooja_booking = bookingpooja_model.objects.get(pk=pid)
#         payment = payment_model.objects.create( poojabook=pooja_booking,card_type=card_type,card_holder_name=card_holder_name, Card_number=card_number,card_exp_date=card_exp_date,cvv_number=cvv_number,Total_amount=total_amount)
#     context['f'] =frm
#     return render(request,'payment.html')
def payment(request, pid,subtotal):
    context = {}
    did = request.session["devote_id"]
    devote_object = devotee_model.objects.get(id=did)
    if request.method == 'POST':
        frm = payment_form(request.POST)
        if frm.is_valid():
            card_type = request.POST.get('card_type')
            card_holder_name = request.POST.get('card_holder_name')
            card_number = request.POST.get('Card_number')
            card_exp_date = request.POST.get('card_exp_date')
            cvv_number = request.POST.get('cvv_number')
            total_amount = subtotal
            income_date=django.utils.timezone.now()
            Narration='pooja booking'
            typeid=income_model.objects.get(pk=1)
            pooja_booking = bookingpooja_model.objects.get(pk=pid)
            payment = payment_model.objects.create(poojabook=pooja_booking, card_type=card_type, card_holder_name=card_holder_name, Card_number=card_number, card_exp_date=card_exp_date, cvv_number=cvv_number, Total_amount=total_amount)
            incomes = incomes_model.objects.create(Devotee=devote_object,Bookingpooja=pooja_booking, income_typeid=typeid, income_date=income_date,Amount=total_amount, Narration=Narration)
        return render(request, 'receipt.html', context)
    else:

        frm = payment_form(initial={'Total_amount': subtotal})
    context['f'] = frm
    return render(request, 'payment.html', context)


def index(request):

    return render(request, 'index.html')
