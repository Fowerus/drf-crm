from django.urls import path

from . import views


urlpatterns = [
    path('product-category-l/', views.ProductCategoryListAPIView.as_view(), name = 'product_category_l'),

    path('product-l/<int:organization>/', views.ProductListAPIView.as_view(), name = 'product_l'),
    path('product-r/<int:id>/<int:organization>/', views.ProductRetrieveAPIView.as_view(), name = 'product_r'),
    path('product-c/', views.ProductCreateAPIView.as_view(), name = 'product_c'),
    path('product-ud/<int:organization>/', views.ProductUpdateDestroyAPIView.as_view(), name = 'product_ud'),

    path('cashbox-l/<int:organization>/', views.CashboxListAPIView.as_view(), name = 'cashbox_l'),
    path('cashbox-r/<int:id>/<int:organization>/', views.CashboxRetrieveAPIView.as_view(), name = 'cashbox_r'),
    path('cashbox-c/', views.CashboxCreateAPIView.as_view(), name = 'cashbox_c'),
    path('cashbox-ud/<int:id>/<int:organization>/', views.CashboxUpdateDestroyAPIView.as_view(), name = 'cashbox_ud'),

    path('purchase-l/<int:organization>/', views.PurchaseListAPIView.as_view(), name = 'purchase_l'),
    path('purchase-r/<int:id>/<int:organization>/', views.PurchaseRetrieveAPIView.as_view(), name = 'purchase_r'),
    path('purchase-c/', views.PurchaseCreateAPIView.as_view(), name = 'purchase_c'),
    path('purchase-ud/<int:id>/<int:organization>/', views.PurchaseUpdateDestroyAPIView.as_view(), name = 'purchase_ud'),
]
