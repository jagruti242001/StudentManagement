from django.db import models

# Create your models here.

class StudentModel(models.Model):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=10)
    dob = models.DateField()
    address = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    student_image = models.ImageField(upload_to='Student_Image/' , blank=True)
    course = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=6)
    hobbies = models.CharField(max_length=100)
    blood_group = models.CharField(max_length=100)
    known_language = models.CharField(max_length=100)
    education = models.CharField(max_length=100)
    why_you_want = models.CharField(max_length=100)




class StaffModel(models.Model):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=25)
    staff_image = models.ImageField(upload_to='Staff_Image/' , blank=True)
    dob = models.DateField()
    present_address = models.CharField(max_length=100)
    permenant_address = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    education = models.CharField(max_length=100)
    project_done = models.CharField(max_length=100)
    work_experience = models.CharField(max_length=100)
    salary_expectations = models.IntegerField()
    material_status = models.CharField(max_length=100)


class FeedbackModel2(models.Model):
    name = models.CharField(max_length=100)
    feedback = models.CharField(max_length=200)


class LeaveModel(models.Model):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=10)
    course = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    reason = models.CharField(max_length=100)

