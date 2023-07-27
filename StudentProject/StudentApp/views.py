from django.shortcuts import render, redirect
from . forms import LoginForm , RegisterForm , StaffRegisterForm , StudentLoginForm , StaffloginForm
from django.contrib.auth import authenticate , login , logout
from django.views import View
from . models import StudentModel , StaffModel, FeedbackModel2 , LeaveModel
from django.contrib import messages
# Create your views here.


def home_view(request):
    return render(request , 'StudentApp/home.html')

def adminlogin_view(request):
    forms = LoginForm()
    context = {'forms': forms}
    return render(request , 'StudentApp/adminlogin.html' , context)


def register_view(request):
    forms = RegisterForm()
    context = {'forms': forms}
    return render(request, 'StudentApp/register.html',context)

class staffregistration(View):
    def get(self,request):
        forms = StaffRegisterForm()
        context = {'forms':forms}
        return render (request,"StudentApp/staffRegistration.html",context)

    def post(self,request):
        forms = StaffRegisterForm(request.POST,request.FILES)
        if forms.is_valid():
            forms.save()
            messages.success(request , 'Successfully StaffRegister')
            return redirect('staffregistration')
            
        return redirect('home')


def staff_view(request , id):
    data = StaffModel.objects.get(id=id)
    context = {'data':data}
    return render(request , 'StudentApp/staff.html' , context)


def signin_view(request):
    if request.method == "POST":
        username1 = request.POST['username']
        pass1 = request.POST['password']

        user = authenticate(username = username1 , password = pass1)
        if user is not None:
            login(request,user)
            messages.success(request , 'Successfully admin login')
            return redirect('studentDetails')

    return redirect('home')



def studentDetails_view(request):
    data=StudentModel.objects.all()
    context={'data':data}
    return render(request , 'StudentApp/studentDetails.html',context)

def students_view(request , id):
    data = StudentModel.objects.get(id=id)
    context = {'data':data}
    return render(request , 'StudentApp/students.html',context)



def signout_view(request):
    logout(request)
    messages.info   (request , 'Successfully user logout')
    return redirect('home')


def fees_view(request):
    return render(request, 'StudentApp/fees.html')



def feedback_view(request):
    feedback=FeedbackModel2.objects.all()
    context={'feedback':feedback}
    return render(request , 'StudentApp/feedback.html', context)

def leave(request):
    leave=LeaveModel.objects.all()
    context={'leave':leave}
    return render(request , 'StudentApp/leave.html',context)

def deletestudent(request , id):
    leave = LeaveModel.objects.get(pk = id)
    leave.delete()

    return redirect('leave')


def contactus_view(request):
    return render(request, "StudentApp/contactus.html")

def aboutus(request):
    return render(request , 'StudentApp/aboutus.html')


#Student Section

class registration(View):
    def get(self,request):
        forms = RegisterForm()
        context = {'forms':forms}
        return render (request,"StudentApp/registration.html",context)

    def post(self,request):
        forms = RegisterForm(request.POST,request.FILES)
        if forms.is_valid():
            forms.save()
            messages.success(request , 'Student Successfully Register')
            return redirect('registration')

            
        return redirect('home')

def studentHome_view(request):
    data=StudentModel.objects.all()
    context={'data':data}
    if request.method == "POST":
        email = request.POST['email']
        pass1 = request.POST['password']
        print("email is", email)
        print("password is", pass1)

        model = StudentModel.objects.get(email = email)
        print(model)
        if model.email == email and model.password == pass1:
            messages.success(request , 'Student login ...')
            return render(request , 'StudentApp/StudentHome.html',context)

        else:
            messages.warning(request , 'Please enter valid email id or password ...')
            return redirect('studentlogin')



    # if request.method == "POST":
    #     email = request.POST['email']
    #     pass1 = request.POST['password']

    #     user = StudentModel.objects.get(email = email , password = pass1)
    #     if user is not None:
    #         login(request,user)
    #         messages.success(request , 'Successfully student login')
    #         return redirect('studentDetails')
        




    return render(request , 'StudentApp/StudentHome.html',context)

def studentprofile(request ,id ):
    data = StudentModel.objects.filter(id=id)
    context = {'data':data}
    
    return render(request , 'StudentApp/studentprofile.html', context)


def studentfeedback(request):
    data=StudentModel.objects.all()
    context={'data':data}

    if request.method =='POST':
        name = request.POST["name"]
        feedback = request.POST['feedback']
        
        data = FeedbackModel2(name = name,feedback = feedback)
        messages.success(request , 'Student Feedback Successfully Register')
        data.save()

        return redirect('studentHome')
    return render(request , 'StudentApp/studentfeedback.html',context)

def studentleave(request):
    data=StudentModel.objects.all()
    context={'data':data}

    if request.method =='POST':
        f_name = request.POST["f_name"]
        l_name = request.POST['l_name']
        email = request.POST['email']
        contact = request.POST['contact']
        course = request.POST['course']
        department = request.POST['department']
        reason = request.POST['reason']
        
        data = LeaveModel(f_name = f_name , l_name = l_name , email = email , contact = contact , course = course , department = department, reason = reason)

        data.save()

        return redirect('studentHome')
    return render(request , 'StudentApp/studentleave.html',context )



def update_view(request, id):
    data = StudentModel.objects.get(id = id)
    print("1.data is ", data)
    context = {'data':data}
    

    if request.method == "POST":
        updated_email = request.POST["email"]
        updated_contact = request.POST["contact"]
        updated_address = request.POST["address"]
        updated_course = request.POST["course"]
        updated_department = request.POST["department"]
        updated_city = request.POST["city"]
        updated_education = request.POST["education"]
        

        
        data.email = updated_email
        data.contact = updated_contact
        data.address = updated_address
        data.course = updated_course
        data.department = updated_department
        data.city = updated_city
        data.education = updated_education
        messages.success(request , 'Student Successfully Updated')
        data.save()
        
        return redirect("home")

    return render(request , 'StudentApp/updatestudent.html', context)


def studentlogin(request):
    forms = StudentLoginForm()
    context = {'forms': forms}
    
    return render(request , 'StudentApp/studentlogin.html', context)



# def studentsignin(request):
#     form = StudentLoginForm()
            
#     if request.method == "POST":
#         username = request.POST['username']
#         pass1 = request.POST['password']
#         print("username is", username)
#         print("password is", pass1)

        # user = authenticate(username = username , password = pass1)
        # print(user)
        # if user is not None:
        #     login(request,user)
        #     # messages.success(request , 'Successfully user login')
        #     return redirect('studentDetails')

    # context = {'form':form}
    # return redirect('home')



#Staff section

def staffDetails_view(request):
    data=StaffModel.objects.all()
    context={'data':data}
    return render(request , 'StudentApp/staffDetails.html' , context)


def staff_signin_view(request):

    # forms = StaffRegisterForm()
    # if request.method == "POST":
    #     username1 = request.POST['username']
    #     pass1 = request.POST['password']

    #     user = authenticate(username = username1 , password = pass1)
    #     if user is not None:
    #         login(request,user)
    #         # messages.success(request , 'Successfully staff login')
    #         return redirect('staffDetails')

    #     return redirect('home')
    # context = {"forms":forms}
    return render(request , 'StudentApp/registration.html')


def staffhome_view(request):
    data=StaffModel.objects.all()
    context={'data':data}

    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['password']
        print("username is", username)
        print("password is", pass1)

        staff = StaffModel.objects.get(username = username)
        print(staff)
        if staff.username == username and staff.password == pass1:
            messages.success(request , 'Staff login ...')
            return render(request , 'StudentApp/staffhome.html',context)

        else:
            messages.warning(request , 'Please enter valid username id or password ...')
            return redirect('stafflogin')
    

def staffupdate_view(request ,id):
    
    data = StaffModel.objects.get(id = id)
    print("1.data is ", data)
    context = {'data':data}
    

    if request.method == "POST":
    
        updated_contact = request.POST["contact"]
        updated_present_address = request.POST["present_address"]
        updated_project_done = request.POST["project_done"]
        updated_education = request.POST["education"]
        

        data.contact = updated_contact
        data.present_address = updated_present_address
        data.project_done = updated_project_done
        data.education = updated_education
        messages.success(request , 'Successfully Staff Updated')
        data.save()
        
        return redirect("home")

    return render(request , 'StudentApp/staffupdate.html' , context)

def stafflogin(request):
    forms = StaffloginForm()
    context = {'forms': forms}
    return render(request , 'StudentApp/stafflogin.html', context)

def staffprofile(request , id):
    data = StaffModel.objects.get(id=id)
    context = {'data':data}
    return render(request , 'StudentApp/staffprofile.html',context)