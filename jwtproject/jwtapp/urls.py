from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns =[
    path("profile/", views.ProfileList.as_view()),
    path("profile/<int:pk>/", views.ProfileDetail.as_view()),
    path("users/", views.UserList.as_view()),
    path("users/<int:pk>", views.UserDetail.as_view()),
    path("hello/", views.HelloView.as_view(), name="hello"),
    path("protected/", views.ProtectedView.as_view(), name="protected")
]

# Also offer .<format> URLs
urlpatterns = format_suffix_patterns(urlpatterns)
