from django.conf.urls import url
from jwt.app.user.views import UserRegistrationView
from jwt.app.user.views import UserLoginSerializer


urlpatterns = [
    url(r'^signup', UserRegistrationView.as_view()),
    url(r'^signin', UserLoginSerializer.as_view()),
    ]