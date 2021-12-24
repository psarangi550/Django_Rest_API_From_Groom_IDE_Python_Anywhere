from django.shortcuts import render
from .models import WFMTTaskModel
from .serializers import WFMTTaskModelSerializer
from rest_framework.viewsets import ModelViewSet
from .paginations import WFMTPagination
# Create your views here.

class WFMTCRUDView(ModelViewSet):
    queryset = WFMTTaskModel.objects.all()
    serializer_class=WFMTTaskModelSerializer
    pagination_class=WFMTPagination
    