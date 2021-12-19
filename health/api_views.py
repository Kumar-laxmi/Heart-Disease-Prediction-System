from rest_framework import viewsets
from . import models
from . import serializers

class PatientViewset(viewsets.ModelViewSet):
    queryset = models.Patient.objects.all()
    serializer_class = serializers.PatientSerializer
    lookup_field = 'user'
    lookup_url_kwarg = 'user'
    filterset_fields = ('id','user' )
    extra_kwargs = {'url': {'lookup_field':'user'}}