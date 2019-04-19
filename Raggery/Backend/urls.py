from django.urls import path
from . import views

urlpatterns=[
    path('login',views.backendLogin,name='login'),
    path('logout',views.backendLoginout,name="logout"),
    path('',views.homeView,name="dashboard"),

    #start categry url
    path('category',views.category,name="category"),
    path('category_delete/<int:pk>',views.category_delete,name="category_delete"),
    path('category_pdf',views.category_pdf,name="category_pdf"),
    path('category_download',views.category_download,name="category_download"),
    path('category_update/<int:pk>',views.category_update,name="category_update"),
    path('category_status/<int:pk>',views.category_status,name="category_status"),
    #end category url

     #start categry url
    path('sub-category',views.subcategory,name='subcategory'),
    path('subcategory_status/<int:pk>',views.subcategory_status,name='subcategory_status'),
    path('subcategory_delete/<int:pk>',views.subcategory_delete,name="subcategory_delete"),
    path('subcatgory_update/<int:pk>',views.subcategory_update,name="subcategory_update"),


    #end subcategory url
    #start product type url
    path('product-type',views.productType,name="producttype"),
    path('product_status/<int:pk>',views.product_status,name="product_status"),
    path('product_delete/<int:pk>',views.product_delete,name="product_delete"),
    path('product_update/<int:pk>',views.product_update,name="product_update"),
    #end product type url
    path('brand',views.brand,name="brand"),
    # start product material url
    path('product-material',views.productMaterial,name="material"),
    path('sucategory_data',views.getSubcategory,name='get_subcategory'),
    path('get_producttype',views.getProducttype,name='get_producttype'),
    path('product_metarial_delete/<int:pk>',views.productMetarialDelete,name='product_metarial_delete'),
    path('product_metarial_update/<int:pk>',views.productMetarialUpdate,name="product_metarial_update"),
    # end product material url
    path('product-specification',views.productSpecification,name="specification"),
    path('product-size',views.productSize,name="size"),
    path('product-template',views.productTemplate,name="template"),
    path('product-add',views.productAdd,name="productadd"),
    path('stock-report',views.stockReport,name="stockreport"),
    path('general-setting',views.generalSetting,name="general-settings")
  
]