from rest_framework import viewsets
from rest_framework import filters

from .serializers import ShipmentSerializer
from .models import Shipment


class ShipmentListApi(viewsets.ModelViewSet):
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = [
        'driver__name',           # افترض أن نموذج Driver يحتوي على حقل 'name'
        'customer_branch__name',  # افترض أن نموذج Branch يحتوي على حقل 'name'
        'destination__name_ar',   # افترض أن نموذج City يحتوي على حقل 'name_ar'
    ]
