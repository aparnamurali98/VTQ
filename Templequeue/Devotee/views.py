from datetime import date
from time import timezone

import django.utils.timezone
from MySQLdb.constants.FIELD_TYPE import NULL
from django.contrib import messages
from django.db.models import Sum, Prefetch
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

from Adminhome.models import priest_model


# Create your views here.
def home (request):
    context = {}
    context['careers_list'] = careers_model.objects.all()
    context['special_day'] = specialday_model.objects.all()

    return render(request, "customerhome.html",context)
    # return HttpResponse("<a href='show_staff'>view staff</a>"
    #                    "<br><br><a href='show_templeinfo'> view templeinfo</a>"
    #                     "<br><br><a href='show_schedule'> view schedule</a>"
    #                     "<br><br><a href='show_special'> view special</a>"
    #                     "<br><br><a href='show_income'> viewincome</a>"
    #                     "<br><br><a href='show_careers'> view careers</a>"
    #                     "<br><br><a href='show_darshan'> view darshan timing</a>"
    #
    #                     "<br><br><a href='search_temple'>Search tempe</a>"
    #                     "<br><br><a href='show_pooja'>show_pooja </a>"
    #                     "<br><br><a href='index'>index </a>"
    #                     )


def show_staff(request):
    context = {}

    try:
        # Retrieve all staff records from the database
        context['staff_list'] = staff_model.objects.all()

    except Exception as ex:
        # Handle any unexpected exceptions
        messages.error(request, f"An error occurred while fetching staff records: {str(ex)}")

    # Render the template with the context data
    return render(request, "showstaff.html", context)


def show_templeinfo(request):
    context = {}

    try:
        # Retrieve all temple information records from the database
        context['info_list'] = templeinfo_model.objects.all()

    except Exception as ex:
        # Handle any unexpected exceptions
        messages.error(request, f"An error occurred while fetching temple information: {str(ex)}")

    # Render the template with the context data
    return render(request, "vietemp.html", context)


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
    return render(request, "viewprie.html", context)



def show_schedule(request,temple_id):
    context = {}

    try:
        temple = templeinfo_model.objects.get(id=temple_id)
        schedule_list = poojaschedule_model.objects.filter(Temple_name=temple)
        # Retrieve all schedule records from the database
        context['temple'] = temple
        context['schedule_list'] = schedule_list

    except Exception as ex:
        # Handle any unexpected exceptions
        messages.error(request, f"An error occurred while fetching the schedule records: {str(ex)}")

    # Render the template with the context data
    return render(request, "viewchedule.html", context)



def show_special(request):
    context = {}

    try:
        # Retrieve all special day records from the database
        context['special_list'] = specialday_model.objects.all()

    except Exception as ex:
        # Handle any unexpected exceptions
        messages.error(request, f"An error occurred while fetching special day records: {str(ex)}")

    # Render the template with the context data
    return render(request, "viewspecial.html", context)

def show_income(request):
    context = {}

    try:
        # Retrieve all income records from the database
        context['income_list'] = income_model.objects.all()

    except Exception as ex:
        # Handle any unexpected exceptions
        messages.error(request, f"An error occurred while fetching income records: {str(ex)}")

    # Render the template with the context data
    return render(request, "viewincome.html", context)

def show_careers(request):
    context = {}

    try:
        # Retrieve all career records from the database
        context['careers_list'] = careers_model.objects.all()

    except Exception as ex:
        # Handle any unexpected exceptions
        messages.error(request, f"An error occurred while fetching career records: {str(ex)}")

    # Render the template with the context data
    return render(request, "viewcareers.html", context)




def show_darshan(request,temple_id):
    context = {}

    try:
        temple = templeinfo_model.objects.get(id=temple_id)
        darshan_list = darshan_model.objects.filter(Temple_name=temple)
        # Retrieve all schedule records from the database
        context['temple'] = temple
        context['darshan_list'] = darshan_list

    except Exception as ex:
        # Handle any unexpected exceptions
        messages.error(request, f"An error occurred while fetching the schedule records: {str(ex)}")

    # Render the template with the context data
    return render(request, "viewdarshan.html", context)


def search_temple(request):
    context = {}

    try:
        # Initialize the form with POST data if available
        frm = location_form(request.POST or None)

        # Add the form to the context for rendering
        context['f'] = frm

    except Exception as ex:
        # Handle any unexpected exceptions
        messages.error(request, f"An error occurred while processing the search form: {str(ex)}")

    # Render the search temple template with the context data
    return render(request, "serachtemple.html", context)


# def search_temple1(request):
#     locid = request.GET.get('selected_value')
#     data = templeinfo_model.objects.filter(loc=locid)
#     data_list = [{'id':item.id ,'tname': item.tname, 'taddress': item.address, 'tdiscription': item.discription, 'tcotname': item.cotname, 'tPhoto': item.Photo.url} for item in data]
#     print(data_list)
#     return JsonResponse({'data': data_list})

def search_temple1(request):
    try:
        # Retrieve location ID from the GET request parameters
        locid = request.GET.get('selected_value')

        # Filter temple information based on the location ID
        data = templeinfo_model.objects.filter(loc=locid)

        # Create a list of dictionaries with selected temple details
        data_list = [
            {
                'id': item.id,
                'tname': item.tname,
                'taddress': item.address,
                'tdiscription': item.discription,
                'tcotname': item.cotname,
                'tPhoto': item.Photo.url
            }
            for item in data
        ]

        print(data_list)  # Print the list of temple data for debugging purposes

        # Return the data as a JSON response
        return JsonResponse({'data': data_list})

    except Exception as e:
        # Print error for debugging if an exception occurs
        print(f"An error occurred while searching for temples: {e}")


def insert_Application(request, cid):
    context = {}

    try:
        # Retrieve the devotee ID from the session
        did = request.session["devote_id"]
        devote_object = devotee_model.objects.get(id=did)  # Get the devotee object based on the ID
        print(did)

        # Get the career object based on the career ID (cid)
        careerid = careers_model.objects.get(id=cid)

        # Initialize the application form with POST data and files if available
        frm = application_form(request.POST or None, request.FILES or None)

        if request.POST:
            # If the form is valid, create a new application record
            if frm.is_valid():
                Resume = request.FILES.get('Resume')  # Get the uploaded resume file
                appli = application_model.objects.create(
                    careerid=careerid, Devotee_id=devote_object, Resume=Resume
                )
                return HttpResponseRedirect("/Devotee/")  # Redirect to the careers page after successful insertion

    except Exception as ex:
        # Handle any unexpected exceptions
        messages.error(request, f"An error occurred while inserting the application: {str(ex)}")

    # Pass the form to the context for rendering
    context['f'] = frm
    return render(request, "apply_career.html", context)




def show_pooja(request,id):
    context = {}
    count = 1  # Initialize the count variable

    try:
        # Retrieve the devotee ID from the session and get the corresponding devotee object
        did = request.session["devote_id"]
        devote_object = devotee_model.objects.get(pk=did)

        if request.method == 'POST':
            # Retrieve the selected pooja ID from the POST data
            pid = request.POST.get("poojaid")


            # Get the pooja object based on the ID
            pooja_object = pooja_model.objects.get(id=pid)

            # Get or create a bookingpooja object with the devotee and status 'New'
            book_obj, created = bookingpooja_model.objects.get_or_create(Devotee=devote_object, Status='New')

            # Increment the count
            count += 1

            # Get or create a poojabook object with the given details
            pooja, p_created = poojabook_model.objects.get_or_create(
                Devotee=devote_object, pooja=pooja_object, booking=book_obj, Name=count
            )

            # If the poojabook object was created, reset its Name and save it
            if p_created:
                pooja.Name = ''
                pooja.save()
                return redirect(Addtocart)

            else:
                pooja.Name = ''
                pooja.save()
                return redirect(Addtocart)

    except Exception as ex:
        # Handle any unexpected exceptions
        messages.error(request, f"An error occurred while processing the pooja booking: {str(ex)}")

    # Retrieve all pooja records and pass them to the context

    temple = templeinfo_model.objects.prefetch_related('Pooja').get(id=id)
    context["pooja_list"] = temple.Pooja.all()
    p=temple.Pooja.all()
    print(p,'p')
    request.session["temple_id"] =temple.id
    print(temple.id,'temple')



    # Render the template with the context data
    return render(request, "viewpooja1.html", context)


def Addtocart(request):
    context = {}

    try:
        # Retrieve the devotee ID from the session
        did = request.session["devote_id"]

        # Get the devotee object based on the ID
        devote_object = devotee_model.objects.get(pk=did)

        # Fetch pooja book list related to the devotee that are in the cart
        poojabook_list = poojabook_model.objects.select_related('pooja').filter(Devotee=devote_object, Status='cart')

        # Add the pooja book list to the context
        context['poojabook_list'] = poojabook_list

        # Calculate the subtotal of the pooja amounts
        subtotal = poojabook_list.aggregate(subtotal=Sum('pooja__amount'))['subtotal'] or 0

        # Add the subtotal to the context
        context['subtotal'] = subtotal
        context["today"] = date.today().isoformat()  # Pass today's date in YYYY-MM-DD format

    except Exception as e:
        # Handle exceptions and provide an error message in the context
        context['error'] = f"An error occurred: {str(e)}"
    context["temple_id"] = request.session["temple_id"]


        # Render the viewcart.html template with the context data
    return render(request, "viewcart.html", context)


def add_addtocart(request):
    context = {}
    try:
        # Retrieve devotee ID from session and get devotee object
        did = request.session["devote_id"]
        devote_object = devotee_model.objects.get(pk=did)

        # Get pooja ID from the POST request and retrieve the cart item for the devotee
        pooja = request.POST.get('poojaid')
        obj = get_object_or_404(poojabook_model, id=pooja, Devotee=devote_object, Status='cart')
        print(obj)  # Debug print to show the retrieved object

        if request.POST:
            # Retrieve name and star details from POST data
            print('name1')  # Debug print to indicate processing
            Dname = request.POST.get('Dname')
            print(Dname)  # Debug print to show retrieved name
            star = request.POST.get('star')

            # Update cart item with new name and star values
            obj.Name = Dname
            obj.star = star
            print('star', star)  # Debug print to show retrieved star value

            # Save the updated object
            obj.save()

            # Redirect to Add to Cart page after saving
            return HttpResponseRedirect('/Devotee/Addtocart')

    except Exception as e:
        # Handle any exception that occurs and print the error for debugging
        print(f"An error occurred while adding to the cart: {e}")


def delete_addtocart(request, poojaid):
    context = {}
    try:
        # Retrieve the pooja item by ID or raise a 404 error if not found
        obj = get_object_or_404(poojabook_model, id=poojaid)

        # Delete the retrieved pooja item from the cart
        obj.delete()

        # Redirect to the Add to Cart page after successful deletion
        return redirect(Addtocart)

    except Exception as e:
        # Handle any exceptions that occur and print the error for debugging
        print(f"An error occurred while deleting the item: {e}")


def Confirm_order(request):
    context = {}
    try:
        # Retrieve devotee ID from the session
        did = request.session["devote_id"]
        devote_object = devotee_model.objects.get(id=did)
        print(did)  # Debug: print the devotee ID

        if request.POST:  # Check if the form is submitted
            # Get booking date and total amount from the POST request
            Bookingdate = request.POST.get('bdate')
            total_amount = request.POST.get('amount')
            print(total_amount)  # Debug: print the total amount

            # Retrieve the booking record for the devotee with 'New' status
            bk = bookingpooja_model.objects.get(Devotee=devote_object, Status='New')
            pooja_book = get_object_or_404(bookingpooja_model, pk=bk.id)

            # Update booking details
            pooja_book.Want_date = Bookingdate
            pooja_book.Total_amount = total_amount
            pooja_book.Status = 'confirmed'
            pooja_book.save()

            # Update all 'cart' status items for the devotee to 'confirm'
            obj = poojabook_model.objects.filter(Status='cart', Devotee=devote_object)
            for poojaobject in obj:

                new_status = 'confirm' # Set new status
                poojaobject.Status = new_status
                poojaobject.save()

            # Redirect to payment page with booking ID and total amount
            url = reverse('payment', kwargs={'pid': bk.id, 'subtotal': total_amount})
            return redirect(url)

        # Redirect to Add to Cart page if no POST request
        return HttpResponseRedirect("/Devotee/Addtocart")

    except Exception as e:
        # Print error for debugging if an exception occurs
        print(f"An error occurred while confirming the order: {e}")


# def payment(request, pid, subtotal):
#     context = {}
#
#     try:
#         # Retrieve devotee ID from session
#         did = request.session["devote_id"]
#         devote_object = devotee_model.objects.get(id=did)
#
#         if request.method == 'POST':
#             # Get payment details from the POST request
#             card_type = request.POST.get('card_type')
#             card_holder_name = request.POST.get('card_holder_name')
#             card_number = request.POST.get('Card_number')
#             card_exp_date = request.POST.get('card_exp_date')
#             cvv_number = request.POST.get('cvv_number')
#             total_amount = subtotal  # Set total amount from the subtotal parameter
#             income_date = timezone.now()  # Get the current date and time
#             Narration = 'pooja booking'  # Set narration for the income entry
#             typeid = income_model.objects.get(pk=10)  # Get income type by ID
#
#             # Retrieve the pooja booking record by ID
#             pooja_booking = bookingpooja_model.objects.get(pk=pid)
#
#             # Create a payment record in the payment model
#             payment = payment_model.objects.create(
#                 poojabook=pooja_booking,
#                 card_type=card_type,
#                 card_holder_name=card_holder_name,
#                 Card_number=card_number,
#                 card_exp_date=card_exp_date,
#                 cvv_number=cvv_number,
#                 Total_amount=total_amount
#             )
#
#             # Create an income record in the incomes model
#             incomes = incomes_model.objects.create(
#                 Devotee=devote_object,
#                 Bookingpooja=pooja_booking,
#                 income_typeid=typeid,
#                 income_date=income_date,
#                 Amount=total_amount,
#                 Narration=Narration
#             )
#
#             # Redirect to the receipt page
#             url = reverse('receipt', kwargs={'pid': pid})
#             return redirect(url)
#
#         context['subtotal'] = subtotal  # Pass the subtotal to the template
#         return render(request, 'payment.html', context)
#
#     except Exception as e:
#         # Print error for debugging if an exception occurs
#         print(f"An error occurred during the payment process: {e}")
#         return render(request, 'payment.html', context)  # Optionally, render the payment page again

def payment(request, pid,subtotal):

    context = {}
    did = request.session["devote_id"]
    devote_object = devotee_model.objects.get(id=did)

    if request.method == 'POST':
        card_type = request.POST.get('card_type')
        card_holder_name = request.POST.get('card_holder_name')
        card_number = request.POST.get('Card_number')
        card_exp_date = request.POST.get('card_exp_date')
        cvv_number = request.POST.get('cvv_number')
        if not all([card_type, card_holder_name, card_number, card_exp_date, cvv_number]):
            messages.error(request, "All fields are required!")
            return redirect(request.path)
        total_amount = subtotal
        income_date=django.utils.timezone.now()
        Narration='pooja booking'
        typeid = income_model.objects.get(pk=10)
        pooja_booking = bookingpooja_model.objects.get(pk=pid)
        payment = payment_model.objects.create(poojabook=pooja_booking, card_type=card_type, card_holder_name=card_holder_name, Card_number=card_number, card_exp_date=card_exp_date, cvv_number=cvv_number, Total_amount=total_amount)
        incomes = incomes_model.objects.create(Devotee=devote_object,Bookingpooja=pooja_booking, income_typeid=typeid, income_date=income_date,Amount=total_amount, Narration=Narration)
        url = reverse('receipt', kwargs={'pid':pid })
        return redirect(url)

    context['subtotal'] = subtotal
    return render(request, 'payment.html', context)


def index(request):

    return render(request, 'index.html')

def receipt(request, pid):
    context = {}
    dt=NULL

    try:
        # Retrieve the devotee ID from the session
        did = request.session.get("devote_id")

        # Get the devotee object using the ID
        devote_object = devotee_model.objects.get(pk=did)

        # Retrieve the list of pooja bookings associated with the given booking ID (pid)
        poojabook_list = poojabook_model.objects.select_related('pooja', 'booking').filter(booking=pid)
        for obj in poojabook_list:
            dt= obj.booking.booked_date


        # Add the poojabook list to the context for rendering in the template
        context['poojabook_list'] = poojabook_list
        context['dt'] = dt
        print(dt,'date')

        # Calculate the subtotal of pooja amounts and handle the case where subtotal might be None
        subtotal = poojabook_list.aggregate(subtotal=Sum('pooja__amount'))['subtotal'] or 0
        context['subtotal'] = subtotal

        # Render the receipt template with the context data
        return render(request, "receipt.html", context)

    except devotee_model.DoesNotExist:
        # Handle the case where the devotee object is not found
        print("Devotee does not exist.")
        return render(request, "error.html", {"error": "Devotee not found."})

    except Exception as e:
        # Handle any other exceptions that may occur
        print(f"An error occurred: {str(e)}")
        return render(request, "error.html", {"error": "An error occurred while generating the receipt."})


