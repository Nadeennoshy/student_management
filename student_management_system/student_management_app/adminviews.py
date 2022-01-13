from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.urls import reverse
from django.http.response import HttpResponseRedirect
from student_management_app.models import CustomUser,Semesters,Courses,Staffs,Students,FeedBackStudent



def admin_home(request):
    return render(request,"student_management_app/admin/adminpage.html")

def add_staff(request):
    return render(request,"student_management_app/admin/add_staff.html")


def add_staff_save(request):
    if request.method != 'POST':
        return HttpResponse('Method Not Allowed')
    else:
        
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        address = request.POST.get("address")
        try:
            user = CustomUser.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type = 2)
            user.staffs.address = address
            user.save()
            messages.success(request,"Successfully Added Staff")
            return HttpResponseRedirect(reverse("add_staff"))
        except:
            messages.error(request,"Failed To Add Staff")
            return HttpResponseRedirect(reverse("add_staff"))

def add_semester(request):
    return render(request,"student_management_app/admin/add_semester.html")


def add_semester_save(request):
    if request.method != 'POST':
        return HttpResponseRedirect("Method Not Allowed")
    else:
        semester= request.POST.get("semester")
        try:
            semester_model = Semesters(semester_name = semester)
            semester_model.save()
            messages.success(request,"Successfully Added Semester")
            return HttpResponseRedirect(reverse("add_semester"))
        except:
            messages.error(request,"Failed To Add semester")
            return HttpResponseRedirect(reverse("add_semester"))

def add_student(request):
    semesters = Semesters.objects.all()
    return render(request,"student_management_app/admin/add_student.html",{"semesters":semesters})

def add_student_save(request):
    if request.method != 'POST':
        return HttpResponse('Method Not Allowed')
    else:
        
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        address = request.POST.get("address")
        session_start = request.POST.get("session_start")
        session_end = request.POST.get("session_end")
        semester_id = request.POST.get("semester")
        gender = request.POST.get("gender")
        profile_pic = request.FILES['profile_pic']
        fs = FileSystemStorage()
        filename = fs.save(profile_pic.name,profile_pic)
        profile_pic_url = fs.url(filename)
        try:
            user = CustomUser.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type = 3)
            user.students.address = address
            semester_obj = Semesters.objects.get(id=semester_id)
            user.students.semester_id = semester_obj
            user.students.session_start_year = session_start
            user.students.session_end_year = session_end
            user.students.gender = gender
            user.students.profile_pic = profile_pic_url
            user.save()
            messages.success(request,"Successfully Added Student")
            return HttpResponseRedirect(reverse("add_student"))
        except:
            messages.error(request,"Failed To Add Student")
            return HttpResponseRedirect(reverse("add_student"))

def add_course(request):
    semesters = Semesters.objects.all()
    staffs = CustomUser.objects.filter(user_type=2)
    return render(request,"student_management_app/admin/add_course.html",{"staffs":staffs,"semesters":semesters})

def add_course_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        course_name = request.POST.get("course_name")
        semester_id = request.POST.get("semester")
        semester = Semesters.objects.get(id=semester_id)
        staff_id = request.POST.get("staff")
        staff = CustomUser.objects.get(id=staff_id)
        try:
            course = Courses(course_name=course_name,semester_id=semester,staff_id=staff)
            course.save()
            messages.success(request,"Successfully Added Course")
            return HttpResponseRedirect(reverse("add_course"))
        except:
            messages.error(request,"Failed To Add Course")
            return HttpResponseRedirect(reverse("add_course"))

def manage_staff(request):
    staffs = Staffs.objects.all()
    return render(request,"student_management_app/admin/manage_staff.html",{"staffs":staffs})

def manage_student(request):
    students = Students.objects.all()
    return render (request,"student_management_app/admin/manage_student.html",{"students":students})

def manage_semester(request):
    semesters = Semesters.objects.all()
    return render (request,"student_management_app/admin/manage_semester.html",{"semesters":semesters}) 

def manage_course(request):
    courses = Courses.objects.all()
    return render (request,"student_management_app/admin/manage_course.html",{"courses":courses})

def edit_staff(request,staff_id):
    # return HttpResponse("Staff Id: "+ staff_id)
    staff = Staffs.objects.get(admin=staff_id)
    return render (request,"student_management_app/admin/edit_staff.html",{"staff":staff})

def edit_staff_save(request):
    if request.method != 'POST':
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        staff_id = request.POST.get("staff_id")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        username = request.POST.get("username")
        address = request.POST.get("address")
        try:
            user=CustomUser.objects.get(id=staff_id)
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.username = username
            user.save()

            staff_model = Staffs.objects.get(admin = staff_id)
            staff_model.address = address
            staff_model.save()
            messages.success(request,"Successfully Edited Staff")
            return HttpResponseRedirect(reverse("edit_staff",kwargs={"staff_id":staff_id}))
        except:
            messages.error(request,"Failed To Edit Staff")
            return HttpResponseRedirect(reverse("edit_staff",kwargs={"staff_id":staff_id}))

def edit_student(request,student_id):
    semesters = Semesters.objects.all()
    student = Students.objects.get(admin = student_id)
    return render(request,"student_management_app/admin/edit_student.html",{"student":student,"semesters":semesters})

def edit_student_save(request):
    if request.method != 'POST':
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        student_id = request.POST.get("student_id")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        address = request.POST.get("address")
        session_start = request.POST.get("session_start")
        session_end = request.POST.get("session_end")
        semester_id = request.POST.get("semester")
        gender = request.POST.get("gender")

        if request.FILES['profile_pic']:
            profile_pic = request.FILES['profile_pic']
            fs = FileSystemStorage()
            filename = fs.save(profile_pic.name,profile_pic)
            profile_pic_url = fs.url(filename)
        else:
            profile_pic_url = None
        try:
            user = CustomUser.objects.get(id = student_id)
            user.first_name = first_name
            user.last_name = last_name
            user.username = username
            user.email = email
            user.save()

            student = Students.objects.get(admin = student_id)
            student.address = address
            student.session_start_year = session_start
            student.session_end_year = session_end
            student.gender = gender
            semester = Semesters.objects.get(id=semester_id)
            student.semester_id = semester
            if profile_pic_url != None:
                student.profile_pic = profile_pic_url
            student.save()
            messages.success(request,"Successfully Edited Student")
            return HttpResponseRedirect(reverse("edit_student",kwargs={"student_id":student_id}))
        except:
            messages.error(request,"Failed To Edit Student")
            return HttpResponseRedirect(reverse("edit_student",kwargs={"student_id":student_id}))

def edit_course(request,course_id):
    course = Courses.objects.get(id = course_id)
    semesters = Semesters.objects.all()
    staffs = CustomUser.objects.filter(user_type = 2)
    return render(request,"student_management_app/admin/edit_course.html",{"course":course,"semesters":semesters,"staffs":staffs})


def edit_course_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        course_id = request.POST.get("course_id")
        course_name = request.POST.get("course_name")
        staff_id = request.POST.get("staff")
        semester_id = request.POST.get("semester")

        try:
            course = Courses.objects.get(id=course_id)
            course.course_name = course_name
            staff = CustomUser.objects.get(id=staff_id)
            course.staff_id = staff
            semester = Semesters.objects.get(id = semester_id)
            course.semester_id = semester
            course.save()
            messages.success(request,"Successfully Edited Course")
            return HttpResponseRedirect(reverse("edit_course",kwargs={"course_id":course_id}))
        except:
            messages.error(request,"Failed To Edit Course")
            return HttpResponseRedirect(reverse("edit_course",kwargs={"course_id":course_id}))

      

def edit_semester(request,semester_id):
    semester = Semesters.objects.get(id = semester_id)
    return render(request,"student_management_app/admin/edit_semester.html",{"semester":semester})

def edit_semester_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        semester_id = request.POST.get("semester_id")
        semester_name = request.POST.get("semester")

        try:
            semester = Semesters.objects.get(id=semester_id)
            semester.semeter_name = semester_name
            semester.save()
            messages.success(request,"Successfully Edited Semester")
            return HttpResponseRedirect(reverse("edit_semester",kwargs={"semester_id":semester_id}))
        except:
            messages.error(request,"Failed To Edit Semester")
            return HttpResponseRedirect(reverse("edit_semester",kwargs={"semester_id":semester_id}))
