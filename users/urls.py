from django.urls.conf import path

from users.apps import UsersConfig
from users.views import ProfileUpdateAPIView, LoginAPIView, UserCreateAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login'),
    path('profile/update/', ProfileUpdateAPIView.as_view(), name='profile_update'),
    # path('profile/update/', ProfileUpdateAPIView.as_view(), name='profile_update'),
    path("register/", UserCreateAPIView.as_view(), name="register"),
]
