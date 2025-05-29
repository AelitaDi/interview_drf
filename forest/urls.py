from django.urls import path

from forest.apps import ForestConfig
from forest.views import TreeListAPIView, TreeCreateAPIView

app_name = ForestConfig.name

urlpatterns = [
    path("trees/", TreeListAPIView.as_view(), name="tree_list"),
    path("trees/create/", TreeCreateAPIView.as_view(), name="tree_create"),
]
