from django.urls import path
from amar2.views import *
app_name='nothing'
urlpatterns=[
    path('lucky/',lucky,name='lucky'),
    path('ram/',ram,name='ram'),
]