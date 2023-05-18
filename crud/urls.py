from django.urls import path, include
from .views import ProductsListAPI
from .views import ProductsDetailAPI
from .views import ProductsCreateAPI
from .views import ProductsUpdateAPI
from .views import ProductsDeleteAPI
#from .views import ApisView


urlpatterns = [
               #path('apis/$', ApisView.as_view(), name='apis'),             
               path('productlist/', ProductsListAPI.as_view()),
               path('product/create/', ProductsCreateAPI.as_view()),
               path('product/detail/(<pk>[0-9]+)/', ProductsDetailAPI.as_view()),
               path('product/update/(<pk>[0-9]+)/', ProductsUpdateAPI.as_view()),
               path('product/delete/(<pk>[0-9]+)/', ProductsDeleteAPI.as_view()),
               ]