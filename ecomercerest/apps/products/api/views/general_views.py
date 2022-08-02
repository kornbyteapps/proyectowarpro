from apps.base.general_api_view import GeneralListApiView
from apps.products.models import MeasureUnit,Indicator,CategoryProduct
from apps.products.api.serializers.general_serializer import MeasureUnitSerializer,IndicatorSerializer,CategoryProductSerializer

class MeasureUnitListApiView(GeneralListApiView):
    serializer_class = MeasureUnitSerializer
    

class IndicatorListApiView(GeneralListApiView):
    serializer_class = IndicatorSerializer
    

class CategoryProductListApiView(GeneralListApiView):
    serializer_class = CategoryProductSerializer