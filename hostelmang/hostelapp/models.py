
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.core.exceptions import ValidationError
import uuid

STATUS_CHOICES = [
        (0, 'Pending'),
        (1, 'Approved'),
        (2, 'Rejected'),
    ]


class Hostels(models.Model):
     hostelname = models.CharField('hostelname', max_length=20,unique=True)
     gender_type = [('Male','Male'),('Female','Female')]
     gender=models.CharField(default=1,choices=gender_type,max_length=10)
     level_type= [('PG','PG'),('Phd','Phd')]
     level= models.CharField(default=1,choices=level_type, max_length=30)
     course_type= [('MSc/MCA','MSc/MCA'),('MA/Mcom/MPEd','MA/Mcom/MPEd')]
     course= models.CharField(default=1,choices=course_type, max_length=30)
     no_rooms= models.IntegerField('no_rooms', default=0)
     room_cap= models.IntegerField(default=0)
     mess= models.BooleanField(default=False)
     hostelfees=models.PositiveIntegerField(default=0)

     def __str__(self):
        return self.hostelname
     
class add_dep(models.Model):
    dep_name = models.CharField(max_length=100)
    dep_contact = models.CharField(max_length=15)
    dep_email = models.EmailField()     

    def __str__(self):
        return self.dep_name

class gender_type(models.Model):
    gender=models.CharField(max_length=10, choices=Hostels.gender_type)
    def __str__(self):
        return self.gender
    
class course_type(models.Model):
    course=models.CharField(max_length=30, choices=Hostels.course_type)
    def __str__(self):
        return self.course



class StudentApplication(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        # Add other genders if needed
    ]

    COURSE_CHOICES = [
        ('MSc/MCA', 'MSc/MCA '),
        ('MA', 'MA'),
        # Add other courses as needed
    ]

    STATUS_CHOICES = [
        (0, 'Pending'),
        (1, 'Approved'),
        (2, 'Rejected'),
    ]

    FEE_STATUS_CHOICES = [
        (0, 'Not Paid'),
        (1, 'Paid'),
    ]

    full_name = models.CharField(max_length=100, verbose_name="Full Name")
    date_of_birth = models.DateField(verbose_name="Date of Birth")
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, verbose_name="Gender")
    nationality = models.CharField(max_length=50, verbose_name="Nationality")
    contact_number = models.CharField(max_length=15, verbose_name="Contact Number")
    email_address = models.EmailField(verbose_name="Email Address")
    cast = models.CharField(max_length=10, verbose_name="Cast")
    cast_no = models.CharField(max_length=15, verbose_name="Cast No")
    permanent_address = models.TextField(verbose_name="Permanent Address")
    current_address = models.TextField(blank=True, null=True, verbose_name="Current Address")
    guardian_full_name = models.CharField(max_length=100, verbose_name="Guardian Full Name")
    guardian_relationship = models.CharField(max_length=50, verbose_name="Guardian Relationship")
    guardian_contact_number = models.CharField(max_length=15, verbose_name="Guardian Contact Number")
    previous_university = models.CharField(max_length=100, verbose_name="Previous University")
    previous_college = models.CharField(max_length=100, verbose_name="Previous College")
    register_number = models.CharField(max_length=20, verbose_name="Register Number")
    previous_course = models.CharField(max_length=100, verbose_name="Previous Course")
    total_marks = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Total Marks")
    obt_marks = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Obtained Marks")
    percentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name="Percentage")
    year_of_study = models.PositiveIntegerField(verbose_name="Year of Study")
    course = models.CharField(max_length=100, choices=COURSE_CHOICES, verbose_name="Course")
    department = models.ForeignKey(add_dep, on_delete=models.CASCADE, verbose_name="Department")
    year = models.PositiveIntegerField(verbose_name="Year")
    date = models.DateField(verbose_name="Date")
    hostel_choice = models.ForeignKey(Hostels, on_delete=models.CASCADE)
    medical_conditions = models.TextField(verbose_name="Medical Conditions")
    allergies = models.TextField(verbose_name="Allergies")
    id_copy = models.FileField(upload_to='id_copy/', verbose_name="ID Copy")
    passport_photo = models.ImageField(upload_to='passport_photos/', verbose_name="Passport Photo")
    marks_card = models.FileField(upload_to='marks_card/', verbose_name="Marks Card")
    undertaking_form = models.FileField(upload_to='undertaking_forms/', verbose_name="Undertaking Form")
    status = models.IntegerField(choices=STATUS_CHOICES, default=0, verbose_name="Status")
    fee_status = models.IntegerField(choices=FEE_STATUS_CHOICES, default=0, verbose_name="Fee Status")
    room_allotted = models.BooleanField(default=False, verbose_name="Room Allotted")

    def __str__(self):
        return self.full_name

    def id_copy_upload_path(self, filename):
        return f'id_copy/{self.full_name}/{filename}'
    
    def get_warden_for_application(self):
        try:
            return warden.objects.get(hostel_id=self.hostel_choice)
        except warden.DoesNotExist:
            return None


    

    



class warden(models.Model):
    warden_name = models.CharField(max_length=100)
   
    
    contact = models.CharField(max_length=15)
    hostel_id = models.ForeignKey(Hostels, on_delete=models.CASCADE)
    
    password=models.CharField(max_length=15)
    def get_students_in_hostel(self):
        # Retrieve students in the same hostel as the warden
        return StudentApplication.objects.filter(hostel_choice=self.hostel_id)
     

class RoomAllotment(models.Model):
    student = models.ForeignKey(StudentApplication, on_delete=models.CASCADE)
    
    hostel = models.ForeignKey(Hostels,on_delete=models.CASCADE)
    room_number = models.IntegerField()
    
    def get_student_contact_number(self):
        return self.student.contact_number

       





class PaymentDetail(models.Model):
    student_application = models.ForeignKey(StudentApplication, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=16)
    expiry_date = models.CharField(max_length=5)  # MM/YY format
    cvv = models.CharField(max_length=4)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Payment for {self.student_application.student.full_name} on {self.timestamp}'
    
class Complaint(models.Model):
    student_name = models.CharField(max_length=100)
    room_number = models.IntegerField()
    complaint_text = models.TextField()
    hostel=models.CharField(max_length=20)
    complaint_status = models.IntegerField(choices=STATUS_CHOICES, default=0, verbose_name="Status")
   
    def __str__(self):
        return f"Complaint from {self.student_name} (Room {self.room_number})"


class MessBill(models.Model):
    student_name = models.CharField(max_length=100)
    room_number =models.IntegerField()
    mess_bill_image = models.ImageField(upload_to='mess_bills/', null=True, blank=True)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f'Mess Bill for {self.student.full_name}'


class PaymentDetailStudents(models.Model):
    student = models.ForeignKey(StudentApplication, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    challen_number = models.CharField(max_length=20)
    challen_image = models.ImageField(upload_to='challen_images/')

    def __str__(self):
        return f'Payment for {self.student.full_name}'