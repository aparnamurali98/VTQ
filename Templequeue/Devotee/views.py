from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect

from Adminhome.models import staff_model

from Adminhome.models import templeinfo_model

from Adminhome.models import poojaschedule_model

from Adminhome.models import specialday_model

from Adminhome.models import income_model

from Adminhome.models import careers_model

from Adminhome.models import darshan_model

from .searchtemple_form import location_form



# Create your views here.
def home (request):
    return HttpResponse("<a href='show_staff'>view staff</a>"
                       # "<br><br><a href='show_templeinfo'> view templeinfo</a>"
                        "<br><br><a href='show_schedule'> view schedule</a>"
                        "<br><br><a href='show_special'> view special</a>"
                        "<br><br><a href='show_income'> viewincome</a>"
                        "<br><br><a href='show_careers'> view careers</a>"
                        "<br><br><a href='show_darshan'> view darshan timing</a>"
                        "<br><br><a href='search_temple'> Search Temple</a>"

                        )


def show_staff(request):
    context = {}
    context['staff_list'] = staff_model.objects.all()
    return render(request, "viewstaff.html", context)

# def show_templeinfo(request):
#     context = {}
#     context['info_list'] = templeinfo_model.objects.all()
#     return render(request, "vietemp.html", context)

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
    data_list = [{'tname': item.tname, 'taddress': item.address} for item in data]
    return JsonResponse({'data': data_list})
