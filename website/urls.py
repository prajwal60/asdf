from django.urls import path
from .views import *

app_name = 'website'

urlpatterns = [
    path('',index, name='index'),
    path('aboutus/',aboutus, name='aboutus'),
    path('services/',services, name='services'),
    path('software/',software, name='software'),
    path('school/',school, name='school'),
    path('mobile/',mobile, name='mobile'),
    path('webapp/',webapp, name='webapp'),
    path('domain/',domain, name='domain'),
    path('bulkSms/',bulkSms, name='bulkSms'),
    path('graphic/',graphic, name='graphic'),
    path('video/',video, name='video'),
    path('terms/',terms, name='terms'),
]
