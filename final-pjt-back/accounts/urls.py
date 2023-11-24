from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('<username>/', views.get_user_info, name='get_user_info'),
]
