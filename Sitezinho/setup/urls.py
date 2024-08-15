from django.contrib import admin
from django.urls import path

from App_site import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home.as_view(), name='home'),
    path('Cadastrar-se/',views.RegisterView.as_view(),name='Cadastro')
]
