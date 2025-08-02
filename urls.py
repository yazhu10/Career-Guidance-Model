from django.urls import path
from . import views

urlpatterns = [
	path('', views.register,name="register"),
	path('login/', views.student_login,name="student_login"),
	path('dashboard/', views.dashboard,name="dashboard"),
	path('logout/', views.logout,name="logout"),
	path('admin_home/', views.admin_home,name="admin_home"),
	path('engineering_search/', views.engineering_search,name="engineering_search"),
	
]
