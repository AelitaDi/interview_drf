from django.urls.conf import path

from users.apps import UsersConfig
from users.views import LoginAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login'),
]
