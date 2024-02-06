from django.shortcuts import render
from django.http import HttpResponse,HttpRequest,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import StudentApplication
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render, redirect
from django.contrib import messages
from . forms import *
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
# Create your views here.


def home(request):
    form = StatusCheckForm()
    return render(request, 'home.html', {})
    




def application(request):
    if request.method == 'POST':
        form = StudentApplicationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Application submitted successfully.')
            return redirect('application')  # Redirect to a success page
        else:
            messages.error(request, 'Form submission failed. Please check the provided information.')
    else:
        # If it's a GET request, just create an empty form
        form = StudentApplicationForm()
       
        print(form.errors)

    context = {'form': form}
    return render(request, 'application.html', context)




def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)

        if user is not None and user.is_superuser:
            login(request,user)
            return render(request,'admin_dash.html')
    
         
    return render(request,'admin_login.html',{})

def addhostel(request):
    if  request.method=='POST':
        form=hostelform(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse_lazy('addhostel'))
        
    else:

        form=hostelform
    return render(request,'add_hostel.html',{'form':form})


def viewhostel(request):
    data=Hostels.objects.all()
    
    return render(request, 'viewhostel.html', {'data': data})


def edithostel(request, hostel_id):
    hostel = get_object_or_404(Hostels, id=hostel_id)

    if request.method == 'POST':
        print(request.POST) 
        hostel.hostelname = request.POST.get('hostelname')
        hostel.gender = request.POST.get('gender')
        hostel.level = request.POST.get('level')
        hostel.course = request.POST.get('course')
        hostel.no_rooms = request.POST.get('no_rooms')
        hostel.room_cap = request.POST.get('room_cap')
        hostel.mess = request.POST.get('mess')
        hostel.hostelfees = request.POST.get('hostelfees')
        # Update other fields similarly...

        hostel.save()
        return redirect('viewhostel')  # Redirect to the view_hostels page after saving

    return render(request, 'edithostel.html', {'hostel': hostel})

def delete_hostel(request, hostel_id):
    hostel = get_object_or_404(Hostels, id=hostel_id)
    hostel.delete()
    return redirect('viewhostel')


def add_depar(request):
    if  request.method=='POST':
        form=depform(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse_lazy('add_depar'))
        
    else:

        form=depform
    return render(request,'add_dep.html',{'form':form})


def view_dep(request):
    data=add_dep.objects.all()
    
    return render(request, 'view_dep.html', {'data': data})

def delete_department(request, dep_id):
    department = get_object_or_404(add_dep, id=dep_id)
    department.delete()
    return redirect('view_dep')


def edit_dep(request, dep_id):
    dep = get_object_or_404(add_dep, id=dep_id)

    if request.method == 'POST':
        print(request.POST) 
        dep.dep_name = request.POST.get('dep_name')
        dep.dep_contact = request.POST.get('dep_contact')
        dep.dep_email = request.POST.get('dep_email')
        
        dep.save()
        return redirect('view_dep')  # Redirect to the view_hostels page after saving

    return render(request, 'edit_dep.html', {'dep': dep})

def add_warden(request):
    if  request.method=='POST':
        form=wardenform(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse_lazy('add_warden'))
        
    else:

        form=wardenform
    
          
    return render(request,'add_warden.html',{'form':form})



def view_warden(request):
    data=warden.objects.all()
    
    return render(request, 'view_warden.html', {'data': data})
        

def edit_warden(request, warden_id):
    wardens = get_object_or_404(warden, id=warden_id)

    if request.method == 'POST':
        # Update the fields based on the form data
        wardens.warden_name = request.POST.get('warden_name')
        wardens.dep_name = request.POST.get('dep_name')
        wardens.contact = request.POST.get('contact')
        
        # Assuming hostel_id is an integer, you should convert it to int
        hostel_id = int(request.POST.get('hostel_id'))
        
        # Get the Hostel instance using the ID
        hostel = get_object_or_404(Hostels, id=hostel_id)
        
        # Assign the Hostel instance to the warden's hostel_id
        wardens.hostel_id = hostel

        wardens.user = request.POST.get('user')

        # Save the updated warden instance
        wardens.save()
        return redirect('view_warden')

    return render(request, 'edit_warden.html', {'wardens': wardens})


def delete_warden(request, warden_id):
    wardens = get_object_or_404(warden, id=warden_id)
    wardens.delete()
    return redirect('view_warden')




def warden_login(request):
    error_message = None

    if request.method == 'POST':
        contact = request.POST.get('contact')
        password = request.POST.get('password')

        try:
            user = warden.objects.get(contact=contact, password=password)
            hostel_id = user.hostel_id_id
            student_applications = StudentApplication.objects.filter(hostel_choice_id=hostel_id)

            if not student_applications.exists():
                error_message = "No student applications found for this warden's hostel."

            return render(request, 'warden_dash.html', {'form': student_applications, 'error_message': error_message})
        except warden.DoesNotExist:
            error_message = "Invalid username or password."

    return render(request, 'warden_login.html', {'error_message': error_message})





def add_gender(request):
    if  request.method=='POST':
        form=genderform(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse_lazy('gender_type'))
        
    else:

        form=genderform
    return render(request,'add_gender.html',{'form':form})


def add_course(request):
    if  request.method=='POST':
        form=courseform(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse_lazy('course_type'))
        
    else:

        form=courseform
    return render(request,'add_course.html',{'form':form})



def approve_application(request,stud_id):
  stud=StudentApplication.objects.get(id=stud_id)
  #if request.method=='POST':
  #stud= StudentApplication()
  print(stud.status)
  stud.status=1
  stud.save()
  form=StudentApplication.objects.all()
  messages.success(request, 'Application approved. ')
  return render(request,'warden_dash.html',{'form':form})



def reject_application(request,stud_id):
  stud=StudentApplication.objects.get(id=stud_id)
  #if request.method=='POST':
  #stud= StudentApplication()
  print(stud.status)
  stud.status=2
  stud.save()
  form=StudentApplication.objects.all()
  return render(request,'warden_dash.html',{'form':form})




@login_required
def warden_dash(request):
    
    
    return render(request, 'warden_dash.html')

def view_applications(request,hostel_id):

    hostel = get_object_or_404(Hostels, pk=hostel_id)
    form = StudentApplication.objects.filter(hostel_choice_id=hostel)

   

    
    return render(request, 'view_applications.html', {'form': form})






def room_allotment(request, hostel_id):
    hostel = get_object_or_404(Hostels, pk=hostel_id)
    form = StudentApplication.objects.filter(hostel_choice_id=hostel, status=1, fee_status=1, room_allotted=0)

    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        room_number = int(request.POST.get('room_number'))

        # Validate room number against the available number of rooms in the hostel
        if room_number < 1 or room_number > hostel.no_rooms:
            error_message = f"Invalid room number. Please enter a room number between 1 and {hostel.no_rooms}."
            return render(request, 'room_allotment.html', {'error_message': error_message, 'form': form, 'hostel': hostel})

        try:
            # Check if the student is already allotted a room
            existing_allotment = RoomAllotment.objects.filter(student_id=student_id).exists()
            if existing_allotment:
                error_message = "This student is already allotted a room."
                return render(request, 'room_allotment.html', {'error_message': error_message, 'form': form, 'hostel': hostel})

            # Create a RoomAllotment instance and save it to the database
            student = get_object_or_404(StudentApplication, pk=student_id)
            room_allotment = RoomAllotment(student=student, hostel=hostel, room_number=room_number)
            room_allotment.save()

            # Update the student's room_allotted field
            student.room_allotted = True
            student.save()

            # Create a success message
            success_message = "Room allotted successfully!"
            return render(request, 'room_allotment.html', {'success_message': success_message, 'form': form, 'hostel': hostel})

        except Exception as e:
            error_message = f"An error occurred during room allotment: {str(e)}"
            return render(request, 'room_allotment.html', {'error_message': error_message, 'form': form, 'hostel': hostel})

    else:
        return render(request, 'room_allotment.html', {'form': form, 'hostel': hostel})





def room_allotment_success(request):
    return render(request, 'room_allotment_success.html')




def check_status(request):
    if request.method == 'POST':
        form = StatusCheckForm(request.POST)
        if form.is_valid():
            mobile_number = form.cleaned_data['mobile_number']
            date_of_birth = form.cleaned_data['date_of_birth']

            # Check if the student with the provided mobile number and date of birth exists
            try:
                student = StudentApplication.objects.get(contact_number=mobile_number, date_of_birth=date_of_birth)
                if student.status == 1:
                    messages.success(request, 'Student application is approved.')
                    return redirect('payment', student_id=student.id)
                    
                else:
                    messages.warning(request, 'Student application is waiting or rejected.')
            except StudentApplication.DoesNotExist:
                messages.error(request, 'No student found with the provided details.')
    else:
        form = StatusCheckForm()

    return render(request, 'check_status.html', {'form': form})


def payment(request, student_id):
    student_application = get_object_or_404(StudentApplication, pk=student_id)

    if request.method == 'POST':
        challen_number = request.POST.get('challen_number')
        name = request.POST.get('name')

        # Assuming payment was successful and updating fee_status
        student_application.fee_status = 1
        student_application.save()

        # Save payment details
        payment_detail = PaymentDetailStudents(
            student=student_application,
            challen_number=challen_number,
            name=name,
            # Assuming you have a file input named 'challan_image' in your form
            challen_image=request.FILES['challen_image']
        )
        payment_detail.save()

        messages.success(request, 'Payment Successful!')
        return redirect('payment_success')

    return render(request, 'payment.html', {'student_application': student_application})


def payment_success(request):
    return HttpResponse('Payment Successful!')





def student_login(request):
    contact_number = None
    student_id = None

    if request.method == 'POST':
        room_number = request.POST.get('room_number')
        contact_number = request.POST.get('contact_number')

        try:
            # Get the RoomAllotment object for the given room number
            room_allotment = RoomAllotment.objects.get(room_number=room_number)

            # Get the student_id
            student_id = room_allotment.student.id
          
            # Check if the contact number matches
            if room_allotment.get_student_contact_number() == contact_number:
                # Set student's name and hostel in session
                request.session['student_name'] = room_allotment.student.full_name
                 
                request.session['room_number'] = room_allotment.room_number
                request.session['hostel_choice'] = room_allotment.student.hostel_choice_id

                messages.success(request, 'Login successful.')
                print(room_allotment.student.hostel_choice_id)
                return HttpResponseRedirect(f'/student_dashboard/{student_id}/')
            else:
                messages.error(request, 'Invalid contact number. Please try again.')
        except RoomAllotment.DoesNotExist:
            messages.error(request, 'Invalid room number. Please try again.')

    return render(request, 'student_login.html', {'contact_number': contact_number})





def student_dashboard(request, student_id):
    try:
        # Retrieve the student application
        student_application = get_object_or_404(StudentApplication, id=student_id)
        
        # Retrieve the room allotment associated with the student application
        room_allotment = get_object_or_404(RoomAllotment, student=student_application)

        # Access the student's name from StudentApplication
        student_name = student_application.full_name

        # Access the room number from RoomAllotment
        room_number = room_allotment.room_number
        
    except StudentApplication.DoesNotExist:
        return render(request, 'error.html', {'message': 'Student application not found.'})
    except RoomAllotment.DoesNotExist:
        return render(request, 'error.html', {'message': 'Room allotment not found.'})

    context = {
        'student_name': student_name,
        'room_number': room_number,
        # Add other context data as needed
    }

    return render(request, 'student_dashboard.html', context)

from django.http import JsonResponse

def hostel_details(request, hostel_id):
    # Fetch hostel details based on the hostel_id
    try:
        hostel = Hostels.objects.get(id=hostel_id)
        hostel_data = {
            'hostelname': hostel.hostelname,
            'gender': hostel.get_gender_display(),
            'hostelfees': hostel.hostelfees,
            'no_rooms': hostel.no_rooms,
            'room_cap': hostel.room_cap
            # Add more hostel details as needed
        }
        return JsonResponse({'hostel_details': hostel_data})
    except Hostels.DoesNotExist:
        return JsonResponse({'error': 'Hostel not found'}, status=404)
    
def hostel_details_page(request):
    hostels = Hostels.objects.all()
    return render(request, 'hostel_details_page.html', {'hostels': hostels})

def search_student(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id', '')
        # Fetch the student based on the provided student ID
        try:
            student = StudentApplication.objects.get(pk=student_id)
            return render(request, 'student_details.html', {'student': student})
        except StudentApplication.DoesNotExist:
            error_message = 'Student with ID {} does not exist.'.format(student_id)
            return render(request, 'warden_dashboard.html', {'error_message': error_message})
    return redirect('warden_dashboard')

@login_required
def raise_complaint(request):
    student_name = request.session.get('student_name')
    student_id = request.session.get('student_id')
    room_number = request.session.get('room_number')
    hostel_choice = request.session.get('hostel_choice')

    try:
        # Get the RoomAllotment object for the student
        room_allotment = RoomAllotment.objects.get(student_id=student_id)
        room_number = room_allotment.room_number
       
    except RoomAllotment.DoesNotExist:
        #room_number = None
        pass

    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            complaint = form.save(commit=False)
            complaint.student_name = student_name
            complaint.room_number = room_number
            complaint.hostel_choice= hostel_choice
            print(hostel_choice)
            complaint.save()
           

            return redirect('raise_complaint')  # Redirect to a success page

    else:
        initial_data = {
            'student_name': student_name,
            'room_number': room_number,
            'hostel_choice': hostel_choice
        }
        form = ComplaintForm(initial=initial_data)

    return render(request, 'raise_complaint.html', {'form': form})

@login_required
def pay_mess_bill(request):
    student_name = request.session.get('student_name')
    student_id = request.session.get('student_id')
   
    room_number = request.session.get('room_number')
    hostel_choice = request.session.get('hostel_choice')
    
    try:
        # Get the RoomAllotment object for the student
        room_allotment = RoomAllotment.objects.get(student_id=student_id)
        room_number = room_allotment.room_number
       
    except RoomAllotment.DoesNotExist:
        #room_number = None
        pass

    if request.method == 'POST':
        form = MessBillForm(request.POST)
        if form.is_valid():
            complaint = form.save(commit=False)
            complaint.student_name = student_name
            complaint.room_number = room_number
            complaint.hostel_choice= hostel_choice
            
            complaint.save()
            print(hostel_choice)

            return redirect('pay_mess_bill')  # Redirect to a success page

    else:
        initial_data = {
            'student_name': student_name,
            'room_number': room_number,
            'hostel_choice': hostel_choice
        }
        form = MessBillForm(initial=initial_data)
    return render(request, 'pay_mess_bill.html', {'form': form})
        

def apply_for_fund(request):
    if request.method == 'POST':
        form = StayFundApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'application_success.html')
    else:
        form = StayFundApplicationForm()
    return render(request, 'apply_fund.html', {'form': form})

def view_complaints(request, hostel_id):
    hostel = get_object_or_404(Hostels, pk=hostel_id)
    form = Complaint.objects.filter(hostel=hostel_id)


    return render(request, 'view_complaints.html', {'form': form})

def accept_complaint(request,stud_id):
  stud=Complaint.objects.get(id=stud_id)
 
  stud.complaint_status=1
  stud.save()
  form=Complaint.objects.all()
  return render(request,'view_complaints.html',{'form':form})


def view_allocations(request, hostel_id):
    hostel = get_object_or_404(Hostels, pk=hostel_id)
    room_allotments = RoomAllotment.objects.filter(hostel=hostel_id)
    student_details = []

    for room_allotment in room_allotments:
        student = {
            'name': room_allotment.student.full_name,
            'room_number': room_allotment.room_number,
            'phone_number': room_allotment.student.contact_number,
            'date_of_birth': room_allotment.student.date_of_birth,
            'student_id': room_allotment.student.id,
        }
        student_details.append(student)

    return render(request, 'view_allocations.html', {'student_details': student_details})


def edit_student(request, student_id):
    student = get_object_or_404(StudentApplication, id=student_id)
    room_allotment, created = RoomAllotment.objects.get_or_create(student=student)

    if request.method == 'POST':
        # Process form submission for editing student details
        form = RoomAllotmentForm(request.POST)
        if form.is_valid():
            room_allotment.room_number = form.cleaned_data['room_number']
            # Update other fields as needed
            room_allotment.save()
            return redirect('view_allocations', hostel_id=student.hostel_choice.id)
    else:
        form = RoomAllotmentForm(initial={'room_number': room_allotment.room_number})

    return render(request, 'edit_student.html', {'form': form})

def delete_student(request, student_id):
    student = get_object_or_404(StudentApplication, id=student_id)
    room_allotment, created = RoomAllotment.objects.get_or_create(student=student)
    room_allotment.delete()
    return redirect('edit_student',student_id=student_id)