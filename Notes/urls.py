"""Notes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app1.views import (index,Logout,about,contact,userlogin,adminlogin,
                        admindashboard,registerPage,userdetail,
                        changepassword,Profile,Uploadnotes,
                        viewnotes,delete,viewuser,pending,status,viewallnotes
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",index, name="home"),
    path("contact",contact, name="contact"),
    path("about",about, name="about"),
    path("login",userlogin, name="login"),
    path("adminlogin",adminlogin, name="adminlogin"),
    path("admindashboard",admindashboard, name="admindashboard"),
    path("logout",Logout, name="logout"),
    path("register",registerPage, name="register"),
    path("datail",userdetail, name="detail"),
    path("changepassword",changepassword, name="changepassword"),
    path("profile",Profile, name="profile"),
    path("notes",Uploadnotes, name="notes"),
    path("viewnotes",viewnotes, name="viewnotes"),
    path('delete/<str:pk>',delete,name = 'delete'),
    path('viewuser',viewuser,name = 'viewuser'),
    path("pending/<slug:data>",pending, name="pending"),
    path("status/<str:pk>/<slug:data>",status, name="status"),
    path("viewallnotes",viewallnotes, name="viewallnotes")

]
urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
