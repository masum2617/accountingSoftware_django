from rest_framework import generics
from .serializers import AssetSerializer
from inventory.models import Asset

class AssetListView(generics.ListCreateAPIView):
    serializer_class = AssetSerializer

    def get_queryset(self):
        return Asset.objects.all()

class AssetDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer
