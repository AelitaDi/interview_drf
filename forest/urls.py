from django.urls import path

from forest.apps import ForestConfig
from forest.views import TreeListAPIView, TreeCreateAPIView

app_name = ForestConfig.name

urlpatterns = [
    path("trees/", TreeListAPIView, name="tree_list"),
    path("trees/create/", TreeCreateAPIView, name="tree_create"),
]
