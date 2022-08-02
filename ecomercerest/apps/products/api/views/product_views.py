from numpy import product
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from apps.base.general_api_view import GeneralListApiView
from apps.products.api.serializers.product_serializer import ProductSerializer

class ProductListApiView(GeneralListApiView):
    serializer_class = ProductSerializer

class ProductListCreateApiView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = ProductSerializer.Meta.model.objects.filter(state=True)
    def post(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Producto creado con exito' },status= status.HTTP_201_CREATED)
        return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)

class ProductRetrieveApiView(generics.RetrieveAPIView):
    serializer_class = ProductSerializer
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)
    #def get(self,request,pk=None )

class ProductDestroyApiView(generics.DestroyAPIView):
    serializer_class = ProductSerializer
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)
    def delete(self,request,pk=None):
        product = self.get_queryset().filter(id = pk).first()
        if product:
            product.state = False
            product.save()
            return Response({'message':'Producto eliminado correctamente'})
        return Response({'error':'No existe un producto con estos datos'})

class ProductUpdateApiView(generics.UpdateAPIView):
    serializer_class = ProductSerializer
    def get_queryset(self,pk):
        return self.get_serializer().Meta.model.objects.filter(state = True).filter(id=pk).first()

    def patch(self,request,pk=None):
        if self.get_queryset(pk):
            product_serialiazer = self.serializer_class(self.get_queryset(pk))
            return Response(product_serialiazer.data,status = status.HTTP_200_OK)
        return Response({'error':'No existe un producto con estos datos'})
    def put(self,request,pk=None):
        if self.get_queryset(pk):
            product_serializer = self.serializer_class(self.get_queryset(pk),data = request.data)
            if product_serializer.is_valid():
                product_serializer.save()
                return Response(product_serializer.data,status = status.HTTP_200_OK)
            return Response(product_serializer.errors,status = status.HTTP_400_BAD_REQUEST)