from django.urls import path,include
from student_management_app.views import ShowLoginPage,doLogin,GetUserDetails,logout_user
from student_management_app.adminviews import admin_home,add_staff,add_staff_save,add_semester,add_semester_save,add_student,add_student_save,add_course,add_course_save,manage_staff,manage_student,manage_semester,manage_course
from student_management_app.adminviews import edit_staff,edit_staff_save,edit_student,edit_student_save,edit_course_save,edit_course,edit_semester,edit_semester_save
from student_management_app.studentviews import student_home,courses_grades,identity_cards,university_mail,student_time_table,examstable,academic_registration,semestetone_or_two,choose_courses,student_account


urlpatterns = [
    path('',ShowLoginPage,name="show_login"),
    path('doLogin',doLogin,name="do_login"),
    path('get_user_details',GetUserDetails),
    path('logout_user',logout_user,name="logout"),
    path('adminhome/',admin_home,name="admin_home"),
    path('add_staff',add_staff, name="add_staff"),
    path('add_staff_save',add_staff_save,name="add_staff_save"),
    path('add_semester',add_semester,name="add_semester"),
    path('add_semester_save',add_semester_save,name="add_semester_save"),
    path('add_student',add_student,name="add_student"),
    path('add_student_save',add_student_save,name="add_student_save"),
    path('add_course',add_course,name="add_course"),
    path('add_course_save',add_course_save,name="add_course_save"),
    path('manage_staff',manage_staff,name="manage_staff"),
    path('manage_student',manage_student,name="manage_student"),
    path('manage_semester',manage_semester,name="manage_semester"),
    path('manage_course',manage_course,name="manage_course"),
    path('edit_staff/<str:staff_id>',edit_staff,name="edit_staff"),
    path('edit_staff_save',edit_staff_save,name="edit_staff_save"),
    path('edit_student/<str:student_id>',edit_student,name="edit_student"),
    path('edit_student_save',edit_student_save,name="edit_student_save"),
    path('edit_course/<str:course_id>',edit_course,name="edit_course"),
    path('edit_course_save',edit_course_save,name="edit_course_save"),
    path('edit_semester/<str:semester_id>',edit_semester,name="edit_semester"),
    path('edit_semester_save',edit_semester_save,name="edit_semester_save"),
    path('student_home',student_home,name="student_home"),
    path('courses_grades',courses_grades,name="courses_grades"),
    path("identity_cards",identity_cards,name="identity_cards"),
    path("university_mail",university_mail,name="university_mail"),
    path("student_time_table",student_time_table,name="student_time_table"),
    path("examstable",examstable,name="examstable"),
    path("academic_registration",academic_registration,name="academic_registration"),
    path("semestetone_or_two",semestetone_or_two,name="semestetone_or_two"),
    path("choose_courses",choose_courses,name="choose_courses"),
    path("student_account",student_account,name="student_account"),
]