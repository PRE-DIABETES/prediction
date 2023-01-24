from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',index,name='index'),
    path("login/", login_request, name="login"),
    # path('signin',signin,name='signin'),
    path('registration',registration,name='registration'),
    path('inner',inner,name="inner"),
    path('result',result,name="result"),
    path('predict',predict,name="predict"),
    path('Viewpred',Viewpred,name="Viewpred"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('signup',signup,name="signup"),
    path('view',view,name="view"),

     
  
    
]