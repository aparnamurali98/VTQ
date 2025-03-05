from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import EmailMessage, get_connection
from django.conf import settings
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
    return render(request, "adminheader.html")
    # return HttpResponse("<a href='insert_district'>District</a>"
    #                     "<br><br><a href='insert_location'>Location</a>"
    #                     "<br><br><a href='insert_staff'> staff</a>"
    #                     "<br><br><a href='insert_templeinfo'>Temple info</a>"
    #                     "<br><br><a href='insert_priest'>Hindu Priest</a>"
    #
    #                     "<br><br><a href='insert_pooja'>Poojatype</a>"
    #                     "<br><br><a href='insert_day'>Day</a>"
    #                     "<br><br><a href='insert_transf'>transfermode</a>"
    #                     "<br><br><a href='insert_income'>income</a>"
    #                     "<br><br><a href='insert_month'>month</a>"
    #                     "<br><br><a href='insert_expense'>expense</a>"
    #                     "<br><br><a href='insert_schedule'>schedule</a>"
    #                     "<br><br><a href='insert_special'>special</a>"
    #                     "<br><br><a href='insert_careers'>Careers</a>"
    #                     "<br><br><a href='insert_darshan'>Darshana timming</a>"
    #                     "<br><br><a href='view_enquiry'> view enquiry</a>"
    #                     "<br><br><a href='view_application'> view Applications</a>"
    #                     "<br><br><a href='insert_poojatype'>Pooja Type </a>"
    #
    #
    #                     )

def insert_district(request):
    context = {}

    # Initialize the district form with POST data if available; otherwise, use None
    frm = dist_form(request.POST or None)

    # Retrieve the district name from the POST data
    dist = request.POST.get('distname')

    try:
        # Check if a district with the same name already exists in the database
        if distric_model.objects.filter(distname=dist).exists():
            # If it exists, show an info message to the user
            messages.info(request, 'District Already Exists')
            # Redirect the user back to the district form
            return redirect('/Adhome/insert_district')
        else:
            # If the district doesn't exist, check if the form is valid
            if frm.is_valid():
                # If the form is valid, save the form data to the database
                frm.save()
                # Redirect the user back to the district form after saving
                return redirect('/Adhome/insert_district')

    except Exception as ex:
        # Handle any unexpected exceptions
        # Log the exception (optional) or show an error message
        messages.error(request, f"An error occurred: {str(ex)}")
        # You could also redirect to an error page or simply return to the form

    # Add the form to the context dictionary
    context['f'] = frm

    # Fetch all districts from the database and add them to the context
    context['distric_list'] = distric_model.objects.all()

    # Render the district form page with the current context, including the list of districts
    return render(request, "adddist.html", context)

def show_district(request):
    context = {}

    try:
        # Fetch all district records from the database
        context['distric_list'] = distric_model.objects.all()

    except Exception as ex:
        # Handle any unexpected exceptions
        # Log the exception (optional) or show an error message
        messages.error(request, f"An error occurred while fetching districts: {str(ex)}")
        # If desired, you can also redirect to an error page or set an empty list
        context['distric_list'] = []

    # Render the adddist.html template with the district list in context
    return render(request, "adddist.html", context)

def update_district(request, did):
    context = {}

    try:
        # Fetch the district object by ID, or return a 404 error if not found
        obj = get_object_or_404(distric_model, id=did)

        # Initialize the form with POST data and the existing district object (for updating)
        frm = dist_form(request.POST or None, instance=obj)

        # Check if the form is valid
        if frm.is_valid():
            # Save the updated district information to the database
            frm.save()
            # Redirect to the district insertion page after saving
            return HttpResponseRedirect("/Adhome/insert_district")

    except Exception as ex:
        # Handle any unexpected exceptions
        # Display an error message using Django's messaging framework
        messages.error(request, f"An error occurred while updating the district: {str(ex)}")
        # Optionally, you could log the error or handle it differently

    # Add the form to the context dictionary for rendering the template
    context['dis_data'] = frm

    # Render the update district page with the current context
    return render(request, "updatedistrict.html", context)

def delete_district(request, did):
    context = {}

    try:
        # Fetch the district object by ID, or return a 404 error if not found
        obj = get_object_or_404(distric_model, id=did)

        # Delete the district object from the database
        obj.delete()

        # Redirect to the district insertion page after deletion
        return HttpResponseRedirect("/Adhome/insert_district")

    except Exception as ex:
        # Handle any unexpected exceptions
        # Display an error message using Django's messaging framework
        messages.error(request, f"An error occurred while deleting the district: {str(ex)}")
        # Optionally, you could log the error or handle it differently

        # Redirect to the district insertion page even if there's an error
        return HttpResponseRedirect("/Adhome/insert_district")

def insert_location(request):
    context = {}

    try:
        # Initialize the location form with POST data if available; otherwise, use None
        frm = loca_form(request.POST or None)

        # Retrieve the location name from the POST data
        loca = request.POST.get('locname')

        # Check if a location with the same name already exists in the database
        if location_model.objects.filter(locname=loca).exists():
            # If it exists, show an info message to the user
            messages.info(request, 'Location Name Already Exists')
            # Redirect the user back to the location form
            return redirect('/Adhome/insert_location')
        else:
            # If the location doesn't exist, check if the form is valid
            if frm.is_valid():
                # If the form is valid, save the form data to the database
                frm.save()
                # Redirect the user back to the location form after saving
                return redirect('/Adhome/insert_location')

    except Exception as ex:
        # Handle any unexpected exceptions
        # Log the exception (optional) or show an error message
        messages.error(request, f"An error occurred while inserting the location: {str(ex)}")
        # If desired, you could also redirect to an error page or simply return to the form

    # Add the form to the context dictionary
    context['f'] = frm

    # Fetch all locations from the database and add them to the context
    context['location_list'] = location_model.objects.all()

    # Render the location form page with the current context, including the list of locations
    return render(request, "addloc.html", context)

def show_location(request):
    context = {}

    try:
        # Fetch all location records from the database
        context['location_list'] = location_model.objects.all()

    except Exception as ex:
        # Handle any unexpected exceptions
        # Display an error message using Django's messaging framework
        messages.error(request, f"An error occurred while fetching locations: {str(ex)}")
        # Optionally, you can log the error or handle it differently
        # Set an empty list in the context to avoid breaking the template
        context['location_list'] = []

    # Render the addloc.html template with the location list in context
    return render(request, "addloc.html", context)

def update_location(request, lid):
    context = {}

    try:
        # Fetch the location object by ID, or return a 404 error if not found
        obj = get_object_or_404(location_model, id=lid)

        # Initialize the form with POST data if available, and bind it to the existing location object
        frm = loca_form(request.POST or None, instance=obj)

        # Check if the form is valid
        if frm.is_valid():
            # Save the updated location information to the database
            frm.save()
            # Redirect to the location insertion page after saving
            return HttpResponseRedirect("/Adhome/insert_location")

    except Exception as ex:
        # Handle any unexpected exceptions
        # Display an error message using Django's messaging framework
        messages.error(request, f"An error occurred while updating the location: {str(ex)}")
        # Optionally, log the error or handle it differently

    # Add the form to the context dictionary for rendering the template
    context['loc_data'] = frm

    # Render the update location page with the current context
    return render(request, "updateloca.html", context)

def delete_location(request, lid):
    context = {}

    try:
        # Fetch the location object by ID, or return a 404 error if not found
        obj = get_object_or_404(location_model, id=lid)

        # Delete the location object from the database
        obj.delete()

        # Redirect to the location insertion page after deletion
        return HttpResponseRedirect("/Adhome/insert_location")

    except Exception as ex:
        # Handle any unexpected exceptions
        # Display an error message using Django's messaging framework
        messages.error(request, f"An error occurred while deleting the location: {str(ex)}")
        # Optionally, you could log the error or handle it differently

        # Redirect to the location insertion page even if there's an error
        return HttpResponseRedirect("/Adhome/insert_location")

def insert_staff(request):
    context={}
    frm= staf_form(request.POST or None,request.FILES or None)
    if request.POST:
        print(request.POST)
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
            temp_id = request.POST.get('Temple_name')
            temp_instance = templeinfo_model.objects.get(id=temp_id)
            staffusername = request.POST.get('username')
            staffpassword = request.POST.get('password')
            staffconfirm_password = request.POST.get('confirm_password')
            if staffconfirm_password == staffpassword:
                if frm.is_valid():
                    loginid=User.objects.create_user(username=staffusername,password=staffpassword)
                    role = role_model.objects.create(login=loginid, roletype=3)
                    staffreg=staff_model.objects.create(sname=staffname,address=saddress,email=semail,mobile=smobile,photo=sphoto,dob=dob,age=sage,gender=gender,Temple_name=temp_instance,login=loginid)
                    return HttpResponseRedirect('/Adhome')
            else:
                messages.error(request,"password does not match")
        except Exception as ex:
            print(ex)
            error_message="User Name Alredy Exists"

            messages.error(request,error_message)

    context['f']=frm
    context['staff_list'] = staff_model.objects.all()
    return render(request,"addstaff.html",context)

def insert_templeinfo(request):
    context = {}

    try:
        # Initialize the temple form with POST data if available and handle file uploads
        frm = temple_form(request.POST or None, request.FILES)

        # Retrieve the temple name from the POST data
        temple = request.POST.get('tname')

        # Check if a temple with the same name already exists in the database
        if templeinfo_model.objects.filter(tname=temple).exists():
            # If it exists, show an info message to the user
            messages.info(request, 'Temple Name Already Exists')
            # Redirect the user back to the temple information form
            return redirect('/Adhome/insert_templeinfo')
        else:
            # If the temple doesn't exist, check if the form is valid
            if frm.is_valid():
                # If the form is valid, save the form data (including file uploads) to the database
                frm.save()
                # Redirect the user back to the temple information form after saving
                return redirect('/Adhome/insert_templeinfo')

    except Exception as ex:
        # Handle any unexpected exceptions
        # Display an error message using Django's messaging framework
        messages.error(request, f"An error occurred while inserting the temple information: {str(ex)}")
        # Optionally, you could log the error or handle it differently

    # Add the form to the context dictionary
    context['f'] = frm

    # Fetch all temple information records from the database and add them to the context
    context['info_list'] = templeinfo_model.objects.all()

    # Render the addtemp.html template with the current context, including the form and list of temple information
    return render(request, "addtemp.html", context)

#display temple info details
def show_templeinfo(request):
    context = {}

    try:
        # Fetch all temple information records from the database
        context['info_list'] = templeinfo_model.objects.all()

    except Exception as ex:
        # Handle any unexpected exceptions
        # Display an error message using Django's messaging framework
        messages.error(request, f"An error occurred while fetching temple information: {str(ex)}")
        # Optionally, you could log the error or handle it differently
        # Set an empty list in the context to avoid breaking the template
        context['info_list'] = []

    # Render the addtemp.html template with the current context, including the list of temple information
    return render(request, "addtemp.html", context)

#update district
def update_templeinfo(request, tid):
    context = {}

    try:
        # Fetch the temple information object by ID, or return a 404 error if not found
        obj = get_object_or_404(templeinfo_model, id=tid)

        # Initialize the form with POST data and files if available, and bind it to the existing temple object
        frm = temple_form(request.POST or None, request.FILES or None, instance=obj)

        # Check if the form is valid
        if frm.is_valid():
            # If the form is valid, save the updated temple information to the database
            frm.save()
            # Redirect to the temple information insertion page after saving
            return HttpResponseRedirect("/Adhome/insert_templeinfo")

    except Exception as ex:
        # Handle any unexpected exceptions
        # Display an error message using Django's messaging framework
        messages.error(request, f"An error occurred while updating the temple information: {str(ex)}")
        # Optionally, you could log the error or handle it differently

    # Add the form to the context dictionary for rendering the template
    context['info_data'] = frm

    # Render the update temple information page with the current context
    return render(request, "updatetemple.html", context)

#delete district
def delete_templeinfo(request, tid):
    context = {}

    try:
        # Fetch the temple information object by ID, or return a 404 error if not found
        obj = get_object_or_404(templeinfo_model, id=tid)

        # Delete the temple information object from the database
        obj.delete()

        # Redirect to the temple information insertion page after deletion
        return HttpResponseRedirect("/Adhome/insert_templeinfo")

    except Exception as ex:
        # Handle any unexpected exceptions
        # Display an error message using Django's messaging framework
        messages.error(request, f"An error occurred while deleting the temple information: {str(ex)}")
        # Optionally, you could log the error or handle it differently

        # Redirect to the temple information insertion page even if there's an error
        return HttpResponseRedirect("/Adhome/insert_templeinfo")


def insert_priest(request):
    context = {}

    try:
        # Initialize the priest form with POST data if available
        frm = prie_form(request.POST or None)

        # Retrieve the priest name and phone number from the POST data
        priest = request.POST.get('Pname')
        phoneno = request.POST.get('Phone')

        # Check if a priest with the same name and phone number already exists
        if priest_model.objects.filter(Pname=priest, Phone=phoneno).exists():
            # If it exists, show an info message to the user
            messages.info(request, 'Priest Already Exists')
            # Redirect the user back to the priest insertion page
            return redirect('/Adhome/insert_priest')
        else:
            # If the priest does not exist, check if the form is valid
            if frm.is_valid():
                # If the form is valid, save the priest information to the database
                frm.save()
                # Redirect the user back to the priest insertion page after saving
                return redirect('/Adhome/insert_priest')

    except Exception as ex:
        # Handle any unexpected exceptions
        # Display an error message using Django's messaging framework
        messages.error(request, f"An error occurred while inserting the priest: {str(ex)}")
        # Optionally, you could log the error or handle it differently

    # Add the form and list of priests to the context dictionary
    context['f'] = frm
    context['priest_list'] = priest_model.objects.all()

    # Render the addprie.html template with the current context
    return render(request, "addprie.html", context)


def show_priest(request):
    context = {}

    try:
        # Fetch all priest records from the database
        context['priest_list'] = priest_model.objects.all()

    except Exception as ex:
        # Handle any unexpected exceptions
        # Display an error message using Django's messaging framework
        messages.error(request, f"An error occurred while fetching priest information: {str(ex)}")
        # Optionally, you could log the error or handle it differently
        # Set an empty list in the context to avoid breaking the template
        context['priest_list'] = []

    # Render the addprie.html template with the current context, including the list of priests
    return render(request, "addprie.html", context)


def update_priest(request, pid):
    context = {}

    try:
        # Fetch the priest object by ID, or return a 404 error if not found
        obj = get_object_or_404(priest_model, id=pid)

        # Initialize the form with POST data if available, and bind it to the existing priest object
        frm = prie_form(request.POST or None, instance=obj)

        # Check if the form is valid
        if frm.is_valid():
            # If the form is valid, save the updated priest information to the database
            frm.save()
            # Redirect to the priest insertion page after saving
            return HttpResponseRedirect("/Adhome/insert_priest")

    except Exception as ex:
        # Handle any unexpected exceptions
        # Display an error message using Django's messaging framework
        messages.error(request, f"An error occurred while updating the priest information: {str(ex)}")
        # Optionally, you could log the error or handle it differently

    # Add the form to the context dictionary for rendering the template
    context['priest_data'] = frm

    # Render the update priest template with the current context
    return render(request, "updatepriest.html", context)


def delete_priest(request, pid):
    context = {}

    try:
        # Fetch the priest object by ID, or return a 404 error if not found
        obj = get_object_or_404(priest_model, id=pid)

        # Delete the priest object from the database
        obj.delete()

        # Redirect to the priest insertion page after deletion
        return HttpResponseRedirect("/Adhome/insert_priest")

    except Exception as ex:
        # Handle any unexpected exceptions
        # Display an error message using Django's messaging framework
        messages.error(request, f"An error occurred while deleting the priest: {str(ex)}")
        # Optionally, you could log the error or handle it differently

        # Redirect to the priest insertion page even if there's an error
        return HttpResponseRedirect("/Adhome/insert_priest")


def insert_pooja(request):
    context = {}

    try:
        # Initialize the pooja form with POST data and files if available
        frm = pooja_form(request.POST or None, request.FILES)

        # Retrieve the pooja type ID from the POST data
        pooja = request.POST.get('poojatypeid')
        poojaname=request.POST.get('pname')



        # Check if a pooja with the same type ID already exists
        if pooja_model.objects.filter(poojatypeid=pooja,pname='poojaname').exists():
            # If it exists, show an info message to the user
            messages.info(request, 'Pooja Already Exists')
            # Redirect the user back to the pooja insertion page
            return redirect('/Adhome/insert_pooja')

        else:
            # If the pooja does not exist, check if the form is valid
            if frm.is_valid():
                # If valid, save the pooja information to the database
                frm.save()
                # Redirect to the pooja insertion page after saving
                return redirect('/Adhome/insert_pooja')

    except Exception as ex:
        # Handle any unexpected exceptions
        # Display an error message using Django's messaging framework
        messages.error(request, f"An error occurred while inserting the pooja: {str(ex)}")
        # Optionally, you could log the error or handle it differently

    # Add the form and list of pooja types to the context dictionary
    context['f'] = frm
    context['pooja_list'] = pooja_model.objects.all()

    # Render the addpooja.html template with the current context
    return render(request, "addpooja.html", context)

def show_pooja(request):
    context = {}

    try:
        # Fetch all pooja records from the database
        context['pooja_list'] = pooja_model.objects.all()

    except Exception as ex:
        # Handle any unexpected exceptions
        # Display an error message using Django's messaging framework
        messages.error(request, f"An error occurred while fetching pooja information: {str(ex)}")
        # Optionally, you could log the error or handle it differently
        # Set an empty list in the context to avoid breaking the template
        context['pooja_list'] = []

    # Render the addpooja.html template with the current context, including the list of poojas
    return render(request, "addpooja.html", context)

def update_pooja(request, pid):
    context = {}

    try:
        # Fetch the pooja object by ID, or return a 404 error if not found
        obj = get_object_or_404(pooja_model, id=pid)

        # Initialize the form with POST data if available, and bind it to the existing pooja object
        frm = pooja_form(request.POST or None,request.FILES or None, instance=obj)

        # Check if the form is valid
        if frm.is_valid():
            # If valid, save the updated pooja information to the database
            frm.save()
            # Redirect to the pooja insertion page after saving
            return HttpResponseRedirect("/Adhome/insert_pooja")

    except Exception as ex:
        # Handle any unexpected exceptions
        # Display an error message using Django's messaging framework
        messages.error(request, f"An error occurred while updating the pooja: {str(ex)}")
        # Optionally, you could log the error or handle it differently

    # Add the form to the context dictionary for rendering the template
    context['pooja_data'] = frm

    # Render the update pooja template with the current context
    return render(request, "updatepooja.html", context)

def delete_pooja(request, pid):
    context = {}

    try:
        # Fetch the pooja object by ID, or return a 404 error if not found
        obj = get_object_or_404(pooja_model, id=pid)

        # Delete the pooja object from the database
        obj.delete()

        # Redirect to the pooja insertion page after deletion
        return HttpResponseRedirect("/Adhome/insert_pooja")

    except Exception as ex:
        # Handle any unexpected exceptions
        # Display an error message using Django's messaging framework
        messages.error(request, f"An error occurred while deleting the pooja: {str(ex)}")
        # Optionally, you could log the error or handle it differently

        # Redirect back to the pooja insertion page in case of an error
        return HttpResponseRedirect("/Adhome/insert_pooja")

def insert_day(request):
    context = {}

    try:
        # Initialize the form with POST data if available
        frm = day_form(request.POST or None)

        # Get the day value from the POST data
        day = request.POST.get('day')

        # Check if the day already exists in the database
        if day_model.objects.filter(day=day).exists():
            # If it exists, show an informational message to the user
            messages.info(request, 'This Day Already Exists')
            # Redirect to the insert day page
            return redirect('/Adhome/insert_day')
        else:
            # If the form is valid, save the new day to the database
            if frm.is_valid():
                frm.save()
                # Redirect to the insert day page after saving
                return redirect('/Adhome/insert_day')

        # Add the form to the context dictionary
        context['f'] = frm
        # Fetch all existing days to display in the template
        context['day_list'] = day_model.objects.all()

    except Exception as ex:
        # Handle any unexpected exceptions
        # Display an error message using Django's messaging framework
        messages.error(request, f"An error occurred while inserting the day: {str(ex)}")
        # Optionally, you could log the error or handle it differently

        # Ensure the form and day list are still available in the context
        context['f'] = frm
        context['day_list'] = day_model.objects.all()

    # Render the addday.html template with the current context
    return render(request, "addday.html", context)

def show_day(request):
    context = {}

    try:
        # Fetch all day records from the day_model
        # The result is stored in the context dictionary under the key 'day_list'
        context['day_list'] = day_model.objects.all()
    except Exception as ex:
        # Handle any unexpected exceptions during the data retrieval process
        # Display an error message using Django's messaging framework
        messages.error(request, f"An error occurred while fetching day information: {str(ex)}")

        # To avoid breaking the template, set 'day_list' to an empty list if an exception occurs
        context['day_list'] = []

    # Render the 'addday.html' template with the context that includes the list of days
    return render(request, "addday.html", context)

def update_day(request, did):
    context = {}

    try:
        # Fetch the day object by ID, or return a 404 error if not found
        obj = get_object_or_404(day_model, id=did)

        # Initialize the form with POST data if available, and bind it to the existing day object
        frm = day_form(request.POST or None, instance=obj)

        # Check if the form is valid
        if frm.is_valid():
            # If valid, save the updated day information to the database
            frm.save()
            # Redirect to the day insertion page after saving
            return HttpResponseRedirect("/Adhome/insert_day")

    except Exception as ex:
        # Handle any unexpected exceptions
        # Display an error message using Django's messaging framework
        messages.error(request, f"An error occurred while updating the day: {str(ex)}")
        # Optionally, you could log the error or handle it differently

    # Add the form to the context dictionary for rendering the template
    context['day_data'] = frm

    # Render the update day template with the current context
    return render(request, "updateday.html", context)

def delete_day(request, did):
    context = {}

    try:
        # Fetch the day object by ID, or return a 404 error if not found
        obj = get_object_or_404(day_model, id=did)

        # Delete the day object from the database
        obj.delete()

        # Redirect to the day insertion page after deletion
        return HttpResponseRedirect("/Adhome/insert_day")

    except Exception as ex:
        # Handle any unexpected exceptions
        # Display an error message using Django's messaging framework
        messages.error(request, f"An error occurred while deleting the day: {str(ex)}")
        # Optionally, you could log the error or handle it differently

        # Redirect back to the day insertion page in case of an error
        return HttpResponseRedirect("/Adhome/insert_day")

def insert_transf(request):
    context = {}

    try:
        # Initialize the form with POST data if available
        frm = transf_form(request.POST or None)

        # Get the transaction mode from the POST data
        trans = request.POST.get('transmode')

        # Check if the transaction mode already exists in the database
        if transtype_model.objects.filter(transmode=trans).exists():
            # If it exists, show an informational message to the user
            messages.info(request, 'This Transaction Mode Already Exists')
            # Redirect to the insert transaction mode page
            return redirect('/Adhome/insert_transf')
        else:
            # If the form is valid, save the new transaction mode to the database
            if frm.is_valid():
                frm.save()
                # Redirect to the insert transaction mode page after saving
                return redirect('/Adhome/insert_transf')

        # Add the form and transaction modes list to the context
        context['f'] = frm
        context['trans_list'] = transtype_model.objects.all()

    except Exception as ex:
        # Handle any unexpected exceptions
        # Display an error message using Django's messaging framework
        messages.error(request, f"An error occurred while inserting the transaction mode: {str(ex)}")
        # Optionally, you could log the error or handle it differently

        # Ensure the form and transaction modes list are still available in the context
        context['f'] = frm
        context['trans_list'] = transtype_model.objects.all()

    # Render the addtrans.html template with the current context
    return render(request, "addtrans.html", context)


def show_transf(request):
    context = {}

    try:
        # Fetch all transaction modes from the database
        context['trans_list'] = transtype_model.objects.all()

        # Render the addtrans.html template with the transaction modes list
        return render(request, "addtrans.html", context)

    except Exception as ex:
        # Handle any unexpected exceptions
        # Display an error message using Django's messaging framework
        messages.error(request, f"An error occurred while retrieving transaction modes: {str(ex)}")
        # Optionally, you could log the error or handle it differently

        # Redirect to a safe page or re-render the same template with an error message
        return redirect('/Adhome/insert_transf')

def update_trans(request, tid):
    context = {}

    try:
        # Fetch the transaction mode object by ID, or return a 404 error if not found
        obj = get_object_or_404(transtype_model, id=tid)

        # Initialize the form with POST data if available, and bind it to the existing transaction mode object
        frm = transf_form(request.POST or None, instance=obj)

        # Check if the form is valid
        if frm.is_valid():
            # If valid, save the updated transaction mode information to the database
            frm.save()
            # Redirect to the transaction mode insertion page after saving
            return HttpResponseRedirect("/Adhome/insert_transf")

        # Add the form to the context dictionary for rendering the template
        context['trans_data'] = frm

    except Exception as ex:
        # Handle any unexpected exceptions
        # Display an error message using Django's messaging framework
        messages.error(request, f"An error occurred while updating the transaction mode: {str(ex)}")
        # Optionally, you could log the error or handle it differently

        # Add the form to the context to allow the user to correct errors
        context['trans_data'] = frm

    # Render the update transaction mode template with the current context
    return render(request, "updatetrans.html", context)

def delete_trans(request, tid):
    context = {}

    try:
        # Fetch the transaction mode object by ID, or return a 404 error if not found
        obj = get_object_or_404(transtype_model, id=tid)

        # Delete the transaction mode object from the database
        obj.delete()

        # Redirect to the transaction mode insertion page after deletion
        return HttpResponseRedirect("/Adhome/insert_transf")

    except Exception as ex:
        # Handle any unexpected exceptions
        # Display an error message using Django's messaging framework
        messages.error(request, f"An error occurred while deleting the transaction mode: {str(ex)}")
        # Optionally, you could log the error or handle it differently

        # Redirect to a safe page or re-render the same template with an error message
        return redirect('/Adhome/insert_transf')

def insert_income(request):
    context = {}

    try:
        # Initialize the form with POST data if available
        frm = income_form(request.POST or None)

        # Get the income type from the POST data
        income = request.POST.get('inctype')

        # Check if the income type already exists in the database
        if income_model.objects.filter(inctype=income).exists():
            # If it exists, show an informational message to the user
            messages.info(request, 'Income Already Exists')
            # Redirect to the insert income page
            return redirect('/Adhome/insert_income')
        else:
            # If the form is valid, save the new income information to the database
            if frm.is_valid():
                frm.save()
                # Redirect to the insert income page after saving
                return redirect('/Adhome/insert_income')

        # Add the form and income list to the context
        context['f'] = frm
        context['income_list'] = income_model.objects.all()

    except Exception as ex:
        # Handle any unexpected exceptions
        # Display an error message using Django's messaging framework
        messages.error(request, f"An error occurred while inserting income: {str(ex)}")
        # Optionally, you could log the error or handle it differently

        # Ensure the form and income list are still available in the context
        context['f'] = frm
        context['income_list'] = income_model.objects.all()

    # Render the addincome.html template with the current context
    return render(request, "addincome.html", context)

def show_income(request):
    context = {}

    try:
        # Fetch all income records from the database
        context['income_list'] = income_model.objects.all()

        # Render the addincome.html template with the income list
        return render(request, "addincome.html", context)

    except Exception as ex:
        # Handle any unexpected exceptions
        # Display an error message using Django's messaging framework
        messages.error(request, f"An error occurred while retrieving income records: {str(ex)}")
        # Optionally, you could log the error or handle it differently

        # Redirect to a safe page or render the same template with an error message
        return redirect('/Adhome/insert_income')

def update_income(request, iid):
    context = {}

    try:
        # Fetch the income record by ID, or return a 404 error if not found
        obj = get_object_or_404(income_model, id=iid)

        # Initialize the form with POST data if available, and bind it to the existing income object
        frm = income_form(request.POST or None, instance=obj)

        # Check if the form is valid
        if frm.is_valid():
            # Save the updated income information to the database
            frm.save()
            # Redirect to the income insertion page after saving
            return HttpResponseRedirect("/Adhome/insert_income")

        # Add the form to the context for rendering the template
        context['income_data'] = frm

    except Exception as ex:
        # Handle any unexpected exceptions
        # Display an error message using Django's messaging framework
        messages.error(request, f"An error occurred while updating the income record: {str(ex)}")
        # Optionally, you could log the error or handle it differently

        # Ensure the form is still available in the context
        context['income_data'] = frm

    # Render the updateincome.html template with the current context
    return render(request, "updateincome.html", context)

def delete_income(request, iid):
    context = {}

    try:
        # Fetch the income record by ID, or return a 404 error if not found
        obj = get_object_or_404(income_model, id=iid)

        # Delete the income record from the database
        obj.delete()

        # Redirect to the income insertion page after deletion
        return HttpResponseRedirect("/Adhome/insert_income")

    except Exception as ex:
        # Handle any unexpected exceptions
        # Display an error message using Django's messaging framework
        messages.error(request, f"An error occurred while deleting the income record: {str(ex)}")

        # Optionally, redirect to a safe page or render the same template with an error message
        return redirect('/Adhome/insert_income')

def insert_month(request):
    context = {}

    try:
        # Initialize the form with POST data if available
        frm = month_form(request.POST or None)

        # Get the month value from the POST data
        mont = request.POST.get('Month')

        # Check if a record with the same month already exists
        if month_model.objects.filter(Month=mont).exists():
            messages.info(request, 'Month Already Exists')
            # Redirect to the same page to inform the user
            return redirect('/Adhome/insert_month')
        else:
            # If the form is valid, save the new month record
            if frm.is_valid():
                frm.save()
                # Redirect to the same page after saving
                return redirect('/Adhome/insert_month')

        # Add the form and existing month records to the context
        context['f'] = frm
        context['month_list'] = month_model.objects.all()

    except Exception as ex:
        # Handle any unexpected exceptions
        # Display an error message using Django's messaging framework
        messages.error(request, f"An error occurred while inserting the month record: {str(ex)}")
        # Ensure the form and existing month records are still available in the context
        context['f'] = frm
        context['month_list'] = month_model.objects.all()

    # Render the addmonth.html template with the current context
    return render(request, "addmonth.html", context)

def show_month(request):
    context = {}

    try:
        # Fetch all month records from the database
        context['month_list'] = month_model.objects.all()

    except Exception as ex:
        # Handle any unexpected exceptions
        # Display an error message using Django's messaging framework
        messages.error(request, f"An error occurred while retrieving month records: {str(ex)}")
        # Initialize month_list with an empty list to avoid errors in the template
        context['month_list'] = []

    # Render the addmonth.html template with the current context
    return render(request, "addmonth.html", context)

def update_month(request, mid):
    context = {}

    try:
        # Retrieve the month record by ID or return a 404 error if not found
        obj = get_object_or_404(month_model, id=mid)

        # Initialize the form with POST data and the existing instance
        frm = month_form(request.POST or None, instance=obj)

        # Check if the form is valid
        if frm.is_valid():
            frm.save()  # Save the updated record to the database
            return HttpResponseRedirect("/Adhome/insert_month")

        # Add the form to the context if the form is not valid
        context['month_data'] = frm

    except Exception as ex:
        # Handle any unexpected exceptions
        # Display an error message using Django's messaging framework
        messages.error(request, f"An error occurred while updating the month record: {str(ex)}")

        # Add the form to the context with the existing instance to allow correction
        context['month_data'] = frm

    # Render the updatemonth.html template with the current context
    return render(request, "updatemonth.html", context)

def delete_month(request, mid):
    context = {}

    try:
        # Retrieve the month record by ID or return a 404 error if not found
        obj = get_object_or_404(month_model, id=mid)

        # Delete the retrieved record
        obj.delete()

        # Redirect to the month insertion page after deletion
        return HttpResponseRedirect("/Adhome/insert_month")

    except Exception as ex:
        # Handle any unexpected exceptions
        # Display an error message using Django's messaging framework
        messages.error(request, f"An error occurred while deleting the month record: {str(ex)}")

        # Redirect to the month insertion page even if an error occurs
        return HttpResponseRedirect("/Adhome/insert_month")


def insert_expense(request):
    context = {}

    try:
        # Initialize the form with POST data
        frm = expense_form(request.POST or None)

        # Get the expense type from POST data
        exp = request.POST.get('Exptype')

        # Check if an expense with the same type already exists
        if expense_model.objects.filter(Exptype=exp).exists():
            messages.info(request, 'This Expense Type Already Exists')
            return redirect('/Adhome/insert_expense')

        # Check if the form is valid
        if frm.is_valid():
            frm.save()  # Save the new expense record to the database
            return redirect('/Adhome/insert_expense')

    except Exception as ex:
        # Handle any unexpected exceptions
        messages.error(request, f"An error occurred while inserting the expense: {str(ex)}")

    # Prepare context with the form and list of all expenses
    context['f'] = frm
    context['expense_list'] = expense_model.objects.all()

    # Render the template with the current context
    return render(request, "addexpense.html", context)

def show_expense(request):
    context = {}

    try:
        # Retrieve all expense records from the database
        context['expense_list'] = expense_model.objects.all()

    except Exception as ex:
        # Handle any unexpected exceptions
        # Display an error message using Django's messaging framework
        messages.error(request, f"An error occurred while retrieving the expense records: {str(ex)}")

        # Optionally, you can set an empty list to ensure the template doesn't break
        context['expense_list'] = []

    # Render the template with the current context
    return render(request, "addexpense.html", context)

def update_expense(request, eid):
    context = {}

    try:
        # Retrieve the specific expense record by ID or return a 404 error if not found
        obj = get_object_or_404(expense_model, id=eid)

        # Initialize the form with POST data and the retrieved instance
        frm = expense_form(request.POST or None, instance=obj)

        # Check if the form is valid
        if frm.is_valid():
            frm.save()  # Save the updated expense record to the database
            return HttpResponseRedirect("/Adhome/insert_expense")

    except Exception as ex:
        # Handle any unexpected exceptions
        messages.error(request, f"An error occurred while updating the expense: {str(ex)}")

    # Prepare context with the form instance and render the update template
    context['expense_data'] = frm
    return render(request, "updateexpense.html", context)

def delete_expense(request, eid):
    try:
        # Retrieve the specific expense record by ID or return a 404 error if not found
        obj = get_object_or_404(expense_model, id=eid)

        # Delete the retrieved expense record
        obj.delete()

        # Redirect to the expense insertion page after successful deletion
        return HttpResponseRedirect("/Adhome/insert_expense")

    except Exception as ex:
        # Handle any unexpected exceptions
        messages.error(request, f"An error occurred while deleting the expense: {str(ex)}")

        # Redirect to the expense insertion page in case of error
        return HttpResponseRedirect("/Adhome/insert_expense")


def insert_schedule(request):
    context = {}

    try:
        # Initialize the form with POST data (if available)
        frm = schedule_form(request.POST or None)

        # Get POST data for validation
        pooja = request.POST.get('poojaid')
        day = request.POST.get('dayid')
        timings = request.POST.get('Timings')
        Temple_name= request.session["Temp_name"]
        temple_instance = templeinfo_model.objects.get(id=Temple_name)

        # Check if a schedule with the same details already exists
        if poojaschedule_model.objects.filter(dayid=day, poojaid=pooja, Timings=timings,Temple_name=Temple_name).exists():
            messages.info(request, 'This Schedule Already Exists')
            return redirect('/Adhome/insert_schedule')

        # If form is valid, save the new schedule
        if frm.is_valid():
            obj = frm.save()
            obj.Temple_name = temple_instance
            frm.save()
            return redirect('/Adhome/insert_schedule')

    except Exception as ex:
        # Handle any unexpected exceptions
        messages.error(request, f"An error occurred while inserting the schedule: {str(ex)}")

    # Prepare context with the form instance and existing schedules
    context['f'] = frm
    context['schedule_list'] = poojaschedule_model.objects.filter(Temple_name=Temple_name)

    # Render the template with the prepared context
    return render(request, "addschedule.html", context)

def show_schedule(request):
    context = {}

    try:
        # Retrieve all schedule records from the database
        context['schedule_list'] = poojaschedule_model.objects.all()

    except Exception as ex:
        # Handle any unexpected exceptions
        messages.error(request, f"An error occurred while retrieving the schedule list: {str(ex)}")
        # Optionally, you can redirect to a different page or render an error template here

    # Render the template with the prepared context
    return render(request, "addschedule.html", context)

def update_schedule(request, sid):
    context = {}
    obj = get_object_or_404(poojaschedule_model, id=sid)
    frm = schedule_form(request.POST or None, instance=obj)
    if frm.is_valid():
        frm.save()
        return redirect('/Adhome/insert_schedule')
    context['schedule_data'] = frm
    return render(request, "updateschedule.html", context)
def delete_schedule(request, sid):
    context = {}

    try:
        # Retrieve the schedule object or return a 404 if not found
        obj = get_object_or_404(poojaschedule_model, id=sid)

        # Delete the retrieved schedule object
        obj.delete()

        # Redirect to the schedule insertion page after deletion
        return HttpResponseRedirect("/Adhome/insert_schedule")

    except Exception as ex:
        # Handle any unexpected exceptions
        messages.error(request, f"An error occurred while deleting the schedule: {str(ex)}")

        # Optionally, redirect to a different page or render an error template here
        return HttpResponseRedirect("/Adhome/insert_schedule")


def insert_special(request):
    context = {}

    try:
        # Initialize the form with POST data (if available)
        frm = specialday_form(request.POST or None)

        # Retrieve the 'Title' field from the POST data
        special = request.POST.get('Title')
        Temple = request.session["Temp_name"]
        temple_instance = templeinfo_model.objects.get(id=Temple)

        # Check if an entry with the same title already exists
        if specialday_model.objects.filter(Title=special).exists():
            messages.info(request, 'This Title Already Exists')
            return redirect('/Adhome/insert_special')

        # If the form is valid, save the new special day entry
        if frm.is_valid():
            obj=frm.save()
            obj.Temple_name= temple_instance
            frm.save()
            return redirect('/Adhome/insert_special')

    except Exception as ex:
        # Handle any unexpected exceptions
        messages.error(request, f"An error occurred while inserting the special day: {str(ex)}")

    # Prepare context with the form instance and all special day entries
    context['f'] = frm
    context['special_list'] = specialday_model.objects.filter(Temple_name=Temple)

    # Render the template for adding a special day
    return render(request, "addspecial.html", context)

def show_special(request):
    context = {}
    try:
        # Fetch all special days from the database
        context['special_list'] = specialday_model.objects.all()
    except Exception as ex:
        # Handle any unexpected exceptions
        messages.error(request, f"An error occurred while fetching special days: {str(ex)}")

    # Render the template 'addspecial.html' with the special days data
    return render(request, "addspecial.html", context)

def update_special(request, sid):
    context = {}

    try:
        # Retrieve the special day record to be updated using the provided ID
        obj = get_object_or_404(specialday_model, id=sid)

        # Initialize the form with POST data or the existing record instance
        frm = specialday_form(request.POST or None, instance=obj)

        # Check if the form is valid
        if frm.is_valid():
            frm.save()  # Save the updated record
            return HttpResponseRedirect("/Adhome/insert_special")

    except Exception as e:
        # Handle any unexpected exceptions and display an error message
        messages.error(request, f"An error occurred while updating the special day: {e}")

    # Pass the form to the context if the form is invalid or an error occurred
    context['special_data'] = frm

    # Render the template with the context data
    return render(request, "updatespecial.html", context)

def delete_special(request, sid):
    context = {}

    try:
        # Fetch the special day object based on the provided ID (sid)
        obj = get_object_or_404(specialday_model, id=sid)

        # Delete the fetched special day object from the database
        obj.delete()

        # Redirect the user to the insert_special page after successful deletion
        return HttpResponseRedirect("/Adhome/insert_special")

    except specialday_model.DoesNotExist:
        # Handle the case where the special day object does not exist
        messages.error(request, "The special day you are trying to delete does not exist.")
        return redirect('/Adhome/insert_special')

    except Exception as ex:
        # Handle any other unexpected exceptions
        messages.error(request, f"An error occurred while deleting the special day: {str(ex)}")
        return redirect('/Adhome/insert_special')


def insert_careers(request):
    context = {}

    try:
        # Initialize the careers form with POST data, if any
        frm = careers_form(request.POST or None, request.FILES)

        # Retrieve the reference number from the POST data
        careers = request.POST.get('Refno')
        jobtitle = request.POST.get('Jobtitle')

        # Check if a career entry with the same reference number already exists
        if careers_model.objects.filter(Refno=careers,Jobtitle=jobtitle).exists():
            messages.info(request, 'This Reference Id Already Exists')
            return redirect('/Adhome/insert_careers')
        else:
            # If the form is valid, save the new career entry
            if frm.is_valid():
                frm.save()
                return redirect('/Adhome/insert_careers')

        # Add the form and existing careers list to the context for rendering
        context['f'] = frm
        context['careers_list'] = careers_model.objects.all()

    except Exception as ex:
        # Handle any unexpected errors
        messages.error(request, f"An error occurred while inserting the career entry: {str(ex)}")
        return redirect('/Adhome/insert_careers')

    # Render the addcareers.html template with the provided context
    return render(request, "addcareers.html", context)

def show_careers(request):
    context = {}
    try:
        # Retrieve all career records from the database
        context['careers_list'] = careers_model.objects.all()
    except Exception as e:
        # Handle any unexpected exceptions and display an error message
        messages.error(request, f"An error occurred while fetching careers: {e}")
        context['careers_list'] = []  # Return an empty list in case of error

    # Render the template with the context data
    return render(request, "addcareers.html", context)

def update_careers(request, cid):
    context = {}

    try:
        # Fetch the career object by ID, or return a 404 error if not found
        obj = get_object_or_404(careers_model, id=cid)

        # Initialize the form with POST data if available, and bind it to the existing career object
        frm = careers_form(request.POST or None, instance=obj)

        # Check if the form is valid
        if frm.is_valid():
            # If the form is valid, save the updated career information to the database
            frm.save()
            # Redirect to the career insertion page after saving
            return HttpResponseRedirect("/Adhome/insert_careers")

    except Exception as ex:
        # Handle any unexpected exceptions
        # Display an error message using Django's messaging framework
        messages.error(request, f"An error occurred while updating the career information: {str(ex)}")
        # Optionally, you could log the error or handle it differently

    # Add the form to the context dictionary for rendering the template
    context['careers_data'] = frm

    # Render the update careers template with the current context
    return render(request, "updatecareers.html", context)

def delete_careers(request, cid):
    context = {}

    try:
        # Fetch the career object by ID, or return a 404 error if not found
        obj = get_object_or_404(careers_model, id=cid)

        # Delete the fetched career object
        obj.delete()

        # Redirect to the career insertion page after deletion
        return HttpResponseRedirect("/Adhome/insert_careers")

    except Exception as ex:
        # Handle any unexpected exceptions
        # Display an error message using Django's messaging framework
        messages.error(request, f"An error occurred while deleting the career: {str(ex)}")
        # Optionally, you could log the error or handle it differently

        # Redirect to the career insertion page to show the error
        return HttpResponseRedirect("/Adhome/insert_careers")



def insert_darshan(request):
    context = {}

    try:
        # Initialize the form with POST data if available
        frm = darsh_form(request.POST or None)

        # Retrieve the darshan time from the POST request
        day = request.POST.get('Day')
        Temple_name =request.session["Temp_name"]
        temple_instance = templeinfo_model.objects.get(id=Temple_name)


        # Check if a darshan record with the same time already exists
        if darshan_model.objects.filter(Day=day , Temple_name=temple_instance).exists():
            messages.info(request, 'This darshan time already exists')
            return redirect('/Adhome/insert_darshan')
        else:
            # If the form is valid, save the new darshan record
            if frm.is_valid():
                obj=frm.save()
                obj.Temple_name=temple_instance
                obj.save()
                return redirect('/Adhome/insert_darshan')

    except Exception as ex:
        # Handle any unexpected exceptions
        messages.error(request, f"An error occurred while inserting the darshan record: {str(ex)}")

    # Pass the form and the list of existing darshan records to the context
    context['f'] = frm
    context['darshan_list'] = darshan_model.objects.filter(Temple_name=Temple_name)

    # Render the template with the context data
    return render(request, "adddarshan.html", context)


def show_darshan(request):
    context = {}

    try:
        # Retrieve all darshan records from the database
        context['darshan_list'] = darshan_model.objects.all()

    except Exception as ex:
        # Handle any unexpected exceptions
        messages.error(request, f"An error occurred while fetching darshan records: {str(ex)}")

    # Render the template with the context data
    return render(request, "adddarshan.html", context)

def update_darshan(request, did):
    context = {}

    try:
        # Fetch the darshan object by ID, or return a 404 error if not found
        obj = get_object_or_404(darshan_model, id=did)

        # Initialize the form with POST data if available, and bind it to the existing darshan object
        frm = darsh_form(request.POST or None, instance=obj)

        # Check if the form is valid
        if frm.is_valid():
            # Save the updated darshan information to the database
            frm.save()
            # Redirect to the darshan insertion page after saving
            return HttpResponseRedirect("/Adhome/insert_darshan")

    except Exception as ex:
        # Handle any unexpected exceptions
        # Display an error message using Django's messaging framework
        messages.error(request, f"An error occurred while updating the darshan: {str(ex)}")

    # Add the form to the context dictionary for rendering the template
    context['dars_data'] = frm

    # Render the update darshan template with the current context
    return render(request, "updatedarshan.html", context)

def delete_darshan(request, did):
    try:
        # Retrieve the darshan object by ID, or return a 404 error if not found
        obj = get_object_or_404(darshan_model, id=did)

        # Delete the retrieved darshan object
        obj.delete()

        # Redirect to the darshan insertion page after deletion
        return HttpResponseRedirect("/Adhome/insert_darshan")

    except Exception as ex:
        # Handle any unexpected exceptions
        # Display an error message using Django's messaging framework
        messages.error(request, f"An error occurred while deleting the darshan: {str(ex)}")

        # Redirect back to the darshan insertion page in case of error
        return HttpResponseRedirect("/Adhome/insert_darshan")


def view_enquiry(request):
    context = {}

    try:
        # Attempt to retrieve all enquiries with 'new' status from the database
        context['enq_list'] = enquiry_model.objects.filter(Status='new')

    except Exception as ex:
        # Handle any unexpected exceptions
        messages.error(request, f"An error occurred while fetching enquiries: {str(ex)}")

    # Render the template with the context data
    return render(request, "viewenquiry.html", context)




def more_enquiry(request, enid):
    if request.method == "POST":
        try:
            obj = get_object_or_404(enquiry_model, id=enid)

            # Update the status of the enquiry to 'read'
            obj.Status = 'read'
            obj.save()  # Save the changes to the database

            # Email sending logic
            with get_connection(
                host=settings.EMAIL_HOST,
                port=settings.EMAIL_PORT,
                username=settings.EMAIL_HOST_USER,
                password=settings.EMAIL_HOST_PASSWORD,
                use_tls=settings.EMAIL_USE_TLS
            ) as connection:
                subject = request.POST.get("subject")
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [request.POST.get("email")]
                message = request.POST.get("message")
                EmailMessage(subject, message, email_from, recipient_list, connection=connection).send()
            return HttpResponse(
                "<script>alert('Email sent successfully!');window.location='/Adhome/view_enquiry';</script>")


        except Exception as e:
            print(f"Error sending email: {e}")
            return HttpResponse(f"Failed to send email: {e}")

    else:
        # Fetch the enquiry details to pre-fill the form
        obj = get_object_or_404(enquiry_model, id=enid)
        context = {
            'enid': enid,
            'email': obj.Email,  # Fetch the email
            'query': obj.Query,   # Fetch the query
        }
        return render(request, 'Activate_enquiry.html', context)


def delete_enquiry(request, eid):
    context = {}

    try:
        # Fetch the enquiry object by ID, or return a 404 error if not found
        obj = get_object_or_404(enquiry_model, id=eid)

        # Delete the enquiry object from the database
        obj.delete()

        # Redirect to the show enquiry page after deletion
        return HttpResponseRedirect("/Adhome/view_enquiry")

    except Exception as ex:
        # Handle any unexpected exceptions
        messages.error(request, f"An error occurred while deleting the enquiry: {str(ex)}")

        # Redirect to the show enquiry page in case of an error
        return HttpResponseRedirect("/Adhome/view_enquiry")


def view_application(request):
    context = {}

    try:
        # Retrieve all application records with related 'Devotee_id' and 'careerid' to optimize database access
        context["view_appli"] = application_model.objects.prefetch_related('Devotee_id', 'careerid')

    except Exception as ex:
        # Handle any unexpected exceptions
        messages.error(request, f"An error occurred while fetching application records: {str(ex)}")

    # Render the template with the context data
    return render(request, "showapplication.html", context)


def insert_poojatype(request):
    context = {}

    try:
        # Initialize the form with POST data and files if available
        frm = poojatype_form(request.POST or None, request.FILES)

        # Get the pooja type from POST data
        pooja = request.POST.get('Pooja_type')

        # Check if the pooja type already exists in the database
        if poojatype_model.objects.filter(Pooja_type=pooja).exists():
            messages.info(request, 'Pooja Type Already Exists')
            return redirect('/Adhome/insert_poojatype')
        else:
            # If the form is valid, save the new pooja type record
            if frm.is_valid():
                frm.save()
                return redirect('/Adhome/insert_poojatype')

    except Exception as ex:
        # Handle any unexpected exceptions
        messages.error(request, f"An error occurred while inserting pooja type: {str(ex)}")

    # Pass the form and existing pooja type records to the context
    context['f'] = frm
    context['poojatype_list'] = poojatype_model.objects.all()

    # Render the template with the context data
    return render(request, "addpoojatype.html", context)

def show_poojatype(request):
    context = {}

    try:
        # Retrieve all pooja type records from the database
        context['poojatype_list'] = poojatype_model.objects.all()

    except Exception as ex:
        # Handle any unexpected exceptions
        messages.error(request, f"An error occurred while fetching pooja types: {str(ex)}")

    # Render the template with the context data
    return render(request, "addpoojatype.html", context)

def update_poojatype(request, pid):
    context = {}

    try:
        # Retrieve the pooja type object by ID or return a 404 error if not found
        obj = get_object_or_404(poojatype_model, id=pid)

        # Initialize the form with POST data if available, and bind it to the existing pooja type object
        frm = poojatype_form(request.POST or None,request.FILES,instance=obj)

        # Check if the form is valid
        if frm.is_valid():
            # If the form is valid, save the updated pooja type information to the database
            frm.save()
            # Redirect to the pooja type insertion page after saving
            return HttpResponseRedirect("/Adhome/insert_poojatype")

    except Exception as ex:
        # Handle any unexpected exceptions
        # Display an error message using Django's messaging framework
        messages.error(request, f"An error occurred while updating the pooja type: {str(ex)}")

    # Add the form to the context dictionary for rendering the template
    context['poojatype_data'] = frm

    # Render the update pooja type template with the current context
    return render(request, "updatepoojatype.html", context)


def delete_poojatype(request, pid):
    context = {}

    try:
        # Retrieve the pooja type object by ID, or return a 404 error if not found
        obj = get_object_or_404(poojatype_model, id=pid)

        # Delete the retrieved object from the database
        obj.delete()

        # Redirect to the pooja type insertion page after deletion
        return HttpResponseRedirect("/Adhome/insert_poojatype")

    except Exception as ex:
        # Handle any unexpected exceptions
        # Display an error message using Django's messaging framework
        messages.error(request, f"An error occurred while deleting the pooja type: {str(ex)}")

    # Optionally, you could also render a template or return a different response in case of an error
    return HttpResponseRedirect("/Adhome/insert_poojatype")
