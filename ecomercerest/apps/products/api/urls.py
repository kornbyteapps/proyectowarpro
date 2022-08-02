from django.urls import URLPattern, path, include
from apps.products.api.views.general_views import MeasureUnitListApiView,IndicatorListApiView,CategoryProductListApiView
from apps.products.api.views.product_views import ProductListApiView,ProductListCreateApiView,ProductRetrieveApiView,ProductDestroyApiView,ProductUpdateApiView
urlpatterns =[
    path('measure_unit/',MeasureUnitListApiView.as_view(),name='measure_unit'),
    path('indicator/',IndicatorListApiView.as_view(),name='indicator'),
    path('category_products/',CategoryProductListApiView.as_view(),name='category_products'),
    path('products/list/',ProductListApiView.as_view(),name='products_list'),
    path('products/',ProductListCreateApiView.as_view(),name='products_create'),
    path('products/retrieve/<int:pk>',ProductRetrieveApiView.as_view(),name='product_retrieve'),
    path('products/destroy/<int:pk>',ProductDestroyApiView.as_view(),name='product_destroy'),
    path('products/update/<int:pk>',ProductUpdateApiView.as_view(),name='product_update'),



]