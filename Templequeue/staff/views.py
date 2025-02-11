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
from staff.models import incomes_models


def home (request):
    return render(request, "staffheader.html")
    # return HttpResponse("<a href='view_staff'>view_staff</a>"
    #                     "<br><a href='incomes'>insert_incomes</a>"
    #                     "<br><a href='view_income'>view_income</a>"
    #
    #                     )


def view_staff(request):
    context = {}
    try:
        # Retrieve staff_id from the session
        staff_id = request.session["staff_id"]
        # Fetch staff records for the given staff_id
        context['staff_list'] = staff_model.objects.filter(id=staff_id)
    except Exception as e:
        # Handle any exception that occurs
        context['staff_list'] = []
        # Optionally log the error or show an error message
        messages.error(request, f"An error occurred: {str(e)}")

    # Render the viewstaff.html template with the staff list in context
    return render(request, "viewstaff.html", context)


def update_staff(request, sid):
    context = {}
    try:
        # Fetch the staff object with the given id, or return a 404 if not found
        obj = get_object_or_404(staff_model, id=sid)

        # Create a form instance with POST data (or None) and FILES data (if any), for the given object
        frm = staff_form(request.POST or None, request.FILES or None, instance=obj)

        # If the form is valid, save the changes and redirect
        if frm.is_valid():
            frm.save()
            return HttpResponseRedirect("/staff_home/view_staff")

        # Add the form to context if it is not valid or in case of a GET request
        context['staff_data'] = frm

    except Exception as e:
        # Handle any exception that occurs
        messages.error(request, f"An error occurred: {str(e)}")
        return HttpResponseRedirect("/staff_home")  # Redirect to a safe location

    # Render the updatestaff.html template with the form in context
    return render(request, "updatestaff.html", context)


def incomes(request):
    context = {}
    try:
        # Retrieve staff_id from the session
        staff_id = request.session["staff_id"]

        # Fetch the staff object with the given id or raise a 404 if not found
        staff = get_object_or_404(staff_model, id=staff_id)

        # Initialize the form
        frm = incomes_form(request.POST or None)

        # Check if the request method is POST
        if request.POST:
            if frm.is_valid():
                # Retrieve form data
                income_date = request.POST.get('income_date')
                Amount = request.POST.get('Amount')
                income_typeid = frm.cleaned_data['income_typeid']
                Narration = request.POST.get('Narration')
                Temple_name= frm.cleaned_data['Temple_name']


                # Create a new income record
                incomes_models.objects.create(
                    income_typeid=income_typeid,
                    income_date=income_date,
                    Amount=Amount,
                    Narration=Narration,
                    staff=staff,
                    Temple_name=Temple_name
                )


                # Redirect to the incomes page after successful form submission
                return HttpResponseRedirect('/staff_home/incomes')

        # Add the form to context for rendering in the template
        context['f'] = frm

    except Exception as e:
        # Handle any exception that occurs and display an error message
        messages.error(request, f"An error occurred: {str(e)}")
        return HttpResponseRedirect('/staff_home/incomes')  # Redirect to the incomes page

    # Render the template with the form in context
    return render(request, "incomesstaff.html", context)


def view_income(request):
    context = {}

    total_staff_income = incomes_models.objects.filter(staff__isnull=False).aggregate(total=Sum('Amount'))['total']
    total_pooja_income = incomes_models.objects.filter(Bookingpooja__isnull=False).aggregate(total=Sum('Amount'))['total']
    context['total_staff_income'] = total_staff_income
    context['total_pooja_income'] = total_pooja_income
    return render(request, "viewincometotal.html", context)

# def pooja_booking(request):
#     context = {}
#
#     try:
#         # Retrieve all temple information records from the database
#         context['booking'] = poojabook_model.objects.values(
#             'Devotee',  # Devotee ID
#             'pooja',  # Pooja Name
#             'Name',  # Name
#             'star'  # Star
#         )
#
#     except Exception as ex:
#         # Handle any unexpected exceptions
#         messages.error(request, f"An error occurred while fetching temple information: {str(ex)}")
#
#     # Render the template with the context data
#     return render(request, "viewbooking.html", context)
#
