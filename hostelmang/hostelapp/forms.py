from django import forms
from .models import *

class StudentApplicationForm(forms.ModelForm):
    class Meta:
        model = StudentApplication
        fields = '__all__'  # Include all fields from the model
        exclude = ['status', 'fee_status', 'room_allotted','cast','cast_no','current_address',
                   'guardian_full_name','guardian_relationship','guardian_contact_number','date','medical_conditions','allergies']
    
    
    widgets = {
        'date_of_birth': forms.DateInput(attrs={'type': 'date'})
    }



class hostelform(forms.ModelForm):
    class Meta:
        model=Hostels
        fields='__all__'

class genderform(forms.ModelForm):
    class Meta:
        model=gender_type
        fields='__all__'

class courseform(forms.ModelForm):
    class Meta:
        model=course_type
        fields='__all__'
        


class viewhostelform(forms.Form):
    hostel=forms.ModelChoiceField(queryset=Hostels.objects.all(),empty_label='view a hostel')


class depform(forms.ModelForm):
    class Meta:
        model=add_dep
        fields='__all__'    



class view_depform(forms.Form):
    dep=forms.ModelChoiceField(queryset=add_dep.objects.all(),empty_label='view a department')


class wardenform(forms.ModelForm):
    class Meta:
        model=warden
        fields='__all__'    

class view_wardenform(forms.Form):
    warden=forms.ModelChoiceField(queryset=warden.objects.all(),empty_label='view a warden')



class StatusCheckForm(forms.Form):
    mobile_number = forms.CharField(max_length=15, required=True, label='Mobile Number')
    date_of_birth = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}), required=True, label='Date of Birth')

class RoomAllotmentForm(forms.Form):
    student_id = forms.IntegerField()
    room_number = forms.IntegerField(min_value=1, max_value=100)

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['complaint_text','hostel'] 

class ComplaintStatusUpdateForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['complaint_status']
        


class MessBillForm(forms.ModelForm):
    class Meta:
        model = MessBill
        fields =['mess_bill_image']
        exclude=['is_paid']
        

class StayFundApplicationForm(forms.Form):
    student_name=forms.CharField()
    gender=forms.CharField()
    hostel_name=forms.CharField()


