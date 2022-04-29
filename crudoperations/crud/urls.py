from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_edit, name="employee_add"),
    path('<int:id>/', views.employee_edit, name="employee_update"),
    path('list/', views.employee_list, name="employee_list"),
    path('delete/<int:id>', views.employee_delete, name="employee_delete"),

    path('student/', views.studentDetails, name="studentList"),
    path('CreateStudent/', views.CreateStudent, name="CreateStudent"),
    path('CreateStudent/<int:id>/', views.CreateStudent, name="updateStudent"),
    path('crops/', views.createCrops, name="createCrops"),
    path('crops/<int:id>/', views.createCrops, name="updateCrops"),

]
