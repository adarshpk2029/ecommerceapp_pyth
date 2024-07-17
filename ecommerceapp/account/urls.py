from django.urls import path,include
from account.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('login',LoginView.as_view(),name="login"),
    path('reg',RegView.as_view(),name="reg"),
    path("user/",include("user.urls")),
    path('',LandingView.as_view(),name="landing"),
    path('logout',LogoutView.as_view(),name="logout")

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)