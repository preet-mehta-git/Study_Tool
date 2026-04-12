"""
URL configuration for student project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from tool import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.register,name='register'),
    path('home/',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('profile/',views.profile,name='profile'),
    path('analysis/',views.analysis,name='analysis'),
    path('chat/', views.chat, name='chat'),
    path('chat/like/<int:comment_id>/', views.like_comment, name='like_comment'),
    path('quiz/',views.quiz,name='quiz'),
    path('schedule/', views.schedule, name='schedule'),
    path('faq/',views.faq,name='faq'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('tos/',views.tos,name='tos'),
    path('contact_us/',views.contact_us,name='contact_us'),
]
