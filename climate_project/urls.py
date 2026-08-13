
from django.contrib import admin
from django.urls import path
from Dashboard.views import index,details,climate,forcast

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('home/',index),
    path('details/',details),
    path('climate/',climate),
    path('forcast/',forcast),
]
