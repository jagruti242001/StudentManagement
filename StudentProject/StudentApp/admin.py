from django.contrib import admin
from . models import StudentModel , StaffModel , FeedbackModel2 , LeaveModel
# Register your models here.

@admin.register(StudentModel)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id","f_name", "l_name",'username','password',"email", "contact",'dob','address', "gender",'student_image','course','department',"city", "state",'pincode','hobbies','blood_group', "known_language","education", "why_you_want"]

    
@admin.register(StaffModel)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['id','f_name','l_name','username','password','staff_image','dob','present_address','permenant_address','contact','education','project_done','work_experience','salary_expectations','material_status']


@admin.register(FeedbackModel2)
class Feedback2Admin(admin.ModelAdmin):
    list_display = ['id',"name", "feedback"]

@admin.register(LeaveModel)
class LeaveAdmin(admin.ModelAdmin):
    list_display = ['id' , 'f_name', 'l_name', 'email', 'contact', 'course' , 'department', 'reason']