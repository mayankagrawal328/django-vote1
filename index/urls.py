from django.urls import path
from . import views
urlpatterns=[
    path('',views.Home,name="Home"),
    path('otp',views.otp,name="otp"),
    path('vote',views.vote,name="vote"),
    path('thanks',views.thanks,name="thanks"),
    path('result',views.result,name="result"),
    path('send123',views.send123,name="send123"),
        path('pp',views.pp,name="pp"),
    

    ]

