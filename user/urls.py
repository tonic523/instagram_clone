from django.urls import path, include

from user.views import SignupView
urlpatterns = [
    path('/signup', SignupView.as_view())
]