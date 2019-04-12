from django.urls import path
from . import views

urlpatterns=[
    path('login',views.backendLogin,name='login'),
    path('logout',views.backendLoginout,name="logout"),
    path('',views.homeView,name="dashboard"),
    path('category',views.category,name="category"),
    path('sub-category',views.subcategory,name='subcategory'),
    path('product-type',views.productType,name="producttype"),
    path('brand',views.brand,name="brand"),
    path('product-material',views.productMaterial,name="material"),
    path('product-specification',views.productSpecification,name="specification"),
    path('product-size',views.productSize,name="size"),
    path('product-template',views.productTemplate,name="template"),
    path('product-add',views.productAdd,name="productadd"),
    path('stock-report',views.stockReport,name="stockreport"),
    path('general-setting',views.generalSetting,name="general-settings")
  
]