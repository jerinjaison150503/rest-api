from django.urls import path
from . import views

urlpatterns=[
    # path('',views.fun0),
    path('<pk>',views.fun1),
]