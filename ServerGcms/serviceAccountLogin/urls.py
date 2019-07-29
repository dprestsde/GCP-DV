from django.urls import path
from .views import CreateServiceAccount,UserServiceAccount
urlpatterns = [
    path('addservice/', CreateServiceAccount.as_view()),
    path('userservice/', UserServiceAccount.as_view()),
   

]
