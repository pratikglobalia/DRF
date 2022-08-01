from .models import Mobile
from .serializers import MobileSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.
class LCMobileApiView(ListCreateAPIView):
    queryset = Mobile.objects.all()
    serializer_class = MobileSerializer

class RUDMobileApiView(RetrieveUpdateDestroyAPIView):
    queryset = Mobile.objects.all()
    serializer_class = MobileSerializer