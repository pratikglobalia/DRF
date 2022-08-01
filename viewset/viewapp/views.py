from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .serializers import MobileSerializer
from .models import Mobile


# Create your views here.

###############  model view set  ##################
# class MobileViewSet(viewsets.ModelViewSet):
#     queryset = Mobile.objects.all()    
#     serializer_class = MobileSerializer


###############  viewset  #################
class MobileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Mobile.objects.all()    
    serializer_class = MobileSerializer


###############  viewset  #################
# class MobileViewSet(viewsets.ViewSet):
#     def list(self, request):
#         mob = Mobile.objects.all()
#         serializer = MobileSerializer(mob, many=True)
#         return Response(serializer.data)
    
#     def create(self, request):
#         serializer = MobileSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Data Created'})
#         return Response(serializer.errors)
    
#     def retrieve(self, request, pk=None):
#         mob = Mobile.objects.get(id=pk)
#         serializer = MobileSerializer(mob)
#         return Response(serializer.data)
    
#     def update(self, request, pk=None):
#         mob = Mobile.objects.get(id=pk)
#         serializer = MobileSerializer(mob, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Updated Successfully'})
#         return Response(serializer.errors)
    
#     def partial_update(self, request, pk=None):
#         mob = Mobile.objects.get(id=pk)
#         serializer = MobileSerializer(mob, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Updated Successfully'})
#         return Response(serializer.errors)
    
#     def destroy(self, request, pk=None):
#         mob = Mobile.objects.get(id=pk)
#         mob.delete()
#         return Response({'msg':'Data Deleted'})