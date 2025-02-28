from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .enquiry_form import enquiry_form
from .models import devotee_model, role_model, enquiry_model
from Adminhome.models import location_model

from Adminhome.models import staff_model


# Create your views here.
def home (request):
    return redirect(login)
def insert_devotee(request):
    context={}
    if request.POST:
        try:
            devname=request.POST.get('dname')
            addre=request.POST.get('address')
            devage=request.POST.get('age')
            devgender=request.POST.get('gender')
            devstar = request.POST.get('star')
            devemail = request.POST.get('email')
            devmobile = request.POST.get('mobile')
            devusername  = request.POST.get('username')
            devupassword = request.POST.get('password')
            devuconfirm_password = request.POST.get('confirm_password')
            if devuconfirm_password==devupassword:

                devloc = request.POST.get('loc')
                print(devloc,'location')
                locid = location_model.objects.get(id=devloc)
                loginid=User.objects.create_user(username=devusername,password=devupassword)
                role=role_model.objects.create(login=loginid,roletype=2)
                devoteereg=devotee_model.objects.create(dname=devname,address=addre,age=devage,gender=devgender,star=devstar,email=devemail,mobile=devmobile,loc=locid,login=loginid)
                return HttpResponseRedirect('/login')
            else:
                messages.error(request,"password does not match")
        except Exception as ex:
            error_message="User Name Alredy Exists"
            # error_message = ex

            messages.error(request,error_message)
    context['loc'] =location_model.objects.all()
    return render(request,"adddevo.html",context)

def insert_enquiry(request):
    context = {}

    # Initialize the form with POST data if available, otherwise use None
    frm = enquiry_form(request.POST or None)

    # Get the 'Name' from the POST data
    enquiry = request.POST.get('Name')
    query = request.POST.get('Query')

    try:
        # Check if an enquiry with the same name already exists in the database
        if enquiry_model.objects.filter(Name=enquiry,Query=query).exists():
            # If it exists, show an info message to the user
            messages.info(request, 'This Query Already Exists')
            # Redirect the user back to the enquiry form
            return redirect('/login/insert_enquiry')
        else:
            # If the enquiry doesn't exist, check if the form is valid
            if frm.is_valid():
                # If the form is valid, save the form data to the database
                frm.save()
                # Redirect the user back to the enquiry form after saving
                return redirect('/login/insert_enquiry')

    except Exception as ex:
        # Handle any unexpected exceptions
        # Log the exception (optional) or show an error message
        messages.error(request, f"An error occurred: {str(ex)}")
        # You could also redirect to an error page or simply return to the form

    # Add the form to the context dictionary
    context['f'] = frm

    # Render the enquiry form page with the current context
    return render(request, "addenquiry.html", context)



def login(request):
    # Check if the request is a POST request
    if request.POST:
        context = {}

        # Retrieve username and password from the POST request
        Uname = request.POST.get('username')
        paswrd = request.POST.get('password')

        try:
            # Authenticate the user with the provided username and password
            user = authenticate(username=Uname, password=paswrd)

            # If authentication is successful
            if user is not None:
                user_id = user.id
                sp = user.is_superuser

                # If the user is a superuser, redirect to the admin home page
                if sp is True:
                    return HttpResponseRedirect('/Adhome')

                # Check the user's role in the role_model
                roll_obj = role_model.objects.filter(login=user_id)
                for role_obj in roll_obj:
                    type = role_obj.roletype
                    print(type)

                    # If the role type is '2', treat the user as a devotee
                    if type == '2':
                        devote_object = devotee_model.objects.filter(login=user_id)
                        for obj in devote_object:
                            # Set session variables for the devotee
                            request.session["devote_id"] = obj.id
                            request.session["devote_name"] = obj.dname

                            return HttpResponseRedirect('/Devotee')

                    # If the role type is '3', treat the user as a staff member
                    elif type == '3':
                        staff_object = staff_model.objects.filter(login=user_id)
                        for obj in staff_object:
                            # Set session variables for the staff member
                            request.session["staff_id"] = obj.id
                            request.session["staff_name"] = obj.sname
                            request.session["Temp_name"] =obj.Temple_name.id

                            return HttpResponseRedirect('/staff_home')

                        # If no valid role is found, return an invalid credential response
                        else:
                            return HttpResponse(
                                "<script>alert('Invalid Credential !!!');window.location='/login';</script>")

            # If authentication fails, return an invalid credential response
            else:
                return HttpResponse("<script>alert('Invalid Credential !!!');window.location='/login';</script>")

        except Exception as ex:
            # Handle any unexpected exceptions and display an error message
            return HttpResponse(f"<script>alert('An error occurred: {str(ex)}');window.location='/login';</script>")

    # Render the login page if the request is not a POST request
    return render(request, "login.html")





