from rest_framework.generics import ListAPIView, CreateAPIView

from rest_framework.permissions import IsAuthenticated

from forest.models import Tree
from forest.serializers import TreeSerializer, AdminTreeSerializer, TreeCreateSerializer
from users.permissions import IsStaffUser


class TreeListAPIView(ListAPIView):
    """Tree list."""
    permission_classes = [IsAuthenticated,]

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


class TreeCreateAPIView(CreateAPIView):
    """Tree create."""
    queryset = Tree.objects.all()
    serializer_class = TreeCreateSerializer
    permission_classes = [IsAuthenticated,]

    def perform_create(self, serializer):
        # print('fffffffffffffffffffffffffffff')
        # print(self.request.user)
        tree = serializer.save()
        tree.owner = self.request.user
        tree.save()
