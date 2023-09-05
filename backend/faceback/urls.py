from django.urls import path

from .views import(
    User_List_api,
    User_Detail_api
)


urlpatterns = [
    path("users/", User_List_api.as_view()),
    path("users/<int:account>/", User_Detail_api.as_view()),
]


