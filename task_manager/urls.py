
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from projects.views import dashboard, add_task, delete_task

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard, name='home'),
    path('add/', add_task, name='add_task'),
    path('delete/<int:id>/', delete_task, name='delete_task'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html')),
    path('logout/', auth_views.LogoutView.as_view()),
]
