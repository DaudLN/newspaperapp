from django.urls import path

from .views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    # path('password_change/', PasswordChange.as_view(), name='password_change')
]
