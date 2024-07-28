from django.urls import path
from . import views

urlpatterns = [
    path('create-brand/', views.create_brand, name='create_brand'),
    path('create-mobile/', views.create_mobile, name='create_mobile'),
    path('brands/', views.brand_list, name='brand_list'),
    path('', views.mobile_list, name='mobile_list'),
    path('korean-brands/', views.korean_brands, name='korean_brands'),
    path('mobiles-by-brand/', views.mobiles_by_brand, name='mobiles_by_brand'),
    path('matching-nationality-mobiles/', views.matching_nationality_mobiles, name='matching_nationality_mobiles'),
]