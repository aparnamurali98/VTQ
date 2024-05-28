import datetime

from django.contrib import messages
from django.db.models import Sum
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect

from Adminhome.models import staff_model

from staff.staff_form import staff_form

from Registration.models import devotee_model

from Adminhome.models import income_model
from Devotee.models import bookingpooja_model
from .income_form import incomes_form
from staff.models import incomes_model


def home (request):
    return HttpResponse("<a href='view_staff'>update staff</a>"
                        "<br><a href='incomes'>insert_incomes</a>"
                        "<br><a href='view_income'>view_income</a>"

                        )


def view_staff(request):
    context = {}
    staff_id=request.session["staff_id"]
    context['staff_list'] = staff_model.objects.filter(id=staff_id)
    return render(request, "viewstaff.html", context)
def update_staff(request,sid):
    context={}
    obj=get_object_or_404(staff_model,id=sid)
    frm = staff_form(request.POST or None,request.FILES or None,instance=obj)
    if frm.is_valid():
        frm.save()
        return HttpResponseRedirect("/staff_home/view_staff")
    context['staff_data'] = frm
    return render(request, "updatestaff.html", context)
def incomes(request):
    context={}
    staff_id=request.session["staff_id"]
    staff = get_object_or_404(staff_model, id=staff_id)
    frm=incomes_form(request.POST or None)
    if request.POST:
        if frm.is_valid():
            income_date = request.POST.get('income_date')
            Amount = request.POST.get('Amount')
            income_typeid = frm.cleaned_data['income_typeid']
            Narration = request.POST.get('Narration')
            incomes=incomes_model.objects.create(income_typeid=income_typeid,income_date=income_date,Amount=Amount,Narration=Narration,staff=staff)
            return HttpResponseRedirect('/staff_home/incomes')
    context['f'] = frm
    return render(request,"incomesstaff.html",context)
def view_income(request):
    context = {}

    total_staff_income = incomes_model.objects.filter(staff__isnull=False).aggregate(total=Sum('Amount'))['total']
    total_pooja_income = incomes_model.objects.filter(Bookingpooja__isnull=False).aggregate(total=Sum('Amount'))['total']
    context['total_staff_income'] = total_staff_income
    context['total_pooja_income'] = total_pooja_income
    return render(request, "viewincometotal.html", context)

