# from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework.generics import ListAPIView, CreateAPIView

from django.views.decorators.csrf import csrf_exempt
from forest.models import Tree
from forest.serializers import TreeSerializer, AdminTreeSerializer, TreeCreateSerializer
from users.permissions import IsStaffUser


@csrf_exempt
class TreeListAPIView(LoginRequiredMixin, ListAPIView):
    """Tree list."""
    def get_queryset(self):
        """Checks user permissions for queryset."""
        if IsStaffUser().has_permission(self.request, self):
            return Tree.objects.all()
        else:
            return Tree.objects.filter(owner=self.request.user)

    def get_serializer_class(self):
        """Checks user permissions for serializer class."""
        if IsStaffUser().has_permission(self.request, self):
            return AdminTreeSerializer
        else:
            return TreeSerializer


@csrf_exempt
class TreeCreateAPIView(LoginRequiredMixin, CreateAPIView):
    """Tree create."""
    queryset = Tree.objects.all()
    serializer_class = TreeCreateSerializer

    def perform_create(self, serializer):
        tree = serializer.save()
        tree.owner = self.request.user
        tree.save()
