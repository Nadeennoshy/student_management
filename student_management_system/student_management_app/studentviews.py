from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
from student_management_app.models import Students,FeedBackStudent,LeaveReportStudent

def student_home(request):
    return render(request,"student_management_app/student/studentpage.html")

def courses_grades(request):
    return render(request,"student_management_app/student/courses_grades.html")

def identity_cards(request):
    return render(request,"student_management_app/student/identity_cards.html")

def university_mail(request):
   return render(request,"student_management_app/student/university_mail.html")

def examstable(request):
   return render(request,"student_management_app/student/examstable.html")

def academic_registration(request):
   return render(request,"student_management_app/student/academic_registration.html")

def semestetone_or_two(request):
   return render(request,"student_management_app/student/semesterone_or_two.html")


def choose_courses(request):
   return render(request,"student_management_app/student/choose_courses.html")

def student_account(request):
   return render(request,"student_management_app/student/student_account.html")




def student_time_table(request):
   return render(request,"student_management_app/student/student_time_table.html")





# def student_apply_leave(request):
#     staff_obj = Students.objects.get(admin= request.user.id)
#     leave_date = LeaveReportStudent.objects.filter(student_id=staff_obj)
#     return render(request,"student_management_app/student/student_apply_leave.html",{"leave_date":leave_date})

# def student_apply_leave_save(request):
#     if request.method != "POST":
#         return HttpResponseRedirect(reverse("student_apply_leave"))
#     else:
#         leave_date = request.POST.get("leave_date")
#         leave_msg = request.POST.get("leave_msg")

#         student_obj = Students.objects.get(admin= request.user.id)
#         try:
#             leave_report = LeaveReportStudent(student_id=student_obj,leave_date=leave_date,leave_message=leave_msg,leave_status=0)
#             leave_report.save()
#             messages.success(request,"Successfully Applied For Leave")
#             return HttpResponseRedirect(reverse("student_apply_leave"))
#         except:
#             messages.error(request,"Failed To Apply For Leave")
#             return HttpResponseRedirect(reverse("student_apply_leave"))


# def student_feedback(request):
#     staff_id = Students.objects.get(admin=request.user.id)
#     feedback_data = FeedBackStudent.objects.filter(student_id=staff_id)
#     return render(request,"student_management_app/student/student_feedback.html",{"feedback_data":feedback_data})

# def student_feedback_save(request):
#     if request.method != "POST":
#         return HttpResponseRedirect(reverse("student_feedback"))
#     else:
#         feedback_msg = request.POST.get("feedback_msg")

#         student_obj = Students.objects.get(admin= request.user.id)
#         try:
#             feedback = FeedBackStudent(student_id=student_obj,feedback=feedback_msg,feedback_reply="")
#             feedback.save()
#             messages.success(request,"Successfully Sent Feedback")
#             return HttpResponseRedirect(reverse("student_feedback"))
#         except:
#             messages.error(request,"Failed To Send Feedback")
#             return HttpResponseRedirect(reverse("student_feedback"))