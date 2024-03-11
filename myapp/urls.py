from django.urls import path
from .views import MyModelList, MyModelDetail, UserRegistrationView

urlpatterns = [
    path('mymodel/', MyModelList.as_view(), name='mymodel-list'),
    path('mymodel/<int:pk>/', MyModelDetail.as_view(), name='mymodel-detail'),
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
]