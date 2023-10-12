from django.urls import path

from .views import(
    User_List_api,
    Login_api,
    Register_api,
)


urlpatterns = [
    path('userlist/', User_List_api.as_view(),name='userlist'),
    path('login/', Login_api.as_view(),name='login'),
    path('register/', Register_api.as_view(),name='register'),
]


