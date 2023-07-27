from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django import forms
from . models import StudentModel ,StaffModel


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Enter Admin Username' , widget=forms.TextInput(attrs={'class':'form-control'}))

    password = forms.CharField(label='Enter Admin Password' , widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User


class StudentLoginForm(AuthenticationForm):
    username = forms.CharField(label='Enter Student Username' , widget=forms.TextInput(attrs={'class':'form-control'}))

    password = forms.CharField(label='Enter Student Password' , widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = StudentModel



gender_choice = [("Male","Male"),("Female","Female"),("Other","Other")]
city_choice = [("Thane","Thane"),("Kalyan","Kalyan"),("Andheri","Andheri")]
state_choice = [("Maharashtra","Maharashtra"),("bengluru","bengluru"),('Gujrat','Gujrat')]
Language_choice = [("English","English"),("Hindi","Hindi"),("Marathi","Marathi")]
education_choice = [("HSC","HSC"),("FY","FY"),('SY','SY'),('TY','TY')]
course_choice = [('BA','BA'),('BCOM','BCOM'),('BSC','BSC')]
department_choice = [('BA','BA'),('BCOM','BCOM'),('BMS','BMS'),('Chemistry','Chemistry'),('IT','IT'),('CS','CS')]
hobbies_choice = [('Reading','Reading'),('Writing','Writing'),('Singing','Singing'),('Dancing','Dancing'),('Other','Other')]

class RegisterForm(forms.ModelForm):

    gender = forms.ChoiceField(choices = gender_choice, label= "Gender",widget=forms.RadioSelect)

    city = forms.ChoiceField(choices= city_choice, label = "Select City", widget= forms.Select(attrs= {"class":"form-control"}))

    state = forms.ChoiceField(choices= state_choice, label = "Select state", widget= forms.Select(attrs= {"class":"form-control"}))

    known_language = forms.MultipleChoiceField(choices= Language_choice, label = "Select language", widget= forms.CheckboxSelectMultiple)

    education = forms.ChoiceField(choices = education_choice, label= "Education",widget=forms.RadioSelect)

    course = forms.ChoiceField(choices=course_choice , label ='Select your course',widget=forms.RadioSelect )

    department = forms.ChoiceField(choices= department_choice , label='Select your department',widget=forms.RadioSelect)

    hobbies = forms.MultipleChoiceField(choices=hobbies_choice , label= 'Select your hobbies' , widget=forms.CheckboxSelectMultiple)

    password = forms.CharField(label='Enter Password' , widget=forms.PasswordInput(attrs={'class':'form-control'}))

    


    class Meta:
        model = StudentModel
        fields = ["f_name", "l_name",'username','password', "email", "contact",'dob','address', "gender",'student_image','course','department',"city", "state",'pincode','hobbies','blood_group', "known_language","education", "why_you_want"]

        labels = {
            "f_name": "Enter First name",
            "l_name": "Enter Last name",
            'username': 'Enter Username',
            'password' : 'Enter Password',
            "email": "Enter email",
            "contact": "Enter contact number",
            'dob':'Enter DOB',
            'address':'Enter your address',
            'gender':'Select your Gender',
            'student_image':'Upload your profile photo',
            'city':'Select your city',
            'state':'Select your state',
            'pincode':'Enter your Pincode',
            'why_you_want' : 'Why You Want to become a student of our college'
        }

        widgets = {
            "f_name":forms.TextInput(attrs={"class":"form-control"}),
            "l_name":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "contact":forms.TextInput(attrs={"class":"form-control"}),
            'dob' : forms.TextInput(attrs={'class':'form-control'}),
            'address': forms.TextInput(attrs={'class':'form-control'}),
            'student_image' : forms.FileInput(attrs={'class':'form-control'}),
            'pincode':forms.TextInput(attrs={'class':'form-control'}),
            'why_you_want':forms.Textarea(attrs={'class':'form-control'})

        }



class StaffloginForm(AuthenticationForm):
    
    
    class Meta:
        model = StaffModel



class StaffRegisterForm(forms.ModelForm):
    username = forms.CharField(label='Enter Staff Username' , widget=forms.TextInput(attrs={'class':'form-control'}))

    password = forms.CharField(label='Enter Staff Password' , widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = StaffModel

        fields = ['id','f_name','l_name','username','password','staff_image','dob','present_address','permenant_address','contact','education','project_done','work_experience','salary_expectations','material_status']

        labels = {
            "f_name": "Enter First name",
            "l_name": "Enter Last name",
            'username': 'Enter Staff Username',
            'password' : 'Enter Password',
            'staff_image' : 'Upload your profile image',
            'dob' : 'Enter DOB',
            'present_address': 'Enter Present Address',
            'permenant_address' : 'Enter Permenant address',
            'contact':'Enter your contact number',
            'education':'Enter your education',
            'project_done': 'Mention Project done',
            'work_experience': 'Enter your work experience',
            'salary_expectations':'Enter salary expectations',
            'material_status':'Your material status',
        }

        widgets = {
            "f_name":forms.TextInput(attrs={"class":"form-control"}),
            "l_name":forms.TextInput(attrs={"class":"form-control"}),
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "password":forms.TextInput(attrs={"class":"form-control"}),
            "dob":forms.TextInput(attrs={"class":"form-control"}),
            "present_address":forms.TextInput(attrs={"class":"form-control"}),
            "permenant_address":forms.TextInput(attrs={"class":"form-control"}),
            "contact":forms.TextInput(attrs={"class":"form-control"}),
            "education":forms.TextInput(attrs={"class":"form-control"}),
            "project_done":forms.TextInput(attrs={"class":"form-control"}),
            "work_experience":forms.TextInput(attrs={"class":"form-control"}),
            "salary_expectations":forms.TextInput(attrs={"class":"form-control"}),
            "material_status":forms.TextInput(attrs={"class":"form-control"}),

        }

class FeedbackForm2(forms.ModelForm):
    class Meta:
        fields = ["id", "name", "feedback"]


class LeaveForm(forms.ModelForm):
    class Meta:
        fields = ['id' , 'f_name', 'l_name', 'email', 'contact', 'course' , 'department', 'reason']