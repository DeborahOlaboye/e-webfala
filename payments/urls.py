from django.urls import path
<<<<<<< HEAD
from .views import create_checkout_session, payments, success, cancel

urlpatterns = [
    path('', payments, name='payments'),
    path('create-checkout-session/<int:course_id>/', create_checkout_session, name='create_checkout_session'),
    path('success/', success, name='success'),
    path('cancel/', cancel, name="cancel")
=======
from . import views  

urlpatterns = [
    path('', views.payments, name='payments'),
>>>>>>> 841eeeea387a928f1446e8cbf39a8bf08abe4b11
]